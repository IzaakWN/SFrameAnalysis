#! /usr/bin/env python

import os, sys, re
from math import floor, ceil
from argparse import ArgumentParser
sys.path.append('../plots')
from array import array
import ROOT
from ROOT import gPad, gROOT, gStyle, gDirectory, kFALSE, TFile,\
                 TH1, TH2, TH1F, TH2F
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
globalTag  = "_2017_V2_full_noRC"
pottag     = "_full_noRC"
loadMacros, onlyDY = False, False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands
OUT_DIR = ensureDirectory("Zpt")

varlabel = { 'm_2':   "m_{#tau}",     'm_genboson':  "Z boson mass",
             'm_vis': "dimuon mass",  'pt_genboson': "Z boson p_{T}", }
baseline = "iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && m_vis>20"
mbins    = [20,30,40,50,60,70,80,85,88,89,89.5,90,90.5,91,91.5,92,93,94,95,100,110,120,180,250,500,1000]
#Zmbins   = [20,30,40,50,60,70,80,85,86,87,88,88.5,89,89.5,90,90.5,91,91.5,92,92.5,93,94,95,100,110,120,180,250,500,1000]
Zmbins   = [20,30,40,50,60,70,80,85,86,87,88,88.5,89,89.2,89.4,89.6,89.8,
                                                  90,90.2,90.4,90.6,90.8,
                                                  91,91.2,91.4,91.6,91.8,
                                                  92,92.2,92.4,92.6,92.8,
                                                  93,93.2,93.4,93.6,93.8,94,95,100,110,120,180,250,500,1000]
ptbins     = [0,2,4,6,8,10,12,15,20,30,40,50,60,70,80,90,100,120,140,160,180,200,500,1000]
filename   = "%s/Zpt_weights_2017_Izaak.root"%(OUT_DIR)
gROOT.Macro("%s/zptweight_check.C+"%(OUT_DIR))
zmax       = 3
markersize = 0.88

print ">>> mbins:  %s"%mbins
print ">>> Zmbins: %s"%Zmbins
print ">>> ptbins: %s"%ptbins


def measureZptWeightsReco(samples):
    """Measure Z pT weights in reco-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> "+green("measureZptWeightsReco()")
    
    tag     = ""
    outdir  = OUT_DIR
    logx    = True #and False
    logy    = True #and False
    logz    = True #and False
    exts    = ['png','pdf'] if args.pdf else ['png']
    
    # SETTINGS
    file = TFile(filename,'UPDATE')
    selections = baseline
    ztitle     = "reco weight"
    histname   = "zptmass"
    xvar, xtitle, xbins = "m_vis", "dimuon mass [GeV]",  mbins
    yvar, ytitle, ybins = "pt_ll", "dimuon p_{T} [GeV]", ptbins
    
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
    histSF_gaps = histSF.Clone("gaps")
    setMaximumContent(histSF,3.0)
    fillTH2Gaps(histSF,axis='x')
    extendContent(histSF)
    
    # WRITE
    file.cd()
    writeTH2D(histSF,histname+"_weights_reco","Z boson weights",xtitle,ytitle,ztitle)
    writeTH2D(histDY,histname+"_DY",          "Drell-Yan",      xtitle,ytitle,"Events")
    writeTH2D(histB, histname+"_exp",         "expected",       xtitle,ytitle,"Events")
    writeTH2D(histD, histname+"_data",        "data",           xtitle,ytitle,"Data")
    
    # PLOT
    for extra, hist in [("",histSF),("_gaps",histSF_gaps)]:
      name       = "%s/%s_weights_reco%s%s%s.png"%(outdir,histname,extra,tag,pottag)
      plot = Plot2D(hist)
      plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,zmax=zmax,
                logx=logx,logy=logy,option="COLZTEXT44",markersize=markersize)
      plot.saveAs(name,ext=exts)
      plot.close()
    
    for samplename, hist in [("DY",histDY),("exp",histB),("data",histD)]:
      name = "%s/%s_%s%s%s.png"%(outdir,histname,samplename,tag,pottag)
      plot = Plot2D(hist)
      plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle="Events",
                logx=logx,logy=logy,logz=logz,option="COLZ",rmargin=0.17)
      plot.saveAs(name,ext=exts)
      plot.close()
    
    
    file.Close()
    


def measureZptWeightsGen(samples):
    """Measure Z pT weights in gen-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> "+green("measureZptWeightsGen()")
    
    tag    = ""
    outdir = OUT_DIR
    logx   = True #and False
    logy   = True #and False
    exts   = ['png','pdf'] if args.pdf else ['png']
    
    # SETTINGS
    file       = TFile(filename,'UPDATE')
    selections = baseline
    ztitle     = "weight"
    rtitle     = "gen / reco weight"
    histname   = "zptmass"
    xvar, xtitle, xbins = "m_genboson",  "Z boson mass [GeV]",  Zmbins
    yvar, ytitle, ybins = "pt_genboson", "Z boson p_{T} [GeV]", ptbins
    weight     = "getZpt_reco(m_vis,pt_ll)"
    gROOT.ProcessLine("loadZptWeights_reco()")
    
    # HISTOGRAMS
    sampleDY = samples.get("DY",unique=True)
    print ">>>   creating Drell-Yan without reco weights"
    histDY   = sampleDY.hist2D(xvar,xbins,yvar,ybins,selections)
    print ">>>   creating Drell-Yan with reco weights"
    histDYw  = sampleDY.hist2D(xvar,xbins,yvar,ybins,selections,weight=weight,append="_SF")
    histSF   = histDYw.Clone("weights")
    
    # AVERAGE WEIGHTS  =  DY_with_weight_reco / DY
    histSF.Divide(histDY)
    histSF_gaps = histSF.Clone("gaps")
    setMaximumContent(histSF,3.0)
    fillTH2Gaps(histSF,axis='x')
    extendContent(histSF)
    
    # NORMALIZE nominator and denominator => only shape effect
    intnom = histDYw.Integral()
    intden = histDY.Integral()
    scale  = intnom/intden
    print ">>>   DY with weight = %.1f,  DY without weight = %.1f,  ratio = %.2f"%(intnom,intden,scale)
    histSF.Scale(1./scale)
    
    # RATIO
    #histSF_reco  = file.Get(histname+"_weights_reco")
    #histSF_ratio = histSF.Clone("ratio")
    #histSF_ratio.Divide(histSF_reco)
    
    # WRITE
    file.cd()
    writeTH2D(histDY,      histname+"_DY_gen",              "Drell-Yan",              xtitle,ytitle,ztitle)
    writeTH2D(histDYw,     histname+"_DY_gen_weighted_reco","Drell-Yan reco-weighted",xtitle,ytitle,ztitle)
    writeTH2D(histSF,      histname+"_weights",             "Z boson weights",        xtitle,ytitle,ztitle)
    #writeTH2D(histSF_ratio,histname+"_weights_ratio",       "ratio gen/reco weights", xtitle,ytitle,rtitle)
    
    # PLOT
    for extra, hist in [("",histSF),("_gaps",histSF_gaps)]:
      name       = "%s/%s_weights%s%s%s.png"%(outdir,histname,extra,tag,pottag)
      plot = Plot2D(histSF)
      plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,zmax=zmax,
                logx=logx,logy=logy,option="COLZTEXT44",markersize=markersize)
      plot.saveAs(name,ext=exts)
      plot.close()
    
    # PLOT RATIO
    #name_ratio = "%s/%s_weights_ratio%s%s.png"%(outdir,histname,tag,pottag)
    #plot = Plot2D(histSF_ratio)
    #plot.plot(xtitle="mass [GeV]",ytitle="p_{T} [GeV]",ztitle=rtitle,zmin=0.45,zmax=1.4,
    #          logx=logx,logy=logy,option="COLZTEXT44")
    #plot.saveAs(name_ratio,ext=exts)
    #plot.close()
    close(histDY,histDYw) #,histSF_reco
    file.Close()
    


def validateZptWeights(samples):
    """Validate Z pT weights in reco-level dimuon pT vs. dimuon mass."""
    print ">>>\n>>> "+green("validateZptWeights()")
    
    selections = baseline
    xvar, xtitle, xbins = "m_vis", "dimuon mass [GeV]",  mbins
    yvar, ytitle, ybins = "pt_ll", "dimuon p_{T} [GeV]", ptbins
    gROOT.ProcessLine("loadZptWeights()")
    gROOT.ProcessLine("loadZptWeights_reco()")
    
    for bins in [xbins,ybins]:
      if bins[0]==0.0: bins[0] = 1
    
    sampleDY  = samples.get("DY",unique=True)
    weights   = [ "",
                  "getZpt_reco(m_vis,pt_ll)",
                  "getZpt_gen(m_genboson,pt_genboson)"
    ]
    variables = [
      var(xvar,   100,  0, 200, title=xtitle, position="rightright", filename="m_mumu_low", ymin=100, logy=True ),
      var(xvar,    44, 80, 102, title=xtitle, position="rightright", filename="m_mumu_zoom", logy=False         ),
      var(xvar,    30, 60, 120, title=xtitle, position="right", filename="m_mumu", ymin=100, logy=True          ),
      var(xvar,   100,  0, 500, title=xtitle, position="right", filename="m_mumu", ymin=100, logy=True          ),
      var(yvar,   100,  0, 500, title=ytitle, position="rightright", filename="pt_mumu", ymin=100, logy=True    ),
      var(xvar, xbins, title=xtitle, position="topright",   filename="m_mumu", ymin=100,  logx=True, logy=True  ),
      var(yvar, ybins, title=ytitle, position="rightright", filename="pt_mumu", ymin=100, logx=True, logy=True  ),
      var("pt_1", 60,  10, 250, title="leading muon pt",    position="rightright", ymin=100, logy=True          ),
      var("pt_2", 35,  10, 150, title="subleading muon pt", position="rightright", ymin=100, logy=True          ),
      var("deta_ll", 45,  0, 4.5,      title="deta_mumu", filename="deta_mumu",     position="right"            ),
      var("abs(dphi_ll)", 50,  0, 3.5, title="dphi_mumu", filename="dphi_mumu",     position="left"             ),
      var("deta_ll",      45,  0, 4.5, title="deta_mumu", filename="deta_mumu_log", position="toprightright",  ymin=500, ymargin=2,  logy=True ),
      var("abs(dphi_ll)", 50,  0, 5.0, title="dphi_mumu", filename="dphi_mumu_log", position="toptopleftleft", ymin=500, ymargin=20, logy=True ),
      var("eta_1",   28, -3.0, 2.6, title="leading muon eta",   position="toptopleftleft", ymargin=1.25         ),
      var("eta_2",   28, -3.0, 2.6, title="subeading muon eta", position="toptopleftleft", ymargin=1.25         ),
    ]
    
    for weight in weights:
      print '>>>   plot with weights "%s"'%(weight)
      if sampleDY.weight:
        print '>>>   replaceing Drell-Yan\'s weight "%s"'%(sampleDY.weight)
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
          text = "no Z p_{T} reweighting"
        cuts = selections.replace(" && m_vis>20","") if "_low" in variable.filename else selections
        plotVariable(variable,cuts,text=text,app=append)
    


def plotVariable(variable,selections,**kwargs):
    """Plot variables for some selection."""
    
    title      = kwargs.get('title',  "Z -> mumu region" )
    text       = kwargs.get('text',   ""                 )
    outdir     = kwargs.get('out',    OUT_DIR            )
    weight     = kwargs.get('weight', ""                 )
    append     = kwargs.get('app',    ""                 )
    exts       = kwargs.get('ext',    [ ]                )
    
    xtitle   = variable.title
    position = variable.position
    logx     = variable.logx
    logy     = variable.logy
    ymargin  = variable.ymargin
    divideByBinSize = logx
    name     = "%s/%s%s%s.png"%(outdir,variable.filename,append,pottag)
    exts     = ['png','pdf'] if args.pdf else ['png']
    
    plot = samples.plotStack(variable,selections,weight=weight,title=title,QCD=False,JFR=False,divideByBinSize=divideByBinSize)
    plot.plot(xtitle=xtitle,logx=logx,logy=logy,ratio=True,staterror=True,position=position,text=text,ymargin=ymargin)
    plot.saveAs(name,ext=exts)
    plot.close()
    


def writeTH2D(hist,name,title,xtitle,ytitle,ztitle,**kwargs):
    hist.SetTitle(title)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle(ytitle)
    hist.GetZaxis().SetTitle(ztitle)
    hist.Write(name,TH1.kOverwrite)
    

def setMaximumContent(hist,maximum,**kwargs):
    """Set maximum bin content for a histogram."""
    if isinstance(hist,TH2):
      nxbins, nybins = hist.GetXaxis().GetNbins(), hist.GetYaxis().GetNbins()
      for ybin in xrange(0,nybins+2):
        for xbin in xrange(0,nxbins+2):
          binc = hist.GetBinContent(xbin,ybin)
          if binc>maximum:
            hist.SetBinContent(xbin,ybin,maximum)
    elif isinstance(hist,TH1):
      nxbins = hist.GetXaxis().GetNbins()
      for xbin in xrange(0,nxbins+2):
        binc = hist.GetBinContent(xbin)
        if binc>maximum:
          hist.SetBinContent(xbin,maximum)


def extendContent(hist,axis='xy',flow='uo',**kwargs):
    """Extend bin content to neighbouring under- and overflow."""
    if isinstance(hist,TH2):
      nxbins, nybins = hist.GetXaxis().GetNbins(), hist.GetYaxis().GetNbins()
      uflow, oflow = 'u' in flow, 'o' in flow
      if uflow:
        hist.SetBinContent(       0,       0,hist.GetBinContent(     1,     1))
        hist.SetBinContent(nxbins+1,       0,hist.GetBinContent(nxbins,     1))
      if oflow:
        hist.SetBinContent(       0,nybins+1,hist.GetBinContent(     1,nybins))
        hist.SetBinContent(nxbins+1,nybins+1,hist.GetBinContent(nxbins,nybins))
      if 'x' in axis:
        for ybin in xrange(1,nybins+1):
          if uflow: hist.SetBinContent(       0,ybin,hist.GetBinContent(     1,ybin))
          if oflow: hist.SetBinContent(nxbins+1,ybin,hist.GetBinContent(nxbins,ybin))
      if 'y' in axis:
        for xbin in xrange(1,nxbins+1):
          if uflow: hist.SetBinContent(xbin,       0,hist.GetBinContent(xbin,     1))
          if oflow: hist.SetBinContent(xbin,nybins+1,hist.GetBinContent(xbin,nybins))
    elif isinstance(hist,TH1):
      nxbins = hist.GetXaxis().GetNbins()
      if uflow: hist.SetBinContent(       0,hist.GetBinContent(       1))
      if oflow: hist.SetBinContent(nxbins+1,hist.GetBinContent(nxbins+1))
    
def fillTH2Gaps(hist,axis='x'):
    #bins = [ (x,y) for x in xrange(1,hist.GetXaxis().GetNbins()+1) for y in xrange(1,hist.GetYaxis().GetNbins()+1) ]
    for x in xrange(1,hist.GetXaxis().GetNbins()+1):
      for y in xrange(1,hist.GetYaxis().GetNbins()+1):
        binc = hist.GetBinContent(x,y)
        if binc==0:
          fillTH2BinGap(hist,x,y,axis=axis,next=0)
    
def fillTH2BinGap(hist,x,y,axis='x',next=0):
    """Recursively scan over zero bins until at least two neighbouring bins are found that
    can be used to get an average for the empty bin. Returns false if the edge is reached."""
    #print ">>> (x,y) = (%2d,%2d),  "%(x,y),
    #if 'x' in axis: print "next (x+%d,y) = (%2d,%2d)"%(next,x+next,y)
    #if 'y' in axis: print "next (x,y+%d) = (%2d,%2d)"%(next,x,y+next)
    
    binc   = hist.GetBinContent(x,y)
    nxbins = hist.GetXaxis().GetNbins()
    nybins = hist.GetYaxis().GetNbins()
    if 'x' in axis:
      if next==0:
        next = -1 if x==nxbins else +1
      elif next>0 and x>nxbins: # hit upper edge
        return False
      elif next<0 and x<1: # hit lower edge
        return False
      while binc==0:
        binc_nxt = hist.GetBinContent(x+next,y)
        average, error, nonzero = weightedAverage(hist,x,y)
        if nonzero>1:
          binc = hist.SetBinContent(x,y,average) # average
          binc = hist.SetBinError(x,y,error) # average
          return True
        elif binc_nxt==0.0:
          if not fillTH2BinGap(hist,x+next,y,axis='x',next=+1): # check next bin 
            return False
        else:
          ynext = -1 if y==nybins else +1
          if not fillTH2BinGap(hist,x,y,axis='y',next=ynext):
            return False
    elif 'y' in axis:
      if next==0:
        next = -1 if y==nybins else +1
      elif next>0 and y>nybins: # hit upper edge
        return False
      elif next<0 and y<1: # hit lower edge
        return False
      while binc==0:
        binc_nxt = hist.GetBinContent(x,y+next)
        average, error, nonzero = weightedAverage(hist,x,y)
        if nonzero>1:
          binc = hist.SetBinContent(x,y,average) # average
          binc = hist.SetBinError(x,y,error) # average
          return True
        elif binc_nxt==0.0:
          if not fillTH2BinGap(hist,x,y+next,axis='y',next=+1): # check next bin 
            return False
        else:
          xnext = -1 if x==nxbins else +1
          if not fillTH2BinGap(hist,x,y,axis='x',next=xnext):
            return False
    hist.SetBinContent(x,y,binc)
    return True
    

def weightedAverage(hist,x,y):
    """CaweightedAveragelculate average of neighbouring bins, weighted by uncertainty.
    Returns average with uncertainty and the number of nozero bins."""
    nonzero = 0
    average = 0.0
    error   = 0.0
    denom   = 0.0
    for xn in [x-1,x,x+1]:
      for yn in [y-1,y,y+1]:
        if x==xn and yn==y: continue
        binc = hist.GetBinContent(xn,yn)
        if binc!=0:
          nonzero += 1
          binerr   = hist.GetBinError(xn,yn)
          if binerr==0:
            print ">>> Warning! weightedAverage: (xn,yn)=(%d,%d) with non-zero bin content %.2f has zero bin error"%(xn,yn,binc)
            binerr = 10**(-6)
          average += binc/(binerr)**2
          denom   += 1./(binerr)**2
    if denom:
      average /= denom
      error    = sqrt(1./denom)
    return average, error, nonzero


def testFillGapFunction():
    """Test fill gap function."""
    print ">>>\n>>> testFillGapFunction()"
    
    tag    = ""
    outdir = OUT_DIR
    logx   = True #and False
    logy   = True #and False
  
    file     = TFile(filename,'UPDATE')
    ztitle   = "weight"
    histname = "zptmass"
    name     = "%s/%s_weights%s%s.png"%(outdir,histname,tag,pottag)
    xtitle   = "Z boson mass [GeV]"
    ytitle   = "Z boson p_{T} [GeV]"
    hist_old = file.Get(histname+"_weights_reco")
    hist_new = hist_old.Clone("new")
    fillTH2Gaps(hist_new,axis='x')
    #fillTH2BinGap(hist_new,1,1,axis='x',next=0)
    
    # PLOT
    for histname, hist in [("old",hist_old),("new",hist_new),]:
      plot = Plot2D(hist_old)
      plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,zmax=zmax,
                logx=logx,logy=logy,option="COLZTEXT44")
      plot.saveAs("%s.png"%(histname))
      plot.close()

def green(string,**kwargs):
    return kwargs.get('pre',"")+"\x1b[0;32;40m%s\033[0m"%string


def main():
    print ">>> "
    
    channel  = "mumu"
    treename = "tree_%s"%(channel)
    samples.setChannel(channel,treename=treename)
    
    measureZptWeightsReco(samples)
    measureZptWeightsGen(samples)
    validateZptWeights(samples)
    ###testFillGapFunction()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




