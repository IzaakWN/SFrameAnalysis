#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

import os, re
#from ROOT import * #TFile, TCanvas, TH2D, TH2D, THStack, TAxis, TGaxis, TGraph...
from ROOT import TFile, TCanvas, TPad, TPaveText, TH1, TH1D, TLegend, TAxis, THStack, TGraph, TGraphAsymmErrors, TLine,\
                 TGaxis, gDirectory, gROOT, gPad, Double,\
                 kBlack, kGray, kWhite, kRed, kBlue, kGreen, kYellow,\
                 kAzure, kCyan, kMagenta, kOrange, kPink, kSpring, kTeal, kViolet,\
                 kSolid, kDashed, kDotted
import CMS_lumi, tdrstyle
from math import sqrt, pow, log, log10, floor, ceil
from SettingTools   import *
from SelectionTools import *
from VariableTools  import *
from PrintTools     import *

# CMS style
CMS_lumi.cmsText      = "CMS"
CMS_lumi.extraText    = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX      = 0.13
CMS_lumi.outOfFrame   = True
CMS_lumi.lumi_13TeV   = "%s fb^{-1}"%luminosity if luminosity else ""
tdrstyle.setTDRStyle()

# https://root.cern.ch/doc/master/classTColor.html
# http://imagecolorpicker.com/nl
# TColor::GetColor(R,B,G)
legendtextsize = 0.040
colors     = [ kRed+1, kAzure+5, kGreen+2, kOrange+1, kMagenta-4, kYellow+1,
               kRed-9, kAzure-4, kGreen-2, kOrange+6, kMagenta+3, kYellow+2 ]
fillcolors = [ kRed-2, kAzure+5,
               kMagenta-3, kYellow+771, kOrange-5,  kGreen-2,
               kRed-7, kAzure-9, kOrange+382,  kGreen+3,  kViolet+5, kYellow-2 ]
               #kYellow-3
styles     = [ kSolid, kDashed, kDotted ]

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    


def makeCanvas(**kwargs):
    """Make canvas and pads for ratio plots."""
    
    global luminosity
    square              = kwargs.get('square',              False       )
    scaleleftmargin     = kwargs.get('scaleleftmargin',     1.          )
    scalerightmargin    = kwargs.get('scalerightmargin',    1.          )
    scaletopmargin      = kwargs.get('scaletopmargin',      1.          )
    scalebottommargin   = kwargs.get('scaletopmargin',      1.          )
    pads                = kwargs.get('pads',                [ ]         ) # pass list as reference
    double              = kwargs.get('ratio', False ) or kwargs.get('residue', False )
    
    CMS_lumi.lumi_13TeV   = "%s, %s fb^{-1}"%(era,luminosity) if era else "%s fb^{-1}"%(luminosity) if luminosity else ""
    if not CMS_lumi.lumi_13TeV:
      scaletopmargin *= 0.7
    
    W = 800; H  = 600
    if square:
        W = 800; H  = 800
        scalerightmargin  *= 3.6
    elif double:
        W = 800; H  = 750
        #scaleleftmargin       *= 0.98
        #scalerightmargin      *= 0.64
        #scaletopmargin        *= 0.80
        #scalebottommargin     *= 0.92
        CMS_lumi.cmsTextSize   = 0.68
        CMS_lumi.lumiTextSize  = 0.64
        CMS_lumi.relPosX       = 0.10
    else:
        scaletopmargin        *= 1.1
        CMS_lumi.cmsTextSize   = 0.68
        CMS_lumi.lumiTextSize  = 0.64
        CMS_lumi.relPosX       = 0.12
    
    canvas = TCanvas("canvas","canvas",100,100,W,H)
    canvas.SetFillColor(0)
    canvas.SetFillStyle(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameBorderMode(0)
    
    if double:
        canvas.SetTopMargin(  0.0 ); canvas.SetBottomMargin( 0.0 )
        canvas.SetLeftMargin( 0.0 ); canvas.SetRightMargin(  0.0 )
        canvas.Divide(2)
        canvas.cd(1)
        gPad.SetPad("pad1","pad1", 0, 0.33, 1.0, 1.0)
        gPad.SetLeftMargin(0.128);  gPad.SetRightMargin(0.03)
        gPad.SetTopMargin(0.095);   gPad.SetBottomMargin(0.00001)
        gPad.SetFillColor(0) #SetFillColorAlpha(0,1.0)
        gPad.SetFillStyle(0) # 4000
        gPad.SetBorderMode(0)
        gPad.Draw()
        canvas.cd(2)
        gPad.SetPad("pad2","pad2", 0, 0.05, 1, 0.30)
        gPad.SetLeftMargin(0.128);  gPad.SetRightMargin(0.03)
        gPad.SetTopMargin(0.00001); gPad.SetBottomMargin(0.22)
        gPad.SetFillColor(0) #SetFillColorAlpha(0,1.0)
        gPad.SetFillStyle(0) # 4000
        gPad.SetBorderMode(0)
        gPad.Draw()
        canvas.cd(1)
    else:
        T, B = 0.08*scaletopmargin,  0.14*scalebottommargin
        L, R = 0.14*scaleleftmargin, 0.05*scalerightmargin
        canvas.SetTopMargin(  T ); canvas.SetBottomMargin( B )
        canvas.SetLeftMargin( L ); canvas.SetRightMargin(  R )
    
    return canvas
    


def makeLegend(*hists,**kwargs):
    """Make legend for a list of histograms."""
    
    global legendtextsize
    title       = kwargs.get('title',           ""                  )
    entries     = kwargs.get('entries',         [ ]                 )
    position    = kwargs.get('position',        ""                  ).lower()
    transparent = kwargs.get('transparent',     False               )
    histsB      = kwargs.get('histsB',          [ ]                 )
    histsS      = kwargs.get('histsS',          [ ]                 )
    histsD      = kwargs.get('histsD',          [ ]                 )
    errorband   = kwargs.get('error',           None                )
    errortitle  = kwargs.get('errortitle',      errorband.GetTitle() if errorband else "" )
    x1          = kwargs.get('x1',              0                   )
    x2          = kwargs.get('x2',              0                   )
    y1          = kwargs.get('y1',              0                   )
    y2          = kwargs.get('y2',              0                   )
    width       = kwargs.get('width',           -1                  )
    height      = kwargs.get('height',          -1                  )
    style0      = kwargs.get('style0',          'l'                 )
    style1      = kwargs.get('style',           'l'                 )
    stack       = kwargs.get('stack',           False               )
    textsize    = kwargs.get('textsize',        legendtextsize      )
    text        = kwargs.get('text',            ""                  )
    
    if not hists: hists = histsD+histsB+histsS
    styleB      = 'f' if histsB and histsD else 'l'
    styleS      = 'l'
    styleD      = 'lep'
    if not isList(text): text = [ text ]
    
    if title=="noname": title = ""
    
    if entries and hists and len(entries)!=len(hists):
      LOG.error("makeLegend - %d=len(entries)!=len(hists)=%d !"%(len(entries),len(hists)))
      while len(entries)<len(hists):
        entries.append(hists[len(entries)-1].GetTitle())
    elif len(entries)==0:
      entries = [ h.GetTitle() for h in hists ]
    
    # count number of lines in legend
    nLines = len(entries)+sum([e.count("splitline") for e in entries])
    if title: nLines += 1 + title.count("splitline")
    else:     nLines += 0.80
    if text:  nLines += 1 + text.count("splitline")
    
    # set default width, height and
    if width<0:  width  = 0.22 if textsize>legendtextsize else 0.20
    if height<0: height = 1.10*textsize*nLines
    x2 = 0.86-gPad.GetRightMargin(); x1 = x2 - width
    y2 = 0.96-gPad.GetTopMargin();   y1 = y2 - height
    
    if position:
      if   'leftleft'     in position: x1 = 0.02+gPad.GetLeftMargin();   x2 = x1 + width
      elif 'rightright'   in position: x2 = 0.92-gPad.GetRightMargin();  x1 = x2 - width
      elif 'center'  in position:
        if 'right'  in position: center = (1+gPad.GetLeftMargin()-gPad.GetRightMargin())/2 + 0.06
        elif 'left' in position: center = (1+gPad.GetLeftMargin()-gPad.GetRightMargin())/2 - 0.06
        else:                    center = (1+gPad.GetLeftMargin()-gPad.GetRightMargin())/2
        x1 = center-width/2; x2 = center+width/2
      elif 'left'         in position: x1 = 0.08+gPad.GetLeftMargin();   x2 = x1 + width
      elif 'right'        in position: x2 = 0.85-gPad.GetRightMargin();  x1 = x2 - width
      if   'bottombottom' in position: y1 = 0.02+gPad.GetBottomMargin(); y2 = y1 + height
      elif 'bottom'       in position: y1 = 0.08+gPad.GetBottomMargin(); y2 = y1 + height
      elif 'toptop'       in position: y2 = 0.98-gPad.GetTopMargin();    y1 = y2 - height
      elif 'top'          in position: y1 = 0.95-gPad.GetTopMargin();    y2 = y1 - height
    #y1 += yoffset; y2 += yoffset
    legend = TLegend(x1,y1,x2,y2)
    legend.SetMargin(0.20)
    
    if transparent: legend.SetFillStyle(0) # 0 = transparent
    else: legend.SetFillColor(kWhite)
    legend.SetBorderSize(0)
    legend.SetTextSize(textsize)
    legend.SetTextFont(62) # bold for title
    
    if title:
      legend.SetHeader(makeTitle(title))
      #if len(title)<30:
      #  legend.SetHeader(makeTitle(title))
      #else: # split
      #  title = makeTitle(title)
      #  part1 = title[:len(title)/2]
      #  part2 = title[len(title)/2:]
      #  if   ' ' in part2: i = len(part1)+part2.find(' ')
      #  elif ' ' in part1: i = part1.rfind(' ')
      #  else:              i = len(title)
      #  print i
      #  print title[:i]
      #  print title[i+2:]
      #  legend.SetHeader(title[:i])
      #  if i<len(tit   le): legend.AddEntry(0,title[i+1:],'')
    else:
      legend.SetHeader("")
    legend.SetTextFont(42) # no bold for entries
    
    if hists:
      for hist, entry in zip( hists, entries ):
        style = style1
        if   hist in histsB: style = styleB
        elif hist in histsD: style = styleD
        elif hist in histsS: style = styleS
        elif i==0:           style = style0
        legend.AddEntry(hist,makeTitle(entry),style)
    if errorband:
      legend.AddEntry(errorband,errortitle,'f')
    for line in text:
      legend.AddEntry(0,makeTitle(line),'')
    
    legend.Draw()
    return legend
    

def createFile(filename,**kwargs):
    verbosity  = kwargs.get('verbosity', 1                  )
    name       = kwargs.get('name',      "histograms.root"  )
    option     = kwargs.get('option',    'RECREATE'         )
    text       = kwargs.get('text',      ""                 )
    title      = kwargs.get('title',     ""                 )
    canvasname = kwargs.get('canvas',    "selection"        )
    file       = TFile(filename,option)
    if verbosity>0:
      print ">>> created file with histograms: %s"%(file.GetName())
    if text:
      canvas, pave = canvasWithText(text,title=title)
      canvas.Write(canvasname)
    return file


def canvasWithText(*lines,**kwargs):
    title  = kwargs.get('title', "" )
    name   = kwargs.get('name',  "" )
    canvas = TCanvas(name,"canvas",100,100,1000,300)
    pave = TPaveText(0.05,0.1,0.95,0.9)
    pave.SetTextFont(82)
    pave.SetTextSize(0.08)
    if title:
      pave.AddText(title)
      pave.GetListOfLines().Last().SetTextFont(62)
      pave.GetListOfLines().Last().SetTextSize(0.11)
    for line in lines:
      pave.AddText(line)
    pave.Draw()
    return canvas, pave
    

    
def makeAxes(frame, *args, **kwargs):
    """Make axis for for a simple plot or the main pad of ratio plot."""
    
    if isinstance(frame,Ratio):
      return makeAxesRatio(frame, *args, **kwargs)
    
    args         = list(args)
    xmin         = frame.GetXaxis().GetXmin()
    xmax         = frame.GetXaxis().GetXmax()
    ymin, ymax   = None, None
    binning      = [ ]
    for arg in args[:]:
      if isNumber(arg):
        binning.append(arg)
        args.remove(arg)
    if len(binning)>1:
        xmin, xmax = binning[:2]
    
    hists          = args
    hists.append(frame)
    main           = kwargs.get('main',            False              ) # main pad in ratio plot
    xmin           = kwargs.get('xmin',            xmin               )
    xmax           = kwargs.get('xmax',            xmax               )
    ymin           = kwargs.get('ymin',            ymin               )
    ymax           = kwargs.get('ymax',            ymax               )
    ymargin        = kwargs.get('ymargin',         1.16               )
    negativeY      = kwargs.get('negativeY',       True               )
    xlabel         = makeLatex(kwargs.get('xlabel', frame.GetTitle()) )
    ylabel         = kwargs.get('ylabel',          ""                 )
    logx           = kwargs.get('logx',            False              )
    logy           = kwargs.get('logy',            False              )
    ycenter        = kwargs.get('center',          False              )
    
    if main:
      xlabelsize   = kwargs.get('xlabelsize',     0.0                 )
      xtitlesize   = kwargs.get('xtitlesize',     0.0                 )
      ylabelsize   = kwargs.get('ylabelsize',     0.056               )
      ytitlesize   = kwargs.get('ytitlesize',     0.068               )
      ytitleoffset = kwargs.get('ytitleoffset',   1.01                )
    else:
      xlabelsize   = kwargs.get('xlabelsize',     0.050               )
      xtitlesize   = kwargs.get('xtitlesize',     0.060               )
      ylabelsize   = kwargs.get('ylabelsize',     0.050               )
      ytitlesize   = kwargs.get('ytitlesize',     0.060               )
      ytitleoffset = kwargs.get('ytitleoffset',   1.25                )
    
    if isinstance(frame,THStack):
        maxs = [ frame.GetMaximum() ]
        for hist in hists:
            maxs.append(hist.GetMaximum())
        if not ymax: ymax = ceilToSignificantDigit(max(maxs)*ymargin,digits=2)
    else:
        mins = [ 0 ]
        maxs = [   ]
        for hist in hists:
            if negativeY: mins.append(hist.GetMinimum())
            maxs.append(hist.GetMaximum())
        if not ymin: ymin = min(mins)*(1.1 if ymin>0 else 0.9)
        if not ymax: ymax = ceilToSignificantDigit(max(maxs)*ymargin,digits=2)
    frame.GetXaxis().SetRangeUser(xmin,xmax)
    if ymin: frame.SetMinimum(ymin)
    if ymax: frame.SetMaximum(ymax)
    
    if logy:
      #if ymin==0: ymin = min(0.1,10**(magnitude(ymax)-3))
      gPad.Update(); gPad.SetLogy()
    if logx:
      #if xmin==0: xmin = min(0.1,10**(magnitude(xmax)-3))
      gPad.Update(); gPad.SetLogx()
    
    if not ylabel:
      ylabel = "Events"
      #if "multiplicity" in xlabel: ylabel = "Events"
      #else: ylabel = ("Events / %.3f" % frame.GetXaxis().GetBinWidth(0)).rstrip("0").rstrip(".")
      #if "GeV" in xlabel: ylabel += " GeV"
    
    # X axis
    frame.GetXaxis().SetLabelSize(xlabelsize)
    frame.GetXaxis().SetTitleSize(xtitlesize)
    frame.GetXaxis().SetTitleOffset(1.02)
    frame.GetXaxis().SetNdivisions(510)
    frame.GetXaxis().SetTitle(xlabel)
    #gPad.SetTicks(1,1)
    #gPad.SetGrid(1,1)
    
    # Y axis
    if ycenter:
      frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetLabelSize(ylabelsize)
    frame.GetYaxis().SetTitleSize(ytitlesize)
    frame.GetYaxis().SetTitleOffset(ytitleoffset)
    frame.GetYaxis().SetTitle(ylabel)
    TGaxis.SetExponentOffset(-0.074,0.005,'y')
    
    return xmin, xmax, ymin, ymax
    
def makeAxesRatio(frame, *args, **kwargs):
    """Make axis for ratio pad."""
    
    if isinstance(frame,Ratio):
      frame     = frame.frame
    
    args        = list(args)
    xmin        = frame.GetXaxis().GetXmin()
    xmax        = frame.GetXaxis().GetXmax()
    binning     = [ ]
    for arg in args[:]:
      if isNumber(arg):
        binning.append(arg)
        args.remove(arg)
    if len(binning)>1:
        xmin, xmax = binning[:2]
    
    xmin        = kwargs.get('xmin',            xmin                )
    xmax        = kwargs.get('xmax',            xmax                )
    ymin        = kwargs.get('ymin',            0.5                 )
    ymax        = kwargs.get('ymax',            1.5                 )
    ratiorange  = kwargs.get('ratiorange',      0.0                 ) 
    xlabel      = makeLatex(kwargs.get('xlabel', frame.GetTitle())  )
    ylabel      = kwargs.get('ylabel',          "ratio"             ) #"data / M.C."
    logx        = kwargs.get('logx',            False               )
    logy        = kwargs.get('logy',            False               )
    
    if ratiorange:
      ymin, ymax = 1-ratiorange, 1+ratiorange
    if logy:
      #if ymin==0: ymin = min(0.1,10**(magnitude(ymax)-3))
      gPad.Update(); gPad.SetLogy()
    if logx:
      #if xmin==0: xmin = min(0.1,10**(magnitude(xmax)-3))
      gPad.Update(); gPad.SetLogx()
    
    # X axis
    frame.GetXaxis().SetTitle(xlabel)
    frame.GetXaxis().SetLabelSize(0.156)
    frame.GetXaxis().SetTitleSize(0.182)
    frame.GetXaxis().SetTitleOffset(1.02)
    #frame.GetYaxis().CenterTitle(True)
    #gPad.SetTicks(1,1)
    #gPad.SetGrid(1,1)
    frame.GetXaxis().SetNdivisions(510)
    frame.GetXaxis().SetRangeUser(xmin,xmax)
    
    # Y axis
    frame.GetYaxis().SetRangeUser(ymin,ymax)
    frame.GetYaxis().SetLabelSize(0.15)
    frame.GetYaxis().SetTitleSize(0.17)
    frame.GetYaxis().SetNdivisions(505)
    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitleOffset(0.40)
    frame.GetYaxis().SetTitle(ylabel)
    
    return xmin, xmax, ymin, ymax
    

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
    
def roundToSignificantDigit(x,digits=1,multiplier=1):
    """Round off number x to first signicant digit."""
    x = float(x)/multiplier
    precision = (digits-1)-magnitude(x)
    if multiplier!=1 and int(x*10**precision)==1: precision += 1
    return multiplier*round(x,precision)
    
def ceilToSignificantDigit(x,digits=1,multiplier=1):
    """Round up number x to first signicant digit."""
    if x==0: return 0
    x = float(x)
    e = int(floor(log(abs(x),10)))-(digits-1)
    if multiplier>1: e = e - ceil(log(multiplier,10))
    return ceil(x/multiplier/(10.**e))*(10.**e)*multiplier

def magnitude(x):
    """Get magnitude of a number. E.g. 45 is 2, 2304 is 4, 0.84 is -1"""
    if x==0: return 0
    return int(floor(log(abs(x),10)))

def findClosestDivisor(n,m):
   """Find divisor of n that is closest to m."""
   if m>n:    return n
   if n%round(m)==0: return m
   xlow = round(m)
   xup  = round(m)
   while xup<n:
     xup += 1
     if n%xup==0: break
   while 0<xlow:
     xlow -= 1
     if n%xlow==0: break
   if m-xlow>=xup-m:
     return int(xup)
   return int(xlow)

def symmetricYRange(self, frame, **kwargs):
    """Make symmetric y-range around some center value.
       Made for ratio plots with variable y-axis."""
    
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
    

def getTGraphYRange(graph,ymin=+999989,ymax=-999989):
    """Get full y-range of a given TGraph object."""
    N = graph.GetN()
    x, y = Double(), Double()
    for i in xrange(0,N):
      graph.GetPoint(i,x,y)
      yup  = y+graph.GetErrorYhigh(i)
      ylow = y-graph.GetErrorYlow(i)
      if yup >ymax: ymax = yup
      if ylow<ymin: ymin = ylow
    return (ymin,ymax)


def rebin(hist,nbins,*args):
    """Smart (?) rebinning of a histogram."""
    bins   = [a for a in args if isNumber(a)]
    nbins0 = hist.GetNbinsX()
    xmin0  = hist.GetXaxis().GetXmin()
    xmax0  = hist.GetXaxis().GetXmax()
    factor = -1
    
    if len(bins)==2 and (xmin0!=bins[0] or xmax0!=bins[1]):
      xmin, xmax = bins[0], bins[1]
      width      = float(xmax-xmin)/nbins
      width0     = float(xmax0-xmin0)/nbins0 
      if width0>width:
        LOG.warning("rebin: Cannot rebin: new binning (%s,%s,%s) with bin width (%.2f) < old bin width (%.2f) from binning (%s,%s,%s)"%(nbins,xmin,xmax,width,width0,nbins0,xmin0,xmax0))
      else:
        nbins1   = float(xmax0-xmin0)/width
        factor   = float(nbins0)/nbins1
        if nbins0%nbins1!=0:
          factor = findClosestDivisor(nbins0,factor)
          LOG.warning("rebin: old bin width (%.2f) from binning (%s,%s,%s) is not a divisor of new width (%.2f) from new binning (%s,%s,%s) -> rounded to %d"%(width0,nbins0,xmin0,xmax0,width,nbins,xmin,xmax,factor))
        hist.Rebin(int(factor))
        hist.GetXaxis().SetRangeUser(xmin,xmax)
    else:
      if nbins>nbins0:
        LOG.warning("rebin: Cannot rebin: new nbins (%d) > old nbins (%d)"%(nbins,nbins0))
      else:
        factor = float(nbins0)/nbins
        if nbins0%nbins!=0:
          factor = findClosestDivisor(nbins0,factor)
          LOG.warning("rebin: new nbins (%d) is not a divisor of old nbins (%d) -> rounded to %d"%(nbins,nbins0,factor))
        hist.Rebin(int(factor))
    return factor
    


def setFillStyle(*hists,**kwargs):
    """Set the fill style for a list of histograms."""
    global fillcolors
    fillcolors0 = kwargs.get('colors', fillcolors )
    for i, hist in enumerate(hists):
        color0 = fillcolors0[i%len(fillcolors0)]
        hist.SetFillColor(color0)

def setLineStyle(*hists,**kwargs):
    """Set the line style for a list of histograms."""
    global colors, styles
    colors0      = kwargs.get('colors',         colors  )
    style        = kwargs.get('style',          True    )
    width        = kwargs.get('width',          2       )
    offset       = kwargs.get('offset',         0       )
    style_offset = kwargs.get('style_offset',   0       )
    for i, hist in enumerate(hists):
        hist.SetFillColor(0)
        hist.SetLineColor(colors0[i%len(colors0)])
        if style: hist.SetLineStyle(styles[i%len(styles)])
        hist.SetLineWidth(width)
        if not isinstance(hist,TLine): hist.SetMarkerSize(0)

def setMarkerStyle(*hists,**kwargs):
    """Set the marker style for a list of histograms."""
    global colors
    colors0      = kwargs.get('colors',         colors  )
    size         = kwargs.get('size',           0.6     )
    style        = kwargs.get('style',          True    )
    offset       = kwargs.get('offset',         0       )
    style_offset = kwargs.get('style_offset',   0       )
    for i, hist in enumerate(hists):
        color = colors0[i%len(colors0)]
        hist.SetMarkerColor(color)
        hist.SetLineColor(color)
        hist.SetMarkerStyle(20)
        hist.SetMarkerSize(size)

def setErrorBandStyle(hist_error,**kwargs):
    """Set the error band style for a histogram."""
    # https://root.cern.ch/doc/v608/classTAttFill.html#F2
    # 3001 small dots, 3003 large dots, 3004 hatched
    
    color = kwargs.get('color',     kBlack      )
    style = kwargs.get('style',     'hatched'   )
    if   style in 'hatched': style = 3004
    elif style in 'dots':    style = 3002
    elif style in 'cross':   style = 3013
    hist_error.SetLineStyle(1)
    hist_error.SetMarkerSize(0)
    hist_error.SetLineColor(kWhite)
    hist_error.SetFillColor(color)
    hist_error.SetFillStyle(style)
    


def makeErrorBand(hists,**kwargs):
    """Make an error band histogram for a list of histograms, or stack."""
    
    if isinstance(hists,THStack): hists = [hists.GetStack.Last()]
    elif not isList(hists):       hists = [hists]
    
    name        = kwargs.get('name',        "error_"+hists[0].GetName() )
    title       = kwargs.get('title',       "stat. error"               )
    color       = kwargs.get('color',       kBlack                      )
    verbosity   = kwargs.get('verbosity',   0                           )
    (N, a, b)   = (hists[0].GetNbinsX(), hists[0].GetXaxis().GetXmin(),hists[0].GetXaxis().GetXmax())
    hist_error  = hists[0].Clone(name)
    hist_error.SetTitle(title)
    hist_error.Reset()
    #hist_error.Sumw2()
    
    for hist in hists:
        hist_error.Add(hist)
    
    if verbosity>1:
        printRow("bin","content","sqrt(content)","error",append=("  "+name),widths=[4,14],line="abovebelow")
        for i in range(0,N+2):
            printRow(i,hist_error.GetBinContent(i),sqrt(hist_error.GetBinContent(i)),hist_error.GetBinError(i),widths=[4,14])
    
    setErrorBandStyle(hist_error,color=color)
    #hist_error.SetLineColor(hists[0].GetLineColor())
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
    if not isList(histsDown):               histsDown       = [histsDown]
    if not isList(histsCentral):            histsCentral    = [histsCentral]
    if not isList(histsUp):                 histsUp         = [histsUp]
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
    
    setErrorBandStyle(errors)
    errors.SetFillStyle(3004)
    errors.SetLineColor(hist0.GetLineColor())
    errors.SetFillColor(hist0.GetLineColor())
    errors.SetLineWidth(hist0.GetLineWidth())
    # Draw('2 SAME')
    
    return errors
    


def groupHistsInList(hists,searchterms,name,title,**kwargs):
    """Group histograms in a list, returns list of histograms."""
    
    searchterms = ensureList(searchterms)
    hists_matched = getHist(hists,*searchterms)
    if not hists_matched:
      LOG.warning("groupHistsInList: No matched histograms") 
      return hists
    hindex = hists.index(hists_matched[0])
    
    histsum = hists_matched[0].Clone(name)
    histsum.SetTitle(title)
    for i, hist in enumerate(hists_matched):
      if i>0: histsum.Add(hist)
      hists.remove(hist)
    hists.insert(hindex,histsum)
    
    return hists
    
def groupHists(*args,**kwargs):
    """Find histograms corresponding to some search term, return the sum histgram."""
    
    strings     = [ ]
    hists       = [ ]
    searchterms = [ ]
    
    for arg in args:
      if isinstance(a,str):
        strings.append(arg)
      elif isinstance(a,TH1):
        hists.append(arg)
      elif isListOfHists(arg):
        hists = arg
      elif isList(arg) and not any(not isinstance(s,str) for s in arg):
        searchterms = arg
    
    if not hists:
      LOG.warning("groupHists - Could not group histograms, because none are given!")
    name        = strings[0] if len(strings)>0 else hists[0].GetName()
    title       = strings[1] if len(strings)>1 else hists[0].GetTitle()
    if len(strings)>2:
      searchterms = [ strings[2] ]
    
    verbosity   = kwargs.get('verbosity',   0             )
    name        = kwargs.get('name',        name          )
    title       = kwargs.get('title',       title         )
    
    hists_matched = getHist(hists,*searchterms) if searchterms else hists
    histsum     = hists_matched[0].Clone(name)
    histsum.SetTitle(title)
    for hist in hists_matched[1:]: histsum.Add(hist)
    return histsum

def getHist(hists,*searchterms,**kwargs):
    """Help function to get all histograms corresponding to some name and optional searchterm."""
    matches   = [ ]
    unique    = kwargs.get('unique',      False   )
    regex     = kwargs.get('regex',       False   )
    exclusive = kwargs.get('excl',        False   )
    for hist in hists:
      yes = True
      for searchterm in searchterms:
        if not regex:
          searchterm = re.sub(r"(?<!\\)\+",r"\+",  searchterm) # replace + with \+
          searchterm = re.sub(r"([^\.])\*",r"\1.*",searchterm) # replace * with .*
        yes = yes and re.search(searchterm,hist.GetName())
        if yes and not exclusive: break
        elif not yes: break
      if yes: matches.append(hist)
    if not matches:
      LOG.warning("Could not find a sample with search terms %s..." % (', '.join(searchterms)))
    elif unique:
      if len(matches)>1: LOG.warning("Found more than one match to %s. Using first match only: %s" % (", ".join(searchterms),", ".join([h.name for h in matches])))
      return matches[0]
    return matches
    


def substractStackFromHist(stack,hist0,**kwargs):
    """Substract stacked MC histograms from a data histogram,
       bin by bin if the difference is larger than zero."""
    
    verbosity   = kwargs.get('verbosity',   0                       )
    name        = kwargs.get('name',        "diff_"+hist0.GetName() )
    title       = kwargs.get('title',       "difference"            )
    N, a, b     = hist0.GetNbinsX(), hist0.GetXaxis().GetXmin(), hist0.GetXaxis().GetXmax()
    hist_diff   = TH1D(name,title,N,a,b)
    stackhist   = stack.GetStack().Last() if isinstance(stack,THStack) else stackhist
    
    if verbosity>1:
        print ">>>\n>>> substractStackFromHist: %s - %s"%(name,title)
        print '>>>   (BC = "bin content", BE = "bin error")'
        print ">>>   %4s  %9s  %8s  %8s  %8s  %8s  %8s"%("bin","data BC","data BE","MC BC","MC BE","QCD BC","QCD BE")
    
    for i in range(1,N+1): # include overflow
        hist_diff.SetBinContent(i, max(0,hist0.GetBinContent(i)-stackhist.GetBinContent(i)))
        hist_diff.SetBinError(i,sqrt(hist0.GetBinError(i)**2+stackhist.GetBinError(i)**2))
        if verbosity>1:
          print ">>>   %4s  %9.1f  %8.2f  %8.2f  %8.2f  %8.2f  %8.2f"%(
                      i,hist0.GetBinContent(i),hist0.GetBinError(i),stackhist.GetBinContent(i),stackhist.GetBinError(i),
                                                                    hist_diff.GetBinContent(i),hist_diff.GetBinError(i))
    
    return hist_diff
    
def substractHistsFromData(histD,*hists,**kwargs):
    """Substract MC histograms from a data histogram."""
    if len(hists)>0 and isinstance(hists[0],list): hists = hists[0]
    name        = hists[0].GetName() if len(hists)>0 else ""
    verbosity   = kwargs.get('verbosity',   0              )
    name        = kwargs.get('name',        "diff_"+name   )
    title       = kwargs.get('title',       "difference"   )
    allowneg    = kwargs.get('allowneg',    False          )
    
    hist_diff = hists[0].Clone(name)
    hist_diff.Reset()
    hist_diff.SetTitle(title)
    hist_diff.Add(histD)
    hist_diff.SetOption('HIST')
    for hist in hists:
      hist_diff.Add(hist,-1)
    
    if not allowneg:
      for i, bin in enumerate(hist_diff):
        if bin<0.0:
          hist_diff.SetBinContent(i,0)
        #print ">>> %4d - %5.1f +/- %4.1f"%(i,hist_diff.GetBinContent(i),hist_diff.GetBinError(i))
    
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
    """Normalize histogram."""
    if isList(hists[0]): hists = hists[0]
    for hist in hists:
        I = hist.Integral()
        if I: hist.Scale(1/I)
        else: LOG.warning("norm: Could not normalize; integral = 0!")
    
def close(*hists,**kwargs):
    """Close histograms."""
    verbosity = getVerbosity(kwargs,verbosityPlotTools)
    if len(hists)>0 and isList(hists):
      hists = hists[0]
    for hist in hists:
      if isinstance(hist,THStack):
        if verbosity>1: print '>>> close: Deleting histograms from stack "%s"...'%(hist.GetName())
        for subhist in hist.GetStack():
          deleteHist(subhist,**kwargs)
        deleteHist(hist,**kwargs)
      else:
        deleteHist(hist,**kwargs)
    
def deleteHist(*hists,**kwargs):
    """Completely remove histograms from memory."""
    verbosity = getVerbosity(kwargs,verbosityPlotTools) 
    for hist in hists:
      if verbosity>1: print '>>> deleteHist: deleting histogram "%s"'%(hist.GetName())
      gDirectory.Delete(hist.GetName())
      del hist
    


class Ratio(object):
    """Class to make bundle histograms (ratio, stat. error on MC and line) for ratio plot."""
    
    def __init__(self, hist0, *hists, **kwargs):
        """Make a ratio of two histograms bin by bin. Second hist may be a stack,
           to do data / MC stack."""
        
        self.ratios     = [ ]
        self.error      = None
        self.title      = kwargs.get('title',       "ratio"         )
        self.line       = kwargs.get('line',        True            )
        self.drawZero   = kwargs.get('drawZero',    True            ) # draw ratio of two zero bins as 1
        error0          = kwargs.get('error',       None            )
        staterror       = kwargs.get('staterror',   True            )
        denominator     = kwargs.get('denominator', -1              )
        
        if len(hists)==0:
            LOG.warning("Ratio::init: No histogram to compare with!")
        elif denominator>0:
            hists = list(hists)
            hists.insert(0,hist0)
            hist0 = hists[denominator-1]
            self.line = False
        if isinstance(hist0,THStack):
            hist0 = hist0.GetStack().Last() # should have correct bin content and error
        for hist in hists:
            if isinstance(hist,THStack):
              hist = hist.GetStack().Last()
            hist1 = hist.Clone("ratio_%s-%s"%(hist0.GetName(),hist.GetName()))
            hist1.Reset()
            hist1.SetTitle(self.title)
            self.ratios.append(hist1)
        self.hist0      = hist0
        self.ratio      = self.ratios[0]
        self.frame      = self.ratios[0]
        nbins           = hist0.GetNbinsX()
        
        if isinstance(error0,TGraphAsymmErrors):
            self.error  = error0.Clone()
        elif staterror:
            self.error  = TGraphAsymmErrors(nbins+2)
        
        #printRow("bin","data_bc","data_err","MC_bc","MC_err","ratio_bc","ratio_err","stat_bc","stat_err",widths=[4,11],line="abovebelow")
        #printRow("bin","error x","error y","errorDown","errorUp",widths=[4,11],line="abovebelow")
        for i in xrange(0,nbins+2):
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
          elif self.drawZero:
            for ratio, hist in zip(self.ratios,hists):
              binc1 = hist.GetBinContent(i)
              if binc1==0:
                ratio.SetBinContent(i, 1 )
                ratio.SetBinError(  i, 0 ) # error?

            
    
    def Draw(self, *options, **kwargs):
        """Draw all objects."""
        
        ratios      = self.ratios
        option      = options[0] if len(options)>0 else 'E'
        frame       = ratios[0]
        xmin        = frame.GetXaxis().GetXmin()
        xmax        = frame.GetXaxis().GetXmax()
        xmin        = kwargs.get('xmin',      xmin      )
        xmax        = kwargs.get('xmax',      xmax      )
        ymin        = kwargs.get('ymin',      0.5       )
        ymax        = kwargs.get('ymax',      1.5       )
        ylabel      = kwargs.get('ylabel',    "ratio"   ) #"data / M.C."
        xlabel      = kwargs.get('xlabel',    ""        )
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
            setErrorBandStyle(self.error,style='hatched')
            self.error.Draw('2 SAME')
        
        if self.line:
            self.line = TLine(xmin,1,xmax,1)
            if "E" in option:
              self.line.SetLineColor(12)
              self.line.SetLineWidth(1)
              self.line.SetLineStyle(2)
            else:
              self.line.SetLineColor(self.hist0.GetLineColor())
              self.line.SetLineWidth(self.hist0.GetLineWidth())
              self.line.SetLineStyle(1)
            self.line.Draw('SAME') # only draw line if a histogram has been drawn!
        
        for ratio in self.ratios:
            ratio.Draw(option+'SAME')
    
    def close(self):
        """Delete the histograms."""
        for ratio in self.ratios:
          deleteHist(ratio)
        if self.error:
          deleteHist(self.error)
        if self.line:
          deleteHist(self.line)
        




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
        self.weight             = kwargs.get('weight',      ""               )
        self.channel            = kwargs.get('channel',     "mutau"          )
        self.name               = kwargs.get('name',        "noname"         )
        self.title              = kwargs.get('title',       self.name        )
        
        frame = self.hists[0] if len(self.hists) else None
        if variable:
          self.var              = kwargs.get('var',         variable.name    )
          self.xmin             = kwargs.get('xmin',        variable.xmin    )
          self.xmax             = kwargs.get('xmax',        variable.xmax    )
          self.xlabel           = kwargs.get('xlabel',      variable.title   )
          self.logy             = kwargs.get('logy',        variable.logy    )
        else: 
          self.var              = kwargs.get('var',         frame.GetXaxis().GetTitle() )
          self.xmin             = kwargs.get('xmin',        frame.GetXaxis().GetXmin()  )
          self.xmax             = kwargs.get('xmax',        frame.GetXaxis().GetXmax()  )
          self.xlabel           = kwargs.get('xlabel',      self.var         )
          self.logy             = kwargs.get('logy',        False            )
        self.ylabel             = kwargs.get('ylabel',      ""               )
        
        self.errorband          = None
        self.error              = None
        self.ratio              = kwargs.get('ratio',       False            )
        self.stack              = kwargs.get('stack',       False            )
        self.reset              = kwargs.get('reset',       False            )
        self.split              = kwargs.get('split',       False            )
        self.signal             = kwargs.get('signal',      True             )
        self.background         = kwargs.get('background',  True             )
        self.data               = kwargs.get('data',        True             )
        self.ignore             = kwargs.get('ignore',      [ ]              )
        self.append             = kwargs.get('append',      ""               )
        self.black              = kwargs.get('black',       False            )
        self.normalize          = kwargs.get('normalize',   False            )
        
        self.canvas             = None
        self.frame              = frame
        self.legend             = None
        #self.width              = 0.08
        #self.height             = 0.05+0.05*(len(self.histsD)+len(self.histsB)+len(self.histsS))
        #self.x2 = 0.89; self.x1 = self.x2-self.width
        #self.y2 = 0.92; self.y1 = self.y2-self.height
        self.fillcolors         = fillcolors[:]
        self.markercolors       = colors[:]
        self.colors             = colors[:]
        if self.black: self.colors.insert(0,kBlack)
        
        if self.normalize:
          self.ylabel = "A.U."
          norm(self.hists)
    
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
        vartitle    = makeLatex(args[0]) if args else self.xlabel if self.xlabel else self.var if self.var else ""
        stack       = kwargs.get('stack',           False               ) or self.stack
        ratio       = (kwargs.get('ratio',          False               ) or self.ratio)
        residue     = kwargs.get('residue',         False               )
        errorbars   = kwargs.get('errorbars',       False               )
        staterror   = kwargs.get('staterror',       False               )
        JEC_errors  = kwargs.get('JEC_errors',      False               )
        drawData    = kwargs.get('data',            True                ) and self.histsD
        drawSignal  = kwargs.get('signal',          True                ) and self.histsS
        norm        = kwargs.get('norm',            False               )
        title       = kwargs.get('title',           self.title          )
        xlabel      = kwargs.get('xlabel',          vartitle            )
        ylabel      = kwargs.get('ylabel',          self.ylabel         )
        xmin        = kwargs.get('xmin',            self.xmin           )
        xmax        = kwargs.get('xmax',            self.xmax           )
        ymin        = kwargs.get('ymin',            None                )
        ymax        = kwargs.get('ymax',            None                )
        ymargin     = kwargs.get('ymargin',         1.16                )
        logx        = kwargs.get('logx',            False               )
        logy        = kwargs.get('logy',            False               )
        legend      = kwargs.get('legend',          True                )
        entries     = kwargs.get('entries',         [ ]                 )
        text        = kwargs.get('text',            [ ]                 ) # extra text for legend
        textsize    = kwargs.get('textsize', legendtextsize*(1 if self.histsD else 1.2))
        errortitle  = kwargs.get('errortitle',      "stat. unc."        )
        position    = kwargs.get('position',        ""                  )
        autostyle   = kwargs.get('autostyle',       True                )
        linestyle   = kwargs.get('linestyle',       True                )
        linewidth   = kwargs.get('linewidth',       2                   )
        ratiorange  = kwargs.get('ratiorange',      0.46                )
        option      = 'hist' #+ kwargs.get('option',  '')
        if errorbars: option = 'E0 '+option 
        if not xmin:  xmin = self.xmin
        if not xmax:  xmax = self.xmax
        
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
            self.setLineStyle(*self.histsB,style=linestyle)
        if self.histsD:
            self.setMarkerStyle(*self.histsD)
        if self.histsS:
            self.setLineStyle(*self.histsS,style=linestyle)
        
        # STATISTICAL ERROR
        if staterror:
            self.errorband = makeErrorBand(self.histsB, name=makeHistName("stat_error",self.name),
                                                               title=errortitle)
            if stack and JEC_errors:
                self.error = self.makeErrorFromJECShifts(JEC=JEC_errors)
                self.error.Draw('E2 SAME')
            else:
                self.errorband.Draw('E2 SAME')
        
        # AXES & LEGEND
        self.makeAxes(self.frame, *(self.histsB+self.histsD), xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax,
                      xlabel=xlabel, ylabel=ylabel, ymargin=ymargin, main=ratio, logy=logy, logx=logx)
        if legend:
            if not ratio: textsize *= 0.80
            self.makeLegend(title=title, entries=entries, position=position, text=text, textsize=textsize)
        
        # CMS LUMI
        if CMS_lumi.lumi_13TeV:
          CMS_lumi.CMS_lumi(gPad,13,0)
        
        # RATIO
        if ratio:
            self.canvas.cd(2)
            hargs       = [self.stack, self.histsD[0]] if stack else self.histsB
            roption     = "E" if drawData else "HIST"
            denominator = ratio if isinstance(ratio,int) and ratio>1 else -1 
            self.ratio  = Ratio(*hargs, staterror=staterror, error=self.error, denominator=denominator, drawZero=(not drawData))
            self.ratio.Draw(roption, xmin=xmin, xmax=xmax)
            self.makeAxes(self.ratio, xmin=xmin, xmax=xmax, ylabel="ratio", xlabel=xlabel, ratiorange=ratiorange)
        
    
    
    def saveAs(self,filename0,**kwargs):
        """Save plot, close canvas and delete the histograms."""
        
        save  = kwargs.get('save',  True    )
        close = kwargs.get('close', True    )
        exts  = kwargs.get('ext',   [ ]     )
        
        printSameLine("")
        if save:
          if exts:
            for ext in ensureList(exts):
              if '.' not in ext[0]: ext = '.'+ext
              filename = re.sub(r"\.?(png|pdf|jpg|gif|eps|tiff?)?$",ext,filename0,flags=re.IGNORECASE)
              self.canvas.SaveAs(filename)
          else:
            self.canvas.SaveAs(filename0)
        if close:
          self.close()
        
    
    def close(self):
        """Close canvas and delete the histograms."""
        
        if self.canvas:
            self.canvas.Close()
        for hist in self.hists:
            deleteHist(hist)
        if self.errorband:
            deleteHist(self.errorband)
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
        if self.stack:
          kwargs['histsB'] = self.histsB[::-1]
        else:
          kwargs['histsB'] = self.histsB
        kwargs['histsS'] = self.histsS
        kwargs['error']  = self.errorband
        #kwargs['x1'],    kwargs['x2']     = self.x1,    self.x2
        #kwargs['y1'],    kwargs['y2']     = self.y1,    self.y2
        #kwargs['width'], kwargs['height'] = self.width, self.height
        self.legend = makeLegend(*args,**kwargs)
        
    
    def makeAxes(self, frame, *args, **kwargs):
        """Make axis."""
        if isinstance(frame,Ratio):
          makeAxesRatio(frame,*args,**kwargs)
        else:
          self.xmin, self.xmax, self.ymin, self.ymax = makeAxes(frame,*args,**kwargs)
        
    def setLineStyle(self, *hists, **kwargs):
        """Set the line style for a list of histograms."""
        reset = kwargs.get('reset',  True  )
        if not hists: hists = self.hists[:]
        if not reset: hists = [h for h in hists if h.GetFillColor() in [kBlack,kWhite]]
        if hists:
          kwargs.setdefault('colors',self.colors)
          setLineStyle(*hists,**kwargs)
          
    def setMarkerStyle(self, *hists, **kwargs):
        """Set the marker style for a list of histograms."""
        reset = kwargs.get('reset',  True  )
        if not hists: hists = self.hists[:]
        hists = [h for h in hists if h.GetMarkerColor()!=kBlack]
        if hists:
          kwargs.setdefault('colors',self.markercolors)
          setMarkerStyle(*hists,**kwargs)
    
    def setFillStyle(self, *hists, **kwargs):
        """Set the fill style for a list of histograms."""
        reset     = kwargs.get('reset',     False  )
        blackline = kwargs.get('blackline', True   )
        if not hists: hists = self.hists[:]
        i = 0
        for hist in hists:
          #print hist.GetFillColor()
          if not reset and hist.GetFillColor() not in [kBlack,kWhite]: continue
          #print '>>> Plot::setFillStyle: hist "%s" has unset color!'%(hist.GetName())
          color0 = getColor(hist.GetName() )
          if not color0:
            color0 = self.fillcolors[i%len(self.fillcolors)]
            i += 1
          hist.SetFillColor(color0)
          if blackline:
            hist.SetLineColor(kBlack)
        
    
    
    def makeErrorFromJECShifts(self,**kwargs):
        """Method to create a SF for a given var, s.t. the data and MC agree."""
        



class Plot2D(object):
    """Class to automatically make CMS plot."""
    
    def __init__(self, sample, var1, nbins1, a1, b1, var2, nbins2, a2, b2, **kwargs):
        self.sample     = sample
        self.var1       = var1
        self.nbins1     = nbins1
        self.a1         = a1
        self.b1         = b1
        self.var2       = var2
        self.nbins2     = nbins2
        self.a2         = a2
        self.b2         = b2
        self.cuts       = kwargs.get('cuts', "")
        self.weight     = kwargs.get('weight', "")
        self.canvas     = None
        self.legend     = None
        self.width  = 0.20; self.height = 0.08 + 0.05 * 1
        self.x2     = 0.95; self.x1 = self.x2 - self.width
        self.y1     = 0.48; self.y2 = self.y1 + self.height
        self.hist       = sample.hist2D(var1, nbins1, a1, b1, var2, nbins2, a2, b2, weight=self.weight, cuts=self.cuts)
        
    
    
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
    


def isListOfHists(args):
    """Help function to test if list of arguments is a list of histograms."""
    if not isList(args): return False
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
      if isNumber(arg):
        args.remove(arg)
        binning.append(arg)
    if not variable and len(binning)>2:
      variable(varname,*binning[:3])
    
    if isListOfHists(args):
        return variable, [ ], args, [ ]
    if len(args)==1:
      if isListOfHists(args[0]):
        return variable, [ ], args[0], [ ]
    if len(args)==2:
      args0 = args[0]
      if isListOfHists(args[0]) and len(args[0])==1:
        args0 = args0[0]
      if isinstance(args0,TH1) and isListOfHists(args[1]):
        return variable, [args0], args[1], [ ]
    if len(args)==3:
      if isinstance(args[0],TH1) and isListOfHists(args[1]) and isListOfHists(args[2]):
        return variable, [args[0]], args[1], args[2]
      if isListOfHists(args[0]) and isListOfHists(args[1]) and isListOfHists(args[2]):
        return variable, args[0], args[1], args[2]
    print error('unwrapHistLists: Could not unwrap "%s"'%(args))
    exit(1)



from SampleTools import *
