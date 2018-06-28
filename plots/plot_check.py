#! /usr/bin/env python

import os, sys
from argparse import ArgumentParser
sys.path.append('../plots')
# import PlotTools.PlotTools
# from PlotTools.PlotTools import Plot, rebin, makeFileName
# import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
# from PlotTools.PrintTools import color, warning, error, printSameLine, header
import ROOT
from ROOT import gPad, gROOT, gStyle, gRandom, gDirectory, TGaxis, TFile, TTree, TH1F, TH2F, TH1D, THStack, TCanvas, TLegend, TGraphErrors, TGraphAsymmErrors,\
                 TText, TLatex, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)
TGaxis.SetExponentOffset(-0.060,0.005,'y')

argv = sys.argv
description = '''This script make some checks.'''
parser = ArgumentParser(prog="checkPlots",description=description,epilog="Succes!")
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="print verbose" )
args = parser.parse_args()

# LOAD config
#configFile = "PlotTools/config_ltau2017.py"
configFile = "PlotTools/config_ltau2016.py"
#configFile = "PlotTools/config_mumu2017.py"
from PlotTools.SettingTools import *
print ">>> loading configuration file %s for plot.py"%(configFile)
settings, commands = loadConfigurationFromFile(configFile,verbose=args.verbose)
exec settings
doStack = False; doDatacard = False; doTESscan = False; doTES = False; doMES = False; normalizeWJ = False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands

#SFRAME_DIR = "SFrameAnalysis_ltau2017"
IN_DIR  = SAMPLE_DIR #"/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_ltau2017"
OUT_DIR = "checks"

# CMS style
#lumi = 41.86
#PlotTools.PlotTools.luminosity = lumi
CMS_lumi.cmsText      = "CMS"
CMS_lumi.extraText    = "Preliminary"
CMS_lumi.cmsTextSize  = 0.75
CMS_lumi.lumiTextSize = 0.70
CMS_lumi.relPosX      = 0.12
CMS_lumi.outOfFrame   = True
#CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
tdrstyle.setTDRStyle()

colors     = [ kRed+3, kAzure+4, kOrange-6, kGreen+3, kMagenta+3, kYellow+2,
               kRed-7, kAzure-4, kOrange+6, kGreen-2, kMagenta-3, kYellow-2 ]


def quicktest():
  """Compare shapes of different variables for the same sample file."""
  print ">>>\n>>> compareVarsForSamples()"
  
  filenames = [
    ("TT",  "TTTo2L2Nu",    "ttbar", ),
  ]
  
  vars      = [
    (["met","met_UncEnUp","met_UncEnDown"],50,0,200),
    (["jpt_1","jpt_2"],50,0,200),
  ]
  
  baseline  = "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"
  cuts = [
    ("baseline", baseline),
  ]
  
  dirname   = ensureDirectory("%s/checks"%(OUT_DIR))
  globalTag = "_2017_V2"
  channel   = "mutau"
  weight    = "puweight"
  treename  = "tree_%s_cut_relaxed"%(channel)
  
  for ifile, (subdir,filename0,samplename) in enumerate(filenames,1):
      print ">>>   %2s: %10s, %10s"%(ifile,filename0,samplename)
      filename    = "%s/%s/TauTauAnalysis.%s%s.root"%(IN_DIR,subdir,filename0,globalTag)
      file        = TFile(filename)
      for cutname, cut in cuts:
        for ivar, (varlist,nBins,xmin,xmax) in enumerate(vars):
          print ">>>   %s - %s" % (cutname,varlist[0])
          var0 = varlist[0]
          cut  = "(%s)*%s"%(cut,weight)
          
          hists = [ ]
          for i, var in enumerate(varlist):
              histname    = "%s_%s"%(subdir,var)
              hist        = TH1F(histname,histname,nBins,xmin,xmax)
              tree        = file.Get(treename)
              out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
              #N1          = hist.GetEntries()
              #hist.Scale(1/N1)
              hists.append(hist)
          
          plot = Plot(hists)
          plot.plot(var0,ratio=2,linestyle=False)
          plot.saveAs("test.png")
        
      file.Close()
    

def TTSFs(samples):
    """Study TTbar SF in function of MET cut."""
    
    
    channels = [ "mutau", "etau" ]
    isocuts     = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
    vetos       = "lepton_vetos==0"
    triggers    = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline    = "channel>0 && %s && %s && %s && q_1*q_2<0"%(triggers,isocuts,vetos)
    categorybbA = "ncbtag>0"
    category1   = "ncbtag>0 && ncjets==1 && nfjets >0"
    category2J  = "ncbtag>0 && ncjets==2 && nfjets==0"
    selections  = [
      ("1b1f", "%s && %s && %s"%(baseline,category1,  "pfmt_1<60")),
      ("1b1c", "%s && %s && %s"%(baseline,category2J, "pfmt_1<60")),
    ]
    
    METcuts = [ 30, 40, 50, 60, 70, 80 ]
    mT      = 60
    results = [ ]
    
    graphs = [ ]
    for channel in channels:
      treename = "tree_%s_cut_relaxed"%(channel)
      samples.setChannel(channel,treename=treename)
      
      for cutname, cuts in selections:
        graphname = "%s, %s"%(channel.replace('mu','#mu').replace('tau','#tau'),cutname)
        graph = TGraphErrors()
        graph.SetTitle(graphname)
        graphs.append(graph)
        for i, met in enumerate(METcuts):
          print ">>> %s, MET>%s"%(cutname,met)
          TTSF, err = samples.renormalizeTT(cuts,baseline=baseline,MET=met,mT=mT,save=False,revert=False,apply=False,verbosity=1)
          graph.SetPoint(i,float(met),TTSF)
          graph.SetPointError(i,0.0,err)
    
    xtitle = "lower cut on MET [GeV]"
    ytitle = "t#bar{t} normalization scale factor"
    canvasname = "%s/TT_SF_scan.png"%(OUT_DIR)
    drawTGraphs(graphs,xtitle=xtitle,ytitle=ytitle,xmin=20,xmax=90,ymin=0.0,ymax=2.1,legend=True,option="LEP",canvas=canvasname,exts=['png','pdf'])


def purity(samples):
    """Compare shapes."""
    
    channel  = "mutau"
    treename = "tree_%s_cut_relaxed"%(channel)
    var      = "m_sv"
    nbinx, xmin, xmax = 200, 0, 200
    samples.setChannel(channel,treename=treename)
    
    isocuts     = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
    vetos       = "lepton_vetos==0"
    triggers    = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline    = "channel>0 && %s && %s && %s && decayMode_2<11 && q_1*q_2<0"%(triggers,isocuts,vetos)
    categorybbA = "ncbtag>0"
    category1   = "ncbtag>0 && ncjets==1 && nfjets >0"
    category2J  = "ncbtag>0 && ncjets==2 && nfjets==0"
    
    selections = [
      #("1btag",  "%s && %s && %s"%(baseline,categorybbA,"pzetamiss-0.85*pzetavis>-40 && pfmt_1<40"), ),
      ("1b1f",   "%s && %s && %s"%(baseline,category1,  "pfmt_1<60"),                                ),
      ("1b1c",   "%s && %s && %s"%(baseline,category2J, "pfmt_1<60"),                                ),
    ]
    
    for name, cuts in selections:
      print '>>> %s: "%s"'%(name,cuts)
      samples.measurePurityInSignalWindow(var, nbinx, xmin, xmax, cuts, QCD=True)
    


def compareSelectionsForSFrameSample(samples):
    """Compare the shapes of different selections for an SFrame sample."""
    
    channel  = "mutau"
    treename = "tree_%s_cut_relaxed"%(channel)
    isocuts  = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
    vetos    = "lepton_vetos==0"
    baseline = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%(isocuts,vetos)
    samples.setChannel(channel,treename=treename)
    
    samplenames = [
      ("DY",    "DY",    "DY",                  ),
      ("ZTT",   "ZTT",   "DY", "gen_match_2==5" ),
      ("data",  "data",  "SingleMuon",          ),
      ("JTF",   "JTF",   "JTF",                 ),
      ("stack", "stack", "stack",               ),
    ]
    
    selectionsets = [
      ("DM1_m_vis_cut",  "#DM1",
       [sel("m_T<50",               "%s && %s"%(baseline,"pfmt_1<50 && 0.35<m_2 && m_2<1.20 && decayMode_2==1")), #decayMode_2==10
        sel("m_T<50, 50<m_vis<100", "%s && %s"%(baseline,"pfmt_1<50 && 0.35<m_2 && m_2<1.20 && 50<m_vis && m_vis<100 && decayMode_2==1"))]),
      ("DM10_m_vis_cut", "#DM10",
       [sel("m_T<50",               "%s && %s"%(baseline,"pfmt_1<50 && 0.85<m_2 && m_2<1.40 && decayMode_2==10")), #decayMode_2==10
        sel("m_T<50, 50<m_vis<100", "%s && %s"%(baseline,"pfmt_1<50 && 0.85<m_2 && m_2<1.40 && 50<m_vis && m_vis<100 && decayMode_2==10"))]),
      ("DM1_restr",      "#DM1",
       [sel("no tau mass restr.",   "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==1")), #decayMode_2==10
        sel("0.35<m_tau<1.20",      "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==1 && 0.35<m_2 && m_2<1.20"))]),
      ("DM10_restr",     "#DM10",
       [sel("no tau mass restr.",   "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==10")), #decayMode_2==10
        sel("0.85<m_tau<1.40",      "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==10 && 0.85<m_2 && m_2<1.40"))]),
    ]
    
    variables = [
      var("m_2",    28, 0.20, 1.6,   title="m_tau", only='m_2.*decayMode_2==1(?!0)', ),
      var("m_2",    22, 0.70, 1.8,   title="m_tau", only='m_2.*decayMode_2==10',     ),
      var("m_vis",  20,   50, 150,   only="m_vis" ),
    ]
    
    # SETTINGS
    tag       = ""
    outdir    = "./checks"
    ratio     = True
    norm      = True
    staterror = True
    JFR       = True
    exts      = ['png','pdf']
    
    for sampleinfo  in samplenames:
      samplename, sampletitle, searchterm = sampleinfo[:3]
      extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
      sample = None if "stack" in searchterm or "JTF" in searchterm else samples.get(searchterm,unique=True)
      
      for setname, settitle, selectionset in selectionsets:
        #print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),selection.name.replace(' ','_')), color = "magenta", bold=True)
        
        # LOOP over VARIABLES
        for variable in variables:        
          hists  = [ ]
          stacks = [ ]
                    
          if any(not variable.plotForSelection(s) or not s.plotForVariable(variable) for s in selectionset):
            continue
          
          for i, selection in enumerate(selectionset,1):
            app = "_%s"%i
            if "stack" in samplename:
              stack = samples.getStack(variable,selection,append=app,title=selection.title,JFR=JFR,split=False)
              hist = stack.GetStack().Last().Clone()
              hist.SetTitle(selection.title)
              stacks.append(stack)
            elif "JTF" in samplename:
              hist = samples.jetFakeRate(variable,selection,append=app,title=selection.title)
            else:
              hist = sample.hist(variable,selection,append=app,title=selection.title,extracuts=extracuts)
            hists.append(hist)
          if len(hists)!=len(selections): continue
          
          # NAME
          filename = "%s/%s_%s_%s%s.png" % (outdir,variable.filename,samplename.replace(' ','_'),setname,tag)
          filename = makeFileName(filename)
          
          # TITLE
          name       = variable.name
          xtitle     = variable.title
          title      = "%s, %s"%(sampletitle,settitle)
          position   = "" #"centerright"
          ratiorange = 0.11
          
          # PLOT
          plot = Plot(hists,title=title) #, name=name, title=title, channel=channel, QCD=QCD)
          plot.plot(xtitle,ratio=ratio,norm=norm,staterror=staterror,position=position,ratiorange=ratiorange) #, position=position, staterror=staterror, ratio=ratio, errorbars=errorbars, data=data)
          plot.saveAs(filename,ext=exts)
          close(stacks)
    


def compareSFrameSamples(samples1,samples2):
    """Compare shapes of SFrame samples."""
    
    # CHANNEL
    if "mumu" in configFile:
      channel  = "mumu"
      treename = "tree_%s"%(channel)
    else:
      channel  = "mutau"
      treename = "tree_%s_cut_relaxed"%(channel)
    
    isocuts    = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
    isocutsMM  = "iso_1<0.15 && iso_2<0.15"
    vetos      = "lepton_vetos==0"
    vetosMM    = "extraelec_veto==0 && extramuon_veto==0"
    baseline   = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%(isocuts,vetos)
    baselineMM = "%s && %s && q_1*q_2<0 && 70<m_vis && m_vis<110"%(isocutsMM,vetosMM)
    
    samples1.setChannel(channel,treename=treename)
    samples2.setChannel(channel,treename=treename)
    
    samplesets = [
      ( 'DY', "Drell-Yan",
       [(samples1,"HTT Z pt", "DY"), (samples2, "Z pT + 1 b tag", "DY")]),
#       ( 'DY', "Drell-Yan",
#        [(samples1,"no Rochester", "DY"), (samples2, "Rochester", "DY")]),
#       ( 'ZTT', "Z -> tau_{mu}tau_{h}", "gen_match_2==5",
#        [(samples1,"no Rochester", "DY"), (samples2, "Rochester", "DY")]),
#       ( 'ZL', "Z -> #it{ll}, #it{l} -> tau_h fake", "gen_match_2<5",
#        [(samples1,"no Rochester", "DY"), (samples2, "Rochester", "DY")]),
#       ( 'data', "data",
#         [(samples1,"no Rochester", "SingleMuon"), (samples2, "Rochester", "SingleMuon")]),
    ]
    
    selections = [
      sel("baseline",       "%s"%(baseline)                     ),
#       sel("m_T<50",         "%s && %s"%(baseline,"pfmt_1<50")   ),
#       sel("1 b tag",        "%s && %s"%(baseline,"nbtags>0")    ),
#       sel("ZMM region",           baselineMM, title="Z -> mumu region"),
    ]
    
    variables = [
      #var("m_2",    28, 0.20, 1.6, title="m_tau" ),
#       var("m_2",    22, 0.70, 1.8, title="m_tau" ),
      var("m_sv",   50,    0, 200, cbinning={'nc?btag':(44,0,220)} ),
#       var("m_vis",  30,    0, 150, position="left" ),
#       var("m_vis",  24,   50, 110, filename="$NAME_zoom",  position="right" ),
#       var("m_vis",  20,   70, 110, filename="$NAME_zoomZ", position="right" ),
#       var("pt_1",   50,    0, 200, title="muon pt", position="centerright" ),
#       var("pt_2",   35,    0, 140, title="tau pt",  position="centerright" ),
#       var("m_vis",  40,   70, 110, title="dimuon mass m_mumu", filename="m_mumu", position="left" ),
#       var("pt_ll",  50,    0, 200, title="dimuon pt",          position="centerright" ),
#       var("pt_1",   50,    0, 200, title="leading muon pt",    position="centerright" ),
#       var("pt_2",   35,    0, 140, title="subleading muon pt", position="centerright" ),
    ]
    
    # SETTINGS
    tag       = ""
    outdir    = "./checks"
    ratio     = True
    norm      = True and False
    staterror = True
    JFR       = True #and False
    exts      = ['png','pdf']
    
    for setinfo in samplesets:
      samplelist = [ ]
      setname, settitle, sampleset = setinfo[:3]
      extracuts0 = "" if len(sampleinfo)<4 else sampleinfo[3]
      print '>>>\n>>> compareSFrameSamples "%s"'%(setname)
      
      for sampleinfo in sampleset:
        set, sampletitle, searchterm = sampleinfo[:3]
        extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
        extraweight = "" if len(sampleinfo)<5 else sampleinfo[4]
        if extracuts0:
          if extraweight: extracuts = "%s && %s"%(extracuts0,extracuts)
          else:           extracuts = extracuts0
        sample = set.get(searchterm,unique=True)
        samplelist.append((sample,sampletitle,extracuts,extraweight))
      
      for selection in selections:
        #print ">>>\n>>> " + color("_%s:_%s_" % (channel.replace(' ','_'),selection.name.replace(' ','_')), color = "magenta", bold=True)
        
        # LOOP over VARIABLES
        for variable in variables:        
          hists  = [ ]
          
          if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
            continue
          
          for i, (sample,sampletitle,extracuts,extraweight) in enumerate(samplelist,1):
            app = "_%s"%i
            hist = sample.hist(variable,selection,append=app,title=sampletitle,extracuts=extracuts,weight=extraweight)
            hists.append(hist)
          
          # NAME
          filename = "%s/%s_%s_%s%s.png"%(outdir,variable.filename,setname.replace(' ','_'),selection.filename,tag)
          filename = makeFileName(filename)
          
          # TITLE
          name       = variable.name
          xtitle     = variable.title
          title      = "%s, %s"%(settitle,selection.title)
          position   = variable.position
          if 'ZL' in setname and "zoom" in filename:
            position = 'left'
          ratiorange = 0.11
          
          # PLOT
          plot = Plot(hists,title=title)
          plot.plot(xtitle,ratio=ratio,norm=norm,staterror=staterror,position=position,ratiorange=ratiorange)
          plot.saveAs(filename,ext=exts)
   


def plotHist2D(samples):
    """Compare shapes."""
    
    channel  = "mutau"
    treename = "tree_%s_cut_relaxed"%(channel)
    isocuts  = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
    vetos    = "lepton_vetos==0"
    baseline = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%(isocuts,vetos)
    samples.setChannel(channel,treename=treename)
    
    samplenames = [
#       ("DY",   "DY",   "DY",                  ),
      ("ZTT",  "ZTT",  "DY", "gen_match_2==5" ),
#       ("JTF",  "JTF",  "JTF",                 ),
#       ("data", "data", "SingleMuon",          ),
      #("stack", "stack", "stack",               ),
    ]
    
    selections = [
      sel("#DM1, m_T<50",                "%s && %s"%(baseline,"pfmt_1<50 && decayMode_2==1")),
      sel("#DM10, m_T<50",               "%s && %s"%(baseline,"pfmt_1<50 && decayMode_2==10")),
      sel("#DM1, m_T<50, 50<m_vis<100",  "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==1"),  filename="DM1-ZTTregion2"),
      sel("#DM10, m_T<50, 50<m_vis<100", "%s && %s"%(baseline,"pfmt_1<50 && 50<m_vis && m_vis<100 && decayMode_2==10"), filename="DM10-ZTTregion2"),
    ]
    
    variables = [
      (var("m_2",   28, 0.20, 1.6, title="m_tau", only='decayMode_2==1(?!0)'),  var("m_vis",  10,  50, 100, only="m_vis" )),
      (var("m_2",   22, 0.70, 1.8, title="m_tau", only='decayMode_2==10'),      var("m_vis",  10,  50, 100, only="m_vis" )),
      (var("m_2",   28, 0.20, 1.6, title="m_tau", only='decayMode_2==1(?!0)'),  var("m_vis",  36,  20, 200, veto="m_vis" )),
      (var("m_2",   22, 0.70, 1.8, title="m_tau", only='decayMode_2==10'),      var("m_vis",  36,  20, 200, veto="m_vis" )),
    ]
    
    # SETTINGS
    tag       = ""
    outdir    = "./checks"
    ratio     = True
    norm      = True
    staterror = True
    JFR       = True
    exts      = ["png","pdf"]
    
    for sampleinfo  in samplenames:
      samplename, sampletitle, searchterm = sampleinfo[:3]
      extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
      sample = None if "stack" in searchterm or "JTF" in searchterm else samples.get(searchterm,unique=True)
      
      for selection in selections:
        
        # LOOP over VARIABLES
        for xvariable, yvariable in variables:
          if not xvariable.plotForSelection(selection) or not selection.plotForVariable(xvariable) or\
             not yvariable.plotForSelection(selection) or not selection.plotForVariable(yvariable):
            continue
          print ">>>\n>>> "+color("_%s:_%s_-_%s_vs_%s_"%(channel.replace(' ','_'),selection.name.replace(' ','_'),xvariable.name.replace(' ','_'),yvariable.name.replace(' ','_')),color="magenta",bold=True)
          
          # NAME
          filename = "%s/%s_vs_%s_%s_%s%s.png"%(outdir,yvariable.filename,xvariable.filename,samplename.replace(' ','_'),selection.filename,tag)
          filename = makeFileName(filename)
          
          # TITLE
          xtitle     = xvariable.title
          ytitle     = yvariable.title
          title      = "%s, %s"%(sampletitle,selection.title)
          position   = "" #"centerright"
          
          # BINNING & CUTS
          xvar, yvar = xvariable.name, yvariable.name
          nxbins, xmin, xmax = xvariable.getBinning()
          nybins, ymin, ymax = yvariable.getBinning()
          cuts = combineCuts(selection.selection,extracuts)
          
          # HIST
          #if "stack" in samplename:
          #  stack = samples.getStack(variable,selection,append=app,title=selection.title,JFR=JFR,split=False)
          #  hist = stack.GetStack().Last().Clone()
          #  hist.SetTitle(selection.title)
          #  stacks.append(stack)
          if "JTF" in samplename:
            hist = samples.jetFakeRate2D(xvar,nxbins,xmin,xmax,yvar,nybins,ymin,ymax,cuts,title=selection.title)
          else:
            hist = sample.hist2D(xvar,nxbins,xmin,xmax,yvar,nybins,ymin,ymax,cuts)
          
          # LINES
          print title
          line = [(0.85,ymin,0.85,ymax),(1.40,ymin,1.40,ymax)] if "DM10" in filename else\
                 [(0.35,ymin,0.35,ymax),(1.20,ymin,1.20,ymax)] if "DM1" in filename else [ ]
          
          # PLOT
          plot = Plot2D(hist)
          plot.plot(xtitle=xtitle,ytitle=ytitle,ztitle="Events",line=line,profile='x',
                    pentry="x-profile",title=title,legend=True,position='left')
          plot.saveAs(filename,ext=exts)
          


def compareSFrameHistograms():
    print ">>>\n>>> compareSFrameHistograms()"
    
    tag = "_filter"
    globalTag = "_Moriond"
    indir  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    outdir = OUT_DIR
    
    dirname = "checks"
    massesX = [20,28,40,50,60,70]
    massesA = [25,30,40,50,60,70]
    variables = [ ]
    variables_VLQ = [
      #( "M_tautau",         "m_{#tau#tau}",             100,   0, 100 ),
      #( "DeltaR_tautau",    "DeltaR_tautau",             -1,   0, 3.5 ),
      #( "DeltaR_taumu",     "DeltaR_taumu",              -1,   0, 3.5 ),
      #( "pt_genmuon",       "muon pt",                   40,   0,  80 ),
      ( "pt_gentau1",       "leading tau pt",            50,   0, 200 ),
      ( "pt_gentau2",       "subleading tau pt",         50,   0, 140 ),
      #( "pt_bquark",        "b quark pt",                50,   0, 200 ),
      #( "pt_lquark",        "light quark pt",            55,   0, 150 ),
      #( "eta_bquark",       "b quark eta",               25,  -5,   5 ),
      #( "eta_lquark",       "light quark eta",           25,  -5,   5, {'position':'center'} ),
    ]
    variables_bbA = [
      ( "M_tautau",         "m_{#tau#tau}",             220,   0, 110 ),
      ( "DeltaR_tautau",    "DeltaR_tautau",             50,   0, 4.0, {'position':'left'} ),
      ( "DeltaR_taumu",     "DeltaR_taumu",              50,   0, 4.0, {'position':'left'} ),
      ( "pt_genmuon",       "muon pt",                   40,   0,  80 ),
      ( "pt_gentau1",       "leading tau pt",            50,   0, 100 ),
      ( "pt_gentau2",       "subleading tau pt",         50,   0, 100 ),
      ( "pt_bquark1",       "leading b quark pt",        40,   0,  80 ),
      ( "pt_bquark2",       "subleading b quark pt",     40,   0,  80 ),
      ( "eta_bquark1",      "leading b quark eta",       25,  -5,   5, {'position':'bottomcenter'} ),
      ( "eta_bquark2",      "subleading b quark eta",    25,  -5,   5, {'position':'bottomcenter'} ),
    ]
    samplessets = [
      [ "VLQ_170", "VLQ m_B' = 170 GeV", [( "LowMass", "LowMassDiTau_M-%s_MB-170"%m,     "m_X = %s GeV"%m ) for m in massesX ],],
      #[ "VLQ_300", "VLQ m_B' = 300 GeV", [( "LowMass", "LowMassDiTau_M-%s_MB-300"%m,     "m_X = %s GeV"%m ) for m in massesX ],],
      #[ "VLQ_450", "VLQ m_B' = 450 GeV", [( "LowMass", "LowMassDiTau_M-%s_MB-450"%m,     "m_X = %s GeV"%m ) for m in massesX ],],
      #[ "bbA",     "gg -> bbA",          [( "SUSY",    "SUSYGluGluToBBa1ToTauTau_M-%s"%m,"m_A = %s GeV"%m ) for m in massesA ],],
    ]
    
    for setname, settitle, samples in samplessets:
      
      files = [ ]
      for subdir, name, title in samples:
        filename = "%s/%s/TauTauAnalysis.%s%s.root"%(indir,subdir,name,globalTag)
        if setname=="VLQ_170" and "28" in name: filename = "../../SFrameAnalysis_Moriond/TauTauResonances/TauTauAnalysis.LowMass28_filterPass.root"
        file = TFile( filename )
        files.append((title,file))
      
      variables_all = variables[:]
      if   'VLQ' in setname: variables_all += variables_VLQ
      elif 'bbA' in setname: variables_all += variables_bbA
      
      for varinfo in variables_all:
        
        var, vartitle, nbins, xmin, xmax = varinfo[:5]
        varkwargs = varinfo[5] if len(varinfo)>5 else { }
        
        hists = [ ]
        for title, file in files:
          histname = "%s/%s"%(dirname,var)
          hist = file.Get(histname)
          if nbins>0:
            rebin(hist,nbins,xmin,xmax)
          hist.SetTitle(title)
          hists.append(hist)
          
        # NAME
        canvasname = "%s/%s_%s_comparison%s.png"%(outdir,var,setname,tag)
        canvasname = makeFileName(canvasname)
        title      = "%s" % (settitle)
        position   = varkwargs.get('position', "" )
        
        if 'pt_gentau1'==var and 'VLQ_450' in setname: #('VLQ_300' in setname or 'VLQ_450' in setname):
          position = 'left'
        if 'pt_bquark'==var and ('VLQ_300' in setname or 'VLQ_450' in setname):
          position = 'left'
        
        # PLOT
        plot = Plot(hists, title=title, normalize=True)
        plot.plot(vartitle,ratio=False,linestyle=False,ylabel="A.U.",xmin=xmin,xmax=xmax,position=position)
        plot.saveAs(canvasname,ext=['png','pdf'])
      

def compareSFrameHistogram():
    print ">>>\n>>> compareSFrameHistogram()"
    
    tag = ""
    globalTag = "_Moriond"
    indir  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    outdir = OUT_DIR
    
    dirname = "checks"
    variables = [
      #( "M_tautau",         "m_{#tau#tau}",             100,   0, 100 ),
      #( "DeltaR_tautau",    "DeltaR_tautau",             -1,   0, 3.5 ),
      #( "DeltaR_taumu",     "DeltaR_taumu",              -1,   0, 3.5 ),
      #( "pt_genmuon",       "muon pt",                   40,   0,  80 ),
      #( "pt_gentau1",       "leading tau pt",            50,   0, 200 ),
      #( "pt_gentau2",       "subleading tau pt",         50,   0, 140 ),
      #( "pt_gentau_matched", "generator-level tau pt",     50,   0, 140 ),
      ( "dpt_gentau_matched", "tau (pt^{reco}-pt^{gen})/pt^{gen}", 100, -1, 1 ),
      #( "pt_bquark",        "b quark pt",                50,   0, 200 ),
      #( "pt_lquark",        "light quark pt",            55,   0, 150 ),
      #( "eta_bquark",       "b quark eta",               25,  -5,   5 ),
      #( "eta_lquark",       "light quark eta",           25,  -5,   5, {'position':'center'} ),
    ]
    samples = [
      ("VLQ-170_28","../../SFrameAnalysis_Moriond/TauTauResonances/TauTauAnalysis.LowMass28_filterPass.root"),
      #("VLQ-170_28","../../SFrameAnalysis_Moriond/TauTauResonances/TauTauAnalysis.LowMass28.UZH.root"),
    ]
    
    for samplename, filename in samples:
      file = TFile( filename )
      for varinfo in variables:
        
        var, vartitle, nbins, xmin, xmax = varinfo[:5]
        varkwargs = varinfo[5] if len(varinfo)>5 else { }
        
        histname = "%s/%s"%(dirname,var)
        hist = file.Get(histname)
        if nbins>0:
          rebin(hist,nbins,xmin,xmax)
        
        # NAME
        canvasname = "%s/%s_%s%s.png"%(outdir,var,samplename,tag)
        canvasname = makeFileName(canvasname)
        #title      = "%s" % (settitle)
        position   = varkwargs.get('position', "" )
        
        # PLOT
        plot = Plot(hist, normalize=True)
        plot.plot(vartitle,ratio=False,linestyle=False,ylabel="A.U.",xmin=xmin,xmax=xmax,legend=False)
        plot.saveAs(canvasname,ext=['png','pdf'])




def compareSFrameHistogram2D():
    print ">>>\n>>> compareSFrameHistogram2D()"
    
    tag = ""
    globalTag = "_Moriond"
    indir  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    outdir = OUT_DIR
    
    dirname = "checks"
    variables = [
      ( "pt_gentau_recotau", "generator-level tau p_{T} [GeV]", 0, 100, "reconstruction-level tau p_{T} [GeV]", 0, 100 ),
    ]
    samples = [
      ("VLQ-170_28","../../SFrameAnalysis_Moriond/TauTauResonances/TauTauAnalysis.LowMass28_filterPass.root"),
      #("VLQ-170_28","../../SFrameAnalysis_Moriond/TauTauResonances/TauTauAnalysis.LowMass28.UZH.root"),
    ]
    
    for samplename, filename in samples:
      file = TFile( filename )
      for varinfo in variables:
        
        var, xtitle, xmin, xmax, ytitle, ymin, ymax = varinfo
        ztitle = "events"
        
        histname = "%s/%s"%(dirname,var)
        hist = file.Get(histname)
        
        # NAME
        canvasname = "%s/%s_%s%s"%(outdir,var,samplename,tag)
        canvasname = makeFileName(canvasname)
        
        # PLOT
        drawHist2D(hist,xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax,canvas=canvasname)





def drawHist2D(hist,**kwargs):
    """Draw 2D histogram on canvas."""
      
    title      = kwargs.get('title',      ""           )
    xtitle     = kwargs.get('xtitle',     hist.GetXaxis().GetTitle() )
    ytitle     = kwargs.get('ytitle',     hist.GetYaxis().GetTitle() )
    ztitle     = kwargs.get('ztitle',     ""           )
    xmin       = kwargs.get('xmin',       None         )
    xmax       = kwargs.get('xmax',       None         )
    ymin       = kwargs.get('ymin',       None         )
    ymax       = kwargs.get('ymax',       None         )
    zmin       = kwargs.get('zmin',       None         )
    zmax       = kwargs.get('zmax',       None         )
    legend     = kwargs.get('legend',     True         )
    position   = kwargs.get('position',   ""           )
    text       = kwargs.get('text',       ""           )
    plottag    = kwargs.get('tag',        ""           )
    line       = kwargs.get('line',       None         )
    lentry     = kwargs.get('lentry',     None         )
    graphs     = kwargs.get('graph',      [ ]          )
    gentries   = kwargs.get('gentry',     [ ]          )
    canvasname = kwargs.get('canvas',     "hist2D.png" )
    option     = kwargs.get('option',     "COLZT"      )
    #if not re.search("\.(png|pdf|gif|tiff|root|C)$",canvasname,re.IGNORECASE):
    #  canvasname += ".png"
    lmargin    = 0.14
    rmargin    = 0.19 if ztitle else 0.12
    if zmin: hist.SetMinimum(zmin)
    if zmax: hist.SetMaximum(zmax)
    if not isinstance(graphs,list) and not isinstance(graphs,tuple):
      graphs = [ graphs ]
    if not isinstance(gentries,list) and not isinstance(gentries,tuple):
      gentries = [ gentries ]
    colors2D = [ kOrange+7, kMagenta-4 ] # kOrange-3,
    
    canvas = TCanvas("canvas","canvas",100,100,800,700)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetTopMargin(    0.07  ); canvas.SetBottomMargin(  0.14  )
    canvas.SetLeftMargin( lmargin ); canvas.SetRightMargin( rmargin )
    canvas.SetTickx(0); canvas.SetTicky(0)
    canvas.SetGrid()
    canvas.cd()
    
    if legend:
      textsize   = 0.041
      lineheight = 0.050
      width      = 0.25
      height     = textsize*1.10*len([o for o in graphs+[title,text,lentry] if o])
      if 'left' in position.lower():   x1 = 0.17; x2 = x1+width
      else:                            x1 = 0.78; x2 = x1-width 
      if 'bottom' in position.lower(): y1 = 0.20; y2 = y1+height
      else:                            y1 = 0.90; y2 = y1-height
      legend = TLegend(x1,y1,x2,y2)
      legend.SetTextSize(textsize)
      legend.SetBorderSize(0)
      legend.SetFillStyle(0)
      legend.SetFillColor(0)
      if title:
        legend.SetTextFont(62)
        legend.SetHeader(title) 
      legend.SetTextFont(42)
    
    hist.GetXaxis().SetTitleSize(0.058)
    hist.GetYaxis().SetTitleSize(0.058)
    hist.GetZaxis().SetTitleSize(0.056)
    hist.GetXaxis().SetLabelSize(0.048)
    hist.GetYaxis().SetLabelSize(0.048)
    hist.GetZaxis().SetLabelSize(0.044)
    hist.GetXaxis().SetLabelOffset(0.010)
    hist.GetXaxis().SetTitleOffset(1.04)
    hist.GetYaxis().SetTitleOffset(1.12)
    hist.GetZaxis().SetTitleOffset(1.25)
    hist.GetZaxis().CenterTitle(True)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle(ytitle)
    hist.GetZaxis().SetTitle(ztitle)
    hist.SetMarkerColor(kRed);
    hist.Draw(option)
    
    for i, graph in enumerate(graphs):
      if not graph: continue
      color = colors2D[i%len(colors2D)]
      graph.SetLineColor(color)
      graph.SetMarkerColor(color)
      graph.SetLineWidth(3)
      graph.SetMarkerSize(3)
      graph.SetLineStyle(1)
      graph.SetMarkerStyle(3)
      graph.Draw('LPSAME')
      if legend:
        gtitle = gentries[i] if i<len(gentries) else graph.GetTitle()
        legend.AddEntry(graph, graph.GetTitle(), 'lp')
    
    if line:
      line = TLine(*line[:4])
      line.SetLineColor(kBlack)
      line.SetLineStyle(7)
      line.SetLineWidth(2)
      line.Draw('SAME')
      if lentry and legend:
        legend.AddEntry(line, lentry, 'l')
    
    if text:
      if legend:
        legend.AddEntry(0,text,'')
      else:
        if 'left' in position.lower():   align = 10; x = 0.17
        else:                            align = 30; x = 0.78
        if 'bottom' in position.lower(): align += 1; y = 0.20
        else:                            align += 3; y = 0.90
        latex = TLatex()
        latex.SetTextSize(0.050)
        latex.SetTextAlign(align)
        latex.SetTextFont(42)
        #latex.SetTextColor(kRed)
        latex.SetNDC(True)
        latex.DrawLatex(x,y,text)
    if legend:
      legend.Draw()
      
    
    #CMS_lumi.relPosX = 0.15
    #CMS_lumi.CMS_lumi(canvas,13,0)
    canvas.SaveAs(canvasname+".png")
    canvas.SaveAs(canvasname+".pdf")
    canvas.Close()









#def compareVarIntegrals():
#    """Compare intregral of variables (e.g. weights) of the same sample file."""
#    print ">>>\n>>> compareVarIntegrals()"
#    # TODO: allow for stitching
#    
#    dirname       = ensureDirectory("%s/%s"%(OUT_DIR,"integrals"))
#    mylabel       = "_Moriond"
#    channel       = "mutau"
#    weight        = "" #"weight*trigweight_or_1"
#    triggers      = "abs(eta_1)<2.1 && trigger_cuts==1"
#    baseline      = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
#    category1_nob = "ncjets == 1 && nfjets  > 0 && jpt_1>30 && jpt_2>30"
#    category2_nob = "ncjets == 2 && nfjets == 0 && jpt_1>30 && jpt_2>30 && dphi_ll_bj>2 && met<60"
#    category1     = "ncjets == 1 && nfjets  > 0 && jpt_1>30 && jpt_2>30 && nbtag > 0"
#    category2     = "ncjets == 2 && nfjets == 0 && jpt_1>30 && jpt_2>30 && nbtag > 0 && dphi_ll_bj>2 && met<60"
#    category12    = "ncjets == 1 && nfjets  > 0 && jpt_1>30 && jpt_2>30 && nbtag > 0 && met<60 && pfmt_1<60"
#    category22    = "ncjets == 2 && nfjets == 0 && jpt_1>30 && jpt_2>30 && nbtag > 0 && dphi_ll_bj>2 && met<60 && pfmt_1<60"
#    
#    filenames = [
#        ("TT",  "TT_TuneCUETP8M1",               "ttbar"        ),
##         ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1",  "DY inclusive" ),
##         ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1", "DY + 1 jet"   ),
##         ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1", "DY + 2 jets"  ),
##         ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1", "DY + 3 jets"  ),
##         ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1", "DY + 4 jets"  ),
#    ]
#    
#    vars        = [
##                     (  "b tag weight",
##                      [("weightbtag",         "nominal"                ),
##                       ("weightbtag_bcDown",  "heavy flavor down"      ),
##                       ("weightbtag_bcUp",    "heavy flavor up"        ),
##                       ("weightbtag_udsgDown","light flavor down"      ),
##                       ("weightbtag_udsgUp",  "light flavor up"        ), ]),
##                     (  "jet multiplicity",
##                      [("njets",             "nominal"                   ),
##                       ("njets_jesUp",       "JES up"                    ),
##                       ("njets_jesDown",     "JES down"                  ),
##                       ("njets_nom",         "JES nominal"               ),
##                       ("njets_jerUp",       "JER up"                    ),
##                       ("njets_jerDown",     "JER down"                  ),]),
##                     (  "category 1 JEC",
##                      [(      category1,            "nominal"       ),
##                       (shift(category1,'jerDown'), "JER down"      ),
##                       (shift(category1,'jerUp'  ), "JER up"        ),
##                       (shift(category1,'jesDown'), "JES down"      ),
##                       (shift(category1,'nom'    ), "JES central"   ),
##                       (shift(category1,'jesUp'  ), "JES up"        ),]),
##                     (  "category 2 JEC",
##                      [(      category2,            "nominal"       ),
##                       (shift(category2,'jerDown'), "JER down"      ),
##                       (shift(category2,'jerUp'  ), "JER up"        ),
##                       (shift(category2,'jesDown'), "JES down"      ),
##                       (shift(category2,'nom'    ), "JES central"   ),
##                       (shift(category2,'jesUp'  ), "JES up"        ),]),
#                    (  "category 1.2 JEC",
#                     [(      category12,            "nominal"       ),
#                      (shift(category12,'jerDown'), "JER down"      ),
#                      (shift(category12,'jerUp'  ), "JER up"        ),
#                      (shift(category12,'jesDown'), "JES down"      ),
#                      (shift(category12,'nom'    ), "JES central"   ),
#                      (shift(category12,'jesUp'  ), "JES up"        ),]),
#                    (  "category 2.2 JEC",
#                     [(      category22,            "nominal"       ),
#                      (shift(category22,'jerDown'), "JER down"      ),
#                      (shift(category22,'jerUp'  ), "JER up"        ),
#                      (shift(category22,'jesDown'), "JES down"      ),
#                      (shift(category22,'nom'    ), "JES central"   ),
#                      (shift(category22,'jesUp'  ), "JES up"        ),]),
#                    (  "category 1.2 UncEn",
#                     [(      category12,              "nominal"       ),
#                      (shift(category12,'UncEnUp'  ), "UncEn down"    ),
#                      (shift(category12,'nom'      ), "JES central"   ),
#                      (shift(category12,'UncEnDown'), "UncEn up"      ), ]),
#                    (  "category 2.2 UncEn",
#                     [(      category22,              "nominal"       ),
#                      (shift(category22,'UncEnUp'  ), "UncEn down"    ),
#                      (shift(category22,'nom'      ), "JES central"   ),
#                      (shift(category22,'UncEnDown'), "UncEn up"      ),]),
#    ]
#    
#    cuts = [
##         ("no cuts",  "channel>0"),
#        ("baseline",             "%s"       % (baseline)),
##         ("category 1 (no b)",    "%s && %s" % (baseline,category1_nob)),
##         ("category 2 (no b)",    "%s && %s" % (baseline,category2_nob)),
##         ("category 1",           "%s && %s" % (baseline,category1)),
##         ("category 2",           "%s && %s" % (baseline,category2)),
##         ("optimized category 1", "%s && %s" % (baseline,category12)),
##         ("optimized category 2", "%s && %s" % (baseline,category22)),
#    ]
#    
#    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ]
#    
#    for ifile, (subdir,filename0,samplename) in enumerate(filenames,1):
#        print ">>>\n>>>   %2s: %10s, %10s"%(ifile,filename0,samplename)
#        filename    = "%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,subdir,filename0,mylabel)
#        file        = TFile(filename)
#        filename0   = filename0.split('_')[0]
#        #if 'Jets' in filename0: filename0 = filename0[:filename0.index('Jets')] + "J"
#        for cutname, cut in cuts:
#            for ivar, (varname0,varlist) in enumerate(vars,1):
#                print ">>>   %s - %s" % (cutname,varname0)
#                
#                # CHECK
#                if ("category 1" in cutname and "category 2" in varname0) or ("category 2" in cutname and "category 1" in varname0):
#                    print "Warning! compareVarIntegrals - skipping \"%s\" selections for \"%s\" variable"%(cutname,varname0)
#                    continue
#                
#                N       = len(varlist)+1
#                (a,b)   = (0,N)
#                (x1,x2) = (0.75,0.91)
#                (y1,y2) = (0.90,0.65)
#                canvas = TCanvas("canvas","canvas",100,100,800,600) # TODO: smaller height + larger margins and ymax ?
#                canvas.SetBottomMargin(0.10)
#                canvas.SetRightMargin(0.06)
#                canvas.SetLeftMargin(0.12)
#                canvas.SetTopMargin(0.07)
#                #legend = TLegend(x1,y1,x2,y2)
#                
#                var0        = varname0
#                histname0   = "%s"%(varname0.replace(' ','_'))
#                hist0       = TH1F(histname0,varname0,N,a,b)
#                hists       = [hist0]
#                integrals   = [ ]
#                ymax        = 0
#                treename    = "tree_%s_cut_relaxed"%channel
#                
#                for i, (var,varname) in enumerate(varlist,1):
#                    histname    = "%s_%s"%(subdir,varname.replace(' ','_'))
#                    (N,a,b)     = (2,0,2)
#                    hist        = TH1F(histname,histname,N,a,b)
#                    tree        = file.Get(treename)
#                    weight1     = combineWeights(weight,var)
#                    cut1        = "(%s)*%s"%(cut,weight1)
#                    out         = tree.Draw("%s >> %s"%(1,histname),cut1,"gOff")
#                    N1          = hist.GetEntries()
#                    I1          = hist.GetBinContent(2)
#                    #hist.Scale(1/N1)
#                    #print ">>>     N1 = %s,I1 = %s"%(N1,I1)
#                    integrals.append(I1)
#                    if I1 <= 0:
#                        print "Warning! compareVarIntegrals: integral %s I1 = %.1f < 0"%(histname,I1)
#                    hist0.SetBinContent(i,I1)
#                    for split in ["up", "down", "Up", "Down", "central", "center"]:
#                        if " "+split in varname:
#                            spliti  = varname.rfind(" "+split)
#                            varname = "#splitline{%s}{%s}"%(varname[:spliti],varname[spliti:].lstrip(' '))
#                    hist0.GetXaxis().SetBinLabel(i,varname)
#                    hmax        = hist.GetMaximum()
#                    if hmax > ymax:
#                        ymax = hmax
#                    #hist.SetLineWidth(3)
#                    #hist.SetLineStyle(1+(i-1)%2)
#                    #hist.SetLineColor(colors[i-1])
#                    #hist.SetMarkerSize(0)
#                    #if i==0: hist.Draw("Ehist")
#                    #else:    hist.Draw("Ehistsame")
#                    #legend.AddEntry(hist,varname, 'l')
#                    #hists.append(hist)
#                    ROOT.gDirectory.Delete(hist.GetName())
#                
#                gPad.SetTitle(varname0)
#                #hist0.SetTitleOffset(1.0)
#                #print "hist0.GetTitleSize()   = %s"%(hist0.GetTitleSize())
#                #print "hist0.GetTitleOffset() = %s"%(hist0.GetTitleOffset())
#                hist0.Draw("Ehist")
#                gPad.SetTitle(varname0)
#                hist0.SetLineColor(colors[0])
#                hist0.SetLineWidth(2)
#                hist0.SetMarkerSize(0)
#                #hist0.GetXaxis().SetTitle(varname0)
#                hist0.GetYaxis().SetTitle("A.U.")
#                hist0.GetXaxis().SetTitleSize(0.06)
#                hist0.GetYaxis().SetTitleSize(0.05)
#                hist0.GetXaxis().SetTitleOffset(0.94)
#                hist0.GetYaxis().SetTitleOffset(1.26)
#                hist0.GetXaxis().SetLabelSize(0.045)
#                hist0.GetYaxis().SetLabelSize(0.040)
#                hist0.GetXaxis().CenterLabels()
#                hist0.SetMaximum(ymax*1.24)
#                #legend.SetTextSize(0.032)
#                #legend.SetBorderSize(0)
#                #legend.SetFillStyle(0)
#                #legend.Draw()
#                gStyle.SetOptStat(0)
#                #gStyle.SetOptTitle(1) # show title
#                #gStyle.SetTitleBorderSize(0)
#                
#                title     = TLatex()
#                top       = canvas.GetY2()
#                topmargin = canvas.GetTopMargin()
#                fontsize  = topmargin*0.60
#                title.SetTextFont(61)
#                title.SetTextAlign(11)
#                title.SetTextSize(fontsize)
#                title.DrawLatex(0,top*(1-topmargin*0.90),"%s (%s, %s)"%(varname0,filename0,cutname))
#                
#                text = TLatex()
#                for i, I1 in enumerate(integrals):
#                    fraction = 100*(I1/integrals[0]-1)
#                    text.SetTextFont(42)
#                    text.SetTextSize(0.034)
#                    text.SetTextAlign(22)
#                    text.DrawLatex(i+0.5,ymax*1.10,"#splitline{ %.1f}{  %6.3f%%}"%(I1,fraction))
#                
#                cutname     = cutname.replace(' ','_').replace('(','-').replace(')','')
#                canvas.SaveAs("%s/integral_comparison_%s-%s-%s.png" % (dirname,var0.replace(' ','_'),cutname,filename0))
#                canvas.Close()
#                
#                ROOT.gDirectory.Delete(histname0)
#                #for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
#        file.Close()
#    
#
#
#
#
#def compareVarsForSamples():
#    """Compare shapes of different variables for the same sample file."""
#    print ">>>\n>>> compareVarsForSamples()"
#    
#    filenames   = [
#        ("TT",  "TT_TuneCUETP8M1",               "ttbar",       ),
##         ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1",  "DY inclusive" ),
##         ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1", "DY + 1 jet"   ),
##         ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1", "DY + 2 jets"  ),
##         ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1", "DY + 3 jets"  ),
##         ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1", "DY + 4 jets"  ),
#                ]
#    
#    vars        = [
#        (   "b tag weight", "weightbtag_bcShifts",   50,0,1.9,
#         [( "nominal",                  "weightbtag"          ),
#          ( "heavy flavour shift up",   "weightbtag_bcUp"     ),
#          ( "heavy flavour shift down", "weightbtag_bcDown"   ),]),
#        (   "b tag weight", "weightbtag_udsgShifts", 50,0,1.9,
#         [( "nominal",                  "weightbtag"          ),
#          ( "light flavour shift up",   "weightbtag_udsgUp"   ),
#          ( "light flavour shift down", "weightbtag_udsgDown" ),]),
#    ]
#    
#    dirname     = ensureDirectory("%s/%s"%(OUT_DIR,"shapes"))
#    mylabel     = "_Moriond"
#    channel     = "mutau"
#    weight      = "weight*trigweight_or_1"
#    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"
#    cut         = "(%s)*%s"%(baseline,weight)
#    
#    cuts = [
#        #("no cuts",  "channel>0"),
#        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
#    ]
#    
#    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ]
#    
#    for ifile, (subdir,filename0,samplename) in enumerate(filenames,1):
#        print ">>>   %2s: %10s, %10s"%(ifile,filename0,samplename)
#        filename    = "%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,subdir,filename0,mylabel)
#        file        = TFile(filename)
#        for cutname, cut in cuts:
#            for ivar, (varname0,var0,N,a,b,varlist) in enumerate(vars):
#                print ">>>   %s - %s" % (cutname,varname0)
#                cut     = "(%s)*%s"%(cut,weight)
#                
#                (x1,x2) = (0.17,0.33)
#                (y1,y2) = (0.90,0.65)
#                canvas = TCanvas("canvas","canvas",100,100,800,600)
#                canvas.SetBottomMargin(0.12)
#                canvas.SetRightMargin(0.05)
#                canvas.SetLeftMargin(0.12)
#                canvas.SetTopMargin(0.05)
#                legend = TLegend(x1,y1,x2,y2)
#                
#                hists = [ ]
#                max_bin = 0
#                treename    = "tree_%s_cut_relaxed"%channel
#        
#                for i, (var,varname) in enumerate(varlist):
#                    histname    = "%s_%s"%(subdir,var)
#                    hist        = TH1F(histname,histname,N,a,b)
#                    tree        = file.Get(treename)
#                    out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
#                    N1          = hist.GetEntries()
#                    hist.Scale(1/N1)
#                    hmax        = hist.GetMaximum()
#                    if hmax > max_bin:
#                        max_bin = hmax
#                    hist.SetLineWidth(3)
#                    hist.SetLineStyle(1+(i-1)%2)
#                    hist.SetLineColor(colors[i-1])
#                    hist.SetMarkerSize(0)
#                    if i==0: hist.Draw("Ehist")
#                    else:    hist.Draw("Ehistsame")
#                    legend.AddEntry(hist,varname, 'l')
#                    hists.append(hist)
#            
#                hist1 = hists[0]
#                hist1.SetTitle("")
#                hist1.GetXaxis().SetTitle(varname0)
#                hist1.GetYaxis().SetTitle("A.U.")
#                hist1.GetXaxis().SetTitleSize(0.06)
#                hist1.GetYaxis().SetTitleSize(0.06)
#                hist1.GetXaxis().SetTitleOffset(0.95)
#                hist1.GetYaxis().SetTitleOffset(0.9)
#                hist1.GetXaxis().SetLabelSize(0.045)
#                hist1.GetYaxis().SetLabelSize(0.045)
#                hist1.SetMaximum(max_bin*1.10)
#                legend.SetTextSize(0.032)
#                legend.SetBorderSize(0)
#                legend.SetFillStyle(0)
#                legend.Draw()
#                gStyle.SetOptStat(0)
#                cutname     = cutname.replace(' ','_').replace('(','-').replace(')','')
#                filename0   = filename0.split('_')[0]
#                canvas.SaveAs("%s/%s-%s-%s_comparison.png" % (dirname,var0,cutname,filename0))
#                canvas.Close()
#        
#                for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
#        file.Close()
#    
#
#
#
#
#def compareSamplesForVars():
#    """Compare the shape of a variable for different sample files."""
#    print ">>>\n>>> NUP()"
#    
#    filenames = [ ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1_Moriond",  "DY inclusive" ),
#                  ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 1 jet"   ),
#                  ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 2 jets"  ),
#                  ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 3 jets"  ),
#                  ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 4 jets"  ),]
#    
#    vars        = [ ("NUP","number of partons",7,0,7), ("njets","number of reconstructed jets",7,0,7), ]
#    
#    #dirname     = ensureDirectory("%s/%s"%(OUT_DIR,"compare"))
#    channel     = "mutau"
#    weight      = "weight*trigweight_or_1"
#    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"
#    cut         = "(%s)*%s"%(baseline,weight)
#    
#    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ] #kYellow+771, # kOrange+8
#    
#    for var, varname, N, a, b in vars:
#        print ">>>   %s" % (var)
#        
#        (x1,x2) = (0.74,0.90)
#        (y1,y2) = (0.90,0.65)
#        canvas = TCanvas("canvas","canvas",100,100,800,600)
#        canvas.SetBottomMargin(0.12)
#        canvas.SetRightMargin(0.05)
#        canvas.SetLeftMargin(0.12)
#        canvas.SetTopMargin(0.05)
#        legend = TLegend(x1,y1,x2,y2)
#        
#        hists = [ ]
#        files = [ ]
#        max_bin = 0
#        treename    = "tree_%s_cut_relaxed"%channel
#        
#        for i, (subdir,filename,samplename) in enumerate(filenames,1):
#            print ">>>   %2s: %10s, %10s"%(i,filename,samplename)
#            filename    = "%s/%s/TauTauAnalysis.%s.root"%(MORIOND_DIR,subdir,filename)
#            histname    = "%s_%s"%(var,i)
#            file        = TFile(filename)
#            #print ">>>     %2s: %10s, %3s, %3s, %3s"%(i,histname,N,a,b)
#            hist        = TH1F(histname,histname,N,a,b)
#            tree        = file.Get(treename)
#            out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
#            N1          = hist.GetEntries()
#            #print ">>>     %2s: %10s, out=%s, N=%s"%(i,samplename,out,N)
#            hist.Scale(1/N1)
#            hmax        = hist.GetMaximum()
#            if hmax > max_bin:
#                max_bin = hmax
#                #print ">>>   %s has %d entries" % (hist.GetName(),I)
#            hist.SetLineWidth(3)
#            hist.SetLineStyle(1+(i-1)%2) #3
#            hist.SetLineColor(colors[i-1])
#            hist.SetMarkerSize(0)
#            if i==0: hist.Draw("Ehist")
#            else:    hist.Draw("Ehistsame")
#            legend.AddEntry(hist,samplename, 'l')
#            hists.append(hist)
#            #print ">>>     before %s "%(type(hists[-1]))
#            files.append(file)
#        
#        hist1 = hists[0]
#        print ">>>   after %s "%(type(hists[0]))
#        hist1.SetTitle("")
#        hist1.GetXaxis().SetTitle(varname)
#        hist1.GetYaxis().SetTitle("A.U.")
#        hist1.GetXaxis().SetTitleSize(0.06)
#        hist1.GetYaxis().SetTitleSize(0.06)
#        hist1.GetXaxis().SetTitleOffset(0.9)
#        hist1.GetYaxis().SetTitleOffset(0.9)
#        hist1.GetXaxis().SetLabelSize(0.045)
#        hist1.GetYaxis().SetLabelSize(0.045)
#        hist1.SetMaximum(max_bin*1.10)
#        legend.SetTextSize(0.032)
#        legend.SetBorderSize(0)
#        legend.SetFillStyle(0)
#        legend.Draw()
#        gStyle.SetOptStat(0)
#        canvas.SaveAs("%s/%s_comparison.png" % (OUT_DIR,var))
#        canvas.Close()
#        
#        for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
#        for file in files: file.Close()
#    
#
#
#
#
#def compareVarsAndCutsForSamples():
#    print ">>>\n>>> compareVarsAndCutsForSamples()"
#    
#    dirname         = ensureDirectory("%s/%s"%(OUT_DIR,"shape"))
#    triggers        = "abs(eta_1)<2.1 && trigger_cuts==1"
#    baseline        = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
#    baseline_2j     = "%s && njets>1 && jpt_1>30 && jpt_1>30"%(baseline)
#    category1       = "ncjets == 1 && nfjets  > 0 && ncbtag > 0"
#    category2       = "ncjets == 2 && nfjets == 0 && ncbtag > 0 && dphi_ll_bj>2 && met<60"
#    category12      = "ncjets == 1 && nfjets  > 0 && ncbtag > 0 && met<60 && pfmt_1<60"
#    category22      = "ncjets == 2 && nfjets == 0 && ncbtag > 0 && dphi_ll_bj>2 && met<60 && pfmt_1<60"
#    
#    # TTbar CR
#    cuts_sets = [
##         ( "category 1: triggers",("m_sv",35,0.0,350),[
##             ("both triggers",        "%s && %s && %s" % (baseline,category2,"triggers==3")),
##             ("single lepton only",   "%s && %s && %s" % (baseline,category2,"triggers==1")),
##             ("cross trigger only",   "%s && %s && %s" % (baseline,category2,"triggers==2")), ]),
##         ( "category 2: triggers",("m_sv",35,0.0,350),[
##             ("both triggers",        "%s && %s && %s" % (baseline,category2,"triggers==3")),
##             ("single lepton only",   "%s && %s && %s" % (baseline,category2,"triggers==1")),
##             ("cross trigger only",   "%s && %s && %s" % (baseline,category2,"triggers==2")), ]),
##         ( "category 2: single muon",("m_sv",35,0.0,350),[
##             ("l #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2<5")),
##             ("real #tau",            "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==5")),
##             ("j #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==6")), ]),
##         ( "baseline: JER",("jpt_1",70,-10,340),[
##             ("nominal",         "jpt_1",                  baseline              ),
##             ("JES central",     "jpt_1_nom",        shift(baseline,   'nom'    )),
##             ("JER up",          "jpt_1_jerUp",      shift(baseline,   'jerUp'  )),
##             ("JER down",        "jpt_1_jerDown",    shift(baseline,   'jerDown')),     ]),
##         ( "baseline: JES",("jpt_1",70,-10,340),[
##             ("nominal",         "jpt_1",                  baseline              ),
##             ("JES nominal",     "jpt_1_nom",        shift(baseline,   'nom'    )),
##             ("JES up",          "jpt_1_jesUp",      shift(baseline,   'jesUp'  )),
##             ("JES down",        "jpt_1_jesDown",    shift(baseline,   'jesDown')),  ]),
##         ( "baseline, >=2 jets: JER",("met",62,-10,300),[
##             ("nominal",         "met",                    baseline_2j           ),
##             ("JES central",     "met",              shift(baseline_2j,'nom'    )),
##             ("JER up",          "met_jerUp",        shift(baseline_2j,'jerUp'  )),
##             ("JER down",        "met_jerDown",      shift(baseline_2j,'jerDown')),  ]),
##         ( "baseline, >=2 jets: JES",("met",62,-10,300),[
##             ("nominal",         "met",                    baseline_2j           ),
##             ("JES central",     "met",              shift(baseline_2j,'nom'    )),
##             ("JES up",          "met_jesUp",        shift(baseline_2j,'jesUp'  )),
##             ("JES down",        "met_jesDown",      shift(baseline_2j,'jesDown')),  ]),
##         ( "baseline, >=2 jets: JER",("pfmt_1",42,-10,300),[
##             ("nominal",         "pfmt_1",                 baseline_2j           ),
##             ("JES central",     "pfmt_1_nom",       shift(baseline_2j,'nom'    )),
##             ("JER up",          "pfmt_1_jerUp",     shift(baseline_2j,'jerUp'  )),
##             ("JER down",        "pfmt_1_jerDown",   shift(baseline_2j,'jerDown')),  ]),
##         ( "baseline, >=2 jets: JES",("pfmt_1",42,-10,200),[
##             ("nominal",         "pfmt_1",                 baseline_2j           ),
##             ("JES central",     "pfmt_1_nom",       shift(baseline_2j,'nom'    )),
##             ("JES up",          "pfmt_1_jesUp",     shift(baseline_2j,'jesUp'  )),
##             ("JES down",        "pfmt_1_jesDown",   shift(baseline_2j,'jesDown')),  ]),
##         ( "baseline, >=2 jets: JER",("jpt_1",70,-10,340),[
##             ("nominal",         "jpt_1",                  baseline_2j           ),
##             ("JES central",     "jpt_1_nom",        shift(baseline_2j,'nom'    )),
##             ("JER up",          "jpt_1_jerUp",      shift(baseline_2j,'jerUp'  )),
##             ("JER down",        "jpt_1_jerDown",    shift(baseline_2j,'jerDown')),  ]),
##         ( "baseline, >=2 jets: JES",("jpt_1",70,-10,340),[
##             ("nominal",         "jpt_1",                  baseline_2j           ),
##             ("JES nominal",     "jpt_1_nom",        shift(baseline_2j,'nom'    )),
##             ("JES up",          "jpt_1_jesUp",      shift(baseline_2j,'jesUp'  )),
##             ("JES down",        "jpt_1_jesDown",    shift(baseline_2j,'jesDown')),  ]),
##         ( "baseline: JES",("jpt_1_forward2p4",70,-10,340),[
##             ("nominal",         "jpt_1",            shift("%s && %s"%(baseline_2j,"abs(jeta_1)>2.4")           ),
##             ("JES central",     "jpt_1_nom",              "%s && %s"%(baseline_2j,"abs(jeta_1)>2.4"),'nom'    )),
##             ("JES up",          "jpt_1_jesUp",      shift("%s && %s"%(baseline_2j,"abs(jeta_1)>2.4"),'jesUp'  )),
##             ("JES down",        "jpt_1_jesDown",    shift("%s && %s"%(baseline_2j,"abs(jeta_1)>2.4"),'jesDown')),
##             ]),
##         ( "category 1: JES",("met",62,-10,300),[
##             ("nominal",         "met",                    category1           ),
##             ("JES central",     "met",              shift(category1,'nom'    )),
##             ("JES up",          "met_jesUp",        shift(category1,'jesUp'  )),
##             ("JES down",        "met_jesDown",      shift(category1,'jesDown')),  ]),
##         ( "category 2: JES",("met",62,-10,300),[
##             ("nominal",         "met",                    category2           ),
##             ("JES central",     "met",              shift(category2,'nom'    )),
##             ("JES up",          "met_jesUp",        shift(category2,'jesUp'  )),
##             ("JES down",        "met_jesDown",      shift(category2,'jesDown')),  ]),
##         ( "category 1: JES",("pfmt_1",62,-10,300),[
##             ("nominal",         "pfmt_1",                 category1           ),
##             ("JES central",     "pfmt_1_nom",       shift(category1,'nom'    )),
##             ("JES up",          "pfmt_1_jerUp",     shift(category1,'jesUp'  )),
##             ("JES down",        "pfmt_1_jerDown",   shift(category1,'jesDown')),  ]),
##         ( "category 2: JES",("pfmt_1",62,-10,300),[
##             ("nominal",         "pfmt_1",                 category2           ),
##             ("JES central",     "pfmt_1_nom",       shift(category2,'nom'    )),
##             ("JES up",          "pfmt_1_jerUp",     shift(category2,'jesUp'  )),
##             ("JES down",        "pfmt_1_jerDown",   shift(category2,'jesDown')),  ]),
##         ( "category 1: JER",("met",62,-10,300),[
##             ("nominal",         "met",                    category1           ),
##             ("JES central",     "met",              shift(category1,'nom'    )),
##             ("JER up",          "met_jerUp",        shift(category1,'jerUp'  )),
##             ("JER down",        "met_jerDown",      shift(category1,'jerDown')),  ]),
##         ( "category 2: JER",("met",62,-10,300),[
##             ("nominal",         "met",                    category2           ),
##             ("JES central",     "met",              shift(category2,'nom'    )),
##             ("JER up",          "met_jerUp",        shift(category2,'jerUp'  )),
##             ("JER down",        "met_jerDown",      shift(category2,'jerDown')),  ]),
##         ( "category 1.2: JES",("m_sv",70,-10,340),[
##             ("nominal",                                   category12            ),
##             ("JES nominal",                         shift(category12, 'nom'    )),
##             ("JES up",                              shift(category12, 'jesUp'  )),
##             ("JES down",                            shift(category12, 'jesDown')),  ]),
##         ( "category 2.2: JES",("m_sv",70,-10,340),[
##             ("nominal",                                   category22            ),
##             ("JES nominal",                         shift(category22, 'nom'    )),
##             ("JES up",                              shift(category22, 'jesUp'  )),
##             ("JES down",                            shift(category22, 'jesDown')),  ]),
##         ( "category 1.2: UncEn",("m_sv",70,-10,340),[
##             ("nominal",                                   category12            ),
##             ("UncEn up",                            shift(category12, 'UncEnUp'  )),
##             ("UncEn down",                          shift(category12, 'UncEnDown')),  ]),
##         ( "category 2.2: UncEn",("m_sv",70,-10,340),[
##             ("nominal",                                   category22            ),
##             ("UncEn up",                            shift(category22, 'UncEnUp'  )),
##             ("UncEn down",                          shift(category22, 'UncEnDown')),  ]),
#        ( "tau MVA isolation ID",("m_vis",30,0,200),[
#            ("tight",            "iso_2==1 && dR_ll>0.5"             ),
#            ("loose",            "iso_2==1 && dR_ll>0.5"             ),  ]),
#    ]
#    
#    weight0     = "" #"weight*trigweight_or_1" #*ttptweight_runI/ttptweight"
#    samples     = [#("TT",  "TT_TuneCUETP8M1",               "ttbar",            831.76,  "ttptweight_runI/ttptweight"  ),
#                   ("WJ",  "WJetsToLNu",                     "W + jets",         50380.0 ),
#                   #("WJ",  "WJetsToLNu_TuneCUETP8M1",       "W + jets",         50380.0 ),
#                   #("WJ",  "W1JetsToLNu_TuneCUETP8M1",      "W + 1J",            9644.5 ),
#                   #("DY",  "DYJetsToLL_M-50_TuneCUETP8M1",  "Drell-Yan 50",      4954.0 ),
#                   #("DY",  "DY1JetsToLL_M-50_TuneCUETP8M1", "Drell-Yan 1J 50",   1012.5 ),
##                    ("VBF", "VBFHToTauTau_M125_13TeV_powheg_pythia8", "VBF 125",    10.0 ),
#    ]
#    channels            = ["mutau",] #"etau"]
#    doKS                = True and False
#    drawErrorbars       = True #and False
#    drawRatio           = True #and False
#    normalizeToHist0    = True and False
#    plot_label0         = "" #-350_JER"
#    relaxed             = "" #"_cut_relaxed"
#    MORIOND_DIR         = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
#    mylabel             = "_2017_V2"
#    
#    for sampleinfo in samples:
#        
#        (subdir, sample, samplename, sigma) = ("", "", "", 0)
#        weight = weight0
#        if len(sampleinfo) is 4:
#            (subdir,sample,samplename,sigma) = sampleinfo
#        else:
#            (subdir,sample,samplename,sigma,extraweight) = sampleinfo
#            weight += '*'+extraweight
#        
#        filename    = "%s/%s/TauTauAnalysis.%s%s.root" % (MORIOND_DIR,subdir,sample,mylabel)
#        file        = TFile( filename )
#        plot_label = plot_label0
#        
#        for channel in channels:
#            
#            treename    = "tree_%s%s"%(channel,relaxed) #_cut
#            histNname   = "histogram_%s/cutflow_%s"%(channel,channel)
#            tree        = file.Get(treename)
#            histN       = file.Get(histNname)
#            
#            if not tree:  print error("shapes - did not find tree %s in %s"%(treename,filename))
#            if not histN: print error("shapes - did not find hist %s in %s"%(histNname,filename))
#            
#            N_tot       = histN.GetBinContent(8)
#            normscale   = sigma*lumi*1000/N_tot
#            if normalizeToHist0: plot_label += "_norm"
#            I0          = 0
#            print ">>> %s scale = %.3f" % (samplename,normscale)
#            
#            for cutsetname, var_info, cutset in cuts_sets:
#                print ">>> "
#                histu0      = None
#                hists       = [ ]
#                histus      = [ ] # unbinned
#                (var0,N,a,b) = var_info #(50,0.0,50)
#                
#                for i, cut in enumerate(cutset):
#                    
#                    cutname = ""
#                    var = var0
#                    if len(cut) is 2: (cutname,cut) = cut
#                    else:             (cutname,var,cut) = cut
#                    
#                    cut         = "(%s)*%s"%(cut,weight)
#                    histname    = "%s_%s_%d"%(samplename.replace(' ','').replace('+','-'),var,i)
#                    histnameu   = histname+"_unbinned"
#                    hist        = TH1F(histname,histname,N,a,b)
#                    histu       = None
#                    hist.Sumw2()
#                    out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
#                    if doKS:
#                        histu = TH1F(histnameu,histnameu,10000,a,b) # "unbinned" for KolmogorovTest
#                        histu.Sumw2()
#                        out   = tree.Draw("%s >> %s"%(var,histnameu),cut,"gOff")
#                    hist.Scale(normscale)
#                    hists.append(hist)
#                    histus.append(histu)
#                    I = hist.Integral(1,hist.GetNbinsX()) #+1
#                    E = hist.GetEntries()
#                    print ">>> %s (%d, %.1f):\n>>>   %s" % (histname,I,E,cut)
#                    
#                    if not I:
#                        print warning("shapes - %s has integral 0, ignoring"%histname)
#                        continue
#                    
#                    if i is 0:
#                        histu0 = histu
#                        I0 = I
#                    elif normalizeToHist0:
#                        hist.Scale(I0/I)
#                        if doKS: histu.Scale(I0/I)
#                    if not I0: print error("shapes - first histogram %s has integral 0, ignoring"%histname); exit(1)
#                    #entryname   = "%.1f - %s"%(I,cutname)
#                    entryname   = "%d - %s"%(E,cutname)
#                    
#                    if i is not 0 and doKS:
#                        KS = histu0.KolmogorovTest(histu)
#                        entryname = "%s (KS %.3f)"%(entryname,KS)
#                    
#                    print ">>>   entryname = %s"%(entryname)
#                    hist.SetTitle(entryname)
#                
#                if "Jets" in sample: subdir = sample[:sample.index("Jets")+1]
#                title      = "%s - %s: %s " % (subdir,channel,cutsetname.replace("category 1","1b1f").replace("category 2","1b1c"))
#                canvasname = makeFileName("%s/%s%s_%sshape_%s-%s.png" % (dirname,var0,plot_label,subdir,channel,cutsetname))
#                position   = "CenterRightTop" #"LeftTop"#"CenterLeftBottom" #"LeftTop"#
#                
#                comparison = Comparison(*hists)
#                comparison.Draw(title=title,xlabel=var0,position=position,KS=False,linestyle=False,ratio=drawRatio,
#                                                       errorbars=drawErrorbars,staterror=True,markers=False,markers_ratio=False)
#                comparison.saveAs(canvasname)
#                
#                for hist in histus:
#                    if hist: gDirectory.Delete(hist.GetName())
#        
#        file.Close()
#    
#
#
#
#
#def compareOldToNew():
#    print ">>>\n>>> compareOldToNew()"
#    
#    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM"
#    OLD_DIR      = "/scratch/ytakahas/SFrameAnalysis/AnalysisOutputEM"
#    
#    samples = [
#        ("WJ",          "WJ",           "WJetsToLNu_TuneCUETP8M1"           ),
#        ("TT",          "TT",           "TT_TuneCUETP8M1"                   ),
#        ("DY",          "DY",           "DYJetsToLL_M-50_TuneCUETP8M1"      ),
#        #("DY",          "DY1",          "DY1JetsToLL_M-50_TuneCUETP8M1"     ),
#        #("SingleMuon",  "SingleMuon",   "SingleMuon_Run2016"                ),
#        ("MuonEG",      "MuonEG",       "MuonEG_Run2016"                    ),e
#    ]
#    
#    treename = "tree_emu"
#    oldlabel = "OLD"
#    newlabel = "Moriond"
#    norm     = True
#    
#    for sampledir,samplelabel,sample in samples:
#        print ">>>\n>>> comparison %s-%s for \"%s\"" % (oldlabel,newlabel,sample)
#        
#        file1 = TFile( "%s/%s/TauTauAnalysis.%s_%s.root" % (OLD_DIR,    sampledir,sample,"Moriond"))
#        file2 = TFile( "%s/%s/TauTauAnalysis.%s_%s.root" % (MORIOND_DIR,sampledir,sample,"Moriond"))
#        tree1 = file1.Get(treename)
#        tree2 = file2.Get(treename)
#        
#        nocuts      = "channel>0"
#        vetos       = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
#        vetos_emu   = "extraelec_veto == 0 && extramuon_veto == 0"
#        isocuts     = "iso_1<0.15 && iso_2 == 1"
#        isocuts_emu = "iso_1<0.20 && iso_2<0.15"
#        baseline    = "channel>0 && %s && %s && q_1*q_2<0" % (vetos_emu, isocuts_emu)
#        weight      = ""
#        
#        cuts        = [
#            ("no cuts",   nocuts   ),
#            ("baseline",  baseline ),
#                      ]
#        
#        for cutname, cut in cuts:
#            print ">>> selections: %s"     % (cutname)
#            print ">>>             \"%s\"" % (cut)
#            
#            oldcut = cut
#            newcut = cut #" && ".join([cut,"triggers==1 && pt_1>23"])
#            print ">>>   %10s: entries: %d" % (oldlabel,tree1.GetEntries(cut))
#            print ">>>   %10s: entries: %d" % (newlabel,tree2.GetEntries(cut))
#            
#            vars = [
##                 ( "pfmt_1",                              80,      0, 200 ),
##                 ( "dilepton_veto",                        2,      0, 2.0 ),
##                 ( "extraelec_veto",                       2,      0, 2.0 ),
##                 ( "extramuon_veto",                       2,      0, 2.0 ),
##                 ( "lepton_vetos",                         2,      0, 2.0 ),
##                 ( "againstElectronVLooseMVA6_2",          2,      0, 2.0 ),
##                 ( "againstMuonTight3_2",                  2,      0, 2.0 ),
##                 ( "lepton_vetos",                         2,      0, 2.0 ),
##                 ( "iso_1",                               50,      0, 0.3 ),
##                 ( "iso_2",                               50,      0, 0.3 ),
##                 ( "pt_1",                               100,      0, 100 ),
##                 ( "pt_2",                               100,      0, 100 ),
#                ( "q_1",                                  5,     -2,   3 ),
#                ( "q_2",                                  5,     -2,   3 ),
##                 ( "abs(eta_1)",                          50,      0, 2.5 ),
##                 ( "abs(eta_2)",                          50,      0, 2.5 ),
##                 ( "q_1",                                100,       -4, 4 ),
##                 ( "q_2",                                100,       -4, 4 ),
#            ]
#            weightvars = [
#                ( "weight",                             100,   -0.2, 1.5 ),
#                (("weight",     "weight*trigweight_1"), 100,   -0.2, 1.5 ),
#                ( "trigweight_1",                       100,   -0.2, 1.5 ),
#                (("trigweight_1_or","trigweight_or_1"), 100, -0.2, 1.5 ),
#                ( "trigweight_2",                       100,   -0.2, 1.5 ),
#                ( "idisoweight_1",                      100,   -0.2, 1.5 ),
#                ( "idisoweight_2",                      100,   -0.2, 1.5 ),
#                ( "puweight",                           100,   -0.2, 1.5 ),
#                ( "weightbtag",                         100,   -0.2, 1.5 ),
#                ( "ttptweight",                         100,   -0.2, 1.5 ),
#            ]
#            #vars = weightvars
#            
#            for (var,N,a,b) in vars:
#                #print ">>> comparison \"%s\" with \"%s\"" % (var,cut)
#            
#                if isinstance(var,tuple): oldvar, newvar = var
#                else:                     oldvar, newvar = var, var
#                
#                oldname = "%s_old"%(oldvar.replace('(','').replace(')',''))
#                newname = "%s_new"%(newvar.replace('(','').replace(')',''))
#            
#                hist1 = TH1F(oldname, oldname, N, a, b)
#                hist2 = TH1F(newname, newname, N, a, b)
#                tree1.Draw("%s >> %s"%(oldvar,oldname),oldcut,"gOff")
#                tree2.Draw("%s >> %s"%(newvar,newname),newcut,"gOff")
#                N1 = hist1.Integral()
#                N2 = hist2.Integral()
#                if norm:
#                    hist1.Scale(1/N1)
#                    hist2.Scale(1/N2)
#                
#                canvas = TCanvas("canvas","canvas",100,100,800,600)
#                canvas.SetBottomMargin(0.12)
#                canvas.SetRightMargin(0.05)
#                canvas.SetLeftMargin(0.12)
#                canvas.SetTopMargin(0.05)
#                
#                hist1.SetLineWidth(3)
#                hist1.SetLineStyle(1)
#                hist1.SetLineColor(kAzure+4)
#                hist2.SetLineWidth(3)
#                hist2.SetLineStyle(2)
#                hist2.SetLineColor(kRed+3)
#                hist1.Draw("hist")
#                hist2.Draw("histsame")
#                hist1.SetTitle("")
#                hist1.GetXaxis().SetTitle(newvar)
#                hist1.GetYaxis().SetTitle("A.U.")
#                hist1.GetXaxis().SetTitleSize(0.05)
#                hist1.GetYaxis().SetTitleSize(0.05)
#                hist1.GetXaxis().SetTitleOffset(1.00)
#                hist1.GetYaxis().SetTitleOffset(1.20)
#                hist1.GetXaxis().SetLabelSize(0.040)
#                hist1.GetYaxis().SetLabelSize(0.040)
#                hist1.GetYaxis().SetRangeUser(0,max(hist1.GetMaximum(),hist2.GetMaximum())*1.10)
#                
#                (x1,y1) = (0.65,0.90)
#                (w,h)   = (0.18,0.15)
#                (x2,y2) = (x1+w,y1-h)
#                legend = TLegend(x1,y1,x2,y2)
#                legend.SetHeader("%s - %s"%(samplelabel,cutname))
#                legend.AddEntry(hist1,"%s (%d)"%(oldlabel,hist1.GetEntries()), 'l')
#                legend.AddEntry(hist2,"%s (%d)"%(newlabel,hist2.GetEntries()), 'l')
#                legend.SetTextSize(0.040)
#                legend.SetTextFont(42)
#                legend.SetBorderSize(0)
#                legend.SetFillStyle(0)
#                legend.Draw()
#                gStyle.SetOptStat(0)
#                
#                canvas.SaveAs("%s/%s_%s_%s_%s-%s.png" % (OUT_DIR,newvar.replace('(','').replace(')','').replace('*','-'),cutname.replace(' ','_'),samplelabel,oldlabel,newlabel))
#                canvas.Close()
#                ROOT.gDirectory.Delete(hist1.GetName())
#                ROOT.gDirectory.Delete(hist2.GetName())
#            
#        file1.Close()
#        file2.Close()
#        
#    print ">>>"
#    
#
#
#
#
#def vertexDY():
#    print ">>>\n>>> vertexDY()"
#    
#    DIR  = "/shome/ineuteli/analysis/SFrameAnalysis_Moriond/TauTauResonances/"
#    file1 = TFile( DIR + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
#    file2 = TFile( DIR + "TauTauAnalysis.DYJets_M-50.UZH.root" )
#    
#    
#    histnames = [
#        "d0_lepton_tail", "dz_lepton_tail", "d0_lepton", "dz_lepton",
#        "pt_muon_ID", "pt_lepton", "pt_lepton_pt23",
#        "gen_match_1_pt23_eta2p4", "gen_match_1_d0_dz", "gen_match_1_baseline", "gen_match_2_baseline",
#        #"pt_Z", "pt_Z_baseline"
#    ]
#    
#    channel = "mutau"
#    
#    for histname in histnames:
#        print ">>>   %s" % (histname)
#        
#        hist1 = file1.Get("histogram_%s/%s" % (channel,histname))
#        hist2 = file2.Get("histogram_%s/%s" % (channel,histname))
#        N1 = hist1.GetEntries()
#        N2 = hist2.GetEntries()
#        hist1.Scale(1/N1)
#        hist2.Scale(1/N2)
#        max_bin = max(hist1.GetMaximum(),hist2.GetMaximum())
#        
#        if   "gen_match_1"  in histname: var = "gen_match_1"
#        elif "gen_match_2"  in histname: var = "gen_match_2"
#        elif "d0"           in histname: var = "lepton d0"
#        elif "dz"           in histname: var = "lepton dz"
#        elif "pt_Z"         in histname: var = "Z boson pt"
#        elif "pt_muon"      in histname: var = "muon pt"
#        elif "pt_lepton"    in histname: var = "muon pt"
#        else: var = histname
#        if "_baseline"      in histname: var += " (baseline selections)"
#        elif "_pt23_eta2p4" in histname: var += " (p_{T}>23 GeV, |#eta|<2.4)"
#        elif "_pt23"        in histname: var += " (p_{T}>23 GeV)"
#        elif "_d0_dz"       in histname: var += " (p_{T}, #eta, d0, dz cuts)"
#        elif "_muon_ID"     in histname: var += " (medium ID)"
#        
#        (x1,x2) = (0.50,0.90)
#        (y1,y2) = (0.60,0.80)
#        if "dz_lepton_tail" in histname:       (y1,y2) = (0.55,0.35)
#        if "gen_match_1_baseline" in histname: (x1,x2) = (0.68,0.95)
#        if "gen_match_2_baseline" in histname: (x1,x2) = (0.75,0.40)
#        
#        print ">>>     entries  hist1 = %.4f" % (N1)
#        print ">>>     entries  hist2 = %.4f" % (N2)
#        print ">>>     overflow hist1 = %.4f" % (hist1.GetBinContent(hist1.GetNbinsX()+1))
#        print ">>>     overflow hist2 = %.4f" % (hist2.GetBinContent(hist2.GetNbinsX()+1))
#        
#        canvas = TCanvas("canvas","canvas",100,100,800,600)
#        canvas.SetBottomMargin(0.12)
#        canvas.SetRightMargin(0.05)
#        canvas.SetLeftMargin(0.12)
#        canvas.SetTopMargin(0.05)
#        hist1.SetLineWidth(3)
#        hist1.SetLineStyle(1)
#        hist1.SetLineColor(kAzure+4)
#        hist2.SetLineWidth(3)
#        hist2.SetLineStyle(2)
#        hist2.SetLineColor(kRed+3)
#        hist1.Draw("Ehist")
#        hist2.Draw("Ehistsame")
#        hist1.SetTitle("")
#        hist1.GetXaxis().SetTitle(var)
#        hist1.GetYaxis().SetTitle("A.U.")
#        hist1.GetXaxis().SetTitleSize(0.06)
#        hist1.GetYaxis().SetTitleSize(0.06)
#        hist1.GetXaxis().SetTitleOffset(0.9)
#        hist1.GetXaxis().SetLabelSize(0.045)
#        hist1.GetYaxis().SetLabelSize(0.045)
#        hist1.SetMaximum(max_bin*1.08)
#        legend = TLegend(x1,y1,x2,y2)
#        legend.AddEntry(hist1,"DY 10-50", 'l')
#        legend.AddEntry(hist2,"DY 50", 'l')
#        legend.SetTextSize(0.045)
#        legend.SetBorderSize(0)
#        legend.SetFillStyle(0)
#        legend.Draw()
#        gStyle.SetOptStat(0)
#        canvas.SaveAs("%s/%s.png" % (OUT_DIR,histname))
#        canvas.Close()
#        ROOT.gDirectory.Delete(hist1.GetName())
#        ROOT.gDirectory.Delete(hist2.GetName())
#        
#    file1.Close()
#    file2.Close()
#
#
#
#def pileupProfiles():
#    print ">>>\n>>> pileupProfiles()"
#    
#    DIR         = "/shome/ineuteli/analysis/SFrameAnalysis_ltau2017/PileupReweightingTool/histograms/"
#    MORIOND_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_ltau2017/"
#    file1       = TFile( DIR + "Data_PileUp_2017_69200.root" )
#    file2       = TFile( DIR + "MC_PileUp_Winter17_PU25ns_V1.root" )
#    file4       = TFile( MORIOND_DIR + "TT/TauTauAnalysis.TT_TuneCUETP8M2T4_2017.root" )
#    
#    histnames   = [ "pileup" ]
#    histname    = histnames[0]
#    xlabel      = "number of pileup interactions"
#    
#    hist1       = file1.Get(histname)
#    hist2       = file2.Get(histname)
#    nBins, a, b = hist1.GetNbinsX(), hist1.GetXaxis().GetXmin(), hist1.GetXaxis().GetXmax()
#    hist3       = TH1D("ratio","ratio",nBins,a,b)
#    I1          = hist1.Integral()
#    I2          = hist2.Integral()
#    hist1.Scale(1./I1)
#    hist2.Scale(1./I2)
#    max_bin     = max(hist1.GetMaximum(),hist2.GetMaximum())
#    for i in xrange(0,nBins+1):
#        bin1, bin2 = hist1.GetBinContent(i), hist2.GetBinContent(i)
#        print ">>>   bin %3d - %9.4g = %9.3g / %9.3g"%(i,bin1/bin2 if bin2 else 0, bin1,bin2)
#        if bin2: hist3.SetBinContent(i,bin1/bin2)
#    #I3          = hist3.Integral()
#    #hist3.Scale(1./I3)
#    #print ">>>   weight integral before-after: %.5g -> %.2g"%(I3,hist3.Integral())
#    
#    width   = 0.40
#    height  = 0.12
#    (x1,y1) = (0.55,0.69)
#    (x2,y2) = (x1+width,y1+height)
#    
#    canvas = TCanvas("canvas","canvas",100,100,800,600)
#    canvas.SetBottomMargin(0.12)
#    canvas.SetRightMargin(0.05)
#    canvas.SetLeftMargin(0.12)
#    canvas.SetTopMargin(0.05)
#    hist1.SetLineWidth(3)
#    hist1.SetLineStyle(1)
#    hist1.SetLineColor(kAzure+4)
#    hist2.SetLineWidth(3)
#    hist2.SetLineStyle(1)
#    hist2.SetLineColor(kRed+3)
#    hist1.SetTitle("")
#    hist1.Draw("Ehist")
#    hist2.Draw("Ehistsame")
#    hist1.GetXaxis().SetTitle(xlabel)
#    hist1.GetYaxis().SetTitle("A.U.")
#    hist1.GetXaxis().SetTitleSize(0.06)
#    hist1.GetYaxis().SetTitleSize(0.06)
#    hist1.GetXaxis().SetTitleOffset(0.9)
#    hist1.GetXaxis().SetLabelSize(0.045)
#    hist1.GetYaxis().SetLabelSize(0.045)
#    hist1.SetMaximum(max_bin*1.08)
#    hist1.GetXaxis().SetRangeUser(0.0,80.0)
#    legend = TLegend(x1,y1,x2,y2)
#    legend.AddEntry(hist1,"2017 data (B-F)", 'le')
#    legend.AddEntry(hist2,"simulation", 'le')
#    legend.SetTextSize(0.045)
#    legend.SetBorderSize(0)
#    legend.SetFillStyle(0)
#    legend.Draw()
#    gStyle.SetOptStat(0)
#    canvas.SaveAs("%s/%s_data-MC.png" % (OUT_DIR,histname))
#    canvas.Close()
#    
#    canvas = TCanvas("canvas","canvas",100,100,800,600)
#    canvas.SetBottomMargin(0.12)
#    canvas.SetRightMargin(0.05)
#    canvas.SetLeftMargin(0.12)
#    canvas.SetTopMargin(0.05)
#    hist3.SetLineWidth(3)
#    hist3.SetLineStyle(1)
#    hist3.SetLineColor(kAzure+4)
#    hist3.SetLineWidth(2)
#    hist3.SetLineStyle(1)
#    hist3.SetLineColor(kRed+3)
#    hist3.SetTitle("")
#    hist3.Draw("HIST")
#    hist3.GetXaxis().SetTitle(xlabel)
#    hist3.GetYaxis().SetTitle("weight (data/MC)")
#    hist3.GetXaxis().SetTitleSize(0.06)
#    hist3.GetYaxis().SetTitleSize(0.06)
#    hist3.GetXaxis().SetTitleOffset(0.9)
#    hist3.GetYaxis().SetTitleOffset(0.95)
#    hist3.GetXaxis().SetLabelSize(0.045)
#    hist3.GetYaxis().SetLabelSize(0.045)
#    hist3.SetMaximum(hist3.GetMaximum()*1.08)
#    hist3.GetXaxis().SetRangeUser(0.0,80.0)
#    gStyle.SetOptStat(0)
#    canvas.SaveAs("%s/%s_weight.png" % (OUT_DIR,histname))
#    canvas.Close()
#    
#    tree  = file4.Get("tree_mutau")
#    hist4 = TH1F("puweight","puweight",100,0,200)
#    out   = tree.Draw("puweight >> puweight","","gOff")
#    I4    = hist4.Integral()
#    hist4.Scale(1./I4)
#    
#    canvas = TCanvas("canvas","canvas",100,100,800,600)
#    canvas.SetBottomMargin(0.12)
#    canvas.SetRightMargin(0.05)
#    canvas.SetLeftMargin(0.12)
#    canvas.SetTopMargin(0.05)
#    canvas.SetLogy()
#    hist4.SetLineWidth(3)
#    hist4.SetLineStyle(1)
#    hist4.SetLineColor(kAzure+4)
#    hist4.SetLineWidth(2)
#    hist4.SetLineStyle(1)
#    hist4.SetLineColor(kRed+3)
#    hist4.SetTitle("")
#    hist4.Draw("HIST")
#    hist4.GetXaxis().SetTitle("pileup weight")
#    hist4.GetYaxis().SetTitle("A.U.")
#    hist4.GetXaxis().SetTitleSize(0.06)
#    hist4.GetYaxis().SetTitleSize(0.06)
#    hist4.GetXaxis().SetTitleOffset(0.9)
#    hist4.GetYaxis().SetTitleOffset(0.99)
#    hist4.GetXaxis().SetLabelSize(0.045)
#    hist4.GetYaxis().SetLabelSize(0.045)
#    #hist4.SetMaximum(hist3.GetMaximum()*4)
#    hist4.GetXaxis().SetRangeUser(0.0,200.0)
#    gStyle.SetOptStat(0)
#    canvas.SaveAs("%s/puweight_TT.png"%(OUT_DIR))
#    canvas.Close()
#    
#    ROOT.gDirectory.Delete(hist1.GetName())
#    ROOT.gDirectory.Delete(hist2.GetName())
#    file1.Close()
#    file2.Close()
#    file4.Close()
#
#
#
#
#def zptweight():
#    print ">>>\n>>> vertexDY()"
#    
#    DIR  = "/shome/ineuteli/analysis/SFrameAnalysis_Moriond/RecoilCorrections/data/"
#    file1 = TFile( DIR + "Zpt_weights.root" )
#    file2 = TFile( DIR + "Zpt_weights_2016_BtoH.root" )
#    
#    histname = "zptmass_histo"
#    hist1 = file1.Get(histname)
#    hist2 = file2.Get(histname)
#    var = histname
#
#    for hist, period in [(hist1,"ICHEP"),(hist2,"Moriond")]:
#
#
#        print ">>>   %s - %s" % (histname, period)
#        canvas = TCanvas("canvas","canvas",100,100,800,600)
#        canvas.SetBottomMargin(0.12)
#        canvas.SetRightMargin(0.10)
#        canvas.SetLeftMargin(0.12)
#        canvas.SetTopMargin(0.05)
#        hist.Draw("colz")
#        hist.SetTitle("")
#        hist.GetZaxis().SetRangeUser(0.75,2.0)
#        hist.GetXaxis().SetRangeUser(0,100)
#        hist.GetYaxis().SetRangeUser(0,200)
#        hist.GetXaxis().SetTitle("Z mass")
#        hist.GetYaxis().SetTitle("Z pt")
#        hist.GetXaxis().SetTitleSize(0.06)
#        hist.GetYaxis().SetTitleSize(0.06)
#        hist.GetXaxis().SetTitleOffset(0.9)
#        hist.GetXaxis().SetLabelSize(0.045)
#        hist.GetYaxis().SetLabelSize(0.045)
#        gStyle.SetOptStat(0)
#        canvas.SaveAs("%s/%s_%s.png" % (OUT_DIR,histname,period))
#        canvas.Close()
#        
#    file1.Close()
#    file2.Close()
#    
#
#
#
#
#def trigweight():
#    """Compare shapes of different files."""
#    print ">>>\n>>> trigweight()"
#    
#    channel  = "mutau"
#    treename = "tree_%s" % channel
#    vars     = [("trigweight_1","trigger weight",100,0,3), ("trigweight_1","trigger weight",100,0,3)]
#    samples  = [
#        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50" ),
#        ("DY",  "DYJetsToLL_M-50_TuneCUETP8M1", "DY M-50" ),
#    ]
#    cuts = [
#        ("no cuts",  "channel>0"),
#        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
#    ]
#    
#    for var, varnam, N,a,b in vars:
#        for cutname, cut in cuts:
#            for sampledir, samplename, samplelabel in samples:
#                
#                file = TFile("%s/%s/TauTauAnalysis.%s_Moriond.root"%(MORIOND_DIR,sampledir,samplename))
#                tree = file.Get(treename)
#        
#                hist1 = TH1F("hist1", "%s_L"%var, N, a, b)
#                hist2 = TH1F("hist2", "%s_X"%var, N, a, b)
#                hist3 = TH1F("hist3", "%s_B"%var, N, a, b)
#                
#                tree.Draw("%s >> hist1"%(var),"%s && triggers==1 && pt_1>23"%(cut),"gOff")
#                tree.Draw("%s >> hist2"%(var),"%s && triggers==2"%(cut),"gOff")
#                tree.Draw("%s >> hist3"%(var),"%s && triggers==3 && pt_1>23"%(cut),"gOff")
#                
#                maxs = [ ] 
#                for hist in [hist1,hist2,hist3]:
#                    I = hist.Integral()
#                    print ">>>   %s has %d entries" % (hist.GetName(),I)
#                    if I:
#                        hist.Scale(1./I)
#                        maxs.append(hist.GetMaximum())
#                
#                print ">>>   %s - %s" % (samplelabel,var)
#                canvas = TCanvas("canvas","canvas",100,100,800,600)
#                canvas.SetBottomMargin(0.12)
#                canvas.SetRightMargin(0.05)
#                canvas.SetLeftMargin(0.12)
#                canvas.SetTopMargin(0.05)
#                hist1.SetLineWidth(3)
#                hist1.SetLineStyle(1)
#                hist1.SetLineColor(kAzure+4)
#                hist2.SetLineWidth(3)
#                hist2.SetLineStyle(2)
#                hist2.SetLineColor(kRed+3)
#                hist3.SetLineWidth(3)
#                hist3.SetLineStyle(3)
#                hist3.SetLineColor(kGreen+3)
#                hist1.Draw("hist")
#                hist2.Draw("histsame")
#                hist3.Draw("histsame")
#                hist1.SetTitle("")
#                
#                xlabel = varname
#                if "trigweight_1" in var: xlabel="new trigger weight"
#                if "trigweight_2" in var: xlabel="old trigger weight"
#                hist1.GetXaxis().SetTitle(xlabel)
#                hist1.GetYaxis().SetTitle("A.U.")
#                hist1.GetXaxis().SetTitleSize(0.06)
#                hist1.GetYaxis().SetTitleSize(0.06)
#                hist1.GetXaxis().SetTitleOffset(0.9)
#                hist1.GetYaxis().SetTitleOffset(0.9)
#                hist1.GetXaxis().SetLabelSize(0.045)
#                hist1.GetYaxis().SetLabelSize(0.045)
#                hist1.GetYaxis().SetRangeUser(0,max(maxs)*1.08)
#                
#                (x1,y1) = (0.57,0.88)
#                (w,h)   = (0.18,0.24)
#                (x2,y2) = (x1+w,y1-h)
#                legend = TLegend(x1,y1,x2,y2)
#                legend.SetHeader("%s: %s"%(samplelabel,cutname))
#                legend.AddEntry(hist1," L && !X && pt_1>23", 'l')
#                legend.AddEntry(hist2,"!L &&  X", 'l')
#                legend.AddEntry(hist3," L &&  X", 'l')
#                legend.SetTextFont(42)
#                legend.SetTextSize(0.045)
#                legend.SetBorderSize(0)
#                legend.SetFillStyle(0)
#                legend.Draw()
#                
#                gStyle.SetOptStat(0)
#                filename = ("%s/%s_%s_%s.png"%(OUT_DIR,var,samplelabel,cutname)).replace(' ','_')
#                canvas.SaveAs(filename)
#                canvas.Close()
#                ROOT.gDirectory.Delete(hist1.GetName())
#                ROOT.gDirectory.Delete(hist2.GetName())
#                ROOT.gDirectory.Delete(hist3.GetName())
#                
#                file.Close()
#
#
#
#
#def triggers():
#    print ">>>\n>>> triggers()"
#    
#    channel  = "mutau"
#    treename = "tree_%s" % channel
#    var      = "triggers"
#    samples  = [
#        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50" ),
#        ("DY",  "DYJetsToLL_M-50_TuneCUETP8M1", "DY M-50" ),
#    ]
#    cuts = [
#        ("no cuts",  "channel>0"),
#        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),             
#    ]
#    (N,a,b)  = (3,1,4)
#    
#    for cutname, cut in cuts:
#        for sampledir, samplename, samplelabel in samples:
#            
#            file = TFile("%s/%s/TauTauAnalysis.%s_Moriond.root"%(MORIOND_DIR,sampledir,samplename))
#            tree = file.Get(treename)
#            
#            hist1 = TH1F("hist1", "triggers", N, a, b)            
#            tree.Draw("%s >> hist1"%(var),cut,"gOff")
#            
#            maxs = [ ] 
#            I = hist1.Integral()
#            print ">>>   %s has %d entries" % (hist1.GetName(),I)
#            if I:
#                hist1.Scale(1./I)
#                maxs.append(hist1.GetMaximum())
#            
#            print ">>>   %s - %s" % (samplelabel,var)
#            canvas = TCanvas("canvas","canvas",100,100,800,600)
#            canvas.SetBottomMargin(0.12)
#            canvas.SetRightMargin(0.05)
#            canvas.SetLeftMargin(0.12)
#            canvas.SetTopMargin(0.05)
#            hist1.SetLineWidth(3)
#            hist1.SetLineStyle(1)
#            hist1.SetLineColor(kAzure+4)
#            hist1.Draw("hist")
#            #hist1.SetTitle("%s: %s"%(samplelabel,cutname))
#            
#            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(1),"L && !X")
#            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(2),"!L && X")
#            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(3),"L && X")
#            
#            #hist1.GetXaxis().SetTitle("trigger weight")
#            hist1.GetYaxis().SetTitle("A.U.")
#            hist1.GetXaxis().SetTitleSize(0.06)
#            hist1.GetYaxis().SetTitleSize(0.06)
#            hist1.GetXaxis().SetTitleOffset(0.9)
#            hist1.GetYaxis().SetTitleOffset(0.9)
#            hist1.GetXaxis().SetLabelSize(0.080)
#            hist1.GetYaxis().SetLabelSize(0.045)
#            hist1.GetYaxis().SetRangeUser(0,max(maxs)*1.08)
#            
#            # title = "%s: %s"%(samplelabel,cutname)
#            # (x1,y1) = (0.48,0.88)
#            # (w,h)   = (0.18,0.24)
#            # (x2,y2) = (x1+w,y1-h)
#            # legend = TLegend(x1,y1,x2,y2)
#            # legend.SetHeader(title)
#            # legend.SetTextFont(42)
#            # legend.SetTextSize(0.045)
#            # legend.SetBorderSize(0)
#            # legend.SetFillStyle(0)
#            # legend.Draw()
#    
#            gStyle.SetOptStat(0)
#            filename = ("%s/%s_%s_%s.png"%(OUT_DIR,var,samplelabel,cutname)).replace(' ','_')
#            canvas.SaveAs(filename)
#            canvas.Close()
#            ROOT.gDirectory.Delete(hist1.GetName())
#            
#            file.Close()
#        
#
#
#def ratioTest():
#    
#    pads = []
#    canvas = makeCanvas(ratio=True,pads=pads)
#    hist1 = TH1F("hist1","hist1",50,0,100)
#    hist2 = TH1F("hist2","hist2",50,0,100)
#    
#    for i in xrange(10000):
#        hist1.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
#        hist2.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
#    stats = makeStatisticalError(hist2)
#    ratio = makeRatio(hist1,hist2)
#    
#    pads[0].cd()
#    hist1.Draw("E")
#    hist2.Draw("HIST SAME")
#    stats.Draw("E2 SAME")
#    
#    pads[1].cd()
#    ratio.Draw("SAME")
#    
#    canvas.SaveAs("ratio_test.png")
#    
#
#
#def ratioTest2():
#    
#    hist1  = TH1F("hist1","hist1",50,0,100)
#    hist2  = TH1F("hist2","hist2",50,0,100)
#    hist3  = TH1F("hist3","hist3",50,0,100)
#    
#    hist1u = TH1F("hist1u","hist1u",10000,-50,150)
#    hist2u = TH1F("hist2u","hist2u",10000,-50,150)
#    hist3u = TH1F("hist3u","hist3u",10000,-50,150)
#    
#    for i in xrange(10000):
#        r = gRandom.Gaus(50,20)
#        w = gRandom.Gaus(1,0.1)
#        hist1.Fill(r,w)
#        hist1u.Fill(r,w)
#    for i in xrange(10000):
#        r = gRandom.Gaus(50,22)
#        w = gRandom.Gaus(0.99,0.1)
#        hist2.Fill(r,w)
#        hist2u.Fill(r,w)
#    for i in xrange(10000):
#        r = gRandom.Gaus(51,20)
#        w = gRandom.Gaus(1,0.2)
#        hist3.Fill(r,w)
#        hist3u.Fill(r,w)
#        
#    entries = ["1: nominal","2: other gaussian","3: another gaussian"]
#    for i,histu in enumerate([hist2u,hist3u],1):
#        Dn = hist1u.KolmogorovTest(histu)
#        print ">>> KolmogorovTest: Dn=%.3f for %s with %s" % (Dn,hist1u.GetName(),histu.GetName())
#        entries[i] = "%s (KS %.2f)" % (entries[i],Dn)
#    # for i,hist in enumerate([hist2,hist3],1):
#    #     Dn = hist1.KolmogorovTest(hist)
#    #     print ">>> KolmogorovTest: Dn=%.3f for %s with %s" % (Dn,hist1.GetName(),hist.GetName())
#    
#    comparison = Comparison(hist1,hist2,hist3)
#    comparison.Draw(title="comparing gaussians",entries=entries,markers=False,markers_ratio=False,KS=False)
#    comparison.saveAs("ratio_test3.png")
#    
#    
#
#def writeCutTreeToFile(oldfilename,oldtreename,newfilename,newtreename,cut,overwrite=True,newdirname=""):
#    """Write a tree to a file. Overwrite the tree by default, If the tree already exist."""
#    
#    newfile = TFile(newfilename,"UPDATE")
#    oldfile = TFile(oldfilename,"READ")
#    newtree = newfile.Get(newtreename)
#    if overwrite or not newtree:
#        
#        if newdirname: # go to directory, and create it if it does not exist
#            newdir = newfile.GetDirectory(newdirname)
#            if not newdir:
#                print ">>> created directory %s"%(newdirname)
#                newdir = newfile.mkdir(newdirname)
#            newdir.cd()
#        
#        oldtree = oldfile.Get(oldtreename)
#        newtree = oldtree.CopyTree(cut)
#        newtree.Write(newtreename,TTree.kOverwrite)
#    oldfile.Close()
#    newfile.Close()
    


def main():
    
    # MAKE SAMPLES
    #global samples
    #    
    ## USER OPTIONS
    #channel = "mutau"
    #ensureDirectory(OUT_DIR)
    #
    #treename = "tree_%s" % channel
    #if useCutTree and "emu" not in channel:
    #  treename = "tree_%s_cut_relaxed" % channel
    #samples.setChannel(channel)
    
    ## RENORMALIZE WJ
    #print ">>> "
    #if normalizeWJ and channel!="emu":
    #    selectionWJ = selection.selection.replace(' && pfmt_1<100',"")
    #    LOG.header("%s: WJ renormalization" % (channel))
    #    samples.renormalizeWJ("pfmt_1", 200, 80, 200, selectionWJ, QCD=doQCD, reset=True, verbosity=verbosityWJ)
    #else: LOG.warning("Not WJ renormalized! (normalizeWJ=%s, user flag=%s, channel=%s)" % (normalizeWJ,args.noWJrenorm,channel))
    #print ">>> "
    
    # MAKE ALTERNATIVE SAMPLES
    samples2B = [
#       ("DY", "DYJetsToLL_M-50_TuneCP5",           "Drell-Yan 50",        4954.0 ), # LO 4954.0; NLO 5765.4
#       ("DY", "DY1JetsToLL_M-50_TuneCP5",          "Drell-Yan 1J 50",     1012.5 ),
#       ("DY", "DY2JetsToLL_M-50_TuneCP5",          "Drell-Yan 2J 50",      332.8 ),
#       ("DY", "DY3JetsToLL_M-50_TuneCP5",          "Drell-Yan 3J 50",      101.8 ),
      ("DY", "DYJetsToLL_M-10to50_TuneCUETP8M1",  "Drell-Yan 10-50",    18610.0 ),
      ("DY", "DY1JetsToLL_M-10to50_TuneCUETP8M1", "Drell-Yan 1J 10-50",   421.5 ),
      ("DY", "DY2JetsToLL_M-10to50_TuneCUETP8M1", "Drell-Yan 2J 10-50",   184.3 ),
      ("DY", "DY3JetsToLL_M-10to50_TuneCUETP8M1", "Drell-Yan 3J 10-50",    95.0 ),
      ("DY", "DYJetsToLL_M-50_TuneCUETP8M1",      "Drell-Yan 50",        4954.0 ),
      ("DY", "DY1JetsToLL_M-50_TuneCUETP8M1",     "Drell-Yan 1J 50",     1012.5 ),
      ("DY", "DY2JetsToLL_M-50_TuneCUETP8M1",     "Drell-Yan 2J 50",      332.8 ),
      ("DY", "DY3JetsToLL_M-50_TuneCUETP8M1",     "Drell-Yan 3J 50",      101.8 ),
      ("DY", "DY4JetsToLL_M-50_TuneCUETP8M1",     "Drell-Yan 4J 50",       54.8 ),
    ]
    samples2S = [ ]
    samples2D = {
#         'mutau' : ( "SingleMuon", "SingleMuon_Run2017", "observed" ),
#         'mumu'  : ( "SingleMuon", "SingleMuon_Run2017", "observed" ),
    }
#     makeSFrameSamples(samples2D,samples2B,samples2S,weight=_weight,binN_weighted=10,cycle="DiMuonAnalysis",tag=globalTag+"_noRC")
#     makeSFrameSamples(samples2D,samples2B,samples2S,weight=_weight,binN_weighted=10,cycle="TauTauAnalysis",tag=globalTag+"_RC")
    makeSFrameSamples(samples2D,samples2B,samples2S,weight=_weight,binN_weighted=8,cycle="TauTauAnalysis",tag=globalTag+"_newZpt")
#     samples2 = SampleSet(samples2D,samples2B,samples2S,channel="mumu")
    samples2 = SampleSet(samples2D,samples2B,samples2S,channel="mutau")
    samples2.printTable()
    samples2.stitch("DY*J*M-50",     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan" )
    samples2.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
    samples2.merge( 'DY',                             name="DY",          title="Drell-Yan"             )

    
    # MAIN ROUTINES
#     purity(samples)
#     TTSFs(samples)
#     plotHist2D(samples)
#     compareSelectionsForSFrameSample(samples)
#     compareSFrameSamples(samples,samples2)
    compareSFrameSamples(samples2,samples)
    
    #plotSampleShapes(samples,channel,DIR=OUT_DIR)
    #plotStacks(samples,channel,DIR=OUT_DIR)
    #compareSFrameHistograms()
    #compareSFrameHistogram()
    #compareSFrameHistogram2D()
    #quicktest()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




