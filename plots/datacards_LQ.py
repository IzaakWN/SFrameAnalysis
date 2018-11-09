#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (October 2018)

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
description = """This script make input histograms for the datacards."""
parser = ArgumentParser(prog="datacards",description=description,epilog="Succes!")
parser.add_argument( '-i', "--config",      dest="configFile", type=str, default="", action='store',
                     metavar="CONFIG_FILE", help="name of config file containing the settings, samples, selections and variables" )
parser.add_argument( '-y', "--year",        dest="year", choices=[2016,2017,2018], default=2017, action='store',
                                            help="year of dataset" )
parser.add_argument( '-s', "--category",    dest="category", type=int, default=-1, action='store',
                     metavar="CATEGORY",    help="run only for this category of selection and cuts" )
parser.add_argument( '-c', "--channel",     dest="channels", choices=['tautau','ltau','mutau','etau','emu'], nargs='+', default=['tautau'], action='store',
                     metavar="CHANNEL",     help="run only for this channel" )
#parser.add_argument( '--bbA',               dest="bbA", default=False, action='store_true',
#                                            help="make datacard for bbA categories" )
#parser.add_argument( '--VLQ',               dest="VLQ", default=False, action='store_true',
#                                            help="make datacard for VLQ categories" )
parser.add_argument( '-v', "--verbose",     dest="verbose", default=False, action='store_true',
                                            help="make script verbose" )
parser.add_argument( '-n', "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                                            help="renormalize W+Jets" )
parser.add_argument( '-t', "--tag",         dest="tag", type=str, default="", action='store',
                                            help="tag" )

args = parser.parse_args()
if not args.configFile:
  channel = 'ltau' if "mutau" in args.channels or "etau" in args.channels else args.channels[0]
  args.configFile = "PlotTools/config_%s_LQ_%d.py"%(channel,args.year)

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for datacards_LQ.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
channels = args.channels
doStack, doDatacard = False, True
doQCD, doFakeRate, doFakeFactor = False, False, True
mergeTop = False
if args.noWJrenorm: normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands



    ##########################
    # writeDataCardHistogram #
    ##########################

def writeDataCard(sampleset,channel,var,varname,binWidth,xmin,xmax,**kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    
    verbosity     = kwargs.get('verbosity',   0               )
    filter        = kwargs.get('filter',      [ ]             )
    process       = kwargs.get('process',     'LQ3'           )
    outdir        = kwargs.get('outdir',      DATACARDS_DIR   )
    recreate      = kwargs.get('recreate',    False           )
    tag           = kwargs.get('tag',         args.tag        ) # WEIGHTED
    extracut      = kwargs.get('extracut',    ""              )
    replacecut    = kwargs.get('replacecut',  None            )
    extraweight   = kwargs.get('extraweight', ""              )
    masses        = kwargs.get('masses',      [500,1000,1500] )
    year          = kwargs.get('year',        args.year       )
    CME           = kwargs.get('E',           13              )
    unclabel      = kwargs.get('unclabel',    ""              )
    TES           = kwargs.get('TES',         ""              )
    EES           = kwargs.get('EES',         ""              )
    JES           = kwargs.get('JES',         ""              )
    JER           = kwargs.get('JER',         ""              )
    UncEn         = kwargs.get('UncEn',       ""              )
    LTF           = kwargs.get('LTF',         ""              )
    JTF           = kwargs.get('JTF',         ""              )
    FR            = kwargs.get('FR',          ""              )
    Zpt           = kwargs.get('Zpt',         ""              )
    TTpt          = kwargs.get('TTpt',        ""              )
    QCD           = kwargs.get('QCD',         ""              )
    shiftQCD      = kwargs.get('shiftQCD',    0               ) # e.g 0.30
    nBins         = int(kwargs.get('nBins',   (xmax-xmin)/binWidth ))
    option        = 'RECREATE' if recreate else 'UPDATE'
    doShift       = TES or EES or LTF or JTF or Zpt or TTpt or JES or JER or UncEn
    channel0      = channel.replace('tau','t').replace('mu','m')
    
    # SELECTIONS
    if channel=="tautau":
      idcuts     = "idDecayMode_1==1 && idDecayMode_2==1"
      antiLep    = "idAntiMu_1>=1 && idAntiEle_1>=1 && idAntiMu_2>=1 && idAntiEle_2>=1"
      isocuts    = "idMVAoldDM2017v2_1>=16 && idMVAoldDM2017v2_2>=16"
      vetos      = "extramuon_veto==0 && extraelec_veto==0"
    else:      
      idcuts     = "idDecayMode_2==1"
      antiLep    = "idAntiMu_2>=2 && idAntiEle_2>=1" if "mutau" in channel else "idAntiMu_2>=1 && idAntiEle_2>=8"
      isocuts    = "%s && idMVAoldDM2017v2_2>=16"%("pfRelIso04_all_1<0.15" if "mutau" in channel else "pfRelIso03_all_1<0.10")
      vetos      = "extramuon_veto==0 && extraelec_veto==0 && dilepton_veto==0"
    baseline     = "q_1*q_2<0 && %s && %s && %s && %s"%(idcuts,antiLep,isocuts,vetos)
    signalregion = "pt_1>50 && pt_2>50 && m_vis>95"    
    selectionsDC = [
      ( '1b',       "%s && %s && %s"%(baseline,signalregion,"nbtag>0 && jpt_1>50" ),                         ),
#       ( '1j',       "%s && %s && %s"%(baseline,signalregion,           "njets==1 && jpt_1>50"),              ),
#       ( '2j',       "%s && %s && %s"%(baseline,signalregion,           "njets>=2 && jpt_1>50 && jpt_2>50"),  ),
#       ( '1b1j',     "%s && %s && %s"%(baseline,signalregion,"nbtag==1 && njets==1 && jpt_1>50"),             ),
#       ( '1b2j',     "%s && %s && %s"%(baseline,signalregion,"nbtag==1 && njets>=2 && jpt_1>50 && jpt_2>50"), ),
#       ( '2b2j',     "%s && %s && %s"%(baseline,signalregion,"nbtag>=2 && njets>=2 && jpt_1>50 && jpt_2>50"), ),
#       ( 'geq1b2j',  "%s && %s && %s"%(baseline,signalregion,"nbtag>=1 && njets>=2 && jpt_1>50 && jpt_2>50"), ),
    ]
    
    # OPTIMIZATIONS
    if extracut:   selectionsDC = [ (s,"%s && %s"%(c,extracut)) for s,c in selectionsDC ]
    if replacecut: selectionsDC = [ (s,c.replace(*replacecut))  for s,c in selectionsDC ]
    
    # FILE LOGISTICS
    ensureDirectory(outdir)
    outfilename = makeDataCardOutputName(process,varname,channel0,year=year,E=CME,tag=tag)
    outfilename = "%s/%s"%(outdir,outfilename)
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
    if "tautau"==channel:
      GMT = "genPartFlav_1==5 && genPartFlav_2==5"
      GML = "genPartFlav_1>0 && genPartFlav_2>0 && (genPartFlav_1<5 || genPartFlav_2<5)"
      GMJ = "(genPartFlav_1==0 || genPartFlav_2==0)"
    else:
      GMT = "genPartFlav_2==5"
      GML = "genPartFlav_2>0 && genPartFlav_1<5"
      GMJ = "genPartFlav_2==0"
    samples_dict = {
    # search term     label          extracuts
      'TT':   [    ( 'TTT',    GMT ),
                   ( 'TTL',    GML ),
                   ( 'TTJ',    GMJ ), ],
      'DY':    [   ( 'ZTT',    GMT ),
                   ( 'ZL',     GML ),
                   ( 'ZJ',     GMJ ), ],
      'WJ':    [   ( 'W',      ""  ), ],
      'VV':    [   ( 'VV',     ""  ), ],
      'ST':    [   #( 'STT',    GMT ),
                   #( 'STJ',    GMJ ),
                   ( 'ST',     ""  ), ],
    }
    
    # COMPONENTS
    if doFakeFactor:
      samples_dict.pop('WJ',  None)
      for sample in [s for s in samples_dict if samples_dict[s]==GMJ]:
        samples_dict.pop(sample, None)
      samples_dict['JTF'] = [( 'JTF',    ""  )]
    elif doQCD:
      for sample in [s for s in samples_dict if samples_dict[s]==GMJ]:
        samples_dict.pop(sample, None)
      samples_dict['QCD'] = [( 'QCD',    ""  )]
    if TES:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if GMT in s[1] ]
    if JTF:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if "!=5" in s[1] or "==0" in s[1] ]
    if LTF:
      for key in samples_dict:
        samples_dict[key] = [ s for s in samples_dict[key] if "!=5" in s[1] or "<5" in s[1] ]
    
    # DATA
    if not doShift:
      samples_dict['observed'] = [( 'data_obs', "" )]
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        if not any(fkey in key or key in fkey for fkey in filter):
          samples_dict.pop(key,None)
    
    # SIGNAL mass points
    if not filter or 'signal' in filter:
      extraweight = ""
      for mass in masses:
        samples_dict["LQ3ToTauB_s-channel_M%d"%mass]       = [( "SLQ-s-M%d"%mass, "" )]
        samples_dict["LQ3ToTauB_pair_M%d"%mass]            = [( "SLQ-p-M%d"%mass, "" )]
        samples_dict["VectorLQ3ToTauB_s-channel_M%d"%mass] = [( "VLQ-s-M%d"%mass, "" )]
        samples_dict["VectorLQ3ToTauB_pair_M%d"%mass]      = [( "VLQ-p-M%d"%mass, "" )]
    
    # PRINT
    if verbosity>0 or not doShift:
      print ">>> selections:"
      for cutname, cut in selectionsDC:
        print ">>>   %-14s %s"%(cutname,cut)
      print ">>> "
    
    # SYSTEMATIC UNCERTAINTY
    # TODO: add year
    if TES:     unclabel += "_CMS_%s_shape_t_%s_%s%s"        %(process,channel0,E,TES)
    if JES:     unclabel += "_CMS_%s_shape_jes_%s%s"         %(process,         E,JES)
    if JER:     unclabel += "_CMS_%s_shape_jer_%s%s"         %(process,         E,JER)
    if UncEn:   unclabel += "_CMS_%s_shape_uncEn_%s%s"       %(process,         E,UncEn)
    if EES:     unclabel += "_CMS_%s_shape_e_%s_%s%s"        %(process,channel0,E,EES)
    if LTF:     unclabel += "_CMS_%s_shape_ZL_%s_%s%s"       %(process,channel0,E,LTF)
    #if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s%s"  %(process,channel0,E,JTF) # channel dependent
    if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s%s"  %(process,         E,JTF)
    #if Zpt:     unclabel += "_CMS_%s_shape_dy_%s_%s%s"       %(process,channel0,E,Zpt) # channel dependent
    if Zpt:     unclabel += "_CMS_%s_shape_dy_%s%s"          %(process,         E,Zpt)
    if TTpt:    unclabel += "_CMS_%s_shape_ttbar_%s%s"       %(process,         E,TTpt)
    if QCD:     unclabel += "_CMS_%s_yield_QCD_%s_%s%s"      %(process,channel0,E,QCD)
    
    # LOOP over CATEGORIES
    print ">>> writing %s(%d,%s,%s) shapes to %s (%sd)"%(var,nBins,xmin,xmax,outfilename,option)
    if unclabel: print ">>> systematic uncertainty label = " + color("%s" % (unclabel.lstrip('_')), color="grey")
    for category, selection in selectionsDC:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),category.replace(' ','_')), color="magenta", bold=True)
        
        # MAKE DIR
        sampleset.refreshMemory()
        (dir,dirname) = makeDataCardTDir(outfile,category)
        
        # WRITE selection string
        if recreate:
          canvas, pave = canvasWithText(selection,title=category)
          canvas.Write("selection")
          canvas.Close()
        
        # LOOP over SAMPLES
        for samplename in sorted(samples_dict):
            if not samples_dict[samplename]: continue
            
            # FIND SAMPLE
            sample  = None
            if  'JTF' not in samplename and 'QCD' not in samplename and samples_dict[samplename]:
                matches = [ s for s in sampleset if s.isPartOf(samplename,start=True) ]
                if not matches:
                  LOG.warning('Could not make a datacard histogram: no "%s" sample!'%(samplename),pre="  ")
                  continue
                elif len(matches)>1: LOG.warning('  Found more than one "%s" sample! %s'%(samplename,matches))
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
                if 'JTF' in subsample:
                  hist = sampleset.jetTauFake(var,nBins,xmin,xmax,cuts,name=name,weight=extraweight)
                  if hist is None:
                    LOG.warning("QCD histogram failed!")
                    continue
                  hist.SetOption('HIST')

                elif 'QCD' in subsample:
                  hist = sampleset.QCD(var,nBins,xmin,xmax,cuts,name=name,weight=extraweight,shift=FR)
                  if hist is None:
                    LOG.warning("QCD histogram failed!")
                    continue
                  hist.SetOption('HIST')
                else:
                  hist = sample.hist(var,nBins,xmin,xmax,cuts,name=name,weight=extraweight,verbosity=1)
                  hist.SetOption('E0' if sample.isData else 'EHIST')
                hist.GetXaxis().SetTitle(varname)
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
    


def makeDataCardOutputName(process,varname,channel,year=args.year,E=13,tag=""):
    """Make name of output file."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    channel = channel.replace('tau','t').replace('mu','m')
    outputname = "%s_%s_%s%s.inputs-%s-%sTeV.root"%(process,varname,channel,tag,year,E)
    return outputname
    


def makeDataCardTDir(outfile, category):
    """Make name of directory in root."""
    category = category.replace(' ','_').replace('.','_').replace(',','-')
    dirname = category
    dir = outfile.GetDirectory(dirname)
    if not dir:
      dir = outfile.mkdir(dirname)
      outfilename = '/'.join(outfile.GetPath().replace(":/",'').split('/')[-2:])
      print '>>>   created directory "%s" in %s'%(dirname,outfilename)
    dir.cd()
    return (dir,dirname)
    


    ########
    # main #
    ########

def main():
    """Main function."""
    
    #checkDataCardHistograms()
    #exit(0)
    
    vars = [
      ("pt_1+pt_2+jpt_1",       "st_1", 50, 0, 2500),
      ("pt_1+pt_2+jpt_1+jpt_1", "st_2", 50, 0, 2500),
    ]
    
    # MAKE SAMPLES
    global samples
    #global samples_TESUp, samples_TESDown, samples_EESUp, samples_EESDown
    
    # LOOP over CHANNELS
    for i, channel in enumerate(channels):
        print ">>>\n>>>"
        
        # DIRECTORIES
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,globalTag)
        
        # SET TREENAME
        if i>0:
          samples.setChannel(channel)
          if   "etau" in channel:  samples.replaceWeight("getLeptonTauFake(1","getLeptonTauFake(2")
          elif "mutau" in channel: samples.replaceWeight("getLeptonTauFake(2","getLeptonTauFake(1")
        LOG.header("%s: WJ renormalization" % (channel))
        WJscale = 0.80 if "etau" in channel else 1.0
        print ">>>   scaling %.3f for %s"%(WJscale,baseline)
        sampleWJ = samples.get('WJ',unique=True)
        sampleWJ.resetScale(WJscale)
        print ">>> "
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        for var, varname, width, xmin, xmax in vars:
          dargs  = (channel, var, varname, width, xmin, xmax)
          kwargs = { 'process': 'LQ3', 'masses':masses, 'tag': args.tag }
          if doNominal:
              writeDataCard(samples,          *dargs, recreate=True, **kwargs )
          ###if doShapes:
          ###  if doQCDshift:
          ###    writeDataCard(samples,          *dargs, QCD="Down", filter=['WJ','QCD'], shiftQCD=-0.20, **kwargs )
          ###    writeDataCard(samples,          *dargs, QCD="Up",   filter=['WJ','QCD'], shiftQCD=+0.20, **kwargs )
          ###  if doEES and "e" in channel:
          ###    writeDataCard(samples_EESUp,    *dargs, EES="Up",   **kwargs )
          ###    writeDataCard(samples_EESDown,  *dargs, EES="Down", **kwargs )
          ###    writeDataCard(samples_EESUp,    *dargs, EES="Up",   filter=['DY'], **kwargs )
          ###    writeDataCard(samples_EESDown,  *dargs, EES="Down", filter=['DY'], **kwargs )
          ###  if doLTF and "tau" in channel:
          ###    writeDataCard(samples_LTFUp,    *dargs, LTF="Up",   filter=['DY'], **kwargs )
          ###    writeDataCard(samples_LTFDown,  *dargs, LTF="Down", filter=['DY'], **kwargs )
          ###  if doTES and "tau" in channel:
          ###    writeDataCard(samples_TESUp,    *dargs, TES="Down", filter=['TT','DY','signal'], **kwargs )
          ###    writeDataCard(samples_TESDown,  *dargs, TES="Up",   filter=['TT','DY','signal'], **kwargs )
          ###    writeDataCard(samples_TESUp,    *dargs, TES="Down", filter=['DY'], **kwargs )
          ###    writeDataCard(samples_TESDown,  *dargs, TES="Up",   filter=['DY'], **kwargs )
          ###  if doJEC:
          ###    writeDataCard(samples,          *dargs, JES="Up",   **kwargs )
          ###    writeDataCard(samples,          *dargs, JES="Down", **kwargs )
          ###  if doJER:
          ###    writeDataCard(samples,          *dargs, JER="Up",   **kwargs )
          ###    writeDataCard(samples,          *dargs, JER="Down", **kwargs )
          ###  if doUncEn:
          ###    writeDataCard(samples,          *dargs, UncEn="Up",   **kwargs )
          ###    writeDataCard(samples,          *dargs, UncEn="Down", **kwargs )
          ###  if doZpt:
          ###    writeDataCard(samples_ZptDown,  *dargs, Zpt="Down",  filter=['DY'], **kwargs )
          ###    writeDataCard(samples_ZptUp,    *dargs, Zpt="Up",    filter=['DY'], **kwargs )
          ###  if doTTpt:
          ###    writeDataCard(samples_TTptDown, *dargs, TTpt="Down", filter=['TT'], **kwargs )
          ###    writeDataCard(samples_TTptUp,   *dargs, TTpt="Up",   filter=['TT'], **kwargs )
        
          # OTPIMIZATIONS
          optimizations  = [ ]
          ###optimizations += [("_bptgt20", ("ncbtag>0","ncbtag20>0")),("_bptgt30", "")]
          ###optimizations += [( "_mt%s"%m,           "pfmt_1<%s"%m               ) for m in [20,30,40,50,60,70,80]]
          ###optimizations += [( "_dz%s_mt%s"%(m,M),  "pzeta_disc>%s && pfmt_1<%s"%(d,m) ) for m in [30,40,50,60,70] for d in [-30,-40,-50,-60,-70]]
          for tag, optimization in optimizations:
             okwargs = kwargs.copy()
             if isinstance(optimization,tuple):
               okwargs['replacecut'] = optimization
             else:
               okwargs['extracut'] = optimization
             writeDataCard(samples, *dargs, recreate=True, tag=tag, **okwargs )
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"
    

