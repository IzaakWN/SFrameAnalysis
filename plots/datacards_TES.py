#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2018)

print
from argparse import ArgumentParser
import os, sys, time
import copy
from math import sqrt, pow, floor, ceil
import ROOT
from ROOT import TFile, TH1D, THStack, gDirectory, kAzure, kGreen, kRed
# from PlotTools import *
ROOT.gROOT.SetBatch(ROOT.kTRUE)

argv = sys.argv
description = """This script make plots."""
parser = ArgumentParser(prog="plotter",description=description,epilog="Succes!")
parser.add_argument( "-i", "--config", dest="configFile", type=str, default="", action='store',
                     metavar="CONFIG_FILE", help="name of config file containing the settings, samples, selections and variables" )
parser.add_argument( "-s", "--category", dest="category", type=int, default=-1, action='store',
                     metavar="CATEGORY", help="run only for this category of selection and cuts" )
parser.add_argument( "-c", "--channel", dest="channel", default="", action='store',
                     metavar="CHANNEL", help="run only for this channel" )
parser.add_argument( "-e", "--etau", dest="etau", default=False, action='store_true',
                     help="run only for the etau channel" )
parser.add_argument( "-m", "--mutau", dest="mutau", default=False, action='store_true',
                     help="run only for the mutau channel" )
parser.add_argument( "-u", "--emu", dest="emu", default=False, action='store_true',
                     help="run only for the emu channel" )
parser.add_argument( "-l", "--list", dest="list", default=False, action='store_true',
                     help="list all available categories" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="make script verbose" )
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                     help="renormalize W+Jets" )
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
if args.noWJrenorm: normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
setVerbose(args.verbose)
exec commands




    ##########################
    # checkDataCardHistogram #
    ##########################

def checkDataCardHistograms():
    """Plot histgrams for check"""
    print ">>> checkDataCardHistograms"
    
    filename    = "./datacards/ttbar_mt_tid_pfmt_1.inputs-13TeV_mtlt100.root"
    file        = TFile(filename)
    dirname     = "pass-loose"
    
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
    plot.plot(ratio=True)
    plot.saveAs("test.png")
    
    


    ##########################
    # writeDataCardHistogram #
    ##########################

def writeDataCardHistograms(samples, channel, var, binWidth, a, b, **kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    
    filter      = kwargs.get('filter',      [ ]             )
    process     = kwargs.get('process',     "ztt"           )
    analysis    = kwargs.get('analysis',    "tes"           )
    DIR         = kwargs.get('DIR',         DATACARDS_DIR   )
    label       = kwargs.get('label',       ""              ) # WEIGHTED
    su_label    = kwargs.get('su_label',    ""              )
    E           = kwargs.get('E',           "13TeV"         )
    TES         = kwargs.get('TES',         ""              )
    TESscan     = kwargs.get('TESscan',     ""              )
    EES         = kwargs.get('EES',         ""              )
    LTF         = kwargs.get('LTF',         ""              )
    JTF         = kwargs.get('JTF',         ""              )
    Zpt         = kwargs.get('Zpt',         ""              )
    TTpt        = kwargs.get('TTpt',        ""              )
    QCD_WJ      = kwargs.get('QCD_WJ',      ""              )
    nBins       = int(kwargs.get('nBins',   (b-a)/binWidth ))
    extraweight = "" #weight"
    
    vetos       = "lepton_vetos==0"
    iso1        = "iso_1<0.15" if "mutau" in channel else "iso_1<0.10"
    iso2        = "iso_2==1"
    baseline    = "%s && %s && %s && q_1*q_2<0" % (iso1,iso2,vetos)
    if "emu" in channel:
      vetos     = "extraelec_veto==0 && extramuon_veto==0"
      iso1      = "iso_1<0.20 && iso_2<0.15"
      baseline  = "%s && %s && q_1*q_2<0" % (iso1,vetos)
    
    selectionsDC = [ ]
    selectionsDC_TES = [
      ("DM0",           "%s && %s"%(baseline,"decayMode_2==0 && pfmt_1<50")         ),
      ("DM1",           "%s && %s"%(baseline,"decayMode_2==1 && pfmt_1<50")         ),
      ("DM10",          "%s && %s"%(baseline,"decayMode_2==10 && pfmt_1<50")        ),
      #("DM11",          "%s && %s"%(baseline,"decayMode_2==11 && pfmt_1<50")        ),
      ("all",           "%s && %s"%(baseline,"decayMode_2<11 && pfmt_1<50")        ),
    ]
    selectionsDC_TID = [
      ### MVA-based ###
      ("pass-vloose",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vloose==1")   ),
      ("fail-vloose",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vloose!=1")   ),
      ("pass-loose",    "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_loose==1")   ),
      ("fail-loose",    "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_loose!=1")   ),
      ("pass-medium",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_medium==1")  ),
      ("fail-medium",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_medium!=1")  ),
      ("pass-tight",    "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2==1")         ),
      ("fail-tight",    "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2!=1")         ),
      ("pass-vtight",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vtight==1")  ),
      ("fail-vtight",   "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vtight!=1")  ),
      ("pass-vvtight",  "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vvtight==1") ),
      ("fail-vvtight",  "%s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && iso_2_vvtight!=1") ),
      ### CUT-based ###
      #("pass-cut-loose",  "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byLooseCombinedIsolationDeltaBetaCorr3Hits_2==1")   ),
      #("fail-cut-loose",  "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byLooseCombinedIsolationDeltaBetaCorr3Hits_2!=1")   ),
      #("pass-cut-medium", "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byMediumCombinedIsolationDeltaBetaCorr3Hits_2==1")  ),
      #("fail-cut-medium", "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byMediumCombinedIsolationDeltaBetaCorr3Hits_2!=1")  ),
      #("pass-cut-tight",  "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byTightCombinedIsolationDeltaBetaCorr3Hits_2==1")   ),
      #("fail-cut-tight",  "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag>0 && byTightCombinedIsolationDeltaBetaCorr3Hits_2!=1")   ),
    ]
    if "emu" in channel:
      selectionsDC_TID = [
        ("emuCR",               "%s && %s && %s && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0")),
        ###("notau-emuCR",         "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3<1")),
        ("pass-vloose-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBoldDMwLT_3==1")   ),
        ("fail-vloose-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVLooseIsolationMVArun2v1DBoldDMwLT_3!=1")   ),
        ("pass-loose-emuCR",    "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBoldDMwLT_3==1")   ),
        ("fail-loose-emuCR",    "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byLooseIsolationMVArun2v1DBoldDMwLT_3!=1")   ),
        ("pass-medium-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBoldDMwLT_3==1")  ),
        ("fail-medium-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byMediumIsolationMVArun2v1DBoldDMwLT_3!=1")  ),
        ("pass-tight-emuCR",    "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3==1")   ),
        ("fail-tight-emuCR",    "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3!=1")   ),
        ("pass-vtight-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBoldDMwLT_3==1")  ),
        ("fail-vtight-emuCR",   "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBoldDMwLT_3!=1")  ),
        ("pass-vvtight-emuCR",  "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBoldDMwLT_3==1") ),
        ("fail-vvtight-emuCR",  "%s && %s && %s && decayMode_3<11 && q_1*q_2<0"%(iso1,vetos,"ncbtag_noTau>0 && againstLepton_3==1 && byVVTightIsolationMVArun2v1DBoldDMwLT_3!=1") ),
    ]
    if analysis=='tid':
      if 'pfmt' in var: b = 100
      nBins,a,bmt=20,0,100; selectionsDC_TID = [(n,"%s && pfmt_1<%s"%(s,bmt)) for n, s in selectionsDC_TID]; label="_mtlt%s"%bmt
      #nBins,a,b=40,0,200; selectionsDC_TID = [(n,"%s && met>30"%s) for n, s in selectionsDC_TID]; label="_metgt30"
    elif 'm_2' in var and (a>0.8 or b<1.5):
      label += ("_%s-%s"%(a,b)).replace('.','p')
      selectionsDC_TES = [(n,"%s && %s < m_2 && m_2 < %s"%(s,a,b)) for n, s in selectionsDC_TES]
    elif 'm_2' in var and (binWidth<0.08):
      label += ("_%s"%(binWidth)).replace('.','p')
    
    samples_dict = {
    # search term             label          extracuts
      "TT":   #[   ( 'TT',     ""                 ), ],
               [   ( 'TTT',    "gen_match_2 == 5" ),
                   #( 'TTL',    "gen_match_2  < 5" ),
                   ( 'TTJ',    "gen_match_2 != 5" ), ],
      "DY":    [   ( 'ZTT',    "gen_match_2 == 5" ),
                   ( 'ZL',     "gen_match_2  < 5" ),
                   ( 'ZJ',     "gen_match_2 == 6" ), ],
      "WJ":    [   ( 'W',      ""                 ), ],
      "VV":    [   ( 'VV',     ""                 ), ],
      'ST':    [   ( 'ST',     ""                 ), ],
      'QCD':   [   ( 'QCD',    ""                 ), ],
    }
    if TESscan: samples_dict = { 'Drell Yan': [( 'ZTT', "gen_match_2 == 5" ),] }
    if analysis=='tes': samples_dict['ttbar'] = [( 'TT',  "" ),]
    
    # DATA
    if  "mutau" in channel: samples_dict["single muon"]     = [( "data_obs", "" )]
    elif "etau" in channel: samples_dict["single electron"] = [( "data_obs", "" )]
    elif "emu"  in channel: samples_dict["single muon"]     = [( "data_obs", "" )]
    
    # MEASUREMENT
    if analysis=='tes': selectionsDC = selectionsDC_TES
    if analysis=='tid': selectionsDC = selectionsDC_TID
    if var=="m_2":      selectionsDC = [s for s in selectionsDC if s[0]!="DM0"]
    print ">>> selections:"
    for cutname, cut in selectionsDC:
      print ">>>   %-18s %s"%(cutname,cut)
    print ">>> "
    
    # FILE LOGISTICS
    option      = 'UPDATE'
    if kwargs.get('recreate',False): option = 'RECREATE'
    outdir      = "%s%s/" % (DIR,"datacards" if "datacards" not in DIR else "")
    ensureDirectory(outdir)
    outfilename = outdir + makeDataCardOutputName_TES(process,analysis,channel,var,label=label)
    outfile     = TFile(outfilename, option)
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        #if key not in filter: samples_dict.pop(key,None)
        for fkey in filter:
          if fkey in key or key in fkey: break
        else: samples_dict.pop(key,None)
    
    # SYSTEMATIC UNCERTAINTY
    channel0    = channel.replace("tau","t").replace("mu","m")
    shift_QCD   = kwargs.get('shift_QCD',0) # e.g 0.30
    hist_QCD    = None
    name_QCD    = ""
    
    #if shift_QCD:
    #    samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sDown"              % (channel0,E), "" ))
    #    samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sUp"                % (channel0,E), "" ))
    #else: samples_dict.pop('QCD',None) # only run QCD if it's also shifted
    if TES:     su_label += "_CMS_htt_shape_t_%s_%s%s"      % (channel0,E,TES)
    if TESscan: su_label += "_TES%s"                        % (TESscan)
    if EES:     su_label += "_CMS_htt_shape_e_%s_%s%s"      % (channel0,E,EES)
    if LTF:     su_label += "_CMS_htt_ZLShape_%s_%s%s"      % (channel0,E,LTF)
    if JTF:     su_label += "_CMS_htt_jetFakeShape_%s_%s%s" % (channel0,E,JTF)
    if Zpt:     su_label += "_CMS_htt_dyShape_%s_%s%s"      % (channel0,E,Zpt)
    if TTpt:    su_label += "_CMS_htt_ttbarShape_%s_%s%s"   % (channel0,E,TTpt)
    if QCD_WJ:  su_label += "_QCD_extrap_%s_%s%s"           % (channel0,E,QCD_WJ)
    print ">>> writing %s shapes to %s (%sd)" % (var,outfilename,option)
    if su_label: print ">>> systematic uncertainty label = " + color("%s" % (su_label.lstrip("_")), color="grey")
    
    # LOOP over CATEGORIES
    for category, cuts in selectionsDC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color = "magenta", bold=True)
        
        # MAKE DIR
        (dir,dirname) = makeDataCardTDir_TES(outfile,category)
        
        # RENORMALIZE WJ
        if len(filter)==0 and analysis=='tid' and "iso_2" in cuts and "pass" in category and "emu" not in channel:
          isoWP = re.findall(r"iso_2(.*)==1",cuts)[0]
          newbaseline = baseline.replace("iso_2==1","iso_2%s==1"%isoWP)
          samples.renormalizeWJ("pfmt_1", 200, 80, 200, newbaseline, QCD=doQCD, reset=True, verbosity=1)
          print ">>> "
        
        # LOOP over SAMPLES
        for samplename in samples_dict:
            if not samples_dict[samplename]: continue
            
            # FIND SAMPLE
            sample  = None
            if 'QCD' not in samplename and samples_dict[samplename]:
                matches = [ s for s in samples if s.isPartOf(samplename) ]
                if not matches:
                    LOG.warning('Could not make datacard histogram! No "%s" sample!' % (samplename),pre="  ")
                    continue
                elif len(matches)>1: LOG.warning('  Found more than one "%s" sample!' % (samplename))
                else: sample = matches[0]
            
            for subsample, extracuts in samples_dict[samplename]:
                printSameLine(">>>   %5s" % (subsample.ljust(14))) # TODO: make table instead
                
                # SETUP NAMES
                if 'emu' in channel and ('pass' in category or 'fail' in category):
                    extracuts=extracuts.replace("gen_match_2","gen_match_3")
                name        = subsample+su_label
                cuts1       = combineCuts(cuts,extracuts,"%s<%s && %s<%s"%(a,var,var,b))
                
                # MAKE HIST
                hist        = None
                if 'QCD' in subsample: # QCD
                    if "Down" in subsample and shift_QCD:
                        hist = hist_QCD.Clone(name)
                        hist.Scale(1-shift_QCD)
                    elif "Up" in subsample and shift_QCD:
                        hist = hist_QCD.Clone(name)
                        hist.Scale(1+shift_QCD)
                    else:
                        hist = samples.QCD(var,nBins,a,b,cuts1,name=name,weight=extraweight,verbosity=0)
                        if shift_QCD:
                            hist_QCD = hist.Clone(name+"_QCD_clone") # don't calculate QCD trice!
                    if hist is None:
                        LOG.warning("QCD histogram failed!")
                        continue
                else:
                    hist = sample.hist(var,nBins,a,b,cuts1,name=name,weight=extraweight,verbosity=0)
                hist.GetXaxis().SetTitle(var)
                hist.SetLineStyle(1)
                hist.SetLineWidth(2)
                
                for i,bin in enumerate(hist):
                    if bin<0:
                        print ">>> replace bin %d (%.3f<0) of \"%s\""%(i,bin,hist.GetName())
                        hist.SetBinContent(i,0)
                
                # WRITE HIST
                hist.Write(name,TH1D.kOverwrite)
                print "->  written %5.1f events (%5d entries)" % (hist.GetSumOfWeights(),hist.GetEntries())
                #gDirectory.Delete(name)
                
        #if name_QCD: gDirectory.Delete(name_QCD)
        
    outfile.Close()
    print ">>>\n>>> "
    


def makeDataCardOutputName_TES(process, analysis, channel, var, E="13TeV", label=""):
    """Make name of output file for TES."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    
    if "t" in channel:
        if   "m" in channel: channel = "mt"
        elif "e" in channel: channel = "et"
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = "em"
    else: print ">>> makeOutputName: channel not found!"
    #var = var.replace('pfmt_1','mt')
    
    outputname = "%s_%s_%s_%s.inputs-%s%s.root" % (process,channel,analysis,var,E,label)
    return outputname
    

def makeDataCardTDir_TES(outfile, category):
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
    
    if args.list:
        listCategories()
        return 0
    
    # MAKE SAMPLES
    global samples, samplesB, samplesS, samplesD
    global samplesB_EESUp, samplesB_EESDown, samplesB_JTFUp, samplesB_JTFDown
    
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
        
        #samples             = samplesB                                + samplesD.get(channel,[]) # for normal plots
        #samples_EES0p99     = samplesB_EES0p99                        + samplesD.get(channel,[]) # for WJ renorm only
        #samples_EES1p01     = samplesB_EES1p01                        + samplesD.get(channel,[]) # for WJ renorm only
        #samples_QCD_WJDown  = samplesB_QCD_WJUp   + samplesB_noQCD_WJ + samplesD.get(channel,[]) # for WJ renorm only
        #samples_QCD_WJUp    = samplesB_QCD_WJDown + samplesB_noQCD_WJ + samplesD.get(channel,[]) # for WJ renorm only
        
        # SET TREENAME
        treename = "tree_%s" % channel
        if useCutTree and "emu" not in channel:
          treename = "tree_%s_cut_relaxed" % channel
        samples.setTreeName(treename)
        if doEES:
          samplesB_EESUp.setTreeName(treename)
          samplesB_EESDown.setTreeName(treename)
        if doJTF:
          samplesB_JTFUp.setTreeName(treename)
          samplesB_JTFDown.setTreeName(treename)
        
        # RENORMALIZE WJ
        #print ">>> "
        #if normalizeWJ and channel!="emu":
        #    LOG.header("%s: WJ renormalization" % (channel))
        #    samples.renormalizeWJ("pfmt_1", 200, 80, 200, baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #    # TODO renormalize WJ in other sample sets
        #else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        #print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        keys = [ #("ztt","tes","m_2",0.1,0,3),("ztt","tes","m_vis",5,0,200),
                 #("ztt","tes","m_2",0.04,0.9,1.3),("ztt","tes","m_2",0.04,0,3),
                 ("ttbar","tid","pfmt_1",5,0,300), ("ttbar","tid","m_vis",5,0,200),
        ]
        for process, analysis, var, width, a, b in keys:
            kwargs = { 'process': process, 'analysis': analysis }
            if doNominal:
                writeDataCardHistograms(    samples,        channel, var, width, a, b, recreate=recreateDC, **kwargs )
            if doTESscan and analysis=='tes':
              for label,set in samplesB_TESscanDown:
                writeDataCardHistograms(set,                channel, var, width, a, b, TESscan=label,  filter=['DY'],   **kwargs )
              for label,set in samplesB_TESscanUp:
                writeDataCardHistograms(set,                channel, var, width, a, b, TESscan=label,  filter=['DY'],   **kwargs )
            #elif doTES:
            #    writeDataCardHistograms(samplesB_TES0p97,    channel, var, width, a, b, TES="Down",   filter=["ttbar","Drell Yan"], analysis=analysis )
            #    writeDataCardHistograms(samplesB_TES1p03,    channel, var, width, a, b, TES="Up",     filter=["ttbar","Drell Yan"], analysis=analysis )
            if doEES:
                writeDataCardHistograms(samplesB_EESUp,    channel, var, width, a, b, EES="Up",   filter=['TT','ST'],  **kwargs )
                writeDataCardHistograms(samplesB_EESDown,  channel, var, width, a, b, EES="Down", filter=['TT','ST'],  **kwargs )
            if doJTF:
                writeDataCardHistograms(samplesB_JTFUp,    channel, var, width, a, b, JTF="Up",   filter=['TT','ST'],  **kwargs )
                writeDataCardHistograms(samplesB_JTFDown,  channel, var, width, a, b, JTF="Down", filter=['TT','ST'],  **kwargs )
            #if doZpt:
            #    writeDataCardHistograms(samplesB_ZptDown,    channel, var, width, a, b, Zpt="Down",    filter=["Drell Yan"],    analysis=analysis )
            #    writeDataCardHistograms(samplesB_ZptUp,      channel, var, width, a, b, Zpt="Up",      filter=["Drell Yan"],    analysis=analysis )
            #if doTTpt:
            #    writeDataCardHistograms(samplesB_TTptDown,   channel, var, width, a, b, TTpt="Down",   filter=["ttbar"],        analysis=analysis )
            #    writeDataCardHistograms(samplesB_TTptUp,     channel, var, width, a, b, TTpt="Up",     filter=["ttbar"],        analysis=analysis )
            #if doQCD_WJ:
            #    writeDataCardHistograms(samplesB_QCD_WJDown, channel, var, width, a, b, QCD_WJ="Down", filter=["W + jets"],     analysis=analysis )
            #    writeDataCardHistograms(samplesB_QCD_WJUp,   channel, var, width, a, b, QCD_WJ="Up",   filter=["W + jets"],     analysis=analysis )
        
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


