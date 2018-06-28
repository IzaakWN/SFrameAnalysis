#! /usr/bin/env python

import os, sys, re
from math import floor, ceil
from argparse import ArgumentParser
sys.path.append('../plots')
from array import array
import ROOT
from ROOT import gPad, gROOT, gStyle, gRandom, gDirectory, TGaxis, Double, kFALSE, TFile, TTree,\
                 TH1, TH1F, TH2F, TH1D, THStack, TCanvas, TLegend, TGraph, TGraphAsymmErrors, TLine, TLatex,\
                 TText, TLatex, kBlack, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta, kTeal
ROOT.gROOT.SetBatch(ROOT.kTRUE)

argv = sys.argv
description = '''This script make some checks.'''
parser = ArgumentParser(prog="checkPlots",description=description,epilog="Succes!")
parser.add_argument( "-p", "--pdf",     dest="pdf", default=False, action='store_true',
                                        help="create pdf version as well" )
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                                        help="print verbose" )
args = parser.parse_args()

# LOAD SFRAME STUFF
configFile = "PlotTools/config_mumu2017.py"
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(configFile)
settings, commands = loadConfigurationFromFile(configFile,verbose=args.verbose)
exec settings
globalTag = "_2017_V2_full_noEW"
pottag    = "_full_RC_noEW"
loadSettings(globals(),settings,verbose=args.verbose)
exec commands
OUT_DIR = ensureDirectory("Zpt")

varlabel = { 'm_2':   "m_{#tau}",     'm_genboson':  "Z boson mass",
             'm_vis': "dimuon mass",  'pt_genboson': "Z boson p_{T}", }
baseline = "iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && m_vis>60"
mbins    = [60,70,80,85,90,95,100,120,180,250,500,1000] #[60,70,80,85,89,90,91,95,100,110,120] #[0,60,80,90,100,120,180,250,500,1000]
ptbins   = [0,2,4,6,8,10,12,15,20,30,40,50,60,70,80,90,100,120,140,160,180,200,500,1000]
filename = "%s/Zpt_weights_2017_Izaak.root"%(OUT_DIR)
gROOT.Macro("Zpt/zptweight_check.C+")
zmax     = 3



def measureZptWeightsReco(samples):
    """Measure Z pT weights in reco-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> measureZptWeightsReco()"
    
    tag     = ""
    outdir  = OUT_DIR
    ratio   = True
    norm    = True
    logx    = True #and False
    logy    = True #and False
    exts    = ["png","pdf"] if args.pdf else ["png"]
    measure = True #and False
    plot1D  = True and False
    
    # SETTINGS
    file = TFile(filename,'UPDATE')
    selections = baseline
    ztitle     = "reco weight"
    histname   = "zptmass"
    canvasname = "%s/%s_weights_reco%s%s.png"%(outdir,histname,tag,pottag)
    xvar, xtitle, xbins = "m_vis", "dimuon mass [GeV]",  mbins
    yvar, ytitle, ybins = "pt_ll", "dimuon p_{T} [GeV]", ptbins
    
    if measure:
      # HISTOGRAMS
      histsD, histsB, histsS = samples.createHistograms2D(xvar,xbins,yvar,ybins,selections,
                                                          signal=False,split=False,blind=False,QCD=False,JTF=False)
      
      # DRELL-YAN
      histsDY = [h for h in histsB if 'DY' in h.GetName()]
      if len(histsDY)!=1:
        print ">>> ERROR! measureZptWeightsReco: histsDY = %s"%(histsDY); exit(1)
      histDY  = histsDY[0]
      
      # BACKGROUNDS
      histB   = histDY.Clone("background_reco")
      for hist in histsB:
        if 'DY' not in hist.GetName(): histB.Add(hist)
      
      # WEIGHTS  =  ( DATA - MC + DY ) / DY
      histD  = histsD[0]
      histSF = histD.Clone(histname+"weights_reco")
      histSF.Sumw2()
      histSF.SetTitle(ztitle)
      histSF.Add(histB,-1)
      histSF.Add(histDY)
      histSF.Divide(histDY)
    
      # NORMALIZE nominator and denominator => only shape effect
      intnom = histD.Integral()
      intden = histDY.Integral()
      scale  = intnom/intden
      print ">>>   data DY = %.1f,  MC DY = %.1f,  ratio = %.2f"%(intnom,intden,scale)
      histSF.Scale(1./scale)
      # TODO: fill empty gaps by extrapolating weight ?
      
      # WRITE
      file.cd()
      writeTH2D(histSF,histname+"_weights_reco","Z boson weights",xtitle,ytitle,ztitle)
      writeTH2D(histDY,histname+"_DY",          "Drell-Yan",      xtitle,ytitle,"Events")
      writeTH2D(histB, histname+"_exp",         "expected",       xtitle,ytitle,"Events")
      writeTH2D(histD, histname+"_data",        "data",           xtitle,ytitle,"Data")
      
      # PLOT
      plot = Plot2D(histSF)
      plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,zmax=zmax,
                logx=logx,logy=logy,option="COLZTEXT44",rmargin=0.16)
      plot.saveAs(canvasname,ext=exts)
      plot.close()
      close(histDY,histB,histD)
      file.Close()
    


def measureZptWeightsGen(samples):
    """Measure Z pT weights in gen-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> measureZptWeightsGen()"
    
    tag    = ""
    outdir = OUT_DIR
    ratio  = True
    norm   = True
    logx   = True #and False
    logy   = True #and False
    exts   = ["png","pdf"] if args.pdf else ["png"]
    measure = True #and False
    plot1D  = True and False
    
    # SETTINGS
    file       = TFile(filename,'UPDATE')
    selections = baseline
    ztitle     = "weight"
    rtitle     = "gen / reco weight"
    histname   = "zptmass"
    name       = "%s/%s_weights%s%s.png"%(outdir,histname,tag,pottag)
    name_ratio = "%s/%s_weights_ratio%s%s.png"%(outdir,histname,tag,pottag)
    xvar, xtitle, xbins = "m_genboson",  "Z boson mass [GeV]",  mbins
    yvar, ytitle, ybins = "pt_genboson", "Z boson p_{T} [GeV]", ptbins
    weight     = "getZpt_reco(m_vis,pt_ll)"
    gROOT.ProcessLine("loadZptWeights_reco()")
    
    # HISTOGRAMS
    sampleDY = samples.get("DY",unique=True)
    print ">>>   creating Drell-Yan without reco weights"
    histDY   = sampleDY.hist2D(xvar,xbins,yvar,ybins,selections)
    print ">>>   creating Drell-Yan with reco weights"
    histSF   = sampleDY.hist2D(xvar,xbins,yvar,ybins,selections,weight=weight,append="_SF")
    histSF.Divide(histDY)
    # TODO: fill empty gaps by extrapolating weight ?
    
    # AVERAGE WEIGHTS = DY_with_weight_reco / DY
    histSF_reco  = file.Get(histname+"_weights_reco")
    histSF_ratio = histSF.Clone("ratio")
    histSF_ratio.Divide(histSF_reco)
    
    # WRITE
    file.cd()
    writeTH2D(histSF,      histname+"_weights",      "Z boson weights",       xtitle,ytitle,ztitle)
    writeTH2D(histSF_ratio,histname+"_weights_ratio","ratio gen/reco weights",xtitle,ytitle,rtitle)
    #fillTH2Gaps(histSF_ratio)
    
    # PLOT
    plot = Plot2D(histSF)
    plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,zmax=zmax,
              logx=logx,logy=logy,option="COLZTEXT44",rmargin=0.16)
    plot.saveAs(name,ext=exts)
    plot.close()
    
    # PLOT RATIO
    plot = Plot2D(histSF_ratio)
    plot.plot(xtitle="mass [GeV]",ytitle="p_{T} [GeV]",ztitle=rtitle,zmin=0.45,zmax=1.4,
              logx=logx,logy=logy,option="COLZTEXT44",rmargin=0.16)
    plot.saveAs(name_ratio,ext=exts)
    plot.close()
    close(histDY,histSF_reco)
    file.Close()
    


def validateZptWeights(samples):
    """Validate Z pT weights in reco-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> validateZptWeights()"
    
    selections = baseline
    ztitle     = "reco scale factor"
    histname   = "zptmass"
    xvar, xtitle, xbins = "m_vis", "dimuon mass [GeV]",  mbins
    yvar, ytitle, ybins = "pt_ll", "dimuon p_{T} [GeV]", ptbins
    gROOT.ProcessLine("loadZptWeights()")
    gROOT.ProcessLine("loadZptWeights_reco()")
    
    for bins in [xbins,ybins]:
      if bins[0]==0.0: bins[0] = 1
    
    sampleDY  = samples.get("DY",unique=True)
    weights   = [ "", "getZpt_reco(m_vis,pt_ll)", "getZpt_gen(m_genboson,pt_genboson)" ]
    variables = [
      var(xvar,   100,  0, 200, title=xtitle, position="rightright", filename="m_mumu_low",  logy=True   ),
#       var(xvar,    44, 80, 102, title=xtitle, position="rightright", filename="m_mumu_zoom", logy=False   ),
#       var(xvar,    30, 60, 120, title=xtitle, position="right", filename="m_mumu", logy=True         ),
#       var(xvar,    88, 60, 500, title=xtitle, position="right", filename="m_mumu", logy=True         ),
#       var(yvar,   100,  0, 500, title=ytitle, position="rightright", filename="pt_mumu", logy=True   ),
#       var(xvar, xbins, title=xtitle, position="topright",   filename="m_mumu",  logx=True, logy=True ),
#       var(yvar, ybins, title=ytitle, position="rightright", filename="pt_mumu", logx=True, logy=True ),
#       var("pt_1", 60,  10, 250, title="leading muon pt",    position="rightright", logy=True         ),
#       var("pt_2", 35,  10, 150, title="subleading muon pt", position="rightright", logy=True         ),
    ]
    
    for weight in weights:
      print '>>>   plot with weights "%s"'%(weight)
      sampleDY.weight = weight
      for variable in variables:
        append = ""
        text   = ""
        if variable.logx:     append += "_log"
        if  "reco" in weight:
          append += "_Zptweight_reco"
          text = "reco reweighting"
        elif "gen" in weight:
          append += "_Zptweight"
          text = "Z p_{T} reweighting"
        else:
          text = "no reweighting"
        selections1 = selections
        if "_low" in variable.filename: 
          selections1 = selections.replace(" && m_vis>60","")
        plotVariable(variable,selections1,text=text,app=append)
    


def plotVariable(variable,selections,**kwargs):
    """Plot variables for some selection."""
    
    title      = kwargs.get('title',  "Z -> mumu region" )
    text       = kwargs.get('text',   ""                 )
    ymin       = kwargs.get('ymin',   100                )
    outdir     = kwargs.get('out',    OUT_DIR            )
    weight     = kwargs.get('weight', ""                 )
    append     = kwargs.get('app',    ""                 )
    exts       = kwargs.get('ext',    [ ]                )
    
    xtitle   = variable.title
    position = variable.position
    logx     = variable.logx
    logy     = variable.logy
    divideByBinSize = logx
    name     = "%s/%s%s%s.png"%(outdir,variable.filename,append,pottag)
    exts     = ["png","pdf"] if args.pdf else ["png"]
    
    plot = samples.plotStack(variable,selections,weight=weight,title=title,QCD=False,JFR=False,divideByBinSize=divideByBinSize)
    plot.plot(xtitle=xtitle,logx=logx,logy=logy,ratio=True,staterror=True,position=position,ymin=ymin,text=text)
    plot.saveAs(name,ext=exts)
    plot.close()
    


def writeTH2D(hist,name,title,xtitle,ytitle,ztitle,**kwargs):
    hist.SetTitle(title)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle(ytitle)
    hist.GetZaxis().SetTitle(ztitle)
    hist.Write(name,TH1.kOverwrite)
    


def fillTH2Gaps(hist,axis='y',**kwargs):
    for xbin in xrange(1,hist.GetXaxis().GetNbins()+1):
      for ybin in xrange(1,hist.GetYaxis().GetNbins()+1):
        binc = hist.GetBinContent(xbin,ybin)
        if binc: continue
        if 'x' in axis:
          binc_prev = hist.GetBinContent(xbin-1,ybin)
          binc_next = hist.GetBinContent(xbin+1,ybin)
        else:
          binc_prev = hist.GetBinContent(xbin,ybin-1)
          binc_next = hist.GetBinContent(xbin,ybin+1)
        if   binc_prev==0: binc = binc_next
        elif binc_next==0: binc = binc_prev
        else:              binc = (binc_next+binc_prev)/2
        hist.SetBinContent(xbin,ybin,binc)
    


def main():
    print ""
    
    channel  = "mumu"
    treename = "tree_%s"%(channel)
    samples.setChannel(channel,treename=treename)
    
#     measureZptWeightsReco(samples)
#     measureZptWeightsGen(samples)
    validateZptWeights(samples)
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




