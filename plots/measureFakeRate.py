#! /usr/bin/env python

import os, sys, re
from math import floor, ceil
from argparse import ArgumentParser
sys.path.append('../plots')
from array import array
import PlotTools.PlotTools
from PlotTools.SettingTools import ensureDirectory
from PlotTools.PlotTools import Plot, rebin, makeFileName
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.PrintTools import color, warning, error, printSameLine, header
import ROOT
from ROOT import gPad, gROOT, gStyle, gRandom, gDirectory, TGaxis, Double, kFALSE, TFile, TTree,\
                 TH1F, TH2F, TH1D, THStack, TCanvas, TLegend, TGraph, TGraphAsymmErrors, TLine, TLatex,\
                 TText, TLatex, kBlack, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta, kTeal
ROOT.gROOT.SetBatch(ROOT.kTRUE)

argv = sys.argv
description = '''This script make some checks.'''
parser = ArgumentParser(prog="checkPlots",description=description,epilog="Succes!")
parser.add_argument( "-v", "--verbose", dest="verbose", default=False, action='store_true',
                     help="print verbose" )
args = parser.parse_args()

SFRAME_DIR = "SFrameAnalysis_ltau2017"
IN_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_mumu2017"
OUT_DIR = "plots_check"

# CMS style
era, luminosity = "2017", 41.3
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_13TeV   = "%s, %s fb^{-1}"%(era,luminosity) if era else "%s fb^{-1}"%(luminosity) if luminosity else ""
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.11
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()
TGaxis.SetExponentOffset(-0.060,0.005,'y')
gStyle.SetOptStat(0)
gStyle.SetOptFit(0)

colors   = [ kBlack, kBlue, kRed, kGreen, kMagenta, kOrange, kTeal, kAzure+2, kYellow-3 ]
varlabel = { 'm_2':   "m_{#tau}", #_{h}
             'm_vis': "m_{vis}",
             'DM0':   "h^{#pm}",
             'DM1':   "h^{#pm}h^{0}",
             'DM10':  "h^{#pm}h^{#mp}h^{#pm}",
             'DM11':  "h^{#pm}h^{#mp}h^{#pm}h^{0}",
}


def measureFakeRate():
    print ">>>\n>>> measureFakeRate()"
    
    measure     = True #and False
    draw1D      = True #and False
    draw2D      = True #and False
    CCdef       = True and False
    
    indir       = IN_DIR
    sampledir   = "SingleMuon"
    samplename  = "SingleMuon_Run2017"
    globalTag   = "_2017_V2"
    channel     = "mumu"
    treename    = "tree_%s" % channel
    outdir      = ensureDirectory("fakeRate") 
    plottag     = "" if not CCdef else "_CCdef"
    
    filename    = "%s/%s/DiMuonAnalysis.%s%s.root"%(indir,sampledir,samplename,globalTag) # data
    filenameout = "%s/fakeRate2017_Izaak.root"%(outdir) if not CCdef else\
                  "%s/fakeRate2017_Izaak_CCdef.root"%(outdir)
    
    file        = TFile(filename,'READ')
    fileout     = TFile(filenameout,'UPDATE')
    tree        = file.Get(treename)
    fileout.cd()
    
    IDs = [
#       ('MVArun2v1oldDM', "MVA 2017MC_v1 training",       "MVArerun",      "by%sIsolationMVArun2v1DBoldDMwLT_3",        'VLoose' ),
#       ('MVArun2v2oldDM', "MVA 2017MC_v2 training",       "MVArerunv2",    "by%sIsolationMVArun2v2DBoldDMwLT_3",        'VLoose' ),
      ('MVArun2v1newDM', "MVA 2017MC_v2 training newDM", "MVArerunv1new", "by%sIsolationMVArun2v1DBnewDMwLT_3",        'VLoose' ),
      ('cut-based',      "combined #Delta#beta corr. 3", "comb3",         "by%sCombinedIsolationDeltaBetaCorr3Hits_3", 'Loose'  ),
    ]
    WPs  = [
      ('Loose' ),
      ('Medium'),
      ('Tight' ),
    ]
    DMs  = [
      ("DM0",   "h^{\pm}",                    "decayMode_3==0" ),
      ("DM1",   "h^{\pm}h^{0}",               "decayMode_3==1" ),
      ("DM10",  "h^{\pm}h^{\mp}h^{\pm}",      "decayMode_3==10"),
      ("DM11",  "h^{\pm}h^{\mp}h^{\pm}h^{0}", "decayMode_3==11")
    ]
    cut        = "iso_1<0.15 && iso_2<0.15 && extraelec_veto==0 && extramuon_veto==0 && q_1*q_2<0 && pt_3>20"
    xvarname, xvartitle = "pt_3", "tau p_{T} [GeV]"
    yvarname, yvartitle = "m_3", "tau mass [GeV]"
    xbins      = [20,25,30,35,40,45,50,60,80,100,200]
    xbins2D    = [20,25,30,35,40,45,50,55,200]
    ybins_dict = { 'DM1':  [0.1,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.6,1.8,2.0,3.0],
                   'DM10':                 [0.6,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8],
                   'DM11':                 [0.6,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8],
    }
    xmin, xmax =  0.0, 220
    rmin, rmax =  0.05, 2.0
    draw1D     = len(DMs)>=3
    
    for idfilename, idtitle, idname, idpattern, wpdenname in IDs:
      print green("  %s"%(idtitle))
      for wpnomname in WPs:
        if wpnomname==wpdenname: continue
        ymin, ymax = 0.0, 0.95
        if 'cut' in idfilename:
          if 'Tight' in wpnomname: ymax = 1.2
          else:                    ymax = 3.2
        
        wpnomcut = "%s==1"%(idpattern%(wpnomname))
        wpdencut = "%s==1 && %s!=1"%(idpattern%(wpdenname),idpattern%(wpnomname)) if not CCdef else\
                   "%s==1"%(idpattern%(wpdenname)) # Cecile's definition
        wpnom    = getWPLetters(wpnomname).upper()
        wpden    = getWPLetters(wpdenname).upper()
        
        canvasname = "%s/fakeRate-%s-%s%s.png"%(outdir,idfilename,wpnomname.lower(),plottag)
        canvasname2D = "%s/fakeRate-%s-%s-%%s%s.png"%(outdir,idfilename,wpnomname.lower(),plottag)
        dentitle   = "%s && !%s"%(wpdenname,wpnomname) if not CCdef else wpdenname # Cecile's definition
        title      = "%s, %s / (%s)"%(idtitle,wpnomname,dentitle)
        xtitle     = xvartitle
        ytitle     = "fake rate"
        ztitle     = "fake rate"
        
        # GET FAKE RATES
        graphs  = [ ]
        hists2D = [ ]
        maxs    = [ ]
        for i, (dmname, dmtitle, dmcut) in enumerate(DMs):
          if '11' in dmcut and 'newDM' not in idpattern: continue
          
          # GRAPH
          gname   = "h_%s%s_%s_h_%s%s_%s"%(idname,wpnom,dmname.lower(),idname,wpden,dmname.lower())
          hname2D = "h_%s%s_%s_h_%s%s_%s_mass"%(idname,wpnom,dmname.lower(),idname,wpden,dmname.lower())
          gtitle  = dmtitle
          if measure:
            cutnom  = "%s && %s && %s"%(cut,dmcut,wpnomcut)
            cutden  = "%s && %s && %s"%(cut,dmcut,wpdencut)
            print '>>>     making %s... \n>>>       "%s"\n>>>       "%s"'%(dmname,cutnom,cutden)
            if draw1D:
              # 1D GRAPH
              namenom = dmname+"_nom"; titlenom = "nominator "+dmtitle
              nameden = dmname+"_den"; titleden = "denominator "+dmtitle
              histnom = TH1F(namenom,titlenom,len(xbins)-1,array('d',xbins))
              histden = TH1F(nameden,titleden,len(xbins)-1,array('d',xbins))
              histnom.SetBinErrorOption(TH1F.kPoisson)
              histden.SetBinErrorOption(TH1F.kPoisson)
              tree.Draw("%s >> %s"%(xvarname,namenom),cutnom,"gOff")
              tree.Draw("%s >> %s"%(xvarname,nameden),cutden,"gOff")
              nom     = histnom.Integral()
              den     = histden.Integral()
              graph   = makeRatioHists(histnom,histden,name=dmname,title=gtitle,underflow=False,overflow=False)
              gtitle  = "%s (%d/%d)"%(dmtitle,nom,den)
              graph.Write(gname,TGraphAsymmErrors.kOverwrite)
              gDirectory.Delete(histnom.GetName())
              gDirectory.Delete(histden.GetName())
              print ">>>       => %d/%d = %.3f"%(nom,den,nom/den)
            if draw2D and dmname!='DM0' and 'loose' not in wpnomname.lower():
              # 2D HIST
              namenom2D = dmname+"_nom_2D"; titlenom2D = "%s nominator"%(dentitle)
              nameden2D = dmname+"_den_2D"; titleden2D = "%s denominator"%(dentitle)
              ybins     = ybins_dict[dmname]
              histnom2D = TH2F(namenom2D,titlenom2D,len(xbins2D)-1,array('d',xbins2D),len(ybins)-1,array('d',ybins))
              histden2D = TH2F(nameden2D,titleden2D,len(xbins2D)-1,array('d',xbins2D),len(ybins)-1,array('d',ybins))
              histnom2D.SetBinErrorOption(TH2F.kPoisson)
              histden2D.SetBinErrorOption(TH2F.kPoisson)
              tree.Draw("%s:%s >> %s"%(yvarname,xvarname,namenom2D),cutnom,"gOff")
              tree.Draw("%s:%s >> %s"%(yvarname,xvarname,nameden2D),cutden,"gOff")
              nom2D   = histnom2D.Integral()
              den2D   = histden2D.Integral()
              ratio2D = makeRatioHists2D(histnom2D,histden2D,name=dmname+"_2D",title="fake rate")
              ratio2D.GetXaxis().SetTitle(xvartitle)
              ratio2D.GetYaxis().SetTitle(yvartitle)
              ratio2D.Write(hname2D,TH2F.kOverwrite)
              print ">>>       => %d/%d = %.3f (2D)"%(nom2D,den2D,nom2D/den2D)
              hists2D.append((ratio2D,histnom2D,histden2D))
          else:
            graph = fileout.Get(gname)
          
          if draw1D:
            graph.SetTitle(gtitle)
            setGraphStyle(graph,i)
            ymin, ymax = getTGraphYRange(graph,ymin,ymax)
            graphs.append((gtitle,graph))
        
        # DRAW FAKE RATES
        ymax = ymax*1.2
        if graphs:
          canvas = TCanvas("canvas","canvas",100,100,800,600)
          canvas.SetFillColor(0)
          canvas.SetBorderMode(0)
          canvas.SetFrameFillStyle(0)
          canvas.SetFrameBorderMode(0)
          canvas.SetTopMargin(  0.08 ); canvas.SetBottomMargin( 0.14 )
          canvas.SetLeftMargin( 0.12 ); canvas.SetRightMargin(  0.04 )
          canvas.SetTickx(0); canvas.SetTicky(0)
          canvas.SetGrid()
          canvas.cd()
        
          textsize   = 0.045
          lineheight = 0.055
          x1, width  = 0.16, 0.25
          y1, height = 0.90, lineheight*4
          legend = TLegend(x1,y1,x1+width,y1-height)
          legend.SetTextSize(textsize)
          legend.SetBorderSize(0)
          legend.SetFillStyle(0)
          legend.SetFillColor(0)
          legend.SetTextFont(62)
          legend.SetHeader(title)
          legend.SetTextFont(42)
        
          frame = canvas.DrawFrame(xmin,ymin,xmax,ymax)
          frame.GetYaxis().SetTitleSize(0.060)
          frame.GetXaxis().SetTitleSize(0.060)
          frame.GetXaxis().SetLabelSize(0.050)
          frame.GetYaxis().SetLabelSize(0.050)
          frame.GetXaxis().SetLabelOffset(0.010)
          frame.GetXaxis().SetTitleOffset(1.04)
          frame.GetYaxis().SetTitleOffset(1.04)
          frame.GetXaxis().SetNdivisions(508)
          frame.GetYaxis().SetTitle(ytitle)
          frame.GetXaxis().SetTitle(xtitle)
        
          for i, (gtitle,graph) in enumerate(graphs):
            graph.Draw('LPsame')
            legend.AddEntry(graph, gtitle, 'lp')
        
          legend.Draw()
        
          CMS_lumi.relPosX = 0.11
          CMS_lumi.CMS_lumi(canvas,13,0)
          gPad.SetTicks(1,1)
          gPad.Modified()
          frame.Draw('sameaxis')
      
          canvas.SaveAs(canvasname)
          canvas.Close()
        
        # MASS-DEPENDENCE
        intsnom    = [ ] # integrals
        intsden    = [ ] 
        intstitles = [ ]
        #ymax = ymax*1.2
        zmax       = 3.0 if "cut" in idfilename else 1.0
        for histrat, histnom, histden in hists2D:
          
          intsnom = integrateSlicesFromTH2(histnom)
          intsden = integrateSlicesFromTH2(histden)
          intstitles = [" (%d/%d)"%(n,d) for (n,d) in zip(intsnom,intsden)]
          #print intstitles
          
          text = varlabel[getDM(histnom.GetName())]
          canvasnamerat = canvasname2D%histrat.GetName()
          canvasnamenom = canvasname2D%histnom.GetName()
          canvasnameden = canvasname2D%histden.GetName()
          canvasnameslices = canvasname2D%(histrat.GetName().replace('_2D','_mass'))
          #option = "COLZ" if re.search('DM1(?!0)',canvasnamerat) else "COLZTEXT44"
          
          # 2D
          drawHist2D(histrat,title=title,xtitle=xtitle,ytitle=yvartitle,ztitle=histrat.GetTitle(),text=text,canvas=canvasnamerat,option="COLZ") #zmin=0.0) #,zmax=zmax)
          drawHist2D(histnom,title=title,xtitle=xtitle,ytitle=yvartitle,ztitle=histnom.GetTitle(),text=text,canvas=canvasnamenom)
          drawHist2D(histden,title=title,xtitle=xtitle,ytitle=yvartitle,ztitle=histden.GetTitle(),text=text,canvas=canvasnameden)
          
          # mass slices
          ymax   = 0.85 if 'tight' in canvasnamerat.lower() and 'MVA' in canvasnamerat else ymax
          slices = makeTGraphSlicesFromTH2(histrat,var="m_{#tau}",underflow=False,apptitles=intstitles)
          denom  = min(3,len(slices))
          
          kwargs = { 'title': title, 'xtitle': xtitle, 'ytitle': ytitle, 'text': text, 'canvas': canvasnameslices,
                     'xmin':  xmin,  'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'rmin': rmin, 'rmax': rmax, 'denom': denom, }
          if len(slices)<8:
            drawTGraphsWithRatio(slices,**kwargs)
          else:
            kwargs['canvas'] = canvasnameslices.replace('_mass','_mass_left')
            drawTGraphsWithRatio(slices[:len(slices)/2],**kwargs)
            kwargs['canvas'] = canvasnameslices.replace('_mass','_mass_right')
            drawTGraphsWithRatio(slices[len(slices)/2:],**kwargs)
          for hist in [histrat,histnom,histden]:
            gDirectory.Delete(hist.GetName())
        
    file.Close()
    fileout.Close()
    


def compareFakeRate():
    print ">>>\n>>> measureFakeRate()"
    
    indir      = "fakeRate"
    outdir     = indir
    
    filename1 = "PlotTools/%s/fakeRate2017_histograms_Cecile.root"%(indir)
    filename2 = "%s/fakeRate2017_Izaak_CCdef.root"%(outdir) # Cecile's definition
    file1     = TFile(filename1)
    file2     = TFile(filename2)
    
    IDs = [
      ('MVArun2v1oldDM', "MVA 2017MC_v1 training",       "MVArerun",   'VLoose' ),
      #('MVArun2v2oldDM', "MVA 2017MC_v2 training",       "MVArerunv2", 'VLoose' ),
      #('cut-based',      "combined #Delta#beta corr. 3", "comb3",      'Loose'  ),
    ]
    WPs  = [
      'Loose',
      #'Medium',
      #'Tight',
    ]
    DMs  = [
      ('DM0',   "h^{\pm}",              ),
      ('DM1',   "h^{\pm}#pi^{0}",         ),
      ('DM10',  "h^{\pm}h^{\mp}h^{\pm}" )
    ]
    xvarname, vartitle = "pt_3", "tau p_{T} [GeV]"
    xmin, xmax = 0, 220
    ymin, ymax = -0.5, 2.2
    rmin, rmax = 0.70, 2.50
    
    for idfilename, idtitle, idname, wpdenname in IDs:
      for wpname in WPs:
        if wpname==wpdenname: continue
        for i, (dmname, dmtitle) in enumerate(DMs):
          
          title      = "%s, %s / %s"%(idtitle, wpname,wpdenname) # Cecile's definition
          xtitle     = vartitle
          ytitle     = "fake rate"
          text       = dmtitle
          canvasname = "%s/fakeRate-%s-%s-%s_comparison_CCdef.png"%(outdir,idfilename,wpname.lower(),dmname) # Cecile's definition
          
          wpnom  = getWPLetters(wpname).upper()
          wpden  = getWPLetters(wpdenname).upper()
          gname  = "h_%s%s_%s_h_%s%s_%s"%(idname,wpnom,dmname.lower(),idname,wpden,dmname.lower())
          graph1 = file1.Get(gname)
          graph2 = file2.Get(gname)
          if not graph1: print 'Did not find "%s" in %s'%(gname,filename1)
          if not graph2: print 'Did not find "%s" in %s'%(gname,filename2)
          graph1.SetTitle("Cecile")
          graph2.SetTitle("Izaak")
          graphs = [graph1,graph2]
          #ymin, ymax = getTGraphYRange(graph1,ymin,ymax)
          #ymin, ymax = getTGraphYRange(graph2,ymin,ymax)
          
          drawTGraphsWithRatio(graphs,title=title,xtitle=xtitle,ytitle=ytitle,text=text,canvas=canvasname,
                               xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax,rmin=rmin,rmax=rmax)
    
    file1.Close()
    file2.Close()
    


def drawHist2D(hist,**kwargs):
    """Draw 2D histogram on canvas."""
    
    title      = kwargs.get('title',    ""           )
    xtitle     = kwargs.get('xtitle',   hist.GetXaxis().GetTitle() )
    ytitle     = kwargs.get('ytitle',   hist.GetYaxis().GetTitle() )
    ztitle     = kwargs.get('ztitle',   ""           )
    xmin       = kwargs.get('xmin',     None         )
    xmax       = kwargs.get('xmax',     None         )
    ymin       = kwargs.get('ymin',     None         )
    ymax       = kwargs.get('ymax',     None         )
    zmin       = kwargs.get('zmin',     None         )
    zmax       = kwargs.get('zmax',     None         )
    text       = kwargs.get('text',     ""           )
    option     = kwargs.get('option',   "COLZTEXT44" )
    canvasname = kwargs.get('canvas',   "hist2D.png" )
    
    canvas = TCanvas("canvas","canvas",100,100,800,700)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetTopMargin(  0.08 ); canvas.SetBottomMargin( 0.14 )
    canvas.SetLeftMargin( 0.12 ); canvas.SetRightMargin(  0.19 )
    canvas.SetTickx(0); canvas.SetTicky(0)
    canvas.SetGrid()
    canvas.cd()
    
    if zmin: hist.SetMinimum(zmin)
    if zmax: hist.SetMaximum(zmax)
    
    hist.GetXaxis().SetTitleSize(0.058)
    hist.GetYaxis().SetTitleSize(0.058)
    hist.GetZaxis().SetTitleSize(0.056)
    hist.GetXaxis().SetLabelSize(0.048)
    hist.GetYaxis().SetLabelSize(0.048)
    hist.GetZaxis().SetLabelSize(0.044)
    hist.GetXaxis().SetLabelOffset(0.010)
    hist.GetXaxis().SetTitleOffset(1.04)
    hist.GetYaxis().SetTitleOffset(1.04)
    hist.GetZaxis().SetTitleOffset(1.25)
    hist.GetZaxis().CenterTitle(True)
    hist.GetXaxis().SetTitle(xtitle)
    hist.GetYaxis().SetTitle(ytitle)
    hist.GetZaxis().SetTitle(ztitle)
    hist.SetMarkerColor(kRed)
    #hist.SetMarkerSize(1)
    hist.Draw(option)
    
    latex = None
    if text:
      latex = TLatex()
      latex.SetTextSize(0.050)
      latex.SetTextAlign(33)
      latex.SetTextFont(42)
      #latex.SetTextColor(kRed)
      latex.SetNDC(True)
      latex.DrawLatex(0.79,0.90,text)
    
    CMS_lumi.relPosX = 0.14
    CMS_lumi.CMS_lumi(canvas,13,0)
    canvas.SaveAs(canvasname)
    canvas.Close()
    


def drawTGraphsWithRatio(graphs,**kwargs):

    title      = kwargs.get('title',    ""           )
    xtitle     = kwargs.get('xtitle',   ""           )
    ytitle     = kwargs.get('ytitle',   ""           )
    xmin       = kwargs.get('xmin',     0            )
    xmax       = kwargs.get('xmax',     100          )
    ymin       = kwargs.get('ymin',     0            )
    ymax       = kwargs.get('ymax',     100          )
    rmin       = kwargs.get('rmin',     0.5          )
    rmax       = kwargs.get('rmax',     1.5          )
    text       = kwargs.get('text',     ""           )
    denom      = kwargs.get('denom',    1            )-1 # denominator for ratio
    canvasname = kwargs.get('canvas',   "graphs.png" )
    graphsleg  = columnize(graphs) if len(graphs)>6 else graphs # reordered for two columns
    
    # MAIN plot
    L, R = 0.12, 0.04
    canvas = TCanvas("canvas","canvas",100,100,800,800)
    canvas.Divide(2)
    canvas.cd(1)
    gPad.SetPad("pad1","pad1",0,0.33,1,1,0,-1,0)
    
    gPad.SetFillColor(0)
    gPad.SetBorderMode(0)
    gPad.SetFrameFillStyle(0)
    gPad.SetFrameBorderMode(0)
    gPad.SetTopMargin(  0.10 ); gPad.SetBottomMargin( 0.01 )
    gPad.SetLeftMargin(   L  ); gPad.SetRightMargin(   R   )
    gPad.SetTickx(0); gPad.SetTicky(0)
    gPad.SetGrid()
    
    if len(graphs)>6:
      textsize   = 0.040
      x1, width  = 0.16, 0.75
      y1, height = 0.86, textsize*1.08*ceil(len([l for l in [text]+graphs if l])/2.)
      if title: height += textsize*1.08
    else:
      textsize   = 0.045
      x1, width  = 0.16, 0.25
      y1, height = 0.86, textsize*1.08*len([l for l in [title,text]+graphs if l])
    if title: height += textsize*1.08
    legend = TLegend(x1,y1,x1+width,y1-height)
    legend.SetTextSize(textsize)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.SetFillColor(0)
    legend.SetTextFont(62)
    if title: legend.SetHeader(title)
    legend.SetTextFont(42)
    if len(graphs)>6:
      legend.SetNColumns(2)
      legend.SetColumnSeparation(0.06)
    
    frame = gPad.DrawFrame(xmin,ymin,xmax,ymax)
    frame.GetYaxis().SetTitleSize(0.060)
    frame.GetXaxis().SetTitleSize(0.060*0)
    frame.GetXaxis().SetLabelSize(0.050*0)
    frame.GetYaxis().SetLabelSize(0.052)
    frame.GetXaxis().SetLabelOffset(0.010)
    frame.GetXaxis().SetTitleOffset(0.98)
    frame.GetYaxis().SetTitleOffset(0.98)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().SetTitle(ytitle)
    frame.GetXaxis().SetTitle(xtitle)
    
    for i, graph in enumerate(graphs):
      setGraphStyle(graph,i)
      graph.Draw('LP')
    for graph in graphsleg:
      legend.AddEntry(graph, graph.GetTitle(), 'lp')
    if text:
      legend.AddEntry(0, text, '')
    legend.Draw()
    
    CMS_lumi.relPosX = 0.11
    CMS_lumi.CMS_lumi(gPad,13,0)
    gPad.SetTicks(1,1)
    gPad.Modified()
    frame.Draw('sameaxis')
    
    # RATIO plot
    canvas.cd(2)
    gPad.SetPad("pad2","pad2",0,0,1,0.32,0,-1,0)
    gPad.SetTopMargin(  0.04 ); gPad.SetBottomMargin( 0.30 )
    gPad.SetLeftMargin(   L  ); gPad.SetRightMargin(   R   )
    
    frame_ratio = gPad.DrawFrame(xmin,rmin,xmax,rmax)
    frame_ratio.GetYaxis().CenterTitle()
    frame_ratio.GetYaxis().SetTitleSize(0.12)
    frame_ratio.GetXaxis().SetTitleSize(0.13)
    frame_ratio.GetXaxis().SetLabelSize(0.12)
    frame_ratio.GetYaxis().SetLabelSize(0.11)
    frame_ratio.GetXaxis().SetLabelOffset(0.012)
    frame_ratio.GetXaxis().SetTitleOffset(1.02)
    frame_ratio.GetYaxis().SetTitleOffset(0.50)
    frame_ratio.GetXaxis().SetNdivisions(508)
    frame_ratio.GetYaxis().CenterTitle(True)
    frame_ratio.GetYaxis().SetTitle("ratio")
    frame_ratio.GetXaxis().SetTitle(xtitle)
    frame_ratio.GetYaxis().SetNdivisions(5)
    
    ratios = [ ]
    for i, graph in enumerate(graphs):
      if i==denom: continue
      ratio = makeRatioTGraphs(graph,graphs[denom])
      ratio.SetLineColor(graph.GetLineColor())
      ratio.SetLineStyle(graph.GetLineStyle())
      ratio.SetLineWidth(graph.GetLineWidth())
      ratio.Draw('LSAME')
      ratios.append(ratio)
    line = TLine(xmin,1.,xmax,1.)
    line.SetLineColor(graphs[denom].GetLineColor())
    line.SetLineWidth(graphs[denom].GetLineWidth())
    line.SetLineStyle(1)
    line.Draw('SAME')
    
    gPad.SetTicks(1,1)
    gPad.SetGrid()
    gPad.Modified()
    frame_ratio.Draw('sameaxis')
    
    canvas.SaveAs(canvasname)
    canvas.Close()
    


def makeRatioHists(histnom,histden,**kwargs):
    """Make ratio of two normalized histograms.
    Alternatively, use TGraphAsymmErrors::Divide."""
    nbins   = histnom.GetNbinsX()
    norm    = kwargs.get('normalize',      False     )
    name    = kwargs.get('name',           "ratio"   )
    title   = kwargs.get('title',          "ratio"   )
    yrange  = kwargs.get('yrange',         None      )
    first   = 0 if kwargs.get('underflow', True      ) else 1
    last    = 1 if kwargs.get('overflow',  True      ) else 0
    last   += nbins
    if norm:
      I1    = histnom.Integral()
      I2    = histden.Integral()
      histnom.Scale(1./I1)
      histden.Scale(1./I2)
      print ">>> I1=%s, I2=%s"%(I1,I2)
    ratio = histnom.Clone(name)
    ratio.Sumw2()
    ratio.SetTitle(title)
    ratio.Divide(histden)
    
    graph = TGraphAsymmErrors()
    #graph = TGraphAsymmErrors.Divide(histnom,histden)
    for i, bin in enumerate(ratio):
      if i<first: continue
      if i>last:  continue
      #print graph.GetName(), graph.GetTitle(), i, bin
      center = ratio.GetBinCenter(i)
      width  = ratio.GetBinWidth(i)/2
      error  = ratio.GetBinError(i)
      graph.SetPoint( i-first, center, bin )
      graph.SetPointError( i-first, width, width, error, error )
      if yrange!=None and len(yrange)==2:
        ymin = bin-error
        ymax = bin+error
        if ymin<yrange[0]: yrange[0] = ymin
        if ymax>yrange[1]: yrange[1] = ymax
    
    return graph
    

def makeRatioHists2D(histnom,histden,**kwargs):
    """Make ratio of two normalized histograms."""
    name    = kwargs.get('name',  "ratio2D"  )
    title   = kwargs.get('title', "ratio 2D" )
    ratio = histnom.Clone(name)
    ratio.Sumw2()
    ratio.SetTitle(title)
    ratio.Divide(histden)
    
    return ratio
    

# MAKE ratio
def makeRatioTGraphs(graph0,graph1,**kwargs):
    """Make a ratio of two TGraphs bin by bin."""
    
    # SETTINGS
    verbose     = kwargs.get('verbose',False)    
    N           = graph0.GetN()
    x0, y0      = Double(), Double()
    x1, y1      = Double(), Double()
    graph_ratio = TGraph()
    
    # CHECK binning hist1
    N1 = graph1.GetN()
    if N != N1:
      print ">>> Warning! makeRatioTGraphs: different number of points: %d != %d!"%(N,N1)
      exit(1)
    
    if verbose:
      print ">>> %3s  %9s %9s %9s %9s %9s"%("i","x0","x1","y0","y1","ratio")
    
    # CALCULATE ratio bin-by-bin
    for i in range(0,N):
        graph0.GetPoint(i,x0,y0)
        graph1.GetPoint(i,x1,y1)
        if x0!=x1:
          print ">>> Warning! makeRatioTGraphs: graphs' %i points have different x values: %.2f vs. $.2f !"%(x0,x1)
          exit(0)
        ratio = 0
        if y1:          ratio = y0/y1
        elif y0==y1:    ratio = 1.0
        elif y0>100*y1: ratio = 100.0
        graph_ratio.SetPoint( i, x0, ratio )
        if verbose:
          print ">>> %3s  %9.3f %9.3f %9.3f %9.3f %9.3f"%(i,x0,x1,y0,y1,ratio)
    
    return graph_ratio
    

# MAKE slices
def makeTGraphSlicesFromTH2(hist,**kwargs):
    """Make a TGraph from a 2D histogram bin by bin."""
    
    verbose     = kwargs.get('verbose',        False   )
    name        = kwargs.get('name',           "ratio" )
    title       = kwargs.get('title',          ""      )
    yrange      = kwargs.get('yrange',         None    )
    axis        = kwargs.get('axis',           'y'     )
    var         = kwargs.get('var',            ""      )
    apptitles   = kwargs.get('apptitles',      [ ]     )
    first       = 0 if kwargs.get('underflow', True    ) else 1
    last        = 1 if kwargs.get('overflow',  True    ) else 0
    
    if axis.lower()=='y':
      baxis = hist.GetYaxis()
      xaxis = hist.GetXaxis()
    else:
      baxis = hist.GetXaxis()
      xaxis = hist.GetYaxis()
    nbbins  = baxis.GetNbins()
    nxbins  = xaxis.GetNbins()
    last   += nxbins
    
    graphs = [ ]
    for j in xrange(0,nbbins+1):
      graph   = TGraphAsymmErrors()
      if var:
        title = "%.1f < %s < %.1f"%(baxis.GetBinLowEdge(j),var,baxis.GetBinUpEdge(j))
        #title = "%#.2g < %s < %#.2g"%(baxis.GetBinLowEdge(j),var,baxis.GetBinUpEdge(j))
      if j<len(apptitles):
        title += apptitles[j]
      graph.SetTitle(title)
      allzero = True
      for i in xrange(0,nxbins+1):
        if i<first: continue
        if i>last:  continue
        ix, iy = (i,j) if axis.lower()=='y' else (j,i)
        bin    = hist.GetBinContent(ix,iy)
        center = xaxis.GetBinCenter(i)
        width  = xaxis.GetBinWidth(i)/2
        error  = hist.GetBinError(ix,iy)
        graph.SetPoint( i-first, center, bin )
        graph.SetPointError( i-first, width, width, error, error )
        if yrange!=None and len(yrange)==2:
          ymin = bin-error
          ymax = bin+error
          if ymin<yrange[0]: yrange[0] = ymin
          if ymax>yrange[1]: yrange[1] = ymax
        if bin!=0: allzero = False
      if not allzero: graphs.append(graph)
    return graphs

# INTEGRATE slices
def integrateSlicesFromTH2(hist,**kwargs):
    """Integrate histogram bin by bin."""
    
    verbose     = kwargs.get('verbose',     False   )
    axis        = kwargs.get('axis',        'y'     )
    first       = 0 if kwargs.get('underflow', True ) else 1
    last        = 1 if kwargs.get('overflow',  True ) else 0
    
    if axis.lower()=='y':
      baxis = hist.GetYaxis()
      xaxis = hist.GetXaxis()
    else:
      baxis = hist.GetXaxis()
      xaxis = hist.GetYaxis()
    nbbins  = baxis.GetNbins()
    nxbins  = xaxis.GetNbins()
    last   += nxbins
    
    integrals = [ ]
    for j in xrange(0,nbbins+1):
      integrals.append(0.0)
      for i in xrange(0,nxbins+1):
        if i<first: continue
        if i>last:  continue
        if axis.lower()=='y':
          integrals[j] += hist.GetBinContent(i,j)
        else:
          integrals[j] += hist.GetBinContent(j,i)
    return integrals


def getTGraphYRange(graphs,ymin=+999989,ymax=-999989):
    """Get full y-range of a given TGraph object."""
    if not isinstance(graphs,list) and not isinstance(graphs,tuple):
      graphs = [ graphs ]
    for graph in graphs:
      N = graph.GetN()
      x, y = Double(), Double()
      for i in xrange(0,N):
        graph.GetPoint(i,x,y)
        yup  = y+graph.GetErrorYhigh(i)
        ylow = y-graph.GetErrorYlow(i)
        if yup >ymax: ymax = yup
        if ylow<ymin: ymin = ylow
    return (ymin,ymax)


def getWPLetters(WP):
    wplower = WP.lower()
    matches = [ ]
    if "loose" in wplower:
      matches = re.findall("(v*l)oose",wplower)
    elif "medium" in wplower:
      matches = ['M']
    elif "tight" in wplower:
      matches = re.findall("(v*t)ight",wplower)
    if not matches:
      return ""
    return matches[0].upper()

def getDM(string):
    """Helpfunction to format nuisance parameter."""
    matches = re.findall(r"DM\d+",string)
    return matches[0]
    

def setGraphStyle(graph,i):
    color = colors[i%len(colors)]
    style = 1 if i<len(colors) else 2
    graph.SetLineColor(color)
    graph.SetLineStyle(style)
    graph.SetLineWidth(2)
    graph.SetMarkerColor(color)
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(1)


def columnize(zlist):
    """Reorder of list suchs that a TLegend column is transposed from left-to-righ-top-to-bottom
    to top-to-bottom-left-to-right. E.g. [1,2,3,4,5,6,7] -> [1,5,2,6,3,7,4]."""
    newlist = [ ]
    ihalf = int(ceil(len(zlist)/2.))
    for i,j in zip(zlist[:ihalf],zlist[ihalf:]):
      newlist.append(i)
      newlist.append(j)
    if len(zlist)%2!=0:
      newlist.append(zlist[ihalf-1])
    return newlist
    

def green(string,**kwargs):
    return kwargs.get('pre',">>> ")+"\x1b[0;32;40m%s\033[0m"%string



def main():
    print ""
    
    measureFakeRate()
    #compareFakeRate()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




