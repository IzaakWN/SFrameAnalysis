#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
import PlotTools.PlotTools
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.SampleTools import getEfficienciesFromHistogram, getEfficienciesFromTree
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
    
    cutflow = [ "no cuts",
                "JSON",
                "triggers",
                "MET filters",
                "lepton",
                "lepton-tau",
                #"no cuts (weighted)",
               ]
    
    cuts = [    ("lep-tau",         "channel>0"),
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
    oldcuts = cuts
    newcuts = cuts #[(n,c+" && triggers==1" if i>1 else c) for i,(n,c) in enumerate(cuts)] 
    
    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    ICHEP_DIR    = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    
    samples = [
                    #("WJ",          "WJetsToLNu_TuneCUETP8M1"       ),
                    #("DY",          "DYJetsToLL_M-50_TuneCUETP8M1"  ),
                    ("SingleMuon",  "SingleMuon_Run2016"            ),
                ]
    
    for sampledir,sample in samples:
        print ">>>\n>>> ICHEP - Moriond comparison for \"%s\"" % (sample)
        
        file1 = TFile( "%s/%s/TauTauAnalysis.%s_ICHEP.root"   % (ICHEP_DIR,  sampledir,sample))
        file2 = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (MORIOND_DIR,sampledir,sample))
        hist1 = file1.Get("histogram_mutau/cutflow_mutau")
        hist2 = file2.Get("histogram_mutau/cutflow_mutau")
        tree1 = file1.Get("tree_mutau")
        tree2 = file2.Get("tree_mutau")
        
        print ">>> ratio Moriond/ICHEP = 35.9/12.9 = %.2g" % (35.9/12.9)
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
#     compareOldToNewEfficiency()
#     compareDataSetEfficiencies()
#     compareTriggerEfficiencies()
    compareSampleSetEfficiency()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()


 
# def signalEfficiency():
#     print ">>>\n>>> signalEfficiency()"
# 
#     # bin 1: no cuts
#     # bin 2: JSON / gen weight
#     # bin 3: triggers
#     # bin 4: MET filters
#     # bin 5: lepton selection
#     # bin 6: lepton-tau pair selection
#     # bin 7: no cuts gen weighted
#     
#     cuts = [    "no cuts",
#                 "JSON/weight",
#                 "triggers",
#                 "MET filters",
#                 "lepton",
#                 "lepton-tau",
#                 "no cuts (weighted)",
#             ]
#     
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     efficiencies = [ ]
#     for i, cut in zip(range(1,len(cuts)+1),cuts):
#         N = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i)
#         N_tot = 0
#         if i is 1:
#             N = 1
#             N_tot = 1
#         else:
#             N_tot = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i-1)
#             
#         if N and N_tot:
#             efficiencies.append(( cut, N / N_tot ))
#         else:
#             print ">>> Warning: GetBinContent(%i) = %s, GetBinContent(%i) = %s " % (i,N,i-1,N_tot)
#     
#     for cut, efficiency in efficiencies:
#         print ">>> %s: %5.2f%%" % (cut,efficiency*100)



# def ptSignalAcceptence():
#     print ">>>\n>>> ptSignalAcceptence()"
# 
#     cut = 23. 
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     pt_taus = file.Get("checks/pt_gentaus")
#     pt_tau1 = file.Get("checks/pt_gentau1")
#     pt_tau2 = file.Get("checks/pt_gentau2")
#     pt_muon = file.Get("checks/pt_genmuon")
#     
#     bincut_taus = pt_taus.FindBin(cut)
#     bincut_tau1 = pt_tau1.FindBin(cut)
#     bincut_tau2 = pt_tau2.FindBin(cut)
#     bincut_muon = pt_muon.FindBin(cut)
#     N_taus = pt_taus.Integral()
#     N_tau1 = pt_tau1.Integral()
#     N_tau2 = pt_tau2.Integral()
#     N_muon = pt_muon.Integral()
#     
#     eff_taus = pt_taus.Integral(bincut_taus, pt_taus.GetNbinsX()) / N_taus
#     eff_tau1 = pt_tau1.Integral(bincut_tau1, pt_tau1.GetNbinsX()) / N_tau1
#     eff_tau2 = pt_tau2.Integral(bincut_tau2, pt_tau2.GetNbinsX()) / N_tau2
#     eff_muon = pt_muon.Integral(bincut_muon, pt_muon.GetNbinsX()) / N_muon
#     
#     print ">>> efficiency of pt cut of %s on signal's gen tau and reco muon:" % cut
#     print ">>> gen tau:  %5.2f%%" % (100*eff_taus)
#     print ">>> gen tau1: %5.2f%%" % (100*eff_tau1)
#     print ">>> gen tau2: %5.2f%%" % (100*eff_tau2)
#     print ">>> gen muon: %5.2f%%" % (100*eff_muon)
# 
#     print ">>> check: bincut_taus = %3i,  N_taus =%7i" % (bincut_taus,N_taus)
#     print ">>> check: bincut_tau2 = %3i,  N_tau1 =%7i" % (bincut_tau1,N_tau1)
#     print ">>> check: bincut_tau3 = %3i,  N_tau2 =%7i" % (bincut_tau2,N_tau2)
#     print ">>> check: bincut_muon = %3i,  N_muon =%7i" % (bincut_muon,N_muon)
#     
#     # DRAW
#     canvas = TCanvas("canvas","canvas",100,100,800,600) # 600,600
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     pt_taus.SetLineWidth(3)
#     pt_muon.SetLineWidth(3)
#     pt_taus.SetLineColor(kAzure+4)
#     pt_muon.SetLineColor(kRed+3)
#     pt_taus.Scale(1/N_taus)
#     pt_muon.Scale(1/N_muon/3)
#     #pt_taus.Rebin(2)
#     #pt_muon.Rebin(2)
#     pt_taus.Draw("hist")
#     pt_muon.Draw("histsame")
#     pt_taus.SetTitle("")
#     pt_taus.GetXaxis().SetRangeUser(0,100)
#     pt_taus.GetXaxis().SetTitle("p_{T} of generator level particle")
#     pt_taus.GetYaxis().SetTitle("A.U.")
#     #pt_taus.GetYaxis().SetTitleSize(0)
#     pt_taus.GetXaxis().SetTitleSize(0.05)
#     pt_taus.GetYaxis().SetTitleSize(0.05)
#     pt_taus.GetXaxis().SetTitleOffset(1.14)
#     pt_taus.GetYaxis().SetTitleOffset(1.17)
#     pt_taus.GetXaxis().SetLabelSize(0.045)
#     pt_taus.GetYaxis().SetLabelSize(0.040)
#     #pt_taus.GetYaxis().SetLabelSize(0)    
#     legend = TLegend(0.56,0.68,0.80,0.84)
#     legend.AddEntry(pt_taus, " gen #tau", 'l')
#     legend.AddEntry(pt_muon, " gen #mu from #tau", 'l')
#     legend.SetTextSize(0.055)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     #gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/pt.png")
#     canvas.Close()



# def DYAcceptence():
#     print ">>>\n>>> DYAcceptence()"
# 
#     DIR2 = "/shome/ineuteli/analysis/SFrameAnalysis/TauTauResonances/"
# 
# #     file = TFile( DIR2 + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
#     file = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-10to50_TuneCUETP8M1%s.root" % mylabel )
#     pt = file.Get("checks/pt_muon")
#     d0 = file.Get("checks/d0_muon")
#     dz = file.Get("checks/dz_muon")
#     d0_cut = file.Get("checks/d0_muon_cut")
#     dz_cut = file.Get("checks/dz_muon_cut")
# #     file2 = TFile( DIR2 + "TauTauAnalysis.DYJets_M-50.UZH.root" )
#     file2 = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1%s.root" % mylabel )
#     pt2 = file2.Get("checks/pt_muon")
#     d02 = file2.Get("checks/d0_muon")
#     dz2 = file2.Get("checks/dz_muon")
#     d02_cut = file2.Get("checks/d0_muon_cut")
#     dz2_cut = file2.Get("checks/dz_muon_cut")
#     var_dict = { "pt_muon":"muon p_{T}", "d0_muon":"muon d0", "dz_muon":"muon |dz|",
#                  "d0_muon_cut":"muon d0", "dz_muon_cut":"muon |dz|" }
#     
#     print ">>>\n>>> overflow DY check"
#     print ">>> DY M-10to50 pt overflow:              %9i /%9i = %5.1f%%" % ( pt.GetBinContent(pt.GetNbinsX()+1),   pt.GetEntries(),  pt.GetBinContent(pt.GetNbinsX()+1)   /  pt.GetEntries()*100 )
#     print ">>> DY M-50     pt overflow:              %9i /%9i = %5.1f%%" % ( pt2.GetBinContent(pt2.GetNbinsX()+1), pt2.GetEntries(), pt2.GetBinContent(pt2.GetNbinsX()+1) / pt2.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow:              %9i /%9i = %5.1f%%" % ( d0.GetBinContent(d0.GetNbinsX()+1),   d0.GetEntries(),  d0.GetBinContent(d0.GetNbinsX()+1)   / d0.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow:              %9i /%9i = %5.1f%%" % ( d02.GetBinContent(d02.GetNbinsX()+1), d02.GetEntries(), d02.GetBinContent(d02.GetNbinsX()+1) / d02.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d0_cut.GetBinContent(d0_cut.GetNbinsX()+1),   d0_cut.GetEntries(),  d0_cut.GetBinContent(d0_cut.GetNbinsX()+1)   / d0_cut.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d02_cut.GetBinContent(d02_cut.GetNbinsX()+1), d02_cut.GetEntries(), d02_cut.GetBinContent(d02_cut.GetNbinsX()+1) / d02_cut.GetEntries()*100 )
#     print ">>> DY M-10to50 dz overflow:              %9i /%9i = %5.1f%%" % ( dz.GetBinContent(dz.GetNbinsX()+1),   dz.GetEntries(),  dz.GetBinContent(dz.GetNbinsX()+1)   / dz.GetEntries()*100  )
#     print ">>> DY M-50     dz overflow:              %9i /%9i = %5.1f%%" % ( dz2.GetBinContent(dz2.GetNbinsX()+1), dz2.GetEntries(), dz2.GetBinContent(dz2.GetNbinsX()+1) / dz2.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz_cut.GetBinContent(dz_cut.GetNbinsX()+1),   dz_cut.GetEntries(),  dz_cut.GetBinContent(dz_cut.GetNbinsX()+1)   / dz_cut.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1), dz2_cut.GetEntries(), dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1) / dz2_cut.GetEntries()*100 )
#     
#     for var, hist, hist2 in [ ("pt_muon",pt,pt2), ("d0_muon",d0,d02), ("dz_muon",dz,dz2), ("d0_muon_cut",d0_cut,d02_cut), ("dz_muon_cut",dz_cut,dz2_cut) ]:
#         canvas = TCanvas("canvas","canvas",100,100,800,600)
#         canvas.SetBottomMargin(0.12)
#         canvas.SetRightMargin(0.05)
#         canvas.SetLeftMargin(0.05)
#         canvas.SetTopMargin(0.05)
#         hist.SetLineWidth(3)
#         hist.SetLineStyle(1)
#         hist.SetLineColor(kAzure+4)
#         hist2.SetLineWidth(3)
#         hist2.SetLineStyle(7)
#         hist2.SetLineColor(kRed+3)
#         hist.Draw("hist")
#         hist2.Draw("histsame")
#         hist.Scale(1/hist.Integral())
#         hist2.Scale(1/hist2.Integral())
#         hist.SetTitle("")
#         #hist.GetXaxis().SetRangeUser(0,100)
#         hist.GetXaxis().SetTitle(var_dict[var]) #replace
#         hist.GetYaxis().SetTitleSize(0)
#         hist.GetXaxis().SetTitleSize(0.05)
#         hist.GetXaxis().SetTitleOffset(1.15)
#         hist.GetXaxis().SetLabelSize(0.045)
#         hist.GetYaxis().SetLabelSize(0)
#         hist.GetYaxis().SetRangeUser(0,max(hist.GetMaximum(),hist2.GetMaximum())*1.12)
#         h = 0.18
#         w = 0.25
#         legend = TLegend(0.64,0.7,0.64-w,0.7-h)
#         legend.AddEntry(hist, " DY 10 < m < 50", 'l')
#         legend.AddEntry(hist2," DY 50 > m", 'l')
#         legend.SetTextSize(0.042)
#         legend.SetBorderSize(0)
#         legend.SetFillStyle(0)
#         legend.Draw()
#         gStyle.SetOptStat(0)
#         canvas.SaveAs("plots_check/%s.png" % var)
#         canvas.Close()
#         
#     vetos   = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
#     isocuts = "iso_1 < 0.15 && iso_2 == 1"
#     cuts    = [ ("SS",         "channel==1 && q_1*q_2<0"),
#                 ("iso",        "channel==1 && %s && q_1*q_2<0" % (isocuts)),
#                 #("isow",       "(channel==1 && %s && q_1*q_2<0)*idisoweight_1*trigweight_1" % (isocuts)),
#                 ("vetos",      "channel==1 && %s && %s && q_1*q_2<0" % (isocuts, vetos)),
#                 ("category 1", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets == 1 && nfjets  > 0" % (isocuts, vetos)),
#                 ("category 2", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets  > 1 && nfjets == 0 && dphi_ll_bj > 2 && met < 60" % (isocuts, vetos)),
#                ]
#     # TODO weights?
#     #  trigweight_1 * idisoweight_1 * trigweight_2 * idisoweight_2
#     
#     tree  = file.Get("tree_mutau")
#     tree2 = file2.Get("tree_mutau")
#     iso_1  = TH1F("iso_1", "iso_1", 100, -10, 10)
#     iso_12 = TH1F("iso_12", "iso_12", 100, -10, 10)
#     tree.Draw( "iso_1 >> iso_1",   "channel==1", "gOff")
#     tree2.Draw("iso_1 >> iso_12",  "channel==1", "gOff")
#     N_tot = iso_1.Integral()
#     N_tot2 = iso_12.Integral()
# 
#     print ">>>\n>>> cuts on DY:"
#     for label, cut in cuts: 
#         iso_1.Reset()
#         iso_12.Reset()
#         tree.Draw("iso_1 >> iso_1",   cut, "gOff")
#         tree2.Draw("iso_1 >> iso_12", cut, "gOff")
#         N  = iso_1.Integral() #GetEntries
#         N2 = iso_12.Integral()
#         print ">>> %s:" % label
#         if N_tot:  print ">>>   DY M-10to50: %4.1f%% (%6i,%6i)" % ( N/N_tot*100.0,   N,  N_tot  )
#         if N_tot2: print ">>>   DY M-50:     %4.1f%% (%6i,%6i)" % ( N2/N_tot2*100.0, N2, N_tot2 )
#         if "category" not in label and "isow" not in label:
#             N_tot  = N
#             N_tot2 = N2
#         
#     file.Close()
#     file2.Close()