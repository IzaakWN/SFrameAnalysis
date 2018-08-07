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
doStack = False; doDatacard = True
if args.noWJrenorm: normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands



    ##########################
    # writeDataCardHistogram #
    ##########################

def writeDataCard(sampleset, channel, var, binWidth, xmin, xmax, **kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    
    global SUSY_bbA, VLQ_bqX, VLQ_bqX_MB300, VLQ_bqX_MB450
    verbosity     = kwargs.get('verbosity',   0               )
    filter        = kwargs.get('filter',      [ ]             )
    process       = kwargs.get('process',     "xtt"           )
    analysis      = kwargs.get('analysis',    "LowMassDiTau"  )
    DIR           = kwargs.get('DIR',         DATACARDS_DIR   )
    recreate      = kwargs.get('recreate',    False           )
    tag           = kwargs.get('tag',         ""              ) # WEIGHTED
    extracut      = kwargs.get('extracut',    ""              )
    replacecut    = kwargs.get('replacecut',  None            )
    extraweight   = kwargs.get('extraweight', ""              )
    E             = kwargs.get('E',           "13TeV"         )
    unclabel      = kwargs.get('unclabel',    ""              )
    masses        = kwargs.get('masses',      range(13,83,3)  )
    TES           = kwargs.get('TES',         ""              )
    EES           = kwargs.get('EES',         ""              )
    JES           = kwargs.get('JES',         ""              )
    JER           = kwargs.get('JER',         ""              )
    UncEn         = kwargs.get('UncEn',       ""              )
    LTF           = kwargs.get('LTF',         ""              )
    JTF           = kwargs.get('JTF',         ""              )
    Zpt           = kwargs.get('Zpt',         ""              )
    TTpt          = kwargs.get('TTpt',        ""              )
    QCD           = kwargs.get('QCD',         ""              )
    shiftQCD      = kwargs.get('shiftQCD',    0               ) # e.g 0.30
    nBins         = int(kwargs.get('nBins',   (xmax-xmin)/binWidth ))
    option        = 'RECREATE' if recreate else 'UPDATE'
    doShift       = TES or EES or LTF or JTF or Zpt or TTpt or JES or JER or UncEn
    
    # SELECTIONS
    isocuts         = "iso_cuts==1"
    triggers        = "abs(eta_1)<2.1 && trigger_cuts==1"
    iso1            = "iso_1<0.15" if "mutau" in channel else "iso_1<0.10"
    iso2            = "iso_2==1"
    vetos           = "lepton_vetos==0"
    baseline        = "%s && %s && %s && q_1*q_2<0" % (isocuts,vetos,triggers)
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
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets == 1 && nfjets == 0"), "_bbA_pt20_j30"      ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets20 == 1 && nfjets == 0"), "_bbA_pt20_j20"    ),
      #("1btag",  "%s && %s"%(baseline,"ncbtag20 == 1 && ncjets20 == 1 && nfjets == 0 && pzeta_disc>-30"), "_bbA_pt20_j20_Dzeta-30" ),
      #("1btag",  "%s && %s"%(baseline,category_bbA.replace('btag','btag20').replace('cjets','cjets20').replace('fjets','fjets20')), "_bbA_pt20_fj20" ),
      #("1btag",  "%s && %s"%(baseline,category_bbA.replace(' && nfjets == 0','')), "_bbA_fj"               ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"pzeta_disc>-10"), "_bbA_Dzeta-10"                ),
      ("1btag",  "%s && %s && %s"%(baseline,category_bbA_NV,"pzeta_disc>-40 && pfmt_1<40"),                ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"met<30"),         "_bbA_met30"                   ),
      #("1btag",  "%s && %s && %s"%(baseline,category_bbA,"pfmt_1<20"),      "_bbA_mt20"                    ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0"), "_noOpt"              ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0"), "_noOpt"              ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2.5"), "_dphi2p5" ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && pfmt_1<80"), "_mt80"  ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && met<60 && pfmt_1<40"), "_met60_mt40" ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj>2 && met<60 && pfmt_1<40"), "_met60_mt40" ),
      #("1b1f",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 1 && nfjets  > 0 && pfmt_1<60 && met<40"), "_mt60_met40" ),
      #("1b1c",   "%s && %s" % (baseline,"ncbtag > 0 && ncjets == 2 && nfjets == 0 && pfmt_1<60 && met<40"), "_mt60_met40" ),
      ("1b1f",   "%s && %s && %s" % (baseline,category1, "pfmt_1<60"),                                     ),
      ("1b1c",   "%s && %s && %s" % (baseline,category2J,"pfmt_1<60"),                                     ),
    ]
    
    # OPTIMIZATIONS
    if extracut:   selectionsDC = [ (s,"%s && %s"%(c,extracut)) for s,c in selectionsDC ]
    if replacecut: selectionsDC = [ (s,c.replace(*replacecut))  for s,c in selectionsDC ]
    
    # FILE LOGISTICS
    if len(selectionsDC[0])>2:
      tag       = selectionsDC[0][2]+tag
      selectionsDC = [c[:2] for c in selectionsDC]
    outdir      = "%s%s/" % (DIR,"datacards" if "datacards" not in DIR else "")
    ensureDirectory(outdir)
    outfilename = outdir + makeDataCardOutputName(process,analysis,channel,tag=tag)
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
      samples_dict["observed"] = [( "data_obs", "" )]
    
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        if not any(fkey in key or key in fkey for fkey in filter):
          samples_dict.pop(key,None)

    # SIGNAL mass points
    if not filter or 'signal' in filter:
      extraweight = ""
      for mass, filterEff in SUSY_bbA:
        #extraweight = "getBosonPtWeight(%s,pt_genboson)"%mass; kwargs['label'] = "_weighted"
        samples_dict['A*%d'%mass] = [( "ATT-M%d"%mass, "" )]
      for mass, filterEff in VLQ_bqX:
        samples_dict['B*%d*%d'%(170,mass)] = [( "XTT-MB%d-M%d"%(170,mass), "")]
      for mass, filterEff in VLQ_bqX_MB300:
        samples_dict['B*%d*%d'%(300,mass)] = [( "XTT-MB%d-M%d"%(300,mass), "")]
      for mass, filterEff in VLQ_bqX_MB450:
        samples_dict['B*%d*%d'%(450,mass)] = [( "XTT-MB%d-M%d"%(450,mass), "")]
    
    # PRINT
    if verbosity>0 or not doShift:
      print ">>> selections:"
      for cutname, cut in selectionsDC:
        print ">>>   %-14s %s"%(cutname,cut)
      print ">>> "
    
    # SYSTEMATIC UNCERTAINTY
    channel0    = channel.replace("tau","t").replace("mu","m")
    
    # LABELS
    #if shiftQCD and 'QCD' in samples_dict:
    #  samples_dict['QCD'].append(( "QCD_yield_QCD_%s_%sDown"   % (channel0,E), "" ))
    #  samples_dict['QCD'].append(( "QCD_yield_QCD_%s_%sUp"     % (channel0,E), "" ))
    #else: samples_dict.pop('QCD',None) # only run QCD if it's also shifted
    if TES:     unclabel += "_CMS_%s_shape_t_%s_%s%s"          % (process,channel0,E,TES)
    if JES:     unclabel += "_CMS_%s_shape_jes_%s%s"           % (process,         E,JES)
    if JER:     unclabel += "_CMS_%s_shape_jer_%s%s"           % (process,         E,JER)
    if UncEn:   unclabel += "_CMS_%s_shape_uncEn_%s%s"         % (process,         E,UncEn)
    if EES:     unclabel += "_CMS_%s_shape_e_%s_%s%s"          % (process,channel0,E,EES)
    if LTF:     unclabel += "_CMS_%s_shape_ZL_%s_%s%s"         % (process,channel0,E,LTF)
    #if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s%s"    % (process,channel0,E,JTF) # channel dependent
    if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s%s"    % (process,         E,JTF)
    #if Zpt:     unclabel += "_CMS_%s_shape_dy_%s_%s%s"         % (process,channel0,E,Zpt) # channel dependent
    if Zpt:     unclabel += "_CMS_%s_shape_dy_%s%s"            % (process,         E,Zpt)
    if TTpt:    unclabel += "_CMS_%s_shape_ttbar_%s%s"         % (process,         E,TTpt)
    if QCD:     unclabel += "_CMS_%s_yield_QCD_%s_%s%s"        % (process,channel0,E,QCD)
    
    # LOOP over CATEGORIES
    skipWJrenorm = 'emu' in channel or 'WJ' not in samples_dict
    skipTTrenorm = 'TT' not in samples_dict
    print ">>> writing %s(%d,%s,%s) shapes to %s (%sd)" % (var,nBins,xmin,xmax,outfilename,option)
    if unclabel: print ">>> systematic uncertainty label = " + color("%s" % (unclabel.lstrip('_')), color="grey")
    for category, selection in selectionsDC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color = "magenta", bold=True)
        
        # MAKE DIR
        sampleset.refreshMemory()
        (dir,dirname) = makeDataCardTDir(outfile,category)
        
        # WRITE selection string
        if recreate:
          canvas, pave = canvasWithText(selection,title=category)
          canvas.Write("selection")
          canvas.Close()
        
        # RENORMALIZE WJ
        if not skipWJrenorm:
          QCDshift = shiftQCD if QCD else 0.0
          shifts   = '_jes%s'%JES if JES else '_jer%s'%JER if JER else "_UncEn%s"%UncEn if UncEn else ""
          replaceweights = [("1/ttptweight","ttptweight_runI/ttptweight"),('getZpt(pt_genboson)',"getZpt_HTT(m_genboson,pt_genboson)")]
          samples.renormalizeWJ(baseline,QCDshift=QCDshift,shift=shifts,replaceweight=replaceweights,verbosity=verbosityWJ)
          skipWJrenorm = True
          print ">>> "
        
        # TT RENORMALIZATION
        if not skipTTrenorm:
          shifts = '_jes%s'%JES if JES else '_jer%s'%JER if JER else ""
          sampleset.renormalizeTT(selection,baseline=baseline,verbosity=verbosityWJ)
        
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
            
            #histQCD = None
            for sampleinfo in samples_dict[samplename]:
                
                subsample, extracuts = sampleinfo[:2]
                extraweight = ""
                if len(sampleinfo)>2: extraweight = sampleinfo[2]
                print ">>>   %5s"%(subsample.ljust(14)), # TODO: make table instead
                
                # SETUP NAMES
                name = subsample+unclabel
                cuts = combineCuts(selection,extracuts,"%s<%s && %s<%s"%(xmin,var,var,xmax))
                
                # MAKE HIST
                gROOT.cd()
                hist = None
                if 'QCD' in subsample: # QCD
                  #if "Down" in subsample and histQCD:
                  #    hist = histQCD.Clone(name)
                  #    hist.Scale(1-shiftQCD)
                  #elif "Up" in subsample and histQCD:
                  #    hist = histQCD.Clone(name)
                  #    hist.Scale(1+shiftQCD)
                  #else:
                  #    hist = sampleset.QCD(var,nBins,xmax,xmin,cuts,name=name,weight=extraweight,verbosity=1)
                  #    histQCD = hist.Clone(name+"_QCD_clone") # don't calculate QCD trice!
                  hist = sampleset.QCD(var,nBins,xmin,xmax,cuts,name=name,weight=extraweight,shift=shiftQCD)
                  #if "Down" in subsample: hist.Scale(1-shiftQCD)
                  #if "Up"   in subsample: hist.Scale(1+shiftQCD)
                  if hist is None:
                      LOG.warning("QCD histogram failed!")
                      continue
                  hist.SetOption("HIST")
                else:
                  hist = sample.hist(var,nBins,xmin,xmax,cuts,name=name,weight=extraweight,verbosity=1)
                  hist.SetOption("E0" if sample.isData else "EHIST")
                hist.GetXaxis().SetTitle(var)
                hist.SetLineColor(hist.GetFillColor())
                hist.SetFillColor(0)
                
                for i,bin in enumerate(hist):
                  if bin<0:
                    print ">>> replace bin %d (%.3f<0) of \"%s\""%(i,bin,hist.GetName())
                    hist.SetBinContent(i,0)
                
                # WRITE HIST
                dir.cd()
                hist.Write(name,TH1D.kOverwrite)
                print "->  written %8.1f events (%5d entries)"%(hist.GetSumOfWeights(),hist.GetEntries())
                gROOT.cd()
                deleteHist(hist)
                
            #if histQCD: deleteHist(histQCD)
    outfile.Close()
    print ">>>\n>>> "
    


def makeDataCardOutputName(process, analysis, channel, E="13TeV", tag=""):
    """Make name of output file."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    
    if "t" in channel:
        if   "m" in channel: channel = "mt"
        elif "e" in channel: channel = "et"
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = "em"
    else: print ">>> makeOutputName: channel not found!"
    #var = var.replace('pfmt_1','mt')
    
    outputname = "%s_%s.inputs-%s-%s%s.root" % (process,channel,analysis,E,tag)
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
    global samples_TESUp, samples_TESDown, samples_EESUp, samples_EESDown
    
    # USER OPTIONS
    global channels
    #if args.category > -1: selectCategory(args.category)
    #if args.channel:       selectChannel(args.channel)
    if args.etau or args.mutau:
        channels = [ ]
        if args.etau:  channels.append("etau")
        if args.mutau: channels.append("mutau")
    
    # LOOP over CHANNELS
    for channel in channels:
        print ">>>\n>>>"
        
        # SET TREENAME
        treename = "tree_%s"%channel
        if useCutTree and "emu" not in channel:
          treename = "tree_%s_cut_relaxed"%channel
        samples.setChannel(channel,treename=treename)
        if doTES:
          samples_TESUp.setChannel(  channel,treename=treename)
          samples_TESDown.setChannel(channel,treename=treename)
        if doEES:
          samples_EESUp.setChannel(  channel,treename=treename)
          samples_EESDown.setChannel(channel,treename=treename)
        if doLTF:
          samples_LTFUp.setChannel(  channel,treename=treename)
          samples_LTFDown.setChannel(channel,treename=treename)
        if doZpt:
          samples_ZptUp.setChannel(  channel,treename=treename)
          samples_ZptDown.setChannel(channel,treename=treename)
        if doTTpt:
          samples_TTptUp.setChannel(  channel,treename=treename)
          samples_TTptDown.setChannel(channel,treename=treename)
        
        ## RENORMALIZE WJ
        #print ">>> "
        #if normalizeWJ and channel!="emu":
        #  LOG.header("%s: WJ renormalization" % (channel))
        #  samples.renormalizeWJ(baseline,QCD=doQCD,reset=True,verbosity=verbosityWJ)
        #  if doQCDshift:
        #    samples_QCDUp.renormalizeWJ(baseline,QCD=doQCD,reset=True,verbosity=verbosityWJ)
        #    samples_QCDDown.renormalizeWJ(baseline,QCD=doQCD,reset=True,verbosity=verbosityWJ)
        #else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        #print ">>> "
        
        # DIRECTORIES
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,globalTag)
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        var, width, xmin, xmax = "m_sv", 5, 0, 350
        dargs  = (channel, var, width, xmin, xmax)
        kwargs = { 'process': 'xtt', 'analysis': "LowMassDiTau", 'tag': "" }
#         if doNominal:
#             writeDataCard(samples,          *dargs, recreate=recreateDC, **kwargs )
        if doShapes:
#           if doQCDshift:
#             writeDataCard(samples,          *dargs, QCD="Down", filter=['WJ','QCD'], shiftQCD=-0.20, **kwargs )
#             writeDataCard(samples,          *dargs, QCD="Up",   filter=['WJ','QCD'], shiftQCD=+0.20, **kwargs )
#           if doEES and "e" in channel:
#             writeDataCard(samples_EESUp,    *dargs, EES="Up",   **kwargs )
#             writeDataCard(samples_EESDown,  *dargs, EES="Down", **kwargs )
#             writeDataCard(samples_EESUp,    *dargs, EES="Up",   filter=['DY'], **kwargs )
#             writeDataCard(samples_EESDown,  *dargs, EES="Down", filter=['DY'], **kwargs )
#           if doLTF and "tau" in channel:
#             writeDataCard(samples_LTFUp,    *dargs, LTF="Up",   filter=['DY'], **kwargs )
#             writeDataCard(samples_LTFDown,  *dargs, LTF="Down", filter=['DY'], **kwargs )
#           if doTES and "tau" in channel:
#             writeDataCard(samples_TESUp,    *dargs, TES="Down", filter=['TT','DY','signal'], **kwargs )
#             writeDataCard(samples_TESDown,  *dargs, TES="Up",   filter=['TT','DY','signal'], **kwargs )
#             writeDataCard(samples_TESUp,    *dargs, TES="Down", filter=['DY'], **kwargs )
#             writeDataCard(samples_TESDown,  *dargs, TES="Up",   filter=['DY'], **kwargs )
#           if doJEC:
#             writeDataCard(samples,          *dargs, JES="Up",   **kwargs )
#             writeDataCard(samples,          *dargs, JES="Down", **kwargs )
#           if doJER:
#             writeDataCard(samples,          *dargs, JER="Up",   **kwargs )
#             writeDataCard(samples,          *dargs, JER="Down", **kwargs )
#           if doUncEn:
#             writeDataCard(samples,          *dargs, UncEn="Up",   **kwargs )
#             writeDataCard(samples,          *dargs, UncEn="Down", **kwargs )
#           if doZpt:
#             writeDataCard(samples_ZptDown,  *dargs, Zpt="Down",  filter=['DY'], **kwargs )
#             writeDataCard(samples_ZptUp,    *dargs, Zpt="Up",    filter=['DY'], **kwargs )
          if doTTpt:
            writeDataCard(samples_TTptDown, *dargs, TTpt="Down", filter=['TT'], **kwargs )
            writeDataCard(samples_TTptUp,   *dargs, TTpt="Up",   filter=['TT'], **kwargs )
        
        # OTPIMIZATIONS
        optimizations  = [ ]
        #optimizations += [("_bptgt20", ("ncbtag>0","ncbtag20>0")),("_bptgt30", "")]
        #optimizations += [( "_mt%s"%m,           "pfmt_1<%s"%m               ) for m in [20,30,40,50,60,70,80]]
        #optimizations += [( "_met%s"%M,          "met<%s"%M                  ) for M in [20,30,40,50,60,70,80]]
        #optimizations += [( "_dz%s"%d,           "pzeta_disc>%s"%d           ) for d in [-20,-30,-40,-50,-60,-70,-80]]
        #optimizations += [( "_dz%s_mt%s"%(m,M),  "pzeta_disc>%s && pfmt_1<%s"%(d,m) ) for m in [30,40,50,60,70] for d in [-30,-40,-50,-60,-70]]
        #optimizations += [( "_mt%s_met%s"%(m,M), "pfmt_1<%s && met<%s"%(m,M) ) for m in [30,40,50,60,70] for M in [30,40,50,60,70,80]]
        for tag, optimization in optimizations:
           dargs   = (channel, var, width, xmin, xmax)
           if isinstance(optimization,tuple):
             kwargs = { 'process': 'xtt', 'analysis': "LowMassDiTau", 'replacecut': optimization }
           else:
             kwargs = { 'process': 'xtt', 'analysis': "LowMassDiTau", 'extracut': optimization }
           writeDataCard(samples, *dargs, recreate=True, tag=tag, **kwargs )
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"
    

