#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
import PlotTools.PlotTools
from PlotTools.PlotTools import Comparison, makeRatio, makeCanvas, makeStatisticalError, combineWeights
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.PrintTools import color, warning, error, printSameLine, header
import ROOT
from ROOT import gPad, gROOT, gStyle, gRandom, gDirectory, TFile, TTree, TH1F, TH2F, THStack, TCanvas, TLegend,\
                 TText, TLatex, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

SFRAME_DIR = "SFrameAnalysis_Moriond"
DIR = "/shome/ineuteli/analysis/%s/AnalysisOutput/" % (SFRAME_DIR)
MORIOND_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
OUT_DIR = "plots_check"
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



def compareOldToNew():
    print ">>>\n>>> compareOldToNew()"
    
    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM"
    OLD_DIR      = "/scratch/ytakahas/SFrameAnalysis/AnalysisOutputEM"
    
    samples = [
        ("WJ",          "WJ",           "WJetsToLNu_TuneCUETP8M1"           ),
        ("TT",          "TT",           "TT_TuneCUETP8M1"                   ),
        ("DY",          "DY",           "DYJetsToLL_M-50_TuneCUETP8M1"      ),
        #("DY",          "DY1",          "DY1JetsToLL_M-50_TuneCUETP8M1"     ),
        #("SingleMuon",  "SingleMuon",   "SingleMuon_Run2016"                ),
        ("MuonEG",      "MuonEG",       "MuonEG_Run2016"                    ),
                ]
    
    treename = "tree_emu"
    oldlabel = "OLD"
    newlabel = "Moriond"
    norm     = True
    
    for sampledir,samplelabel,sample in samples:
        print ">>>\n>>> comparison %s-%s for \"%s\"" % (oldlabel,newlabel,sample)
        
        file1 = TFile( "%s/%s/TauTauAnalysis.%s_%s.root" % (OLD_DIR,    sampledir,sample,"Moriond"))
        file2 = TFile( "%s/%s/TauTauAnalysis.%s_%s.root" % (MORIOND_DIR,sampledir,sample,"Moriond"))
        tree1 = file1.Get(treename)
        tree2 = file2.Get(treename)
        
        nocuts      = "channel>0"
        vetos       = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
        vetos_emu   = "extraelec_veto == 0 && extramuon_veto == 0"
        isocuts     = "iso_1<0.15 && iso_2 == 1"
        isocuts_emu = "iso_1<0.20 && iso_2<0.15"
        baseline    = "channel>0 && %s && %s && q_1*q_2<0" % (vetos_emu, isocuts_emu)
        weight      = ""
        
        cuts        = [
            ("no cuts",   nocuts   ),
            ("baseline",  baseline ),
                      ]
        
        for cutname, cut in cuts:
            print ">>> selections: %s"     % (cutname)
            print ">>>             \"%s\"" % (cut)
            
            oldcut = cut
            newcut = cut #" && ".join([cut,"triggers==1 && pt_1>23"])
            print ">>>   %10s: entries: %d" % (oldlabel,tree1.GetEntries(cut))
            print ">>>   %10s: entries: %d" % (newlabel,tree2.GetEntries(cut))
            
            vars = [
#                 ( "pfmt_1",                              80,      0, 200 ),
#                 ( "dilepton_veto",                        2,      0, 2.0 ),
#                 ( "extraelec_veto",                       2,      0, 2.0 ),
#                 ( "extramuon_veto",                       2,      0, 2.0 ),
#                 ( "lepton_vetos",                         2,      0, 2.0 ),
#                 ( "againstElectronVLooseMVA6_2",          2,      0, 2.0 ),
#                 ( "againstMuonTight3_2",                  2,      0, 2.0 ),
#                 ( "lepton_vetos",                         2,      0, 2.0 ),
#                 ( "iso_1",                               50,      0, 0.3 ),
#                 ( "iso_2",                               50,      0, 0.3 ),
#                 ( "pt_1",                               100,      0, 100 ),
#                 ( "pt_2",                               100,      0, 100 ),
                ( "q_1",                                  5,     -2,   3 ),
                ( "q_2",                                  5,     -2,   3 ),
#                 ( "abs(eta_1)",                          50,      0, 2.5 ),
#                 ( "abs(eta_2)",                          50,      0, 2.5 ),
#                 ( "q_1",                                100,       -4, 4 ),
#                 ( "q_2",                                100,       -4, 4 ),
            ]
            weightvars = [
                ( "weight",                             100,   -0.2, 1.5 ),
                (("weight",     "weight*trigweight_1"), 100,   -0.2, 1.5 ),
                ( "trigweight_1",                       100,   -0.2, 1.5 ),
                (("trigweight_1_or","trigweight_or_1"), 100, -0.2, 1.5 ),
                ( "trigweight_2",                       100,   -0.2, 1.5 ),
                ( "idisoweight_1",                      100,   -0.2, 1.5 ),
                ( "idisoweight_2",                      100,   -0.2, 1.5 ),
                ( "puweight",                           100,   -0.2, 1.5 ),
                ( "weightbtag",                         100,   -0.2, 1.5 ),
                ( "ttptweight",                         100,   -0.2, 1.5 ),
            ]
            #vars = weightvars
            
            for (var,N,a,b) in vars:
                #print ">>> comparison \"%s\" with \"%s\"" % (var,cut)
            
                if isinstance(var,tuple): oldvar, newvar = var
                else:                     oldvar, newvar = var, var
                
                oldname = "%s_old"%(oldvar.replace('(','').replace(')',''))
                newname = "%s_new"%(newvar.replace('(','').replace(')',''))
            
                hist1 = TH1F(oldname, oldname, N, a, b)
                hist2 = TH1F(newname, newname, N, a, b)
                tree1.Draw("%s >> %s"%(oldvar,oldname),oldcut,"gOff")
                tree2.Draw("%s >> %s"%(newvar,newname),newcut,"gOff")
                N1 = hist1.Integral()
                N2 = hist2.Integral()
                if norm:
                    hist1.Scale(1/N1)
                    hist2.Scale(1/N2)
                
                canvas = TCanvas("canvas","canvas",100,100,800,600)
                canvas.SetBottomMargin(0.12)
                canvas.SetRightMargin(0.05)
                canvas.SetLeftMargin(0.12)
                canvas.SetTopMargin(0.05)
                
                hist1.SetLineWidth(3)
                hist1.SetLineStyle(1)
                hist1.SetLineColor(kAzure+4)
                hist2.SetLineWidth(3)
                hist2.SetLineStyle(2)
                hist2.SetLineColor(kRed+3)
                hist1.Draw("hist")
                hist2.Draw("histsame")
                hist1.SetTitle("")
                hist1.GetXaxis().SetTitle(newvar)
                hist1.GetYaxis().SetTitle("A.U.")
                hist1.GetXaxis().SetTitleSize(0.05)
                hist1.GetYaxis().SetTitleSize(0.05)
                hist1.GetXaxis().SetTitleOffset(1.00)
                hist1.GetYaxis().SetTitleOffset(1.20)
                hist1.GetXaxis().SetLabelSize(0.040)
                hist1.GetYaxis().SetLabelSize(0.040)
                hist1.GetYaxis().SetRangeUser(0,max(hist1.GetMaximum(),hist2.GetMaximum())*1.10)
                
                (x1,y1) = (0.65,0.90)
                (w,h)   = (0.18,0.15)
                (x2,y2) = (x1+w,y1-h)
                legend = TLegend(x1,y1,x2,y2)
                legend.SetHeader("%s - %s"%(samplelabel,cutname))
                legend.AddEntry(hist1,"%s (%d)"%(oldlabel,hist1.GetEntries()), 'l')
                legend.AddEntry(hist2,"%s (%d)"%(newlabel,hist2.GetEntries()), 'l')
                legend.SetTextSize(0.040)
                legend.SetTextFont(42)
                legend.SetBorderSize(0)
                legend.SetFillStyle(0)
                legend.Draw()
                gStyle.SetOptStat(0)
                
                canvas.SaveAs("%s/%s_%s_%s_%s-%s.png" % (OUT_DIR,newvar.replace('(','').replace(')','').replace('*','-'),cutname.replace(' ','_'),samplelabel,oldlabel,newlabel))
                canvas.Close()
                ROOT.gDirectory.Delete(hist1.GetName())
                ROOT.gDirectory.Delete(hist2.GetName())
            
        file1.Close()
        file2.Close()
        
    print ">>>"



def vertexDY():
    print ">>>\n>>> vertexDY()"
    
    DIR  = "/shome/ineuteli/analysis/SFrameAnalysis_Moriond/TauTauResonances/"
    file1 = TFile( DIR + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
    file2 = TFile( DIR + "TauTauAnalysis.DYJets_M-50.UZH.root" )
    
    
    histnames = [
        "d0_lepton_tail", "dz_lepton_tail", "d0_lepton", "dz_lepton",
        "pt_muon_ID", "pt_lepton", "pt_lepton_pt23",
        "gen_match_1_pt23_eta2p4", "gen_match_1_d0_dz", "gen_match_1_baseline", "gen_match_2_baseline",
        #"pt_Z", "pt_Z_baseline"
    ]
    
    channel = "mutau"
    
    for histname in histnames:
        print ">>>   %s" % (histname)
        
        hist1 = file1.Get("histogram_%s/%s" % (channel,histname))
        hist2 = file2.Get("histogram_%s/%s" % (channel,histname))
        N1 = hist1.GetEntries()
        N2 = hist2.GetEntries()
        hist1.Scale(1/N1)
        hist2.Scale(1/N2)
        max_bin = max(hist1.GetMaximum(),hist2.GetMaximum())
        
        if   "gen_match_1"  in histname: var = "gen_match_1"
        elif "gen_match_2"  in histname: var = "gen_match_2"
        elif "d0"           in histname: var = "lepton d0"
        elif "dz"           in histname: var = "lepton dz"
        elif "pt_Z"         in histname: var = "Z boson pt"
        elif "pt_muon"      in histname: var = "muon pt"
        elif "pt_lepton"    in histname: var = "muon pt"
        else: var = histname
        if "_baseline"      in histname: var += " (baseline selections)"
        elif "_pt23_eta2p4" in histname: var += " (p_{T}>23 GeV, |#eta|<2.4)"
        elif "_pt23"        in histname: var += " (p_{T}>23 GeV)"
        elif "_d0_dz"       in histname: var += " (p_{T}, #eta, d0, dz cuts)"
        elif "_muon_ID"     in histname: var += " (medium ID)"
        
        (x1,x2) = (0.50,0.90)
        (y1,y2) = (0.60,0.80)
        if "dz_lepton_tail" in histname:       (y1,y2) = (0.55,0.35)
        if "gen_match_1_baseline" in histname: (x1,x2) = (0.68,0.95)
        if "gen_match_2_baseline" in histname: (x1,x2) = (0.75,0.40)
        
        print ">>>     entries  hist1 = %.4f" % (N1)
        print ">>>     entries  hist2 = %.4f" % (N2)
        print ">>>     overflow hist1 = %.4f" % (hist1.GetBinContent(hist1.GetNbinsX()+1))
        print ">>>     overflow hist2 = %.4f" % (hist2.GetBinContent(hist2.GetNbinsX()+1))
        
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.12)
        canvas.SetTopMargin(0.05)
        hist1.SetLineWidth(3)
        hist1.SetLineStyle(1)
        hist1.SetLineColor(kAzure+4)
        hist2.SetLineWidth(3)
        hist2.SetLineStyle(2)
        hist2.SetLineColor(kRed+3)
        hist1.Draw("Ehist")
        hist2.Draw("Ehistsame")
        hist1.SetTitle("")
        hist1.GetXaxis().SetTitle(var)
        hist1.GetYaxis().SetTitle("A.U.")
        hist1.GetXaxis().SetTitleSize(0.06)
        hist1.GetYaxis().SetTitleSize(0.06)
        hist1.GetXaxis().SetTitleOffset(0.9)
        hist1.GetXaxis().SetLabelSize(0.045)
        hist1.GetYaxis().SetLabelSize(0.045)
        hist1.SetMaximum(max_bin*1.08)
        legend = TLegend(x1,y1,x2,y2)
        legend.AddEntry(hist1,"DY 10-50", 'l')
        legend.AddEntry(hist2,"DY 50", 'l')
        legend.SetTextSize(0.045)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.Draw()
        gStyle.SetOptStat(0)
        canvas.SaveAs("%s/%s.png" % (OUT_DIR,histname))
        canvas.Close()
        ROOT.gDirectory.Delete(hist1.GetName())
        ROOT.gDirectory.Delete(hist2.GetName())
        
    file1.Close()
    file2.Close()



def compareVarIntegrals():
    """Compare intregral of variables (e.g. weights) of the same sample file."""
    print ">>>\n>>> compareVarIntegrals()"
    
    filenames = [
        ("TT",  "TT_TuneCUETP8M1",               "ttbar",       ),
#         ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1",  "DY inclusive" ),
#         ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1", "DY + 1 jet"   ),
#         ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1", "DY + 2 jets"  ),
#         ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1", "DY + 3 jets"  ),
#         ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1", "DY + 4 jets"  ),
                ]
    
    vars        = [
#                     (  "btagweight",
#                      [("weightbtag",         "nominal"                  ),
#                       ("weightbtag_bcDown",  "heavy flavour shift down" ),
#                       ("weightbtag_bcUp",    "heavy flavour shift up"   ),
#                       ("weightbtag_udsgDown","heavy flavour shift down" ),
#                       ("weightbtag_udsgUp",  "heavy flavour shift up"   ), ])
                    (  "jet multiplicity",
                     [("ncjets",            "nominal"                   ),
                      ("ncjets_jesUp",      "JES up"                    ),
                      ("ncjets_jesDown",    "JES down"                  ),
                      ("ncjets_jer",        "JER"                       ),
                      ("ncjets_jerUp",      "JER up"                    ),
                      ("ncjets_jerDown",    "JER down"                  ),])
                  ]
    
    mylabel       = "_Moriond"
    channel       = "mutau"
    weight        = "" #"weight*trigweight_or_1"
    triggers      = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline      = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
    category1_nob = "ncjets == 1 && nfjets  > 0"
    category2_nob = "ncjets == 2 && nfjets == 0 && dphi_ll_bj>2 && met<60"
    category1     = "ncjets == 1 && nfjets  > 0 && nbtag > 0"
    category2     = "ncjets == 2 && nfjets == 0 && nbtag > 0 && dphi_ll_bj>2 && met<60"
    category12    = "ncjets == 1 && nfjets  > 0 && nbtag > 0 && met<60 && pfmt_1<60"
    category22    = "ncjets == 2 && nfjets == 0 && nbtag > 0 && dphi_ll_bj>2 && met<60 && pfmt_1<60"
    
    cuts = [
        #("no cuts",  "channel>0"),
        ("baseline",             "%s"       % (baseline)),
#         ("category 1 (no b)",    "%s && %s" % (baseline,category1_nob)),
#         ("category 2 (no b)",    "%s && %s" % (baseline,category2_nob)),
#         ("category 1",           "%s && %s" % (baseline,category1)),
#         ("category 2",           "%s && %s" % (baseline,category2)),
#         ("optimized category 1", "%s && %s" % (baseline,category12)),
#         ("optimized category 2", "%s && %s" % (baseline,category22)),
    ]
    
    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ]
    
    for ifile, (subdir,filename0,samplename) in enumerate(filenames,1):
        print ">>>\n>>>   %2s: %10s, %10s"%(ifile,filename0,samplename)
        filename    = "%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,subdir,filename0,mylabel)
        file        = TFile(filename)
        for cutname, cut in cuts:
            for ivar, (varname0,varlist) in enumerate(vars,1):
                print ">>>   %s - %s" % (cutname,varname0)
                
                N       = len(varlist)+1
                (a,b)   = (0,N)
                (x1,x2) = (0.75,0.91)
                (y1,y2) = (0.90,0.65)
                canvas = TCanvas("canvas","canvas",100,100,800,600)
                canvas.SetBottomMargin(0.12)
                canvas.SetRightMargin(0.06)
                canvas.SetLeftMargin(0.12)
                canvas.SetTopMargin(0.05)
                #legend = TLegend(x1,y1,x2,y2)
                
                var0        = varname0
                histname0   = "%s"%(varname0)
                hist0       = TH1F(histname0,histname0,N,a,b)
                hists = [ ]
                integrals   = [ ]
                max_bin = 0
                treename    = "tree_%s_cut_relaxed"%channel
                
                for i, (var,varname) in enumerate(varlist,1):
                    histname    = "%s_%s"%(subdir,var)
                    (N,a,b)     = (2,0,2)
                    hist        = TH1F(histname,histname,N,a,b)
                    tree        = file.Get(treename)
                    weight1     = combineWeights(weight,var)
                    cut1        = "(%s)*%s"%(cut,weight1)
                    out         = tree.Draw("%s >> %s"%(1,histname),cut1,"gOff")
                    N1          = hist.GetEntries()
                    I1          = hist.GetBinContent(2)
                    #hist.Scale(1/N1)
                    #print ">>>     N1 = %s,I1 = %s"%(N1,I1)
                    integrals.append(I1)
                    hist0.SetBinContent(i,I1)
                    hist0.GetXaxis().SetBinLabel(i,var)
                    hmax        = hist.GetMaximum()
                    if hmax > max_bin:
                        max_bin = hmax
                    #hist.SetLineWidth(3)
                    #hist.SetLineStyle(1+(i-1)%2)
                    #hist.SetLineColor(colors[i-1])
                    #hist.SetMarkerSize(0)
                    #if i==0: hist.Draw("Ehist")
                    #else:    hist.Draw("Ehistsame")
                    #legend.AddEntry(hist,varname, 'l')
                    hists.append(hist)
                
                hist0.Draw("Ehist")
                hist.SetLineColor(colors[0])
                hist.SetLineWidth(2)
                hist0.SetTitle("")
                hist0.SetMarkerSize(0)
                #hist0.GetXaxis().SetTitle(varname0)
                hist0.GetYaxis().SetTitle("A.U.")
                hist0.GetXaxis().SetTitleSize(0.06)
                hist0.GetYaxis().SetTitleSize(0.05)
                hist0.GetXaxis().SetTitleOffset(0.94)
                hist0.GetYaxis().SetTitleOffset(1.26)
                hist0.GetXaxis().SetLabelSize(0.042)
                hist0.GetYaxis().SetLabelSize(0.040)
                hist0.SetMaximum(max_bin*1.24)
                #legend.SetTextSize(0.032)
                #legend.SetBorderSize(0)
                #legend.SetFillStyle(0)
                #legend.Draw()
                gStyle.SetOptStat(0)
                
                text = TLatex()
                for i, I1 in enumerate(integrals):
                    fraction = 100*(I1/integrals[0]-1)
                    text.SetTextFont(42)
                    text.SetTextSize(0.034)
                    text.SetTextAlign(22)
                    text.DrawLatex(i+0.5,max_bin*1.10,"#splitline{ %.1f}{  %6.3f%%}"%(I1,fraction))
                
                cutname     = cutname.replace(' ','_').replace('(','-').replace(')','')
                filename0   = filename0.split('_')[0]
                canvas.SaveAs("%s/%s-%s-%s_integral_comparison.png" % (OUT_DIR,var0.replace(' ','_'),cutname,filename0))
                canvas.Close()
                
                ROOT.gDirectory.Delete(histname0)
                for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
        file.Close()
    


def compareVarsForSamples():
    """Compare shapes of different variables for the same sample file."""
    print ">>>\n>>> compareVarsForSamples()"
    
    filenames = [
        ("TT",  "TT_TuneCUETP8M1",               "ttbar",       ),
#         ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1",  "DY inclusive" ),
#         ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1", "DY + 1 jet"   ),
#         ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1", "DY + 2 jets"  ),
#         ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1", "DY + 3 jets"  ),
#         ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1", "DY + 4 jets"  ),
                ]
    
    vars        = [
                    ([("weightbtag",       "nominal"),
                      ("weightbtag_bcUp",  "heavy flavour shift up"),
                      ("weightbtag_bcDown","heavy flavour shift down")],
                     "weightbtag_bcShifts","b tag weight",50,0,1.9),
                    ([("weightbtag",         "nominal"),
                      ("weightbtag_udsgUp",  "heavy flavour shift up"),
                      ("weightbtag_udsgDown","heavy flavour shift down")],
                     "weightbtag_udsgShifts","b tag weight",50,0,1.9),
                  ]
    
    mylabel     = "_Moriond"
    channel     = "mutau"
    weight      = "weight*trigweight_or_1"
    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"
    cut         = "(%s)*%s"%(baseline,weight)
    
    cuts = [
        #("no cuts",  "channel>0"),
        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
    ]
    
    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ]
    
    for ifile, (subdir,filename0,samplename) in enumerate(filenames,1):
        print ">>>   %2s: %10s, %10s"%(ifile,filename0,samplename)
        filename    = "%s/%s/TauTauAnalysis.%s%s.root"%(MORIOND_DIR,subdir,filename0,mylabel)
        file        = TFile(filename)
        for cutname, cut in cuts:
            for ivar, (varlist,var0,varname0,N,a,b) in enumerate(vars):
                print ">>>   %s - %s" % (cutname,varname0)
                cut     = "(%s)*%s"%(cut,weight)
                
                (x1,x2) = (0.17,0.33)
                (y1,y2) = (0.90,0.65)
                canvas = TCanvas("canvas","canvas",100,100,800,600)
                canvas.SetBottomMargin(0.12)
                canvas.SetRightMargin(0.05)
                canvas.SetLeftMargin(0.12)
                canvas.SetTopMargin(0.05)
                legend = TLegend(x1,y1,x2,y2)
                
                hists = [ ]
                max_bin = 0
                treename    = "tree_%s_cut_relaxed"%channel
        
                for i, (var,varname) in enumerate(varlist):
                    histname    = "%s_%s"%(subdir,var)
                    hist        = TH1F(histname,histname,N,a,b)
                    tree        = file.Get(treename)
                    out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
                    N1          = hist.GetEntries()
                    hist.Scale(1/N1)
                    hmax        = hist.GetMaximum()
                    if hmax > max_bin:
                        max_bin = hmax
                    hist.SetLineWidth(3)
                    hist.SetLineStyle(1+(i-1)%2)
                    hist.SetLineColor(colors[i-1])
                    hist.SetMarkerSize(0)
                    if i==0: hist.Draw("Ehist")
                    else:    hist.Draw("Ehistsame")
                    legend.AddEntry(hist,varname, 'l')
                    hists.append(hist)
            
                hist1 = hists[0]
                hist1.SetTitle("")
                hist1.GetXaxis().SetTitle(varname0)
                hist1.GetYaxis().SetTitle("A.U.")
                hist1.GetXaxis().SetTitleSize(0.06)
                hist1.GetYaxis().SetTitleSize(0.06)
                hist1.GetXaxis().SetTitleOffset(0.95)
                hist1.GetYaxis().SetTitleOffset(0.9)
                hist1.GetXaxis().SetLabelSize(0.045)
                hist1.GetYaxis().SetLabelSize(0.045)
                hist1.SetMaximum(max_bin*1.10)
                legend.SetTextSize(0.032)
                legend.SetBorderSize(0)
                legend.SetFillStyle(0)
                legend.Draw()
                gStyle.SetOptStat(0)
                cutname     = cutname.replace(' ','_').replace('(','-').replace(')','')
                filename0   = filename0.split('_')[0]
                canvas.SaveAs("%s/%s-%s-%s_comparison.png" % (OUT_DIR,var0,cutname,filename0))
                canvas.Close()
        
                for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
        file.Close()



def compareSamplesForVars():
    """Compare the shape of a variable for different sample files."""
    print ">>>\n>>> NUP()"
    
    filenames = [ ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1_Moriond",  "DY inclusive" ),
                  ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 1 jet"   ),
                  ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 2 jets"  ),
                  ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 3 jets"  ),
                  ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1_Moriond", "DY + 4 jets"  ),]
    
    vars        = [ ("NUP","number of partons",7,0,7), ("njets","number of reconstructed jets",7,0,7), ]
    
    channel     = "mutau"
    
    weight      = "weight*trigweight_or_1"
    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"
    cut         = "(%s)*%s"%(baseline,weight)
    
    colors     = [ kRed+1, kAzure+4, kRed-9, kGreen+2, kAzure-4, kYellow+2, ] #kYellow+771, # kOrange+8
    
    for var, varname, N, a, b in vars:
        print ">>>   %s" % (var)
        
        (x1,x2) = (0.74,0.90)
        (y1,y2) = (0.90,0.65)
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.12)
        canvas.SetTopMargin(0.05)
        legend = TLegend(x1,y1,x2,y2)
        
        hists = [ ]
        files = [ ]
        max_bin = 0
        treename    = "tree_%s_cut_relaxed"%channel
        
        for i, (subdir,filename,samplename) in enumerate(filenames,1):
            print ">>>   %2s: %10s, %10s"%(i,filename,samplename)
            filename    = "%s/%s/TauTauAnalysis.%s.root"%(MORIOND_DIR,subdir,filename)
            histname    = "%s_%s"%(var,i)
            file        = TFile(filename)
            #print ">>>     %2s: %10s, %3s, %3s, %3s"%(i,histname,N,a,b)
            hist        = TH1F(histname,histname,N,a,b)
            tree        = file.Get(treename)
            out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
            N1          = hist.GetEntries()
            #print ">>>     %2s: %10s, out=%s, N=%s"%(i,samplename,out,N)
            hist.Scale(1/N1)
            hmax        = hist.GetMaximum()
            if hmax > max_bin:
                max_bin = hmax
                #print ">>>   %s has %d entries" % (hist.GetName(),I)
            hist.SetLineWidth(3)
            hist.SetLineStyle(1+(i-1)%2) #3
            hist.SetLineColor(colors[i-1])
            hist.SetMarkerSize(0)
            if i==0: hist.Draw("Ehist")
            else:    hist.Draw("Ehistsame")
            legend.AddEntry(hist,samplename, 'l')
            hists.append(hist)
            #print ">>>     before %s "%(type(hists[-1]))
            files.append(file)
        
        hist1 = hists[0]
        print ">>>   after %s "%(type(hists[0]))
        hist1.SetTitle("")
        hist1.GetXaxis().SetTitle(varname)
        hist1.GetYaxis().SetTitle("A.U.")
        hist1.GetXaxis().SetTitleSize(0.06)
        hist1.GetYaxis().SetTitleSize(0.06)
        hist1.GetXaxis().SetTitleOffset(0.9)
        hist1.GetYaxis().SetTitleOffset(0.9)
        hist1.GetXaxis().SetLabelSize(0.045)
        hist1.GetYaxis().SetLabelSize(0.045)
        hist1.SetMaximum(max_bin*1.10)
        legend.SetTextSize(0.032)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.Draw()
        gStyle.SetOptStat(0)
        canvas.SaveAs("%s/%s_comparison.png" % (OUT_DIR,var))
        canvas.Close()
        
        for hist in hists: ROOT.gDirectory.Delete(hist.GetName())
        for file in files: file.Close()
    


def compareCutsForVars():
    print ">>>\n>>> compareCutsForVars()"
    
    triggers    = "abs(eta_1)<2.1 && trigger_cuts==1"
    baseline    = "channel>0 && iso_cuts==1 && lepton_vetos==0 && %s && q_1*q_2<0" % (triggers)
    category1   = "ncjets == 1 && nfjets  > 0 && ncbtag > 0"
    category2   = "ncjets == 2 && nfjets == 0 && ncbtag > 0 && dphi_ll_bj>2 && met<60"
    category1_jesUp = category1
    category2_jesUp = category2
    category1_jerUp = category1
    category2_jerUp = category2
    
    replaceVars = [ "jets", "btag", "met", "pfmt_1", "dphi_ll_bj", ]
    for var in replaceVars:
        category1_jesUp = category1_jesUp.replace(var,"%s_jesUp"%(var))
        category2_jesUp = category2_jesUp.replace(var,"%s_jesUp"%(var))
        category1_jerUp = category1_jerUp.replace(var,"%s_jerUp"%(var))
        category2_jerUp = category2_jerUp.replace(var,"%s_jerUp"%(var))
    
    # TTbar CR
    cuts_sets = [
#         ( "category 1: triggers",("m_sv",35,0.0,350),[
#             ("both triggers",        "%s && %s && %s" % (baseline,category2,"triggers==3")),
#             ("single lepton only",   "%s && %s && %s" % (baseline,category2,"triggers==1")),
#             ("cross trigger only",   "%s && %s && %s" % (baseline,category2,"triggers==2")), ]),
#         ( "category 2: triggers",("m_sv",35,0.0,350),[
#             ("both triggers",        "%s && %s && %s" % (baseline,category2,"triggers==3")),
#             ("single lepton only",   "%s && %s && %s" % (baseline,category2,"triggers==1")),
#             ("cross trigger only",   "%s && %s && %s" % (baseline,category2,"triggers==2")), ]),
#         ( "category 2: single muon",("m_sv",35,0.0,350),[
#             ("l #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2<5")),
#             ("real #tau",            "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==5")),
#             ("j #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==1 && gen_match_2==6")), ]),
#         ( "category 2: all triggers",("m_sv",35,0.0,350),[
#             ("l #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==3 && gen_match_2<5")),
#             ("real #tau",            "%s && %s && %s" % (baseline,category2,"triggers==3 && gen_match_2==5")),
#             ("j #rightarrow #tau",   "%s && %s && %s" % (baseline,category2,"triggers==3 && gen_match_2==6")), ]),
#         ( "optimized category 1: JEC",("jpt_1",35,0.0,350),[
#             ("normative",       "%s && %s" % (baseline,category1)),
#             ("JES up",          "%s && %s" % (baseline,category1_jesUp)),
#             ("JES down",        "%s && %s" % (baseline,category1_jesUp.replace("Up","Down"))),
#             #("JER nominal",     "%s && %s" % (baseline,category1_jerUp.replace("Up",""))),
#             #("JER up",          "%s && %s" % (baseline,category1_jerUp)),
#             #("JER down",        "%s && %s" % (baseline,category1_jerUp.replace("Up","Down"))),
#             ]),
        ( "optimized category 2: JES",("jpt_1",35,0.0,350),[
            ("nominal",         "jpt_1",         "%s && %s" % (baseline,category2)),
#             ("JER",             "%s && %s" % (baseline,category2_jerUp)),
            ("JES up",          "%s && %s" % (baseline,category2_jesUp)),
            ("JES down",        "%s && %s" % (baseline,category2_jesUp.replace("Up","Down"))),
#             ("JER normative",   "%s && %s" % (baseline,category2_jerUp.replace("Up",""))),
#             ("JER down",        "%s && %s" % (baseline,category2_jerUp.replace("Up","Down"))),
            ]),
        ( "optimized category 2: JES",("jpt_1",35,0.0,350),[
#             ("nominal",         "%s && %s" % (baseline,category2)),
            ("JER",             "%s && %s" % (baseline,category2_jerUp)),
            ("JER up",          "%s && %s" % (baseline,category2_jerUp)),
            ("JER down",        "%s && %s" % (baseline,category2_jerUp.replace("Up","Down"))),
#             ("JER normative",   "%s && %s" % (baseline,category2_jerUp.replace("Up",""))),
#             ("JER down",        "%s && %s" % (baseline,category2_jerUp.replace("Up","Down"))),
            ]),
#         ( "category 1",[
#             (" 1bj,  0cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==1 && nfjets>0"), # && met<60 && pfmt_1<60
#             (">0bj,  2cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets>0"),
#             (">0bj, >1cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets >1 && nfjets>0"),]),
#         ( "category 2",[
#             (" 1bj,  2cj, 0fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag==1 && ncjets==2 && nfjets==0"), # && met<60 && pfmt_1<60
#             (">0bj,  2cj, 0fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0  && ncjets==2 && nfjets==0"),
#             (">0bj, >1cj, 0fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0  && ncjets >1 && nfjets==0"),]),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets>0"),
#         ("pfmt_1<60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets==0"),
    ]
    
    weight      = "weight*trigweight_or_1*ttptweight_runI/ttptweight"
    samples     = [("TT",  "TT_TuneCUETP8M1",           "ttbar",            831.76  ), ]
    channels    = ["mutau",] #"etau"]
    doKS                = True and False
    drawErrorbars       = True and False
    drawRatio           = True #and False
    normalizeToHist0    = True #and False
    plot_label  = "-350_JER"
    
    for subdir,sample,samplename,sigma in samples:
        filename    = "%s/%s/TauTauAnalysis.%s%s.root" % (MORIOND_DIR,subdir,sample,mylabel)
        file        = TFile( filename )
        
        for channel in channels:
            
            treename    = "tree_%s%s"%(channel,"_cut_relaxed") #_cut
            histNname   = "histogram_%s/cutflow_%s"%(channel,channel)
            tree        = file.Get(treename)
            histN       = file.Get(histNname)
            
            if not tree:  print error("shapes - did not find tree %s in %s"%(treename,filename))
            if not histN: print error("shapes - did not find hist %s in %s"%(histNname,filename))
            
            N_tot       = histN.GetBinContent(8)
            normscale   = sigma*lumi*1000/N_tot
            if normalizeToHist0: plot_label += "_norm"
            I0          = 0
            print ">>> %s scale = %.3f" % (samplename,normscale)
            
            for cutsetname, var_info, cutset in cuts_sets:
                print ">>> "
                histu0      = None
                hists       = [ ]
                histus      = [ ]
                (var,N,a,b) = var_info #(50,0.0,50)
                
                for i, cut in enumerate(cutset):
                    
                    cutname = ""
                    if len(cut) is 2:
                        (cutname, cut) = cut
                    else:
                        (cutname,var,cut) = cut
                    
                    cut         = "(%s)*%s"%(cut,weight)
                    histname    = "%s_%s_%d"%(samplename.replace(' ',''),var,i)
                    histnameu   = histname+"_unbinned"
                    hist        = TH1F(histname,histname,N,a,b)
                    histu       = TH1F(histnameu,histnameu,10000,a,b)
                    hist.Sumw2()
                    out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
                    out         = tree.Draw("%s >> %s"%(var,histnameu),cut,"gOff")
                    hist.Scale(normscale)
                    hists.append(hist)
                    histus.append(histu)
                    I = hist.Integral(1,hist.GetNbinsX()) #+1
                    E = hist.GetEntries()
                    print ">>> %s (%d, %.1f):\n>>>   %s" % (histname,I,E,cut)
                    
                    if not I:
                        print warning("shapes - %s has integral 0, ignoring"%histname)
                        continue
                    
                    if i is 0:
                        histu0 = histu
                        I0 = I
                    elif normalizeToHist0:
                        hist.Scale(I0/I)
                        histu.Scale(I0/I)
                    if not I0: print error("shapes - first histogram %s has integral 0, ignoring"%histname); exit(1)
                    #entryname   = "%.1f - %s"%(I,cutname)
                    entryname   = "%d - %s"%(E,cutname)
                    
                    if i is not 0 and doKS:
                        KS = histu0.KolmogorovTest(histu)
                        entryname = "%s (KS %.3f)"%(entryname,KS)
                    
                    
                    print ">>>   entryname = %s"%(entryname)
                    hist.SetTitle(entryname)
                
                title      = "%s - %s: %s " % (subdir,channel.replace("mu","#mu").replace("tau","#tau"),cutsetname.replace("category 1","1b1f").replace("category 2","1b1c"))
                canvasname = "%s/%s%s_%sshape_%s-%s.png" % (OUT_DIR,var.replace('(','').replace(')',''),plot_label,subdir,channel,cutsetname.replace(': ','-').replace(' ','_'))
                position   = "CenterRightTop" #"LeftTop"#"CenterLeftBottom" #"LeftTop"#
                
                comparison = Comparison(*hists)
                comparison.Draw(title=title,xlabel=var,position=position,KS=False,linestyle=False,ratio=drawRatio,
                                                       errorbars=drawErrorbars,staterror=True,markers=False,markers_ratio=False)
                comparison.saveAs(canvasname)
                
                for hist in histus: gDirectory.Delete(hist.GetName())
                
                # canvas = TCanvas("canvas","canvas",100,100,800,600)
                # canvas.SetBottomMargin(0.12)
                # canvas.SetRightMargin(0.05)
                # canvas.SetLeftMargin(0.12)
                # canvas.SetTopMargin(0.05)
                # 
                # hist = hists[0]
                # hist.SetLineWidth(3)
                # hist.SetLineStyle(1)
                # hist.SetLineColor(colors[0])
                # hist.SetMarkerSize(0)
                # hist.Draw("hist E")
                # for i,h in enumerate(hists[1:]):
                #     h.SetLineWidth(3)
                #     h.SetLineStyle(i%4+1)
                #     h.SetLineColor(colors[i+1])
                #     h.SetMarkerSize(0)
                #     h.Draw("hist E same")
                # hist.GetXaxis().SetTitle("SVFit mass m_{sv} [GeV]")
                # hist.GetYaxis().SetTitle("number of events / %s GeV"%((b-a)/N))
                # hist.GetXaxis().SetTitleSize(0.05)
                # hist.GetYaxis().SetTitleSize(0.05)
                # hist.GetXaxis().SetTitleOffset(1.00)
                # hist.GetYaxis().SetTitleOffset(1.20)
                # hist.GetXaxis().SetLabelSize(0.040)
                # hist.GetYaxis().SetLabelSize(0.040)
                # hist.GetYaxis().SetRangeUser(0,max(hist.GetMaximum(),hist.GetMaximum())*1.15)
                # 
                # (x1,y1) = (0.35,0.25)
                # (w,h)   = (0.18,0.02+0.05*len(hists))
                # (x2,y2) = (x1+w,y1+h)
                # legend = TLegend(x1,y1,x2,y2)
                # legend.SetHeader("%s: %s"%(channel.replace("mu","#mu").replace("tau","#tau"),cutsetname))
                # for h in hists:
                #     print ">>> h.GetTitle()=%s"%(h.GetTitle())
                #     legend.AddEntry(h,h.GetTitle(), 'l')
                # legend.SetTextSize(0.035)
                # legend.SetTextFont(42)
                # legend.SetBorderSize(0)
                # legend.SetFillStyle(0)
                # legend.Draw()
                # gStyle.SetOptStat(0)
                # 
                # canvas.SaveAs("%s/%s_%sshape_%s-%s.png" % (OUT_DIR,var.replace('(','').replace(')',''),subdir,channel,cutsetname.replace(' ','')))
                # canvas.Close()
                # #1ROOT.gDirectory.Delete(hist1.GetName())
        
        file.Close()
        


def zptweight():
    print ">>>\n>>> vertexDY()"
    
    DIR  = "/shome/ineuteli/analysis/SFrameAnalysis_Moriond/RecoilCorrections/data/"
    file1 = TFile( DIR + "Zpt_weights.root" )
    file2 = TFile( DIR + "Zpt_weights_2016_BtoH.root" )
    
    histname = "zptmass_histo"
    hist1 = file1.Get(histname)
    hist2 = file2.Get(histname)
    var = histname

    for hist, period in [(hist1,"ICHEP"),(hist2,"Moriond")]:


        print ">>>   %s - %s" % (histname, period)
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.10)
        canvas.SetLeftMargin(0.12)
        canvas.SetTopMargin(0.05)
        hist.Draw("colz")
        hist.SetTitle("")
        hist.GetZaxis().SetRangeUser(0.75,2.0)
        hist.GetXaxis().SetRangeUser(0,100)
        hist.GetYaxis().SetRangeUser(0,200)
        hist.GetXaxis().SetTitle("Z mass")
        hist.GetYaxis().SetTitle("Z pt")
        hist.GetXaxis().SetTitleSize(0.06)
        hist.GetYaxis().SetTitleSize(0.06)
        hist.GetXaxis().SetTitleOffset(0.9)
        hist.GetXaxis().SetLabelSize(0.045)
        hist.GetYaxis().SetLabelSize(0.045)
        gStyle.SetOptStat(0)
        canvas.SaveAs("%s/%s_%s.png" % (OUT_DIR,histname,period))
        canvas.Close()
        
    file1.Close()
    file2.Close()




def trigweight():
    """Compare shapes of different files."""
    print ">>>\n>>> trigweight()"
    
    channel  = "mutau"
    treename = "tree_%s" % channel
    vars     = [("trigweight_1","trigger weight",100,0,3), ("trigweight_1","trigger weight",100,0,3)]
    samples  = [
        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50" ),
        ("DY",  "DYJetsToLL_M-50_TuneCUETP8M1", "DY M-50" ),
    ]
    cuts = [
        ("no cuts",  "channel>0"),
        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
    ]
    
    for var, varnam, N,a,b in vars:
        for cutname, cut in cuts:
            for sampledir, samplename, samplelabel in samples:
                
                file = TFile("%s/%s/TauTauAnalysis.%s_Moriond.root"%(MORIOND_DIR,sampledir,samplename))
                tree = file.Get(treename)
        
                hist1 = TH1F("hist1", "%s_L"%var, N, a, b)
                hist2 = TH1F("hist2", "%s_X"%var, N, a, b)
                hist3 = TH1F("hist3", "%s_B"%var, N, a, b)
                
                tree.Draw("%s >> hist1"%(var),"%s && triggers==1 && pt_1>23"%(cut),"gOff")
                tree.Draw("%s >> hist2"%(var),"%s && triggers==2"%(cut),"gOff")
                tree.Draw("%s >> hist3"%(var),"%s && triggers==3 && pt_1>23"%(cut),"gOff")
                
                maxs = [ ] 
                for hist in [hist1,hist2,hist3]:
                    I = hist.Integral()
                    print ">>>   %s has %d entries" % (hist.GetName(),I)
                    if I:
                        hist.Scale(1./I)
                        maxs.append(hist.GetMaximum())
                
                print ">>>   %s - %s" % (samplelabel,var)
                canvas = TCanvas("canvas","canvas",100,100,800,600)
                canvas.SetBottomMargin(0.12)
                canvas.SetRightMargin(0.05)
                canvas.SetLeftMargin(0.12)
                canvas.SetTopMargin(0.05)
                hist1.SetLineWidth(3)
                hist1.SetLineStyle(1)
                hist1.SetLineColor(kAzure+4)
                hist2.SetLineWidth(3)
                hist2.SetLineStyle(2)
                hist2.SetLineColor(kRed+3)
                hist3.SetLineWidth(3)
                hist3.SetLineStyle(3)
                hist3.SetLineColor(kGreen+3)
                hist1.Draw("hist")
                hist2.Draw("histsame")
                hist3.Draw("histsame")
                hist1.SetTitle("")
                
                xlabel = varname
                if "trigweight_1" in var: xlabel="new trigger weight"
                if "trigweight_2" in var: xlabel="old trigger weight"
                hist1.GetXaxis().SetTitle(xlabel)
                hist1.GetYaxis().SetTitle("A.U.")
                hist1.GetXaxis().SetTitleSize(0.06)
                hist1.GetYaxis().SetTitleSize(0.06)
                hist1.GetXaxis().SetTitleOffset(0.9)
                hist1.GetYaxis().SetTitleOffset(0.9)
                hist1.GetXaxis().SetLabelSize(0.045)
                hist1.GetYaxis().SetLabelSize(0.045)
                hist1.GetYaxis().SetRangeUser(0,max(maxs)*1.08)
                
                (x1,y1) = (0.57,0.88)
                (w,h)   = (0.18,0.24)
                (x2,y2) = (x1+w,y1-h)
                legend = TLegend(x1,y1,x2,y2)
                legend.SetHeader("%s: %s"%(samplelabel,cutname))
                legend.AddEntry(hist1," L && !X && pt_1>23", 'l')
                legend.AddEntry(hist2,"!L &&  X", 'l')
                legend.AddEntry(hist3," L &&  X", 'l')
                legend.SetTextFont(42)
                legend.SetTextSize(0.045)
                legend.SetBorderSize(0)
                legend.SetFillStyle(0)
                legend.Draw()
                
                gStyle.SetOptStat(0)
                filename = ("%s/%s_%s_%s.png"%(OUT_DIR,var,samplelabel,cutname)).replace(' ','_')
                canvas.SaveAs(filename)
                canvas.Close()
                ROOT.gDirectory.Delete(hist1.GetName())
                ROOT.gDirectory.Delete(hist2.GetName())
                ROOT.gDirectory.Delete(hist3.GetName())
                
                file.Close()




def triggers():
    print ">>>\n>>> triggers()"
    
    channel  = "mutau"
    treename = "tree_%s" % channel
    var      = "triggers"
    samples  = [
        #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50" ),
        ("DY",  "DYJetsToLL_M-50_TuneCUETP8M1", "DY M-50" ),
    ]
    cuts = [
        ("no cuts",  "channel>0"),
        ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),             
    ]
    (N,a,b)  = (3,1,4)
    
    for cutname, cut in cuts:
        for sampledir, samplename, samplelabel in samples:
            
            file = TFile("%s/%s/TauTauAnalysis.%s_Moriond.root"%(MORIOND_DIR,sampledir,samplename))
            tree = file.Get(treename)
            
            hist1 = TH1F("hist1", "triggers", N, a, b)            
            tree.Draw("%s >> hist1"%(var),cut,"gOff")
            
            maxs = [ ] 
            I = hist1.Integral()
            print ">>>   %s has %d entries" % (hist1.GetName(),I)
            if I:
                hist1.Scale(1./I)
                maxs.append(hist1.GetMaximum())
            
            print ">>>   %s - %s" % (samplelabel,var)
            canvas = TCanvas("canvas","canvas",100,100,800,600)
            canvas.SetBottomMargin(0.12)
            canvas.SetRightMargin(0.05)
            canvas.SetLeftMargin(0.12)
            canvas.SetTopMargin(0.05)
            hist1.SetLineWidth(3)
            hist1.SetLineStyle(1)
            hist1.SetLineColor(kAzure+4)
            hist1.Draw("hist")
            #hist1.SetTitle("%s: %s"%(samplelabel,cutname))
            
            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(1),"L && !X")
            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(2),"!L && X")
            hist1.GetXaxis().SetBinLabel(hist1.GetXaxis().FindBin(3),"L && X")
            
            #hist1.GetXaxis().SetTitle("trigger weight")
            hist1.GetYaxis().SetTitle("A.U.")
            hist1.GetXaxis().SetTitleSize(0.06)
            hist1.GetYaxis().SetTitleSize(0.06)
            hist1.GetXaxis().SetTitleOffset(0.9)
            hist1.GetYaxis().SetTitleOffset(0.9)
            hist1.GetXaxis().SetLabelSize(0.080)
            hist1.GetYaxis().SetLabelSize(0.045)
            hist1.GetYaxis().SetRangeUser(0,max(maxs)*1.08)
            
            # title = "%s: %s"%(samplelabel,cutname)
            # (x1,y1) = (0.48,0.88)
            # (w,h)   = (0.18,0.24)
            # (x2,y2) = (x1+w,y1-h)
            # legend = TLegend(x1,y1,x2,y2)
            # legend.SetHeader(title)
            # legend.SetTextFont(42)
            # legend.SetTextSize(0.045)
            # legend.SetBorderSize(0)
            # legend.SetFillStyle(0)
            # legend.Draw()
    
            gStyle.SetOptStat(0)
            filename = ("%s/%s_%s_%s.png"%(OUT_DIR,var,samplelabel,cutname)).replace(' ','_')
            canvas.SaveAs(filename)
            canvas.Close()
            ROOT.gDirectory.Delete(hist1.GetName())
            
            file.Close()
        


def ratioTest():
    
    pads = []
    canvas = makeCanvas(ratio=True,pads=pads)
    hist1 = TH1F("hist1","hist1",50,0,100)
    hist2 = TH1F("hist2","hist2",50,0,100)
    
    for i in xrange(10000):
        hist1.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
        hist2.Fill(gRandom.Gaus(50,20),gRandom.Gaus(1,0.1))
    stats = makeStatisticalError(hist2)
    ratio = makeRatio(hist1,hist2)
    
    pads[0].cd()
    hist1.Draw("E")
    hist2.Draw("HIST SAME")
    stats.Draw("E2 SAME")
    
    pads[1].cd()
    ratio.Draw("SAME")
    
    canvas.SaveAs("ratio_test.png")
    


def ratioTest2():
    
    hist1  = TH1F("hist1","hist1",50,0,100)
    hist2  = TH1F("hist2","hist2",50,0,100)
    hist3  = TH1F("hist3","hist3",50,0,100)
    
    hist1u = TH1F("hist1u","hist1u",10000,-50,150)
    hist2u = TH1F("hist2u","hist2u",10000,-50,150)
    hist3u = TH1F("hist3u","hist3u",10000,-50,150)
    
    for i in xrange(10000):
        r = gRandom.Gaus(50,20)
        w = gRandom.Gaus(1,0.1)
        hist1.Fill(r,w)
        hist1u.Fill(r,w)
    for i in xrange(10000):
        r = gRandom.Gaus(50,22)
        w = gRandom.Gaus(0.99,0.1)
        hist2.Fill(r,w)
        hist2u.Fill(r,w)
    for i in xrange(10000):
        r = gRandom.Gaus(51,20)
        w = gRandom.Gaus(1,0.2)
        hist3.Fill(r,w)
        hist3u.Fill(r,w)
        
    entries = ["1: nominal","2: other gaussian","3: another gaussian"]
    for i,histu in enumerate([hist2u,hist3u],1):
        Dn = hist1u.KolmogorovTest(histu)
        print ">>> KolmogorovTest: Dn=%.3f for %s with %s" % (Dn,hist1u.GetName(),histu.GetName())
        entries[i] = "%s (KS %.2f)" % (entries[i],Dn)
    # for i,hist in enumerate([hist2,hist3],1):
    #     Dn = hist1.KolmogorovTest(hist)
    #     print ">>> KolmogorovTest: Dn=%.3f for %s with %s" % (Dn,hist1.GetName(),hist.GetName())
    
    comparison = Comparison(hist1,hist2,hist3)
    comparison.Draw(title="comparing gaussians",entries=entries,markers=False,markers_ratio=False,KS=False)
    comparison.saveAs("ratio_test3.png")
    


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
    


def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
        
        
        
        
def main():
    print ""
    
    makeDirectory(OUT_DIR)
    
    # MAIN CHECKS
#     compareOldToNew()
#     vertexDY()
#     zptweight()
#     trigweight()
#     triggers()
#     ratioTest()
#     ratioTest2()
#     compareOldToNew()
#     compareSamplesForVars()
#     compareVarsForSamples()
#     compareCutsForVars()
    compareVarIntegrals()
#     fitVars()
#     fitUnbinnedVars()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()




