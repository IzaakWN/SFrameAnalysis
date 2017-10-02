#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
sys.path.append('./fit/PDFs')
import PlotTools.PlotTools
from PlotTools.PlotTools import Comparison, makeRatio, makeCanvas, makeStatisticalError, combineWeights, makeLatex
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.PrintTools import color, warning, error, printSameLine, header
import ROOT
from ROOT import gPad, gROOT, gSystem, gStyle, gRandom, gDirectory, TFile, TTree, TH1F, TH2F, THStack, TCanvas, TLegend,\
                 TText, TLatex, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta, kDashed, kDotted, kTRUE, TLine
gSystem.Load("fit/PDFs/HWWLVJRooPdfs_cxx.so")
from ROOT import RooRealVar, RooArgSet, RooArgList, RooGaussian, RooLandau, RooDataHist, RooAddPdf, RooErfExpPdf
from ROOT.RooFit import Title, LineStyle, LineColor, Binning, Components, Name, Normalization,\
                        Import, Cut, SumW2Error, Save, Range, ConditionalObservables
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

SFRAME_DIR = "SFrameAnalysis_Moriond"
DIR = "/shome/ineuteli/analysis/%s/AnalysisOutput/" % (SFRAME_DIR)
MORIOND_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
OUT_DIR = "fit"
mylabel = "_Moriond"

# CMS style
lumi = 35.9 # 12.9
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.105
CMS_lumi.outOfFrame = True
CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
tdrstyle.setTDRStyle()

colors     = [ kRed+3, kAzure+4, kOrange-6, kGreen+3, kMagenta+3, kYellow+2,
               kRed-7, kAzure-4, kOrange+6, kGreen-2, kMagenta-3, kYellow-2 ]



def fitVars():
    print ">>>\n>>> fit variables()"
    
    from ROOT import RooRealVar, RooArgSet, RooGaussian, RooLandau
    from ROOT.RooFit import LineColor, Title, Binning, Import, Cut
    
    mylabel     = "_Moriond"
    channel     = "mutau"
    weight      = "weight*trigweight_or_1*ttptweight_runI/ttptweight"
    treename    = "tree_%s_cut_relaxed"%channel
    
    triggers    = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
    category1   = "ncjets == 1 && nfjets  > 0 && ncbtag > 0"
    category2   = "ncjets == 2 && nfjets == 0 && ncbtag > 0 && dphi_ll_bj>2 && met<60"
    category12  = "ncjets == 1 && nfjets  > 0 && ncbtag > 0 && met<60 && pfmt_1<60"
    category22  = "ncjets == 2 && nfjets == 0 && ncbtag > 0 && dphi_ll_bj>2 && met<60 && pfmt_1<60"
    
    
    samples  = [
        ("TT",  "TT_TuneCUETP8M1",                  "ttbar",        831.76 ),
        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50", 18610.0 ),
        #("DY",  "DYJetsToLL_M-50_TuneCUETP8M1",     "DY M-50",      4954.0 ),
    ]
    cuts = [
        #("no cuts",  "channel>0"),
        #("baseline",            "%s"       % (baseline)),
#         ("category 1",                        "%s && %s" % (baseline,category1)),
#         ("category 2",                        "%s && %s" % (baseline,category2)),
#         ("category 12",                       "%s && %s" % (baseline,category12)),
#         ("category 22",                       "%s && %s" % (baseline,category22)),
#         ("category 1, single muon triggers",    "%s && %s && %s" % (baseline,category1,"triggers==1")),
#         ("category 1, cross flavour triggers",  "%s && %s && %s" % (baseline,category1,"triggers==2")),
#         ("category 1, all triggers",            "%s && %s && %s" % (baseline,category1,"triggers==3")),
#         ("category 2, single muon triggers",    "%s && %s && %s" % (baseline,category2,"triggers==1")),
#         ("category 2, cross flavour triggers",  "%s && %s && %s" % (baseline,category2,"triggers==2")),
#         ("category 2, all triggers",            "%s && %s && %s" % (baseline,category2,"triggers==3")),
        ("category 2, single muon triggers",    "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2<5")),
        ("category 2, single muon triggers",    "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==5")),
        ("category 2, single muon triggers",    "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==6")),
    ]
    vars = [
        ("m_sv","SVFit mass",70,0,350),
    ]
    
    for isample, (sampledir,samplename,samplelabel,sigma) in enumerate(samples,1):
        print ">>>\n>>> %s: %s" %(isample,samplelabel)
        file   = TFile("%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,sampledir,samplename,mylabel))
        tree   = file.Get(treename)
        hist   = file.Get("histogram_mutau/cutflow_mutau")
        if not hist: hist = file.Get("histogram_emu/cutflow_emu")
        N_tot  = hist.GetBinContent(8)
        N_tot0 = hist.GetBinContent(1)
        scale  = lumi * sigma * 1000 / N_tot
        for var, vartitle, N, a, b in vars:
            for cutname, cut in cuts:
                print color("%s - %s" %(vartitle,cutname), color='grey', prepend=">>>\n>>>   ")
                cut   = "(%s)*%s*%s"%(cut,weight,scale)
                print ">>>   %s" %(cut)
                
                hist1 = TH1F("hist1", "hist_%s_%s"%(var,samplename),N,a,b)
                tree.Draw("%s >> hist1"%(var),cut,"gOff")
                
                I1   = hist1.Integral()
                ymax = hist1.GetMaximum()
                print ">>>   %s has %d entries" % (hist1.GetName(),I1)
                #if I:
                    #hist1.Scale(1./I)
                
                x         = RooRealVar("x","x",a,b)
                x.setRange("signal",15,b)
                dataHist  = RooDataHist("dataHist","dataHist",RooArgList(x),Import(hist1))
                
                
                mean_g1   = RooRealVar("mean_g1", "mean of gaussian 1",   100, 20,200)
                sigma_g1  = RooRealVar("sigma_g1","width of gaussian 1",   40,  0,220)
                gauss1    = RooGaussian("gauss1", "gauss1",x,mean_g1,sigma_g1)
                
                mean_g2   = RooRealVar("mean_g2", "mean of gaussian 2",    40, 20, 80)
                sigma_g2  = RooRealVar("sigma_g2","width of gaussian 2",   10,  0, 40)
                gauss2    = RooGaussian("gauss2", "gauss2",x,mean_g2,sigma_g2)
                
                
                mean_l1   = RooRealVar("mean_l1", "mean of landau 1",     120, 70,160) # 50
                sigma_l1  = RooRealVar("sigma_l1","width of landau 1",     30, 10,100)
                landau1   = RooLandau("landau1",  "landau1",x,mean_l1,sigma_l1)
                
                mean_l2   = RooRealVar("mean_l2", "mean of landau 2",      40, 10, 50)
                sigma_l2  = RooRealVar("sigma_l2","width of landau ",      10,  4, 40)
                landau2   = RooLandau("landau2",  "landau2",x,mean_l2,sigma_l2)
                
                mean_l3   = RooRealVar("mean_l3", "mean of landau 3",      60, 50,110)
                sigma_l3  = RooRealVar("sigma_l3","width of landau ",      20,  4, 80)
                landau3   = RooLandau("landau3",  "landau3",x,mean_l3,sigma_l3)
                
                
                offset_e1 = RooRealVar("offset_e1","offset of erfExp1 ",   90, 20,200)
                width_e1  = RooRealVar("width_e1", "width of erfExp1",    100, 10,200)
                const_e1  = RooRealVar("const_e1", "const of erfExp1",  -0.05, -2,  0)
                erfExp1   = RooErfExpPdf("erfExp1","erfExp1",x,const_e1,offset_e1,width_e1)
                
                offset_e2 = RooRealVar("offset_e2","offset of erfExp2 ",   40, 25,150) #35
                width_e2  = RooRealVar("width_e2", "width of erfExp2",     20,  4,100)
                const_e2  = RooRealVar("const_e2", "const of erfExp2",  -0.05, -2,  0)
                erfExp2   = RooErfExpPdf("erfExp2","erfExp2",x,const_e2,offset_e2,width_e2)
                
                offset_e3 = RooRealVar("offset_e3","offset of erfExp3 ",   60, 40,150)
                width_e3  = RooRealVar("width_e3", "width of erfExp3",     40,  4,100)
                const_e3  = RooRealVar("const_e3", "const of erfExp3",  -0.06, -2,  0)
                erfExp3   = RooErfExpPdf("erfExp3","erfExp3",x,const_e3,offset_e3,width_e3)
                
                offset_e4 = RooRealVar("offset_e4","offset of erfExp4 ",   60, 40,150)
                width_e4  = RooRealVar("width_e4", "width of erfExp4",     40,  5,100)
                const_e4  = RooRealVar("const_e4", "const of erfExp4",  -0.06, -2,  0)
                erfExp4   = RooErfExpPdf("erfExp4","erfExp4",x,const_e4,offset_e4,width_e4)
                
                
                pdf_dict = { "gauss1":  gauss1,   "gauss2":  gauss2,
                             "landau1": landau1,  "landau2": landau2,  "landau3": landau3,
                             "erfExp1": erfExp1,  "erfExp2": erfExp2,  "erfExp3": erfExp3,  "erfExp4": erfExp4,
                }
                
                models = [
#                     ("landau1",),
#                     ("landau1", "gauss2" ),
#                     ("landau1", "landau2"),
#                     ("landau1", "landau2", "landau3"),
                    ("erfExp1",),
#                     ("erfExp1", "gauss2" ),
                    ("erfExp1", "erfExp2"),
#                     ("erfExp1", "erfExp2", "erfExp3"),
                ]
                
                pdf_colors = [ kOrange, kMagenta, kRed, kGreen+1 ]
                
                model_label = "-25" #-35"
                for pdfs in models:
                    
                    # NAMING
                    pdfnames = [pdfname[:-1] for pdfname in pdfs]
                    modelname  = ""
                    for pdfname in sorted(set(pdfnames),key=pdfnames.index):
                        modelname += "%d%s-"%(pdfnames.count(pdfname),pdfname)
                    modelname = modelname.rstrip('-') + model_label
                    
                    # MODEL
                    print color("     MODEL %s"%modelname,color='magenta',prepend=">>>\n>>>\n>>>")
                    print ">>>\n>>>\n"
                    model    = None
                    fracs    = [ ]
                    argsets  = [ ]
                    arglists = [ ]
                    titles   = [ ]
                    models   = [ ]
                    if len(pdfs) is 1:
                        model = pdf_dict[pdfs[0]]
                    else:
                        frac1   = RooRealVar("frac1","fraction 1",0.70,0.07,0.95)
                        arglist = RooArgList(*[pdf_dict[pdfname] for pdfname in pdfs[:2]])
                        model1  = RooAddPdf("model1","model 1",arglist,RooArgList(frac1))
                        fracs.append(frac1)
                        arglists.append(arglist)
                        models.append(model1)
                        model   = model1
                        for i, pdfname in enumerate(pdfs[2:],2):
                            frac    = RooRealVar("frac%d"%i,"fraction %d"%i,0.20,0.10,0.95)
                            arglist = RooArgList(model,pdf_dict[pdfs[i]])
                            model   = RooAddPdf("model%d"%i,"model %d"%i,arglist,RooArgList(frac))
                            fracs.append(frac)
                            arglists.append(arglist)
                            models.append(model)
                            model   = models[-1]
                    
                    
                    # FIT
                    result = model.fitTo(dataHist,SumW2Error(True),Save(kTRUE),Range("signal"))
                    #print ">\n>> result:\n"
                    #print result.Print()
                    
                    # PLOT
                    frame1  = x.frame() # RooPlot
                    dataHist.plotOn(frame1,Name("data"))
                    model.plotOn(frame1, Name(model.GetName()))
                    titles.append(( model.GetName(), makePdfLegendTitle(model,x) ))
                    if len(pdfs) > 1:
                        for i, (pdfname, pdf_color) in enumerate(zip(pdfs,pdf_colors),1):
                            pdf    = pdf_dict[pdfname]
                            name   = pdf.GetName()
                            fraci   = calculateFraction(i,fracs)
                            argset = RooArgSet(pdf)
                            model.plotOn(frame1,Components(argset),LineColor(pdf_color),LineStyle(kDashed),Name(name))
                            titles.append(( name, makePdfLegendTitle(pdf,x,fraction=fraci) ))
                    chi2 = frame1.chiSquare(model.GetName(),"data")
                    
                    # DRAW
                    #gStyle.SetOptStat(0)
                    canvas = TCanvas("canvas","canvas",100,100,1000,1000)
                    canvas.Divide(2)
                    canvas.cd(1)
                    gPad.SetPad("pad1","pad1",0,0.33,1,1,0,-1,0)
                    gPad.SetTopMargin(0.10); gPad.SetBottomMargin(0.03)
                    gPad.SetLeftMargin(0.14); gPad.SetRightMargin(0.04)
                    gPad.SetBorderMode(0)
                    gStyle.SetTitleFontSize(0.062)
                    frame1.GetYaxis().SetTitle("Events / %.3g GeV"%frame1.getFitRangeBinW())
                    frame1.GetYaxis().SetTitleSize(0.059)
                    frame1.GetYaxis().SetTitleOffset(1.21)
                    #frame1.GetYaxis().SetRangeUser(0,ymax*1.12)
                    frame1.SetMaximum(1.05*frame1.GetMaximum())
                    #frame1.GetYaxis().SetLabelOffset(0.010)
                    frame1.GetXaxis().SetLabelSize(0); frame1.GetYaxis().SetLabelSize(0.045)
                    frame1.Draw()
                    
                    # LEGEND
                    title = "%s: %s"%(channel,cutname)
                    title = title.replace("category 1","1b1f").replace("category 2","1b1c").replace("mutau","#mutau").replace("tau","#tau")
                    fontsize = 0.043
                    (x1,y1) = (0.59,0.82)
                    (w,h)   = (0.18,0.10+0.05*len(titles))
                    (x2,y2) = (x1+w,y1-h)
                    legend  = TLegend(x1,y1,x2,y2)
                    legend.SetTextSize(fontsize)
                    legend.SetHeader(title)
                    legend.SetTextFont(42)
                    legend.SetBorderSize(0)
                    legend.SetFillStyle(0)
                    legend.AddEntry("data",samplelabel,'LEP')
                    #print legend.GetMargin()
                    for name, title in titles:
                        #print name, title
                        legend.AddEntry(name,title,'L')
                    legend.Draw()
                    
                    # TEXT
                    chi2_text = "#chi^{2} = %6.3f"%(chi2)
                    text = TLatex()
                    text.SetNDC() # Normalized Device Coordinates
                    text.SetTextFont(42)
                    text.SetTextSize(fontsize) #*0.90
                    text.SetTextAlign(13) # centered: 22
                    #text.DrawLatex(0.80*b,ymax*0.94,"#chi^{2} = %6.3f"%(chi2))
                    offset = (legend.GetX2()-legend.GetX1())*legend.GetMargin()*1.04
                    text.DrawLatexNDC(legend.GetX1()+offset,legend.GetY1()-0.01,chi2_text)
                    
                    # RATIO
                    pullHist = frame1.pullHist("data",model.GetName())
                    frame2 = x.frame()
                    frame2.addPlotable(pullHist,"P")
                    canvas.cd(2)
                    gPad.SetPad("pad2","pad2",0,0,1,0.33,0,-1,0)
                    gPad.SetTopMargin(0.01); gPad.SetBottomMargin(0.30)
                    gPad.SetLeftMargin(0.14); gPad.SetRightMargin(0.04)
                    gPad.SetBorderMode(0)
                    gPad.SetGridy(kTRUE)
                    line1 = TLine(frame2.GetXaxis().GetXmin(),0,frame2.GetXaxis().GetXmax(),0)
                    line2 = TLine(frame2.GetXaxis().GetXmin(),0,frame2.GetXaxis().GetXmax(),0)
                    line1.SetLineColor(0) # white to clear dotted grid lines
                    line2.SetLineColor(12) # dark grey
                    line2.SetLineStyle(2)
                    frame2.SetTitle("")
                    frame2.GetYaxis().SetTitle("pull")
                    frame2.GetXaxis().SetTitle(makeLatex(var))
                    frame2.GetXaxis().SetTitleSize(0.13);   frame2.GetYaxis().SetTitleSize(0.12)
                    frame2.GetXaxis().SetTitleOffset(1.0);  frame2.GetYaxis().SetTitleOffset(0.58)
                    frame2.GetXaxis().SetLabelSize(0.10);   frame2.GetYaxis().SetLabelSize(0.10)
                    frame2.GetXaxis().SetLabelOffset(0.02); frame2.GetYaxis().SetLabelOffset(0.01)
                    frame2.GetYaxis().SetRangeUser(-5,5)
                    #frame2.GetXaxis().SetRangeUser(0,5) # does not work ?
                    frame2.GetYaxis().CenterTitle(True)
                    frame2.GetYaxis().SetNdivisions(505)
                    frame2.Draw("")
                    line1.Draw("SAME")
                    line2.Draw("SAME")
                    frame2.Draw("SAME")
                    
                    # SAVE
                    cutname1    = cutname.replace(', ','-').replace(' ','_').replace('(','-').replace(')','')
                    filename    = ("%s/%s_%s_%s-%s_fit-%s.png"%(OUT_DIR,var,samplelabel,channel,cutname1,modelname)).replace(' ','_')
                    canvas.SaveAs(filename)
                    canvas.Close()
                    print
                    #print ">>>\n>>>"
        
        ROOT.gDirectory.Delete(hist1.GetName())                    
        file.Close()
            


def fitUnbinnedVars():
    print ">>>\n>>> fit variables with unbinned datasets"
    
    importRooFit()
    
    mylabel     = "_Moriond"
    channel     = "mutau"
    weight      = "weight*trigweight_or_1"
    treename    = "tree_%s_cut_relaxed"%channel
    
    triggers    = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
    category1   = "ncjets == 1 && nfjets  > 0 && nbtag > 1"
    category2   = "ncjets == 2 && nfjets == 0 && nbtag > 1 && dphi_ll_bj>2 && met<60"
    
    samples  = [
        ("TT",  "TT_TuneCUETP8M1",                  "ttbar",        831.76 ),
        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50", 18610.0 ),
        #("DY",  "DYJetsToLL_M-50_TuneCUETP8M1",     "DY M-50",      4954.0 ),
    ]
    cuts = [
        ("category 1",          "%s && %s" % (baseline,category1)),
        ("category 2",          "%s && %s" % (baseline,category2)),
    ]
    vars = [
        ("m_sv","SVFit mass",70,0,350),
    ]
    
    for i, (sampledir,samplename,samplelabel,sigma) in enumerate(samples,1):
        print ">>>\n>>> %s: %s" %(i,samplelabel)
        for var, vartitle, N, a, b in vars:
            for cutname, cut in cuts:
                print ">>>\n>>>   %s - %s" %(vartitle,cutname)
                cut   = "(%s)*%s"%(cut,weight)
                print ">>>   %s" %(cut)
                
                oldfilename = "%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,sampledir,samplename,mylabel)
                oldtreename = treename
                newfilename = "%s/fit.root"%(OUT_DIR)
                newtreename = "tree_%s"%(samplelabel.replace(' ','_'))
                newdirname  = cutname.replace(' ','_').replace('(','-').replace(')','')
                writeCutTreeToFile(oldfilename,oldtreename,newfilename,newtreename,cut,overwrite=True,newdirname=newdirname)
                
#                 file  = TFile("%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,sampledir,samplename,mylabel))
#                 tree  = file.Get(treename)
#                 hist1 = TH1F("hist1", "hist_%s_%s"%(var,samplename),N,a,b)
#                 tree.Draw("%s >> hist1"%(var),cut,"gOff")
#                 
#                 maxs = [ ] 
#                 I = hist1.Integral()
#                 print ">>>   %s has %d entries" % (hist1.GetName(),I)
#                 if I:
#                     #hist1.Scale(1./I)
#                     maxs.append(hist1.GetMaximum())
#                 
#                 canvas = TCanvas("canvas","canvas",100,100,800,600)
#                 canvas.SetBottomMargin(0.12)
#                 canvas.SetRightMargin(0.05)
#                 canvas.SetLeftMargin(0.12)
#                 canvas.SetTopMargin(0.05)
#                 hist1.SetLineWidth(3)
#                 hist1.SetLineStyle(1)
#                 hist1.SetLineColor(kAzure+4)
#                 hist1.Draw("hist")
#                 #hist1.SetTitle("%s: %s"%(samplelabel,cutname))
#                 
#                 #hist1.GetXaxis().SetTitle("trigger weight")
#                 hist1.GetYaxis().SetTitle("A.U.")
#                 hist1.GetXaxis().SetTitleSize(0.06)
#                 hist1.GetYaxis().SetTitleSize(0.06)
#                 hist1.GetXaxis().SetTitleOffset(0.9)
#                 hist1.GetYaxis().SetTitleOffset(0.9)
#                 hist1.GetXaxis().SetLabelSize(0.080)
#                 hist1.GetYaxis().SetLabelSize(0.045)
#                 hist1.GetYaxis().SetRangeUser(0,max(maxs)*1.08)
#                 
#                 # title = "%s: %s"%(samplelabel,cutname)
#                 # (x1,y1) = (0.48,0.88)
#                 # (w,h)   = (0.18,0.24)
#                 # (x2,y2) = (x1+w,y1-h)
#                 # legend = TLegend(x1,y1,x2,y2)
#                 # legend.SetHeader(title)
#                 # legend.SetTextFont(42)
#                 # legend.SetTextSize(0.045)
#                 # legend.SetBorderSize(0)
#                 # legend.SetFillStyle(0)
#                 # legend.Draw()
#                 
#                 gStyle.SetOptStat(0)
#                 cutname     = cutname.replace(' ','_').replace('(','-').replace(')','')
#                 filename    = ("%s/fit_%s_%s_%s.png"%(OUT_DIR,var,samplelabel,cutname)).replace(' ','_')
#                 canvas.SaveAs(filename)
#                 canvas.Close()
#                 ROOT.gDirectory.Delete(hist1.GetName())
#                 
#                 file.Close()
            


def writeCutTreeToFile(oldfilename,oldtreename,newfilename,newtreename,cut,overwrite=True,newdirname=""):
    """Write a tree to a file. Overwrite the tree by default, If the tree already exist."""
    
    newfile = TFile(newfilename,"UPDATE")
    oldfile = TFile(oldfilename,"READ")
    newtree = newfile.Get(newtreename)
    if overwrite or not newtree:
        
        if newdirname: # go to directory, and create it if it does not exist
            newdir = newfile.GetDirectory(newdirname)
            if not newdir:
                print ">>> created directory %s"%(newdirname)
                newdir = newfile.mkdir(newdirname)
            newdir.cd()
        
        oldtree = oldfile.Get(oldtreename)
        newtree = oldtree.CopyTree(cut)
        newtree.Write(newtreename,TTree.kOverwrite)
    oldfile.Close()
    newfile.Close()
    


def makePdfLegendTitle(pdf,x,fraction=""):
    name = pdf.GetName().lower()
    params = pdf.getParameters(RooArgSet(x))
    if fraction: fraction = "#scale[0.85]{%4.1f%%} "%(fraction*100)
    if "landau" in name:
        return fraction+"Landau(#scale[0.85]{%.3g,%.3g})" %\
            (params.selectByName("mean*").first().getVal(),
             params.selectByName("sigma*").first().getVal())
    elif "gauss" in name:
        return fraction+"Gauss(#scale[0.85]{%.3g,%.3g})" %\
            (params.selectByName("mean*").first().getVal(),
             params.selectByName("sigma*").first().getVal())
    elif "erfexp" in name:
        return fraction+"#scale[0.92]{ErfExp(#scale[0.85]{%.3g,%.3g,%.2g})}" %\
            (params.selectByName("offset*").first().getVal(),
             params.selectByName("width*").first().getVal(),
             params.selectByName("const*").first().getVal())
    elif "model" in name:
        return "model"
    return fraction+name
    



def calculateFraction(i,fracs):
    """Calculate fraction for RooFit model of several summed up pdfs"""
    fraci  = 1
    if i is 1:  fraci  = fracs[0].getVal()
    else:       fraci  = (1-fracs[i-2].getVal())
    fraci0 = max(1,i-1)
    for frac in fracs[fraci0:len(fracs)]: fraci *= frac.getVal()
    return fraci

def testCalculateFraction():
    """Test logic of fraction calculation for RooFit model of several summed up pdfs"""
    #  2 pdf model:           f1 +          (1-f1)
    #  3 pdf model:        f2*f1 +       f2*(1-f1) +       (1-f2)
    #  4 pdf model:     f3*f2*f1 +    f3*f2*(1-f1) +    f3*(1-f2) +    (1-f3)
    #  5 pdf model:  f4*f3*f2*f1 + f4*f3*f2*(1-f1) + f4*f3*(1-f2) + f4*(1-f3) + (1-f4)

    fracs0 = [0.50,0.30,0.10,0.06,0.04,0.01,0.05]
    
    print
    for n in range(2,6):
        print ">>> n = %s"%n
        formulas = ""
        fracs = fracs0[:n-1]
        print ">>>      %s"%fracs
        for i in range(1,n+1):
            fraci = 1
            if i is 1:
                fraci    = fracs[0]
                formulas += "f%d"%i
            else:
                fraci = (1-fracs[i-2])
                formulas += "(1-f%d)"%(i-1)
            fraci0 = max(1,i-1)
            print ">>>   %d: %s"%(i,fracs[fraci0:len(fracs)])
            for j, frac in enumerate(fracs[fraci0:len(fracs)],fraci0):
                fraci    *= frac
                formulas += "*f%d"%(j+1)
            formulas += " (%.1f%%),  "%(100*fraci)
        print ">>>   %s\n>>>"%(formulas)
    print
    


def ratioTest():
    """Example of how to use the makeRatio function from PlotTools."""
    
    pads = []
    canvas = makeCanvas(ratio=True,pads=pads)
    hist1 = TH1F("hist1","hist1",50,0,100)
    hist2 = TH1F("hist2","hist2",50,0,100)
    
    for i in xrange(10000):
        hist1.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
        hist2.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
    stats = makeStatisticalError(hist2)
    ratio = makeRatio(hist1,hist2,staterror=True)
    
    pads[0].cd()
    hist1.Draw("E")
    hist2.Draw("HIST SAME")
    stats.Draw("E2 SAME")
    
    pads[1].cd()
    ratio.Draw("SAME")
    
    canvas.SaveAs("ratio_test.png")
    


def pullTest():
    """Example of how to use the RooPlot::pullHist to make a pull bottom plot.
       Inspired from rf109_chi2residpull.C"""
    
    # MODEL
    x     = RooRealVar("x","x",-10,10)
    sigma = RooRealVar("sigma","sigma",3,0.1,10)
    mean  = RooRealVar("mean","mean",0,-10,10)
    gauss = RooGaussian("gauss","gauss",x,RooConst(0),sigma) # RooConst(0) gives segfaults
    data  = gauss.generate(RooArgSet(x),100000) # RooDataSet
    sigma.setVal(3.15)    
    frame1 = x.frame(Title("Data with distorted Gaussian pdf"),Bins(40)) # RooPlot
    data.plotOn(frame1,DataError(RooAbsData.SumW2))
    gauss.plotOn(frame1)
    hresid = frame1.residHist() # RooHist
    hpull  = frame1.pullHist() # RooHist
    frame2 = x.frame(Title("Residual Distribution")) # RooPlot
    frame2.addPlotable(hresid,"P")
    frame3 = x.frame(Title("Pull Distribution")) # RooPlot
    frame3.addPlotable(hpull,"P")
    
    # PLOT
    print ">>> draw with pull plot..."
    canvas = TCanvas("canvas","canvas",100,100,1000,1000)
    canvas.Divide(2)
    canvas.cd(1)
    gPad.SetPad("pad1","pad1",0,0.33,1,1,0,-1,0)
    gPad.SetTopMargin(0.10); gPad.SetBottomMargin(0.03)
    gPad.SetLeftMargin(0.14); gPad.SetRightMargin(0.04)
    gPad.SetBorderMode(0)
    gStyle.SetTitleFontSize(0.062)
    frame1.GetYaxis().SetTitle("Events / %.3g GeV"%frame1.getFitRangeBinW())
    frame1.GetYaxis().SetTitleSize(0.059)
    frame1.GetYaxis().SetTitleOffset(1.21)
    #frame1.GetYaxis().SetLabelOffset(0.010)
    frame1.GetXaxis().SetLabelSize(0); frame1.GetYaxis().SetLabelSize(0.045)
    frame1.Draw()
    canvas.cd(2)
    gPad.SetPad("pad2","pad2",0,0,1,0.33,0,-1,0)
    gPad.SetTopMargin(0.01); gPad.SetBottomMargin(0.30)
    gPad.SetLeftMargin(0.14); gPad.SetRightMargin(0.04)
    gPad.SetBorderMode(0)
    gPad.SetGridy(kTRUE)
    line1 = TLine(frame3.GetXaxis().GetXmin(),0,frame3.GetXaxis().GetXmax(),0)
    line2 = TLine(frame3.GetXaxis().GetXmin(),0,frame3.GetXaxis().GetXmax(),0)
    line1.SetLineColor(0) # white to clear dotted grid lines
    line2.SetLineColor(12) # dark grey
    line2.SetLineStyle(2)
    frame3.SetTitle("")
    frame3.GetYaxis().SetTitle("pull")
    frame3.GetXaxis().SetTitle("#Deltam^{2}_{ll} [GeV]")
    frame3.GetXaxis().SetTitleSize(0.13);   frame3.GetYaxis().SetTitleSize(0.12)
    frame3.GetXaxis().SetTitleOffset(1.0);  frame3.GetYaxis().SetTitleOffset(0.58)
    frame3.GetXaxis().SetLabelSize(0.10);   frame3.GetYaxis().SetLabelSize(0.10)
    frame3.GetXaxis().SetLabelOffset(0.02); frame3.GetYaxis().SetLabelOffset(0.01)
    frame3.GetYaxis().SetRangeUser(-5,5)
    frame3.GetYaxis().CenterTitle(True)
    frame3.GetYaxis().SetNdivisions(505)
    frame3.Draw("")
    line1.Draw("SAME")
    line2.Draw("SAME")
    frame3.Draw("SAME")
    canvas.SaveAs("rooFit109_ratiolike.png")
    canvas.Close()
    



def testErfExp():
    """Plots of some ErfExp functions"""
    
    offset0 = 100
    width0  =  20
    const0  = -0.01
    colors  = [ kRed, kBlue, kOrange, kMagenta, kAzure-4]
    
    x       = RooRealVar("x","x",0,460)
    offset  = RooRealVar("offset","offset of erfExp ",offset0)
    width   = RooRealVar("width", "width of erfExp",  width0)
    const   = RooRealVar("const", "const of erfExp",  const0)
    erfExp  = RooErfExpPdf("erfExp","erfExp",x,const,offset,width)
    
    var_dict = { 
        "offset": ( offset, offset0, [    50,   100,    150, ] ),
        "width":  ( width,  width0,  [    10,    40,     60, ] ),
        "const":  ( const,  const0,  [ -0.02, -0.01, -0.005, ] ),
    }
    
    canvas = TCanvas("canvas","canvas",100,100,1400,400)
    canvas.Divide(3)
    frames  = [ ]
    legends = [ ]
    for i, varname in enumerate(["offset","width","const"],1):
        #canvas = TCanvas("canvas","canvas",100,100,1600,1200)
        canvas.cd(i)
        (x1,w) = (0.552,0.42)
        #if i is 1: x1 = 0.555
        legend = TLegend(x1,0.86,x1+w,0.66)
        legend.SetHeader("ErfExp(#scale[0.95]{#font[82]{offset,width,const}})")
        legend.SetTextFont(82)
        legend.SetTextSize(0.035)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        gPad.SetLeftMargin(0.10); gPad.SetRightMargin(0.01)
        
        frame  = x.frame(Title("Varying %s"%varname))
        titles = [ ]
        (var, value0, values) = var_dict[varname]
        for j, (value, color) in enumerate(zip(values,colors),1):
            var.setVal(value)
            #print ">>>  before: %.5f, %.5f, %.5f" % (erfExp.getVal(),erfExp.getVal(RooArgSet(x)),erfExp.getNorm(RooArgSet(x)))
            x_ymax = erfExp.asTF(RooArgList(x)).GetMaximumX()
            x.setVal(x_ymax)
            ymax = erfExp.getVal(RooArgSet(x))
            #print ">>>   after: %.5f, %.5f, %.5f" % (erfExp.getVal(),erfExp.getVal(RooArgSet(x)),erfExp.getNorm(RooArgSet(x)))
            #print ">>>   %s; x_ymax = %.6f; ymax = %.6f" % (varname,x_ymax,ymax)
            #print ">>>   %s " % (erfExp.getNorm(RooArgSet(x)) * ymax / erfExp.getVal())
            #print ">>>   %s " % (erfExp.getNorm(RooArgSet(x)) / ymax)
            #print ">>> %s; max = %.8f; %.8f" % (varname,erfExp.getMaxVal(RooArgSet(x)),erfExp.maxVal(1))
            # normalize by    erfExp.getNorm(RooArgSet(x)) * ymax / erfExp.getVal()
            erfExp.plotOn(frame,Name("pdf_%d"%j),LineColor(color),Normalization((100/4.5)/ymax))
            titles.append("%5.3g,%4.3g,%6.3g"%(offset.getVal(),width.getVal(),const.getVal()))
        var.setVal(value0)
        
        frame.GetYaxis().SetTitle("")
        frame.GetXaxis().SetTitleSize(0.058);   frame.GetYaxis().SetTitleSize(0.045)
        frame.GetXaxis().SetTitleOffset(1.1);   frame.GetYaxis().SetTitleOffset(1.5)
        frame.GetXaxis().SetLabelSize(0.048);   frame.GetYaxis().SetLabelSize(0.042)
        frame.GetXaxis().SetLabelOffset(0.010); frame.GetYaxis().SetLabelOffset(0.010)
        frame.SetMaximum(1.04*frame.GetMaximum()) #GetYaxis()
        frame.Draw()
        legend.Draw()
        frames.append(frame)
        legends.append(legend)
        for j, title in enumerate(titles,1): legend.AddEntry("pdf_%s"%j, title, 'L')
    canvas.SaveAs("%s/ErfExp_flat.png"%OUT_DIR)
    canvas.Close()
    


def testLandau():
    """Plots of some ErfExp functions"""
    
    mean0  = 120
    width0 =  20
    colors = [ kRed, kBlue, kOrange, kMagenta, kAzure-4]
    
    x      = RooRealVar("x","x",0,460)
    mean   = RooRealVar("mean", "mean of erfExp ",mean0)
    width  = RooRealVar("width","width of erfExp",width0)
    landau = RooLandau("landau","landau",x,mean,width)
    
    var_dict = { 
        "mean":  ( mean,  mean0,  [ 80, 120, 160, ] ),
        "width": ( width, width0, [ 10,  20,  30, ] ),
    }
    
    canvas = TCanvas("canvas","canvas",100,100,1400,600)
    canvas.Divide(2)
    frames  = [ ]
    legends = [ ]
    for i, varname in enumerate(["mean","width"],1):
        #canvas = TCanvas("canvas","canvas",100,100,1600,1200)
        canvas.cd(i)
        (x1,w) = (0.552,0.42)
        legend = TLegend(x1,0.86,x1+w,0.66)
        legend.SetHeader("Landau(#scale[0.95]{#font[82]{mean,width}})")
        legend.SetTextFont(82)
        legend.SetTextSize(0.035)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        gPad.SetLeftMargin(0.10); gPad.SetRightMargin(0.01)
        
        frame  = x.frame(Title("Varying %s"%varname))
        titles = [ ]
        (var, value0, values) = var_dict[varname]
        for j, (value, color) in enumerate(zip(values,colors),1):
            var.setVal(value)
            #print ">>>  before: %.5f, %.5f, %.5f, %.5f" % (landau.getVal(),landau.getVal(RooArgSet(x)),landau.getNorm(RooArgSet(x)),landau.getVal())
            x_ymax = landau.asTF(RooArgList(x)).GetMaximumX()
            x.setVal(x_ymax)
            ymax = landau.getVal(RooArgSet(x))
            #print ">>>   %s; x_ymax = %.6f; ymax = %.6f" % (varname,x_ymax,ymax)
            landau.plotOn(frame,Name("pdf_%d"%j),LineColor(color),Normalization((100/4.5)/ymax))
            titles.append("%4.3g,%4.3g"%(mean.getVal(),width.getVal()))
        var.setVal(value0)
        
        frame.GetYaxis().SetTitle("")
        frame.GetXaxis().SetTitleSize(0.058);   frame.GetYaxis().SetTitleSize(0.045)
        frame.GetXaxis().SetTitleOffset(1.1);   frame.GetYaxis().SetTitleOffset(1.5)
        frame.GetXaxis().SetLabelSize(0.048);   frame.GetYaxis().SetLabelSize(0.042)
        frame.GetXaxis().SetLabelOffset(0.010); frame.GetYaxis().SetLabelOffset(0.010)
        frame.SetMaximum(1.04*frame.GetMaximum()) #GetYaxis()
        frame.Draw()
        legend.Draw()
        frames.append(frame)
        legends.append(legend)
        for j, title in enumerate(titles,1): legend.AddEntry("pdf_%s"%j, title, 'L')
    canvas.SaveAs("%s/Landau_flat.png"%OUT_DIR)
    canvas.Close()


def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
        
        
        
        
def main():
    print ""
    
    makeDirectory(OUT_DIR)
    
    # MAIN CHECKS
    #ratioTest()
#     testErfExp()
#     testLandau()
    fitVars()
    #fitUnbinnedVars()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




