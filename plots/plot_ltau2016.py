#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

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
description = '''This script make plots.'''
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
    args.configFile = "PlotTools/config_emu2016.py" if args.emu else "PlotTools/config_ltau2016.py"

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
doStack = True; doDataCard = False
if args.noWJrenorm: normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
#setVerbose(args.verbose)
exec commands



    ###############
    # stack plots #
    ###############

def plotStacks(samples, channel, **kwargs):
    """Plot stacked histograms with data."""
    LOG.header("%s channel: Stacks plots %s"%(channel,samples.name))
    
    global plotlabel
    DIR         = kwargs.get('DIR', "%s/%s" % (PLOTS_DIR,channel))
    label       = plotlabel + samples.label + kwargs.get('label', "")
    ensureDirectory(DIR)
    
    stack       = True #and False
    staterror   = True
    errorbars   = (not staterror)
    data        = True
    blind       = True
    scaleup     = True
    ratio       = data
    
    # LOOP over SELECTIONS
    for selection in selections:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),selection.name.replace(' ','_')), color = "magenta", bold=True)
        
        samples.renormalizeTT(selection,baseline=baseline)
        
        # LOOP over VARIABLES
        for variable in variables:
            if not variable.plotForSelection(selection):
              print ">>> plotStacks: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
            if "restr" in selection.name and not variable.isPartOf('m_2'):
              print ">>> plotStacks: ignoting %s for %s"%(variable.printWithBinning(),selection); continue
            
            # NAME
            filename = "%s/%s_%s%s.png" % (DIR,variable.filename,selection.filename,label)
            filename = makeFileName(filename)
            
            # TITLE
            name  = variable.name
            title = "%s: %s" % (channel,selection.name)
            title = title.replace("category 1.2","optimized category 1").replace("category 2.2","optimized category 2")
            
            # LEGEND POSITION
            position = variable.position
            if "dxy_Sig" in name or "eta_" in name[:6] or "d0" in name or "eRatio" in name:
              position = "leftleft"
            logy = variable.logy
            
            # QCD
            QCD = doQCD and ("gen_match" not in variable.name or "npu" not in variable.name)
            
            # PLOT
            plot = samples.plotStack(variable,selection,name=name,title=title,channel=channel,QCD=QCD)
            plot.plot(stack=stack,position=position,staterror=staterror,logy=logy,ratio=ratio,errorbars=errorbars,data=data,blind=blind,scaleup=scaleup)
            plot.saveAs(filename)
            
            # RESET CUTS
            #if doSignalUpScaling:
            #    for sample in samples:
            #        if sample.isSignal: sample.scale = sample.scaleBU
            


    #######################
    # Measure OS/SS ratio #
    #######################
    
def measureOSSSratios(samples, channel, **kwargs):
    """Measure the OS/SS ratios."""
    print header("%s channel: Measure OS/SS ratio" % channel)
    
    category_bbA     = "ncbtag==1 && ncjets==1 && nfjets==0" # no optimizations
    category_bbA2    = "ncbtag >0 && ncbtag==ncjets && nfjets==0"
    category_bbA_rel = "ncbtag >0"
    category1        = "ncbtag>0 && ncjets==1 && nfjets >0"
    category2J       = "ncbtag>0 && ncjets==2 && nfjets==0"
    category1_rel    = "ncbtag>0 && ncjets>0 && nfjets >0"
    category2J_rel   = "ncbtag>0 && ncjets>0 && nfjets==0"
    
    categories      = [
        ("baseline",                 "%s"       % (baseline)),
        ("baseline, m_sv<50",        "%s && %s" % (baseline,"m_sv<50")),
        ("baseline, 50<=m_sv<100",   "%s && %s" % (baseline,"50<=m_sv && m_sv<100")),
        ("baseline, 100<=m_sv<150",  "%s && %s" % (baseline,"100<=m_sv && m_sv<150")),
        ("baseline, 150<=m_sv",      "%s && %s" % (baseline,"150<=m_sv")),
        ("1b1f",                     "%s && %s"       % (baseline,category1_rel)),
        ("1b1f, m_sv<50",            "%s && %s && %s" % (baseline,category1_rel,"m_sv<50")),
        ("1b1f, 50<=m_sv<100",       "%s && %s && %s" % (baseline,category1_rel,"50<=m_sv && m_sv<100")),
        ("1b1f, 100<=m_sv<150",      "%s && %s && %s" % (baseline,category1_rel,"100<=m_sv && m_sv<150")),
        ("1b1f, 150<=m_sv",          "%s && %s && %s" % (baseline,category1_rel,"150<=m_sv")),
        ("1b1c",                     "%s && %s"       % (baseline,category2J_rel)),
        ("1b1c, m_sv<50",            "%s && %s && %s" % (baseline,category2J_rel,"m_sv<50")),
        ("1b1c, 50<=m_sv<100",       "%s && %s && %s" % (baseline,category2J_rel,"50<=m_sv && m_sv<100")),
        ("1b1c, 100<=m_sv<150",      "%s && %s && %s" % (baseline,category2J_rel,"100<=m_sv && m_sv<150")),
        ("1b1c, 150<=m_sv",          "%s && %s && %s" % (baseline,category2J_rel,"150<=m_sv")),
        ("1 b tag + veto",                 "%s && %s"       % (baseline,category_bbA)),
        ("1 b tag + veto, m_sv<50",        "%s && %s && %s" % (baseline,category_bbA,"m_sv<50")),
        ("1 b tag + veto, 50<=m_sv<100",   "%s && %s && %s" % (baseline,category_bbA,"50<=m_sv && m_sv<100")),
        ("1 b tag + veto, 100<=m_sv<150",  "%s && %s && %s" % (baseline,category_bbA,"100<=m_sv && m_sv<150")),
        ("1 b tag + veto, 150<=m_sv",      "%s && %s && %s" % (baseline,category_bbA,"150<=m_sv")),
        ("1 b tag",                 "%s && %s"       % (baseline,category_bbA_rel)),
        ("1 b tag, m_sv<50",        "%s && %s && %s" % (baseline,category_bbA_rel,"m_sv<50")),
        ("1 b tag, 50<=m_sv<100",   "%s && %s && %s" % (baseline,category_bbA_rel,"50<=m_sv && m_sv<100")),
        ("1 b tag, 100<=m_sv<150",  "%s && %s && %s" % (baseline,category_bbA_rel,"100<=m_sv && m_sv<150")),
        ("1 b tag, 150<=m_sv",      "%s && %s && %s" % (baseline,category_bbA_rel,"150<=m_sv")),
    ]
    variables0      = [ ("pfmt_1",100,0,400)]
    verbosityOSSS   = 0 
    
    # LOOP over SELECTIONS
    for label, cuts in categories:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),label.replace(' ','_')), color = "magenta", bold=True)
        
        # TT RENORMALIZATION
        #if normalizeTT: renormalizeTT(samples, label=label, channel=channel, QCD=doQCD, verbosity=verbosityTT)        
        
        # LOOP over VARIABLES
        for var, nBins, a, b in variables0:
            samples.measureOSSSratio(var,nBins,a,b,cuts,relaxed=True,verbosity=1)
            #samples.measureOSSSratio(var,nBins,a,b,cuts,relaxed=False,verbosity=1)




    ##################
    # Help functions #
    ##################

def ensureDirectory(DIR):
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
    """List all available selections"""

    print ">>> list of available selections:"
    for name, cuts in selections:
        print ">>>\t%s" % name
    print ">>>\t"

def selectCategory(category):
    """Only run for this category"""
    global selections
    if -1 < category < len(selections) and category == round(category):
        print ">>> select selection category %i" % category
        selections = [selections[category]]
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
        if doJTF:
          samplesB_JTFUp.setTreeName(treename)
          samplesB_JTFDown.setTreeName(treename)
        
        # RENORMALIZE WJ
        print ">>> "
        if normalizeWJ and "emu" not in channel:
            LOG.header("%s: WJ renormalization" % (channel))
            if doNominal:
              samples.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
            if doEES:
              samplesB_EESUp.renormalizeWJ(  baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
              samplesB_EESDown.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
            if doJTF:
              samplesB_JTFUp.renormalizeWJ(  baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
              samplesB_JTFDown.renormalizeWJ(baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        if doStack:
            if doNominal:
                plotStacks(samples,         channel,DIR=DIR)
                #measureOSSSratios(samples,channel)
            if drawShifts:
              if doEES and "emu" in channel:
                plotStacks(samplesB_EESUp,  channel,DIR=DIR)
                plotStacks(samplesB_EESDown,channel,DIR=DIR)
              if doJTF:
                plotStacks(samplesB_JTFUp,  channel,DIR=DIR)
                plotStacks(samplesB_JTFDown,channel,DIR=DIR)
              if doTES:
                plotStacks(samplesB_TESUp,channel,DIR=DIR)
                plotStacks(samplesB_TESDown,channel,DIR=DIR)
            
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


