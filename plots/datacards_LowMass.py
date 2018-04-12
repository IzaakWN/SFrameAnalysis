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
parser.add_argument( "--bbA", dest="bbA", default=False, action='store_true',
                     help="make datacard for bbA categories" )
parser.add_argument( "--VLQ", dest="VLQ", default=False, action='store_true',
                     help="make datacard for VLQ categories" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="make script verbose" )
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                     help="renormalize W+Jets" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()
if not args.configFile:
    args.configFile = "PlotTools/config_emu2016.py" if args.emu else "PlotTools/config_ltau2016.py"

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
doStack = False; doDataCard = True
if args.noWJrenorm: normalizeWJ = False
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
    
    global SUSY_bbA, VLQ_bqX, VLQ_bqX_MB300, VLQ_bqX_MB450
    verbosity     = kwargs.get('verbosity',   0               )
    filter        = kwargs.get('filter',      [ ]             )
    process       = kwargs.get('process',     "xtt"           )
    analysis      = kwargs.get('analysis',    "LowMassDiTau"  )
    DIR           = kwargs.get('DIR',         DATACARDS_DIR   )
    recreate      = kwargs.get('recreate',    False           )
    label         = kwargs.get('label',       ""              ) # WEIGHTED
    su_label      = kwargs.get('su_label',    ""              )
    masses        = kwargs.get('masses',      range(13,83,3)  )
    E             = kwargs.get('E',           "13TeV"         )
    JES           = kwargs.get('JES',         ""              )
    JER           = kwargs.get('JER',         ""              )
    TES           = kwargs.get('TES',         ""              )
    TESscan       = kwargs.get('TESscan',     ""              )
    EES           = kwargs.get('EES',         ""              )
    LTF           = kwargs.get('LTF',         ""              )
    JTF           = kwargs.get('JTF',         ""              )
    Zpt           = kwargs.get('Zpt',         ""              )
    TTpt          = kwargs.get('TTpt',        ""              )
    QCD_WJ        = kwargs.get('QCD_WJ',      ""              )
    nBins         = int(kwargs.get('nBins',   (b-a)/binWidth ))
    option        = 'RECREATE' if recreate else 'UPDATE'
    doShift       = TES or EES or LTF or JTF or Zpt or TTpt
    extraweight   = "" #weight"
    
    # SELECTIONS
    iso1            = "iso_1<0.15" if "mutau" in channel else "iso_1<0.10"
    iso2            = "iso_2==1"
    vetos           = "lepton_vetos==0"
    baseline        = "%s && %s && %s && q_1*q_2<0" % (iso1,iso2,vetos)
    if "emu" in channel:
      vetos         = "extraelec_veto==0 && extramuon_veto==0"
      iso1          = "iso_1<0.20 && iso_2<0.15"
      baseline      = "%s && %s && q_1*q_2<0" % (iso1,vetos)
    category_bbA2   = "ncbtag >0 && ncbtag==ncjets && nfjets==0"
    category_bbA    = "ncbtag==1 && ncjets==1 && nfjets==0" # no optimizations
    category_bbA_NV = "ncbtag>0"
    category1       = "ncbtag>0 && ncjets==1 && nfjets >0"
    category2       = "ncbtag>0 && ncjets==2 && nfjets==0"
    category2J      = "ncbtag>0 && ncjets==2 && nfjets==0"
    
    selectionsDC = [
      #("1btag",  "%s && %s"%(baseline,category_bbA.replace('btag','btag20').replace('cjets','cjets20')), "_bbA_pt20" ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets == 1 && nfjets == 0"), "_bbA_pt20_j30"   ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets20 == 1 && nfjets == 0"), "_bbA_pt20_j20" ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets20 == 1 && nfjets == 0 && pzeta_disc>-30"), "_bbA_pt20_j20_Dzeta-30" ),
      #("1btag",  "%s && %s"%(baseline,category_bbA.replace('btag','btag20').replace('cjets','cjets20').replace('fjets','fjets20')), "_bbA_pt20_fj20" ),
      #("1btag",  "%s && %s"%(baseline,category_bbA.replace(' && nfjets == 0','')), "_bbA_fj"            ),
      #("1btag",  "%s && %s"%(baseline,category_bbA2),                       "_bbA2"                     ),
      #("1btag",  "%s && %s"%(baseline,category_bbA),                        "_bbA_noOpt"                ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag==1"),                         "_bbA_noVeto"               ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20==1"),                       "_bbA_pt20_noVeto"          ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20==1 && pzeta_disc>-80"),     "_bbA_pt20_noVeto_Dzeta-80" ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag==1 && njets<3"),              "_bbA_noVeto2"              ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag==1 && njets<4"),              "_bbA_noVeto3"              ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag>1"),                         "_bbA2_noVeto"               ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"pzeta_disc>-10"), "_bbA_Dzeta-10"             ),
      ("1btag",  "%s && %s && %s"%(baseline,category_bbA_NV,"pzeta_disc>-40 && pfmt_1<40"),              ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"met<30"),         "_bbA_met30"                ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"pfmt_1<20"),      "_bbA_mt20"                 ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0"), "_noOpt"           ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0"), "_noOpt"           ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2.5"), "_dphi2p5" ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && pfmt_1<80"), "_mt80" ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && met<60 && pfmt_1<40"), "_met60_mt40" ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2 && met<60 && pfmt_1<40"), "_met60_mt40" ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && pfmt_1<60 && met<40"), "_mt60_met40" ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && pfmt_1<60 && met<40"), "_mt60_met40" ),
      ("1b1f",   "%s && %s && %s" % (baseline,category1,"pfmt_1<60"),                                    ),
      ("1b1c",   "%s && %s && %s" % (baseline,category2J,"pfmt_1<60"),                                   ),
    ]
    
    # FILE LOGISTICS
    if len(selectionsDC[0])>2:
      label     = selectionsDC[0][2]+label
      selectionsDC = [c[:2] for c in selectionsDC]
    outdir      = "%s%s/" % (DIR,"datacards" if "datacards" not in DIR else "")
    ensureDirectory(outdir)
    outfilename = outdir + makeDataCardOutputName(process,analysis,channel,label=label)
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
    
    # SAMPLES  
    samples_dict = {
    # search term     label          extracuts
      "TT":   [    ( 'TTT',    "gen_match_2==5" ),
                   ( 'TTL',    "gen_match_2 <5" ),
                   ( 'TTJ',    "gen_match_2==6" ), ],
      "DY":    [   ( 'ZTT',    "gen_match_2==5" ),
                   ( 'ZL',     "gen_match_2 <5" ),
                   ( 'ZJ',     "gen_match_2==6" ), ],
      "WJ":    [   ( 'W',      ""               ), ],
      "VV":    [   ( 'VV',     ""               ), ],
      'ST':    [   #( 'STT',    "gen_match_2==5" ),
                   #( 'STJ',    "gen_match_2!=5" ),
                   ( 'ST',     ""               ), ],
      'QCD':   [   ( 'QCD',    ""               ), ],
    }
    
    # COMPONENTS
    if TES:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if "gen_match_2==5" in s[1] ]
    if JTF:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if "gen_match_2!=5" in s[1] or "gen_match_2==6" in s[1] ]
    if LTF:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if "gen_match_2!=5" in s[1] or "gen_match_2 <5" in s[1] ]
    
    # DATA
    if not doShift:
      if  "mutau" in channel: samples_dict["single muon"]     = [( "data_obs", "" )]
      elif "etau" in channel: samples_dict["single electron"] = [( "data_obs", "" )]
      elif "emu"  in channel: samples_dict["electron-muon"]   = [( "data_obs", "" )]
    
    # SIGNAL mass points
    extraweight = ""
    for mass, filterEff in SUSY_bbA:
      #extraweight = "getBosonPtWeight(%s,pt_genboson)"%mass; kwargs['label'] = "_weighted"
      samples_dict['bbA*%d'%mass] = [( "ATT-M%d"%mass, "" )]
    for mass, filterEff in VLQ_bqX:
      samples_dict['VLQ*%d*%d'%(170,mass)] = [( "XTT-MB%d-M%d"%(170,mass), "")]
    for mass, filterEff in VLQ_bqX_MB300:
      samples_dict['VLQ*%d*%d'%(300,mass)] = [( "XTT-MB%d-M%d"%(300,mass), "")]
    for mass, filterEff in VLQ_bqX_MB450:
      samples_dict['VLQ*%d*%d'%(450,mass)] = [( "XTT-MB%d-M%d"%(450,mass), "")]
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        for fkey in filter:
          if fkey in key or key in fkey: break
        else: samples_dict.pop(key,None)
    
    # PRINT
    if verbosity>0 or not doShift:
      print ">>> selections:"
      for cutname, cut in selectionsDC:
        print ">>>   %-14s %s"%(cutname,cut)
      print ">>> "
    
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
    if TES:     su_label += "_CMS_%s_shape_t_%s_%s%s"        % (process,channel0,E,TES)
    if JES:     su_label += "_CMS_%s_shape_jes_%s_%s%s"      % (process,channel0,E,JES)
    if JER:     su_label += "_CMS_%s_shape_jer_%s_%s%s"      % (process,channel0,E,JER)
    if TESscan: su_label += "_TES%s"                         % (TESscan)
    if EES:     su_label += "_CMS_%s_shape_e_%s_%s%s"        % (process,channel0,E,EES)
    if LTF:     su_label += "_CMS_%s_ZLShape_%s_%s%s"        % (process,channel0,E,LTF)
    #if JTF:    su_label += "_CMS_%s_shape_jetTauFake_%s_%s%s" % (process,channel0,E,JTF) # channel dependent
    if JTF:     su_label += "_CMS_%s_shape_jetTauFake_%s%s"  % (process,E,JTF)
    if Zpt:     su_label += "_CMS_%s_shape_dy_%s_%s%s"       % (process,channel0,E,Zpt)
    if TTpt:    su_label += "_CMS_%s_shape_ttbar_%s_%s%s"    % (process,channel0,E,TTpt)
    if QCD_WJ:  su_label += "_QCD_extrap_%s_%s%s"            % (channel0,E,QCD_WJ)
    
    # LOOP over CATEGORIES
    print ">>> writing %s shapes to %s (%sd)" % (var,outfilename,option)
    if su_label: print ">>> systematic uncertainty label = " + color("%s" % (su_label.lstrip('_')), color="grey")
    for category, selection in selectionsDC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color = "magenta", bold=True)
        
        # MAKE DIR
        sampleset.refreshMemory()
        (dir,dirname) = makeDataCardTDir(outfile,category)
        
        # TT RENORMALIZATION
        if normalizeTT and '1bt' not in category:
          shifts = '_jes%s'%JES if JES else '_jer%s'%JER if JER else ""
          sampleset.renormalizeTT(selection,baseline=baseline,shift=shifts,QCD=doQCD,verbosity=verbosityWJ)
        
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
            for sampleinfo in samples_dict[samplename]:
                
                subsample, extracuts = sampleinfo[:2]
                extraweight = ""
                if len(sampleinfo)>2: extraweight = sampleinfo[2]
                printSameLine(">>>   %5s" % (subsample.ljust(16))) # TODO: make table instead
                
                # SETUP NAMES
                name = subsample+su_label
                cuts = combineCuts(selection,extracuts,"%s<%s && %s<%s"%(a,var,var,b))
                
                # MAKE HIST
                hist = None
                if 'QCD' in subsample: # QCD
                  if "Down" in subsample and histQCD:
                      hist = histQCD.Clone(name)
                      hist.Scale(1-histQCD)
                  elif "Up" in subsample and histQCD:
                      hist = histQCD.Clone(name)
                      hist.Scale(1+histQCD)
                  else:
                      hist = sampleset.QCD(var,nBins,a,b,cuts,name=name,weight=extraweight,verbosity=1)
                      histQCD = hist.Clone(name+"_QCD_clone") # don't calculate QCD trice!
                  if hist is None:
                      LOG.warning("QCD histogram failed!")
                      continue
                  hist.SetOption("HIST")
                else:
                  hist = sample.hist(var,nBins,a,b,cuts,name=name,weight=extraweight,verbosity=1)
                  hist.SetOption("E0" if sample.isData else "EHIST")
                hist.GetXaxis().SetTitle(var)
                hist.SetLineColor(hist.GetFillColor())
                hist.SetFillColor(0)
                
                for i,bin in enumerate(hist):
                  if bin<0:
                    print ">>> replace bin %d (%.3f<0) of \"%s\""%(i,bin,hist.GetName())
                    hist.SetBinContent(i,0)
                
                # WRITE HIST
                hist.Write(name,TH1D.kOverwrite)
                print "->  written %8.1f events (%5d entries)" % (hist.GetSumOfWeights(),hist.GetEntries())
                deleteHist(hist)
                
            if histQCD: deleteHist(histQCD)
    outfile.Close()
    print ">>>\n>>> "
    


def makeDataCardOutputName(process, analysis, channel, E="13TeV", label=""):
    """Make name of output file."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    
    if "t" in channel:
        if   "m" in channel: channel = "mt"
        elif "e" in channel: channel = "et"
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = "em"
    else: print ">>> makeOutputName: channel not found!"
    #var = var.replace('pfmt_1','mt')
    
    outputname = "%s_%s.inputs-%s-%s%s.root" % (process,channel,analysis,E,label)
    return outputname
    

def makeDataCardTDir(outfile, category):
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
    
    #checkDataCardHistograms()
    #exit(0)
    
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
        
        # SET TREENAME
        treename = "tree_%s" % channel
        if useCutTree and "emu" not in channel:
          treename = "tree_%s_cut_relaxed" % channel
        samples.setTreeName(treename)
        if doEES:
          samplesB_EESUp.setTreeName(treename)
          samplesB_EESDown.setTreeName(treename)
        if doLTF:
          samplesB_LTFUp.setTreeName(treename)
          samplesB_LTFDown.setTreeName(treename)
        if doJTF:
          samplesB_JTFUp.setTreeName(treename)
          samplesB_JTFDown.setTreeName(treename)
        
        # RENORMALIZE WJ
        print ">>> "
        if normalizeWJ and channel!="emu":
            LOG.header("%s: WJ renormalization" % (channel))
            samples.renormalizeWJ(baseline,QCD=doQCD,reset=True,verbosity=verbosityWJ)
            # TODO renormalize WJ in other sample sets
        else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        var, width, a, b = "m_sv", 5, 0, 350
        kwargs = { 'process': 'xtt', 'analysis': "LowMassDiTau" }
        if doNominal:
            writeDataCardHistograms(samples,           channel, var, width, a, b, recreate=recreateDC, **kwargs )
        if doShapes:
          if doEES:
            writeDataCardHistograms(samplesB_EESUp,    channel, var, width, a, b, EES="Up",   filter=['TT','ST'],  **kwargs )
            writeDataCardHistograms(samplesB_EESDown,  channel, var, width, a, b, EES="Down", filter=['TT','ST'],  **kwargs )
          if doJTF and "tau" in channel:
            writeDataCardHistograms(samplesB_JTFUp,    channel, var, width, a, b, JTF="Up",   filter=['TT','ST','WJ'],  **kwargs )
            writeDataCardHistograms(samplesB_JTFDown,  channel, var, width, a, b, JTF="Down", filter=['TT','ST','WJ'],  **kwargs )
          if doTES and "tau" in channel:
            writeDataCardHistograms(samplesB_TESUp,    channel, var, width, a, b, TES="Down", filter=['TT','ST','DY'], **kwargs )
            writeDataCardHistograms(samplesB_TESDown,  channel, var, width, a, b, TES="Up",   filter=['TT','ST','DY'], **kwargs )
          if doJEC:
            writeDataCardHistograms(samples,           channel, var, width, a, b, JES="Up",   **kwargs )
            writeDataCardHistograms(samples,           channel, var, width, a, b, JES="Down", **kwargs )
          if doJER:
            writeDataCardHistograms(samples,           channel, var, width, a, b, JER="Up",   **kwargs )
            writeDataCardHistograms(samples,           channel, var, width, a, b, JER="Down", **kwargs )
          if doZpt:
            writeDataCardHistograms(samplesB_ZptDown,  channel, var, width, a, b, Zpt="Down", filter=['DY'], **kwargs )
            writeDataCardHistograms(samplesB_ZptUp,    channel, var, width, a, b, Zpt="Up",   filter=['DY'], **kwargs )
          if doTTpt:
            writeDataCardHistograms(samplesB_TTptDown, channel, var, width, a, b, TTpt="Down", filter=['TT'], **kwargs )
            writeDataCardHistograms(samplesB_TTptUp,   channel, var, width, a, b, TTpt="Up",   filter=['TT'], **kwargs )
          if doQCD_WJ:
            writeDataCardHistograms(samplesB_QCD_WJDown, channel, var, width, a, b, QCD_WJ="Down", filter=['WJ'], **kwargs )
            writeDataCardHistograms(samplesB_QCD_WJUp,   channel, var, width, a, b, QCD_WJ="Up",   filter=['WJ'], **kwargs )
            
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


