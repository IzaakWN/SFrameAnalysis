#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

#from ROOT import * #TFile, TCanvas, TH2D, TH2D, THStack, TAxis, TGaxis, TGraph...
from ROOT import TFile, TCanvas, TPad, TH1, TH1D, TLegend, TAxis, THStack, TGraph, TGraphAsymmErrors, TLine,\
                 TGaxis, gDirectory, gROOT, gPad, Double,\
                 kBlack, kGray, kWhite, kRed, kBlue, kGreen, kYellow,\
                 kAzure, kCyan, kMagenta, kOrange, kPink, kSpring, kTeal, kViolet,\
                 kDashed, kDotted
import CMS_lumi, tdrstyle
import os, re
from math import sqrt, pow, log
from SettingTools   import *
from SelectionTools import *
from VariableTools  import *
from PrintTools     import *
#gROOT.Macro('PlotTools/QCDModelingEMu.C+')
#gROOT.Macro('PlotTools/weightJEta1.C+')

# CMS style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.105
CMS_lumi.outOfFrame = True
CMS_lumi.lumi_13TeV = "%s fb^{-1}" % luminosity
tdrstyle.setTDRStyle()
TGaxis.SetExponentOffset(-0.058,0.005,'y')

# https://root.cern.ch/doc/master/classTColor.html
# http://imagecolorpicker.com/nl
# TColor::GetColor(R,B,G)
legendTextSize = 0.034 #0.036
colors     = [ kBlack,
               kRed+1, kAzure+5, kGreen+2, kOrange+1, kMagenta-4, kYellow+1,
               kRed-9, kAzure-4, kGreen-2, kOrange+6, kMagenta+3, kYellow+2 ]
fillcolors = [ kRed-2, kAzure+5,
               kMagenta-3, kYellow+771, kOrange-5,  kGreen-2,
               kRed-7, kAzure-9, kOrange+382,  kGreen+3,  kViolet+5, kYellow-2 ]
               #kYellow-3

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    


def makeCanvas(**kwargs):
    """Make canvas and pads for ratio plots."""
    
    square              = kwargs.get('square',              False       )
    scaleleftmargin     = kwargs.get('scaleleftmargin',     1           )
    scalerightmargin    = kwargs.get('scalerightmargin',    1           )
    scaletopmargin      = kwargs.get('scaletopmargin',      1           )
    scalebottommargin   = kwargs.get('scaletopmargin',      1           )
    residue             = kwargs.get('residue',             False       )
    ratio               = kwargs.get('ratio',               False       )
    pads                = kwargs.get('pads',                [ ]         ) # pass list as reference
    CMS_lumi.lumi_13TeV = "%s fb^{-1}" % luminosity
    
    W = 800; H  = 600
    if square:
        W = 800; H  = 800
        scalerightmargin = 3.5*scalerightmargin
    elif ratio or residue:
        W = 800; H  = 750
        scaleleftmargin   = 1.14*scaleleftmargin
        scalerightmargin  = 0.80*scalerightmargin
        scaletopmargin    = 0.80*scaletopmargin
        scalebottommargin = 1.06*scaletopmargin
        CMS_lumi.cmsTextSize  = 0.55
        CMS_lumi.lumiTextSize = 0.45
        CMS_lumi.relPosX      = 0.08
    
    T, B = 0.08*scaletopmargin,  0.12*scalebottommargin
    L, R = 0.12*scaleleftmargin, 0.04*scalerightmargin
    
    canvas = TCanvas("canvas","canvas",100,100,W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetTopMargin(  T ); canvas.SetBottomMargin( B )
    canvas.SetLeftMargin( L ); canvas.SetRightMargin(  R )
    
    if ratio or residue:
        canvas.Divide(2)
        canvas.cd(1)
        gPad.SetPad("pad1","pad1", 0, 0.33, 1, 0.95)
        gPad.SetLeftMargin(0.125);  gPad.SetRightMargin(0.03)
        gPad.SetTopMargin(0.02);    gPad.SetBottomMargin(0.00001)
        gPad.SetFillColor(0)
        gPad.SetBorderMode(0)
        gPad.Draw()
        canvas.cd(2)
        gPad.SetPad("pad2","pad2", 0, 0.05, 1, 0.30)
        gPad.SetLeftMargin(0.125);  gPad.SetRightMargin(0.03)
        gPad.SetTopMargin(0.00001); gPad.SetBottomMargin(0.20)
        gPad.SetFillColor(0)
        gPad.SetBorderMode(0)
        gPad.Draw()
        canvas.cd(1)
    
    return canvas
    


def makeLegend(*hists,**kwargs):
    """Make legend."""
    
    title       = kwargs.get('title',           ""              )
    entries     = kwargs.get('entries',         [ ]             )
    position    = kwargs.get('position',        ""              ).lower()
    transparent = kwargs.get('transparent',     False           )
    histsB      = kwargs.get('histsB',          [ ]             )
    histsS      = kwargs.get('histsS',          [ ]             )
    histsD      = kwargs.get('histsD',          [ ]             )
    x1          = kwargs.get('x1',              0               )
    x2          = kwargs.get('x2',              0               )
    y1          = kwargs.get('y1',              0               )
    y2          = kwargs.get('y2',              0               )
    width       = kwargs.get('width',           0               )
    height      = kwargs.get('height',          0               )
    style0      = kwargs.get('style0',          'l'             )
    style1      = kwargs.get('style',           'l'             )
    stack       = kwargs.get('stack',           False           )
    textSize    = kwargs.get('stack',           legendTextSize  )
    
    if not hists: hists = histsB+histsS+histsD
    styleB      = 'f' if histsB else 'l'
    styleS      = 'l'
    styleD      = 'lep'
    
    if entries and hists and len(entries)!=len(hists):
      print error("makeLegend - %d=len(entries)!=len(hists)=%d !"%(len(entries),len(hists)))
    elif len(entries)==0:
      entries = [ h.GetTitle() for h in hists ]
    
    nLines = len(entries)+sum([e.count("newline") for e in entries])
    if title: nLines += 1 + title.count("newline")
    
    if width==0:  width  = 0.16
    if height==0: height = 1.0*textSize*nLines
    x2 = 0.90; x1 = x2 - width
    y2 = 0.92; y1 = y2 - height
    
    if position:
      if   "leftleft"     in position: x1 = 0.15;         x2 = x1 + width
      elif "rightright"   in position: x2 = 1 - 0.10;     x1 = x2 - width
      elif "centerright"  in position: x1 = 0.60-width/2; x2 = 0.60+width/2
      elif "centerleft"   in position: x1 = 0.48-width/2; x2 = 0.48+width/2
      elif "left"         in position: x1 = 0.18;         x2 = x1 + width
      elif "right"        in position: x2 = 1 - 0.15;     x1 = x2 - width
      elif "center"       in position: x1 = 0.55-width/2; x2 = 0.55+width/2
      if   "bottombottom" in position: y1 = 0.15;         y2 = y1 + height
      elif "bottom"       in position: y1 = 0.20;         y2 = y1 + height
      elif "toptop"       in position: y2 = 0.95;         y1 = y2 - height
      elif "top"          in position: y1 = 0.93;         y2 = y1 - height
    legend = TLegend(x1,y1,x2,y2)
    
    if transparent: legend.SetFillStyle(0) # 0 = transparent
    else: legend.SetFillColor(kWhite)
    legend.SetBorderSize(0)
    legend.SetTextSize(textSize)
    legend.SetTextFont(62) # bold for title
                   
    if title: legend.SetHeader(makeTitle(title))
    else:     legend.SetHeader("")
    legend.SetTextFont(42) # no bold for entries
    
    if hists:
      for hist, entry in zip( hists, entries ):
        style = style1
        if   hist in histsB: style = styleB
        elif hist in histsD: style = styleD
        elif hist in histsS: style = styleS
        elif i==0:           style = style0
        legend.AddEntry(hist,makeLatex(entry),style)
    
    legend.Draw()
    return legend
    


def makeAxes(frame, *args, **kwargs):
    """Make axis."""
    
    ratio       = False
    if isinstance(frame,Ratio):
      frame     = frame.frame
      ratio     = True
    
    args        = list(args)
    xmin        = frame.GetXaxis().GetXmin()
    xmax        = frame.GetXaxis().GetXmax()
    binning     = [ ]
    for arg in args[:]:
      if isinstance(arg,float) or isinstance(arg,int):
        binning.append(arg)
        args.remove(arg)
    if len(binning)>1:
        xmin, xmax = binning[:2]
    
    hists       = args
    hists.append(frame)
    ratio       = kwargs.get('ratio',           ratio               )
    negativeY   = kwargs.get('negativeY',       True                )
    ylabel      = kwargs.get('ylabel',          ""                  )
    xlabel      = makeLatex(kwargs.get('xlabel', frame.GetTitle())  )
    logy        = kwargs.get('logy',            False               )
    logx        = kwargs.get('logx',            False               )
    scale       = 1
    
    if ratio:
        scale = 2.6
    elif isinstance(frame,THStack):
        maxs = [ frame.GetMaximum() ]
        for hist in hists:
            maxs.append(hist.GetMaximum())
        #frame.SetMinimum(0)
        frame.SetMaximum(max(maxs)*1.15)
    else:
        mins = [ 0 ]
        maxs = [   ]
        for hist in hists:
            if negativeY: mins.append(hist.GetMinimum())
            maxs.append(hist.GetMaximum())
        frame.GetYaxis().SetRangeUser(min(mins),max(maxs)*1.14)
    frame.GetXaxis().SetRangeUser(xmin,xmax)
    
    if logy:
        #frame.SetMinimum(0.01)
        gPad.Update(); gPad.SetLogy()
    if logx:
        #frame.SetMinimum(0.01)
        gPad.Update(); gPad.SetLogx()
    
    if not ylabel:
        ylabel = "Events"
        #if "multiplicity" in xlabel: ylabel = "Events"
        #else: ylabel = ("Events / %.3f" % frame.GetXaxis().GetBinWidth(0)).rstrip("0").rstrip(".")
        #if "GeV" in xlabel: ylabel += " GeV"
    
    # Y axis
    # TODO: for Axis label https://root.cern.ch/root/roottalk/roottalk03/3375.html
    if ratio:
        ylabel = "ratio" #"data / M.C."
        frame.GetYaxis().SetTitle(ylabel)
        frame.GetYaxis().SetLabelSize(0.15)
        frame.GetYaxis().SetTitleSize(0.17)
        frame.GetYaxis().SetRangeUser(0.4,1.6)
        frame.GetYaxis().SetNdivisions(505)
        frame.GetYaxis().CenterTitle(True)
        frame.GetYaxis().SetTitleOffset(0.42)
    else:
        frame.GetYaxis().SetTitle(ylabel)
        frame.GetYaxis().SetLabelSize(0.056)
        frame.GetYaxis().SetTitleSize(0.068)
        frame.GetYaxis().SetTitleOffset(1.04)
    
    # X axis
    frame.GetXaxis().SetTitle(xlabel)
    frame.GetXaxis().SetLabelSize(0.060*scale)
    frame.GetXaxis().SetTitleSize(0.070*scale)
    frame.GetXaxis().SetTitleOffset(1.05)
    if kwargs.get('noxaxis',False): # e.g. for main plot above a ratio
        frame.GetXaxis().SetLabelSize(0)
        frame.GetXaxis().SetTitleSize(0)  
    #frame.GetYaxis().CenterTitle(True)
    frame.GetXaxis().SetNdivisions(510)
    #ROOT.gPad.SetTicks(1,1)
    #ROOT.gPad.SetGrid(1,1)


    
def symmetricYRange(self, frame, **kwargs):
    """Make symmetric Y range around some center value.
       Made for ratio plots with variable y axis."""
    
    center = kwargs.get('center',0) 
    min = center
    Max = center
    min_large = center
    Max_large = center
    
    for i in range(1,frame.GetNbinsX()+1):
        low = frame.GetBinContent(i) - frame.GetBinError(i)
        up  = frame.GetBinContent(i) + frame.GetBinError(i)
        if low and low < min:
             if center and low < min_large and low < center-center*2:
                 min_large = low
             else:
                 min = low
        if up  and up  > Max:
             if center and up  > Max_large and up  > center+center*2:
                 Max_large = up
             else:
                 Max = up
    
    if min is center and Max is center: # no Max, no min found
        if min_large < center: min = min_large
        else:  min = center - 0.3
        if Max_large > center: Max = Max_large
        else:  Max = center + 0.3
    
    width = max(abs(center-min),abs(Max-center))*1.10
    return [ center-width, center+width ]    




def setFillStyle(*hists,**kwargs):
    """Make fill style."""
    for i, hist in enumerate(hists):
        color0 = fillcolors[i%len(fillcolors)]
        hist.SetFillColor(color0)
    
def setLineStyle(*hists,**kwargs):
    """Make line color."""
    style        = kwargs.get('style',True)
    offset       = kwargs.get('offset',0)
    style_offset = kwargs.get('style_offset',0)+1
    if kwargs.get('noblack',True): offset += 1 # skip black
    colors0 = colors[offset:]
    if len(hists) is 0: hists = self.hists
    for i, hist in enumerate(hists):
        colori = colors0[i%len(colors0)]
        hist.SetLineColor(colori)
        if style: hist.SetLineStyle(style_offset+i%3)
        hist.SetLineWidth(2)
        if not isinstance(hist,TLine): hist.SetMarkerSize(0)

def setMarkerStyle(*hists,**kwargs):
    """Make marker style."""
    size         = kwargs.get('size',0.8)
    style        = kwargs.get('style',True)
    offset       = kwargs.get('offset',0)
    style_offset = kwargs.get('style_offset',0)+1
    if kwargs.get('noblack',False): offset += 1 # skip black
    colors0 = colors[offset:]
    for i, hist in enumerate(hists):
        colori = colors0[i%len(colors0)]
        hist.SetMarkerColor(colori)
        hist.SetLineColor(colori)
        if style: hist.SetLineStyle(style_offset+i%3)
        hist.SetMarkerStyle(20)
        hist.SetMarkerSize(size)
    
def setStatisticalErrorStyle(hist_error,**kwargs):
    """Set fill area style."""
    # https://root.cern.ch/doc/v608/classTAttFill.html#F2
    # 3001 small dots, 3003 large dots, 3004 hatched
    
    style = kwargs.get('style','hatched')
    if   style in 'hatched': style = 3004
    elif style in 'dots':    style = 3002
    elif style in 'cross':   style = 3013
    color = kwargs.get('color', kBlack)
    hist_error.SetLineStyle(1)
    hist_error.SetMarkerSize(0)
    hist_error.SetFillColor(color)
    hist_error.SetFillStyle(style)
    


def makeStatisticalError(hists,**kwargs):
    """Make histogram of statistical error for a set of histograms, or stack."""
    
    if isinstance(hists,THStack):    hists = [hists.GetStack.Last()]
    elif not isinstance(hists,list): hists = [hists]
    
    name        = kwargs.get('name',        "error_"+hists[0].GetName()     )
    title       = kwargs.get('title',       "stat. error"                   )
    color       = kwargs.get('color',       kBlack                          )
    verbosity   = kwargs.get('verbosity',   0                               )#False)
    (N, a, b)   = (hists[0].GetNbinsX(), hists[0].GetXaxis().GetXmin(),hists[0].GetXaxis().GetXmax())
    hist_error  = hists[0].Clone(name)
    hist_error.SetTitle(title)
    hist_error.Reset()
    #hist_error.Sumw2()
    
    for hist in hists:
        hist_error.Add(hist)
    
    if verbosity>1:
        printRow("bin","content","sqrt(content)","error",append=("  "+name),widths=[4,14],line="abovebelow")
        #for i, binc in enumerate(hist_error):
        #    printRow(i,binc,sqrt(binc),hist.GetBinError(i))
        for i in range(0,N+2):
            printRow(i,hist_error.GetBinContent(i),sqrt(hist_error.GetBinContent(i)),hist_error.GetBinError(i),widths=[4,14])
    
    setStatisticalErrorStyle(hist_error,color=color)
    hist_error.SetLineColor(hists[0].GetLineColor())
    hist_error.SetLineWidth(hists[0].GetLineWidth()) # Draw(E2 SAME)
    
    return hist_error
    



def makeAsymmErrorFromShifts(hist0,histsDown0,histsCentral0,histsUp0,hist_staterror,**kwargs):
    """Create asymmetric error from combining up and down shifts. Also include statistical
       error, if present. Formula:
          sqrt( (nominal - up shift)^2 + (nominal - down shift)^2 + statistical^2 )"""
    
    # CHECKS
    histsDown       = histsDown0[:]
    histsCentral    = histsCentral0[:]
    histsUp         = histsUp0[:]
    hist_JERCentral = kwargs.get('JERCentral',None)
    if isinstance(hist0,THStack):           hist0           = hist0.GetStack().Last()
    if isinstance(hist_JERCentral,THStack): hist_JERCentral = hist_JERCentral.GetStack().Last()
    if not isinstance(histsDown,list):      histsDown       = [histsDown]
    if not isinstance(histsCentral,list):   histsCentral    = [histsCentral]
    if not isinstance(histsUp,list):        histsUp         = [histsUp]
    for i, hist in enumerate(histsDown0):
        if isinstance(hist,THStack):        histsDown[i]    = hist.GetStack().Last()
    for i, hist in enumerate(histsCentral0):
        if isinstance(hist,THStack):        histsCentral[i] = hist.GetStack().Last()
    for i, hist in enumerate(histsUp0):
        if isinstance(hist,THStack):        histsUp[i]      = hist.GetStack().Last()
    if len(histsUp) != len(histsDown):
        LOG.warning("makeAsymmErrorFromShifts: len(histsUp) != len(histsDown)")
        exit(1)
    elif len(histsCentral) != len(histsUp):
        if len(histsCentral) == 1: histsCentral = [histsCentral]*len(histsUp)
        else:
            LOG.warning("makeAsymmErrorFromShifts: 1 != len(histsCentral) != len(histsUp) == len(histsDown)")
            exit(1)
    #if 'jes' not in histUp.GetName() or 'jes' not in histDown.GetName():
    #    LOG.warning("makeAsymmErrorFromShifts: JES histograms not matching!")
    
    # SETTINGS
    verbosity       = kwargs.get('verbosity',0)
    (N,a,b)         = (hist0.GetNbinsX(), hist0.GetXaxis().GetXmin(),hist0.GetXaxis().GetXmax())
    errors          = TGraphAsymmErrors()
    
    # CHECK BINNING
    check = histsUp+histsCentral+histsDown+[hist_staterror]
    if hist_JERCentral: check.append(hist_JERCentral)
    for hist in check:
        if verbosity>0: print ">>> makeAsymmErrorFromShifts: name = %s"%(hist.GetName())
        (N1,a1,b1) = (hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
        if N != N1 or a != a1 or b != b1 :
            LOG.warning("makeRatio: Binning between data (%d,%.1f,%.1f) and error (%s,%d,%.1f,%.1f) histogram is not the same!"%\
                  (N,a,b,N1,a1,b1,hist.GetTitle()))
    
    # CALCULATE BINNING
    if verbosity>0: printRow("bin","type","errDown2","errUp2","errDown_tot2","errUp_tot2","errDown_tot","errUp_tot",widths=[3,8,18,14],line="abovebelow")
    for i in range(0,N+2):
        biny = hist0.GetBinContent(i)
        binx = hist0.GetXaxis().GetBinCenter(i)
        errors.SetPoint(i,binx,biny)
        errorUp2   = 0
        errorDown2 = 0
        if hist_staterror:
            biny1 = hist_staterror.GetBinContent(i)
            if biny != biny1:
                LOG.warning("makeAsymmErrorFromShifts: "+\
                      "Bincontent hist0 (%.1f) and hist_staterror (%.1f) are not the same!" % (biny,biny1))
            errorUp2   += hist_staterror.GetBinError(i)**2
            errorDown2 += hist_staterror.GetBinError(i)**2
            if verbosity>0: printRow(i,"stat",hist_staterror.GetBinError(i),hist_staterror.GetBinError(i),errorDown2,errorUp2,widths=[3,8,18,14])
        for histUp, histCentral, histDown in zip(histsUp,histsCentral,histsDown):
            binyCentral = histCentral.GetBinContent(i)
            errorDown   = binyCentral-histDown.GetBinContent(i)
            errorUp     = binyCentral-histUp.GetBinContent(i)
            if binyCentral and 'nom' in histCentral.GetName().lower() and\
                               'jes' in histUp.GetName().lower() and 'jes' in histDown.GetName().lower(): #'jpt' in histCentral.GetName()    and
                ratioJERToNom = hist_JERCentral.GetBinContent(i)/binyCentral
                if verbosity>0: print ">>>   %12s scaling JES shift: JER pt / nominal pt = %.3f"%("",ratioJERToNom)
                errorDown = errorDown*ratioJERToNom
                errorUp   = errorUp  *ratioJERToNom
            
            if errorDown<0: errorUp2   += (errorDown)**2
            else:           errorDown2 += (errorDown)**2
            if errorUp<0:   errorUp2   += (errorUp)**2
            else:           errorDown2 += (errorUp)**2
            if verbosity>0: printRow("","shift",(errorDown)**2,(errorUp)**2,errorDown2,errorUp2,widths=[3,8,18,14])
            if verbosity>0: print ">>>   %12s %.2f=(%.4f-%.4f), %.2f=(%.4f-%.4f)" % ("",errorDown,binyCentral,histDown.GetBinContent(i),errorUp,binyCentral,histUp.GetBinContent(i))
        
        width = hist0.GetXaxis().GetBinWidth(i)/2
        if verbosity>0: printRow("","total","","",errorDown2,errorUp2,sqrt(errorDown2),sqrt(errorUp2),widths=[3,8,18,14],line="below")
        errors.SetPointError(i,width,width,sqrt(errorDown2),sqrt(errorUp2))
    
    setStatisticalErrorStyle(errors)
    errors.SetFillStyle(3004)
    errors.SetLineColor(hist0.GetLineColor())
    errors.SetFillColor(hist0.GetLineColor())
    errors.SetLineWidth(hist0.GetLineWidth())
    # Draw('2 SAME')
    
    return errors
    


def substractStackFromHist(stack,hist0,**kwargs):
    """Substract stacked MC histograms from a data histogram,
       bin by bin if the difference is larger than zero."""
    
    verbosity   = kwargs.get('verbosity',   0                       )
    name        = kwargs.get('name',        "diff_"+hist0.GetName() )
    title       = kwargs.get('title',       "difference"            )
    N, a, b     = hist0.GetNbinsX(), hist0.GetXaxis().GetXmin(), hist0.GetXaxis().GetXmax()
    hist_diff   = TH1D(name,title,N,a,b)
    stackhist   = stack.GetStack().Last()
    
    if verbosity>1:
        print ">>>\n>>> substractStackFromHist: %s - %s"%(name,title)
        print ">>>   (BC = \"bin content\", BE = \"bin error\")"
        print ">>>   %4s  %9s  %8s  %8s  %8s  %8s  %8s"%("bin","data BC","data BE","MC BC","MC BE","QCD BC","QCD BE")
    
    for i in range(1,N+1): # include overflow
        hist_diff.SetBinContent(i, max(0,hist0.GetBinContent(i)-stackhist.GetBinContent(i)))
        hist_diff.SetBinError(i,sqrt(hist0.GetBinError(i)**2+stackhist.GetBinError(i)**2))
        if verbosity>1:
          print ">>>   %4s  %9.1f  %8.2f  %8.2f  %8.2f  %8.2f  %8.2f"%(
                      i,hist0.GetBinContent(i),hist0.GetBinError(i),stackhist.GetBinContent(i),stackhist.GetBinError(i),
                                                                    hist_diff.GetBinContent(i),hist_diff.GetBinError(i))
    
    return hist_diff
    


def integrateStack(*args,**kwargs):
    """Integrate stack."""
    
    a, b = kwargs.get('a',0), kwargs.get('b',0)
    if   len(args) == 1:
        stack = args[0].GetStack().Last()
    elif len(args) == 3:
        stack = args[0].GetStack().Last()
        a = args[1]
        b = args[2]
        
    integral = 0
    if a < b: integral = stack.Integral(stack.FindBin(a), stack.FindBin(b))
    else:     integral = stack.Integral(stack.FindBin(b), stack.FindBin(a))
    return integral
    


def integrateHist(*args,**kwargs):
    """Integrate histogram."""
    
    a = kwargs.get('a',0)
    b = kwargs.get('b',0)
    if len(args) == 1:
        hist = args[0]
        if not a and not b: return hist.Integral()
    elif len(args) == 3:
        hist = args[0]
        a = args[1]
        b = args[2]
    else:
        LOG.warning("Could not integrate!")
        return 0
    
    integral = 0
    if a < b: integral = hist.Integral(hist.FindBin(a), hist.FindBin(b))
    else:     integral = hist.Integral(hist.FindBin(b), hist.FindBin(a))
    return integral
    


def norm(*hists,**kwargs):
    """ Normalize histogram."""
    if isinstance(hists[0],list): hists = hists[0]
    for hist in hists:
        I = hist.Integral()
        if I: hist.Scale(1/I)
        else: LOG.warning("norm: Could not normalize; integral = 0!")
    
def close(*hists,**kwargs):
    """ Close histograms."""
    verbosity = getVerbosity(kwargs,verbosityPlotTools) 
    if len(hists)>0 and (isinstance(hists,list) or isinstance(hists,tuple)):
      hists = hists[0]
    for hist in hists:
      if isinstance(hist,THStack):
        for subhist in hist.GetStack():
            if verbosity>1: print ">>> close: Deleting histogram %s from stack %s..."%(subhist.GetName(),hist.GetName())
            gDirectory.Delete(subhist.GetName())
        if verbosity>1: print ">>> close: Deleting stack %s..."%(hist.GetName())
        gDirectory.Delete(hist.GetName())
      else:
        if verbosity>1: print ">>> close: Deleting histogram %s..."%(hist.GetName())
        gDirectory.Delete(hist.GetName())
    


class Ratio(object):
    """Class to make bundle histograms (ratio, stat. error on MC and line) for ratio plot."""
    
    def __init__(self, hist0, *hists, **kwargs):
        """Make a ratio of two histograms bin by bin. Second hist may be a stack,
           to do data / MC stack."""
        
        self.ratios     = [ ]
        self.title      = kwargs.get('title',       "ratio"         )
        self.line       = kwargs.get('line',        True            )
        error0          = kwargs.get('error',       None            )
        staterror       = kwargs.get('staterror',   True            )
        
        if len(hists)<1:
            LOG.warning("Ratio::init: No histogram to compare with!")
        if isinstance(hist0,THStack):
            hist0 = hist0.GetStack().Last() # should have correct bin content and error
        for hist in hists:
            hist1       = hist.Clone("ratio_%s-%s"%(hist0.GetName(),hist.GetName()))
            hist1.SetTitle(self.title)
            hist1.Reset()
            self.ratios.append(hist1)
        self.ratio      = self.ratios[0]
        self.frame      = self.ratios[0]
        nBins           = hist0.GetNbinsX()
        
        self.error      = None
        if isinstance(error0,TGraphAsymmErrors):
            self.error  = error0.Clone()
        elif staterror:
            self.error  = TGraphAsymmErrors(nBins+2)
        
        #printRow("bin","data_bc","data_err","MC_bc","MC_err","ratio_bc","ratio_err","stat_bc","stat_err",widths=[4,11],line="abovebelow")
        #printRow("bin","error x","error y","errorDown","errorUp",widths=[4,11],line="abovebelow")
        for i in xrange(0,nBins+2):
          binc0 = hist0.GetBinContent(i)
          if binc0:
            for ratio, hist in zip(self.ratios,hists):
              binc1 = hist.GetBinContent(i)
              if binc1 and binc1/binc0 < 100:
                ratio.SetBinContent(i, binc1/binc0)
                ratio.SetBinError(i, hist.GetBinError(i)/binc0) # assume error on MC is 0
            if error0:
                x,y = Double(), Double()
                self.error.GetPoint(i,x,y)
                self.error.SetPoint(i,x,1)
                self.error.SetPointEYlow(i,error.GetErrorYlow(i)/binc0)
                self.error.SetPointEYhigh(i,error.GetErrorYhigh(i)/binc0)
            elif staterror:
                x     = hist0.GetXaxis().GetBinCenter(i)
                width = hist0.GetXaxis().GetBinWidth(i)
                self.error.SetPoint(i,x,1)
                self.error.SetPointError(i,width/2,width/2,hist0.GetBinErrorLow(i)/binc0,hist0.GetBinErrorUp(i)/binc0)
    
    
    def Draw(self, *option, **kwargs):
        """Draw all objects."""
        
        option      = option[0] if len(option)>0 else "E same"
        frame       = self.ratios[0]
        xmin        = frame.GetXaxis().GetXmin()
        xmax        = frame.GetXaxis().GetXmax()
        xmin        = kwargs.get('xmin',    xmin    )
        xmax        = kwargs.get('xmax',    xmax    )
        ymin        = kwargs.get('ymin',    0.4     )
        ymax        = kwargs.get('ymax',    1.6     )
        ylabel      = kwargs.get('ylabel',  "ratio" ) #"data / M.C."
        xlabel      = kwargs.get('xlabel',  ""      )
        size        = 1.0 #0.9
        
        frame.GetYaxis().SetTitle(ylabel)
        if xlabel:
            self.ratio.GetXaxis().SetTitle(xlabel)
        #frame.GetYaxis().SetLabelSize(0.10)
        #frame.GetXaxis().SetLabelSize(0.11)
        #frame.GetYaxis().SetTitleSize(0.12)
        #frame.GetXaxis().SetTitleSize(0.10)
        #frame.GetYaxis().CenterTitle(True)
        #frame.GetYaxis().SetTitleOffset(0.5)
        frame.GetXaxis().SetRangeUser(xmin,xmax)
        frame.GetYaxis().SetRangeUser(ymin,ymax)
        #frame.GetYaxis().SetNdivisions(505)
        #frame.SetNdivisions(505)
        frame.SetMarkerSize(size)
        frame.Draw(option+" AXIS")
        
        if self.error:
            setStatisticalErrorStyle(self.error,style='hatched')
            self.error.Draw('2 SAME')
        
        if self.line:
            self.line = TLine(xmin,1,xmax,1)
            self.line.SetLineColor(12) # dark grey
            self.line.SetLineStyle(2)
            self.line.Draw('SAME') # only draw line if a histogram has been drawn!
        
        frame.Draw(option)
    
    
    def close(self):
        """Delete the histograms."""
        for ratio in self.ratios:
          gDirectory.Delete(ratio.GetName())
        if self.error:
          gDirectory.Delete(self.error.GetName())
        if self.line:
          gDirectory.Delete(self.line.GetName())
        




class Plot(object):
    """Class to automatically make CMS plot.
    TODO:
    - allow for comparisons of histograms with/without ratio
    - compare two sets of histograms using same color set for each, but one with solid, on with dashed line"""
    
    def __init__(self, *hists, **kwargs):
        
        #if not isinstance(samples,SampleSet):
        #    LOG.warning("Plot::init - passed sample list is of type %s, not a SampleSet"%(type(samples)))

        self.verbosity          = getVerbosity(kwargs,verbosityPlotTools)
        variable, self.histsD, self.histsB, self.histsS = unwrapHistogramLists(*hists)
        self.weight             = kwargs.get('weight',             ""               )
        self.shift_QCD          = kwargs.get('shift_QCD',          0                )
        self.ratio_WJ_QCD_SS    = kwargs.get('ratio_WJ_QCD_SS',    0                )
        self.ratio_TT_QCD_SS    = kwargs.get('ratio_TT_QCD_SS',    0                )
        self.channel            = kwargs.get('channel',            "mutau"          )
        self.name               = kwargs.get('name',               "noname"         )
        self.title              = kwargs.get('title',              self.name        )
        
        frame = self.hists[0]
        if variable:
            self.var            = kwargs.get('var',                variable.name    )
            self.xmin           = kwargs.get('xmin',               variable.xmin    )
            self.xmax           = kwargs.get('xmax',               variable.xmax    )
            self.xlabel         = kwargs.get('xlabel',             variable.title   )
            self.logy           = kwargs.get('logy',               variable.logy    )
        else:
            self.var            = kwargs.get('var',                frame.GetXaxis().GetTitle() )
            self.xmin           = kwargs.get('xmin',               frame.GetXaxis().GetXmin() )
            self.xmax           = kwargs.get('xmax',               frame.GetXaxis().GetXmax() )
            self.xlabel         = kwargs.get('xlabel',             self.var         )
            self.logy           = kwargs.get('logy',               False            )
        self.ylabel             = kwargs.get('ylabel',             ""               )
        
        self.hist_error         = None
        self.error              = None
        self.ratio              = None
        self.stack              = kwargs.get('stack',              False            )
        self.reset              = kwargs.get('reset',              False            )
        self.split              = kwargs.get('split',              False            )
        self.signal             = kwargs.get('signal',             True             )
        self.background         = kwargs.get('background',         True             )
        self.data               = kwargs.get('data',               True             )
        self.ignore             = kwargs.get('ignore',             [ ]              )
        self.append             = kwargs.get('append',             ""               )
        #self.histsS, self.histsB, self.histsD = self.samples.createHistograms(self.variable,self.selection,**kwargs)
        #self.samples_dict
        
        self.canvas             = None
        self.frame              = frame
        self.legend             = None
        #self.width              = 0.08
        #self.height             = 0.05+0.05*(len(self.histsD)+len(self.histsB)+len(self.histsS))
        #self.x2 = 0.89; self.x1 = self.x2-self.width
        #self.y2 = 0.92; self.y1 = self.y2-self.height
        self.fillcolors         = fillcolors[:]
        self.colors             = colors[1:]
    
    @property
    def hists(self): return ( self.histsB + self.histsS + self.histsD )
    @hists.setter
    def hists(self, value): LOG.warning("Plot - no hists setter!")
    
    @property
    def histsMC(self): return ( self.histsB + self.histsS )
    @histsMC.setter
    def histsMC(self, value): LOG.warning("Plot - no hists setter!")
    
    
    def get(self,*labels,**kwargs):
        """Method to get all sample corresponding to some name."""
        return getSample(self.samples,*labels,**kwargs)
        
    
    def getHist(self,*labels,**kwargs):
        """Method to get hists corresponding to some name."""
        if kwargs.get('MC', False):
            return getHist(self.histsMC,*labels,**kwargs)
        else:
            return getHist(self.hists,*labels,**kwargs)
        
    
    def plot(self,*args,**kwargs):
        """Central method of Plot class: make plot with canvas, axis, error, ratio..."""
        
        # https://root.cern.ch/doc/master/classTHStack.html
        # https://root.cern.ch/doc/master/classTHistPainter.html#HP01e
        stack       = kwargs.get('stack',       False           ) or self.stack
        residue     = kwargs.get('residue',     False           ) and self.histsD
        ratio       = kwargs.get('ratio',       False           ) and self.histsD
        errorbars   = kwargs.get('errorbars',   False           )
        staterror   = kwargs.get('staterror',   False           )
        JEC_errors  = kwargs.get('JEC_errors',  False           )
        drawData    = kwargs.get('data',        True            ) and self.histsD
        drawSignal  = kwargs.get('signal',      True            ) and self.histsS
        norm        = kwargs.get('norm',        False           )
        title       = kwargs.get('title',       self.title      )
        ylabel      = kwargs.get('xlabel',      self.ylabel     )
        xlabel      = kwargs.get('xlabel',      self.xlabel     )
        legend      = kwargs.get('legend',      True            )
        position    = kwargs.get('position',    ""              )
        option      = 'hist' #+ kwargs.get('option', '')
        if errorbars: option = 'E0 '+option
        
        # CANVAS
        self.makeCanvas(square=kwargs.get('square', False),
                        residue=residue, ratio=ratio,
                        scaleleftmargin=kwargs.get('scaleleftmargin', 1),
                        scalerightmargin=kwargs.get('scalerightmargin', 1))
        # TODO: make frame
        
        # MONTE CARLO
        if stack:
            stack = THStack(makeHistName("stack",self.name),"")
            self.stack = stack
            self.frame = stack
            for hist in self.histsB: stack.Add(hist)
            stack.Draw(option)
            if drawSignal:
              for hist in self.histsS: hist.Draw(option+' SAME')
        else:
            for hist in self.histsMC: hist.Draw(option+' SAME')
        
        # DATA
        if drawData:
            for hist in self.histsD:
                hist.Draw('E SAME')
        
        # NORM
        if norm:
            norm(self.hists)
        
        # STYLE
        if stack:
            self.setFillStyle(*self.histsB)
            for hist in self.histsMC: hist.SetMarkerStyle(1)
        else:
            setLineStyle(*self.histsB)
        if self.histsD:
            setMarkerStyle(*self.histsD)
        if self.histsS:
            self.setLineStyle(*self.histsS)
        
        # STATISTICAL ERROR
        if staterror:
            self.hist_error = makeStatisticalError(self.histsB, name=makeHistName("stat_error",self.name),
                                                   title="statistical error")
            if stack and JEC_errors:
                self.error = self.makeErrorFromJECShifts(JEC=JEC_errors)
                self.error.Draw('E2 SAME')
            else:
                self.hist_error.Draw('E2 SAME')
        
        # AXES & LEGEND
        self.makeAxes(self.frame, *(self.histsB+self.histsD), xlabel=xlabel, noxaxis=ratio,
                       logy=kwargs.get('logy',False), logx=kwargs.get('logx',False))
        if legend:
            self.makeLegend(title=title, entries=kwargs.get('entries', [ ]),
                                         position=position)
        
        # CMS LUMI
        CMS_lumi.cmsTextSize  = 0.65
        CMS_lumi.lumiTextSize = 0.60
        CMS_lumi.relPosX      = 0.105
        CMS_lumi.CMS_lumi(self.canvas,13,0)
        
        # RATIO
        if ratio and stack and self.histsD:
            self.canvas.cd(2)
            self.ratio = Ratio(self.stack, self.histsD[0], staterror=staterror, error=self.error,
                                name=makeHistName("ratio",self.name))
            self.ratio.Draw('SAME')
            self.makeAxes(self.ratio, ylabel="ratio", xlabel=xlabel)
        
    
    def saveAs(self,filename,**kwargs):
        """Save plot, close canvas and delete the histograms."""
        
        save = kwargs.get('save',True)
        close = kwargs.get('close',True)
        printSameLine("")
        if save:
            self.canvas.SaveAs(filename)
            #self.canvas.SaveAs(filename.replace(".png",".pdf"))
            #if self.canvas_sigma:
                #self.canvas_sigma.SaveAs(filename.replace(".png","_eff.png"))
                #self.canvas_sigma.SaveAs(filename.replace(".png","_eff.pdf"))
        if close: self.close()
        
    
    def close(self):
        """Close canvas and delete the histograms."""
        
        if self.canvas:       self.canvas.Close()
        #if self.canvas_sigma: self.canvas_sigma.Close()
        for hist in self.hists:
            gDirectory.Delete(hist.GetName())
        if self.hist_error:
            gDirectory.Delete(self.hist_error.GetName())
        if self.ratio:
            self.ratio.close()
        
    
    def makeCanvas(self,**kwargs):
        """Make canvas and pads for ratio plots."""
        if kwargs.get('ratio',False):
            self.width = 0.25
        self.canvas = makeCanvas(**kwargs)
        
    
    def makeLegend(self,*args,**kwargs):
        """Make legend."""
        kwargs['histsD'] = self.histsD
        kwargs['histsB'] = self.histsB
        kwargs['histsS'] = self.histsS
        #kwargs['x1'],    kwargs['x2']     = self.x1,    self.x2
        #kwargs['y1'],    kwargs['y2']     = self.y1,    self.y2
        #kwargs['width'], kwargs['height'] = self.width, self.height
        self.legend = makeLegend(*args,**kwargs)
        
    
    def makeAxes(self, frame, *args, **kwargs):
        """Make axis."""
        makeAxes(frame,*args,**kwargs)
        
    
    
    def setLineStyle(self, *hists, **kwargs):
        """Make line style."""

        if len(hists) is 0: hists = self.hists
        gen = kwargs.get('gen', False)
        colors2 = self.colors
        
        if gen:
          line = [1,3,2,3]
          for i, hist in enumerate(hists):
            if hist.GetFillColor!=kBlack: continue
            hists[i].SetLineColor(colors2[i])
            hists[i].SetLineStyle(line[i%4])
            hists[i].SetLineWidth(3)
        else:
          for i, hist in enumerate(hists):
            if hist.GetFillColor!=kBlack: continue
            hists[i].SetLineColor(colors2[i%len(colors2)])
            hists[i].SetLineStyle(i%4+1)
            hists[i].SetLineWidth(3)
        
    
    
    def setFillStyle(self, *hists):
        """Make fill style."""
        if len(hists) is 0: hists = self.hists
        for i, hist in enumerate(hists):
            if hist.GetFillColor!=kBlack: continue
            print  "setFillStyle - hist \"%s\" has unset color!"
            color0 = self.fillcolors_dict.get(hist.GetName(),self.fillcolors[i%len(self.fillcolors)])
            hist.SetFillColor(color0)
        
    def makeErrorFromJECShifts(self,**kwargs):
        """Method to create a SF for a given var, s.t. the data and MC agree."""
        



class Plot2D(object):
    """Class to automatically make CMS plot."""
    
    def __init__(self, sample, var1, nBins1, a1, b1, var2, nBins2, a2, b2, **kwargs):
        self.sample     = sample
        self.var1       = var1
        self.nBins1     = nBins1
        self.a1         = a1
        self.b1         = b1
        self.var2       = var2
        self.nBins2     = nBins2
        self.a2         = a2
        self.b2         = b2
        self.cuts       = kwargs.get('cuts', "")
        self.weight     = kwargs.get('weight', "")
        self.canvas     = None
        self.legend     = None
        self.width  = 0.20; self.height = 0.08 + 0.05 * 1
        self.x2     = 0.95; self.x1 = self.x2 - self.width
        self.y1     = 0.48; self.y2 = self.y1 + self.height
        self.hist       = sample.hist2D(var1, nBins1, a1, b1, var2, nBins2, a2, b2, weight=self.weight, cuts=self.cuts)
        
    
    
    def plot(self,*args,**kwargs):
        """Central method of Plot class: make plot with canvas, axis, error, ratio..."""
        
        var1 = self.var1
        var2 = self.var2
        
        # CANVAS
        self.canvas = makeCanvas( square=kwargs.get('square', True),
                                  scaleleftmargin=kwargs.get('scaleleftmargin', 1.1),
                                  scalerightmargin=kwargs.get('scalerightmargin', 1)  )
        self.hist.SetTitle("")
        self.hist.Draw('colz')
        
        # STYLE
        # ...
        
        # AXES & LEGEND
        self.hist.GetYaxis().SetLabelSize(0.040)
        self.hist.GetYaxis().SetTitleSize(0.042)
        self.hist.GetXaxis().SetLabelSize(0.040)
        self.hist.GetXaxis().SetTitleSize(0.047)
        self.hist.GetXaxis().SetTitleOffset(1.1)
        self.hist.GetYaxis().SetTitleOffset(1.5)
        self.hist.GetYaxis().SetTitle(makeLatex(var1))
        self.hist.GetXaxis().SetTitle(makeLatex(var2))
        #self.legend = TLegend(0.90,0.75,0.50,0.90)
        #self.legend.AddEntry(prof,"average #DeltaR", 'l')
        #self.legend.SetTextSize(0.045)
        #self.legend.SetBorderSize(0)
        #self.legend.SetFillStyle(0)
        #self.legend.Draw()
        
        # CMS LUMI
        CMS_lumi.lumi_13TeV = "%s fb^{-1}" % luminosity
        CMS_lumi.cmsTextSize  = 0.65
        CMS_lumi.lumiTextSize = 0.60
        CMS_lumi.relPosX = 0.16
        CMS_lumi.CMS_lumi(self.canvas,13,0)
        
    
    
    def saveAs(self,filename):
        """Save plot, close canvas and delete the histograms."""
        
        printSameLine("")
        self.canvas.SaveAs(filename)
        self.close()
        
    
    
    def close(self):
        """Close canvas and delete the histograms."""
        
        if self.canvas: self.canvas.Close()
        if self.hist:   gDirectory.Delete(self.hist.GetName())
    


def isListOfHists(*args):
    """Help function to test if list of arguments is a list of histograms."""
    if not (isinstance(args,list) or isinstance(args,tuple)): return False
    for arg in args:
      if not isinstance(arg,TH1): return False
    return True
    
def unwrapHistogramLists(*args):
    """Help function to unwrap arguments for initialization of Plot object in order:
       1) variable, 2) data, 3), backgrounds, 4) signals."""
    
    args = list(args)
    variable = None
    varname  = ""
    binning  = [ ]
    for arg in args[:]:
      if isinstance(arg,Variable) and not variable:
        variable = arg
        args.remove(arg)
        break
      if isinstance(arg,str):
        varname = arg
        args.remove(arg)
      if isinstance(arg,float) or isinstance(arg,int):
        args.remove(arg)
        binning.append(arg)
    if not variable and len(binning)>2:
      variable(varname,*binning[:3])
    
    if isListOfHists(*args):
        return variable, [ ], args, [ ]
    if len(args)==1:
      if isListOfHists(*args[0]):
        return variable, [ ], args[0], [ ]
    if len(args)==2:
      if isinstance(args[0],TH1) and isListOfHists(*args[1]):
        return variable, [args[0]], args[1], [ ]
    if len(args)==3:
      if isinstance(args[0],TH1) and isListOfHists(*args[1]) and isListOfHists(*args[2]):
        return variable, [args[0]], args[1], args[2]
      if isListOfHists(*args[0]) and isListOfHists(*args[1]) and isListOfHists(*args[2]):
        return variable, args[0], args[1], args[2]
    print error("unwrapHistLists - Could not unwrap", args)
    exit(1)



from SampleTools import *
