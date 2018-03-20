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
parser.add_argument( "-i", "--config", dest="configFile", type=str, default="PlotTools/config_ltau2017.py", action='store',
                     metavar="CONFIG_FILE", help="name of config file containing the settings, samples, selections and variables" )
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
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                     help="renormalize W+Jets" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
if args.noWJrenorm: normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
setVerbose(args.verbose)
exec commands



    ###############
    # stack plots #
    ###############

def plotStacks(samples, channel, **kwargs):
    """Plot stacked histograms with data."""
    LOG.header("%s channel: Stacks plots" % channel)
    
    global plotlabel
    DIR         = kwargs.get('DIR', "%s/%s" % (PLOTS_DIR,channel))
    label       = plotlabel + kwargs.get('label', "")
    ensureDirectory(DIR)
    
    stack       = True #and False
    staterror   = True
    errorbars   = (not staterror)
    data        = True
    ratio       = data
    
    # LOOP over SELECTIONS
    for selection in selections:
        print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),selection.name.replace(' ','_')), color = "magenta", bold=True)
        
        ## RENORMALIZE WJ
        #print ">>> "
        #if normalizeWJ and channel!="emu":
        #    selectionWJ = selection.selection.replace(' && pfmt_1<100',"")
        #    LOG.header("%s: WJ renormalization" % (channel))
        #    samples.renormalizeWJ("pfmt_1", 200, 80, 200, selectionWJ, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        #else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        #print ">>> "

        
        QCD = False
        if "q_1" in selection.selection and "q_2" in selection.selection: QCD = True and doQCD
                
        # LOOP over VARIABLES
        for variable in variables:
            if not variable.plotForSelection(selection):
              print ">>> plotStacks: Ignoring %s for %s"%(variable,selection); break
            
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
            
            # PLOT
            plot = samples.plotStack(variable, selection, name=name, title=title, channel=channel, QCD=QCD)
            plot.plot(stack=stack, position=position, staterror=staterror, logy=logy, ratio=ratio, errorbars=errorbars, data=data)
            plot.saveAs(filename)
            
            # RESET CUTS
            #if doSignalUpScaling:
            #    for sample in samples:
            #        if sample.isSignal: sample.scale = sample.scaleBU
    




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
#     if args.category > -1: selectCategory(args.category)
#     if args.channel:       selectChannel(args.channel)
#     if args.etau or args.mutau:
#         channels = [ ]
#         if args.etau:  channels.append("etau")
#         if args.mutau: channels.append("mutau")
    
    
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
            samples.renormalizeWJ("pfmt_1", 200, 80, 200, baseline, QCD=doQCD, reset=True, verbosity=verbosityWJ)
        else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
        print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        DIR = "%s/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        if doStack:
            #plotStacks(samples,channel,DIR=DIR)
            plotStacks(samplesB_EESUp,  channel,DIR=DIR,label="_EES1p03")
            plotStacks(samplesB_EESDown,channel,DIR=DIR,label="_EES0p97")
            plotStacks(samplesB_JTFUp  ,channel,DIR=DIR,label="_JTF1p15")
            plotStacks(samplesB_JTFDown,channel,DIR=DIR,label="_JTF0p85")
        
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


