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
parser.add_argument( "-o", "--obs",    dest="obs", nargs='*', type=str, default=[], action='store',
                     metavar="MASS",   help="name of mass observable" )
parser.add_argument( "-c", "--channel", dest="channel", default="", action='store',
                     metavar="CHANNEL", help="run only for this channel" )
parser.add_argument( "-e", "--etau", dest="etau", default=False, action='store_true',
                     help="run only for the etau channel" )
parser.add_argument( "-m", "--mutau", dest="mutau", default=False, action='store_true',
                     help="run only for the mutau channel" )
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                     help="renormalize W+Jets" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="make script verbose" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()
if not args.configFile:
    args.configFile = "PlotTools/config_ltau2017.py"

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
doStack = False; doDatacard = True
normalizeWJ = normalizeWJ and not doFakeRate and not args.noWJrenorm
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

def writeDataCard(sampleset, channel, var, binWidth, a, b, **kwargs):
    """Make histogram from a variable in a tree and write to a new root file."""
    
    verbosity   = kwargs.get('verbosity',   0               )
    filter      = kwargs.get('filter',      [ ]             )
    process     = kwargs.get('process',     "ztt"           )
    analysis    = kwargs.get('analysis',    "tes"           )
    DIR         = kwargs.get('DIR',         DATACARDS_DIR   )
    recreate    = kwargs.get('recreate',    False           )
    label       = kwargs.get('label',       ""              ) # WEIGHTED
    unclabel    = kwargs.get('unclabel',    ""              )
    E           = kwargs.get('E',           "13TeV"         )
    JES         = kwargs.get('JES',         ""              )
    JER         = kwargs.get('JER',         ""              )
    UncEn       = kwargs.get('UncEn',       ""              )
    TES         = kwargs.get('TES',         ""              )
    TESscan     = kwargs.get('TESscan',     ""              )
    EES         = kwargs.get('EES',         ""              )
    MES         = kwargs.get('MES',         ""              )
    JTF         = kwargs.get('JTF',         ""              )
    LTF         = kwargs.get('LTF',         ""              )
    FR          = kwargs.get('FR',          ""              )
    Zpt         = kwargs.get('Zpt',         ""              )
    TTpt        = kwargs.get('TTpt',        ""              )
    QCD_WJ      = kwargs.get('QCD_WJ',      ""              )
    shiftQCD    = kwargs.get('shiftQCD',    0               ) # e.g 0.30
    nBins       = int(kwargs.get('nBins',   (b-a)/binWidth ))
    option      = 'RECREATE' if recreate else 'UPDATE'
    doShift     = TES or EES or MES or LTF or JTF or JES or JER or UncEn or Zpt or TTpt or FR
    extraweight = ""
    
    # SELECTIONS
    #ZTTregion   = { }
    iso1        = "iso_1<0.15"
    iso2        = "iso_2==1"
    vetos       = "lepton_vetos==0"
    baselineNDM = "%s && %s && %s && q_1*q_2<0" % (iso1,iso2,vetos)
    baseline    = "%s && %s && %s && q_1*q_2<0 && decayMode_2<11" % (iso1,iso2,vetos)
    label += "_ZTTregion";  ZTTregion = "pfmt_1<40 && 45<m_vis && m_vis<85 && pt_2>30 && dzeta>-25"
    #label += "_ZTTregion_0p05"; ZTTregion = "pfmt_1<40 && 45<m_vis && m_vis<85 && pt_2>30 && dzeta>-25"
    #label += "_ZTTregion2"; ZTTregion = "pfmt_1<50 && 40<m_vis && m_vis<90 && dzeta>-30"
    #label += "_mtlt50";     ZTTregion = "pfmt_1<50"
    #label += "_mtlt50_0p05"; ZTTregion = "pfmt_1<50"
    #label += "_mtlt50_0photon"; ZTTregion = "pfmt_1<50 && nPhoton_2==0"
    
    selectionsDC = [
      ('DM0',    "%s && %s && %s"%(baselineNDM,ZTTregion,"decayMode_2==0")   ),
      ('DM1',    "%s && %s && %s"%(baselineNDM,ZTTregion,"decayMode_2==1")   ),
      ('DM10',   "%s && %s && %s"%(baselineNDM,ZTTregion,"decayMode_2==10")  ),
      #('DM11',  "%s && %s && %s"%(baselineNDM,ZTTregion,"decayMode_2==11")  ),
      #('all',   "%s && %s && %s"%(baselineNDM,ZTTregion,"decayMode_2<11")   ),
    ]
    
    # RESTRICT
    if 'm_2' in var:
      selectionsDC = [(n,s+(" && 0.85<m_2 && m_2<1.35" if 'DM10' in n else
                            " && 0.35<m_2 && m_2<1.20" if 'DM1'  in n else
                            " && %s<%s && %s<%s"%(a,var,var,b))) for n, s in selectionsDC ]
      if binWidth==0.05: label += "_0p05"
    
    # MEASUREMENT
    if var=="m_2": selectionsDC = [s for s in selectionsDC if s[0]!="DM0"]
    
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
      'QCD':   [   ( 'VV',     ""               ), ],
    }
    
    # COMPONENTS
    if TESscan:
      samples_dict = { 'DY':  [( 'ZTT_TES%s'%TESscan, "gen_match_2==5" ),],
                       'QCD': [( 'QCD_TES%s'%TESscan, ""               ),],
                       'JTF': [( 'JTF_TES%s'%TESscan, ""               ),],}
    else:
      samples_dict['DY']  = [(s.replace('ZTT','ZTT_TES1.000'),c) for (s,c) in samples_dict['DY'] ]
      samples_dict['QCD'] = [(s.replace('QCD','QCD_TES1.000'),c) for (s,c) in samples_dict['QCD']]
    if TES:
      for key in samples_dict:
        samples_dict[key] = [s for s in samples_dict[key] if "match_2==5" in s[1] or "match_2" not in s[1]]
    if JTF:
      for key in samples_dict:
        samples_dict[key] = [s for s in samples_dict[key] if "match_2!=5" in s[1] or "match_2==6" in s[1] or "match_2" not in s[1]]
    if doFakeRate:
      samples_dict.pop('WJ',  None)
      samples_dict.pop('QCD', None)
      for key in samples_dict:
        samples_dict[key] = [(s,vetoJetTauFakes(c)) for (s,c) in samples_dict[key] if "match_2==6" not in s[1]]
      samples_dict['JTF'] = [('JTF',""),]
    
    # DATA
    if not doShift:
      if  'mutau' in channel: samples_dict['single muon']     = [( 'data_obs', "" )]
      elif 'etau' in channel: samples_dict['single electron'] = [( 'data_obs', "" )]
      elif 'emu'  in channel: samples_dict['single muon']     = [( 'data_obs', "" )]
    
    # FILTER
    if filter:
      for key in samples_dict.keys():
        if not any(fkey in key or key in fkey for fkey in filter):
          samples_dict.pop(key,None)
    
    # PRINT
    if verbosity>0 or not doShift or JES or JER or UncEn:
      print ">>> selections:"
      for cutname, cut in selectionsDC:
        print ">>>   %-12s %s"%(cutname,cut)
      print ">>> "
      print ">>> templates:"
      for sample in samples_dict:
        print ">>>   %-6s %s"%(sample+':',samples_dict[sample])
    
    # SYSTEMATIC UNCERTAINTY
    channel0    = channel.replace("tau","t").replace("mu","m")
    hist_QCD    = None
    name_QCD    = ""
    
    # LABELS
    #if shiftQCD:
    #  samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sDown" % (channel0,E), "" ))
    #  samples_dict['QCD'].append(( "QCD_QCD_Yield_%s_%sUp"   % (channel0,E), "" ))
    #else: samples_dict.pop('QCD',None) # only run QCD if it's also shifted
    if EES:     unclabel += "_CMS_%s_shape_e_%s_%s%s"          %(process,channel0,E,EES)
    if MES:     unclabel += "_CMS_%s_shape_m_%s_%s%s"          %(process,channel0,E,MES)
    if TES:     unclabel += "_CMS_%s_shape_t_%s_%s%s"          %(process,channel0,E,TES)
    if LTF:     unclabel += "_CMS_%s_ZLShape_%s_%s%s"          %(process,channel0,E,LTF)
    #if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s_%s%s" %(process,channel0,E,JTF) # channel dependent
    if JTF:     unclabel += "_CMS_%s_shape_jetTauFake_%s%s"    %(process,         E,JTF) # channel independent
    if FR:      unclabel += "_CMS_%s_shape_jetTauFake_%s%s"    %(process,         E,FR)
    if JES:     unclabel += "_CMS_%s_shape_jes_%s%s"           %(process,         E,JES)
    if JER:     unclabel += "_CMS_%s_shape_jer_%s%s"           %(process,         E,JER)
    if UncEn:   unclabel += "_CMS_%s_shape_uncEn_%s%s"         %(process,         E,UncEn)
    if Zpt:     unclabel += "_CMS_%s_shape_dy_%s_%s%s"         %(process,channel0,E,Zpt)
    if TTpt:    unclabel += "_CMS_%s_shape_ttbar_%s_%s%s"      %(process,channel0,E,TTpt)
    if QCD_WJ:  unclabel += "_QCD_extrap_%s_%s%s"              %(channel0,E,QCD_WJ)
    
    # LOOP over CATEGORIES
    print ">>> writing %s shapes to %s (%sd)" % (var,outfilename,option)
    if unclabel: print ">>> systematic uncertainty label = " + color("%s" % (unclabel.lstrip("_")), color="grey")
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
        
        # LOOP over SAMPLES
        for samplename in sorted(samples_dict):
            if not samples_dict[samplename]: continue
            
            # FIND SAMPLE
            sample  = None
            if samplename not in ['QCD','JTF'] and samples_dict[samplename]:
                matches = [ s for s in sampleset if s.isPartOf(samplename,unique=True) ]
                if not matches:
                  LOG.warning('Could not make a datacard histogram: no "%s" sample!' % (samplename),pre="  ")
                  continue
                else: sample = matches[0]
            
            for subsample, extracuts in samples_dict[samplename]:
                printSameLine(">>>   %7s" % (subsample.ljust(10))) # TODO: make table instead
                
                # SETUP NAMES
                name = subsample+unclabel
                cuts = combineCuts(selection,extracuts)
                
                # MAKE HIST
                hist = None
                if 'QCD' in subsample:
                  hist = sampleset.QCD(var,nBins,a,b,cuts,name=name,weight=extraweight,verbosity=0)
                  if hist is None:
                      LOG.warning("QCD histogram failed!")
                      continue
                if 'JTF' in subsample:
                  hist = sampleset.jetFakeRate(var,nBins,a,b,cuts,name=name,weight=extraweight,shift=FR,verbosity=0)
                  if hist is None:
                      LOG.warning("QCD histogram failed!")
                      continue
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
                
        
    outfile.Close()
    print ">>>\n>>> "
    


def makeDataCardOutputName(process, analysis, channel, var, E="13TeV", label=""):
    """Make name of output file."""
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
    if "t" in channel:
        if   "m" in channel: channel = 'mt'
        elif "e" in channel: channel = 'et'
        else: print ">>> makeOutputName: channel not found!"
    elif    "em" in channel: channel = 'em'
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
    


    ########
    # main #
    ########

def main():
    """Main function."""
    
    #checkDataCardHistograms()
    #exit(0)
    
    # MAKE SAMPLES
    global samples, samplesB, samplesS, samplesD
    global samples_MESUp, samples_MESDown, samples_TESscan
    global samples_LTFUp, samples_LTFDown, samples_JTFUp, samples_JTFDown
    
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
        
        # SET TREENAME
        treename = "tree_%s" % channel
        if useCutTree and "emu" not in channel:
          treename = "tree_%s_cut_relaxed" % channel
        samples.setChannel(channel,treename=treename)
        if doJTF:
          samples_JTFUp.setChannel(  channel,treename=treename)
          samples_JTFDown.setChannel(channel,treename=treename)
        if doLTF:
          samples_LTFUp.setChannel(  channel,treename=treename)
          samples_LTFDown.setChannel(channel,treename=treename)
        if doMES:
          samples_MESUp.setChannel(  channel,treename=treename)
          samples_MESDown.setChannel(channel,treename=treename)
        for label, samples_TES in sorted(samples_TESscan.iteritems()):
          samples_TES.setChannel(channel,treename=treename)
        
        # RENORMALIZE WJ
        print ">>> "
        if normalizeWJ and 'emu' not in channel:
           LOG.header("%s: WJ renormalization" % (channel))
           samples.renormalizeWJ(baseline, verbosity=verbosityWJ)
           if doJTF:
             samples_JTFUp.renormalizeWJ(  baseline, verbosity=verbosityWJ)
             samples_JTFDown.renormalizeWJ(baseline, verbosity=verbosityWJ)
        else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, doFakeRate=%s, user flag=%s, channel=%s)" % (normalizeWJ,doFakeRate,args.noWJrenorm,channel))
        print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        LOG.header("%s channel: Writing histogram for datacards" % channel)
        keys = [ ("ztt","tes","m_2",0.04,0.2,2),
                 #("ztt","tes","m_2",0.05,0.2,2),
                 ("ztt","tes","m_vis",5,40,200),
                 #("ztt","tes","m_vis",8,0,200),
        ]
        if args.obs: keys = [k for k in keys if any(o in k[2] for o in args.obs)]
        for process, analysis, var, width, a, b in keys:
            dargs  = (channel, var, width, a, b)
            kwargs = { 'process': process, 'analysis': analysis, 'label': "" }
            #if doNominal:
            writeDataCard(samples,              *dargs, recreate=False, **kwargs )
            if doFakeRate:
                writeDataCard(samples,          *dargs, FR='Up',   filter=['JTF'],  **kwargs )
                writeDataCard(samples,          *dargs, FR='Down', filter=['JTF'],  **kwargs )
            elif doJTF:
                writeDataCard(samples_JTFUp,    *dargs, JTF='Up',   filter=['TT','DY','ST','WJ','QCD'],  **kwargs )
                writeDataCard(samples_JTFDown,  *dargs, JTF='Down', filter=['TT','DY','ST','WJ','QCD'],  **kwargs )
            if doLTF:
                writeDataCard(samples_LTFUp,    *dargs, LTF='Up',   filter=['DY'],  **kwargs )
                writeDataCard(samples_LTFDown,  *dargs, LTF='Down', filter=['DY'],  **kwargs )
            if doMES:
                writeDataCard(samples_MESUp,    *dargs, MES='Up',   filter=['TT','DY','ST','WJ'], **kwargs )
                writeDataCard(samples_MESDown,  *dargs, MES='Down', filter=['TT','DY','ST','WJ'], **kwargs )
            if doJEC:
                writeDataCard(samples,          *dargs, JES='Up',   **kwargs )
                writeDataCard(samples,          *dargs, JES='Down', **kwargs )
            #if doJER:
            #    writeDataCard(samples,          *dargs, JER='Up',   **kwargs )
            #    writeDataCard(samples,          *dargs, JER='Down', **kwargs )
            #if doUncEn:
            #    writeDataCard(samples,          *dargs, UncEn='Up',   **kwargs )
            #    writeDataCard(samples,          *dargs, UncEn='Down', **kwargs )
            if doTESscan:
              for label, set in sorted(samples_TESscan.iteritems()):
                writeDataCard(set,              *dargs, TESscan=label, filter=['DY',], **kwargs ) #'QCD'
                if doJEC:
                  writeDataCard(set,            *dargs, TESscan=label, filter=['DY',], JES='Up',   **kwargs )
                  writeDataCard(set,            *dargs, TESscan=label, filter=['DY',], JES='Down', **kwargs )
                #if doJER:
                #  writeDataCard(set,            *dargs, TESscan=label, filter=['DY',], JER='Up',   **kwargs )
                #  writeDataCard(set,            *dargs, TESscan=label, filter=['DY',], JER='Down', **kwargs )
                #if doUncEn:
                #  writeDataCard(samples,        *dargs, TESscan=label, filter=['DY',], UncEn='Up',   **kwargs )
                #  writeDataCard(samples,        *dargs, TESscan=label, filter=['DY',], UncEn='Down', **kwargs )
                set.reloadFiles()
            #if doZpt:
            #    writeDataCard(samples_ZptDown,    *dargs, Zpt="Down", filter=["DY"], **kwargs )
            #    writeDataCard(samples_ZptUp,      *dargs, Zpt="Up",   filter=["DY"], **kwargs )
            #if doTTpt:
            #    writeDataCard(samples_TTptDown,   *dargs, TTpt="Down", filter=["ttbar"], **kwargs )
            #    writeDataCard(samples_TTptUp,     *dargs, TTpt="Up",   filter=["ttbar"], **kwargs )
            #if doQCD_WJ:
            #    writeDataCard(samples_QCD_WJDown, *dargs, QCD_WJ="Down", filter=["WJ"], **kwargs )
            #    writeDataCard(samples_QCD_WJUp,   *dargs, QCD_WJ="Up",   filter=["WJ"], **kwargs )
            
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


