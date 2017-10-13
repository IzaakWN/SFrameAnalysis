#from ROOT import * #TFile, TCanvas, TH2D, TH2D, THStack, TAxis, TGaxis, TGraph...
from ROOT import TFile, TCanvas, TPad, TH1D, TLegend, TAxis, THStack, TGraph, TGraphAsymmErrors, TLine,\
                 TGaxis, gDirectory, gROOT, gPad, Double,\
                 kBlack, kGray, kWhite, kRed, kBlue, kGreen, kYellow,\
                 kAzure, kCyan, kMagenta, kOrange, kPink, kSpring, kTeal, kViolet
import CMS_lumi, tdrstyle
import os, re
from math import sqrt, pow, log
# from SampleTools import Samples, Sample
from PrintTools import color, warning, error, header, printSameLine, printVerbose, LoadingBar
gROOT.Macro('PlotTools/QCDModelingEMu.C+')
#gROOT.Macro('PlotTools/weightJEta1.C+')

# CMS style
lumi = 12.9 # set in plot.py
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.105
CMS_lumi.outOfFrame = True
CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
tdrstyle.setTDRStyle()

# https://root.cern.ch/doc/master/classTColor.html
# http://imagecolorpicker.com/nl
# TColor::GetColor(R,B,G)
legendTextSize = 0.028 #0.036
colors     = [ kBlack,
               kRed+2, kAzure+5, kOrange-5, kGreen+2, kMagenta+2, kYellow+2,
               kRed-7, kAzure-4, kOrange+6, kGreen-2, kMagenta-3, kYellow-2 ]
fillcolors = [ kRed-2, kAzure+5,
               kMagenta-3, kYellow+771, kOrange-5,  kGreen-2,
               kRed-7, kAzure-9, kOrange+382,  kGreen+3,  kViolet+5, kYellow-2 ]
               #kYellow-3
               
varlist = {
    "jpt_1":  "leading jet pt",                 "jpt_2":    "subleading jet pt",
    "bpt_1":  "leading b jet pt",               "bpt_2":    "subleading b jet pt",
    "abs(jeta_1)": "leading jet abs(eta)",      "abs(jeta_2)": "subleading jet abs(eta)",
    "abs(beta_1)": "leading b jet abs(eta)",    "abs(beta_2)": "subleading b jet abs(eta)",
    "jeta_1": "leading jet eta",                "jeta_2":   "subleading jet eta",
    "beta_1": "leading b jet eta",              "beta_2":   "subleading b jet eta",
    "njets":  "multiplicity of jets",
    "ncjets": "multiplicity of central jets",   "nfjets":   "multiplicity of forward jets",
    "nbtag":  "multiplicity of b tagged jets",  "ncbtag":   "multiplicity of b tagged jets",
    "beta_1": "leading b jet eta",              "beta_2":   "subleading b jet eta",
    "pt_tt":  "pt_ltau",                        "R_pt_m_vis": "R = pt_ltau / m_vis",
    "pt_tt_sv": "SVFit pt_ltau,sv",             "R_pt_m_sv":  "SVFit R_{sv} = pt_ltau / m_sv",
    "m_sv":   "SVFit mass m_sv",
    "dR_ll":  "#DeltaR_{ltau}",
    "pfmt_1": "PF mt_l", "met":"MET"
}



def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR



def makeLatex(title):
    """Convert patterns in a string to LaTeX format."""
    
    if "jpt_1" in title and (title.count(">2.4")+title.count(">3.0")) is 2:
        title = "forward jpt_1"
    elif "jpt_1" in title and (title.count("<2.4")+title.count("<3.0")) is 2:
        title = "central jpt_1"
    elif "jpt_1" in title and title.count("<2.4") is 1:
        title = "central jpt_1 (|#eta|<2.4)"
    elif "jpt_1" in title and title.count(">3.0") is 1:
        title = "forward jpt_1 (|#eta|>3.0)"
    elif "jpt_2" in title and title.count(">3.0") is 1:
        title = "forward jpt_2 (|#eta|>3.0)"
    elif ">" in title or "<" in title or "=" in title:
        print warning("makeLatex: Boolean expression detected! How to replace?")
    if "_jer" in title:
        title = title.replace("_jer","")
    
    for var in varlist:
        if var in title:
            title = title.replace(var,varlist[var])
            break
    
    strings = [ ]
    for string in title.split(' / '):
    
        if "p_t" in string.lower() or "pt" in string.lower():
            if "pt_" in string.lower():
                string = string.replace("pt_","p_{T}^{").replace("Pt_","p_{T}^{") + "}"
            else:
                string = string.replace("p_t","p_{T}").replace("pt","p_{T}").replace("Pt","p_{T}")
        
        if "m_" in string.lower():
            string = string.replace("m_","m_{").replace("M_","M_{") + "}" # TODO: split at next space
        
        if "mt_" in string.lower():
            string = string.replace("mt_","m_{T}^{").replace("M_","M_{T}^{") + "}" # TODO: split at next space
        
        if "tau" in string.lower():
            string = string.replace("tau","#tau").replace("Tau","#tau")
        
        if "phi" in string.lower():
            if "phi_" in string.lower():
                string = string.replace("phi_","#phi_{").replace("Phi_","#phi_{") + "}"
            else:
                string = string.replace("phi","#phi").replace("Phi","#phi")
        
        if "eta" in string.lower() and "#eta" not in string.lower():
            if "eta_" in string.lower():
                string = string.replace("eta_","#eta_{").replace("Eta_","#eta_{") + "}"
            else:
                string = string.replace("eta","#eta").replace("Eta","#eta")
        
        if "abs(" in string and ")" in string:
            string = string.replace("abs(","|").replace(")","") + "|" # TODO: split at next space
        
        if  "mu" in string.lower():
            if "muon" not in string.lower() and "multi" not in string.lower(): 
                string = string.replace("mu","#mu").replace("Mu","#mu")
        
        if "ttbar" in string.lower():
            string = string.replace("ttbar","t#bar{t}").replace("TTbar","t#bar{t}")
        
        if "npv" in string.lower():
            string = string.replace("npv","number of vertices")
        
        strings.append(string)
    
    newtitle = '/'.join(strings)
    
    if "p_" in newtitle or "m_" in newtitle or "M_" in newtitle or "mass" in newtitle or ("MET" in newtitle and "phi" not in newtitle ) or "met" in newtitle:
        newtitle += " [GeV]"
    
    return newtitle
    
def makeHistName(*labels):
    """Use label and var to make an unique and valid histogram name."""
    hist_name = '_'.join(labels)
    hist_name = hist_name.replace("+","-").replace(" - ","-").replace(".","_").replace(" ","_")
    hist_name = hist_name.replace("(","_").replace(")","_").replace("[","_").replace("]","_")
    return hist_name
    




def combineWeights(*weights,**kwargs):
    """Combine cuts and apply weight if needed."""
    
    weights = [ w for w in weights if w and type(w) == str ]
    
    if weights: weights = "*".join(weights)
    else:       weights = ""
    
    #print weights
    return weights
    
def combineCuts(*cuts,**kwargs):
    """Combine cuts and apply weight if needed."""
    
    cuts = [ cut for cut in cuts if cut and type(cut) == str ]
    weight = kwargs.get('weight', False)
    
    # TODO: take "or" into account with parentheses
    for cut in cuts:
        if "||" in cuts: print warning("combineCuts: Be careful with those \"or\" statements!")
        # [cut.strip() for i in cut.split('||')]
        
    if cuts:
        cuts = " && ".join(cuts)
        if weight:  cuts = "(%s)*%s" % (cuts, weight)
    elif weight:    cuts = weight
    else:           cuts = ""

    #print cuts
    return cuts

def invertCharge(cuts,**kwargs):
    """Find, invert and replace charge selections."""
    
    verbosity   = kwargs.get('verbosity',0)
    cuts0       = cuts
    OS          = kwargs.get('OS',False)
    
    # MATCH PATTERNS https://regex101.com
    matchOS = re.findall(r"q_[12]\ *\*\ *q_[12]\ *<\ *0",cuts)
    matchSS = re.findall(r"q_[12]\ *\*\ *q_[12]\ *>\ *0",cuts)
    printVerbose(">>> invertCharge:\n>>>   matchOS = %s\n>>>   matchSS = %s" % (matchOS,matchSS),verbosity,level=2)
    
    # CUTS: invert charge
    if (len(matchOS)+len(matchSS))>1:
        print warning("invertCharge: more than one charge match (%d OS, %d SS) in \"%s\""%(len(matchOS),len(matchSS),cuts))
    if OS:
        for match in matchSS: cuts = cuts.replace(match,"q_1*q_2<0") # invert to OS
    else:
        for match in matchOS: cuts = cuts.replace(match,"q_1*q_2>0") # invert to SS
    if not cuts:
        if OS: cuts = "q_1*q_2<0"
        else:  cuts = "q_1*q_2>0"
    # if "q_1*q_2>0" in cuts.replace(' ',''): scale = 1.0
    # if "q_1*q_2<0" in cuts.replace(' ',''):
    #     cuts = cuts.replace("q_1 * q_2 < 0","q_1*q_2>0").replace("q_1*q_2 < 0","q_1*q_2>0").replace("q_1*q_2<0","q_1*q_2>0")        
    # elif cuts: cuts = "q_1*q_2>0 && %s" % cuts
    # else:      cuts = "q_1*q_2>0"
    
    printVerbose(">>>   \"%s\"\n>>>   -> \"%s\" (%s)\n>>>" % (cuts0,cuts,"OS" if OS else "SS"),verbosity,level=2)
    return cuts
    
def invertIsolation(cuts,**kwargs):
    """Find, invert and replace isolation selections."""
    
    verbosity   = kwargs.get('verbosity',0)
    channel     = kwargs.get('channel','emu')
    iso_relaxed = kwargs.get('to','iso_1<0.5 && iso_2<0.5 && iso_1>0.20') # outdated (iso_1>0.20||iso_2>0.15) pzeta_disc>-35 && nbtag<1
    cuts0       = cuts 
    
    # MATCH PATTERNS https://regex101.com
    match_iso_1 = re.findall(r"iso_1\ *[<>]\ *\d+\.\d+\ *[^\|]&*\ *",cuts)
    match_iso_2 = re.findall(r"iso_2\ *\!?=?[<=>]\ *\d+\.\d+\ *[^\|]&*\ *",cuts)
    printVerbose(">>> invertIsolation:\n>>>   match_iso_1 = %s\n>>>   match_iso_2 = \"%s\"" % (match_iso_1,match_iso_2),verbosity,level=2)
    
    # REPLACE
    if "iso_cuts==1" in cuts.replace(' ',''):
        cuts = re.sub(r"iso_cuts\ *==\ *1",iso_relaxed,cuts)
    elif len(match_iso_1) and len(match_iso_2):
        if len(match_iso_1)>1: print warning("invertIsolation: More than one iso_1 match! cuts=%s"%cuts)
        if len(match_iso_2)>1: print warning("invertIsolation: More than one iso_2 match! cuts=%s"%cuts)
        cuts = cuts.replace(match_iso_1[0],'')
        cuts = cuts.replace(match_iso_2[0],'')
        cuts = "%s && %s" % (iso_relaxed,cuts)
    elif cuts:
        if len(match_iso_1) or len(match_iso_2): print warning("invertIsolation: %d iso_1 and %d iso_2 matches! cuts=%s"%(len(match_iso_1),len(match_iso_2),cuts))
    cuts    = cuts.rstrip(' ').rstrip('&').rstrip(' ')
    
    printVerbose(">>>   \"%s\"\n>>>   -> \"%s\"\n>>>" % (cuts0,cuts),verbosity,level=2)
    return cuts
    
def relaxJetSelection(cuts,**kwargs):
    """Find, relax and replace jet selections:
         1) remove b tag requirements
         2) relax central jet requirements."""
    
    verbosity       = kwargs.get('verbosity',0)
    channel         = kwargs.get('channel','mutau')
    btags_relaxed   = kwargs.get('btags',"")
    cjets_relaxed   = kwargs.get('ncjets',"ncjets>1" if "ncjets==2" in cuts.replace(' ','') else "ncjets>0")
    cuts0           = cuts
    
    # MATCH PATTERNS
    btags = re.findall(r"&*\ *nc?btag\ *[<=>]=?\ *\d+\ *",cuts)
    cjets = re.findall(r"&*\ *ncjets\ *[<=>]=?\ *\d+\ *",cuts)
    printVerbose(">>> relaxJetSelection:\n>>>   btags = %s\n>>>   cjets = \"%s\"" % (btags,cjets),verbosity,level=2)
    
    # REPLACE
    if len(btags) and len(cjets):
        if len(btags)>1: print warning("relaxJetSelection: More than one btags match! cuts=%s"%cuts)
        if len(cjets)>1: print warning("relaxJetSelection: More than one cjets match! cuts=%s"%cuts)
        cuts = cuts.replace(btags[0],'')
        cuts = cuts.replace(cjets[0],'')
        if btags_relaxed: cuts = "%s && %s && %s" % (cuts,btags_relaxed,cjets_relaxed)
        else:             cuts = "%s && %s"       % (cuts,              cjets_relaxed)
    elif cuts:
        if len(btags) or len(cjets): print warning("relaxJetSelection: %d btags and %d cjets matches! cuts=%s"%(len(btags),len(cjets),cuts))
    cuts = cuts.lstrip(' ').lstrip('&').lstrip(' ')
    
    printVerbose(">>>   \"%s\"\n>>>   -> \"%s\"\n>>>" % (cuts0,cuts),verbosity,level=2)
    return cuts



def makeCanvas(**kwargs):
    """Make canvas and pads for ratio plots."""
    
    square              = kwargs.get('square', False)
    scaleleftmargin     = kwargs.get('scaleleftmargin', 1)
    scalerightmargin    = kwargs.get('scalerightmargin', 1)
    scaletopmargin      = kwargs.get('scaletopmargin', 1)
    name                = kwargs.get('name', "canvas").replace(' ','_')
    residue             = kwargs.get('residue', False)
    ratio               = kwargs.get('ratio', False)
    pads                = kwargs.get('pads', []) # pass list as reference
            
    W = 800; H  = 600
    if square:
        W = 800; H  = 800
        scalerightmargin = 3.5*scalerightmargin
    elif residue or ratio:
        W = 800; H  = 750
        scaleleftmargin         = 1.05*scaleleftmargin
        scalerightmargin        = 0.45*scalerightmargin
        scaletopmargin          = 0.80*scaletopmargin
        CMS_lumi.cmsTextSize    = 0.55
        CMS_lumi.lumiTextSize   = 0.45
        CMS_lumi.relPosX        = 0.08
    
    T = 0.08*H*scaletopmargin
    B = 0.12*H
    L = 0.12*W*scaleleftmargin
    R = 0.04*W*scalerightmargin
    
    canvas = TCanvas(name,name,100,100,W,H)
    canvas.SetFillColor(0)
    canvas.SetBorderMode(0)
    canvas.SetFrameFillStyle(0)
    canvas.SetFrameBorderMode(0)
    canvas.SetLeftMargin( L/W )
    canvas.SetRightMargin( R/W )
    canvas.SetTopMargin( T/H )
    canvas.SetBottomMargin( B/H )

    if residue or ratio:
        pads.append(TPad("pad1","pad1", 0, 0.33, 1, 0.95))
        pads.append(TPad("pad2","pad2", 0, 0.05, 1, 0.30))
        pads[0].SetLeftMargin(0.125); #pads[0].SetRightMargin(0.05)
        pads[0].SetTopMargin(0.02);    pads[0].SetBottomMargin(0.00001)
        pads[0].SetBorderMode(0)
        pads[1].SetTopMargin(0.00001); pads[1].SetBottomMargin(0.10)
        pads[1].SetLeftMargin(0.125); #pads[1].SetRightMargin(0.05)
        pads[1].SetBorderMode(0)
        pads[0].Draw()
        pads[1].Draw()
        pads[0].cd()
        pads = pads

    return canvas



def makeLegend(*hists,**kwargs):
    """Make legend."""
    
    title       = kwargs.get('title', None)
    entries     = kwargs.get('entries', [ ])
    position    = kwargs.get('position', "")
    ratio       = kwargs.get('ratio',True)
    fontsize    = kwargs.get('fontsize', 0.038)
    transparent = kwargs.get('transparent', False)
    width, height = 0.16, 0.07+0.06*(len(hists)+sum([e for e in entries if "newline" in e]))
    x2 = 0.86; x1 = x2-width
    y2 = 0.92; y1 = y2-height
    style0      = kwargs.get('style0', 'l')
    style1      = kwargs.get('styles', 'l')
    
    if position:
        if   "LeftLeft"     in position: x1 = 0.15;         x2 = x1 + width
        elif "RightRight"   in position: x2 = 1 - 0.10;     x1 = x2 - width
        elif "CenterRight"  in position: x1 = 0.57-width/2; x2 = 0.57+width/2
        elif "CenterLeft"   in position: x1 = 0.44-width/2; x2 = 0.44+width/2
        elif "Left"         in position: x1 = 0.18;         x2 = x1 + width
        elif "Right"        in position: x2 = 1 - 0.15;     x1 = x2 - width
        elif "Center"       in position: x1 = 0.55-width/2; x2 = 0.55+width/2
        if   "BottomBottom" in position: y1 = 0.15;         y2 = y1 + height
        elif "Bottom"       in position: y1 = 0.20;         y2 = y1 + height
        elif "TopTop"       in position: y2 = 0.95;         y1 = y2 - height
        elif "Top"          in position: y1 = 0.93;         y2 = y1 - height
    if not ratio: (y1,y2) = (y1*0.9,y2*0.9)
    legend = TLegend(x1,y1,x2,y2)
    
    if transparent: legend.SetFillStyle(0) # 0 = transparent
    else: legend.SetFillColor(kWhite)
    legend.SetBorderSize(0)
    legend.SetTextSize(fontsize)
    legend.SetTextFont(62) # bold for title
    
    if title is None: legend.SetHeader("")
    else: legend.SetHeader(title)
    legend.SetTextFont(42) # no bold
    
    if hists:
        if entries:
            for i, (hist, entry) in enumerate(zip( hists, entries )): #reversed
                style = style1
                if i is 0: style = style0
                legend.AddEntry(hist,entry,style)
        else:
            for i, hist in enumerate(hists):
                style = style1
                if i is 0: style = style0
                legend.AddEntry(hist,hist.GetTitle(),style)

        legend.Draw()
        return legend



def makeAxes(hist0, *hists, **kwargs):
    """Make axis."""
    
    frame       = None
    ratio       = kwargs.get('ratio', None)
    stack       = kwargs.get('stack', None)
    negativeY   = kwargs.get('negativeY', True)
    scale       = 1
    
    if ratio:
        frame = ratio.ratio
        scale = 2.5
        frame.GetYaxis().SetRangeUser(0.4,1.6)
        frame.GetYaxis().SetNdivisions(505)
    elif stack:
        frame = stack
        maxs = [ stack.GetMaximum() ]
        for hist in hists0:
            maxs.append(hist.GetMaximum())
        #frame.SetMinimum(0)
        frame.SetMaximum(max(maxs)*1.15)
    else:
        frame = hist0
        mins = [ 0, frame.GetMinimum() ]
        maxs = [ frame.GetMaximum() ]
        for hist in hists:
            mins.append(hist.GetMinimum())
            maxs.append(hist.GetMaximum())
        frame.GetYaxis().SetRangeUser(min(mins),max(maxs)*1.12)
    if not negativeY: frame.SetMinimum(0)
    
    if kwargs.get('logy',False):
        #frame.SetMinimum(0.1)
        gPad.Update(); gPad.SetLogy()
    if kwargs.get('logx',False):
        #frame.SetMinimum(0.1)
        gPad.Update(); gPad.SetLogx()
    
    xlabel = makeLatex(kwargs.get('xlabel', hist0.GetTitle()))
    ylabel = kwargs.get('ylabel', "")
    if not ylabel:
        ylabel = ("Events / %.3f" % frame.GetXaxis().GetBinWidth(0)).rstrip("0").rstrip(".")
        if "GeV" in xlabel:
            ylabel += " GeV"
    
    if ratio:
        ylabel = "ratio"
        frame.GetYaxis().SetTitle(ylabel)
        frame.GetYaxis().SetLabelSize(0.10)
        frame.GetYaxis().SetTitleSize(0.15)
        frame.GetYaxis().CenterTitle(True)
        frame.GetYaxis().SetTitleOffset(0.45)
    else:
        frame.GetYaxis().SetTitle(ylabel)
        frame.GetYaxis().SetLabelSize(0.040)
        frame.GetYaxis().SetTitleSize(0.052)
        frame.GetYaxis().SetTitleOffset(1.25)
    
    # TODO: for Axis label https://root.cern.ch/root/roottalk/roottalk03/3375.html
    frame.GetXaxis().SetTitle(xlabel)
    frame.GetXaxis().SetLabelSize(0.040*scale)
    frame.GetXaxis().SetTitleSize(0.042*scale)
    frame.GetXaxis().SetTitleOffset(1.10)
    if kwargs.get('noxaxis',False): # e.g. for main plot above a ratio
        frame.GetXaxis().SetLabelSize(0)
        frame.GetXaxis().SetTitleSize(0)
    TGaxis.SetExponentOffset(-0.058,0.005,'y')
    




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
    
    name = kwargs.get('name', "error_"+hists[0].GetName())
    title = kwargs.get('title', "error")
    color = kwargs.get('color', kBlack)
    N = hists[0].GetNbinsX()
    a = hists[0].GetXaxis().GetXmin()
    b = hists[0].GetXaxis().GetXmax()
    hist_error = TH1D(name,title,N,a,b)
    hist_error.Sumw2()
    
    for hist in hists:
        hist_error.Add(hist)
    
    setStatisticalErrorStyle(hist_error,color=color)
    hist_error.SetLineColor(hists[0].GetLineColor())
    hist_error.SetLineWidth(hists[0].GetLineWidth()) # Draw(E2 SAME)
    
    return hist_error
    



def makeAsymmErrorFromShifts(hist0,histsDown0,histsNom0,histsUp0,hist_staterror,**kwargs):
    """Create asymmetric error from combining up and down shifts. Also include statistical
       error, if present. Fromula:
          sqrt( (nominal - up shift)^2 + (nominal - down shift)^2 + statistical^2 )"""
    
    # CHECKS
    histsDown = histsDown0[:]
    histsNom  = histsNom0[:]
    histsUp   = histsUp0[:]
    if isinstance(hist0,THStack):      hist0     = hist0.GetStack().Last()
    if not isinstance(histsDown,list): histsDown = [histsDown]
    if not isinstance(histsNom,list):  histsNom  = [histsNom]
    if not isinstance(histsUp,list):   histsUp   = [histsUp]
    for i, hist in enumerate(histsDown0):
        if isinstance(hist,THStack):   histsDown[i] = hist.GetStack().Last()
    for i, hist in enumerate(histsNom0):
        if isinstance(hist,THStack):   histsNom[i]  = hist.GetStack().Last()
    for i, hist in enumerate(histsUp0):
        if isinstance(hist,THStack):   histsUp[i]   = hist.GetStack().Last()
    if len(histsUp) != len(histsDown):
        print warning("makeAsymmErrorFromShifts: len(histsUp) != len(histsDown)")
        exit(1)
    elif len(histsNom) != len(histsUp):
        if len(histsNom) == 1: histsNom = [histsNom]*len(histsUp)
        else:
            print warning("makeAsymmErrorFromShifts: 1 != len(histsNom) != len(histsUp) == len(histsDown)")
            exit(1)
    
    # SETTINGS
    (N,a,b) = (hist0.GetNbinsX(), hist0.GetXaxis().GetXmin(),hist0.GetXaxis().GetXmax())
    errors  = TGraphAsymmErrors()
    
    # CHECK BINNING
    for hist in histsUp+histsNom+histsDown+[hist_staterror]:
        (N1,a1,b1) = (hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
        if N != N1 or a != a1 or b != b1 :
            print warning("makeRatio: Binning between data (%d,%.1f,%.1f) and error (%s,%d,%.1f,%.1f) histogram is not the same!"%\
                  (N,a,b,N1,a1,b1,hist.GetTitle()))
    
    # CALCULATE BINNING
    for i in range(1,N+1):
        biny = hist0.GetBinContent(i)
        binx = hist0.GetXaxis().GetBinCenter(i)
        errors.SetPoint(i-1,binx,biny)
        errorUp2   = 0
        errorDown2 = 0
        if hist_staterror:
            biny1 = hist_staterror.GetBinContent(i)
            if biny != biny1:
                print warning("makeAsymmErrorFromShifts: "+\
                      "Bincontent hist0 (%.1f) and hist_staterror (%.1f) are not the same!" % (biny,biny1))
            errorUp2   += hist_staterror.GetBinError(i)**2
            errorDown2 += hist_staterror.GetBinError(i)**2
        for histUp, histNom, histDown in zip(histsUp,histsNom,histsDown):
            binyNom     = histNom.GetBinContent(i)
            errorUp2   += (binyNom-histUp.GetBinContent(i))**2
            errorDown2 += (binyNom-histDown.GetBinContent(i))**2
        width = hist0.GetXaxis().GetBinWidth(i)/2
        errors.SetPointError(i-1,width,width,sqrt(errorDown2),sqrt(errorUp2))
    
    setStatisticalErrorStyle(errors)
    errors.SetFillStyle(3004)
    errors.SetLineColor(hist0.GetLineColor())
    errors.SetLineWidth(hist0.GetLineWidth())
    # Draw('2 SAME')
    
    return errors
    




def makeRatio(hist0,hist1,**kwargs):
    """Make a ratio of two histograms bin by bin. Second hist may be a stack,
       to do data / MC stack."""
    
    name            = kwargs.get('name', "ratio_%s-%s"%(hist0.GetName(),hist1.GetName()))
    title           = kwargs.get('title', "ratio")
    error0          = kwargs.get('error',None)
    staterror       = kwargs.get('staterror',not error0)
    (N,a,b)         = (hist0.GetNbinsX(),hist0.GetXaxis().GetXmin(),hist0.GetXaxis().GetXmax())
    hist_ratio      = TH1D(name,title,N,a,b)
    hist_staterror  = None
    error           = None
    if staterror:
        hist_staterror = TH1D(name+"_staterror",title+" staterror",N,a,b)
    if error0: # TGraphAsymmErrors
        error = error0.Clone()
    
    if isinstance(hist1,THStack):
        hist1 = hist1.GetStack().Last() # should have correct bin content and error
    
    #print ">>> %3s  %9s %9s %9s %9s %9s %9s %9s %9s" %\
    #      ("i","data_bc","data_err","MC_bc","MC_err","ratio_bc","ratio_err","stat_bc","stat_err")
    for i in xrange(1,N+1):
        binc0 = hist0.GetBinContent(i)
        binc1 = hist1.GetBinContent(i)
        if binc1:
            if staterror:
                hist_staterror.SetBinContent(i,1) # hist1/hist1
                hist_staterror.SetBinError(i,hist1.GetBinError(i)/binc1)
            if error:
                x,y = Double(), Double()
                error.GetPoint(i-1,x,y)
                error.SetPoint(i-1,x,1)
                error.SetPointEYlow(i-1,error.GetErrorYlow(i)/binc1)
                error.SetPointEYhigh(i-1,error.GetErrorYhigh(i)/binc1)
            if binc0 and binc0 / binc1 < 100:
                hist_ratio.SetBinContent(i, binc0 / binc1 ); # hist0/hist1
                hist_ratio.SetBinError(i, hist0.GetBinError(i)/binc1 ) # assume error on MC is 0
            # print ">>> %3s  %9.3f %9.3f %9.3f %9.3f %9.3f %9.3f" %\
            #       (i,hist0.GetBinContent(i),         hist0.GetBinError(i),
            #          hist1.GetBinContent(i),         hist1.GetBinError(i),
            #          hist_ratio.GetBinContent(i),    hist_ratio.GetBinError(i)) +\
            #       ("%9.3f %9.3f"%(hist_staterror.GetBinContent(i),hist_staterror.GetBinError(i)) if staterror else "")
    
    return Ratio( hist_ratio, line=True, staterror=hist_staterror, error=error )
    




def norm(*hists,**kwargs):
    """ Normalize histogram."""
    if isinstance(hists[0],list): hists = hists[0]
    for hist in hists:
        I = hist.Integral()
        if I: hist.Scale(1/I)
        else: print warning("norm: Could not normalize; integral = 0!")
    
def ratioError(a,ea,b,eb):
    """Calculate the error on a ratio a/b given errors ea on a and eb on b"""
    
    if b == 0:
        print warning("ratioError: cannot divide by zero!")
        return ea
    elif a == 0:
        return ea
    return abs(a/b) * sqrt( pow(ea/a,2) + pow(eb/b,2) )
    




class Ratio(object):
    """Class to make bundle histograms (ratio, stat. error on MC and line) for ratio plot."""
    
    def __init__(self, ratio, **kwargs):
        self.ratio      = ratio # histogram
        self.staterror  = kwargs.get('staterror', None)
        self.error      = kwargs.get('error', None)
        self.line       = kwargs.get('line', True)
    
    def Draw(self, *option, **kwargs):
        """Draw all histograms"""
        
        option      = option[0] if len(option)>0 else "E same"
        a, b        = self.ratio.GetXaxis().GetXmin(), self.ratio.GetXaxis().GetXmax()
        a, b        = kwargs.get('xmin',a),   kwargs.get('xmax',b)
        ymin, ymax  = kwargs.get('ymin',0.4), kwargs.get('ymax',1.6)
        ylabel      = kwargs.get('ylabel',"ratio") #"data / M.C."
        xlabel      = kwargs.get('xlabel',"")
        size        = 1.0 #0.9
        
        self.ratio.GetYaxis().SetTitle(ylabel)
        if xlabel:
            self.ratio.GetXaxis().SetTitle(xlabel)
        self.ratio.GetYaxis().SetLabelSize(0.10)
        self.ratio.GetXaxis().SetLabelSize(0.11)
        self.ratio.GetYaxis().SetTitleSize(0.12)
        self.ratio.GetXaxis().SetTitleSize(0.10)
        self.ratio.GetYaxis().CenterTitle(True)
        self.ratio.GetYaxis().SetTitleOffset(0.5)
        self.ratio.GetYaxis().SetRangeUser(ymin,ymax)
        self.ratio.GetYaxis().SetNdivisions(505)
        self.ratio.SetNdivisions(505)
        self.ratio.SetMarkerSize(size)
        self.ratio.Draw(option+" axis")
        
        if self.error:
            setStatisticalErrorStyle(self.error,style='hatched')
            self.error.Draw('2 SAME')
        elif self.staterror:
            setStatisticalErrorStyle(self.staterror,style='hatched')
            self.staterror.Draw('E2 SAME')
            # self.staterror.SetLineStyle(1)
            # self.staterror.SetMarkerStyle(1)
            # self.staterror.SetFillColor(kBlack)
            # self.staterror.SetFillStyle(3004) # 3001 small dots, 3004 hatched
        
        if self.line:
            self.line = TLine(a,1,b,1)
            self.line.SetLineColor(12) # dark grey
            self.line.SetLineStyle(2)
            self.line.Draw('SAME') # only draw line if a histogram has been drawn!
        
        # option = "E SAME"
        # if "hist" in option.lower(): option = "HIST"
        self.ratio.Draw(option)





class Comparison(object):
    """Class to automatically make CMS plot."""
    
    def __init__(self, hist0, *hists, **kwargs):
        if not hists: print warning("Comparison: no second histogram to compare to!")
        self.hist0      = hist0
        self.hists      = hists
        self.nBins      = hist0.GetNbinsX()
        self.a, self.b  = (hist0.GetXaxis().GetXmin(), hist0.GetXaxis().GetXmax())
        self.canvas     = None
        self.pads       = [ ]
        self.staterrors = [ ]
        self.ratios     = [ ]
        self.legend     = None
    
    def Draw(self,*option0,**kwargs):
        """Draw comparison of histograms with ratio plot."""
        
        hist0           = self.hist0
        hists           = self.hists
        option0         = option0[0] if len(option0)>0 else ""
        normalize       = kwargs.get('norm',            False       )
        errorbars       = kwargs.get('errorbars',       True        )
        markers         = kwargs.get('markers',         False       )
        markers_ratio   = kwargs.get('markers_ratio',   True        )
        linestyle       = kwargs.get('linestyle',       True        )
        ratio           = kwargs.get('ratio',           True        )
        staterror       = kwargs.get('staterror',       errorbars   )
        legend          = kwargs.get('legend',          True        )
        position        = kwargs.get('position',        ""          )
        xlabel          = kwargs.get('xlabel',          ""          )
        ylabel          = kwargs.get('ylabel',          ""          )
        title           = kwargs.get('title',           ""          )
        entries         = kwargs.get('entries',         [ ]         ) # for legend
        KS              = kwargs.get('KS',              True        ) # Kolmogorov-Smirnoff test
        Dns             = [ ]
        if entries and len(entries) is not len(hists)+1:
            print warning("Comparison::Draw(): Number of legend entries (%s) not the same as number of histograms"%(len(entries)))
        
        options         = "HIST E SAME"
        option_ratios   = "HIST E SAME"
        style0          = 'l'
        styles          = 'le'
        if markers:
            styles = 'lpe'
            options = "E SAME"
        if markers_ratio:
            option_ratios = "E SAME"
        if not errorbars:
            style0  = style0.replace('e','')
            styles  = styles.replace('e','')
            options = options.replace('E ','')
            option_ratios = option_ratios.replace('E ','')
        
        if normalize:
            norm(hist0)
            for hist in hists: norm(hist)
        if KS:
            for i,hist in enumerate(hists,1):
                Dn = hist0.KolmogorovTest(hist)
                print ">>> KolmogorovTest: Dn=%.3f for %s with %s" % (Dn,hist0.GetName(),hist.GetName())
                Dns.append(Dn)
                if entries: entries[i] = "%s (%.3f KS)" % (entries[i],Dn)
            if not entries: print warning("Comparison::Draw(): No entries to add KS value to!")
        
        # DRAW & STYLE
        if ratio:
            self.canvas = makeCanvas(ratio=True,pads=self.pads)
            self.staterrors.append(makeStatisticalError(hist0))
            for hist in hists:
                self.ratios.append(makeRatio(hist,hist0)) # only draw first
            
            self.pads[0].cd()
            hist0.Draw("HIST")
            if self.staterrors:
                self.staterrors[0].Draw("E2 SAME")
            for hist in hists:
                hist.Draw(options)
            if markers:
                setMarkerStyle(*hists,size=0.7,noblack=True)
                hist0.SetLineWidth(2)
            else:
                hist0.SetLineWidth(2)
                hist0.SetLineColor(kBlack)
                setLineStyle(*hists,style=linestyle,noblack=True)
            
            self.pads[1].cd()
            if self.ratios:
                self.ratios[0].Draw(option_ratios)
                for ratio in self.ratios:
                    ratio.Draw(option_ratios)
                if markers_ratio: setMarkerStyle(*[r.ratio for r in self.ratios],noblack=True)
                else:             setLineStyle(  *[r.ratio for r in self.ratios],style=linestyle,noblack=True)
            self.pads[0].cd()
        else:
            self.canvas = makeCanvas()
            hist0.Draw("E0 HIST")
            for hist in hists:
                hist.Draw("E0 HIST SAME")
            setLineStyle(hist0,*hists)
        
        # AXES & LEGEND
        makeAxes( hist0, *hists, xlabel=xlabel, noxaxis=ratio,
                  logy=kwargs.get('logy',False), logx=kwargs.get('logx',False) )
        if ratio and self.ratios:
            makeAxes(hist0, *hists, ratio=self.ratios[0], ylabel=ylabel, xlabel=xlabel)
        if legend:
            self.legend = makeLegend(hist0,*hists,title=title,entries=entries,position=position,styles=styles,ratio=ratio)
        
        # CMS LUMI
        TGaxis.SetExponentOffset(-0.058,0.005,'y')
        CMS_lumi.cmsTextSize  = 0.65
        CMS_lumi.lumiTextSize = 0.60
        CMS_lumi.relPosX      = 0.105
        CMS_lumi.CMS_lumi(self.canvas,13,0)
    
    
    def saveAs(self,filename,**kwargs):
        """Save plot, close canvas and delete the histograms."""
        close = kwargs.get('close',True)
        printSameLine("")
        self.canvas.SaveAs(filename)
        if close: self.close()
        
    def close(self,**kwargs):
        """Close canvas and delete the histograms."""
        delete = kwargs.get('delete',True)
        if self.canvas:       self.canvas.Close()
        if delete:
            gDirectory.Delete(self.hist0.GetName())
            for hist in self.hists: gDirectory.Delete(hist.GetName())
            for staterror in self.staterrors:
                gDirectory.Delete(staterror.GetName())
            for ratio in self.ratios:
                gDirectory.Delete(ratio.ratio.GetName())
                if ratio.staterror: gDirectory.Delete(ratio.staterror.GetName())
                if ratio.line: gDirectory.Delete(ratio.line.GetName())
            




class Plot(object):
    """Class to automatically make CMS plot."""
    
    def __init__(self, samples, var, nBins, a, b, **kwargs):
        self.samples        = samples[:]
        self.var            = var
        self.nBins          = nBins
        self.a, self.b      = (a,b)
        self.cuts           = kwargs.get('cuts', "") # extra cuts
        self.weight         = kwargs.get('weight', "")
        self.shift_QCD      = kwargs.get('shift_QCD', 0)
        self.ratio_WJ_QCD_SS = kwargs.get('ratio_WJ_QCD_SS',0)
        self.ratio_TT_QCD_SS = kwargs.get('ratio_TT_QCD_SS',0)
        self.channel        = kwargs.get('channel', "mutau")
        
        self.histsS         = [ ]
        self.histsB         = [ ]
        self.histsD         = [ ]
        self._hists         = [ ]
        self._histsMC       = [ ]
        self.hist_error     = None
        self.error          = None
        self.ratio          = None
        self.reset          = kwargs.get('reset', False)
        self.split          = kwargs.get('split', False)
        self.fillcolors     = fillcolors[:]
        self.colors         = [kAzure+4] + colors[:]
        self.fillcolors_dict = { }
        self.ignore         = kwargs.get('ignore',[])
        self.append_name    = kwargs.get('append_name',"")
        self.verbosity      = kwargs.get('verbosity',0)
        self.loadingbar     = kwargs.get('loadingbar', True) and not self.verbosity
        
        if self.loadingbar:
            bar = LoadingBar(len(samples),width=16,prepend=">>> %s: making histograms: " % (self.var),counter=True,remove=True)
        for sample in self.samples:
            if self.loadingbar: bar.message(sample.label)
            if self.reset: sample.scale = sample.scaleBU
            if sample.label in self.ignore:
                #self.colors.pop(self.samples.index(sample))
                self.fillcolors.pop(self.samples.index(sample))
                if self.loadingbar: bar.count("%s skipped"%sample.label)
                continue
            
            # ADD signal
            if sample.isSignal and kwargs.get('signal', True):
                for hist in [sample.hist(var, nBins, a, b, cuts=self.cuts, weight=self.weight, append_name=self.append_name, verbosity=self.verbosity)]:
                    self.histsS.append(hist)
            
            # ADD background
            elif sample.isBackground and kwargs.get('background', True):
                for hist,color0 in sample.histAndColor(var, nBins, a, b, cuts=self.cuts, weight=self.weight, append_name=self.append_name, verbosity=self.verbosity, split=self.split):
                    self.histsB.append(hist)
                    self.fillcolors_dict[hist.GetName()] = color0
            
            # ADD data
            elif sample.isData and kwargs.get('data', True):
                for hist in [sample.hist(var, nBins, a, b, cuts=self.cuts, append_name=self.append_name, verbosity=self.verbosity)]:
                    self.histsD.append(hist)
            
            if self.loadingbar: bar.count("%s done"%sample.label)
        
        # ADD QCD
        if kwargs.get('QCD', False):
            histQCD = self.QCD(ratio_WJ_QCD_SS=self.ratio_WJ_QCD_SS,ratio_TT_QCD_SS=self.ratio_TT_QCD_SS,append_name=self.append_name,verbosity=self.verbosity)
            self.fillcolors_dict[histQCD.GetName()] = kRed-7
            if histQCD: self.histsB.append(histQCD)
        
        self.stack          = None
        self.canvas         = None
        self.graph_sigma    = None
        self.canvas_sigma   = None
        self.pads           = [ ]
        self.frame          = None
        self.legend         = None
        self.width  = 0.11;  self.height = 0.08 + 0.05*len(self.histsB)
        self.x2 = 0.89; self.x1 = self.x2-self.width
        self.y2 = 0.92; self.y1 = self.y2-self.height
    
    @property
    def hists(self): return ( self.histsB + self.histsS + self.histsD )
    
    @hists.setter
    def hists(self, value): self._hists = value
    
    @property
    def histsMC(self): return ( self.histsB + self.histsS )
    
    @histsMC.setter
    def histsMC(self, value): self._histsMC = value



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
        stack       = kwargs.get('stack',      False)
        residue     = kwargs.get('residue',    False) and self.histsD
        ratio       = kwargs.get('ratio',      False) and self.histsD
        errorbars   = kwargs.get('errorbars',  False)
        staterror   = kwargs.get('staterror',  False)
        JEC_errors  = kwargs.get('JEC_errors', False)
        norm        = kwargs.get('norm',       False)
        option      = 'hist' #+ kwargs.get('option', '')
        if errorbars: option = 'E0 '+option
        
        # CANVAS
        self.makeCanvas(  square=kwargs.get('square', False), pads=self.pads,
                          residue=residue, ratio=ratio,
                          scaleleftmargin=kwargs.get('scaleleftmargin', 1),
                          scalerightmargin=kwargs.get('scalerightmargin', 1)  )
        
        # MONTE CARLO
        if stack:
            stack = THStack("stack","")
            self.stack = stack
            for hist in self.histsB: stack.Add(hist)
            stack.Draw(option)
            for hist in self.histsS: hist.Draw(option+' SAME')
        else:
            for hist in self.histsMC: hist.Draw(option+' SAME')
        
        # DATA
        if kwargs.get('data', True):
            for hist in self.histsD:
                hist.Draw('E SAME')
        
        # NORM
        if norm: norm(self.hists)
            
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
            self.hist_error = makeStatisticalError( self.histsB, name=makeHistName("stat_error",self.var),
                                                    title="statistical error" )
            if stack and JEC_errors:
                (histsDown,histsNom,histsUp) = self.makeJECShifts()
                self.error = makeAsymmErrorFromShifts(self.stack,histsDown,histsNom,histsUp,self.hist_error)
                self.error.Draw('E2 SAME')
            else:
                self.hist_error.Draw('E2 SAME')
        
        # AXES & LEGEND
        self.makeAxes( xlabel=kwargs.get('xlabel', self.var), noxaxis=ratio,
                       logy=kwargs.get('logy',False), logx=kwargs.get('logx',False) )
        if kwargs.get('legend', True):
            self.makeLegend( title=kwargs.get('title', ""), entries=kwargs.get('entries', [ ]),
                                                            position=kwargs.get('position', "") )
        
        # CMS LUMI
        CMS_lumi.cmsTextSize  = 0.65
        CMS_lumi.lumiTextSize = 0.60
        CMS_lumi.relPosX      = 0.105
        CMS_lumi.CMS_lumi(self.canvas,13,0)
        
        # RATIO
        if ratio and stack and self.histsD:
            self.pads[1].cd()
            self.ratio = makeRatio( self.histsD[0], self.stack, staterror=self.hist_error, error=self.error,
                                     name=makeHistName("ratio",self.var), title="ratio" )
            self.ratio.Draw('SAME')
            self.makeAxes( ratio=self.ratio, ylabel="ratio", xlabel=kwargs.get('xlabel', self.var))
            
    
    
    
    def saveAs(self,filename,**kwargs):
        """Save plot, close canvas and delete the histograms."""
        
        save = kwargs.get('save',True)
        close = kwargs.get('close',True)
        printSameLine("")
        if save:
            self.canvas.SaveAs(filename)
            #self.canvas.SaveAs(filename.replace(".png",".pdf"))
            if self.canvas_sigma:
                self.canvas_sigma.SaveAs(filename.replace(".png","_eff.png"))
                #self.canvas_sigma.SaveAs(filename.replace(".png","_eff.pdf"))
        if close: self.close()



    def close(self):
        """Close canvas and delete the histograms."""
        
        if self.canvas:       self.canvas.Close()
        if self.canvas_sigma: self.canvas_sigma.Close()
        for hist in self.hists:
            #print "close: Removing %s" % (hist.GetName())
            gDirectory.Delete(hist.GetName())
        if self.hist_error:
            gDirectory.Delete(self.hist_error.GetName())
        if self.ratio:
            gDirectory.Delete(self.ratio.ratio.GetName())
            gDirectory.Delete(self.ratio.staterror.GetName())
            gDirectory.Delete(self.ratio.line.GetName())



    def makeCanvas(self,**kwargs):
        """Make canvas and pads for ratio plots."""
        
        square              = kwargs.get('square', False)
        scaleleftmargin     = kwargs.get('scaleleftmargin', 1)
        scalerightmargin    = kwargs.get('scalerightmargin', 1)
        scaletopmargin      = kwargs.get('scaletopmargin', 1)
        residue             = kwargs.get('residue', False)
        ratio               = kwargs.get('ratio', False)
        pads                = kwargs.get('pads', []) # pass list as reference
        CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
        
        W = 800; H  = 600
        if square:
            W = 800; H  = 800
            self.width = 0.25
            scalerightmargin = 3.5*scalerightmargin
        elif residue or ratio:
            W = 800; H  = 750
            scaleleftmargin  = 1.05*scaleleftmargin
            scalerightmargin = 0.45*scalerightmargin
            scaletopmargin   = 0.80*scaletopmargin
            CMS_lumi.cmsTextSize  = 0.55
            CMS_lumi.lumiTextSize = 0.45
            CMS_lumi.relPosX = 0.08
        
        T = 0.08*H*scaletopmargin
        B = 0.12*H
        L = 0.12*W*scaleleftmargin
        R = 0.04*W*scalerightmargin
        
        canvas = TCanvas("canvas","canvas",100,100,W,H)
        canvas.SetFillColor(0)
        canvas.SetBorderMode(0)
        canvas.SetFrameFillStyle(0)
        canvas.SetFrameBorderMode(0)
        canvas.SetLeftMargin( L/W )
        canvas.SetRightMargin( R/W )
        canvas.SetTopMargin( T/H )
        canvas.SetBottomMargin( B/H )

        if residue or ratio:
            pads.append(TPad("pad1","pad1", 0, 0.33, 1, 0.95))
            pads.append(TPad("pad2","pad2", 0, 0.05, 1, 0.30))
            pads[0].SetLeftMargin(0.125)
            #pads[0].SetRightMargin(0.05)
            pads[0].SetTopMargin(0.02)
            pads[0].SetBottomMargin(0.00001)
            pads[0].SetBorderMode(0)
            pads[1].SetTopMargin(0.00001)
            pads[1].SetBottomMargin(0.10)
            pads[1].SetLeftMargin(0.125)
            #pads[1].SetRightMargin(0.05)
            pads[1].SetBorderMode(0)
            pads[0].Draw()
            pads[1].Draw()
            pads[0].cd()
            #self.pads = pads

        self.canvas = canvas



    def makeLegend(self,*args,**kwargs):
        """Make legend."""
        
        title       = kwargs.get('title', None)
        entries     = kwargs.get('entries', [ ])
        position    = kwargs.get('position', "")
        transparent = kwargs.get('transparent', False)
        hists       = self.hists
        histsS      = self.histsS
        histsD      = self.histsD
        (x1,x2)     = (self.x1,self.x2)
        (y1,y2)     = (self.y1,self.y2)
        width       = self.width
        height      = self.height
        
        styleD      = 'lep'
        styleB      = 'l'
        styleS      = 'l'
        if self.stack: styleB = 'f'
        
        if position:
            if   "LeftLeft"     in position: x1 = 0.15;         x2 = x1 + width
            elif "RightRight"   in position: x2 = 1 - 0.10;     x1 = x2 - width
            elif "CenterRight"  in position: x1 = 0.57-width/2; x2 = 0.57+width/2
            elif "CenterLeft"   in position: x1 = 0.44-width/2; x2 = 0.44+width/2
            elif "Left"         in position: x1 = 0.18;         x2 = x1 + width
            elif "Right"        in position: x2 = 1 - 0.15;     x1 = x2 - width
            elif "Center"       in position: x1 = 0.55-width/2; x2 = 0.55+width/2
            if   "BottomBottom" in position: y1 = 0.15;         y2 = y1 + height
            elif "Bottom"       in position: y1 = 0.20;         y2 = y1 + height
            elif "TopTop"       in position: y2 = 0.95;         y1 = y2 - height
            elif "Top"          in position: y1 = 0.93;         y2 = y1 - height
        legend = TLegend(x1,y1,x2,y2)
        
        if transparent: legend.SetFillStyle(0) # 0 = transparent
        else: legend.SetFillColor(kWhite)
        legend.SetBorderSize(0)
        legend.SetTextSize(legendTextSize)
        legend.SetTextFont(62) # bold for title
                       
        if title is None: legend.SetHeader("")
        else: legend.SetHeader(title)
        legend.SetTextFont(42) # no bol for entries

        if hists:
            if entries:
                for hist, entry in zip( hists, entries ): #reversed
                    style = styleB
                    if hist in histsD: style = styleD
                    if hist in histsS: style = styleS
                    legend.AddEntry(hist,entry,style)
            else:
                for hist in hists:
                    style = styleB
                    if hist in histsD: style = styleD
                    if hist in histsS: style = styleS
                    legend.AddEntry(hist,hist.GetTitle(),style)

            self.legend = legend
            legend.Draw()
            
    
            
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



    def makeAxes(self, *args, **kwargs):
        """Make axis."""
        
        frame       = None
        ratio       = kwargs.get('ratio', None)
        negativeY   = kwargs.get('negativeY', True)
        scale       = 1
        
        if ratio:
            frame = ratio.ratio
            scale = 2.5
            #width = max(abs(1-frame.GetMinimum(0)),abs(1-frame.GetMaximum()))*1.30
            #frame.GetYaxis().SetRangeUser(*self.symmetricYRange(frame,center=1.0))
            frame.GetYaxis().SetRangeUser(0.4,1.6)
            frame.GetYaxis().SetNdivisions(505)
        elif self.stack:
            frame = self.stack
            maxs = [ self.stack.GetMaximum() ]
            for hist in self.histsD:
                maxs.append(hist.GetMaximum())
            #frame.SetMinimum(0)
            frame.SetMaximum(max(maxs)*1.15)
        else:
            frame = self.hists[0]
            mins = [ 0 ]
            maxs = [   ]
            for hist in self.hists:
                if negativeY: mins.append(hist.GetMinimum())
                maxs.append(hist.GetMaximum())
            frame.GetYaxis().SetRangeUser(min(mins),max(maxs)*1.12)
        frame.GetXaxis().SetRangeUser(self.a,self.b)
        
        if kwargs.get('logy',False):
            #frame.SetMinimum(0.1)
            gPad.Update(); gPad.SetLogy()
        if kwargs.get('logx',False):
            #frame.SetMinimum(0.1)
             gPad.Update(); gPad.SetLogx()
        
        xlabel = makeLatex(kwargs.get('xlabel', self.hists[0].GetTitle()))
        ylabel = kwargs.get('ylabel', "")
        if not ylabel:
            if "multiplicity" in xlabel: ylabel = "Events"
            else: ylabel = ("Events / %.3f" % frame.GetXaxis().GetBinWidth(0)).rstrip("0").rstrip(".")
            if "GeV" in xlabel: ylabel += " GeV"
        
        # TODO: for Axis label https://root.cern.ch/root/roottalk/roottalk03/3375.html
        if ratio:
            ylabel = "ratio" #"data / M.C."
            frame.GetYaxis().SetTitle(ylabel)
            frame.GetYaxis().SetLabelSize(0.10)
            frame.GetYaxis().SetTitleSize(0.12)
            frame.GetYaxis().CenterTitle(True)
            frame.GetYaxis().SetTitleOffset(0.5)
        else:
            frame.GetYaxis().SetTitle(ylabel)
            frame.GetYaxis().SetLabelSize(0.040)
            frame.GetYaxis().SetTitleSize(0.042)
            frame.GetYaxis().SetTitleOffset(1.45)
        
        frame.GetXaxis().SetTitle(xlabel)
        frame.GetXaxis().SetLabelSize(0.040*scale)
        frame.GetXaxis().SetTitleSize(0.042*scale)
        frame.GetXaxis().SetTitleOffset(1.10)
        if kwargs.get('noxaxis',False): # e.g. for main plot above a ratio
            frame.GetXaxis().SetLabelSize(0)
            frame.GetXaxis().SetTitleSize(0)  
#         frame.GetYaxis().CenterTitle(True)
#         frame.GetXaxis().SetNdivisions(508)
#         ROOT.gPad.SetTicks(1,1)
#         ROOT.gPad.SetGrid(1,1)
        TGaxis.SetExponentOffset(-0.058,0.005,'y')



    def setLineStyle(self, *hists, **kwargs):
        """Make line style."""

        if len(hists) is 0: hists = self.hists
        gen = kwargs.get('gen', False)
        colors2 = [kAzure+4, kRed+3, kAzure-4, kRed-7, kMagenta+3, kGreen+3, kOrange+6, kMagenta-3]

        if gen:
            line = [1,3,2,3]
            for i in range(len(hists)):
                hists[i].SetLineColor(colors2[i])
                hists[i].SetLineStyle(line[i%4])
                hists[i].SetLineWidth(3)
        else:
            for i in range(len(hists)):
                hists[i].SetLineColor(colors2[i%len(colors2)])
                hists[i].SetLineStyle(i%4+1)
                hists[i].SetLineWidth(3)



    def setFillStyle(self, *hists):
        """Make fill style."""
        if len(hists) is 0: hists = self.hists
        for i, hist in enumerate(hists):
            color0 = self.fillcolors_dict.get(hist.GetName(),self.fillcolors[i%len(self.fillcolors)])
            hist.SetFillColor(color0)
        
    
    
    def substractStackFromHist(self,stack,hist0,**kwargs):
        """Substract stacked MC histograms from a data histogram,
           bin by bin if the difference is larger than zero."""
        
        verbosity   = kwargs.get('verbosity', 0)
        name        = kwargs.get('name', "diff_"+hist0.GetName())
        title       = kwargs.get('title', "difference")
        nBins       = hist0.GetNbinsX()
        (a,b)       = (hist0.GetXaxis().GetXmin(), hist0.GetXaxis().GetXmax())
        hist_diff   = TH1D(name,title,nBins,a,b)
        stackhist   = stack.GetStack().Last()
        printVerbose(">>>\n>>> substractStackFromHist: %s - %s"%(name,title),verbosity)
        printVerbose(">>>   (BC = \"bin content\", BE = \"bin error\")",     verbosity)
        printVerbose(">>>   %4s  %9s  %8s  %8s  %8s  %8s  %8s"%("bin","data BC","data BE","MC BC","MC BE","QCD BC","QCD BE"), verbosity)
        
        for i in range(1,nBins+1): # include overflow
            hist_diff.SetBinContent(i, max(0,hist0.GetBinContent(i)-stackhist.GetBinContent(i)));
            hist_diff.SetBinError(i,sqrt(hist0.GetBinError(i)**2+stackhist.GetBinError(i)**2))
            printVerbose(">>>   %4s  %9.1f  %8.2f  %8.2f  %8.2f  %8.2f  %8.2f"%(i,hist0.GetBinContent(i),    hist0.GetBinError(i),
                                                                      stackhist.GetBinContent(i),stackhist.GetBinError(i),
                                                                      hist_diff.GetBinContent(i),hist_diff.GetBinError(i)),verbosity)
        
        return hist_diff



    def integrateStack(self,*args,**kwargs):
        """Integrate stack."""
        
        a = kwargs.get('a',0)
        b = kwargs.get('b',0)
        
        if   len(args) == 1:
            stack = args[0].GetStack().Last()
        elif len(args) == 2:
            stack = self.stack.GetStack().Last()
            a = args[0]
            b = args[1]
        elif len(args) == 3:
            stack = args[0].GetStack().Last()
            a = args[1]
            b = args[2]
        else:
            stack = self.stack.GetStack().Last()
        
        integral = 0
        if a < b: integral = stack.Integral(stack.FindBin(a), stack.FindBin(b))
        else:     integral = stack.Integral(stack.FindBin(b), stack.FindBin(a))
        return integral



    def integrateHist(self,*args,**kwargs):
        """Integrate histogram."""
        
        (a,b) = (kwargs.get('a',0),kwargs.get('b',0))
        
        if   len(args) == 1:
            hist = args[0]
            if not a and not b: return hist.Integral()
        elif len(args) == 3:
            hist = args[0]
            a = args[1]
            b = args[2]
        else:
            print warning("Could not integrate!")
            return 0
        
        integral = 0
        if a < b: integral = hist.Integral(hist.FindBin(a), hist.FindBin(b))
        else:     integral = hist.Integral(hist.FindBin(b), hist.FindBin(a))
        return integral
    


    def QCD(self,**kwargs):
        """Substract MC from data with same sign (SS) selection of a lepton - tau pair
           and return a histogram of the difference."""
        # TODO: check error propagation: e_QCD = sqrt(e_data^2+e_MC^2)
        
        verbosity       = kwargs.get('verbosity',False)
        if verbosity > 1:
            print header("estimating QCD for variable %s" % (self.var))
            #printVerbose(">>>\n>>> estimating QCD for variable %s" % (self.var),verbosity,level=2)
        
        cuts            = self.cuts
        var             = self.var
        nBins, a, b     = self.nBins, self.a, self.b
        samples         = self.samples
        name            = kwargs.get('name',makeHistName("QCD",var))
        append_name     = kwargs.get('append_name',"")
        ratio_WJ_QCD_SS = self.ratio_WJ_QCD_SS or kwargs.get('ratio_WJ_QCD_SS',False)
        #ratio_TT_QCD_SS = self.ratio_TT_QCD_SS or kwargs.get('ratio_TT_QCD_SS',False)
        
        weight          = combineWeights(kwargs.get('weight',""),self.weight)
        if weight and self.weight: weight = combineWeights(weight,self.weight)
        weight_data     = combineWeights(kwargs.get('weight',""),self.weight)
        
        relax           = 'emu' in self.channel or ("jets" in cuts and "btag" in cuts)
        relax           = kwargs.get('relax',relax) #and False
        
        shift           = kwargs.get('shift',0.0) + self.shift_QCD # for systematics
        scaleup         = 2.0 if "emu" in self.channel else 1.06
        scaleup         = 1.0 if "q_1*q_2>0" in cuts.replace(' ','') else scaleup
        scaleup         = kwargs.get('scaleup',scaleup)
        printVerbose(">>>   QCD: scaleup = %s shift = %s, self.shift_QCD = %s" % (scaleup,shift,self.shift_QCD),verbosity,level=2)
        
        # CUTS: invert charge
        cuts            = invertCharge(cuts)
        
        # CUTS: relax cuts for QCD_SS_SB
        # https://indico.cern.ch/event/566854/contributions/2367198/attachments/1368758/2074844/QCDStudy_20161109_HTTMeeting.pdf
        QCD_OS_SR = 0
        if relax:
            
            # GET yield QCD_OS_SR = SF * QCD_SS_SR
            if 'emu' in self.channel: # use weight instead of scaleup
                scaleup     = 1.0
                weight      = combineWeights("getQCDWeight(pt_2, pt_1, dR_ll)",weight)
                weight_data = "getQCDWeight(pt_2, pt_1, dR_ll)" # SF ~ 2.4 average
            kwargs_SR       = kwargs.copy()
            kwargs_SR.update({ 'scaleup':scaleup, 'weight':weight, 'weight_data':weight_data, 'relax':False })
            histQCD_OS_SR   = self.QCD(**kwargs_SR)
            QCD_OS_SR       = histQCD_OS_SR.Integral(1,nBins+1) # yield
            scaleup         = 1.0
            gDirectory.Delete(histQCD_OS_SR.GetName())
            if QCD_OS_SR < 1: print warning("QCD: QCD_SR = %.1f < 1"%QCD_OS_SR)
            
            # RELAX cuts for QCD_OS_SB = SF * QCD_SS_SB
            iso_relaxed = "iso_1>0.15 && iso_1<0.5 && iso_2==1" #iso_2_medium
            if 'emu' in self.channel: iso_relaxed = "iso_1>0.20 && iso_1<0.5 && iso_2<0.5"
            else: cuts = relaxJetSelection(cuts)
            cuts = invertIsolation(cuts,to=iso_relaxed)
        
        printVerbose(">>>   QCD: cuts = %s %s" % (cuts,"(relaxed)" if relax else ""),verbosity,level=2)
        
        # HISTOGRAMS
        histsMC_SS = [ ]
        histsD_SS  = [ ]
        histWJ = None
        if self.loadingbar: bar = LoadingBar(len(samples),width=16,prepend=">>> %s: calculating QCD: " % (self.var),counter=True,remove=True)
        for sample in samples:
            if self.loadingbar: bar.count(sample.label)
            name_SS = makeHistName(sample.label+"_SS", var)
            if sample.isBackground:
                hist = sample.hist(var, nBins, a, b, cuts=cuts, weight=weight, name=name_SS, verbosity=verbosity)
                histsMC_SS.append(hist)
                if ratio_WJ_QCD_SS and ("WJ" in hist.GetName() or "w-jets" in hist.GetName().lower()):
                    if histWJ: print warning("QCD: more than one W+jets sample in SS region, going with first instance!", prepend="  ")
                    else: histWJ = hist
            elif sample.isData:
                histsD_SS.append(sample.hist(var, nBins, a, b, cuts=cuts, weight=weight_data, name=name_SS, verbosity=verbosity))
            if self.loadingbar: bar.count("%s done"%sample.label)
        if not histsD_SS:
            print warning("No data to make DATA driven QCD!")
            return None
        
        # STACK
        stack_SS = THStack("stack_SS","stack_SS")
        for hist in histsMC_SS: stack_SS.Add(hist)
        histQCD = self.substractStackFromHist(stack_SS,histsD_SS[0],name=name+append_name,title="QCD")
        if not histQCD: print warning("Could not make QCD! QCD histogram is none!", prepend="  ")
        
        # YIELD
        if relax:
            QCD_SS = histQCD.Integral(1,nBins+1)
            if QCD_SS:
                scaleup = QCD_OS_SR/QCD_SS # normalizing to OS_SR
                printVerbose(">>>   QCD: scaleup = QCD_OS_SR/QCD_SS_SB = %.1f/%.1f = %.3f" % (QCD_OS_SR,QCD_SS,scaleup),verbosity,level=2)
            else:
                print warning("QCD: QCD_SS_SB.Integral() == 0!")
        scale = scaleup*(1.0+shift) # scale up QCD 6% in OS region by default
        histQCD.Scale(scale)
        QCD_SS = histQCD.Integral()
        
        # WJ/QCD ratio
        if ratio_WJ_QCD_SS and histWJ:
            WJ_SS  = histWJ.Integral()
            if QCD_SS: ratio_WJ_QCD_SS = WJ_SS/QCD_SS
            else: print warning("QCD: QCD integral is 0!", prepend="  ")
            printVerbose(">>>   QCD: QCD_SS = %.1f, WJ_SS = %.1f, ratio_WJ_QCD_SS = %.3f" % (QCD_SS,WJ_SS,ratio_WJ_QCD_SS),verbosity,level=2)
            self.ratio_WJ_QCD_SS = ratio_WJ_QCD_SS
        else:
            printVerbose(">>>   QCD: QCD_SS = %.1f, scale=%.3f" % (QCD_SS,scale),verbosity,level=2)
        
        for hist in histsMC_SS + histsD_SS:
            gDirectory.Delete(hist.GetName())
        
        return histQCD
    


    def measureOSSSratio(self,**kwargs):
        """Measure OS/SS ratio by substract non-QCD MC from data with opposite sign (OS) and same sign (SS)
           requirements of a lepton pair."""
        
        verbosity       = kwargs.get('verbosity',1)
        if verbosity > 0:
           print header("measure OS/SS ratio in %s" % (self.var))
        
        var             = self.var
        nBins, a, b     = self.nBins, self.a, self.b
        name            = kwargs.get('name',makeHistName("QCD",var))
        cuts            = self.cuts
        weight          = kwargs.get('weight',"")
        samples         = self.samples
        channel         = self.channel
        relaxed         = kwargs.get('relaxed',True)
        
        # INVERT charge and isolation
        if relaxed:
            relaxed_iso     = "iso_2==1 && iso_1>0.15" # iso_1<0.5 && 
            #relaxed_iso     = "iso_1<0.5 && iso_2_medium==1 && iso_1>0.15"
            #relaxed_iso     = "iso_1<0.5 && iso_2_medium==1 && (iso_1>0.15||iso_2==0)"
            if 'emu' in channel:
                relaxed_iso = "iso_1<0.5 && iso_2<0.5 && (iso_1>0.20)" # ||iso_2>0.10
            cuts   = invertIsolation(cuts,to=relaxed_iso)
        cutsOS = invertCharge(cuts,OS=True)
        cutsSS = invertCharge(cuts,OS=False)
        
        # HISTOGRAMS
        histsMC_OS = [ ]
        histsMC_SS = [ ]
        histsD_OS  = [ ]
        histsD_SS  = [ ]
        if self.loadingbar: bar = LoadingBar(len(samples),width=16,prepend=">>> %s: calculating OS/SS: " % (self.var),counter=True,remove=True)
        for sample in samples:
            if self.loadingbar: bar.count(sample.label)
            if sample.isPartOf("QCD"): continue
            name_OS = makeHistName(sample.label+"_SS", var)
            name_SS = makeHistName(sample.label+"_OS", var)
            if sample.isBackground:
                histOS = sample.hist(var, nBins, a, b, cuts=cutsOS, weight=weight, name=name_OS, verbosity=verbosity-1)
                histSS = sample.hist(var, nBins, a, b, cuts=cutsSS, weight=weight, name=name_SS, verbosity=verbosity-1)
                histsMC_OS.append(histOS)
                histsMC_SS.append(histSS)
            elif sample.isData:
                histsD_OS.append(sample.hist(var, nBins, a, b, cuts=cutsOS, name=name_OS, verbosity=verbosity-1))
                histsD_SS.append(sample.hist(var, nBins, a, b, cuts=cutsSS, name=name_SS, verbosity=verbosity-1))
            if self.loadingbar: bar.count("%s done"%sample.label)
        if not histsD_OS or not histsD_SS:
            print warning("No data to make DATA driven QCD!")
            return None
        
        # STACK
        stack_OS = THStack("stack_OS","stack_OS")
        stack_SS = THStack("stack_SS","stack_SS")
        for hist in histsMC_OS: stack_OS.Add(hist)
        for hist in histsMC_SS: stack_SS.Add(hist)
        e_MC_OS,   e_MC_SS   = Double(), Double()
        e_data_OS, e_data_SS = Double(), Double()
        MC_OS = stack_OS.GetStack().Last().IntegralAndError(1,nBins+1,e_MC_OS)
        MC_SS = stack_SS.GetStack().Last().IntegralAndError(1,nBins+1,e_MC_SS)
        data_OS = histsD_OS[0].IntegralAndError(1,nBins+1,e_data_OS)
        data_SS = histsD_SS[0].IntegralAndError(1,nBins+1,e_data_SS)
        
        # CHECK
        if verbosity>0:
            print ">>>"
            print ">>>   \"%s\""%(cutsOS)
            print ">>>   \"%s\""%(cutsSS)
            print ">>> %8s %10s %10s"     % ("sample","OS",   "SS")
            print ">>> %8s %10.1f %10.1f" % ("MC",    MC_OS,  MC_SS)
            print ">>> %8s %10.1f %10.1f" % ("data",  data_OS,data_SS)
        
        # YIELD
        QCD_OS   = data_OS-MC_OS
        QCD_SS   = data_SS-MC_SS
        e_QCD_OS = sqrt(e_data_OS**2+e_MC_OS**2)
        e_QCD_SS = sqrt(e_data_SS**2+e_MC_SS**2)
        if QCD_SS:
            OSSS = QCD_OS/QCD_SS
            e_OSSSS = OSSS*sqrt( (e_data_OS**2+e_MC_OS**2)/QCD_OS**2 + (e_data_SS**2+e_MC_SS**2)/QCD_SS**2)
            printVerbose(">>>   QCD_OS/QCD_SS = %.1f +/-%.1f / %.1f +/-%.1f = %.3f +/-%.3f %s" % (QCD_OS,e_QCD_OS,QCD_SS,e_QCD_SS,OSSS,e_OSSSS,"(relaxed)" if relaxed else ""),verbosity,level=1)
        else:
            print warning("measureOSSSratio: denominator QCD_SS is zero: %.1f/%.1f"% (QCD_OS,QCD_SS))
        
        for hist in histsMC_OS + histsMC_SS + histsD_OS + histsD_SS:
            gDirectory.Delete(hist.GetName())
        #gDirectory.Delete("stack_OS")
        #gDirectory.Delete("stack_SS")
    


    def measureSF(self,**kwargs):
        self.measureSFFromVar(self.var,self.nBins,self.a,self.b,**kwargs)

    def measureSFFromVar(self,var,nBins,a,b,**kwargs):
        """Method to create a SF for a given var, s.t. the data and MC agree."""
        
        verbosity       = kwargs.get('verbosity',False)
        if verbosity > 1:
            print header("measure SF for variable %s" % (self.var))
            #printVerbose(">>>\n>>> estimating QCD for variable %s" % (self.var),verbosity,level=2)
        
        cuts            = kwargs.get('cuts',self.cuts)
        weight          = kwargs.get('weight',"")
        samples         = self.samples
        filename        = kwargs.get('filename',"")
        cutname         = kwargs.get("cutname","") + kwargs.get('append_name',"")
        DIR             = kwargs.get('DIR',"")
        save            = kwargs.get('save',True or filename)
        histname        = kwargs.get('name',makeHistName("SF",var))
        saveoption      = kwargs.get('saveoption',"recreate")
        
        histsMC         = self.histsB
        histsD          = self.histsD
        histD           = None
#         if self.loadingbar: bar = LoadingBar(len(samples),width=16,prepend=">>> %s: calculating SF: " % (self.var),counter=True,remove=True)
#         for sample in samples:
#             if self.loadingbar: bar.count(sample.label)
#             name = makeHistName(sample.label+"_SF", var)
#             if sample.isBackground:
#                 hist = sample.hist(var, nBins, a, b, cuts=cuts, weight=weight, name=name, verbosity=verbosity)
#                 histsMC.append(hist)
#             elif sample.isData:
#                 histsD.append(sample.hist(var, nBins, a, b, cuts=cuts, weight=weight, name=name, verbosity=verbosity))
#             if self.loadingbar: bar.count("%s done"%sample.label)
        if not histsD:
            print warning("measureSFFromVar: No data to measure SF!")
            return None
        else:
            histD = histsD[0]
        
        stack = THStack("stack","stack")
        for hist in histsMC:
            stack.Add(hist)
        stackhist = stack.GetStack().Last()
        
        cutsToSF = { }
        hist_SF = TH1D(histname,histname,nBins,a,b)
        for i in xrange(1,nBins+1):
            MC = stackhist.GetBinContent(i)
            D  = histD.GetBinContent(i)
            SF = 1
            if MC == 0.0:
                print warning("measureSFFromVar: bin %3d (%4.1f,%4.1f) has zero MC events for var %s. SF set to 1."%(i,histD.GetXaxis().GetBinLowEdge(i),histD.GetXaxis().GetBinUpEdge(i),var))
                MC = D
            else:
                SF = D/MC
            eMC = stackhist.GetBinContent(i)
            eD  = histD.GetBinContent(i)
            eSF = 0
            if MC!=0.0 and D!=0: eSF = SF*sqrt( eMC**2/MC**2 + eD**2/D**2 )
            hist_SF.SetBinContent(i,SF)
            hist_SF.SetBinError(i,eSF)
            
            cut = ""
            if i==nBins: cut = "%.2f <= %s"        % (histD.GetXaxis().GetBinLowEdge(i),var)
            elif i==1:           cut = "%s < %.2f" % (var,histD.GetXaxis().GetBinUpEdge(i))
            else:        cut = "%.2f <= %s < %.2f" % (histD.GetXaxis().GetBinLowEdge(i),var,histD.GetXaxis().GetBinUpEdge(i))
            cutsToSF[cut] = SF
            printVerbose(">>> measureSFFromVar: bin %2d, %26s: %5.1f +/- %.2f"%(i,cut,SF,eSF),1)
        
        if save:
            if not filename:
                filename = "%s_SF.root" % (var)
                if cutname: filename = "%s_SF_%s_%s.root" % (var,self.channel,cutname)
                else: filename = "%s_SF_%s.root" % (var,self.channel)
            if DIR:
                ensureDirectory(DIR)
                filename = "%s/%s"%(DIR,filename)
            file = TFile(filename,saveoption)
            hist_SF.Write(histname,TH1D.kOverwrite)
            file.Close()
            printVerbose(">>> measureSFFromVar: made %s"%(filename),1)
        
        return cutsToSF
        
    
    
    def makeJECShifts(self,**kwargs):
        """Method to create a SF for a given var, s.t. the data and MC agree."""
        
        verbosity       = kwargs.get('verbosity',False)
        if verbosity > 1:
            print header("Calculate JEC shift for variable %s" % (self.var))
            #printVerbose(">>>\n>>> estimating QCD for variable %s" % (self.var),verbosity,level=2)
        
        # SETTINGS
        (nBins,a,b)     = (self.nBins,self.a,self.b)
        var             = self.var
        cuts            = kwargs.get('cuts',self.cuts)
        weight          = kwargs.get('weight',self.cuts)
        samples         = self.samples
        histsB_noQCD    = [h for h in self.histsB if not ("QCD" in h.GetName() or "QCD" in h.GetTitle())]
        cutname         = kwargs.get("cutname","") + kwargs.get('append_name',"")
        DIR             = kwargs.get('DIR',"")
        save            = kwargs.get('save',True or filename)
        pattern0        = "_jer" # pattern to be replaced
        
        # CHECK
        if pattern0 not in cuts: print warning("makeJECShifts: \"%s\" not in cuts!"%(pattern0))
        if pattern0 not in var: print warning("makeJECShifts: \"%s\" not in var!"%(pattern0))
        if "jpt" not in var and "jeta" not in var:
            print warning("makeJECShifts: var \"%s\" not applicable for JEC shift!"%var)
            return None
        
        shifts_dict = { 'jesDown': "_jesDown",
                        'jesNom':  "",
                        'jesUp':   "_jesUp",
                        'jerDown': "_jerDown",
                        'jerNom':  "_jer",
                        'jerUp':   "_jerUp",
        }
        
        # MAKE SHIFTS
        for key, shift in shifts_dict.items():
            stack      = THStack("stack_shift"+shift,"stack_shift"+shift)
            var_shift  = var.replace(pattern0,shift)
            cuts_shift = cuts #.replace(pattern0,shift)
            for sample in samples:
                if sample.isPartOf("QCD"): continue
                if not sample.isBackground: continue
                print ">>> %s"%(sample.label)
                name_shift = makeHistName(sample.label,var_shift,"shift")
                hist = sample.hist(var_shift, nBins, a, b, cuts=cuts_shift, weight=weight, name=name_shift, verbosity=verbosity)
                stack.Add(hist)
            shifts_dict[key] = stack
        
        # JER nominal
        # stack = THStack("stack_jer","stack_jer")
        # print ">>> makeJECShifts: making nominal jer stack, adding:"
        # for hist in histsB_noQCD:
        #     print ">>>   %s (%s)" % (hist.GetName(),hist.GetTitle())
        #     stack.Add(hist)
        # shifts_dict['jerNom'] = stack.GetStack().Last()
        
        histsDown = [shifts_dict['jesDown'],shifts_dict['jerDown']]#[ val for key, val in shifts_dict.items() if "Down" in key ]
        histsNom  = [shifts_dict['jesNom'], shifts_dict['jerNom']]#[ val for key, val in shifts_dict.items() if "Nom"  in key ]
        histsUp   = [shifts_dict['jesUp'],  shifts_dict['jerUp']]#[ val for key, val in shifts_dict.items() if "Up"   in key ]
        
        return [histsDown,histsNom,histsUp]
        
    
    
    def renormalizeWJ(self,**kwargs):
        """Renormalize WJ by requireing that MC and data has the same number of events in
           the mt_1 > 80 GeV sideband.
           This method assume that the variable of this Plot object is a transverse mass and is plotted
           from 80 GeV to at least 100 GeV."""
        printSameLine(">>>\n>>> %srenormalizing WJ with mt > 80 GeV sideband for variable %s" % (kwargs.get('prepend',""),self.var))
        
        samples     = self.samples
        cuts        = self.cuts
        var         = self.var
        nBins       = self.nBins
        (a,b)       = (self.a,self.b)
        verbosity   = kwargs.get('verbosity',0)
        
        # STACK
        QCD         = False
        I_QCD       = 0
        stack = THStack("stack","")
        printVerbose(" ",verbosity,level=2)
        for hist in self.histsMC:
            if "signal" in hist.GetName() or "Signal" in hist.GetName():
                printVerbose(">>>   ignored signal sample: %s" % (hist.GetName()),verbosity,level=2)
                continue
            if hist.Integral()<=0:
                print warning("Ignored %s with an integral of %s <= 0 !" % (hist.GetName(),hist.Integral()), prepend="  ")
            if "QCD" in hist.GetName():
                QCD   = True
                I_QCD = hist.Integral()
            printVerbose(">>>   adding to stack %s (%.1f events)" % (hist.GetName(),hist.Integral()),verbosity,level=2)
            stack.Add(hist)
        if QCD and verbosity<2: print "(QCD included)"
        elif not QCD: print " "
        self.stack = stack
        
        # CHECK MC and DATA
        if not self.histsMC:
            print warning("Could not renormalize WJ: no MC!", prepend="  ")
            return
        if not self.stack:
            print warning("Could not renormalize WJ: no stack!", prepend="  ")
            return
        if not self.histsD:
            print warning("Could not renormalize WJ: no data!", prepend="  ")
            return
        
        # CHECK mt
        for v in [ "mt", "m_t" ]:
            if v in var.lower(): break
        else:
            print warning("Could not renormalize WJ: variable %s is not a transverse mass variable!"%(var), prepend="  ")
            return
        
        # CHECK a, b (assume histogram range goes from 80 to >100 GeV)
        printVerbose(">>>   nBins=%s, (a,b)=(%s,%s)" % (nBins,a,b), verbosity)
        printVerbose(">>>   cuts=%s" % (cuts), verbosity)
        if a is not 80:
            print warning("Renormalizing WJ with %s > %s GeV, instead of mt > 80 GeV!" % (var,a), prepend="  ")
        if b < 150:
            print warning("Renormalizing WJ with %s < %s GeV < 150 GeV!" % (var,b), prepend="  ")
            return
        
        # GET WJ SAMPLE to set scale
        WJ = None
        WJs = [ ]
        for sample in samples:
            printVerbose(">>>   %s" % sample.label,verbosity,level=2)
            if "WJ" in sample.label or "w + jets" in sample.label.lower() or "w+jets" in sample.label.lower():
                WJs.append(sample)
                if "TES" in sample.label: print ">>>   note: %s" % (sample.label)
                
        # CHECK WJ SAMPLE
        if   len(WJs) == 1:
            WJ = WJs[0]
        elif len(WJs)  > 1:
            WJ = WJs[0]
            print warning("More than one WJ sample, renormalizing with first instance (%s)!" % (WJ.label), prepend="  ")
        else:
            print warning("Could not renormalize WJ: no WJ sample!", prepend="  ")
            return
                
        # GET WJ HIST to calculate scale
        histWJ = None
        histsWJ = [ ]
        for hist in self.histsMC:
            if "WJ" in hist.GetName() or "w-jets" in hist.GetName().lower():
                histsWJ.append(hist)
                
        # CHECK WJ HIST
        if   len(histsWJ) == 1:
            histWJ = histsWJ[0]
        elif len(histsWJ)  > 1:
            histWJ = histsWJ[0]
            print warning("More than one WJ sample, renormalizing with first instance (%s)!" % (histWJ.GetName()), prepend="  ")
        else:
            print warning("Could not renormalize WJ: no WJ sample!", prepend="  ")
            return
        
        # RESET SCALE
        #if WJ.scale and WJ.scaleBU:
        #    histWJ.Scale(WJ.scaleBU/WJ.scale)
        #WJ.scale = WJ.scaleBU
        
        # INTEGRATE
        I_MC = self.stack.GetStack().Last().Integral()
        I_D  = self.histsD[0].Integral()
        I_WJ = histWJ.Integral()
        R = self.ratio_WJ_QCD_SS
        if I_MC < 10:
            print warning("Could not renormalize WJ: integral of MC is %s < 10!" % I_MC, prepend="  ")
            return
        print ">>>   data: %.1f, MC: %.1f, WJ: %.1f, QCD: %.1f, R: %.3f, WJ prior purity: %.2f%%)" % (I_D,I_MC,I_WJ,I_QCD,R,I_WJ/I_MC)
        if I_D < 10:
            print warning("Could not renormalize WJ: integral of data is %s < 10!" % I_D, prepend="  ")
            return
        if I_WJ < 10:
            print warning("Could not renormalize WJ: integral of WJ is %s < 10!" % I_WJ, prepend="  ")
            return
        
        # SET WJ SCALE
        scale = ( I_D - I_MC + I_WJ - R*I_QCD ) / (I_WJ - R*I_QCD)
        
        if scale < 0:
            print warning("Could not renormalize WJ: scale = %.2f < 0!" % scale, prepend="  ")
            WJ.scale = WJ.scaleBU # use BU scale to overwrite previous renormalizations
            return
        WJ.scale = WJ.scaleBU * scale
        print ">>>   WJ renormalization scale = %.3f (new total scale = %.3f)" % (scale, WJ.scale)
        return scale
        
    
    
    def renormalizeTT(self,**kwargs):
        """Renormalize TT by requireing that MC and data has the same number of events in some control region:
              - category 1: ...
              - category 2: ...
           ..."""
        #printSameLine(">>>\n>>> %srenormalizing TT with met in TT CR" % (kwargs.get('prepend',"")))
        
        samples     = self.samples
        cuts        = self.cuts
        var         = self.var
        nBins       = self.nBins
        (a,b)       = (self.a,self.b)
        verbosity   = kwargs.get('verbosity',0)
        
        # STACK
        stack = THStack("stack","")
        printVerbose(" ",verbosity,level=2)
        for hist in self.histsMC:
            if "signal" in hist.GetName() or "Signal" in hist.GetName():
                printVerbose(">>>   ignored signal sample: %s" % (hist.GetName()),verbosity,level=2)
                continue
            if hist.Integral()<=0:
                print warning("Ignored %s with an integral of %s <= 0 !" % (hist.GetName(),hist.Integral()), prepend="  ")
            printVerbose(">>>   adding to stack %s (%.1f events)" % (hist.GetName(),hist.Integral()),verbosity,level=2)
            stack.Add(hist)
        self.stack = stack
        
        # CHECK MC and DATA
        if not self.histsMC:
            print warning("Could not renormalize TT: no MC!", prepend="  ")
            return
        if not self.stack:
            print warning("Could not renormalize TT: no stack!", prepend="  ")
            return
        if not self.histsD:
            print warning("Could not renormalize TT: no data!", prepend="  ")
            return
        
        # CHECK a, b
        printVerbose(">>>   nBins=%s, (a,b)=(%s,%s)" % (nBins,a,b), verbosity)
        printVerbose(">>>   cuts=%s" % (cuts), verbosity)
        if a < 0:
            print warning("Renormalizing TT with %s > %s GeV! Setting %s>0" % (var,a,var), prepend="  ")
            a = 0
        if b < 100:
            print warning("Renormalizing TT with %s < %s GeV < 100 GeV!" % (var,b), prepend="  ")
        
        # GET TT SAMPLE to set scale
        TT = None
        TTs = [ ]
        for sample in samples:
            printVerbose(">>>   %s" % sample.label,verbosity,level=2)
            if "TT" in sample.label or "ttbar" in sample.label.lower():
                TTs.append(sample)
                if "TES" in sample.label: print ">>>   note: %s" % (sample.label)
        
        # CHECK TT SAMPLE
        if   len(TTs) == 1:
            TT = TTs[0]
        elif len(TTs)  > 1:
            TT = TTs[0]
            print warning("More than one TT sample, renormalizing with first instance (%s)!" % (TT.label), prepend="  ")
        else:
            print warning("Could not renormalize TT: no TT sample!", prepend="  ")
            return
        
        # GET TT HIST to calculate scale
        histTT = None
        histsTT = [ ]
        for hist in self.histsMC:
            if "TT" in hist.GetName() or "ttbar" in hist.GetName().lower():
                histsTT.append(hist)
        
        # CHECK TT HIST
        if   len(histsTT) == 1:
            histTT = histsTT[0]
        elif len(histsTT)  > 1:
            histTT = histsTT[0]
            print warning("More than one TT sample, renormalizing with first instance (%s)!" % (histTT.GetName()), prepend="  ")
        else:
            print warning("Could not renormalize TT: no TT sample!", prepend="  ")
            return
        
        # INTEGRATE
        e_MC    = Double()
        e_D     = Double()
        e_TT    = Double()
        I_MC    = self.stack.GetStack().Last().IntegralAndError(1,nBins,e_MC)
        I_D     = self.histsD[0].IntegralAndError(1,nBins,e_D)
        I_TT    = histTT.IntegralAndError(1,nBins,e_TT)
        if I_MC < 5:
            print warning("Could not renormalize TT: integral of MC is %s < 5!" % I_MC, prepend="  ")
            return
        print ">>>   data: %.1f (%.3f), MC: %.1f (%.3f), TT: %.1f (%.3f) (%.1f%% TT prior purity)" % (I_D,e_D,I_MC,e_MC,I_TT,e_TT,I_TT/I_MC*100)
        if I_D < 5:
            print warning("Could not renormalize TT: integral of data is %s < 5!" % I_D, prepend="  ")
            return
        if I_TT < 5:
            print warning("Could not renormalize TT: integral of TT is %s < 5!" % I_TT, prepend="  ")
            return
        
        # SET TT SCALE
        scale       = ( I_D - I_MC + I_TT ) / (I_TT)
        err_scale   = scale * sqrt( (e_D**2+(e_MC-e_TT)**2)/abs(I_D-I_MC+I_TT)**2 + (e_TT/I_TT)**2 )
        
        if scale < 0:
            print warning("Could not renormalize TT: scale = %.2f < 0!" % scale, prepend="  ")
            TT.scale = TT.scaleBU # use BU scale to overwrite previous renormalizations
            return
        TT.scale = TT.scaleBU * scale
        print ">>>   TT renormalization scale = %.3f (%.3f) (new total scale = %.3f)" % (scale, err_scale, TT.scale)
        return scale
        


    def significanceScan(self,*args,**kwargs):
        """Scan cut on a range of some variable, integrating the signal and background histograms,
           calculating the S/(1+sqrt(B)) and finally drawing a histogram with these values."""
        # assume this Plot object has:
        #   - the appropriate backgrounds (WJ renormalization, QCD if necessary)
        #   - the appropriate cuts, selections, weights, etc.
        
        samples = self.samples
        cuts    = self.cuts
        var     = self.var
        nBins   = self.nBins
        a       = self.a
        b       = self.b
        samples = self.samples
        
        # CHECK MC and DATA
        if not self.histsB:
            print warning("Could not calculate significance: no background MC samples!")
            return
        if not self.stack:
            print warning("Could not calculate significance: no stack!")
            return
        if not self.histsS[0]:
            print warning("Could not calculate significance: no signal MC samples!")
            return
        
        # SET UP
        if len(args) is 2: kwargs['range'] = args
        (a0,b0)         = kwargs.get('range',(a,b))      # range to make cuts
        N               = max(kwargs.get('N',40),10)     # number of cuts in range
        lower           = not kwargs.get('upper',False)  # lower = ( var > cut ), upper = ( var < cut )
        signal          = self.histsS[0]
        stack           = self.stack
        graph_sigma     = TGraph(N)
        
        # CHECK SIGNAL SCALE
        norm   = 1
        for sample in samples:
            if sample.isSignal and sample.scale:
                norm = sample.scaleBU/sample.scale
                break
        #if signal.GetSumOfWeights():
        #    norm        = 5.0/signal.GetSumOfWeights() # signal yield renormalization
        
        # TODO: CHECKS
        if not N: N = 40
        if a0 < a: a0 = a
        if b0 > b: b0 = b
        
        # INTEGRATE
        cut         = 0
        width       = abs(b0-a0)
        sigma_max   = 0
        #N_totB          = stack.GetStack().Last().GetSumOfWeights()
        #N_totS          = signal.GetSumOfWeights()
        b_cut = b0
        a_cut = a0
        #print ">>>   cuts on %s with interval %.2f to %.2f" % (var,a0,b0)
        for i in range(N): # 0, ..., N
            if lower: # scan up on lower limit
                a_cut = a0 + float(i)*width/N
                cut = a_cut
            else:  # scan up on upper limit
                b_cut = b0 - float(N-i)*width/N
                cut = b_cut
            S = self.integrateHist(signal,a_cut,b_cut) * norm
            B = self.integrateStack(stack,a_cut,b_cut)
            sigma = S/(1+sqrt(B))
            #print ">>>   %i: %s cut of %6.2f with S = %.2f, B = %.2f, S/(1+sqrt(B)) = %.2f" % (i,("lower" if lower else "upper"),cut,S,B,sigma)
            if sigma_max < sigma: sigma_max = sigma
            graph_sigma.SetPoint(i,cut,sigma)
            # TODO: add error bars
        
        # DRAW
        W = 800; H  = 600
        T = 0.080*H
        B = 0.122*H
        L = 0.120*W
        R = 0.040*W
        coloreff = kAzure+4
        canvas = makeCanvas(name="canvas_sigma", scaleleftmargin=1.1)
        canvas.cd()
        frame = canvas.DrawFrame(1.4,0.001, 4.1, 10)
        frame.SetMinimum(0)
        frame.SetMaximum(sigma_max*1.05)
        frame.GetXaxis().SetLimits(a0,b0)
        frame.GetXaxis().SetTitleSize(0.045)
        frame.GetYaxis().SetTitleSize(0.050)
        frame.GetXaxis().SetLabelSize(0.040)
        frame.GetYaxis().SetLabelSize(0.038)
        frame.GetXaxis().SetTitleOffset(1.10)
        frame.GetYaxis().SetTitleOffset(1.30)
        frame.GetYaxis().SetTitle("S/(1+#sqrt{B})")
        frame.GetXaxis().SetTitle("%s cut on %s" % ("lower" if lower else "upper", makeLatex(var)))
        graph_sigma.SetLineColor(coloreff)
        graph_sigma.SetMarkerColor(coloreff)
        graph_sigma.SetMarkerSize(1)
        graph_sigma.SetLineWidth(2)
        graph_sigma.SetLineStyle(1)
        graph_sigma.Draw('PL') #E0
        frame.Draw('sameaxis')
        self.graph_sigma = graph_sigma
        self.canvas_sigma = canvas
        
        # CMS LUMI        
        #CMS_lumi.cmsTextSize  = 0.65
        #CMS_lumi.lumiTextSize = 0.60
        #CMS_lumi.relPosX = 0.105
        CMS_lumi.CMS_lumi(self.canvas_sigma,13,0)
        
        return
    

    
    def checkSignal(self,blindlimits=(),S_exp=0):
        """Check signal bump, signal region, signal yield, ..."""
        # TODO: use tree instead of histogram!
        var     = self.var
        signals = [s for s in self.samples if s.isSignal] 
        if len(blindlimits) is 2 and self.stack != None:
            for signal in signals:
                (aa,bb) = blindlimits
                name    = "m_sv_signal_check"
                shist   = signal.hist("m_sv",100,aa,bb,name=name,cuts=self.cuts,weight=self.weight,verbosity=self.verbosity)
                mu      = shist.GetMean()
                sd      = shist.GetStdDev()
                N       = shist.GetEntries()
                S       = shist.GetSumOfWeights()
                B       = self.integrateStack(aa,bb)
                scale   = -1
                upscale = -1
                norm    = 1
                if signal.scaleBU:
                    scale = signal.scale
                    upscale = signal.scale/signal.scaleBU
                    if upscale: S = S*signal.scaleBU/signal.scale
                gDirectory.Delete(name)
                print ">>> " + color("%.1f expected signal events (sum of weights) and %i MC events"     % (S,N), color="grey")
                print ">>> " + color("  signal mean = %.2f, sigma = %.2f, nBins = %d"                    % (mu,sd,self.nBins), color="grey")
                print ">>> " + color("  total scale = %.4f, upscale = %.1f"                              % (scale,upscale), color="grey")
                print ">>> " + color("  thus 1-sigma signal region should be [ %4.1f, %4.1f ]"           % (max(0,mu-1*sd),mu+1*sd), color="grey")
                print ">>> " + color("  thus 2-sigma signal region should be [ %4.1f, %4.1f ]"           % (max(0,mu-2*sd),mu+2*sd), color="grey")
                #print ">>> " + color("  %.1f expected signal events (%.1f%%) in signal region %s(%i,%i)" % (S,100*S/Sw,var,aa,bb), color="grey")
                print ">>> " + color("  %4.1f total expected signal events compared to dimuon analysis"  % (S_exp), color="grey")
                print ">>> " + color("  %4.1f (%.1f) expected signal events in signal region %s(%i,%i)"  % (S,S*283,var,aa,bb), color="grey")
                print ">>> " + color("  %4.1f expected background events in signal region %s(%i,%i)"     % (B,var,aa,bb), color="grey")
                if B:
                    sigma = S/(1+sqrt(B))
                    print ">>> " + color("  %.2f expected significance in signal region %s(%i,%i)"       % (sigma,var,aa,bb), color="grey")
                    print ">>> " + color("  &  %7.1f    &%6.2f &  %5.2f   &  %6.1f &  %5.1f"             % (B,S,sigma,S*283,sigma*283), color="grey")
        else: print warning("Could not check signal yield: \"len(blindlimits)==2\" = %s and \"plot.stack!=None\" = %s" % (len(blindlimits)==2,self.stack!=None))
        
        
        
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
        CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
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
        


from SampleTools import getSample, getHist

