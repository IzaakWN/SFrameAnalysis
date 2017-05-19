from ROOT import * #TFile, TCanvas, TH1F, TH2F, THStack, TAxis, TGaxis, TGraph...
import CMS_lumi, tdrstyle
from math import sqrt, pow, log
# from SampleTools import Samples, Sample
from PrintTools import color, warning, error, printSameLine, printVerbose, LoadingBar
#gROOT.Macro('PlotTools/functionmacro.C+')

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
colors     = [ kAzure+4,
               kRed+3, kAzure+4, kOrange-6, kGreen+3, kMagenta+3, kYellow+2,
               kRed-7, kAzure-4, kOrange+6, kGreen-2, kMagenta-3, kYellow-2 ]
fillcolors = [ kRed-2, kAzure+5,
               kMagenta-3, kYellow+771, kOrange-5,  kGreen-2,
               kRed-7, kAzure-9, kOrange+382,  kGreen+3,  kViolet+5, kYellow-2 ]
               #kYellow-3
               
varlist = { "jpt_1": "leading jet pt",               "jpt_2":  "leading jet pt",
            "bpt_1": "leading b jet pt",             "bpt_2":  "sub-leading b jet pt",
            "abs(jeta_1)": "leading jet abs(eta)",   "abs(jeta_2)": "sub-leading jet abs(eta)",
            "abs(beta_1)": "leading b jet abs(eta)", "abs(beta_2)": "sub-leading b jet abs(eta)",
            "jeta_1": "leading jet eta",             "jeta_2": "sub-leading jet eta",
            "beta_1": "leading b jet eta",           "beta_2": "sub-leading b jet eta",
            "njets":  "multiplicity of jets",
            "ncjets": "multiplicity of central jets",  "nfjets": "multiplicity of forward jets",
            "nbtag":  "multiplicity of b tagged jets", "ncbtag": "multiplicity of b tagged jets",
            "beta_1": "leading b jet eta",             "beta_2": "sub-leading b jet eta",
            "pt_tt":  "pt_ltau",                       "R_pt_m_vis": "R = pt_ltau / m_vis",
            "pt_tt_sv": "SVFit pt_ltau,sv",            "R_pt_m_sv":  "SVFit R_{sv} = pt_ltau / m_sv",
            "m_sv":   "SVFit m_sv",
            "dR_ll":  "#DeltaR_{ltau}",
            "pfmt_1": "PF mt_l", "met":"MET" }





def makeLatex(title):
    """Convert patterns in a string to LaTeX format."""
    
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
        
        if "eta" in string.lower():
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
    
    if "p_" in newtitle or "m_" in newtitle or "M_" in newtitle or "mass" in newtitle or "MET" in newtitle or "met" in newtitle:
        newtitle += " [GeV]"
    
    return newtitle
    
    
    
    
    
def makeHistName(label, var):
    """Use label and var to make an unique and valid histogram name."""
    hist_name = "%s_%s" % (label, var)
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
        if "||" in cuts: print warning("combineCuts: Be carefull with those \"or\" statements!")
        # [cut.strip() for i in cut.split('||')]
        
    if cuts:
        cuts = " && ".join(cuts)
        if weight:  cuts = "(%s)*%s" % (cuts, weight)
    elif weight:    cuts = weight
    else:           cuts = ""

    #print cuts
    return cuts
    




def makeCanvas(**kwargs):
    """Make canvas and pads for ratio plots."""
    
    square = kwargs.get('square', False)
    scaleleftmargin  = kwargs.get('scaleleftmargin', 1)
    scalerightmargin = kwargs.get('scalerightmargin', 1)
    scaletopmargin = kwargs.get('scaletopmargin', 1)
    name = kwargs.get('name', "canvas").replace(' ','_')
    #residue = kwargs.get('residue', False)
    #ratio = kwargs.get('ratio', False)
    
    W = 800; H  = 600
    if square:
        W = 800; H  = 800
        scalerightmargin = 3.5*scalerightmargin
    
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

    return canvas





class Ratio(object):
    """Class to make bundle histograms (ratio, stat. error on MC and line) for ratio plot."""

    def __init__(self, ratio, **kwargs):
        self.ratio      = ratio
        self.staterror  = kwargs.get('staterror', None)
        self.line       = kwargs.get('line', False)
    

    
    def Draw(self, option, **kwargs):
        """Draw all histograms"""
        
        a = self.ratio.GetXaxis().GetXmin()
        b = self.ratio.GetXaxis().GetXmax()
        
        self.ratio.Draw("E same")
        
        if self.staterror:
            self.staterror.Draw("E2 same")
            self.staterror.SetLineStyle(1)
            self.staterror.SetMarkerStyle(1)
            self.staterror.SetFillColor(kBlack)
            self.staterror.SetFillStyle(3004)
        
        if self.line:
            self.line = TLine(a,1,b,1)
            self.line.SetLineStyle(2)
            self.line.Draw("same") # only draw line if a histogram has been drawn!
        
        self.ratio.Draw("E same")





class Plot(object):
    """Class to automatically make CMS plot."""
    
    def __init__(self, samples, var, nBins, a, b, **kwargs):
        self.samples    = samples[:]
        self.var        = var
        self.nBins      = nBins
        self.a          = a
        self.b          = b
        self.cuts       = kwargs.get('cuts', "") # extra cuts
        self.weight     = kwargs.get('weight', "")
        self.shift_QCD  = kwargs.get('shift_QCD', 0)
        self.ratio_WJ_QCD_SS = kwargs.get('ratio_WJ_QCD_SS',0)
        self.ratio_TT_QCD_SS = kwargs.get('ratio_TT_QCD_SS',0)
        self.channel    = kwargs.get('channel', "mutau")
        
        self.histsS     = [ ]
        self.histsB     = [ ]
        self.histsD     = [ ]
        self._hists     = [ ]
        self._histsMC   = [ ]
        self.hist_error = None
        self.ratio      = None
        self.reset      = kwargs.get('reset', False)
        self.colors     = colors[:]
        self.fillcolors = fillcolors[:]
        self.ignore     = kwargs.get('ignore',[])
        self.verbosity  = kwargs.get('verbosity',0)
        self.loadingbar = kwargs.get('loadingbar', True) and not self.verbosity
        
        if self.loadingbar:
            bar = LoadingBar(len(samples),width=16,prepend=">>> %s: making histograms: " % (self.var),counter=True,remove=True)
        for sample in self.samples:
            if self.loadingbar: bar.message(sample.label)
            if self.reset: sample.scale = sample.scaleBU
            if sample.label in self.ignore:
                self.colors.pop(self.samples.index(sample))
                self.fillcolors.pop(self.samples.index(sample))
                if self.loadingbar: bar.count("%s skipped"%sample.label)
                continue
            if sample.isSignal and kwargs.get('signal', True):
                self.histsS.append(sample.hist(var, nBins, a, b, cuts=self.cuts, weight=self.weight, verbosity=self.verbosity))
            elif sample.isBackground and kwargs.get('background', True):
                self.histsB.append(sample.hist(var, nBins, a, b, cuts=self.cuts, weight=self.weight, verbosity=self.verbosity))
            elif sample.isData and kwargs.get('data', True):
                self.histsD.append(sample.hist(var, nBins, a, b, cuts=self.cuts,                     verbosity=self.verbosity))
            if self.loadingbar: bar.count("%s done"%sample.label)
        if kwargs.get('QCD', False):
            histQCD = self.QCD(ratio_WJ_QCD_SS=self.ratio_WJ_QCD_SS,ratio_TT_QCD_SS=self.ratio_TT_QCD_SS,verbosity=self.verbosity)
            if histQCD: self.histsB.append(histQCD)
        
        self.stack      = None
        self.canvas     = None
        self.graph_sigma  = None
        self.canvas_sigma = None
        self.pads       = [ ]
        self.frame      = None
        self.legend     = None
        self.width  = 0.11; self.height = 0.08 + 0.05 * len(self.histsB)
        self.x2     = 0.89; self.x1 = self.x2 - self.width
        self.y2     = 0.92; self.y1 = self.y2 - self.height
    
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



    def plot(self,*args,**kwargs):
        """Central method of Plot class: make plot with canvas, axis, error, ratio..."""
    
        # https://root.cern.ch/doc/master/classTHStack.html
        # https://root.cern.ch/doc/master/classTHistPainter.html#HP01e
        stack       = kwargs.get('stack',     False)
        residue     = kwargs.get('residue',   False) and self.histsD
        ratio       = kwargs.get('ratio',     False) and self.histsD
        errorbars   = kwargs.get('errorbars', False)
        staterror   = kwargs.get('staterror', False)
        norm        = kwargs.get('norm',      False)
        option      = 'hist' #+ kwargs.get('option', '')
        if errorbars: option = 'E0 '+option
        
        # CANVAS
        self.makeCanvas(  square=kwargs.get('square', False),
                          residue=residue, ratio=ratio,
                          scaleleftmargin=kwargs.get('scaleleftmargin', 1),
                          scalerightmargin=kwargs.get('scalerightmargin', 1)  )
        
        # MONTE CARLO
        if stack:
            stack = THStack("stack","")
            self.stack = stack
            for hist in self.histsB: stack.Add(hist)
            stack.Draw(option)
            for hist in self.histsS: hist.Draw(option+' same')
        else:
            for hist in self.histsMC: hist.Draw(option+' same')
        
        # DATA
        if kwargs.get('data', True):
            for hist in self.histsD:
                hist.Draw('E same')
        
        # NORM
        if norm: self.norm(self.hists)
        
        # STATISTICAL ERROR
        if staterror:
            self.hist_error = self.makeStatisticalError( self.histsB, name=makeHistName("stat_error",self.var),
                                                                       title="statistical error" )
            self.hist_error.Draw('E2 same')
            #if self.histS:                
            #    self.hist_error = self.makeStatisticalError( self.histsB, name=makeHistName("stat_error",self.var),
            #                                                               title="statistical error" )
            #    self.hist_error.Draw('E2 same')
        
        # STYLE
        if stack:
            self.setFillStyle(*self.histsB)
            for hist in self.histsMC: hist.SetMarkerStyle(1)
        else:
            self.setLineStyle(*self.histsB)
        if self.histsD:
            self.setMarkerStyle(*self.histsD)
        if self.histsS:
            self.setLineStyle(*self.histsS)
        
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
            self.ratio = self.ratioHistStack( self.histsD[0], self.stack, staterror=self.hist_error,
                                              name=makeHistName("ratio",self.var), title="ratio" )
            self.ratio.Draw("same")
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
        for hist in self.hists: gDirectory.Delete(hist.GetName())



    def makeCanvas(self,**kwargs):
        """Make canvas and pads for ratio plots."""
        
        square = kwargs.get('square', False)
        scaleleftmargin  = kwargs.get('scaleleftmargin', 1)
        scalerightmargin = kwargs.get('scalerightmargin', 1)
        scaletopmargin = kwargs.get('scaletopmargin', 1)
        residue = kwargs.get('residue', False)
        ratio = kwargs.get('ratio', False)
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
            pads = [ TPad("pad1","pad1", 0, 0.33, 1, 0.95),
                     TPad("pad2","pad2", 0, 0.05, 1, 0.30) ]
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
            self.pads = pads

        self.canvas = canvas



    def makeLegend(self,*args,**kwargs):
        """Make legend."""
        
        title = kwargs.get('title', None)
        entries = kwargs.get('entries', [ ])
        position = kwargs.get('position', "")
        transparent = kwargs.get('transparent', False)
        hists = self.hists
        histsS = self.histsS
        histsD = self.histsD
        x1 = self.x1; x2 = self.x2
        y1 = self.y1; y2 = self.y2
        width = self.width
        height = self.height
        
        styleD  = 'le'
        styleB = 'l'
        styleS = 'l'
        if self.stack: styleB = 'f'
        
        if position:
            if "LeftLeft" in position:      x1 = 0.15;      x2 =x1 + width
            elif "Left" in position:        x1 = 0.18;      x2 = x1 + width
            elif "RightRight" in position:  x2 = 1 - 0.10;  x1 = x2 - width
            elif "Right" in position:       x2 = 1 - 0.15;  x1 = x2 - width
            elif "Center" in position:      x1 = 0.55 - width/2;  x2 = 0.55 + width/2
            if "BottomBottom" in position:  y1 = 0.15;      y2 = y2 + height
            elif "Bottom" in position:      y1 = 0.20;      y2 = y2 + height
            elif "TopTop" in position:      y2 = 0.95;      y1 = y2 - height
            elif "Top" in position:         y1 = 0.93;      y2 = y1 - height
        legend = TLegend(x1,y1,x2,y2)
        
        if transparent: legend.SetFillStyle(0) # 0 = transparent
        else: legend.SetFillColor(kWhite)
        legend.SetBorderSize(0)
        legend.SetTextSize(legendTextSize)
                       
        if title is None: legend.SetHeader("")
        else: legend.SetHeader(title)

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
        """Make symmetric Y range around some center value."""
        
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
        
        frame = None
        ratio = kwargs.get('ratio', None)
        scale = 1
        
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
                mins.append(hist.GetMinimum())
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
            ylabel = ("Events / %.3f" % frame.GetXaxis().GetBinWidth(0)).rstrip("0").rstrip(".")
            if "GeV" in xlabel:
                ylabel += " GeV"
        
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
        if kwargs.get('noxaxis',False):
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

        if gen:
            colors2 = [kRed+3, kRed-7, kAzure+4, kAzure-4, kMagenta+3, kGreen+3, kOrange+6, kMagenta-3]
            line = [1,3,2,3]
            for i in range(len(hists)):
                hists[i].SetLineColor(self.colors2[i])
                hists[i].SetLineStyle(line[i%4])
                hists[i].SetLineWidth(3)
        else:
            for i in range(len(hists)):
                hists[i].SetLineColor(self.colors[i%len(self.colors)])
                hists[i].SetLineStyle(i%4+1)
                hists[i].SetLineWidth(3)



    def setFillStyle(self, *hists):
        """Make fill style."""
        
        #print ">>> setFillStyle"
        if len(hists) is 0: hists = self.hists
        for i in range(len(hists)):
            #hists[i].SetLineColor(colors[i%len(colors)])
            #hists[i].SetLineStyle(1)
            hists[i].SetFillColor(self.fillcolors[i%len(colors)])



    def setLineColor(self, *hists):
        """Make line color."""
        
        #print ">>> setLineColor"
        if len(hists) is 0: hists = self.hists
        for i in range(len(hists)):
            hists[i].SetLineColor(self.colors[i%len(colors)])
            hists[i].SetLineStyle(1)
            hists[i].SetLineWidth(3)



    def setMarkerStyle(self, *hists):
        """Make marker style."""
        
        #print ">>> setMarkerStyle"
        if len(hists) is 0: hists = self.hists
        for hist in hists:
            hist.SetMarkerStyle(20)
            hist.SetMarkerSize(0.8)



    def norm(self,*hists):
        """ Normalize histogram."""
        
        if isinstance(hists[0],list): hists = hists[0]
        if len(hists) is 0: hists = self.hists
        for hist in hists:
            I = hist.Integral()
            if I:
                hist.Scale(1/I)



    def makeStatisticalError(self,hists,**kwargs):
        """Make statistical error for a set of histograms."""
        
        name = kwargs.get('name', "error_"+hists[0].GetName())
        title = kwargs.get('title', "error")
        color = kwargs.get('color', kBlack)
        N = hists[0].GetNbinsX()
        a = hists[0].GetXaxis().GetXmin()
        b = hists[0].GetXaxis().GetXmax()
        hist_error = TH1F(name,title,N,a,b)
        
        for hist in hists:
            hist_error.Add(hist)
        #hist_error.Sumw2()
        
        hist_error.SetLineStyle(1);
        hist_error.SetMarkerSize(0);
        hist_error.SetFillColor(color);
        hist_error.SetFillStyle(3001);
        
        return hist_error
        
        
        
    def setStatisticalErrorStyle(self,hist_error,**kwargs):
        color = kwargs.get('color', kBlack)
        hist_error.SetLineStyle(1);
        hist_error.SetMarkerSize(0);
        hist_error.SetFillColor(color);
        hist_error.SetFillStyle(3001);
        
       
        
    def ratioError(self,a,ea,b,eb):
        """Calculate the error on a ratio a/b given errors ea on a and eb on b"""
        
        if b == 0:
            print warning("ratioError: cannot divide by zero!")
            return ea
        elif a == 0:
            return ea
        return abs(a/b) * sqrt( pow(ea/a,2) + pow(eb/b,2) )
        


    def ratioHistStack(self,hist0,stack,**kwargs):
        """Make a ratio of the data histogram / stacked MC histograms,
           bin by bin."""
        
        name = kwargs.get('name', "ratio_"+hist0.GetName())
        title = kwargs.get('title', "ratio")
        staterror = kwargs.get('staterror',True)
        N = hist0.GetNbinsX()
        a = hist0.GetXaxis().GetXmin()
        b = hist0.GetXaxis().GetXmax()
        hist_ratio = TH1F(name,title,N,a,b)
        hist_staterror = TH1F(name+"_staterror",title+" staterror",N,a,b)
        
        # dummy hist to get error and bin content of the stack
        hist_stack = TH1F("hist_stack","hist_stack",N,a,b)
        for hist in stack.GetStack():
            hist_stack.Add(hist)
        
        for i in range(1,N+1):
            stack_binc = stack.GetStack().Last().GetBinContent(i) #hist_stack.GetBinContent(i)
            hist_binc  = hist0.GetBinContent(i)
            if stack_binc:            
                hist_staterror.SetBinContent(i,1)
                hist_staterror.SetBinError(i,hist_stack.GetBinError(i)/stack_binc)
                if hist_binc and hist_binc / stack_binc < 100:
                    hist_ratio.SetBinContent(i, hist_binc / stack_binc );
                    hist_ratio.SetBinError(i, hist.GetBinError(i) / stack_binc ) # assume error on MC is 0
        #gDirectory.Delete(hist.GetName())
        
        if not staterror:
            hist_staterror = None
        
        return Ratio( hist_ratio, line=True, staterror=hist_staterror )
        


    def substractStackFromHist(self,stack,hist0,**kwargs):
        """Substract stacked MC histograms from a data histogram,
           bin by bin if the difference is larger than zero."""
        
        verbosity   = kwargs.get('verbosity', 0)
        name        = kwargs.get('name', "diff_"+hist0.GetName())
        title       = kwargs.get('title', "difference")
        nBins       = hist0.GetNbinsX()
        (a,b)       = (hist0.GetXaxis().GetXmin(), hist0.GetXaxis().GetXmax())
        hist_diff   = TH1F(name,title,nBins,a,b)
        stackhist   = stack.GetStack().Last()
        printVerbose(">>>\n>>> substractStackFromHist: %s - %s"%(name,title),verbosity)
        printVerbose(">>>   (BC = \"bin content\", BE = \"bin error\")",     verbosity)
        printVerbose(">>>   %4s  %9s  %8s  %8s  %8s  %8s  %8s"%("bin","data BC","data BE","MC BC","MC BE","QCD BC","QCD BE"), verbosity)
        
        for i in range(1,nBins+1):
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
        
        cuts            = self.cuts
        weight          = self.weight
        var             = self.var
        nBins           = self.nBins
        (a,b)           = (self.a,self.b)
        samples         = self.samples
        name            = kwargs.get('name',makeHistName("QCD",var))
        ratio_WJ_QCD_SS = self.ratio_WJ_QCD_SS or kwargs.get('ratio_WJ_QCD_SS',False)
        ratio_TT_QCD_SS = self.ratio_TT_QCD_SS or kwargs.get('ratio_TT_QCD_SS',False)
        verbosity       = kwargs.get('verbosity',False)
        printVerbose(">>>\n>>> estimating QCD for variable %s" % (self.var),verbosity,level=2)
        
        shift           = kwargs.get('shift',0.0) + self.shift_QCD
        scaleup         = 2.0 if "emu" in self.channel else 1.06
        scaleup         = kwargs.get('scaleup',scaleup)
        scale           = scaleup*(1.0+shift) # scale up QCD 6% in OS region by default
        printVerbose(">>>   QCD: scaleup = %s shift = %s, self.shift_QCD = %s" % (scaleup,shift,self.shift_QCD),verbosity,level=2)
        if "q_1*q_2>0" in cuts.replace(' ',''): scale = 1.0
        
        if "q_1*q_2<0" in cuts.replace(' ',''):
            cuts = cuts.replace("q_1 * q_2 < 0","q_1*q_2>0").replace("q_1*q_2 < 0","q_1*q_2>0").replace("q_1*q_2<0","q_1*q_2>0")        
        elif cuts:
            cuts = "q_1*q_2>0 && %s" % cuts
        else:
            cuts = "q_1*q_2>0"
            #print warning("Could not make QCD: no charge requirement")
            #return None
        printVerbose(">>>   QCD: cuts = %s" % (cuts),verbosity,level=2)
        
        histsMC_SS = [ ]
        histsD_SS  = [ ]
        histWJ = None
        histTT = None
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
                if ratio_TT_QCD_SS and ("TT" in hist.GetName() or "ttbar" in hist.GetName()):
                    if histTT: print warning("QCD: more than one ttbar sample in SS region, going with first instance!", prepend="  ")
                    else: histTT = hist
            elif sample.isData:
                histsD_SS.append(sample.hist(var, nBins, a, b, cuts=cuts, name=name_SS, verbosity=verbosity))
            if self.loadingbar: bar.count("%s done"%sample.label)
        if not histsD_SS:
            print warning("No data to make DATA driven QCD!")
            return None
        
        stack_SS = THStack("stack_SS","stack_SS")
        for hist in histsMC_SS: stack_SS.Add(hist)
        histQCD = self.substractStackFromHist(stack_SS,histsD_SS[0],name=name,title="QCD")
        QCD_SS = histQCD.Integral()
        histQCD.Scale(scale)
        if not histQCD: print warning("Could not make QCD! QCD histogram is none!", prepend="  ")
        
        if ratio_WJ_QCD_SS and histWJ:
            WJ_SS  = histWJ.Integral()
            if QCD_SS: ratio_WJ_QCD_SS = WJ_SS/QCD_SS
            else: print warning("QCD: QCD integral is 0!", prepend="  ")
            printVerbose(">>>   QCD: QCD = %.1f, WJ = %.1f, ratio_WJ_QCD_SS = %.3f" % (QCD_SS,WJ_SS,ratio_WJ_QCD_SS),verbosity,level=2)
            self.ratio_WJ_QCD_SS = ratio_WJ_QCD_SS
        else:
            printVerbose(">>>   QCD: QCD = %.1f, scale=%.3f" % (QCD_SS,scale),verbosity,level=2)
        
        if ratio_TT_QCD_SS and histTT:
            TT_SS  = histTT.Integral()
            if QCD_SS: ratio_TT_QCD_SS = TT_SS/QCD_SS
            else: print warning("QCD: QCD integral is 0!", prepend="  ")
            printVerbose(">>>\n>>>\n>>>   QCD: QCD = %.1f, TT = %.1f, ratio_TT_QCD_SS = %.3f" % (QCD_SS,TT_SS,ratio_TT_QCD_SS),verbosity,level=2)
            self.ratio_TT_QCD_SS = ratio_TT_QCD_SS
        
        for hist in histsMC_SS + histsD_SS:
            gDirectory.Delete(hist.GetName())
        
        return histQCD



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
        I_MC = self.stack.GetStack().Last().Integral()
        I_D  = self.histsD[0].Integral()
        I_TT = histTT.Integral()
        if I_MC < 5:
            print warning("Could not renormalize TT: integral of MC is %s < 5!" % I_MC, prepend="  ")
            return
        print ">>>   data: %.1f, MC: %.1f, TT: %.1f (%.1f%% TT prior purity)" % (I_D,I_MC,I_TT,I_TT/I_MC*100)
        if I_D < 5:
            print warning("Could not renormalize TT: integral of data is %s < 5!" % I_D, prepend="  ")
            return
        if I_TT < 5:
            print warning("Could not renormalize TT: integral of TT is %s < 5!" % I_TT, prepend="  ")
            return
        
        # SET TT SCALE
        scale = ( I_D - I_MC + I_TT ) / (I_TT)
        
        if scale < 0:
            print warning("Could not renormalize TT: scale = %.2f < 0!" % scale, prepend="  ")
            TT.scale = TT.scaleBU # use BU scale to overwrite previous renormalizations
            return
        TT.scale = TT.scaleBU * scale
        print ">>>   TT renormalization scale = %.3f (new total scale = %.3f)" % (scale, TT.scale)
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
        graph_sigma.SetLineColor(colors[0])
        graph_sigma.SetMarkerColor(colors[0])
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
        


from SampleTools import getSample

