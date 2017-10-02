#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
import PlotTools.PlotTools
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.SampleTools import getEfficienciesFromHistogram, getEfficienciesFromTree, printComparingCutflow
from math import log, floor
import ROOT
from ROOT import TFile, TH1F, TH2F, kRed, kBlue, THStack, TCanvas, TLegend, kAzure, kRed, kGreen, kYellow, kOrange, gPad, gROOT, gStyle
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

SFRAME_DIR = "SFrameAnalysis_Moriond"
DIR = "/shome/ineuteli/analysis/%s/AnalysisOutput/" % (SFRAME_DIR)
MORIOND_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
EM_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM"
MM_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputMM"
OUT_DIR = "plots_check"
mylabel = "_ICHEP"

# CMS style
lumi = 35.9 # 12.9
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.105
CMS_lumi.outOfFrame = True
CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
tdrstyle.setTDRStyle()



def compareSampleSetEfficiency():
    print ">>>\n>>> compareSampleSetEfficiency()"
    
    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    
    cutflowLT = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "lepton",   "lepton-tau",
                    #"trigger matching" , "no cuts (weighted)",
    ]
    cutflowEM = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "muon",     "electron",     "lepton pair",
                    #, "no cuts (weighted)",
    ]
    cutflowMM = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "muon",   "muon pair",
                    #, "no cuts (weighted)",
    ]
               
    cutsLT = [
        ("lepton-tau",      "channel>0"),
        ("iso_1<0.15",      "channel>0 && iso_1<0.15"),
        ("iso_2==1",        "channel>0 && iso_1<0.15 && iso_2==1"),
        ##("iso cuts",        "channel>0 && iso_1<0.15 && iso_2==1"),
        ("lepton vetos",    "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0"),
        ("opp. sign",       "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0"),
        ("ncbtag>0",        "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("nfjets>0",        "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0"),
        ("ncjets==1",       "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1"),
        ("ncbtag>0",        "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("ncjets==2",       "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2"),
        ("nfjets==0",       "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0"),
        ("dphi_ll_bj>2",    "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2"),
        ("met<60",          "channel>0 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2 && met<60"),
    ]
    cutsEM = [
        ("emu",             "channel>0"),
        ("iso_1<0.20",      "channel>0 && iso_1<0.20"),
        ("iso_2<0.15",      "channel>0 && iso_1<0.20 && iso_2<0.15"),
        ("lepton vetos",    "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0"),
        ("opp. sign",       "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0"),
        ("ncbtag>0",        "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0"),
        ("nfjets>0",        "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0"),
        ("ncjets==1",       "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1"),
        ("ncbtag>0",        "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0"),
        ("ncjets==2",       "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2"),
        ("nfjets==0",       "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0"),
        ("dphi_ll_bj>2",    "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2"),
        ("met<60",          "channel>0 && iso_1<0.20 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2 && met<60"),
    ]
    cutsMM = [
        ("mumu",            "channel>0"),
        ("iso_1<0.15",      "channel>0 && iso_1<0.15"),
        ("iso_2<0.15",      "channel>0 && iso_1<0.15 && iso_2<0.15"),
        ("lepton vetos",    "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0"),
        ("opp. sign",       "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0"),
        ("ncbtag>0",        "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0"),
        ("nfjets>0",        "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0"),
        ("ncjets==1",       "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1"),
        ("ncbtag>0",        "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0"),
        ("ncjets==2",       "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2"),
        ("nfjets==0",       "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0"),
        ("dphi_ll_bj>2",    "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2"),
        ("met<60",          "channel>0 && iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2 && met<60"),
    ]
    
    # TTbar CR
    cutsTT = [
        ("iso cuts",        "channel>0 && iso_cuts==1"),
        ("lepton vetos",    "channel>0 && iso_cuts==1 && lepton_vetos==0"),
        ("opp. sign",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
        # CATEGORY 1
        ("ncbtag>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("nfjets>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0"),
        ("ncjets==1",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1"),
        ("met<60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1 && met<60"),
        ("pfmt_1<60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1 && met<60 && pfmt_1<60"),
        # CATEGORY 1 TT CR 1
        ("ncbtag>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("nfjets>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0"),
        ("ncjets==1",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1"),
        ("met>60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1 && met>60"),
        ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && nfjets>0 && ncjets==1 && met>60 && pfmt_1>60"),
        # CATEGORY 1 TT CR 2
        ("ncbtag>1",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1"),
        ("nfjets>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets>0"),
        ("met>60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets>0 && met>60"),
        ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets>0 && met>60 && pfmt_1>60"),
        # CATEGORY 2
        ("ncbtag>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("ncjets>1",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1"),
        ("nfjets==0",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
        ("met<60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0 && met<60"),
        ("pfmt_1<60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0 && met<60 && pfmt_1<60"),
        # CATEGORY 2 TT CR 1
        ("ncbtag>0",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0"),
        ("ncjets>1",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1"),
        ("nfjets==0",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
        ("met>60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0 && met>60"),
        ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0 && met>60 && pfmt_1>60"),
        # CATEGORY 2 TT CR 2
        ("ncbtag>1",        "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1"),
        ("nfjets==0",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets==0"),
        ("met>60",          "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets==0 && met>60"),
        ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets==0 && met>60 && pfmt_1>60"),
            ]
    
    samples_sets = [
#            [ "Low mass samples",
#             [   ("LowMass",     "LowMass_30GeV_DiTauResonance",         "mutau" ),
#                 ("LowMass",     "LowMass_30GeV_DiTauResonance",         "etau"  ),
#                 ("LowMass",     "LowMass_30GeV_DiTauResonance",         "emu"   ),
#                 ("LowMass",     "LowMass_30GeV_DiMuResonance_8TeV",     "mumu 8TeV" ),
#                 ("LowMass",     "LowMass_30GeV_DiMuResonance_13TeV",    "mumu 13TeV" ),
#                     ]],
           [ "ttbar and sample",
            [   ("TT",          "TT_TuneCUETP8M1",                      "ttbar"    ),
                ("LowMass",     "LowMass_30GeV_DiTauResonance",         "low mass" ), ]],
#            [ "Low Mass DiTau",
#             [   ("LowMass",    "LowMass_30GeV_DiTauResonance",          "M-28" ), ]],
#            [ "SUSYGluGluToBBa1ToTauTau",
#             [   ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-25",            "M-25"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-30",            "M-30"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-35",            "M-35"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-40",            "M-40"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-45",            "M-45"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-50",            "M-50"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-55",            "M-55"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-60",            "M-60"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-65",            "M-65"  ),
#                 ("SUSY",    "SUSYGluGluToBBa1ToTauTau_M-70",            "M-70"  ), ]],
#            [ "SUSYGluGluToHToAA_AToBB_AToTauTau",
#             [   ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-15",   "M-15"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-20",   "M-20"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-25",   "M-25"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-30",   "M-30"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-35",   "M-35"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-40",   "M-40"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45",   "M-45"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-50",   "M-50"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-55",   "M-55"  ),
#                 ("SUSY",    "SUSYGluGluToHToAA_AToBB_AToTauTau_M-60",   "M-60"  ), ]],
#            [ "SUSYVBFToHToAA_AToBB_AToTauTau",
#             [   ("SUSY",    "SUSYVBFToHToAA_AToBB_AToTauTau_M-20",      "M-20" ),
#                 ("SUSY",    "SUSYVBFToHToAA_AToBB_AToTauTau_M-40",      "M-40" ),
#                 ("SUSY",    "SUSYVBFToHToAA_AToBB_AToTauTau_M-60",      "M-60" ), ]],
#            [ "DY M-10to50",
#             [   ("DY",      "DYJetsToLL_M-10to50_TuneCUETP8M1",         "incl." ),
#                 ("DY",      "DY1JetsToLL_M-10to50_TuneCUETP8M1",        "1Jet"  ),
#                 ("DY",      "DY2JetsToLL_M-10to50_TuneCUETP8M1",        "2Jets" ),
#                 ("DY",      "DY3JetsToLL_M-10to50_TuneCUETP8M1",        "3Jets" ),
#                                                                                     ]],
#            [ "DY-M50",
#             [   ("DY",      "DYJetsToLL_M-50_TuneCUETP8M1",             "incl." ),
#                 ("DY",      "DY1JetsToLL_M-50_TuneCUETP8M1",            "1Jet"  ),
#                 ("DY",      "DY2JetsToLL_M-50_TuneCUETP8M1",            "2Jets" ),
#                 ("DY",      "DY3JetsToLL_M-50_TuneCUETP8M1",            "3Jets" ),
#                                                                                     ]],
                ]
    
    # oppsign = [i for i,c in enumerate(cuts) if "opp. sign" in c[0]] # list
    # if oppsign: oppsign = min(oppsign) # index
    # else: oppsign = 0 # index
    cutsLT = cutsTT
    for setname,samples in samples_sets:
        print ">>> sample set %s" % (setname)
        header      = ">>> %13s:"%("samples")
        table_hist  = [">>> %13s:"%cut  for cut in cutflowLT]
        table_tree  = [">>> %13s:"%name for name, cut in cutsLT]
        for sampledir,sample,shortname in samples:
            
            (SAMPLE_DIR,cutflow,cuts,channel) = (MORIOND_DIR,cutflowLT,cutsLT,"mutau") # cutsTT / cutsLT
            if  "etau" in shortname: (SAMPLE_DIR,cutflow,cuts,channel) = (MORIOND_DIR,cutflowLT,cutsLT,"etau") # cutsTT / cutsLT
            if  "emu"  in shortname: (SAMPLE_DIR,cutflow,cuts,channel) = (EM_DIR,cutflowEM,cutsEM,"emu")
            if "mumu"  in shortname: (SAMPLE_DIR,cutflow,cuts,channel) = (MM_DIR,cutflowMM,cutsMM,"mumu")
            filename = "%s/%s/TauTauAnalysis.%s_Moriond.root" % (SAMPLE_DIR,sampledir,sample)
            print ">>>   loading %s (%s)..." % (shortname,filename)
            
            cutlabel = ""
            if "tau" in channel: cutlabel = "_cut"
            
            file = TFile(filename)
            hist = file.Get("histogram_%s/cutflow_%s"%(channel,channel))
            tree = file.Get("tree_%s%s"%(channel,cutlabel))
            
            length = max(floor(log(hist.GetBinContent(1),10)),len(shortname),8)+1
            formatter_s = "%%s %%%ds"%(length)
            formatter_d = "%%s %%%dd"%(length)
            
            header = formatter_s % (header,shortname)
        
            efficiencies_hist = getEfficienciesFromHistogram(hist,cutflow)
            if "emu" in shortname: efficiencies_hist = efficiencies_hist[:5]+efficiencies_hist[6:]
            for i,(row, eff) in enumerate(zip(table_hist,efficiencies_hist)):
                table_hist[i] = (formatter_d%(row,eff[1]))#.replace("100.000","  100.0")#.rstrip('0').rstrip('.')
            
            efficiencies_tree = getEfficienciesFromTree(tree,cuts,N=hist.GetBinContent(1))
            for i,(row, eff) in enumerate(zip(table_tree,efficiencies_tree)):
                table_tree[i] = (formatter_d%(row,eff[1]))#.replace("100.000","  100.0")#.rstrip('0').rstrip('.')
        
        # PRINT hist table
        print ">>>\n>>>\n>>> %s %s" % (setname,"cutflow")    
        print header
        for i,row in enumerate(table_hist):
            if i in [1,3]: continue
            print row

        # PRINT tree table
        for i,row in enumerate(table_tree):
            if "btag" in row:
                print ">>> "+'-'*(len(row)-4)
            print row
    
    print ">>>"



def compareOldToNewEfficiency():
    print ">>>\n>>> compareOldToNewEfficiency()"
    
    cutflowLT = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "lepton",   "lepton-tau",
                    #"trigger matching" , "no cuts (weighted)",
    ]
    cutflowEM = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "muon",     "electron",     "lepton pair",
                    #"no cuts (weighted)",
    ]
    cutflowMM = [   "no cuts",  "JSON",
                    "triggers", "MET filters",
                    "muon",   "muon pair",
                    #, "no cuts (weighted)",
    ]
    cutflow = cutflowEM
    
    cuts = [
        ("lep-tau",         "channel>0"),
        ("pt_1>23",         "channel>0 && pt_1>23"),
        ("iso_1<0.15",      "channel>0 && pt_1>23 && iso_1<0.15"),
        ("iso_2==1",        "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1"),
        ("lepton vetos",    "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0"),
        ("q_1*q_2<0",       "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0"),
        ("q_1*q_2>0",       "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0"),
        #("triggers",        "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0 && (triggers==1 || triggers==3)"),
        #("triggers",       "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0 &&  triggers==1"),
        #("againstEle",      "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0")
        #("againstMuon",     "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0"),
        #("lepton vetos",    "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0 && "),
    ]
    cuts        = [ ]
    oldcuts     = cuts
    newcuts     = cuts #[(n,c+" && triggers==1" if i>1 else c) for i,(n,c) in enumerate(cuts)] 
    
    OLD_DIR     = "/scratch/ytakahas/SFrameAnalysis/AnalysisOutputEM"
    NEW_DIR     = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM"
    newlabel    = "_Moriond" #"_ICHEP"
    oldlabel    = "_Moriond"
    
    histname    = "histogram_emu/cutflow_emu"
    treename    = "tree_emu"
    
    samples = [
        #("WJ",          "WJetsToLNu_TuneCUETP8M1"           ),
        #("WJ",          "W1JetsToLNu_TuneCUETP8M1"          ),
        #("WJ",          "W2JetsToLNu_TuneCUETP8M1"          ),
        ("DY",          "DYJetsToLL_M-10to50_TuneCUETP8M1"  ),
        #("DY",          "DY1JetsToLL_M-10to50_TuneCUETP8M1" ),
        #("DY",          "DY2JetsToLL_M-10to50_TuneCUETP8M1" ),
        #("DY",          "DY3JetsToLL_M-10to50_TuneCUETP8M1" ),
        ("DY",          "DYJetsToLL_M-50_TuneCUETP8M1"      ),
        #("DY",          "DY1JetsToLL_M-50_TuneCUETP8M1"     ),
        #("DY",          "DY2JetsToLL_M-50_TuneCUETP8M1"     ),
        #("DY",          "DY3JetsToLL_M-50_TuneCUETP8M1"     ),
        #("DY",          "DY4JetsToLL_M-50_TuneCUETP8M1"     ),
        ("TT",          "TT_TuneCUETP8M1"                   ),
        #("SingleMuon",  "SingleMuon_Run2016"                ),
        ("MuonEG",      "MuonEG_Run2016"                    ),
    ]
    
    print ">>>   old: %s\n>>>   new: %s" % (OLD_DIR,NEW_DIR)    
    for sampledir,sample in samples:
        print ">>>\n>>> old/new comparison for \"%s\"" % (sample)
        
        file1 = TFile("%s/%s/TauTauAnalysis.%s%s.root" % (OLD_DIR,sampledir,sample,oldlabel))
        file2 = TFile("%s/%s/TauTauAnalysis.%s%s.root" % (NEW_DIR,sampledir,sample,newlabel))
        hist1 = file1.Get(histname)
        hist2 = file2.Get(histname)
        tree1 = file1.Get(treename)
        tree2 = file2.Get(treename)
        
        #print ">>> ratio new/old = 35.9/12.9 = %.2g" % (35.9/12.9)
        efficiencies_hist1 = getEfficienciesFromHistogram(hist1,cutflow)
        efficiencies_hist2 = getEfficienciesFromHistogram(hist2,cutflow)
        print ">>> histogram cutflow:"
        printComparingCutflow(efficiencies_hist1,efficiencies_hist2)
        
        efficiencies_tree1 = getEfficienciesFromTree(tree1,oldcuts,N=hist1.GetBinContent(1))
        efficiencies_tree2 = getEfficienciesFromTree(tree2,newcuts,N=hist2.GetBinContent(1))
        print ">>>\n>>> tree cutflow:"
        printComparingCutflow(efficiencies_tree1,efficiencies_tree2)
    
    print ">>>"





def compareTriggerEfficiencies():
    print ">>>\n>>> compareTriggerEfficiency()"
    
    channel = "mutau"
    
    cutflow = [ "no cuts",
                "JSON",
                "triggers",
                "MET filters",
                "lepton",
                "lepton-tau",
                #"no cuts (weighted)",
               ]
    
    cuts = [    ("lep-tau",         "channel>0"),
                ("triggers",        "channel>0"),
                ("iso cuts",        "channel>0 && iso_cuts==1"),
                ("lepton vetos",    "channel>0 && iso_cuts==1 && lepton_vetos==0"),
                ("q_1*q_2<0",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
                ("nbtag>0",         "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && nbtag>0"),
            ]
    
    triggers    = "abs(eta_1)<2.1 &&   pt_1>23 && (triggers==1||triggers==3)"        
    xtriggers   = "abs(eta_1)<2.1 && ((pt_1>23 && (triggers==1||triggers==3))||(pt_1>21 && triggers>1))"
#     if "etau" in channel:
#         triggers    = "abs(eta_1)<2.1 &&   pt_1>26 && (triggers==1||triggers==3)"        
#         xtriggers   = "abs(eta_1)<2.1 && ((pt_1>26 && (triggers==1||triggers==3))||(pt_1>25 && triggers>1))"
    
    oldcuts = [(n,"%s && %s"%(c, triggers) if i>0 else c) for i,(n,c) in enumerate(cuts)]
    newcuts = [(n,"%s && %s"%(c,xtriggers) if i>0 else c) for i,(n,c) in enumerate(cuts)]
    
    samples = [
                    ("LowMass",     "LowMass_30GeV_DiTauResonance"  ),
                    #("WJ",          "WJetsToLNu_TuneCUETP8M1"       ),
                    #("DY",          "DYJetsToLL_M-50_TuneCUETP8M1"  ),
                    #("SingleMuon",  "SingleMuon_Run2016"            ),
                ]
    
    for sampledir,sample in samples:
        print ">>>\n>>> single lepton - crosstrigger comparison for \"%s\"" % (sample)
        
        file  = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (MORIOND_DIR, sampledir,sample))
        hist1 = file.Get("histogram_mutau/cutflow_mutau")
        hist2 = file.Get("histogram_mutau/cutflow_mutau")
        tree1 = file.Get("tree_%s"%channel)
        tree2 = file.Get("tree_%s"%channel)
        
        efficiencies_hist1 = getEfficienciesFromHistogram(hist1,cutflow)
        efficiencies_hist2 = getEfficienciesFromHistogram(hist2,cutflow)
        print ">>> histogram cutflow:"
        printComparingCutflow(efficiencies_hist1,efficiencies_hist2)
        
        efficiencies_tree1 = getEfficienciesFromTree(tree1,oldcuts,N=hist1.GetBinContent(1))
        efficiencies_tree2 = getEfficienciesFromTree(tree2,newcuts,N=hist2.GetBinContent(1))
        print ">>>\n>>> tree cutflow:"
        printComparingCutflow(efficiencies_tree1,efficiencies_tree2)
    
    print ">>>"




def compareDataSetEfficiencies():
    print ">>>\n>>> compareDataSetEfficiencies()"
    
    cutflow = [ "no cuts",
                "JSON",
                "triggers",
                "MET filters",
                "lepton",
                "lepton-tau",
               ]
    
    triggers = "(triggers==1||triggers==3)"
    cuts = [    ("no cuts",         "channel>0"),
                ("triggers",        "channel>0 && %s" % triggers),
                ("pt_1>23",         "channel>0 && %s && pt_1>23" % triggers),
                ("iso_1<0.15",      "channel>0 && %s && pt_1>23 && iso_1<0.15" % triggers),
                ("iso_2==1",        "channel>0 && %s && pt_1>23 && iso_1<0.15 && iso_2==1" % triggers),
                ("lepton vetos",    "channel>0 && %s && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0" % triggers),
                ("q_1*q_2<0",       "channel>0 && %s && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2<0" % triggers),
                ("q_1*q_2>0",       "channel>0 && %s && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0" % triggers),
                #("triggers",        "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0 && (triggers==1 || triggers==3)"),
                #("triggers",       "channel>0 && pt_1>23 && iso_1<0.15 && iso_2==1 && lepton_vetos==0 && q_1*q_2>0 &&  triggers==1"),
                #("againstEle",      "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0")
                #("againstMuon",     "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0"),
                #("lepton vetos",    "channel>0 && pt_1>23 && iso_2==1 && lepton_vetos==0 && "),
            ]
    
    datasets_dict = {   'B':    (272007,275376, 5.788348),
                        'C':    (275657,276283, 2.573399),
                        'D':    (276315,276811, 4.248384),
                        'E':    (276831,277420, 4.009132),
                        'F':    (277772,278808, 3.101618),
                        'G':    (278820,280385, 7.540488),
                        'H':    (280919,284044, 8.605690),
                        'BtoF': (272007,278808,19.720881),
                        'BtoG': (272007,280385,27.261369),
                        'GH':   (278820,284044,16.146178),
                    }
    
    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    samples      = [("SingleMuon",  "SingleMuon_Run2016"),]
    datasets     = [ 
                     ( 'G',    'H'  ),
                     ( 'BtoF', 'H'  ),
                     ( 'BtoF', 'GH' ),
                     ( 'BtoG', 'H'  ),
                    ]
    
    for sampledir,sample in samples:
        for dataset1, dataset2 in datasets:

            (start1,end1,lumi1) = datasets_dict[dataset1]
            (start2,end2,lumi2) = datasets_dict[dataset2]
            period1 = "%d<run && run<%d" % (start1-1,end1+1)
            period2 = "%d<run && run<%d" % (start2-1,end2+1)
            cuts1   = [(n,"%s && %s"%(c,period1)) for n,c in cuts]
            cuts2   = [(n,"%s && %s"%(c,period2)) for n,c in cuts]
    
            print ">>>\n>>> %s vs. %s comparison for \"%s\"" % (dataset1,dataset2,sample)
            print ">>> %-6s: %17s  (%.2f/fb)" % (dataset1,period1,lumi1)
            print ">>> %-6s: %17s  (%.2f/fb)" % (dataset2,period2,lumi2)
        
            file1 = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (MORIOND_DIR,sampledir,sample))
            #hist1 = file1.Get("histogram_mutau/cutflow_mutau")
            tree1 = file1.Get("tree_mutau")
            
            print ">>> ratio %s / %s = %.3f/%.3f = %.3f" % (dataset1,dataset2,lumi1,lumi2,lumi1/lumi2)
            print ">>> ratio %s / %s = %.3f/%.3f = %.3f" % (dataset2,dataset1,lumi2,lumi1,lumi2/lumi1)
            #efficiencies_hist1 = getEfficienciesFromHistogram(hist1,cutflow)
            #efficiencies_hist2 = getEfficienciesFromHistogram(hist2,cutflow)
            #print ">>> histogram cutflow:"
            #printComparingCutflow(efficiencies_hist1,efficiencies_hist2)
            
            efficiencies_tree1 = getEfficienciesFromTree(tree1,cuts1)
            efficiencies_tree2 = getEfficienciesFromTree(tree1,cuts2)
            print ">>>\n>>> tree cutflow:"
            printComparingCutflow(efficiencies_tree1,efficiencies_tree2)
    
    print ">>>"





def writeRunNumbers():
    print ">>>\n>>> writeRunNumbers()"
    
    channel     = "emu"
    emu_check   = "channel>0 && njets==2 && pt_1>25 && pt_2>25 && abs(eta_1)<2.1 && abs(eta_2)<2.1 && iso_1<0.10 && q_1*q_2<0 && 70<m_vis&&m_vis<110"
    DIR         = MORIOND_DIR
    
    if "emu" in channel:
        DIR = DIR.replace("AnalysisOutput","AnalysisOutputEM")
    
    cuts = [    
                ("2j0b",    "%s && %s"  % ("ncbtag==0",emu_check)),
                ("2j",      "%s"        % (emu_check)),
    ]
    
    samples = [
                    #("SingleMuon",  "SingleMuon_Run2016"    ),
                    ("MuonEG",  "MuonEG_Run2016"            ),
    ]
    
    for sampledir, sample in samples:
        print ">>>\n>>> writing run, lumi, event number for %s" % (sample)
    
        file    = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (DIR, sampledir,sample))
        tree    = file.Get("tree_%s"%channel)
        
        for cutname, cut in cuts:
            print ">>> cut \"%s\": \"%s\"" % (cutname,cut)
            
            txtname = "%s/runnumber_%s.txt" % (OUT_DIR,cutname.replace(', ','-').replace(' ','_').replace(':','-').replace('(','').replace(')','').replace('#','').replace('<','lt').replace('>','gt')) 
            #print ">>> %d entries passing the cut"%(tree.GetEntries(cut))
            tree.GetPlayer().SetScanRedirect(True)
            tree.GetPlayer().SetScanFileName(txtname)
            N = tree.Scan("run:lum:evt", cut, "precision=10") #, "colsize=20"
            
            with open(txtname,'r') as txtfile0: data = txtfile0.read()
            with open(txtname,'w') as txtfile1: txtfile1.write(("# %d events with \"%s\" selections:\n#   %s\n\n"%(N,cutname,cut))+data)
            
            
    
    print ">>>"

                



def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR





def main():
    print ""
    
    makeDirectory(OUT_DIR)
    
    # MAIN CHECKS
    #compareOldToNew()
#     compareDataSetEfficiencies()
#     compareTriggerEfficiencies()
#     compareSampleSetEfficiency()
#     compareOldToNewEfficiency()
    writeRunNumbers()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()
