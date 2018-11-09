#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (October, 2018)

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
parser.add_argument( "-i", "--config",      dest="configFile", type=str, default="", action='store',
                     metavar="CONFIG_FILE", help="name of config file containing the settings, samples, selections and variables" )
parser.add_argument( '-y', "--year",        dest="year", choices=[2016,2017,2018], default=2017, action='store',
                                            help="year of dataset" )
parser.add_argument( "-s", "--category",    dest="category", type=int, default=-1, action='store',
                     metavar="CATEGORY",    help="run only for this category of selection and cuts" )
parser.add_argument( '-c', "--channel",     dest="channels", choices=['tautau','ltau','mutau','etau','emu'], nargs='+', default=['tautau'], action='store',
                     metavar="CHANNEL",     help="run only for this channel" )
parser.add_argument( "-l", "--list",        dest="list", default=False, action='store_true',
                                            help="list all available categories" )
parser.add_argument( "-t", "--tag",         dest="plottag", type=str, default="", action='store',
                     metavar="TAG",         help="tag for plot files" )
parser.add_argument( "-n", "--no-WJ-renom", dest="noWJrenorm", default=False, action='store_true',
                                            help="do not renormalize W+Jets" )
parser.add_argument( "-p", "--pdf",         dest="pdf", default=False, action='store_true',
                                            help="make pdf version each plot" )
parser.add_argument( "-v", "--verbose",     dest="verbose", default=False, action='store_true',
                                            help="make script verbose" )
# parser.add_argument( "-y", "--verbosity", dest="verbosity", type=int, default=0, action='store',
#                      metavar="VERBOSITY_LEVEL", help="set verbosity level to VERBOSITY_LEVEL" )
args = parser.parse_args()
if not args.configFile:
  channel = 'ltau' if "mutau" in args.channels or "etau" in args.channels else args.channels[0]
  args.configFile = "PlotTools/config_%s_LQ_%d.py"%(channel,args.year)

# LOAD config
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot_LQ_2017.py"%(args.configFile)
settings, commands = loadConfigurationFromFile(args.configFile,verbose=args.verbose)
exec settings
plottag += args.plottag
channels = args.channels
doStack = True; doDataCard = False
normalizeWJ = normalizeWJ and not doFakeRate and not doFakeFactor and not args.noWJrenorm
makePDF = makePDF or args.pdf
loadSettings(globals(),settings,verbose=args.verbose)
exec commands



    ###############
    # stack plots #
    ###############

def plotStacks(samples, channel, **kwargs):
    """Plot stacked histograms with data."""
    LOG.header("%s channel: Stacks plots %s"%(channel,samples.name))
    
    global plottag
    outdir      = kwargs.get('outdir', "%s/%s"%(PLOTS_DIR,channel))
    label       = plottag + samples.label + kwargs.get('label', "")
    ensureDirectory(outdir)
    
    stack       = True #and False
    staterror   = True
    errorbars   = (not staterror)
    data        = drawData
    ratio       = data
    pdf         = makePDF
    
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
        
        # LOOP over VARIABLES
        for variable in variables:
            if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
              print ">>> plotStacks: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
            if "restr" in selection.name and not variable.isPartOf('m_2'):
              print ">>> plotStacks: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
            
            # NAME
            filename = "%s/%s_%s-%s%s.png"%(outdir,variable.filename,channel.replace('mu','m').replace('tau','t'),selection.filename,label)
            filename = makeFileName(filename)
            saveToFile = "" #filename.replace('.png','.root')
            
            # PDFs
            exts  = ['png','pdf'] if pdf else [ ]
            
            # TITLE
            name  = variable.name
            title = "#bf{%s}: %s"%(channel,selection.title)
            if title.count("mumu")>1: title = selection.title
            
            # LEGEND POSITION
            position = variable.position
            if "dxy_Sig" in name or "eta_" in name[:6] or "d0" in name or "eRatio" in name:
              position = "leftleft"
            logy = variable.logy
            
            # QCD
            QCD = doQCD and ("gen_match" not in variable.name or "npu" not in variable.name)
            JFR = doFakeRate or doFakeFactor
            
            # PLOT
            plot = samples.plotStack(variable,selection,name=name,title=title,channel=channel,QCD=QCD,JFR=JFR,saveToFile=saveToFile,data=data)
            plot.plot(stack=stack,position=position,staterror=staterror,logy=logy,ratio=ratio,errorbars=errorbars,data=data)
            plot.saveAs(filename,ext=exts)
            plot.close()
            


    ##################
    # Help functions #
    ##################

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    
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
    
    # USER OPTIONS
    global channels
    #if args.category > -1: selectCategory(args.category)
    #if args.channel:       selectChannel(args.channel)
    
    
    # LOOP over CHANNELS
    for i, channel in enumerate(channels):
        print ">>>"
        
        # SET TREENAME
        if i>0:
          samples.setChannel(channel)
          if   "etau" in channel:  samples.replaceWeight("getLeptonTauFake(1","getLeptonTauFake(2")
          elif "mutau" in channel: samples.replaceWeight("getLeptonTauFake(2","getLeptonTauFake(1")
          #for selection in selections:
          #  selection.replace(baseline,)
          #  baseline = ...
        
        # RENORMALIZE WJ
        #print ">>> "
        #if normalizeWJ and "emu" not in channel and "tautau" not in channel:
        #  LOG.header("%s: WJ renormalization" % (channel))
        #  if doNominal:
        #    if WJscale>0:
        #      print ">>>   reuse scale %.3f for %s"%(WJscale,baseline)
        #      sampleWJ = samples.get('WJ',unique=True)
        #      sampleWJ.resetScale(WJscale)
        #    else:
        #      samples.renormalizeWJ(baseline,QCD=doQCD,reset=True,verbosity=verbosityWJ)
        #else: LOG.warning('Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel="%s")' % (normalizeWJ,args.noWJrenorm,channel))
        LOG.header("%s: WJ renormalization" % (channel))
        WJscale = 0.80 if "etau" in channel else 1.0
        print ">>>   scaling %.3f for %s"%(WJscale,baseline)
        sampleWJ = samples.get('WJ',unique=True)
        sampleWJ.resetScale(WJscale)
        print ">>> "
        
        # DIRECTORIES
        dirlabel = globalTag
        outdir = "%s/LQ_2017/%s%s"%(PLOTS_DIR,channel,dirlabel)
        
        # MAIN ROUTINES
        if doStack:
            if doNominal:
                plotStacks(samples,channel,outdir=outdir)
        
    


if __name__ == '__main__':
    main()
    print ">>>\n>>> Done with this, son.\n"


