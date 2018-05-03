#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2018)

print
from argparse import ArgumentParser
import os, sys, time
import copy
from math import sqrt, pow, floor, ceil
import ROOT
from ROOT import TFile, TH1D, THStack, TPaveText, TString, gDirectory, kAzure, kGreen, kRed
# from PlotTools import *
ROOT.gROOT.SetBatch(ROOT.kTRUE)

argv = sys.argv
description = """This script make plots."""
parser = ArgumentParser(prog="plotter",description=description,epilog="Succes!")
parser.add_argument( "-i", "--config", dest="configFile", type=str, default="", action='store',
                     metavar="CONFIG_FILE", help="name of config file containing the settings, samples, selections and variables" )
parser.add_argument( "-o", "--obs",    dest="obs", nargs='*', type=str, default=[], action='store',
                     metavar="MASS",   help="name of mass observable" )
parser.add_argument( "-c", "--channel", dest="channel", default="", action='store',
                     metavar="CHANNEL", help="run only for this channel" )
parser.add_argument( "-e", "--etau", dest="etau", default=False, action='store_true',
                     help="run only for the etau channel" )
parser.add_argument( "-m", "--mutau", dest="mutau", default=False, action='store_true',
                     help="run only for the mutau channel" )
parser.add_argument( "-u", "--emu", dest="emu", default=False, action='store_true',
                     help="run only for the emu channel" )
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                     help="renormalize W+Jets" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="make script verbose" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()
if not args.configFile:
    args.configFile = "PlotTools/config_emu2017.py" if args.emu else "PlotTools/config_ltau2017.py"

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
doStack = False; doDatacard = True; doTESscan = False; doFakeRate = False
normalizeWJ = normalizeWJ and not args.noWJrenorm
loadSettings(globals(),settings,verbose=args.verbose)
exec commands




    ##########################
    # checkDataCardHistogram #
    ##########################

def checkDataCardHistograms():
    """Plot histgrams for check."""
    print ">>> checkDataCardHistograms"
    
    filename    = "./datacards/ttbar_mt_tid_pfmt_1.inputs-13TeV_mtlt100.root"
    file        = TFile(filename)
    dirname     = "pass-loose"
    print ">>> checking %s:%s"%(filename,dirname)
    
    samplesB    = [ "QCD", "ZTT", "ZL", "VV", "W", "ST", "TTT", "TTJ" ][::-1]
    samplesD    = [ "data_obs" ]
    
    for i, histname in enumerate(samplesB):
        #print ">>> hist =",histname
        hist = file.Get("%s/%s"%(dirname,histname))
        hist.SetTitle(histname)
        hist.SetFillColor(getColor(histname))
        samplesB[i] = hist
    for i, histname in enumerate(samplesD):
        hist = file.Get("%s/%s"%(dirname,histname))
        hist.SetTitle(histname)
        samplesD[i] = hist
    
    plot = Plot(samplesD,samplesB,stack=True)
    plot.plot(ratio=True,staterror=True)
    plot.saveAs("test.png")
    



    ##########################
    # writeDataCardHistogram #
    ##########################

def writeDataCardHistograms(sampleset, channel, var, binWidth, a, b, **kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    
    verbosity   = kwargs.get('verbosity',   0               )
    filter      = kwargs.get('filter',      [ ]             )
    process     = kwargs.get('process',     "ttbar"         )
    analysis    = kwargs.get('analysis',    "tid"           )
    DIR         = kwargs.get('DIR',         DATACARDS_DIR   )
    recreate    = kwargs.get('recreate',    False           )
    label       = kwargs.get('label',       ""              ) # WEIGHTED
    su_label    = kwargs.get('su_label',    ""              )
    E           = kwargs.get('E',           "13TeV"         )
    JES         = kwargs.get('JES',         ""              )
    JER         = kwargs.get('JER',         ""              )
    UncEn       = kwargs.get('UncEn',       ""              )
    TES         = kwargs.get('TES',         ""              )
    TESscan     = kwargs.get('TESscan',     ""              )
    EES         = kwargs.get('EES',         ""              )
    LTF         = kwargs.get('LTF',         ""              )
    JTF         = kwargs.get('JTF',         ""              )
    Zpt         = kwargs.get('Zpt',         ""              )
    TTpt        = kwargs.get('TTpt',        ""              )
    QCD_WJ      = kwargs.get('QCD_WJ',      ""              )
    nBins       = int(kwargs.get('nBins',   (b-a)/binWidth ))
    option      = 'RECREATE' if recreate else 'UPDATE'
    doShift     = TES or EES or LTF or JTF or JES or JER or UncEn or Zpt or TTpt
    extraweight = ""
    
    # SELECTIONS
    iso1        = "iso_1<0.15" if "mutau" in channel else "iso_1<0.10"
    iso2        = "iso_2==1"
    vetos       = "lepton_vetos==0"
    baseline    = "%s && %s && %s && q_1*q_2<0 && decayMode_2<11" % (iso1,iso2,vetos)
    if "emu" in channel:
      vetos     = "extraelec_veto==0 && extramuon_veto==0"
      iso1      = "iso_1<0.20 && iso_2<0.15"
      baseline  = "%s && %s && q_1*q_2<0 && decayMode_3<11" % (iso1,vetos)
    
    selectionsDC = [ ] 
    
    #if "emu" not in channel:
    #  tauID = {
    #    ('','iso_2_%s'):                                     [ 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight' ],
    #    ('MVAOldV2','by%sIsolationMVArun2v1DBoldDMwLT_2'):   [ 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight' ],
    #    ('MVANewV2','by%sIsolationMVArun2v2DBoldDMwLT_2'):   [ 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight' ],
    #    ('cut','by%sCombinedIsolationDeltaBetaCorr3Hits_2'): [ 'VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight' ],
    #  }
    #  for (key,ID), WPs in tauID.iteritems():
    #    for WP in WPs:
    #      dirnameP = '-'.join(filter(None,['pass',key,WP.lower()]))
    #      dirnameF = '-'.join(filter(None,['fail',key,WP.lower()]))
    #      wpvar    = ID%WP
    #      selectionsDC.append((dirnameP,"%s && %s && q_1*q_2<0 && %s==1"%(iso1,vetos,"nbtag>0",wpvar)))
    #      selectionsDC.append((dirnameF,"%s && %s && q_1*q_2<0 && %s!=1"%(iso1,vetos,"nbtag>0",wpvar)))
    
    selectionsDC = [
      ### MVA-based V1 ###
      ("pass-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vloose==1"  )),
      ("fail-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vloose!=1"  )),
      ("pass-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_loose==1"   )),
      ("fail-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_loose!=1"   )),
      ("pass-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_medium==1"  )),
      ("fail-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_medium!=1"  )),
      ("pass-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2==1"         )),
      ("fail-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2!=1"         )),
      ("pass-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vtight==1"  )),
      ("fail-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vtight!=1"  )),
      ("pass-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vvtight==1" )),
      ("fail-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && iso_2_vvtight!=1" )),
      ### MVA-based V2 ###
      ("pass-MVAOldV2-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseIsolationMVArun2v2DBoldDMwLT_2==1"  )),
      ("fail-MVAOldV2-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseIsolationMVArun2v2DBoldDMwLT_2!=1"  )),
      ("pass-MVAOldV2-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseIsolationMVArun2v2DBoldDMwLT_2==1"   )),
      ("fail-MVAOldV2-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseIsolationMVArun2v2DBoldDMwLT_2!=1"   )),
      ("pass-MVAOldV2-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumIsolationMVArun2v2DBoldDMwLT_2==1"  )),
      ("fail-MVAOldV2-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumIsolationMVArun2v2DBoldDMwLT_2!=1"  )),
      ("pass-MVAOldV2-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightIsolationMVArun2v2DBoldDMwLT_2==1"   )),
      ("fail-MVAOldV2-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightIsolationMVArun2v2DBoldDMwLT_2!=1"   )),
      ("pass-MVAOldV2-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVTightIsolationMVArun2v2DBoldDMwLT_2==1"  )),
      ("fail-MVAOldV2-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVTightIsolationMVArun2v2DBoldDMwLT_2!=1"  )),
      ("pass-MVAOldV2-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVTightIsolationMVArun2v2DBoldDMwLT_2==1" )),
      ("fail-MVAOldV2-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVTightIsolationMVArun2v2DBoldDMwLT_2!=1" )),
      ### MVA-based V2 new DMs ###
      ("pass-MVANewV2-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseIsolationMVArun2v1DBnewDMwLT_2==1"  )),
      ("fail-MVANewV2-vloose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseIsolationMVArun2v1DBnewDMwLT_2!=1"  )),
      ("pass-MVANewV2-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseIsolationMVArun2v1DBnewDMwLT_2==1"   )),
      ("fail-MVANewV2-loose",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseIsolationMVArun2v1DBnewDMwLT_2!=1"   )),
      ("pass-MVANewV2-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumIsolationMVArun2v1DBnewDMwLT_2==1"  )),
      ("fail-MVANewV2-medium",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumIsolationMVArun2v1DBnewDMwLT_2!=1"  )),
      ("pass-MVANewV2-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightIsolationMVArun2v1DBnewDMwLT_2==1"   )),
      ("fail-MVANewV2-tight",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightIsolationMVArun2v1DBnewDMwLT_2!=1"   )),
      ("pass-MVANewV2-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVTightIsolationMVArun2v1DBnewDMwLT_2==1"  )),
      ("fail-MVANewV2-vtight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVTightIsolationMVArun2v1DBnewDMwLT_2!=1"  )),
      ("pass-MVANewV2-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVTightIsolationMVArun2v1DBnewDMwLT_2==1" )),
      ("fail-MVANewV2-vvtight",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVTightIsolationMVArun2v1DBnewDMwLT_2!=1" )),
      ### CUT-based ###
      ("pass-cut-vvloose", "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVLooseCombinedIsolationDeltaBetaCorr3Hits_2==1" )),
      ("fail-cut-vvloose", "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVVLooseCombinedIsolationDeltaBetaCorr3Hits_2!=1" )),
      ("pass-cut-vloose",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseCombinedIsolationDeltaBetaCorr3Hits_2==1"  )),
      ("fail-cut-vloose",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byVLooseCombinedIsolationDeltaBetaCorr3Hits_2!=1"  )),
      ("pass-cut-loose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseCombinedIsolationDeltaBetaCorr3Hits_2==1"   )),
      ("fail-cut-loose",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byLooseCombinedIsolationDeltaBetaCorr3Hits_2!=1"   )),
      ("pass-cut-medium",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumCombinedIsolationDeltaBetaCorr3Hits_2==1"  )),
      ("fail-cut-medium",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byMediumCombinedIsolationDeltaBetaCorr3Hits_2!=1"  )),
      ("pass-cut-tight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightCombinedIsolationDeltaBetaCorr3Hits_2==1"   )),
      ("fail-cut-tight",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag>0 && byTightCombinedIsolationDeltaBetaCorr3Hits_2!=1"   )),
    ]
    if "emu" in channel:
      selectionsDC = [
        ("emuCR",               "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0")),
        ###("notau-emuCR",         "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3<1")),
        ("pass-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBoldDMwLT_3==1"  )),
        ("fail-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBoldDMwLT_3!=1"  )),
        ("pass-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBoldDMwLT_3==1"   )),
        ("fail-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBoldDMwLT_3!=1"   )),
        ("pass-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBoldDMwLT_3==1"  )),
        ("fail-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBoldDMwLT_3!=1"  )),
        ("pass-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3==1"   )),
        ("fail-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3!=1"   )),
        ("pass-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBoldDMwLT_3==1"  )),
        ("fail-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBoldDMwLT_3!=1"  )),
        ("pass-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBoldDMwLT_3==1" )),
        ("fail-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBoldDMwLT_3!=1" )),
        ### MVA-based V2 ###
        ("pass-MVAOldV2-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v2DBoldDMwLT_3==1"  )),
        ("fail-MVAOldV2-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v2DBoldDMwLT_3!=1"  )),
        ("pass-MVAOldV2-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v2DBoldDMwLT_3==1"   )),
        ("fail-MVAOldV2-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v2DBoldDMwLT_3!=1"   )),
        ("pass-MVAOldV2-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v2DBoldDMwLT_3==1"  )),
        ("fail-MVAOldV2-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v2DBoldDMwLT_3!=1"  )),
        ("pass-MVAOldV2-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v2DBoldDMwLT_3==1"   )),
        ("fail-MVAOldV2-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v2DBoldDMwLT_3!=1"   )),
        ("pass-MVAOldV2-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v2DBoldDMwLT_3==1"  )),
        ("fail-MVAOldV2-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v2DBoldDMwLT_3!=1"  )),
        ("pass-MVAOldV2-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v2DBoldDMwLT_3==1" )),
        ("fail-MVAOldV2-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v2DBoldDMwLT_3!=1" )),
        ### MVA-based V2 new DMs ###
        ("pass-MVANewV2-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBnewDMwLT_3==1"  )),
        ("fail-MVANewV2-vloose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBnewDMwLT_3!=1"  )),
        ("pass-MVANewV2-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBnewDMwLT_3==1"   )),
        ("fail-MVANewV2-loose-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBnewDMwLT_3!=1"   )),
        ("pass-MVANewV2-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBnewDMwLT_3==1"  )),
        ("fail-MVANewV2-medium-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBnewDMwLT_3!=1"  )),
        ("pass-MVANewV2-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBnewDMwLT_3==1"   )),
        ("fail-MVANewV2-tight-emuCR",    "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBnewDMwLT_3!=1"   )),
        ("pass-MVANewV2-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBnewDMwLT_3==1"  )),
        ("fail-MVANewV2-vtight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBnewDMwLT_3!=1"  )),
        ("pass-MVANewV2-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBnewDMwLT_3==1" )),
        ("fail-MVANewV2-vvtight-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBnewDMwLT_3!=1" )),
        ### CUT-based ###
        ("pass-cut-vvloose-emuCR", "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3==1" )),
        ("fail-cut-vvloose-emuCR", "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3!=1" )),
        ("pass-cut-vloose-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseCombinedIsolationDeltaBetaCorr3Hits_3==1"  )),
        ("fail-cut-vloose-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byVLooseCombinedIsolationDeltaBetaCorr3Hits_3!=1"  )),
        ("pass-cut-loose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseCombinedIsolationDeltaBetaCorr3Hits_3==1"   )),
        ("fail-cut-loose-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byLooseCombinedIsolationDeltaBetaCorr3Hits_3!=1"   )),
        ("pass-cut-medium-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumCombinedIsolationDeltaBetaCorr3Hits_3==1"  )),
        ("fail-cut-medium-emuCR",  "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byMediumCombinedIsolationDeltaBetaCorr3Hits_3!=1"  )),
        ("pass-cut-tight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightCombinedIsolationDeltaBetaCorr3Hits_3==1"   )),
        ("fail-cut-tight-emuCR",   "%s && %s && q_1*q_2<0 && %s"%(iso1,vetos,"nbtag_noTau>0 && againstLepton_3==1 && byTightCombinedIsolationDeltaBetaCorr3Hits_3!=1"   )),
    ]
    
    # RESTRICT
    #if 'pfmt' in var: b = 100
    #nBins,a,bmt=20,0,100; selectionsDC = [(n,"%s && pfmt_1<%s"%(s,bmt)) for (n,s) in selectionsDC]; label += "_mtlt%s"%bmt
    
    # FILE LOGISTICS
    outdir      = "%s%s/" % (DIR,"datacards" if "datacards" not in DIR else "")
    ensureDirectory(outdir)
    outfilename = outdir + makeDataCardOutputName(process,analysis,channel,var,label=label)
    outfile     = TFile(outfilename, option)
    
    # SHIFT
    if JES:
      var = shift(var,'_jes%s'%JES)
      selectionsDC = [ (n,shift(c,'_jes%s'%JES)) for n,c in selectionsDC ]
      print ">>> shift: %s"%(var)
    if JER:
      var = shift(var,'_jer%s'%JER)
      selectionsDC = [ (n,shift(c,'_jer%s'%JER)) for n,c in selectionsDC ]
      print ">>> shift: %s"%(var)
    if UncEn:
      var = shift(var,'_UncEn%s'%UncEn)
      selectionsDC = [ (n,shift(c,'_UncEn%s'%UncEn)) for n,c in selectionsDC ]
      print ">>> shift: %s"%(var)
    
    # SAMPLES
    samples_dict = {
    # search term     label          extracuts
      'TT':   #[   ( 'TT',     ""               ), ],
               [   ( 'TTT',    "gen_match_2==5" ),
                   #( 'TTL',   "gen_match_2 <5" ),
                   ( 'TTJ',    "gen_match_2!=5" ), ],
      'DY':    [   ( 'ZTT',    "gen_match_2==5" ),
                   ( 'ZL',     "gen_match_2 <5" ),
                   ( 'ZJ',     "gen_match_2==6" ), ],
      'WJ':    [   ( 'W',      ""               ), ],
      'VV':    [   ( 'VV',     ""               ), ],
      'ST':    [   ( 'STT',    "gen_match_2==5" ),
                   ( 'STJ',    "gen_match_2!=5" ), ],
      'QCD':   [   ( 'QCD',    ""               ), ],
    }
    
    # COMPONENTS
    if TES:
      for key in samples_dict:
        samples_dict[key] = [s for s in samples_dict[key] if "match_2==5" in s[1] or "match_2" not in s[1]]
    if JTF:
      for key in samples_dict:
        samples_dict[key] = [s for s in samples_dict[key] if "match_2!=5" in s[1] or "match_2==6" in s[1] or "match_2" not in s[1]]
    
    # EMU
    if 'emu' in channel:
      for key in samples_dict:
        samples_dict[key] = [(s,c.replace("match_2","match_3")) for (s,c) in samples_dict[key]]
    
    # DATA
    if not doShift:
      if  'mutau' in channel: samples_dict['single muon']     = [( 'data_obs', "" )]
      elif 'etau' in channel: samples_dict['single electron'] = [( 'data_obs', "" )]
      elif 'emu'  in channel: samples_dict['single muon']     = [( 'data_obs', "" )]
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        for fkey in filter:
          if fkey in key or key in fkey: break
        else: samples_dict.pop(key,None)
    
    # PRINT
    if verbosity>0 or not doShift or JES or JER or UncEn:
      print ">>> selections:"
      for cutname, cut in selectionsDC:
        print ">>>   %-10s %s"%(cutname,cut)
      print ">>> "
      for sample in samples_dict:
        print ">>>   %-6s %s"%(sample+':',samples_dict[sample])
    
    # SYSTEMATIC UNCERTAINTY
    channel0    = channel.replace("tau","t").replace("mu","m")
    shift_QCD   = kwargs.get('shift_QCD',0) # e.g 0.30
    hist_QCD    = None
    name_QCD    = ""
    
    # LABELS
    #if shift_QCD:
    #  samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sDown" % (channel0,E), "" ))
    #  samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sUp"   % (channel0,E), "" ))
    #else: samples_dict.pop('QCD',None) # only run QCD if it's also shifted
    if EES:     su_label += "_CMS_%s_shape_e_%s_%s%s"          %(process,channel0,E,EES)
    if TES:     su_label += "_CMS_%s_shape_t_%s_%s%s"          %(process,channel0,E,TES)
    if LTF:     su_label += "_CMS_%s_ZLShape_%s_%s%s"          %(process,channel0,E,LTF)
    if JTF:     su_label += "_CMS_%s_shape_jetTauFake_%s%s"    %(process,         E,JTF) # channel independent
    if JES:     su_label += "_CMS_%s_shape_jes_%s%s"           %(process,         E,JES)
    if JER:     su_label += "_CMS_%s_shape_jer_%s%s"           %(process,         E,JER)
    if UncEn:   su_label += "_CMS_%s_shape_uncEn_%s%s"         %(process,         E,UncEn)
    if Zpt:     su_label += "_CMS_%s_shape_dy_%s_%s%s"         %(process,channel0,E,Zpt)
    if TTpt:    su_label += "_CMS_%s_shape_ttbar_%s_%s%s"      %(process,channel0,E,TTpt)
    if QCD_WJ:  su_label += "_QCD_extrap_%s_%s%s"              %(        channel0,E,QCD_WJ)
    
    # LOOP over CATEGORIES
    skipWJrenorm = 'emu' in channel or 'WJ' not in samples_dict
    print ">>> writing %s shapes to %s (%sd)" % (var,outfilename,option)
    if su_label: print ">>> systematic uncertainty label = " + color("%s" % (su_label.lstrip("_")), color="grey")
    for category, selection in selectionsDC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color = "magenta", bold=True)
        
        # MAKE DIR
        sampleset.refreshMemory()
        (dir,dirname) = makeDataCardTDir(outfile,category)
        
        # WRITE selection string
        if recreate:
          canvas, pave = canvasWithText(selection,title=category)
          canvas.Write("selection")
        
        # RENORMALIZE WJ
        if not skipWJrenorm:
          if "iso_2" in selection and "pass" in category:
            newvar = "pfmt_1"
            isoWP  = re.findall(r"iso_2(.*?)==1",selection)[0]
            newbaseline = baseline.replace("iso_2==1","iso_2%s==1"%isoWP)
            shifts = '_jes%s'%JES if JES else '_jer%s'%JER if JER else "_UncEn%s"%UncEn if UncEn else ""
            samples.renormalizeWJ(newbaseline,QCD=doQCD,shift=shifts,reset=True,verbosity=verbosityWJ)
            print ">>> "
          else:
            print ">>>   resetting WJ scale"
            samples.resetScales('WJ',unique=True)
        
        # LOOP over SAMPLES
        for samplename in sorted(samples_dict):
            if not samples_dict[samplename]: continue
            
            # FIND SAMPLE
            sample  = None
            if 'QCD' not in samplename and samples_dict[samplename]:
                matches = [ s for s in sampleset if s.isPartOf(samplename) ]
                if not matches:
                  LOG.warning('Could not make a datacard histogram: no "%s" sample!' % (samplename),pre="  ")
                  continue
                elif len(matches)>1: LOG.warning('  Found more than one "%s" sample!' % (samplename))
                else: sample = matches[0]
            
            histQCD = None
            for subsample, extracuts in samples_dict[samplename]:
                printSameLine(">>>   %5s" % (subsample.ljust(10))) # TODO: make table instead
                
                # SETUP NAMES
                name = subsample+su_label
                cuts = combineCuts(selection,extracuts,"%s<%s && %s<%s"%(a,var,var,b))
                
                # MAKE HIST
                hist = None
                if 'QCD' in subsample: # QCD
                  if 'Down' in subsample and histQCD:
                      hist = histQCD.Clone(name)
                      hist.Scale(1-histQCD)
                  elif 'Up' in subsample and histQCD:
                      hist = histQCD.Clone(name)
                      hist.Scale(1+histQCD)
                  else:
                      hist = sampleset.QCD(var,nBins,a,b,cuts,name=name,weight=extraweight,verbosity=0)
                      histQCD = hist.Clone(name+"_QCD_clone") # don't calculate QCD trice!
                  if hist is None:
                      LOG.warning("QCD histogram failed!")
                      continue
                  hist.SetOption("HIST")
                else:
                  hist = sample.hist(var,nBins,a,b,cuts,name=name,weight=extraweight,verbosity=0)
                  hist.SetOption("E0" if sample.isData else "EHIST")
                hist.GetXaxis().SetTitle(var)
                hist.SetLineColor(kBlack if 'data' in name else hist.GetFillColor())
                hist.SetFillColor(0)
                
                for i, bin in enumerate(hist):
                  if bin<0:
                    print ">>> replace bin %d (%.3f<0) of \"%s\""%(i,bin,hist.GetName())
                    hist.SetBinContent(i,0)
                
                # WRITE HIST
                dir.cd()
                hist.Write(name,TH1D.kOverwrite)
                print "->  written %8.1f events (%5d entries)" % (hist.GetSumOfWeights(),hist.GetEntries())
                deleteHist(hist)
                
            if histQCD: deleteHist(histQCD)
        
    outfile.Close()
    print ">>>\n>>> "
    


def makeDataCardOutputName(process, analysis, channel, var, E="13TeV", label=""):
    """Make name of output file."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    if "t" in channel:
        if   "m" in channel: channel = "mt"
        elif "e" in channel: channel = "et"
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = "em"
    else: print ">>> makeOutputName: channel not found!"
    outputname = "%s_%s_%s_%s.inputs-%s%s.root" % (process,channel,analysis,var,E,label)
    return outputname
    
def makeDataCardTDir(outfile, category):
    """Make directory with given name in given a file."""
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

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    

    
    ########
    # main #
    ########

def main():
    """Main function."""
    
    #checkDataCardHistograms()
    #exit(0)
    
    # MAKE SAMPLES
    global samples, samplesB, samplesS, samplesD
    global samples_TESUp, samples_TESDown, samples_TESscan
    global samples_EESUp, samples_EESDown, samples_JTFUp, samples_JTFDown
    
    # USER OPTIONS
    global channels
    #if args.category > -1: selectCategory(args.category)
    #if args.channel:       selectChannel(args.channel)
    #if args.etau or args.mutau:
    #    channels = [ ]
    #    if args.etau:  channels.append("etau")
    #    if args.mutau: channels.append("mutau")
    
    # LOOP over CHANNELS
    for channel in channels:
        print ">>>\n>>>"
        
        samples.setChannel(channel)
        
        # SET TREENAME
        treename = "tree_%s" % channel
        if useCutTree and "emu" not in channel:
          treename = "tree_%s_cut_relaxed" % channel
        samples.setTreeName(treename)
        if doTES:
          samples_TESUp.setTreeName(treename)
          samples_TESDown.setTreeName(treename)
        if doEES:
          samples_EESUp.setTreeName(treename)
          samples_EESDown.setTreeName(treename)
        if doJTF:
          samples_JTFUp.setTreeName(treename)
          samples_JTFDown.setTreeName(treename)
        for label, samples_TESscan in sorted(samples_TESscan.iteritems()):
          samples_TESscan.setTreeName(treename)
        
        ## RENORMALIZE WJ
        #print ">>> "
        #if normalizeWJ and 'emu' not in channel:
        #   LOG.header("%s: WJ renormalization" % (channel))
        #   samples.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #   if doTES:
        #     samples_TESUp.renormalizeWJ(  baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #     samples_TESDown.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #   if doJTF:
        #     samples_JTFUp.renormalizeWJ(  baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #     samples_JTFDown.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        #print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        keys = [ ("ttbar","tid","pfmt_1",10,0,250),
                 ("ttbar","tid","m_vis",10,0,200),
                 #("ttbar","tid","ht",100,0,300),
        ]
        if args.obs: keys = [k for k in keys if any(o in k[2] for o in args.obs)]
        for process, analysis, var, width, a, b in keys:
            kwargs = { 'process': process, 'analysis': analysis, 'label': "_mt250" }
            #if doNominal:
            writeDataCardHistograms(samples,              channel, var, width, a, b, recreate=True, **kwargs )
            if doTES and "tau" in channel:
                writeDataCardHistograms(samples_TESUp,    channel, var, width, a, b, TES='Down', filter=['TT','DY','ST'], **kwargs )
                writeDataCardHistograms(samples_TESDown,  channel, var, width, a, b, TES='Up',   filter=['TT','DY','ST'], **kwargs )
            if doEES and "emu" in channel:
                writeDataCardHistograms(samples_EESUp,    channel, var, width, a, b, EES='Up',   filter=['TT','ST'],  **kwargs )
                writeDataCardHistograms(samples_EESDown,  channel, var, width, a, b, EES='Down', filter=['TT','ST'],  **kwargs )
            if doJTF:
              if "tau" in channel:
                writeDataCardHistograms(samples_JTFUp,    channel, var, width, a, b, JTF='Up',   filter=['TT','DY','ST','WJ'],  **kwargs )
                writeDataCardHistograms(samples_JTFDown,  channel, var, width, a, b, JTF='Down', filter=['TT','DY','ST','WJ'],  **kwargs )
              else:
                writeDataCardHistograms(samples_JTFUp,    channel, var, width, a, b, JTF='Up',   filter=['TT','ST'],  **kwargs )
                writeDataCardHistograms(samples_JTFDown,  channel, var, width, a, b, JTF='Down', filter=['TT','ST'],  **kwargs )
            if doJEC:
                writeDataCardHistograms(samples,          channel, var, width, a, b, JES='Up',   **kwargs )
                writeDataCardHistograms(samples,          channel, var, width, a, b, JES='Down', **kwargs )
            if doJER:
                writeDataCardHistograms(samples,          channel, var, width, a, b, JER='Up',   **kwargs )
                writeDataCardHistograms(samples,          channel, var, width, a, b, JER='Down', **kwargs )
            if doUncEn:
                writeDataCardHistograms(samples,          channel, var, width, a, b, UncEn='Up',   **kwargs )
                writeDataCardHistograms(samples,          channel, var, width, a, b, UncEn='Down', **kwargs )
            ###if doZpt:
            ###    writeDataCardHistograms(samples_ZptDown,    channel, var, width, a, b, Zpt='Down', filter=["DY"], **kwargs )
            ###    writeDataCardHistograms(samples_ZptUp,      channel, var, width, a, b, Zpt='Up',   filter=["DY"], **kwargs )
            ###if doTTpt:
            ###    writeDataCardHistograms(samples_TTptDown,   channel, var, width, a, b, TTpt='Down', filter=["ttbar"], **kwargs )
            ###    writeDataCardHistograms(samples_TTptUp,     channel, var, width, a, b, TTpt='Up',   filter=["ttbar"], **kwargs )
            ###if doQCD_WJ:
            ###    writeDataCardHistograms(samples_QCD_WJDown, channel, var, width, a, b, QCD_WJ='Down', filter=["W + jets"], **kwargs )
            ###    writeDataCardHistograms(samples_QCD_WJUp,   channel, var, width, a, b, QCD_WJ='Up',   filter=["W + jets"], **kwargs )
            
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


