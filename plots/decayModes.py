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
plottag    = ""
mergeTop, splitTT, splitDY, splitDYbyDM = True, False, False, False
loadSettings(globals(),settings,verbose=args.verbose)
exec commands

OUT_DIR = "decayModes"
gROOT.Macro('%s/compressDecayModes.C+'%OUT_DIR)


# TODO:
#  1) plot fractions as a scan of mass, ...
#  2) make mass plots split by gen/reco decay mode
#  3) make pie chart
#  


# SELECTIONS
isocutsOldv1  = "iso_1<0.15 && iso_2==1"
isocutsOldv2  = "iso_1<0.15 && byTightIsolationMVArun2v2DBoldDMwLT_2==1"
isocutsNew    = "iso_1<0.15 && byTightIsolationMVArun2v1DBnewDMwLT_2==1"
vetos         = "lepton_vetos==0"
baselineOldv1 = "channel>0 && %s && %s && q_1*q_2<0 && decayMode_2<11"%(isocutsOldv1,vetos)
baselineOldv2 = "channel>0 && %s && %s && q_1*q_2<0 && decayMode_2<11"%(isocutsOldv2,vetos)
baselineNew   = "channel>0 && %s && %s && q_1*q_2<0"%(isocutsNew,vetos)
selections    = [
  sel("oldDMv1, m_T<50",  "%s && %s"%(baselineOldv1,"pfmt_1<50")),
#   sel("oldDMv2, m_T<50",  "%s && %s"%(baselineOldv2,"pfmt_1<50")),
#   sel("newDM, m_T<50",    "%s && %s"%(baselineNew,  "pfmt_1<50")),
]

# DECAY MODES
DM_dict = {
  'DM0':  "h^{#pm}",                    'DM1':  "h^{#pm}h^{0}",               'DM2':  "h^{#pm} #geq2h^{0}",
  'DM10': "h^{#pm}h^{#mp}h^{#pm}",      'DM11': "h^{#pm}h^{#mp}h^{#pm}h^{0}", 'DM12': "h^{#pm}h^{#mp}h^{#pm} #geq2h^{0}",
  'LTF': "l #rightarrow #tau_{h} fake", 'JTF': "j #rightarrow #tau_{h} fake"
}
splitByGM = [('ZTT',"Z -> tau_{mu}tau_{h}","gen_match_2==5"),  ('ZL',"Drell-Yan with l -> tau_{h}","gen_match_2!=5")] if doFakeRate else\
            [('ZTT',"Z -> tau_{mu}tau_{h}","gen_match_2==5"),  ('ZJ',"Drell-Yan other",            "gen_match_2!=5")]
splitByRecoDM = [
   ('ZTT_DM0',     "Z -> tau_{mu}tau_{h}: DM0",   "gen_match_2==5 && decayMode_2==0"     ),
   ('ZTT_DM1',     "Z -> tau_{mu}tau_{h}: DM1",   "gen_match_2==5 && decayMode_2==1"     ),
   ('ZTT_DM10',    "Z -> tau_{mu}tau_{h}: DM10",  "gen_match_2==5 && decayMode_2==10"    ),
   ('ZTT_DM11',    "Z -> tau_{mu}tau_{h}: DM11",  "gen_match_2==5 && decayMode_2==11"    ),
   ('ZL',          "Drell-Yan with l -> tau_{h}", "gen_match_2!=5"                       ),
]
splitByRecoDM_ZTTonly = splitByRecoDM[:4]
splitByRecoDM_ZJ = splitByRecoDM[:]
splitByRecoDM_ZJ.insert(-1,('ZJ', "Drell-Yan with j -> tau_{h}", "gen_match_2==5" ))
splitByGenDM = [
   ('ZTT_DM0',     "Z -> tau_{mu}tau_{h}: gen DM0",   "gen_match_2==5 && gen_decayMode_2==0" ),
   ('ZTT_DM1',     "Z -> tau_{mu}tau_{h}: gen DM1",   "gen_match_2==5 && gen_decayMode_2==1" ),
   #('ZTT_DM2',     "Z -> tau_{mu}tau_{h}: %s"%DM_dict['DM2'],
   #                                               "gen_match_2==5 && compressGenDM(gen_decayMode_2)==2"),
   ('ZTT_DM10',    "Z -> tau_{mu}tau_{h}: gen DM10",  "gen_match_2==5 && gen_decayMode_2==10"),
   ('ZTT_DM11',    "Z -> tau_{mu}tau_{h}: gen DM11",  "gen_match_2==5 && gen_decayMode_2==11"),
   #('ZTT_DM12',    "Z -> tau_{mu}tau_{h}: %s"%DM_dict['DM12'],
   #                                               "gen_match_2==5 && compressGenDM(gen_decayMode_2)==5"),
   #('ZTT_DMother', "Z -> tau_{mu}tau_{h}: other", "gen_match_2==5 && gen_decayMode_2!=0 && gen_decayMode_2!=1 && gen_decayMode_2!=10 && gen_decayMode_2!=11"),
   ('ZTT_DMother', "Z -> tau_{mu}tau_{h}: other DMs", "gen_match_2==5 && gen_decayMode_2!=0 && gen_decayMode_2!=1 && gen_decayMode_2!=10 && gen_decayMode_2!=11"),
   ('ZL',          "Drell-Yan with l -> tau_{h}", "gen_match_2!=5"                       ),
] 
colorsDM = { 'LTF':  TColor.GetColor(100,182,232),   'JTF':  kGreen-6,    'ZTT':  kOrange-4,
             'DM0':  kOrange+5,                      'DM1':  kOrange-4,   'DM2':  kOrange+6,
             'DM10': kYellow-6,                      'DM11': kOrange-6,   'DM12': kOrange-8,
}
colors   = [ kBlack, kBlue, kRed, kGreen, kMagenta, kOrange, kTeal, kAzure+2, kYellow-3 ]


def plotDecayMode2D(channel,samples):
    """Plot gen vs. reco decay modes."""
    
    samplenames = [
      ("DY",   "Drell-Yan", "DY",                  ),
      #("ZTT",  "ZTT",       "DY", "gen_match_2==5" ),
    ]
    
    # SETTINGS
    tag       = ""
    outdir    = OUT_DIR
    ratio     = True
    norm      = True
    staterror = True
    JFR       = True
    exts      = ['png','pdf'] if args.pdf else ['png']
    
    for sampleinfo  in samplenames:
      samplename, sampletitle, searchterm = sampleinfo[:3]
      extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
      sample    = samples.get(searchterm,unique=True)
      
      for selection in selections:
        print green('reco vs. genDM with selection "%s"'%(selection.title),pre=">>>\n>>>   ")
        
        cuts     = combineCuts(selection.selection,extracuts)
        cutsDM   = cuts if "gen_match_2==5" in cuts else combineCuts(cuts,"gen_match_2==5")
        doFakes  = "gen_match_2" not in selection.selection
        
        genDMs   = [ 'DM0', 'DM1', 'DM2', 'DM10', 'DM11', 'DM12', ]
        if doFakes: genDMs += [ 'LTF', 'JTF', ]
        recoDMs  = [ 'DM0', 'DM1', 'DM10', 'DM11', ]
        nGenDMs  = len(genDMs)
        nRecoDMs = len(recoDMs)
        
        histGM  = sample.hist2D("decayMode_2",20,0,20,"gen_match_2",    10,0,10,cuts) if doFakes else None
        histDM  = sample.hist2D("decayMode_2",20,0,20,"gen_decayMode_2",30,0,30,cutsDM)
        #hist    = sample.hist2D("compressRecoDM(decayMode_2)",nRecoDMs,0,nRecoDMs,"compressGenDM(gen_decayMode_2,gen_match_2)",nGenDMs,0,nGenDMs,cutsDM)
        
        hist    = TH2F("hist","hist",4,0,4,nGenDMs,0,nGenDMs)
        
        # GET TOTAL EVENTS
        totGenDMs  = { }
        totRecoDMs = { }
        for key in genDMs:
          hist0 = histDM if 'DM' in key else histGM
          tot   = 0
          for ybin in getDMBin(key):
            ybin  = hist0.GetYaxis().FindBin(ybin)
            for xbin in range(0,hist0.GetXaxis().GetNbins()+2):
              tot += hist0.GetBinContent(xbin,ybin)
            totGenDMs[key] = tot
          print '>>> totGenDMs["%s"] = %5.1f'%(key,tot)
        for key in recoDMs:
          tot  = 0
          for xbin in getDMBin(key):
            xbin = histGM.GetXaxis().FindBin(xbin)
            for ybin in range(0,histGM.GetYaxis().GetNbins()+2):
              tot += histGM.GetBinContent(xbin,ybin)
          totRecoDMs[key] = tot
          print '>>> totRecoDMs["%s"] = %5.1f'%(key,tot)
        
        # SET LABELS
        for i, binkey in enumerate(genDMs):
          hist.GetYaxis().SetBinLabel(nGenDMs-i,DM_dict[binkey])
        for i, binkey in enumerate(recoDMs):
          hist.GetXaxis().SetBinLabel(i+1,DM_dict[binkey])
        
        # SET BIN CONTENT
        for xkey in recoDMs:
          for ykey in genDMs:
            #print ">>> %s, %s"%(xkey,ykey)
            hist0 = histDM if 'DM' in ykey else histGM
            binc = 0
            for xbin in getDMBin(xkey):
              xbin = hist0.GetXaxis().FindBin(xbin)
              for ybin in getDMBin(ykey):
                ybin = hist0.GetYaxis().FindBin(ybin)
                #print ">>>   add (%s,%s) = %5.1f"%(xbin,ybin,hist0.GetBinContent(xbin,ybin))
                binc += hist0.GetBinContent(xbin,ybin)
            hist.Fill(DM_dict[xkey],DM_dict[ykey],binc)
        
        # NORMALIZE
        histx = hist.Clone("recoNorm")
        histy = hist.Clone("genNorm")
        histx.SetTitle("fraction of reco decay mode [%]")
        histy.SetTitle("fraction of gen decay mode [%]")
        for xkey in recoDMs:
          xbin = hist.GetXaxis().FindBin(DM_dict[xkey])
          for ykey in genDMs:
            ybin = hist.GetYaxis().FindBin(DM_dict[ykey])
            binc = hist.GetBinContent(xbin,ybin)
            if binc:
              histx.SetBinContent(xbin,ybin,binc/totRecoDMs[xkey]*100.0)
              histy.SetBinContent(xbin,ybin,binc/totGenDMs[ykey]*100.0)
        
        for hist0 in [histx,histy]:
            # NAME
            filename = "%s/gen_vs_recoDM_%s_%s_%s%s.png"%(outdir,hist0.GetName(),samplename,selection.filename,tag)
            filename = makeFileName(filename)
        
            # TITLE
            xtitle     = "reconstructed decay mode"
            ytitle     = "generator decay mode"
            ztitle     = hist0.GetTitle()
            title      = [selection.title,sampletitle]
            text       = title
            position   = "" #"centerright"
            
            # TODO: out of frame text: sample, selections
            
            # PLOT
            plot = Plot2D(hist0)
            plot.plot(option="COLZTEXT",format='.1f',xtitle=xtitle,ytitle=ytitle,ztitle=ztitle,text=text,position='out',
                      textsize=0.040,markersize=2.0,ylabelsize=0.060,xlabelsize=0.066,xlabeloffset=0.005,zmax=100.0,
                      lmargin=0.23,rmargin=0.17,tmargin=0.065,yoffset=2.1,zoffset=1.10,width=860)
            plot.saveAs(filename,ext=exts)
            plot.close()
        
        close(hist,histGM,histDM)



def plotDecayModeDataMC(channel,samples):
    """Plot data-MC comparison for some variables and selection."""
    print ">>>\n>>> "+green("plotDecayModeDataMC()")
    
    outdir     = OUT_DIR
    tag        = "_splitByGenDM_dataMC"
    binlabelsR = [DM_dict[dm] for dm in ['DM0','DM1','DM10','DM11']]
    binlabelsG = [DM_dict[dm] for dm in ['DM0','DM1','DM2','DM10','DM11','DM12','LTF','JTF']]
    samples.split('DY',splitByGenDM)
    
    variables  = [
      var("compressRecoDM(decayMode_2)",
                     3,     0,   3,  filename="recoDecayMode", title="reconstructed decay mode", veto="decayMode_2==", position="toptoprightright",
                                     binlabels=binlabelsR, cbinning={'newDM':(4,0,4)}, ymargin=1.55, ncolumns=2 ),
#       var("m_2",    38,  0.20, 2.1,  title="tau mass", filename="m_tau", veto="decayMode_2==0", position='x=0.63', cposition={'decayMode_2==1(?![01])':'right','decayMode_2==11':'x=0.04'},
#                                      cbinning={'decayMode_2==1(?![01])':(36,0.20,2.0), 'decayMode_2==1[01]':(23,0.70,1.85)} ),
#       var("pt_2",   35,    10, 150, title="tau pt",  position="right" ),
#       var("m_vis",  40,     0, 200, ),
    ]
    
    selections1 = selections
    selections1 += [
      sel("oldDMv1, m_T<50, reco DM0",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==0" )),
      sel("oldDMv1, m_T<50, reco DM1",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==1" )),
      sel("oldDMv1, m_T<50, reco DM10", "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==10")),
#       sel("oldDMv2, m_T<50, reco DM0",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==0" )),
#       sel("oldDMv2, m_T<50, reco DM1",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==1" )),
#       sel("oldDMv2, m_T<50, reco DM10", "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==10")),
#       sel("newDM, m_T<50, reco DM0",    "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==0" )),
#       sel("newDM, m_T<50, reco DM1",    "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==1" )),
#       sel("newDM, m_T<50, reco DM10",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==10")),
#       sel("newDM, m_T<50, reco DM11",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==11")),
    ]
    
    # PLOT
    for selection in selections1:
      print '>>>\n>>>   plot with selection "%s"'%(selection.title)
      for variable in variables:
        if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
          print '>>>   plotDecayModeDataMC: ignoring %s for %s, tag "%s"'%(variable.printWithBinning(),selection,tag); continue
        variable.changeContext(selection.selection)
        plotVariable(samples,variable,selection,app=tag,textsize=0.038)
    


def plotGenDecayMode(channel,samples):
    """Plot stacked DY for some variables and selection."""
    print ">>>\n>>> "+green("plotGenDecayMode()")
    
    outdir     = OUT_DIR
    tag        = "_splitByRecoDM"
    binlabelsR = [DM_dict[dm] for dm in ['DM0','DM1','DM10','DM11']]
    binlabelsG = [DM_dict[dm] for dm in ['DM0','DM1','DM2','DM10','DM11','DM12','LTF','JTF']]
    
    # GET DY SAMPLESET
    samplesDY  = samples.clone("splitByGenDM",filter='DY')
    samplesDY.printTable('splitByGenDM')
    samplesDY.split('DY',splitByRecoDM_ZTTonly)
    
    variables  = [
      var("compressGenDM(gen_decayMode_2,gen_match_2)",
                   6,     0,   6,  filename="genDecayMode", title="generator decay mode",
                                   binlabels=binlabelsG[:6], ymargin=1.20 ),
    ]
    
    # PLOT
    for selection in selections:
      print green('plot with selection "%s"'%(selection.title),pre=">>>\n>>>   ")
      title = "DY, %s"%selection.title
      for variable in variables:
        if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
          print '>>>   plotGenDecayMode: ignoring %s for %s, tag "%s"'%(variable.printWithBinning(),selection,tag); continue
        variable.changeContext(selection.selection)
        plotVariable(samplesDY,variable,selection,app=tag,ratio=False,JFR=False,rightmargin=1.45,xtitleoffset=1.14,title=title)
    


def plotVariable(samples,variable,selection,**kwargs):
    """Plot stack for some variables and selection."""
    
    title        = kwargs.get('title',         selection.title  )
    text         = kwargs.get('text',          ""               )
    weight       = kwargs.get('weight',        ""               )
    append       = kwargs.get('app',           ""               )
    JFR          = kwargs.get('JFR',           True             )
    ratio        = kwargs.get('ratio',         True             )
    rightmargin  = kwargs.get('rightmargin',   1.               )
    textsize     = kwargs.get('textsize',      legendtextsize   )
    xtitleoffset = kwargs.get('xtitleoffset',  1.               )
    outdir       = OUT_DIR
    
    xtitle       = variable.title
    position     = variable.position
    logx         = variable.logx
    logy         = variable.logy
    ymargin      = variable.ymargin
    divideByBinSize = logx
    name         = "%s/%s_%s%s%s.png"%(outdir,variable.filename,selection.filename.replace('recoDM','DM'),append,plottag)
    exts         = ['png','pdf'] if args.pdf else ['png']
    
    plot = samples.plotStack(variable,selection,weight=weight,title=title,QCD=False,JFR=False, #UNSET!!!
                    divideByBinSize=divideByBinSize)
    plot.plot(xtitle=xtitle,xtitleoffset=xtitleoffset,logx=logx,logy=logy,ratio=ratio,staterror=True,position=position,textsize=textsize,text=text,
              ymargin=ymargin,rightmargin=rightmargin)
    plot.saveAs(name,ext=exts)
    plot.close()
    


def plotDecayModeFractions(channel,samples):
    """Plot scans of DM fractions."""
    print green("plotDecayModeFractions()",pre=">>>\n>>> ")
    
    outdir     = OUT_DIR
    tag        = "_splitByGenDM"
    exts       = ['png','pdf'] if args.pdf else ['png']
    doFakes    = True #and False
    genDMs     = [ 'DM0', 'DM1', 'DM2', 'DM10', 'DM11', 'DM12', ]
    if doFakes: genDMs += [ 'LTF', 'JTF', ]
    sampleDY   = samples.get('DY',unique=True)
    
    #decayModes = [ 'DM1', 'DM10', 'DM11',]
    
    selectionsDM = [
      ('DM0',  sel("oldDMv1, m_T<50, reco DM0",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==0")  )),
      ('DM1',  sel("oldDMv1, m_T<50, reco DM1",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==1")  )),
      ('DM10', sel("oldDMv1, m_T<50, reco DM10", "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==10") )),
      ('DM0',  sel("oldDMv2, m_T<50, reco DM0",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==0")  )),
      ('DM1',  sel("oldDMv2, m_T<50, reco DM1",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==1")  )),
      ('DM10', sel("oldDMv2, m_T<50, reco DM10", "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==10") )),
      ('DM0',  sel("newDM, m_T<50, reco DM0",    "%s && %s"%(baselineNew,"pfmt_1<50 && decayMode_2==0")    )),
      ('DM1',  sel("newDM, m_T<50, reco DM1",    "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==1")  )),
      ('DM10', sel("newDM, m_T<50, reco DM10",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==10") )),
      ('DM11', sel("newDM, m_T<50, reco DM11",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==11") )),
    ]
    
    variables  = [
      var("m_2",    18,  0.20, 2.0,  title="tau mass", filename="m_tau", veto="decayMode_2==0",
                                     cbinning={'decayMode_2==1(?![01])':(18,0.20,2.0), 'decayMode_2==1[01]':(11,0.70,1.8)} ),
      var("m_vis",  14,    40, 180, ),
    ]
    
    # PLOT
    for DM, selection in selectionsDM:
      print green('plot with selection "%s"'%(selection.title),pre=">>>\n>>>   ")
      for variable in variables:
        if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
          print '>>>   plotDecayModeFractions: ignoring %s for %s, tag "%s"'%(variable.printWithBinning(),selection,tag); continue
        variable.changeContext(selection.selection)
        
        hist0 = sampleDY.hist(variable,selection) # denominator
        graphs = [ ]
        for i, dm in enumerate(genDMs):
          cuts  = "compressGenDM(gen_decayMode_2,gen_match_2)==%s"%i
          hist  = sampleDY.hist(variable,selection,extracuts=cuts,append="_%d"%i)
          graph = TGraphAsymmErrors()
          graph.Divide(hist,hist0)
          setTGraphStyle(graph,dm)
          scaleTGraph(graph,100.0)
          graphs.append(graph)
          close(hist)
        
        name        = "%s/%s_%s%s%s_fractions.png"%(outdir,variable.filename,selection.filename.replace("reco",''),tag,plottag)
        ymin, ymax  = 0.0, 100.0
        xmin, xmax  = variable.xmin, variable.xmax
        rmin, rmax  = 0.02, 1.2
        title       = selection.title
        text        = "gen decay modes"
        xtitle      = variable.title
        ytitle      = "gen fractions of Drell-Yan [%]"
        rtitle      = "Ratio with %s"%DM_dict[DM]
        position    = 'middleleft' if 'm_vis' in name and DM=='DM10' else 'middleright' if DM=='DM10' else 'topright'
        width       = 0.4
        denom       = genDMs.index(DM)+1
        
        drawTGraphsWithRatio(graphs,name=name,exts=exts,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax,rmin=rmin,rmax=rmax,
                             xtitle=xtitle,ytitle=ytitle,rtitle=rtitle,title=title,text=text,position=position,denom=denom,width=width,style=False)
        close(hist0)
    


def plotDecayModeShapes(channel,samples):
    """Plots comparisons of shapes."""
    print green("plotDecayModeShapes()",pre=">>>\n>>> ")
    
    samplenames = [
      ("DY",    "Drell-Yan",     "DY",                  ),
      #("ZTT",   "Z -> tautau",   "DY", "gen_match_2==5" ), #"Z -> tau_{mu}tau_{h}"
    ]
    
    decayModes = [ 1, 10, 11 ]
    
    variables = [
      var("pt_2",   25,    0, 100,   position="right", cposition={"decayMode_2==0":"x=0.42"} ),
      var("m_2",    18,  0.20, 2.0,  title="tau mass", filename="m_tau", veto="decayMode_2==0",
                                     cbinning={'decayMode_2==1(?![01])':(18,0.20,2.0), 'decayMode_2==1[01]':(11,0.70,1.8)}, cposition={"decayMode_2==11":'left'} ),
      var("m_vis",  40,    0, 200,   position="right" ),
#       var("eta_1",      28,  -3.0, 2.6,  position="topleftleft", title="muon eta", ymargin=1.25 ),
#       var("eta_2",      28,  -3.0, 2.6,  position="topleftleft", title="tau eta",  ymargin=1.30 ),
    ]
    
    # SETTINGS
    tag       = "_splitByGenDM"
    outdir    = OUT_DIR
    ratio     = True #and False
    norm      = True #and False
    staterror = True #and False
    exts      = ['png','pdf'] if args.pdf else ['png']
    
    for sampleinfo  in samplenames:
      samplename, sampletitle, searchterm = sampleinfo[:3]
      extracuts = "" if len(sampleinfo)<4 else sampleinfo[3]
      sample    = samples.get(searchterm,unique=True)
      
      for selection0 in selections:
        
        # LOOP over DECAYMODES
        for iDM in decayModes:
          if iDM==11 and "newDM" not in selection0.title: continue
          seltitle  = "%s, reco DM%d"%(selection0.title,iDM)
          selstring = combineCuts(selection0.selection,"decayMode_2==%d"%iDM,extracuts)
          selection = sel(seltitle,selstring)
          print green('plot %s for selection "%s"'%(sampletitle,selection),pre=">>>\n>>>   ")
          
          # LOOP over VARIABLES
          for variable in variables:
            if not variable.plotForSelection(selection) or not selection.plotForVariable(variable):
              print ">>>   plotDecayModeShapes: ignoring %s for %s"%(variable.printWithBinning(),selection); continue
            variable.changeContext(selection.selection)
            
            DM = 'DM%d'%iDM
            components = [ ("real tau_h, gen %s"%DM_dict[DM], "gen_decayMode_2==%d"%iDM),
                           ("real tau_h, other gen decay modes",   "gen_decayMode_2!=%d"%iDM), ]
            if "gen_match_2==5" not in selection.selection:
              components.append(("fake tau_h",     "gen_match_2!=5" ))
            
            hists  = [ ]
            for i, (title, cuts) in enumerate(components,1):
              app  = "_%s"%i
              hist = sample.hist(variable,selection,append=app,title=title,extracuts=cuts)
              hists.append(hist)
            
            # NAME
            filename = "%s/%s_%s%s_%s_shapes.png"%(outdir,variable.filename,selection.filename.replace('reco',""),tag,samplename)
            filename = makeFileName(filename)
          
            # TITLE
            name       = variable.name
            #title      = "%s, %s"%(sampletitle,selection.title)
            text       = sampletitle
            title      = selection.title
            xtitle     = variable.title
            position   = variable.position if variable.position else "x=0.5"
            ymargin    = 1.26
            ratiorange = 0.21
            
            # PLOT
            plot = Plot(hists,title=title)
            plot.plot(xtitle,ymargin=ymargin,ratiorange=ratiorange,ratio=ratio,norm=norm,staterror=staterror,
                      position=position,textsize=0.040,text=text)
            plot.saveAs(filename,ext=exts)
            plot.close()
        






def plotDecayModeResolution(channel,samples):
    """Plot resolutions."""
    print green("plotDecayModeResolution()",pre=">>>\n>>> ")
    
    outdir     = OUT_DIR
    tag        = "_splitByGenDM"
    exts       = ['png','pdf'] if args.pdf else ['png']
    doFakes    = True #and False
    genDMs     = [ 'DM0', 'DM1', 'DM2', 'DM10', 'DM11', 'DM12', ]
    if doFakes: genDMs += [ 'LTF', 'JTF', ]
    sampleDY   = samples.get('DY',unique=True)
    
    #decayModes = [ 'DM1', 'DM10', 'DM11',]
    
    selectionsDM = [
#       ('DM0',  sel("oldDMv1, m_T<50, reco DM0",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==0")  )),
#       ('DM1',  sel("oldDMv1, m_T<50, reco DM1",  "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==1")  )),
#       ('DM10', sel("oldDMv1, m_T<50, reco DM10", "%s && %s"%(baselineOldv1,"pfmt_1<50 && decayMode_2==10") )),
      ('DM0',  sel("oldDMv2, m_T<50, reco DM0",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==0")  )),
      ('DM1',  sel("oldDMv2, m_T<50, reco DM1",  "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==1")  )),
      ('DM10', sel("oldDMv2, m_T<50, reco DM10", "%s && %s"%(baselineOldv2,"pfmt_1<50 && decayMode_2==10") )),
      ('DM0',  sel("newDM, m_T<50, reco DM0",    "%s && %s"%(baselineNew,"pfmt_1<50 && decayMode_2==0")    )),
      ('DM1',  sel("newDM, m_T<50, reco DM1",    "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==1")  )),
      ('DM10', sel("newDM, m_T<50, reco DM10",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==10") )),
      ('DM11', sel("newDM, m_T<50, reco DM11",   "%s && %s"%(baselineNew,  "pfmt_1<50 && decayMode_2==11") )),
    ]
    
    
    m1bins = [0.0,0.2,0.5] + frange(0.60,1.8,0.1) + [1.8,2.5]
    m2bins = [0.0,0.2,0.5] + frange(0.70,1.8,0.1) + [1.8,2.5]
    ptbins = [0.0] + range(20,50,5) + [50,60,80,100,150,250]
    rbins  = [0.0,0.3,0.5,0.7,0.8,0.9,0.95,1.0,1.05,1.1,1.2,1.5,2.0,4.0]
    
    variables2D = [
      (var("gen_mvis_2",        50,  0,   2,  title="visible gen tau mass", filename="m_tau", veto="decayMode_2==0",
                                              cbinning={'decayMode_2==1(?![01])':m1bins, 'decayMode_2==1[01]':m2bins} ),
       var("m_2/gen_mvis_2",    80,  0,   4,  title="reco m_tau / vis gen m_tau"                  ) ),
#       (#var("gen_ptvis_2",       50,  0, 150,  title="visible gen tau pt", filename="taupt"        ),
#        var("gen_ptvis_2",       ptbins,       title="visible gen tau pt", filename="pt_tau"       ),
#        var("pt_2/gen_ptvis_2",  80,  0,   4,  title="reco tau pt / vis gen tau pt"                ) ),
    ]
    
    # PLOT
    for DM, selection in selectionsDM:
      print green('plot with selection "%s"'%(selection.title),pre=">>>\n>>>   ")
      for xvariable, yvariable in variables2D:
        if not xvariable.plotForSelection(selection) or not selection.plotForVariable(xvariable):
          print '>>>   plotDecayModeResolution: ignoring %s for %s, tag "%s"'%(xvariable.printWithBinning(),selection,tag); continue
        xvariable.changeContext(selection.selection)
                    
        iDM = int(DM.replace('DM',''))
        components = [ ("gen %s"%DM_dict[DM], "gen_decayMode_2==%d"%iDM),
                       ("other gen decay modes",   "gen_decayMode_2!=%d"%iDM), ]
        #if "gen_match_2==5" not in selection.selection:
        #  components.append(("fake tau_h",     "gen_match_2!=5" ))
        
        profiles = [ ]
        for i, (title,cuts) in enumerate(components):
          app  = "_%d"%i
          hist = sampleDY.hist2D(xvariable,yvariable,selection,extracuts=cuts,append=app)
          #prof = averageY(hist,app)
          prof = hist.ProfileX()
          prof.SetTitle(title)
          setTProfileStyle(prof,i)
          profiles.append(prof)
          close(hist)
          #for i in xrange(1,prof.GetXaxis().GetNbins()+1): print i, prof.GetBinContent(i)
        
        name        = "%s/%s_%s%s%s_response.png"%(outdir,xvariable.filename,selection.filename.replace("reco",''),tag,plottag)
        title       = selection.title
        text        = "Z -> tau_{mu}tau_{h} with real tau_h" #"Drell-Yan"
        xtitle      = xvariable.title
        ytitle      = "#LT %s #GT"%yvariable.title
        rtitle      = "Ratio with %s"%DM_dict[DM]
        position    = xvariable.position if xvariable.position else "x=0.46" #'middleleft' if 'm_vis' in name and DM=='DM10' else 'middleright' if DM=='DM10' else 'topright'
        ymin, ymax  = 0.4, 2.1
        ratiorange  = 0.21
        
        # PLOT
        plot = Plot(profiles,title=title)
        plot.plot(xtitle,ytitle=ytitle,ymargin=1.2,ratiorange=ratiorange,ratio=True,norm=False,staterror=True,
                  position=position,textsize=0.048,text=text,ymin=ymin,ymax=ymax,ytitleoffset=0.9)
        plot.saveAs(name,ext=exts)
        plot.close()




def getDMBin(key):
  """Get bin value of some key."""
  if   'DM0' == key: yield 0
  elif 'DM1' == key: yield 1
  elif 'DM2' == key:
    for i in range(2,10):
      yield i
  elif 'DM10' == key: yield 10
  elif 'DM11' == key: yield 11
  elif 'DM12' == key:
    for i in range(12,20):
      yield i
  elif 'LTF' == key:
    for i in range(1,5):
      yield i
  elif 'JTF' == key: yield 6
  return

def setTGraphStyle(graph,dm):
    """Set TGraph style according to decay mode."""
    color = colorsDM[dm]
    graph.SetTitle(DM_dict[dm])
    graph.SetLineColor(color)
    graph.SetLineStyle(1)
    graph.SetLineWidth(2)
    graph.SetMarkerColor(color)
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(1)

def setTProfileStyle(prof,i):
    """Set TGraph style according to decay mode."""
    color = colors[i]
    prof.SetLineColor(color)
    prof.SetLineStyle(1)
    prof.SetLineWidth(2)
    prof.SetMarkerColor(color)
    prof.SetMarkerStyle(20)
    prof.SetMarkerSize(1)

def scaleTGraph(graph,scale):
    """Scale up a TGraph by some constant."""
    for i in xrange(graph.GetN()):
      graph.GetY()[i] *= scale
    if isinstance(graph,TGraphAsymmErrors):
      for i in xrange(graph.GetN()):
        graph.GetEYhigh()[i] *= scale
        graph.GetEYlow()[i]  *= scale

def averageY(hist,app=""):
    """Average histogram."""
    xmin, xmax = hist.GetXaxis().GetXmin(), hist.GetXaxis().GetXmax()
    nxbins  = hist.GetXaxis().GetNbins()
    nybins  = hist.GetYaxis().GetNbins()
    profile = TH1F("average"+app,"average",nxbins,xmin,xmax)
    profile.Sumw2()
    #graph = TGraphAsymmErrors()
    for xbin in xrange(1,nxbins+1):
      nom  = 0.0
      den  = 0.0
      xval = hist.GetXaxis().GetBinCenter(xbin)
      #print ">>> %4d: %6.1f "%(xbin,xval)
      for ybin in xrange(1,nybins+1):
        yval  = hist.GetYaxis().GetBinCenter(ybin)
        ybinc = hist.GetBinContent(xbin,ybin)
        #print ">>>   %4d: %6.1f, %6.1f"%(ybin,yval,ybinc)
        nom += yval*ybinc
        den += ybinc
      if den>0:
        #print ">>>   %7.1f / %7.1f = %6.1f"%(nom,den,nom/den)
        profile.SetBinContent(xbin,ybin,nom/den)
        #graph.SetPoint(xbin-1,xval,nom/den)
    return profile

def frange(start,stop,step):
  flist = [ ]
  flist.append(start)
  next  = start+step
  while next<stop:
    flist.append(next)
    next+=step
  return flist
      
    
          

def sortStringWithNumbers(list):
  """Sort list of strings containing numbers."""
  convert  = lambda t: int(t) if t.isdigit() else t
  alphanum = lambda k: [convert(c) for c in re.split('([0-9]+)',k)]
  return sorted(list,key=alphanum)


def green(string,**kwargs):
    return kwargs.get('pre',"")+"\x1b[0;32;40m%s\033[0m"%string
    


def main():
    print ">>> "
    
    channel  = "mutau"
    treename = "tree_%s_cut_relaxed"%(channel)
    samples.setChannel(channel,treename=treename)
    
#     plotDecayMode2D(channel,samples)
    plotDecayModeDataMC(channel,samples) # SPLIT BY GEN DECAY MODES
#     plotGenDecayMode(channel,samples)    # SPLIT BY RECO DECAY MODES
#     plotDecayModeFractions(channel,samples)
#     plotDecayModeShapes(channel,samples)
#     plotDecayModeResolution(channel,samples)
    
    print ">>>\n>>> done\n"
    


if __name__ == '__main__':
    main()




