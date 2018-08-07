#! /usr/bin/env python

import os, sys, re
from math import floor, ceil
from argparse import ArgumentParser
sys.path.append('../plots')
from array import array
import ROOT
from ROOT import gPad, gROOT, gStyle, gDirectory, kFALSE, TFile,\
                 TH1, TH2, TH1F, TH2F
gROOT.SetBatch(ROOT.kTRUE)

argv = sys.argv
description = '''This script make some checks.'''
parser = ArgumentParser(prog="checkPlots",description=description,epilog="Succes!")
parser.add_argument( "-p", "--pdf",     dest="pdf", default=False, action='store_true',
                                        help="create pdf version as well" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                                        help="print verbose" )
args = parser.parse_args()

# LOAD SFRAME
configFile = "PlotTools/config_ltau2017.py"
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(configFile)
settings, commands = loadConfigurationFromFile(configFile,verbose=args.verbose)
exec settings
globalTag  = "_2017_V2"
pottag     = ""
mergeTop, splitTT = True, False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands
OUT_DIR = ensureDirectory("Zpt/mutau")

gROOT.Macro("Zpt/zptweight_check.C+")
gROOT.ProcessLine("loadZptWeights()")
gROOT.ProcessLine("loadZptWeights_reco()")

print '>>> baseline = "%s"'%(baseline)
selections = [
  ###sel("baseline mutau",      "%s"%(baseline), filename="baseline"                 ),
  sel("m_T < 50 GeV",        "%s && %s"%(baseline,"pfmt_1<50")                     ),
  sel("m_T < 50 GeV, DM0",   "%s && %s"%(baseline,"pfmt_1<50 && decayMode_2==0")   ),
  sel("m_T < 50 GeV, DM1",   "%s && %s"%(baseline,"pfmt_1<50 && decayMode_2==1")   ),
  sel("m_T < 50 GeV, DM10",  "%s && %s"%(baseline,"pfmt_1<50 && decayMode_2==10")  ),
]



def validateZptWeights(samples):
    """Validate Z pT weights in reco-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> "+green("validateZptWeights()")
    
    outdir    = OUT_DIR
    sampleDY  = samples.get("DY",unique=True)
    weights   = [ "", #"getZpt_reco(m_genboson,pt_genboson)",
                  "getZpt_gen(m_genboson,pt_genboson)"
    ]
    variables = [
      var("m_vis",      40,    0, 200,   position="right" ),
      var("m_vis",      25,   50, 100,   position="topright", filename="$VAR_zoom", cposition={"decayMode_2==0":"top;x=0.48"} ),
      var("m_2",        36,  0.20, 2.0,  title="m_tau", veto="decayMode_2==0", cbinning={'decayMode_2==1(?!0)':(36,0.20,2.0), 'decayMode_2==10':(22,0.70,1.8)} ),
      var("pt_tt_vis",  50,     0, 200,  position="right", title="pt_mutau", filename="pt_ll" ),
      var("pt_1",       35,    10, 150,  position="right", title="muon pt"    ),
      var("pt_2",       35,    10, 150,  position="right", title="tau pt" ),
      var("deta_ll",    45,     0, 4.5,  position="right" ),
      var("dphi_ll",    50,     0, 3.5,  position="left"  ),
      var("eta_1",      30,  -3.4, 2.6,  position="topleftleft", title="muon eta", ymargin=1.25 ),
      var("eta_2",      30,  -3.4, 2.6,  position="topleftleft", title="tau eta",  ymargin=1.30 ),
    ]
    
    for weight in weights:
      print '>>>   plot with weights "%s"'%(weight)
      print '>>>   setting Drell-Yan\'s weight "%s" -> "%s"'%(sampleDY.weight,weight)
      sampleDY.setExtraWeight(weight)
      for selection in selections:
        print '>>>\n>>>      plot with selection "%s"'%(selection.title)
        for variable in variables:
          if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
            print ">>> plotStacks: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
          variable.changeContext(selection.selection)
          append = ""
          text   = ""
          if variable.logx:     append += "_log"
          if  "reco" in weight:
            append += "_Zptweight_reco"
            text = "reco Z p_{T} reweighting"
          elif "gen" in weight:
            append += "_Zptweight"
            text = "Z p_{T} reweighting"
          else:
            text = "no Z p_{T} reweighting"
          plotVariable(variable,selection,text=text,app=append)
    


def plotVariable(variable,selection,**kwargs):
    """Plot variables for some selection."""
    
    text     = kwargs.get('text',   ""                 )
    weight   = kwargs.get('weight', ""                 )
    append   = kwargs.get('app',    ""                 )
    outdir   = OUT_DIR
    
    title    = selection.title
    xtitle   = variable.title
    position = variable.position
    logx     = variable.logx
    logy     = variable.logy
    ymargin  = variable.ymargin
    divideByBinSize = logx
    name     = "%s/%s_%s%s%s.png"%(outdir,variable.filename,selection.filename,append,pottag)
    exts     = ["png","pdf"] if args.pdf else ["png"]
    
    plot = samples.plotStack(variable,selection,weight=weight,title=title,QCD=False,JFR=True,divideByBinSize=divideByBinSize)
    plot.plot(xtitle=xtitle,logx=logx,logy=logy,ratio=True,staterror=True,position=position,text=text,ymargin=ymargin)
    plot.saveAs(name,ext=exts)
    plot.close()
    


def validateZptWeights_shapes(samples):
    """Validate Z pT weights in reco-level dimuon pT vs. dimuon mass by comparing shapes."""
    print ">>>\n>>> "+green("validateZptWeights_shapes()")
    
    samplenames = [
      ("DY",    "DY",    "DY",                  ),
      #("ZTT",   "ZTT",   "DY", "gen_match_2==5" ),
      #("JTF",   "JTF",   "JTF",                 ),
      #("stack", "stack", "stack",               ),
    ]
    
    variables = [
#       var("m_vis",      40,    0, 200,   position="right" ),
      var("m_vis",      25,   50, 100,   position="right", filename="$VAR_zoom", cposition={"decayMode_2==0":"x=0.42"} ),
#       var("m_2",        36,  0.20, 2.0,  title="m_tau", veto="decayMode_2==0", cbinning={'decayMode_2==1(?!0)':(36,0.20,2.0), 'decayMode_2==10':(22,0.70,1.8)} ),
#       var("pt_tt_vis",  50,     0, 200,  position="right", title="pt_mutau", filename="pt_ll" ),
#       var("pt_1",       35,    10, 150,  position="right", title="muon pt"    ),
#       var("pt_2",       35,    10, 150,  position="right", title="tau pt"     ),
#       var("deta_ll",    45,     0, 4.5,  position="right" ),
#       var("dphi_ll",    50,     0, 3.5,  position="left"  ),
      var("eta_1",      28,  -3.0, 2.6,  position="topleftleft", title="muon eta", ymargin=1.25 ),
      var("eta_2",      28,  -3.0, 2.6,  position="topleftleft", title="tau eta",  ymargin=1.30 ),
    ]
    
    # SETTINGS
    tag       = ""
    outdir    = OUT_DIR
    ratio     = True
    norm      = True
    staterror = True
    JFR       = True
    exts      = ["png","pdf"] if args.pdf else ["png"]
    sampleDY  = samples.get("DY",unique=True)
    
    for sampleinfo  in samplenames:
      samplename, sampletitle, searchterm = sampleinfo[:3]
      extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
      sample = None if "stack" in searchterm or "JTF" in searchterm else samples.get(searchterm,unique=True)
      
      for selection in selections:
        print '>>>\n>>> plot %s for selection "%s"'%(sampletitle,selection)
        
        # LOOP over VARIABLES
        for variable in variables:
          if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
            print ">>>   plotStacks: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
          variable.changeContext(selection.selection)
          
          hists  = [ ]
          stacks = [ ]
          
          weights = [ ("no Z pt reweighting", ""),
                      ("Z pt reweighting",    "getZpt_gen(m_genboson,pt_genboson)") ]
          
          for i, (title, weight) in enumerate(weights,1):
            app    = "_%s"%i
            #print '>>>   replacing Drell-Yan\'s extra weight "%s" -> "%s"'%(sampleDY.weight,weight)
            sampleDY.setExtraWeight(weight)
            if "stack" in samplename:
              stack = samples.getStack(variable,selection,append=app,title=title,JFR=JFR,split=False)
              hist = stack.GetStack().Last().Clone()
              hist.SetTitle(title)
              stacks.append(stack)
            elif "JTF" in samplename:
              hist = samples.jetFakeRate(variable,selection,append=app,title=title)
            else:
              hist = sample.hist(variable,selection,append=app,title=title,extracuts=extracuts)
            hists.append(hist)
          if len(hists)!=2: continue
          
          # NAME
          filename = "%s/%s_%s_%s%s.png"%(outdir,variable.filename,samplename.replace(' ','_'),selection.filename,tag)
          filename = makeFileName(filename)
          
          # TITLE
          name       = variable.name
          xtitle     = variable.title
          title      = "%s, %s"%(sampletitle,selection.title)
          position   = variable.position
          print position
          ratiorange = 0.21
          
          # PLOT
          plot = Plot(hists,title=title)
          plot.plot(xtitle,ratio=ratio,norm=norm,staterror=staterror,position=position,ratiorange=ratiorange)
          plot.saveAs(filename,ext=exts)
          plot.close()
          close(stacks)
    


def green(string,**kwargs):
    return kwargs.get('pre',"")+"\x1b[0;32;40m%s\033[0m"%string
    


def main():
    print ">>> "
    
    channel  = "mutau"
    treename = "tree_%s_cut_relaxed"%(channel)
    samples.setChannel(channel,treename=treename)
    #validateZptWeights(samples)
    validateZptWeights_shapes(samples)
    print ">>>\n>>> done\n"
    


if __name__ == '__main__':
    main()




