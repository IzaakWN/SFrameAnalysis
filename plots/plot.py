#! /usr/bin/env python

from argparse import ArgumentParser
import os, sys, time
from math import sqrt, pow, floor, ceil
import ROOT
from ROOT import TFile, TH1D, gDirectory, kAzure, kGreen, kRed
import PlotTools.PlotTools, PlotTools.SampleTools
from PlotTools.PlotTools   import Plot, Plot2D, combineCuts
from PlotTools.PrintTools  import color, warning, error, printSameLine, header
from PlotTools.SampleTools import Samples, Sample, makeSamples, renormalizeWJ, renormalizeTT, getSample, getData, removeLowMassDY
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# HTT Working TWiki: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016
# gErrorIgnoreLevel = kInfo;



argv = sys.argv
description = '''This script make plots.'''
parser = ArgumentParser(prog="plotter",description=description,epilog="Succes!")
parser.add_argument( "-s", "--category", dest="category", type=int, default=-1, action='store',
                     metavar="CATEGORY", help="run only for this category of selection and cuts" )
parser.add_argument( "-c", "--channel", dest="channel", default="", action='store',
                     metavar="CHANNEL", help="run only for this channel" )
parser.add_argument( "-e", "--etau", dest="etau", default=False, action='store_true',
                     help="run only for the etau channel" )
parser.add_argument( "-m", "--mutau", dest="mutau", default=False, action='store_true',
                     help="run only for the mutau channel" )
parser.add_argument( "-l", "--list", dest="list", default=False, action='store_true',
                     help="list all available categories" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="make script verbose" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()


# LABELS & LUMI
mylabel     = "_Moriond" # extra label for opening file, saving plots to dir
plotlabel   = "" # extra label for image file #_noWJrenormalization
lumi        = 35.9
if "ICHEP" in mylabel: lumi = 12.9 #24.5


# BLIND REGION
#S_exp       = { "mutau":1.35, "etau":0.45, "emu":0.93 } # expected number of signal events per category
S_exp       = { "baseline":   { "mutau":1.35, "etau":0.45, "emu":0.93 },
                "category 1": { "mutau":0.76, "etau":0.25, "emu":0.52 }, # expected number of signal events per category
                "category 2": { "mutau":0.62, "etau":0.21, "emu":0.40 },}

blindlimits = { "m_vis":      (  12,  36),
                "m_sv" :      (  20,  36),
                "dR_ll" :     (   0, 1.2),
                #"pt_tt":     (  80, 200),
                #"pt_tt_sv":  (  80, 200),
                "R_pt_m_vis": ( 2.5,  10),
                "R_pt_m_sv":  ( 2.0,  10), }
blindlimits_norm= { "m_sv" :  (  20,  36), } # to normalize 28 GeV


# PLOTS OPTIONS
verbosity           = 1
verbosityWJ         = 0
verbosityTT         = 0
verbosityPlots      = 0
doStack             = True #and False
doSigma             = True and False
checkYield          = True and False
doPlot2D            = True and False
doComparison        = True and False
doCheckCutflow      = True and False
doDataCard          = True and False # DATACARD
doLTF               = True and False
doTES               = True and False
doEES               = True and False
doJES               = True and False
doZpt               = True #and False
doTTpt              = True #and False
doQCD_WJ            = True #and False
useCutTree          = True #and False
recreate            = True #and False # recreate datacard
normalizeWJ         = (doStack or doDataCard) #and False
normalizeTT         = (doStack or doDataCard) #and False
normalizeSignal     = True #and False
stitchDY10to50      = True #and False
stitchDY50          = True #and False
doQCD               = True #and False
doSignalUpScaling   = True #and False
drawData            = True #and False
drawSignal          = True #and False
if not drawSignal:  plotlabel+="_noSignal"
if not doQCD:       plotlabel+="_noQCD"
if not normalizeWJ: plotlabel+="_noWJrenormalization"
if not normalizeTT: plotlabel+="_noTTrenormalization"
channels  = [
#                 "mutau",
#                 "etau",
                "emu",
             ]


blindcuts   = { "m_vis":      "( m_vis < %i || %i < m_vis )"           % blindlimits["m_vis"],
                "m_sv" :      "( m_sv  < %i || %i < m_sv  )"           % blindlimits["m_sv" ],
                "dR_ll":      "%i < dR_ll"                             % blindlimits["dR_ll"][1],
                #"pt_tt"   :   "( pt_tt < %i || %i < pt_tt )"     % blindlimits["pt_tt"   ],
                #"pt_tt_sv":   "( pt_tt_sv < %i || %i < pt_tt_sv )"     % blindlimits["pt_tt_sv"],
                "R_pt_m_vis": "( R_pt_m_vis < %i || %i < R_pt_m_vis )" % blindlimits["R_pt_m_vis"],
                "R_pt_m_sv" : "( R_pt_m_sv  < %i || %i < R_pt_m_sv  )" % blindlimits["R_pt_m_sv" ], }


# CATEGORIES / SELECTIONS
weight_      = "weight"
if "emu" in channels: weight_ += "*trigweight_1_or" # emu #*(getQCDWeight(pt_2, pt_1, dR_ll))"
else:                 weight_ += "*trigweight_or_1" # cross trigger
isocuts      = "iso_cuts==1"
vetos        = "lepton_vetos==0"
vetos0       = "dilepton_veto==0 && extraelec_veto==0 && extramuon_veto==0 "
vetos_mutau  = vetos0 + "&& againstElectronVLooseMVA6_2==1 && againstMuonTight3_2==1"
vetos_etau   = vetos0 + "&& againstElectronTightMVA6_2==1 && againstMuonLoose3_2==1"
vetos_emu    = "extraelec_veto==0 && extramuon_veto==0"
baseline_emu = "%s && iso_1<0.2 && iso_2<0.15 && q_1*q_2<0" % (vetos_emu)
ptcut        = "(pt_1>26||(channel==1 && pt_1>23))"
triggers     = "abs(eta_1)<2.1 && (( %s && (triggers==1||triggers==3))||(triggers>1))" % ptcut #pt_1>20 &&
baseline     = "%s && %s && q_1*q_2<0 && %s" % (isocuts,vetos,triggers)
if "emu" in channels: baseline = baseline_emu # emu
category1    = "ncbtag > 0 && ncjets == 1 && nfjets  > 0"
category2    = "ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2 && met<60"
category2J   = "ncbtag > 0 && ncjets == 2 && nfjets == 0"
# category1TT  = "ncbtag > 1 && ncjets  > 0 && nfjets  > 0 && met>60"
# category2TT  = "ncbtag > 0 && ncjets  > 1 && nfjets == 0 && met>60"
category1TT0 = "ncbtag > 1 && ncjets == 2 && nfjets  > 0"
category1TT1 = "ncbtag > 1 && ncjets  > 1 && nfjets  > 0"
category1TT  = "ncbtag > 0 && ncjets == 1 && nfjets  > 0 && met>60 && pfmt_1>60"
category2TT  = "ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2 && met>60 && pfmt_1>60"
(metcut,mt1cut) = ("met<60","pfmt_1<60")
if "emu" in channels: (metcut,mt1cut) = ("met<40","pfmt_1<40")
newcuts      = "%s && %s" % (metcut,mt1cut)
signalwindow = "%s < m_sv && m_sv < %s" % blindlimits_norm["m_sv"]
categories   = [
#                 ("no cuts",             ""),
#                 ("isolation",           "%s" % (isocuts)),
#                 ("lepton vetos",        "%s" % (vetos)),
#                 ("iso, lepton vetos",   "%s && %s" % (isocuts, vetos)),
#                 ("baseline, same sign", "%s" % (baseline.replace("q_1*q_2<0","q_1*q_2>0"))),
                ("baseline",            "%s" % (baseline)),
#                 ("baseline WJ CR",      "%s && %s" % (baseline,"pfmt_1>70")),
                ("category 1",          "%s && %s" % (baseline, category1)),
                ("category 2",          "%s && %s" % (baseline, category2)),
#                 ("category 1, relaxed iso", "%s && %s" % (baseline.replace(isocuts,"iso_1<=0.50 && iso_2==1"),category1)),
#                 ("category 2, relaxed iso", "%s && %s" % (baseline.replace(isocuts,"iso_1<=0.50 && iso_2==1"),category2)),
#                 ("category 1, relaxed iso medium", "%s && %s" % (baseline.replace(isocuts,"iso_1<=0.50 && iso_2_medium==1"),category1)),
#                 ("category 2, relaxed iso medium", "%s && %s" % (baseline.replace(isocuts,"iso_1<=0.50 && iso_2_medium==1"),category2)),
#                 ("category 1 TT CR0",   "%s && %s" % (baseline, category1TT0)),
#                 ("category 1 TT CR1",   "%s && %s" % (baseline, category1TT1)),
#                 ("category 2 jet cuts only", "%s && %s" % (baseline, category2J)),
#                 ("category 1 TT CR",    "%s && %s" % (baseline, category1TT)),
#                 ("category 2 TT CR",    "%s && %s" % (baseline, category2TT)),
#                 ("category 1 met",      "%s && %s && %s" % (baseline, category1, metcut)),
#                 ("category 2 met, no dphi", "%s && %s && %s" % (baseline, category2J, metcut)),
                ##("category 1 mt1",      "%s && %s && %s" % (baseline, category1, mt1cut)),
                ##("category 2 mt1",      "%s && %s && %s" % (baseline, category2, mt1cut)),
#                 ("category 1 SR",       "%s && %s && %s" % (baseline, category1, signalwindow)),
#                 ("category 2 SR",       "%s && %s && %s" % (baseline, category2, signalwindow)), # && met < 60
#                 ("category 1 SR met",   "%s && %s && %s && %s" % (baseline, category1, metcut, signalwindow)),
                ##("category 1 SR mt1",   "%s && %s && %s && %s" % (baseline, category1, mt1cut, signalwindow)),
                ##("category 2 SR mt1",   "%s && %s && %s && %s" % (baseline, category2, mt1cut, signalwindow)),
                ("category 1.2",        "%s && %s && %s" % (baseline, category1, newcuts)),
                ("category 2.2",        "%s && %s && %s" % (baseline, category2, newcuts)),
#                 ("category 2.2 no dphi", "%s && %s && %s" % (baseline, category2J, newcuts)), # no dphi
              ]


# VARIABLES
variables = [
                ##( "m_vis",         35, 0,  70 ),
                ##( "m_sv",          35, 0,  70 ),
#                 ( "m_vis",         35, 0, 140 ),
#                 ( "m_sv",          35, 0, 140 ),
#                 ( "pt_tt",         50, 0, 160 ),
#                 ( "pt_tt_sv",      30, 0, 160 ),
                ( "dR_ll",         30, 0,   6 ), 
#                 ##( "R_pt_m_vis",    50, 0,   7 ),
#                 ( "R_pt_m_sv",     50, 0,   5 ),
#                 ##( "pfmt_1",        45, 0, 200 ),
#                 ( "pfmt_1",        30, 0, 150 ),
#                 ( "pfmt_1",       200, 80, 200 ), # tail
#                 ( "pfmt_1",        40, 0, 200 ),
#                 ( "met",           40, 0, 200 ),
#                 ( "dphi_ll_bj",    30, 0, 4.5 ),
#                 ( "gen_match_2",    8, 0,   8 ),
                  ##( "nbtag",          5, 0,   5 ),
#                 ( "ncbtag",         5, 0,   5 ),
#                 ( "njets",          6, 0,   6 ),
#                 ( "nfjets",         5, 0,   5 ),
#                 ( "ncjets",         5, 0,   5 ),
#                 ( "pol_2",         25, -1.1, 1.1 ),
#                 ##( "mt_1",          40, 0, 200 ),
#                 ##( "NUP",            6, 0,   6 ),
#                 ( "npu",           21, 0,  42 ),
#                 ( "npv",           21, 0,  42 ),
#                 ( "puppimet",      30, 0, 120 ),
#                 ( "mvamet",        30, 0, 120 ),
#                 ( "iso_1",         10, 0, 0.2 ),
#                 ( "decayMode_2",      11, 0, 11 ),
#                 ( "byIsolationMVA3oldDMwLTraw_2", 10, 0.4, 1 ),
            ]
# for p in [ ("",1), ("",2), ("j",1), ("b",1), ("j",2), ("b",2) ]:
#     variables.append(( "%spt_%i" % p,       30,    0, 150   ))
#     #variables.append(( "abs(%seta_%i)" % p, 25,    0,   5   ))
#     variables.append(( "%seta_%i" % p,      31, -3.1,   3.1 ))
# for n in [ "iso_2", "againstElectronVLooseMVA6_2", "againstMuonTight3_2" ]:
#     variables.append(( n,             2, 0,   2 ))


# SAMPLES
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_and_data_samples
SFRAME = "SFrameAnalysis_Moriond"
SAMPLE_DIR = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput/")
if "emu" in channels: SAMPLE_DIR = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM/") # emu
PLOTS_DIR  = os.path.expandvars("/shome/ineuteli/analysis/%s/plots/"%SFRAME)
DATACARDS_DIR = PLOTS_DIR + "datacards"

samplesB = [
        ("TT/", "TT_TuneCUETP8M1",                      "ttbar",                    831.76  ), 
        ###("DY/", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell-Yan 10-50",        18610.0   ),
        ("DY/", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell-Yan 10-50",        18610.0   ), # 18610 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FDYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("DY/", "DY1JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 1J 10-50",       421.5   ), # 421.5 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FDY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("DY/", "DY2JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 2J 10-50",       184.3   ), # 184.3 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FDY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("DY/", "DY3JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 3J 10-50",        95.0   ), # ???
        ("DY/", "DYJetsToLL_M-50_TuneCUETP8M1",         "Drell-Yan 50",            4954.0   ), # LO 4954.0; NLO 5765.4
        ("DY/", "DY1JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 1J 50",         1012.5   ),
        ("DY/", "DY2JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 2J 50",          332.8   ),
        ("DY/", "DY3JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 3J 50",          101.8   ),
        ("DY/", "DY4JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 4J 50",           54.8   ),
        ("WJ/", "WJetsToLNu_TuneCUETP8M1",              "W + jets",               50380.0   ), # LO 50380.0; NLO 61526.7
        ("WJ/", "W1JetsToLNu_TuneCUETP8M1",             "W + 1J",                  9644.5   ),
        ("WJ/", "W2JetsToLNu_TuneCUETP8M1",             "W + 2J",                  3144.5   ),
        ("WJ/", "W3JetsToLNu_TuneCUETP8M1",             "W + 3J",                   954.8   ),
        ("WJ/", "W4JetsToLNu_TuneCUETP8M1",             "W + 4J",                   485.6   ),
        ("WW/", "WWTo1L1Nu2Q_13TeV_nlo",                "WWTo1L1Nu2Q",               49.997 ),
        ("WZ/", "WZTo3LNu_TuneCUETP8M1_13TeV_nlo",      "WZTo3LNu",                   3.05  ),
        ("WZ/", "WZTo1L1Nu2Q_13TeV_nlo",                "WZTo1L1Nu2Q",               10.71  ),
        ("WZ/", "WZTo2L2Q_13TeV_nlo",                   "WZTo2L2Q",                   5.595 ),
        ("WZ/", "WZJToLLLNu_nlo",                       "WZJToLLLNu",                 4.708 ),
        ("ZZ/", "VVTo2L2Nu_13TeV_nlo",                  "VVTo2L2Nu",                 11.95  ),
        ("ZZ/", "ZZTo2L2Q_13TeV_nlo",                   "ZZTo2L2Q",                   3.22  ),
        ("ZZ/", "ZZTo4L_13TeV_nlo",                     "ZZTo4L",                     1.212 ),
        ###("WW/", "WW_TuneCUETP8M1",                      "WW",                        63.21  ), # 63.21  https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWW_TuneCUETP8M1_13TeV-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ###("WZ/", "WZ_TuneCUETP8M1",                      "WZ",                        22.82  ), # 10.71? https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWZ_TuneCUETP8M1_13TeV-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ###("ZZ/", "ZZ_TuneCUETP8M1",                      "ZZ",                        10.32  ), #  3.22? https://cmsweb.cern.ch/das/request?input=dataset%3D%2FZZ_TuneCUETP8M1_13TeV-pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("ST/", "ST_tW_top_5f_inclusiveDecays",         "ST tW",                     35.60  ), #  38.09 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("ST/", "ST_tW_antitop_5f_inclusiveDecays",     "ST atW",                    35.60  ), #  38.09 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("ST/", "ST_t-channel_top_4f_inclusiveDecays",     "ST t",                  136.02  ), #  80.95 TWiki # 80.95 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ("ST/", "ST_t-channel_antitop_4f_inclusiveDecays", "ST at",                  80.95  ), # 136.02 TWiki # 136.02 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal 
        ###("WW/", "WWTo1L1Nu2Q",                          "WW",                        1.212  ), # 1.212 TWiki # 45.85 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ###("WW/", "WWTo4Q_4f",                            "WW",                        45.31  ), # 45.31 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FWWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ###("ST/", "ST_tW_top_5f_NoFullyHadronicDecays",      'ST',                     38.09  ), # 
        ###("ST/", "ST_tW_antitop_5f_NoFullyHadronicDecays",  'ST',                      0.00  ), # 
        ###("ST/", "ST_s-channel_4f_leptonDecays",            'ST',                     10.11  ), # 10.11 https://cmsweb.cern.ch/das/request?input=dataset%3D%2FST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM&instance=prod%2Fglobal
        ###("ST/", "ST_t-channel_antitop_4f_inclusiveDecays", 'ST',                     80.95  ), # 80.95 https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=dataset%3D%2FST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1%2FRunIISummer15GS-MCRUN2_71_V1-v1%2FGEN-SIM
        ###("ST/", "ST_t-channel_top_4f_inclusiveDecays",     'ST',                      0.00  ), # 
            ]

samplesB_comp = [
        ("TT/", "TT_TuneCUETP8M1",                      "ttbar ttpt",               831.76,     "weight"        ),
        ("TT/", "TT_TuneCUETP8M1_noTTpt",               "ttbar no ttpt",            831.76,     "weight"        ),
                 ]

(samplesB_EES0p99,  samplesB_EES1p01)   = ([ ],[ ])
(samplesB_JES0p97,  samplesB_JES1p03)   = ([ ],[ ])
(samplesB_TES0p97,  samplesB_TES1p03)   = ([ ],[ ])
(samplesB_LTF0p97,  samplesB_LTF1p03)   = ([ ],[ ])
(samplesB_ZptUp,    samplesB_ZptDown)   = ([ ],[ ])
(samplesB_TTptUp,   samplesB_TTptDown)  = ([ ],[ ])
(samplesB_QCD_WJUp, samplesB_QCD_WJDown, samplesB_noQCD_WJ) = ([ ],[ ],[ ])
for s in samplesB:
    samplesB_EES0p99.append((s[0],s[1]+"_EES0p99",s[2]+" -1% EES",s[3]))
    samplesB_EES1p01.append((s[0],s[1]+"_EES1p01",s[2]+" +1% EES",s[3]))
    samplesB_JES0p97.append((s[0],s[1]+"_JES0p97",s[2]+" -3% JES",s[3]))
    samplesB_JES1p03.append((s[0],s[1]+"_JES1p03",s[2]+" +3% JES",s[3]))
    if s[0] in ["DY/","TT/"]:
        samplesB_TES0p97.append((s[0],s[1]+"_TES0p97",s[2]+" -3% TES",s[3]))
        samplesB_TES1p03.append((s[0],s[1]+"_TES1p03",s[2]+" +3% TES",s[3]))
    if s[0] in ["DY/"]:
        samplesB_LTF0p97.append(( s[0],s[1]+"_LTF0p97", s[2]+" -3% LTF",s[3]))
        samplesB_LTF1p03.append(( s[0],s[1]+"_LTF1p03", s[2]+" +3% LTF",s[3]))
        samplesB_ZptDown.append(( s[0],s[1],s[2]+" no Zptweight",       s[3], "weight/zptweight"))
        samplesB_ZptUp.append((   s[0],s[1],s[2]+" Zptweight*Zptweight",s[3], "weight*zptweight"))
    if s[0] in ["TT/"]:
        samplesB_TTptDown.append((s[0],s[1],s[2]+" no ttptweight",        s[3], "weight/ttptweight")) # Down: no TTpt weight
        samplesB_TTptUp.append((  s[0],s[1],s[2]+" ttptweight*ttptweight",s[3], "weight*ttptweight")) # Up:   TTpt weight twice applied
    if s[0] in ["WJ/"]:
        samplesB_QCD_WJDown.append((s[0],s[1],s[2]+" -30% QCD",s[3])) # QCD shifted in WJ renormalization procedure
        samplesB_QCD_WJUp.append(  (s[0],s[1],s[2]+" +30% QCD",s[3]))
    else: samplesB_noQCD_WJ.append(s)

samplesS            = [( "LowMass/", "LowMass_30GeV_DiTauResonance",         "signal",         1 )]
if not drawSignal: samplesS = [ ]
samplesS_EES0p99    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_EES0p99", "signal -1% TES", 1 )]
samplesS_EES1p01    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_EES1p01", "signal +1% TES", 1 )]
samplesS_JES0p97    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_JES0p97", "signal -3% JES", 1 )]
samplesS_JES1p03    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_JES1p03", "signal +3% JES", 1 )]
samplesS_TES0p97    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_TES0p97", "signal -3% TES", 1 )]
samplesS_TES1p03    = [( "LowMass/", "LowMass_30GeV_DiTauResonance_TES1p03", "signal +3% TES", 1 )]

samplesD = {
                "mutau" :  ( "SingleMuon/",     "SingleMuon_Run2016",     "single muon"     ),
                "etau"  :  ( "SingleElectron/", "SingleElectron_Run2016", "single electron" ),
            }
if "emu" in channels: samplesD = {"emu": ("MuonEG/","MuonEG_Run2016","electron-muon"),}
if not len(samplesD):
    print warning("No data, so disabled WJ renormalization and data driven QCD!")
    normalizeWJ = False
    doQCD       = False




    ###############
    # stack plots #
    ###############

def plotStacks(samples, channel, **kwargs):
    """Plot stacked histograms with data."""
    print header("%s channel: Stacks plots" % channel)
    
    DIR = kwargs.get('DIR',"%s/%s" % (PLOTS_DIR,channel))
    makeDirectory(DIR)
    
    stack       = True #and False
    staterror   = True
    errorbars   = (not staterror)
    
    # LOOP over SELECTIONS
    for label, cuts in categories:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),label.replace(' ','_')), color = "magenta")
        
        QCD = False
        if "q_1" in cuts and "q_2" in cuts: QCD = True and doQCD
        
        # REMOVE DY LOW MASS for jet categories
        ignore = ""
        if "category" in label: ignore = "Drell-Yan 10-50"
        #if "category" in label: removeLowMassDY(samples)
        
        # TT RENORMALIZATION
        if normalizeTT: renormalizeTT(samples, label=label, channel=channel, QCD=doQCD, reset=True, verbosity=verbosityTT)
        
        # SIGNAL RENORMALIZATION for each jet selection category separately
        category = isCategory(label) 
        if category:
            cuts_norm = "%s && "%baseline
            if "category 1" in category: cuts_norm+=category1
            else:                        cuts_norm+=category2
            for signal in samples:
                if signal.isSignal and normalizeSignal:
                    scale = signal.normalizeSignal(S_exp[category][channel],signalregion=blindlimits_norm["m_sv"],cuts=cuts_norm,verbosity=verbosityPlots)
                    print ">>>\n>>> normalized signal (%s) to %.1f events in the signal region %s (scale=%.3f)" % (signal.label,S_exp[category][channel],blindlimits_norm["m_sv"],scale)
        else: category = "baseline"
        
        
        # LOOP over VARIABLES
        for var, nBins, a, b in variables:
            
            # NAME
            name = "%s/%s_%s%s.png" % (DIR,var,label,plotlabel)
            if "m_vis" == var or "m_sv" == var:
                name = "%s/%s_%i_%s%s.png" % (DIR,var,b,label,plotlabel)
            name = name.replace(" and ","-").replace(" ","").replace(",","-").replace("(","").replace(")","") #.replace("(","").replace(")","")
            
            
            # TITLE
            title = "%s: %s" % (channel.replace("tau","#tau").replace("mu","#mu"),label)
            title.replace("category 1.2","optimized category 1").replace("category 2.2","optimized category 2")
            
            
            # BLIND LIMITS
            data = getData(samples,unique=True)
            if data:
                if "category" in label:
                    if "m_vis" in var:
                        data.blind["m_vis"] = "( m_vis < %i || %i < m_vis )" % (0,90)
                        print ">>> changing blindcuts data.blind[\"m_vis\"]=%s" % (data.blind["m_vis"])
                    if "m_sv" in var:
                        data.blind["m_sv"]  = "( m_sv  < %i || %i < m_sv  )" % (0,90)
                        print ">>> changing blindcuts data.blind[\"m_sv\"]=%s" % (data.blind["m_sv"])
                else: data.blind = blindcuts.copy() # reset
            else: print ">>> no data found to change blindcuts"
            
            
            # WEIGHT
            varweight = ""
            
            
            # RESCALE Signal
            if doSignalUpScaling:
                s = 500
                if "category" in label:   s *=  1
                else:                     s *= 10
                if "etau" in channel:
                    if "m_sv" == var or "m_vis" == var:
                        if   "1.2"      in label: s = 20
                        elif "2.2"      in label: s = 40
                        elif "category" in label: s = 40
                if "mutau" in channel:
                    if "m_sv" == var or "m_vis" == var:
                        if "category 1.2" in label: s = 100
                        if "category 2.2" in label: s = 200
                        elif "category" in label: s = 200
                if "emu" in channel:
                    if "m_sv" == var or "m_vis" == var:
                        if "category" in label: s = 200
                    if "dR"    in var:   s *=  2.0
                if "dR"    in var:   s *=  0.5
                if "pt_tt" in var:   s *=  6.0
                if "n"     in var:   s *=  5.0
                if "SR"    in label: s *=  0.2
                if "TT CR" in label: s *=  2.0
                
                for sample in samples:
                    if sample.isSignal:
                        sample.scale = sample.scaleBU * int(s)
                        #print warning("Signal (%s) enhanced by a factor of %.1f" % (sample.label,sample.scale/sample.scaleBU))
            
            
            # BINS
            if "category" in label:
                if "m_vis" == var or "m_sv" == var: # or "dR" in var:
                    #(a,b) = #8: (4,164)
                    nBins = (b-a)/5
                    print ">>> %s: changed binning to (%i,%i,%i)" % (var,nBins,a,b)
                if "met" == var:
                    (a,b) = (0,200)
                    nBins = (b-a)/8
                    print ">>> %s: changed binning to (%i,%i,%i)" % (var,nBins,a,b)
                if "pfmt_1" == var:
                    (a,b) = (0,200)
                    nBins = (b-a)/8
                    print ">>> %s: changed binning to (%i,%i,%i)" % (var,nBins,a,b)
            # if "dR_" in var:
            #     (a,b) = (0,6)
            #     nBins = 30
            #     print ">>> %s: changed binning to (%i,%i,%i)" % (var,nBins,a,b)
            #elif "m_vis" == var: #or "m_sv" is var:
            #    if b is 140:
            #       a = 2
            #       b = 140 + a
            #       print ">>> %s: changed binning to (%i,%i,%i)" % (var,nBins,a,b)
            if checkYield: nBins = 200
            
            
            # LEGEND POSITION
            position = ""
            logy = False
            if "m_" in var or "iso_" in var or "against" in var:
                position = "Left"
                #if b == 120: position = "LeftLeft"
            if "R_" in var:
                position = "Right"
            if "Iso" in var: # or "NUP" in var:
                position += "Center"
            if "jeta_" in var or "beta_" in var or "NUP" in var:
                position += "Top"
            if "jpt_1" in var and "category" in label:
                position += "Left"
            if "gen_match" in var:
                position = "Left" + position
                        
            # DRAW DATA
            data  = drawData #and not ("category" in label and "CR" not in label and  "SR" not in label and "m_sv" in var)
            ratio = data
            
            # PLOT
            plot = Plot( samples, var, nBins, a, b, cuts=cuts, QCD=QCD, verbosity=verbosityPlots, channel=channel) #, ignore=ignore, weight=varweight)
            plot.plot(stack=stack, position=position, title=title, staterror=staterror, logy=logy, ratio=ratio, errorbars=errorbars, data=data, channel=channel)
            if var in blindlimits: plot.checkSignal(blindlimits=blindlimits[var],S_exp=S_exp[category][channel]) # category defined above
            plotSignificance(plot)
            plot.saveAs(name,save=(not checkYield))
            
            # RESET CUTS
            if doSignalUpScaling:
                for sample in samples:
                    if sample.isSignal: sample.scale = sample.scaleBU





    ################
    # Extra checks #
    ################

def plotSignificance(plot):
    """Plot significance."""
    if not doSigma: return
    elif not plot.histsS:
        print warning("no signal sample to plot significance scan!")
        return
    
    var0 = plot.var
    variables_eff = [
                        ("pfmt_1",       20,   0, 150, True  ),
                        ("met",          20,   0, 120, True  ),
                        ##("pt_tt",        20,   0, 120, False ),
                        ##("pt_tt_sv",     20,   0, 150, False ),
                        ##("dR_ll",        20,   0,   7, True  ),
                        ##("R_pt_m_vis",   20,   0,   7, False ),
                        ##("R_pt_m_sv",    20,   0,   5, False ),
                        ##("pt_1",         20,   0, 150, False ),
                        ##("pt_2",         20,   0, 150, False ),
                        ##("bpt_1",        20,   0, 150, False ),
                        ##("bpt_2",        20,   0, 150, False ),
                        ##("jpt_1",        20,   0, 150, False ),
                        ##("jpt_2",        20,   0, 150, False ),
                        ##("dphi_ll_bj",   20,   0, 150, False ),
                    ]
    
    for var, nBins, a, b, upper in variables_eff:
        if var0 == var:
            #print ">>> " + color("making significance vs. cut value", color="grey")
            print ">>> making significance vs. cut value"
            plot.significanceScan(upper=upper)
    




    #####################
    # plot2DCorrelation #
    #####################

def plot2DCorrelation(samples, channel, **kwargs):
    """Plot correlation between two variables into a 2D histograms."""
    print header("%s channel: 2D Correlation plots" % channel)
    
    DIR         = kwargs.get('DIR',"%s/%s" % (PLOTS_DIR,channel))+"_2D"
    profileX    = kwargs.get('profileX',True)
    makeDirectory(DIR)
    
    label = mylabel
    variables2D = [ ]
    
    
    # VARIABLES
    for s in [ "signal", "ttbar", "Drell-Yan" ]:
        ##variables2D.append(( s, "dR_ll",     40, 0,   5, "m_vis",     40, 0, 100 ))
#         variables2D.append(( s, "m_sv",     40, 0, 100, "pt_tt_sv",  40, 0, 150 ))
#         variables2D.append(( s, "dR_ll",    40, 0,   5, "m_sv",      40, 0, 100 ))
#         variables2D.append(( s, "R_pt_m_sv", 40, 0,   5, "m_sv",     40, 0, 100 ))
#         variables2D.append(( s, "dR_ll",    40, 0,   5, "pt_tt_sv",  40, 0, 150 ))
#         variables2D.append(( s, "dR_ll",    40, 0,   5, "R_pt_m_sv", 40, 0,   5 ))
#         variables2D.append(( s, "pt_tt_sv", 40, 0, 150, "R_pt_m_sv", 40, 0,   5 ))
        variables2D.append(( s, "pt_tt",    40, 0, 200, "m_sv", 40, 0,  200 ))
#         variables2D.append(( s, "met",      40, 0, 150, "pfmt_1",    40, 0, 150 ))
#         variables2D.append(( s, "met",      40, 0, 100, "R_pt_m_sv", 40, 0,   5 ))
#         variables2D.append(( s, "met",      40, 0, 100, "pt_tt_sv",  40, 0, 150 ))
#         variables2D.append(( s, "met",      40, 0, 100, "m_sv",      40, 0, 100 ))
#         variables2D.append(( s, "pfmt_1",   40, 0, 100, "R_pt_m_sv", 40, 0,   5 ))
#         variables2D.append(( s, "pfmt_1",   40, 0, 100, "pt_tt_sv",  40, 0, 150 ))
#         variables2D.append(( s, "pfmt_1",   40, 0, 100, "m_sv",      40, 0, 100 ))
        ##variables2D.append(( s, "met",      40, 0, 150, "mvamet",    40, 0, 150 ))
        ##variables2D.append(( s, "met",      40, 0, 150, "puppimet",  40, 0, 150 ))
        ##variables2D.append(( s, "mvamet",   40, 0, 150, "puppimet",  40, 0, 150 ))
    
    
    # LOOP over SELECTIONS
    for label, cuts in categories:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),label.replace(' ','_')), color = "magenta")
        
        # LOOP over VARIABLES
        for samplename, var1, nBins1, a1, b1, var2, nBins2, a2, b2 in variables2D:
            
            # NAME
            name = "%s/%s_vs_%s_%s_%s.png" % (DIR,var1,var2,samplename,label)
            name = name.replace(" and ","-").replace(" ","").replace(",","-").replace("(","").replace(")","")
            
            # GET SAMPLE
            sample = None
            for s in samples:
                if s.label == samplename:
                    sample = s
                    break
            else:
                print warning("Could not make 2D correlation plot: no sample with name \"%s\"!" % (samplename))
                continue
            
            plot2D = Plot2D(sample, var1, nBins1, a1, b1, var2, nBins2, a2, b2, cuts=cuts)
            plot2D.plot()
            if profileX:
                profile = plot2D.hist.ProfileX()
                profile.SetLineColor(kRed+1)
                profile.SetLineWidth(3)
                plofile.SetMarkerSize(0)
                profile.Draw("HIST same E")
            plot2D.saveAs(name)
    




    ##########################
    # checkCutflowEfficiency #
    ##########################

def checkCutflowEfficiency(samples, channel, **kwargs):
    """Check cutflow efficiency for a set of samples."""
    print header("%s channel: Checking cutflow" % channel)
    # TODO: implement way to include SFrame cutflow histogram; see PlotTools
    
    #vetos1 = vetos_mutau
    #if "etau" in channel:  vetos1 = vetos_etau
    #vetos2 = "lepton_vetos==0"
    var = kwargs.get('var',"m_sv")
    (aa,bb) = (0,60)
    print ">>> SR defined as %i to %i\n>>>" % (aa,bb)

    
    categories_dict = { "no cuts":              "",
                        "iso":                  "%s"                % (isocuts),
                        "vetos":                "%s"                % (vetos),
                        "iso, vetos":           "%s && %s"          % (isocuts, vetos),
                        "iso, vetos, OS":       "%s"                % (baseline),
                        "b jet":                "%s && ncbtag > 0"  % (baseline),
                        "category 1":           "%s && %s"          % (baseline, category1),
                        "category 2":           "%s && %s"          % (baseline, category2),
                        "category 1 met":       "%s && %s && %s"    % (baseline, category1, metcut),
                        "category 1 mt1":       "%s && %s && %s"    % (baseline, category1, mt1cut),
                        "category 2 met":       "%s && %s && %s"    % (baseline, category2, metcut),
                        "category 2 mt1":       "%s && %s && %s"    % (baseline, category2, mt1cut),
                        "category 1.2":         "%s && %s && %s"    % (baseline, category1, newcuts),
                        "category 2.2":         "%s && %s && %s"    % (baseline, category2, newcuts),
                       }
    cutflows = [
                    ("no cuts", "iso, vetos, OS", "category 1", "category 1.2"),
                    ("no cuts", "iso, vetos, OS", "category 2", "category 2.2"),
#                     ("no cuts", "vetos 2", "vetos"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "category 1", "category 1.2"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "category 2", "category 2.2"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "b jet", "category 1", "category 1 met", "category 1.2"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "b jet", "category 2", "category 2 met", "category 2.2"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "b jet", "category 1", "category 1 mt1", "category 1.2"),
#                     ("no cuts", "iso", "iso, vetos", "iso, vetos, OS", "b jet", "category 2", "category 2 mt1", "category 2.2"),
#                     ("category 1", "category 1 mt1", "category 1.2"),
#                     ("category 2", "category 2 mt1", "category 2.2"),
                ]
    
    samplenames = [
#                     "signal",
#                     "ttbar",
#                     "ST",
                    "Drell-Yan 10-50",
                    "Drell-Yan 1J 10-50",
                    "Drell-Yan 2J 10-50",
                    "Drell-Yan 3J 10-50",
#                     "Drell-Yan 50",
                  ]
    
    # FILTER dictionary
    categories_dict0 = { }
    for cutflow in cutflows:
        for label in cutflow:
            if label in categories_dict and label not in categories_dict0:
                categories_dict0[label] = categories_dict[label]
    
    # LOOP over VARIABLES
    for samplename in samplenames:
        print ">>> cutting on %s in %s:" % (var,samplename)
        
        # GET SAMPLE
        sample = None
        sample = getSample(samples,samplename,unique=True)
        if not sample:
            print warning("Could not calculate cutflow efficiency: no sample with name \"%s\"!" % (samplename), prepend="  ")
            continue
        
        # LOOP over dictionary
        yield_dict        = { }
        yield_SR_dict     = { }
        distribution_dict = { }
        for label in categories_dict0:
            cuts = combineCuts("%s > 0" % var,categories_dict0[label])        
            name    = "%s_for_cutflow_eff" % (var)
            hist    = sample.hist(var,250,0,250,cuts=cuts,name=name)
            yield_dict[label]        = (hist.GetSumOfWeights(),hist.GetEntries())
            if sample.isSignal: hist.GetXaxis().SetRangeUser(aa,bb)
            distribution_dict[label] = (hist.GetMean(),hist.GetStdDev())
            hist.GetXaxis().SetRangeUser(*blindlimits[var])
            yield_SR_dict[label]     = (hist.GetSumOfWeights(),hist.GetEntries())
            gDirectory.Delete(name)
            
        # LOOP over CUTFLOWS and their respective SELECTIONS
        for cutflow in cutflows:
            print ">>>\n>>> %20s %10s %10s %12s %12s %14s %16s %10s %10s" % ("selection".ljust(16),"rel eff","abs eff","yield","MC events","yield in SR","MC events in SR","mean","sigma")
            N0 = 0
            N_last = 0
            for label in cutflow:
                if label not in yield_dict: warning("Label not found in categories_dict!")
                (N,MC)      = yield_dict[label]
                (N_SR,MC_SR) = yield_SR_dict[label]
                (mean,sd)   = distribution_dict[label]
                if not N0 and N:
                    N0      = N
                    N_last  = N
                if N_last and N0:
                    print ">>> %20s %9.2f%% %9.2f%% %12.2f %12.0f %14.2f %16.0f %10.2f %10.2f" % (label.ljust(18), 100.0*N/N_last, 100.0*N/N0, N, MC, N_SR, MC_SR, mean, sd)
                if not N:
                    print ">>> zero events left: stop!"
                    break
                N_last = N
        
        print ">>>\n>>> "
    




    ##################
    # plotComparison #
    ##################

def plotComparison(samples_comp, channel, **kwargs):
    """Plot histograms for comparison."""
    print header("%s channel: compare histograms" % channel)
    
    # TODO: make samples without DY Zpt weighted!
    
    comparisons = [
            ("ttbar ttpt", ["ttbar","Drell-Yan 10","Drell-Yan 50","W + jets"], [
                            ( "trigweight_1",      100, 0, 3.0 ),
                            ( "triggers",            5, 0, 5   ),]),
#             ("ttbar ttpt", ["ttbar ttpt","ttbar no ttpt"], [
#                             ( "m_sv",      50, 0, 200 ),
#                             #( "mt_1",      50, 0, 150 ),
#                             ( "pt_1",      50, 0, 160 ),
#                             ( "pt_2",      50, 0, 160 ),
#                             ( "pt_tt_sv",  50, 0, 160 ), ]),
#             ("DY-50 Zpt", ["Drell-Yan 50 Zpt","Drell-Yan 50 no Zpt"], [
#                             ( "m_sv",      50, 0, 150 ),
#                             #( "mt_1",      50, 0, 150 ),
#                             ( "pt_1",      50, 0, 160 ),
#                             ( "pt_2",      50, 0, 160 ),
#                             ( "m_genboson",  5, 0,  5 ),
#                             ( "pt_genboson", 5, 0,  5 ),
#                             ( "ncjets",     5, 0,   5 ),
#                             ( "nbjets",     5, 0,   5 ),
#                             ( "ncbtag",     5, 0,   5 ),
#                             ( "pt_tt_sv",  50, 0, 160 ), ]),
                    ]
    
    categories_comp = [
            ("baseline",            baseline),
            #("category 1.2",        "%s && %s && %s" % (baseline, category1, newcuts)),
            #("category 2.2",        "%s && %s && %s" % (baseline, category2, mt1cut)),
              ]
    
    # SETTINGS
    DIR         = kwargs.get('DIR',PLOTS_DIR)+"_comparison"
    makeDirectory(DIR)
    weight      = "" #weight"
    norm        = True
    errorbars   = False
    position    = ""
    
    # LOOP over COMPARISONS
    for label_comp, samplenames, vars in comparisons:
        print ">>> comparing %s: " % (', '.join(samplenames))
        
        # LOOP over SAMPLENAMES
        samples = [ ]
        for samplename in samplenames:
            sample = getSample(samples_comp,samplename,unique=True)
            samples.append(sample)
        if   len(samples) is 0:
            print warning("Could not make comparisons! Could not find any samples!")
            continue
        
        # LOOP over SELECTIONS
        for label, cuts in categories_comp:
            
            # LOOP over VARS
            for var, nBins, a, b in vars:
                
                title = label
                name = "%s/%s_%s_%s%s.png" % (DIR,label_comp.replace(' ','_'),var,label,plotlabel)
                
                plot = Plot(samples,var,nBins,a,b,cuts=cuts)
                plot.plot(stack=False, title=title, norm=norm, errorbars=errorbars, position=position)
                plot.saveAs(name)
            
        print ">>>"
            




    ##########################
    # writeDataCardHistogram #
    ##########################

def writeDataCardHistograms(samples, channel, **kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    # TODO:
    # 1) save cutflow
    # 2) ...
    # 3) implement JES
    
    categories_DC = [
        ("category 1.2",        "%s && %s && %s" % (baseline, category1, newcuts)),
        ("category 2.2",        "%s && %s && %s" % (baseline, category2, newcuts)),
                    ]
    
    samples_dict = {  # search term               label          extracuts 
                        "ttbar":            [   ( 'TTT',    "gen_match_2 == 5" ),
                                                ( 'TTJ',    "gen_match_2 == 6" ),
                                                ( 'TTL',    "gen_match_2  < 5" ), ],
                        "Drell-Yan 50":     [   ( 'ZTT',    "gen_match_2 == 5" ),
                                                ( 'ZL',     "gen_match_2  < 5" ),
                                                ( 'ZJ',     "gen_match_2 == 6" ), ],
                        "W + jets":         [   ( 'W',      ""                 ), ],
                        "diboson":          [   ( 'VV',     ""                 ), ],
                                                #( "VVT",    "gen_match_2 == 5" ),
                                                #( "VVJ",    "gen_match_2 != 5" ), ],
                        'ST':               [   ( 'ST',     ""                 ), ],
                        'QCD':              [   ( 'QCD',    ""                 ), ],
                        'signal':           [                                     ],
                    }
    
    # DATA
    if  "mutau" in channel: samples_dict["single muon"]     = [( "data_obs", "" )]
    elif "etau" in channel: samples_dict["single electron"] = [( "data_obs", "" )]
    elif "emu"  in channel: samples_dict["electron-muon"]   = [( "data_obs", "" )]
    
    # SIGNAL mass points
    shiftSignal = kwargs.get('shiftSignal',False)
    masses      = kwargs.get('masses',range(13,83,3))
    if shiftSignal:
        for mass in masses:
            samples_dict['signal'].append(( "XTT-S1-M%s"   % (mass), ""))
            #samples_dict['signal'].append(( "XTT-S0-M%s"   % (mass), "")) # model independent
            samples_dict['signal'].append(( "XTT-S283-M%s" % (mass), ""))
    else:
        samples_dict['signal'].append(( "XTT-S1-M%s"   % (28), ""))
        #samples_dict['signal'].append(( "XTT-S0-M%s"   % (28), "")) # model independent
        samples_dict['signal'].append(( "XTT-S283-M%s" % (28), ""))
        
    
    # HIST
    var         = "m_sv"
    (a,b)       = kwargs.get('range',(0,350))
    binWidth    = kwargs.get('binWidth',5)
    nBins       = int(kwargs.get('nBins',(b-a)/binWidth))
    weight      = "weight"
    
    # FILE LOGISTICS
    DIR         = kwargs.get('DIR',DATACARDS_DIR)
    label       = kwargs.get('label',"")
    option      = 'UPDATE'
    if kwargs.get('recreate',False): option = 'RECREATE'
    outdir      = "%s%s/" % (DIR,"datacards" if "datacards" not in DIR else "")
    makeDirectory(outdir)
    outfilename = outdir + makeDataCardOutputName(channel,"LowMassDiTau",label=label)
    outfile     = TFile(outfilename, option)
    
    # FILTER
    filter      = kwargs.get('filter',[ ])
    if filter:
        for key in samples_dict.keys():
            if key not in filter: samples_dict.pop(key,None)
    
    
    # SYSTEMATIC UNCERTAINTY
    su_label    = kwargs.get('su_label',"")
    E           = kwargs.get('E',"13TeV")
    TES         = kwargs.get('TES',"")
    EES         = kwargs.get('EES',"")
    JES         = kwargs.get('JES',"")
    LTF         = kwargs.get('LTF',"")
    Zpt         = kwargs.get('Zpt',"")
    TTpt        = kwargs.get('TTpt',"")
    QCD_WJ      = kwargs.get('QCD_WJ',"")
    channel0    = channel.replace("tau","t").replace("mu","m")
    shift_QCD   = kwargs.get('shift_QCD',0) # e.g 0.30
    hist_QCD    = None
    name_QCD    = ""
    
    if shift_QCD:
        samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sDown"       % (channel0,E), "" ))
        samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sUp"         % (channel0,E), "" ))
    else: samples_dict.pop('QCD',None) # only run QCD is it's also shifted
    if TES    in ["Down","Up"]: su_label += "_CMS_xtt_shape_t_%s_%s%s"      % (channel0,E,TES)
    if EES    in ["Down","Up"]: su_label += "_CMS_xtt_shape_e_%s_%s%s"      % (channel0,E,EES)
    if JES    in ["Down","Up"]: su_label += "_CMS_xtt_shape_j_%s_%s%s"      % (channel0,E,JES)
    if LTF    in ["Down","Up"]: su_label += "_CMS_xtt_ZLShape_%s_%s%s"      % (channel0,E,LTF)
    if Zpt    in ["Down","Up"]: su_label += "_CMS_xtt_dyShape_%s_%s%s"      % (channel0,E,Zpt)
    if TTpt   in ["Down","Up"]: su_label += "_CMS_xtt_ttbarShape_%s_%s%s"   % (channel0,E,TTpt)
    if QCD_WJ in ["Down","Up"]: su_label += "_QCD_Extrapolation_%s_%s%s"    % (channel0,E,QCD_WJ)
    print ">>> writing %s shapes to %s (%sd)" % (var,outfilename,option)
    if su_label: print ">>> systematic uncertainty label = " + color("%s" % (su_label.lstrip("_")), color="grey")
    
    
    # LOOP over CATEGORIES
    for category, cuts in categories_DC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color = "magenta")
        
        # CATEGORY 1 or 2
        categoryi = isCategory(category)
        if not categoryi: print warning("writeDataCardHistograms: Could not find category 1 or 2 of %s"%(category))
        
        # REMOVE DY LOW MASS for jet categories
        ignore = ""
        if "category" in category: ignore = "Drell-Yan 10-50"
        #if "category" in label: removeLowMassDY(samples)
        
        # MAKE DIR
        (dir,dirname) = makeDataCardTDir(outfile,channel,category)
        
        # TT RENORMALIZATION
        if normalizeTT: renormalizeTT(samples, label=category, channel=channel, QCD=doQCD, reset=True, verbosity=verbosityTT)
        
        # LOOP over SAMPLES
        for samplename in samples_dict:
            
            # FIND SAMPLE
            matches = [ ]
            sample  = None
            if 'QCD' not in samplename:
                for sample in samples:
                    #print ">>> sample.label = %s" % (sample.label)
                    if sample.isPartOf(samplename): matches.append(sample)
                if not matches:
                    print warning("Could make datacard histogram! No \"%s\" sample!" % (samplename),prepend="  ")
                    continue
                elif len(matches)>1: print warning("  Found more than one \"%s\" sample!" % (samplename))
                else: sample = matches[0]
            scale_LA = 1
            if "signal" in samplename:
                cuts_norm = "%s && "%baseline
                if   "category 1" in category.lower(): cuts_norm+=category1
                else:                                  cuts_norm+=category2
                scale = sample.normalizeSignal(S_exp[categoryi][channel],signalregion=blindlimits_norm["m_sv"],cuts=cuts_norm,verbosity=verbosityPlots)
                print ">>>\n>>> normalized signal (%s) to %.2f events in the signal region %s (scale=%.3f)" % (sample.label,S_exp[categoryi][channel],blindlimits_norm["m_sv"],scale)
                scale_LA = sample.calculateLumiAcceptance(cuts_norm,signalregion=blindlimits_norm["m_sv"],verbosity=1)
                scale_LA = sample.calculateLumiAcceptance(cuts,signalregion=blindlimits_norm["m_sv"],verbosity=1)
                
            for subsample, extracuts in samples_dict[samplename]:
                printSameLine(">>>   making  %3s histogram..." % (subsample.ljust(14))) # TODO: make table instead
                
                # SETUP NAMES
                name        = subsample+su_label
                cuts1       = combineCuts(cuts,extracuts,"%s<%s && %s<%s"%(a,var,var,b))
                
                # SHIFT & SMEAR signal
                # shift = 0
                # smear = 0
                # if "XTT" in subsample and "-M" in subsample and "-M28" not in subsample:
                #     mass    = int(subsample[subsample.index("-M")+2:])
                #     shift   = mass-28
                #     smear   = mass/28.0
                
                # MAKE HIST
                hist        = None
                plot        = None
                if 'QCD' in subsample: # QCD
                    if "Down" in subsample and shift_QCD:
                        hist = hist_QCD.Clone(name)
                        hist.Scale(1-shift_QCD)
                    elif "Up" in subsample and shift_QCD:
                        hist = hist_QCD.Clone(name)
                        hist.Scale(1+shift_QCD)
                    else:
                        plot = Plot(samples,var,nBins,a,b,cuts=cuts1,QCD=False,ignore=ignore)
                        hist = plot.QCD(name=name)
                        if shift_QCD:
                            name_QCD = name+"_QCD_clone"
                            hist_QCD = hist.Clone(name_QCD) # don't calculate QCD trice!
                    if hist is None:
                        print warning("QCD histogram failed!")
                        continue
                else:
                    hist = sample.hist(var,nBins,a,b,name=name,cuts=cuts1) #,shift=shift,smear=smear)
                hist.SetLineStyle(1)
                hist.SetLineWidth(2)
                
                # SCALE
                if "XTT-S283" in subsample: hist.Scale(283)
                #elif "XTT-S0" in subsample: hist.Scale(scale_LA) # model independent
                
                # WRITE HIST
                hist.Write(hist.GetName(),TH1D.kOverwrite)
                print "     written %5i entries to file (yield is %5.1f)" % (hist.GetEntries(),hist.GetSumOfWeights())
                gDirectory.Delete(name)
                if plot: plot.close()
                
        if name_QCD: gDirectory.Delete(name_QCD)
        
    outfile.Close()
    print ">>>\n>>> "


def makeDataCardOutputName(channel, analysis, label="", E="13TeV", M="28"):
    """Make name of output file according to HTT Working TWiki."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    
    if "t" in channel:
        if   "m" in channel: channel = "mt"
        elif "e" in channel: channel = "et"
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = "em"
    else: print ">>> makeOutputName: channel not found!"
    
    outputname = "xtt_%s.inputs-%s-%s-%s%s.root" % (channel,analysis,E,M,label)
    return outputname
    

def makeDataCardTDir(outfile, channel, category, E="13TeV", M="28"):
    """Make name of directory according to HTT Working TWiki."""
    
    category = category.replace(' ','_').replace('.','_').replace(',','-')
    dirname = category
    
    dir = outfile.GetDirectory(dirname)
    if not dir:
        dir = outfile.mkdir(dirname)
        outfilename = '/'.join(outfile.GetPath().replace(":/","").split('/')[-2:])
        print ">>>   created directory %s in %s" % (dirname,outfilename)
    dir.cd()
    return (dir,dirname)
    




    ##################
    # Help functions #
    ##################

def makeDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    
def isCategory(category):
    """Check whether selections label contain category 1 or 2."""
    if "category 1" in category.lower(): return "category 1"
    if "category 2" in category.lower(): return "category 2" 
    return False
    




    ##############
    # Categories #
    ##############

def listCategories():
    """List all available categories"""

    print ">>> list of available categories:"
    for name, cuts in categories:
        print ">>>\t%s" % name
    print ">>>\t"

def selectCategory(category):
    """Only run for this category"""
    global categories
    if -1 < category < len(categories) and category == round(category):
        print ">>> select selection category %i" % category
        categories = [categories[category]]
    else:
        print error("Category %i does not exist!" % category)
        sys.exit(1)

def selectChannel(channel):
    """Only run for this channel"""
    global channels
    if channel:
        if   "et" in channel[:2]: channel = "etau"
        elif "mt" in channel[:2]: channel = "mutau"
        if channel in channels:
            print ">>> select channel %s" % channel
            channels = [channel]
        else:
            print error("Channel %s does not exist!" % channel)
            sys.exit(1)
    else:
        print error("Channel %s is not a valid input!" % channel)
        sys.exit(1)
    




    ########
    # main #
    ########

def main():
    """Main function."""
    
    if args.list:
        listCategories()
        return 0
        
    if args.verbose:
        global verbosity, verbosityWJ, verbosityTT, verbosityPlots
        verbosity       = 2
        verbosityWJ     = 2
        verbosityTT     = 2
        verbosityPlots  = 2

    
    # MAKE SAMPLES
    global samplesB, samplesS, samplesD
    global samplesB_EES0p99,  samplesB_EES1p01, samplesS_EES0p99,  samplesS_EES1p01
    #global samplesB_JES0p97,  samplesB_JES1p03, samplesS_JES0p97,  samplesS_JES1p03
    global samplesB_TES0p97,  samplesB_TES1p03, samplesS_TES0p97,  samplesS_TES1p03
    global samplesB_LTF0p97,  samplesB_LTF1p03
    global samplesB_ZptUp,    samplesB_ZptDown
    global samplesB_TTptUp,   samplesB_TTptDown
    global samplesB_QCD_WJUp, samplesB_QCD_WJDown, samplesB_noQCD_WJ
    global samplesB_comp
    makeSamples(samplesB=samplesB, samplesS=samplesS, samplesD=samplesD, stitchDY50=stitchDY50, stitchDY10to50=stitchDY10to50, verbosity=verbosity, weight=weight_)
    if doComparison and False:
        makeSamples(samplesB=samplesB_comp,verbosity=verbosity,labels_DY50=["50 Zpt","50 no Zpt"])
    if doDataCard:
        if doTES:
            print header("Tau energy scale samples")
            makeSamples(samplesB=samplesB_TES0p97,  samplesS=samplesS_TES0p97, verbosity=verbosity)
            makeSamples(samplesB=samplesB_TES1p03,  samplesS=samplesS_TES1p03, verbosity=verbosity)
        if doEES:
            print header("Electron energy scale samples")
            makeSamples(samplesB=samplesB_EES0p99,  samplesS=samplesS_EES0p99, verbosity=verbosity)
            makeSamples(samplesB=samplesB_EES1p01,  samplesS=samplesS_EES1p01, verbosity=verbosity)
#         if doJES:
#             print header("Jet energy scale samples")
#             makeSamples(samplesB=samplesB_JES0p97,  samplesS=samplesS_JES0p97, verbosity=verbosity)
#             makeSamples(samplesB=samplesB_JES1p03,  samplesS=samplesS_JES1p03, verbosity=verbosity)
        if doLTF:
            print header("Lepton to tau fake samples")
            makeSamples(samplesB=samplesB_LTF0p97, verbosity=verbosity)
            makeSamples(samplesB=samplesB_LTF1p03, verbosity=verbosity)
        if doZpt:
            print header("Z pt reweighting scale samples")
            makeSamples(samplesB=samplesB_ZptDown, verbosity=verbosity)
            makeSamples(samplesB=samplesB_ZptUp,   verbosity=verbosity)
        if doTTpt:
            print header("Top pt reweighting scale samples")
            makeSamples(samplesB=samplesB_TTptDown, verbosity=verbosity)
            makeSamples(samplesB=samplesB_TTptUp,   verbosity=verbosity)
        if doQCD_WJ:
            print header("QCD scale WJ samples")
            makeSamples(samplesB=samplesB_QCD_WJUp,   verbosity=verbosity)
            makeSamples(samplesB=samplesB_QCD_WJDown, verbosity=verbosity)
            makeSamples(samplesB=samplesB_noQCD_WJ,   verbosity=verbosity)
    
    # USER OPTIONS
    global channels
    if args.category > -1: selectCategory(args.category)
    if args.channel:       selectChannel(args.channel)
    if args.etau or args.mutau:
        channels = [ ]
        if args.etau:  channels.append("etau")
        if args.mutau: channels.append("mutau")
    
        
    # LOOP over CHANNELS
    for channel in channels:
        print ">>>\n>>>"
        
        samples             = samplesB                                + samplesS         + samplesD.get(channel,[]) # for normal plots
        samples_EES0p99     = samplesB_EES0p99                        + samplesS_EES0p99 + samplesD.get(channel,[]) # for WJ renorm only
        samples_EES1p01     = samplesB_EES1p01                        + samplesS_EES1p01 + samplesD.get(channel,[]) # for WJ renorm only
        samplesSB_EES0p99   = samplesB_EES0p99                        + samplesS_EES0p99                            # for datacard
        samplesSB_EES1p01   = samplesB_EES1p01                        + samplesS_EES1p01                            # for datacard
#         samples_JES0p97     = samplesB_JES0p97                        + samplesS_JES0p97 + samplesD.get(channel,[]) # for WJ renorm only
#         samples_JES1p03     = samplesB_JES1p03                        + samplesS_JES1p03 + samplesD.get(channel,[]) # for WJ renorm only
#         samplesSB_JES0p97   = samplesB_JES0p97                        + samplesS_JES0p97                            # for datacard
#         samplesSB_JES1p03   = samplesB_JES1p03                        + samplesS_JES1p03                            # for datacard
        samplesSB_TES0p97   = samplesB_TES0p97                        + samplesS_TES0p97                            # for datacard (noWJ)
        samplesSB_TES1p03   = samplesB_TES1p03                        + samplesS_TES1p03                            # for datacard (noWJ)
        samples_QCD_WJDown  = samplesB_QCD_WJUp   + samplesB_noQCD_WJ                    + samplesD.get(channel,[]) # for WJ renorm only
        samples_QCD_WJUp    = samplesB_QCD_WJDown + samplesB_noQCD_WJ                    + samplesD.get(channel,[]) # for WJ renorm only
        
        # SET TREENAME
        treeName = "tree_%s" % channel
        if useCutTree and "emu" not in channel: treeName = "tree_%s_cut_relaxed" % channel
        for sample in samples+samples_EES0p99+samples_EES1p01+samplesSB_TES0p97+samplesSB_TES1p03+samplesB_LTF0p97+samplesB_LTF1p03+\
                      samples_QCD_WJDown+samples_QCD_WJUp+samplesB_ZptDown+samplesB_ZptUp+samplesB_TTptDown+samplesB_TTptUp:
            if type(sample) is not tuple: sample.treeName=treeName
        
        # NORMALIZE SIGNAL
        print header("%s: signal renormalization" % (channel))
        for signal in samplesS+samplesS_TES0p97+samplesS_TES1p03:
            if type(signal) is not tuple and normalizeSignal:
                scale = signal.normalizeSignal(S_exp["baseline"][channel],signalregion=blindlimits_norm["m_sv"],verbosity=verbosityPlots)
                print ">>>\n>>> normalized signal (%s) to %.1f events in the signal region %s (scale=%.3f)" % (signal.label,S_exp["baseline"][channel],blindlimits_norm["m_sv"],scale)
        
        # RENORMALIZE WJ
        print ">>> "
        if normalizeWJ and channel!="emu":
            print header("%s: WJ renormalization" % (channel))
            renormalizeWJ(samples, cuts=baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
            if doDataCard:
                if doQCD_WJ:
                    renormalizeWJ(samples_QCD_WJDown, cuts=baseline, QCD=doQCD, reset=True, shift_QCD=-0.30, prepend="QCD down shift: ", verbosity=verbosityWJ)
                    renormalizeWJ(samples_QCD_WJUp,   cuts=baseline, QCD=doQCD, reset=True, shift_QCD=+0.30, prepend="QCD up   shift: ", verbosity=verbosityWJ)
                if doEES:
                    renormalizeWJ(samples_EES0p99, cuts=baseline, QCD=doQCD, reset=True, prepend="EES down shift: ", verbosity=verbosityWJ)
                    renormalizeWJ(samples_EES1p03, cuts=baseline, QCD=doQCD, reset=True, prepend="EES up   shift: ", verbosity=verbosityWJ)
                #if doJES:
                #    renormalizeWJ(samples_JES0p97, cuts=baseline, QCD=doQCD, reset=True, prepend="EES down shift: ", verbosity=verbosityWJ)
                #    renormalizeWJ(samples_JES1p03, cuts=baseline, QCD=doQCD, reset=True, prepend="EES up   shift: ", verbosity=verbosityWJ)
        else: print warning("Not WJ renormalized! (normalizeWJ=%s, channel=%s)" % (normalizeWJ,channel))
        print ">>> "
        
        # DIRECTORIES
        dirlabel = mylabel
        DIR = PLOTS_DIR+channel+dirlabel
        
        # MAIN ROUTINES
        if doStack:
            plotStacks(samples,channel,DIR=DIR)
        if doCheckCutflow:
            checkCutflowEfficiency(samples,channel)
        if doPlot2D:
            plot2DCorrelation(samples,channel,DIR=DIR)
        if doComparison:
            plotComparison(samplesB,channel,DIR=DIR)
            #plotComparison(samplesB_comp,channel,DIR=DIR)
        if doDataCard:
            print header("%s channel: Writing histogram for datacards" % channel)
            # for mass in range(31,71,3):
            #     binWidth = int(ceil(mass*0.10))
            #     (a,b) = (mass-binWidth,mass+binWidth)
            #     binlabel = "-scan-M%s" % (mass)
            binWidth = 5
            (a,b) = (0,350)
            binlabel = ""
            writeDataCardHistograms(    samples,           channel, recreate=recreate, shift_QCD=0.30, label=binlabel, binWidth=binWidth, range=(a,b), masses=[28] )
            if doEES:
                writeDataCardHistograms(samplesSB_EES0p99, channel, EES="Down", label=binlabel, binWidth=binWidth, range=(a,b), masses=[28] )
                writeDataCardHistograms(samplesSB_EES1p01, channel, EES="Up",   label=binlabel, binWidth=binWidth, range=(a,b), masses=[28] )
#             if doJES:
#                 writeDataCardHistograms(samplesSB_JES0p97,  channel, JES="Down", label=binlabel, binWidth=binWidth, range=(a,b), masses=[28], ignoreQCD = True )
#                 writeDataCardHistograms(samplesSB_JES1p03,  channel, JES="Up",   label=binlabel, binWidth=binWidth, range=(a,b), masses=[28], ignoreQCD = True )
            if doTES:
                writeDataCardHistograms(samplesSB_TES0p97, channel, TES="Down", filter=["signal","ttbar","Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b), masses=[28] )
                writeDataCardHistograms(samplesSB_TES1p03, channel, TES="Up",   filter=["signal","ttbar","Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b), masses=[28] )
            if doLTF:
                writeDataCardHistograms(samplesB_LTF0p97,  channel, LTF="Down", filter=["Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b) )
                writeDataCardHistograms(samplesB_LTF1p03,  channel, LTF="Up",   filter=["Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b) )
            if doZpt:
                writeDataCardHistograms(samplesB_ZptDown,  channel, Zpt="Down", filter=["Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b) )
                writeDataCardHistograms(samplesB_ZptUp,    channel, Zpt="Up",   filter=["Drell-Yan 50"], label=binlabel, binWidth=binWidth, range=(a,b) )
            if doTTpt:
                writeDataCardHistograms(samplesB_TTptDown, channel, TTpt="Down", filter=["ttbar"], label=binlabel, binWidth=binWidth, range=(a,b) )
                writeDataCardHistograms(samplesB_TTptUp,   channel, TTpt="Up",   filter=["ttbar"], label=binlabel, binWidth=binWidth, range=(a,b) )
            if doQCD_WJ:
                writeDataCardHistograms(samplesB_QCD_WJDown, channel, QCD_WJ="Down", filter=["W + jets"], label=binlabel, binWidth=binWidth, range=(a,b) )
                writeDataCardHistograms(samplesB_QCD_WJUp,   channel, QCD_WJ="Up",   filter=["W + jets"], label=binlabel, binWidth=binWidth, range=(a,b) )
            
        
    


if __name__ == '__main__':
    print
    PlotTools.PlotTools.lumi = lumi
    for var in ['lumi','mylabel','blindcuts','blindlimits',
                'baseline','category1','category2','category1TT','category2TT','SAMPLE_DIR','PLOTS_DIR']:
        setattr(PlotTools.SampleTools,var,globals()[var])
    main()
    print ">>>\n>>> Done with this, son.\n"




