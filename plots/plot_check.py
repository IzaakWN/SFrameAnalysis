#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
import PlotTools.PlotTools
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.PrintTools  import color, warning, error, printSameLine, header
import ROOT
from ROOT import TFile, TH1F, TH2F, THStack, TCanvas, TLegend, kBlue, kAzure, kRed, kGreen, kYellow, kOrange, kMagenta, gPad, gROOT, gStyle
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
    
    MORIOND_DIR  = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    ICHEP_DIR    = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
    
    samples = [
                    #("WJ",          "WJetsToLNu_TuneCUETP8M1"       ),
                    #("TT",          "TT_TuneCUETP8M1"               ),
                    #("DY",          "DYJetsToLL_M-50_TuneCUETP8M1"  ),
                    ("SingleMuon",  "SingleMuon_Run2016"            ),
                ]
    
    for sampledir,sample in samples:
        print ">>>\n>>> comparison ICHEP-Moriond for \"%s\"" % (sample)
        
        file1 = TFile( "%s/%s/TauTauAnalysis.%s_ICHEP.root"   % (ICHEP_DIR,  sampledir,sample))
        file2 = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (MORIOND_DIR,sampledir,sample))
        tree1 = file1.Get("tree_mutau")
        tree2 = file2.Get("tree_mutau")
                
        nocuts      = "channel>0"
        vetos       = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
        isocuts     = "iso_1<0.15 && iso_2 == 1"
        baseline    = "channel>0 && %s && %s && q_1*q_2<0" % (isocuts, vetos)
        
        cuts        = [
                        #("no cuts",   nocuts   ),
                        ("baseline",  baseline ),
                      ]
        
        for cutname, cut in cuts:
            print ">>> selections: %s"     % (cutname)
            print ">>>             \"%s\"" % (cut)
            
            oldcut = cut
            newcut = cut #" && ".join([cut,"triggers==1 && pt_1>23"])
            print ">>>   ICHEP:   entries: %d" % tree1.GetEntries(cut)
            print ">>>   Moriond: entries: %d" % tree2.GetEntries(cut)
            
            vars = [
                            ( "pfmt_1",              50,      0, 150 ),
#                             ( "dilepton_veto",        2,      0, 2.0 ),
#                             ( "extraelec_veto",       2,      0, 2.0 ),
#                             ( "extramuon_veto",       2,      0, 2.0 ),
#                             ( "lepton_vetos",         2,      0, 2.0 ),
#                             ( "againstElectronVLooseMVA6_2", 2, 0, 2 ),
#                             ( "againstMuonTight3_2",  2,     0,  2.0 ),
#                             ( "lepton_vetos",         2,      0, 2.0 ),
#                             ( "iso_1",               50,      0, 0.3 ),
#                             ( "pt_1",               100,      0, 100 ),
#                             ( "pt_2",               100,      0, 100 ),
#                             ( "abs(eta_1)",          50,      0, 2.5 ),
#                             ( "abs(eta_2)",          50,      0, 2.5 ),
#                             ( "q_1",                100,       -4, 4 ),
#                             ( "q_2",                100,       -4, 4 ),
                    ]
            
            weightvars = [ 
                            ( "weight",             100,   -0.2, 1.5 ),
                            ( "trigweight_1",       100,   -0.2, 1.5 ),
                            ( "idisoweight_1",      100,   -0.2, 1.5 ),
                            ( "trigweight_1",       100,   -0.2, 1.5 ),
                            ( "puweight",           100,   -0.2, 1.5 ),
                            ( "weightbtag",         100,   -0.2, 1.5 ),
                        ]
        
            for (var,N,a,b) in vars:
                #print ">>> comparison \"%s\" with \"%s\"" % (var,cut)
            
                oldname = "%s_old"%(var.replace('(','').replace(')',''))
                newname = "%s_new"%(var.replace('(','').replace(')',''))
            
                hist1 = TH1F(oldname, oldname, N, a, b)
                hist2 = TH1F(newname, newname, N, a, b)
                tree1.Draw("%s >> %s"%(var,oldname),oldcut,"gOff")
                tree2.Draw("%s >> %s"%(var,newname),newcut,"gOff")
                N1 = hist1.Integral()
                N2 = hist2.Integral()
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
                hist1.GetXaxis().SetTitle(var)
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
                legend.SetHeader(cutname)
                legend.AddEntry(hist1,"ICHEP   (%d)"%(hist1.GetEntries()), 'l')
                legend.AddEntry(hist2,"Moriond (%d)"%(hist2.GetEntries()), 'l')
                legend.SetTextSize(0.040)
                legend.SetTextFont(42)
                legend.SetBorderSize(0)
                legend.SetFillStyle(0)
                legend.Draw()
                gStyle.SetOptStat(0)
                
                canvas.SaveAs("%s/%s_%s_%s_ICHEP-Moriond.png" % (OUT_DIR,var.replace('(','').replace(')',''),cutname.replace(' ','_'),sampledir))
                canvas.Close()
                ROOT.gDirectory.Delete(hist1.GetName())
                ROOT.gDirectory.Delete(hist2.GetName())
            
        file1.Close()
        file2.Close()
        
    print ">>>"



def shapes():
    print ">>>\n>>> shapes()"
    
    weight    = "weight*trigweight_or_1"
    
    # TTbar CR
    cuts_sets = [
        ( "category 1",[
            (" 1bj,  0cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==1 && nfjets>0"), # && met<60 && pfmt_1<60
            (">0bj,  2cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets==2 && nfjets>0"),
            (">0bj, >1cj, 0>fj",  "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets >1 && nfjets>0"),]),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets>0"),
#         ("pfmt_1<60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>0 && ncjets>1 && nfjets==0"),
#         ("pfmt_1>60",       "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0 && ncbtag>1 && nfjets==0"),
            ]
    
    samples         = [("TT",  "TT_TuneCUETP8M1",                      "ttbar",                    831.76  ), ]
    channels        = ["mutau",] #"etau"]
    
    for subdir,sample,samplename,sigma in samples:
        filename    = "%s/%s/TauTauAnalysis.%s%s.root" % (MORIOND_DIR,subdir,sample,mylabel)
        file        = TFile( filename )
        
        for channel in channels:
            
            treename    = "tree_%s%s"%(channel,"_cut")
            histNname   = "histogram_%s/cutflow_%s"%(channel,channel)
            tree        = file.Get(treename)
            histN       = file.Get(histNname)
            
            if not tree:  print error("shapes - did not find tree %s in %s"%(treename,filename))
            if not histN: print error("shapes - did not find hist %s in %s"%(histNname,filename))
            
            N_tot       = histN.GetBinContent(8)
            normscale   = sigma*lumi*1000/N_tot            
            hists       = [ ]
            var         = "m_sv"
            (N,a,b)     = (50,0.0,250.0)
            I0          = 0
            print ">>> %s scale = %.3f" % (samplename,normscale)
            
            for cutsetname, cutset in cuts_sets:
                for i, (cutname, cut) in enumerate(cutset):
                    
                    cut         = "(%s)*%s"%(cut,weight)
                    histname    = "%s_%s_%d"%(samplename.replace(' ',''),var,i)
                    hist        = TH1F(histname,histname,N,a,b)
                    hist.Sumw2()
                    out         = tree.Draw("%s >> %s"%(var,histname),cut,"gOff")
                    print ">>> %s (%s): %s" % (histname,out,cut)
                    hists.append(hist)
                    hist.Scale(normscale)
                    I           = hist.Integral()
                    if not I:
                        print warning("shapes - %s has integral 0, ignoring"%histname)
                        continue
                    if i is 0:
                        I0 = I
                    if not I0:
                        print error("shapes - first histogram %s has integral 0, ignoring"%histname)
                        exit(1)
                    hist.Scale(I0/I)
                    entryname   = "%.1f - %s"%(I,cutname)
                    print ">>>   entryname = %s"%(entryname)
                    hist.SetTitle(entryname)
                    print ">>> hist.GetTitle()=%s"%(hist.GetTitle())

                canvas = TCanvas("canvas","canvas",100,100,800,600)
                canvas.SetBottomMargin(0.12)
                canvas.SetRightMargin(0.05)
                canvas.SetLeftMargin(0.12)
                canvas.SetTopMargin(0.05)

                hist = hists[0]
                hist.SetLineWidth(3)
                hist.SetLineStyle(1)
                hist.SetLineColor(colors[0])
                hist.SetMarkerSize(0)
                hist.Draw("hist E")
                for i,h in enumerate(hists[1:]):
                    h.SetLineWidth(3)
                    h.SetLineStyle(i%4+1)
                    h.SetLineColor(colors[i+1])
                    h.SetMarkerSize(0)
                    h.Draw("hist E same")
                hist.GetXaxis().SetTitle("SVFit mass m_{sv} [GeV]")
                hist.GetYaxis().SetTitle("number of events / %s GeV"%((b-a)/N))
                hist.GetXaxis().SetTitleSize(0.05)
                hist.GetYaxis().SetTitleSize(0.05)
                hist.GetXaxis().SetTitleOffset(1.00)
                hist.GetYaxis().SetTitleOffset(1.20)
                hist.GetXaxis().SetLabelSize(0.040)
                hist.GetYaxis().SetLabelSize(0.040)
                hist.GetYaxis().SetRangeUser(0,max(hist.GetMaximum(),hist.GetMaximum())*1.15)
            
                (x1,y1) = (0.35,0.25)
                (w,h)   = (0.18,0.02+0.05*len(hists))
                (x2,y2) = (x1+w,y1+h)
                legend = TLegend(x1,y1,x2,y2)
                legend.SetHeader("%s: %s"%(channel.replace("mu","#mu").replace("tau","#tau"),cutsetname))
                for h in hists:
                    print ">>> h.GetTitle()=%s"%(h.GetTitle())
                    legend.AddEntry(h,h.GetTitle(), 'l')
                legend.SetTextSize(0.035)
                legend.SetTextFont(42)
                legend.SetBorderSize(0)
                legend.SetFillStyle(0)
                legend.Draw()
                gStyle.SetOptStat(0)
            
                canvas.SaveAs("%s/%s_%sshape_%s-%s.png" % (OUT_DIR,var.replace('(','').replace(')',''),subdir,channel,cutsetname.replace(' ','')))
                canvas.Close()
                #1ROOT.gDirectory.Delete(hist1.GetName())
        
        file.Close()



def vertexDY():
    print ">>>\n>>> vertexDY()"
    
    DIR  = "/shome/ineuteli/analysis/SFrameAnalysis_Moriond/TauTauResonances/"
    file1 = TFile( DIR + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
    file2 = TFile( DIR + "TauTauAnalysis.DYJets_M-50.UZH.root" )
    
    
    histnames = [ "d0_lepton_tail", "dz_lepton_tail", "d0_lepton", "dz_lepton",
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
    print ">>>\n>>> trigweight()"
    
    channel  = "mutau"
    treename = "tree_%s" % channel
    vars     = ["trigweight_1", "trigweight_2"]
    samples  = [
                    #("DY",  "DYJetsToLL_M-10to50_TuneCUETP8M1", "DY M-10to50" ),
                    ("DY",  "DYJetsToLL_M-50_TuneCUETP8M1", "DY M-50" ),
                ]
    cuts = [
             ("no cuts",  "channel>0"),
             ("baseline", "channel>0 && iso_cuts==1 && lepton_vetos==0 && q_1*q_2<0"),
             
            ]
    (N,a,b)  = (100,0,3) 
    
    for var in vars:
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
                
                xlabel = "trigger weight"
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
                


def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
        
        
        
        
def main():
    print ""
    
    makeDirectory(OUT_DIR)
    
    # MAIN CHECKS
    #compareOldToNew()
#     compareOldToNewEfficiency()
#     compareDataSetEfficiencies()
#     compareTriggerEfficiencies()
#     compareSignalEfficiency()
    #vertexDY()
    #zptweight()
#     trigweight()
#     triggers()
    shapes()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()



        
        
    


# def numbers():
#     print ">>>\n>>> numbers()"
# 
#     ROOT.gROOT.SetBatch(ROOT.kTRUE)
#     lumi  = 24.5
#     DIR = "/shome/ineuteli/analysis/SFrameAnalysis/AnalysisOutput/"
#     samplesB = [
# #                     ("TT/", "TT_TuneCUETP8M1",                      "ttbar",              831.76  ),
#                     ("DY/", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell-Yan 10-50",  18610.0   ),
# #                     ("DY/", "DYJetsToLL_M-50_TuneCUETP8M1",         "Drell-Yan 50",      5765.4   ),
# #                     ("WJ/", "WJetsToLNu_TuneCUETP8M1",              "WJ",               61526.7   ),
# #                     ("WZ/", "WZ_TuneCUETP8M1",                      "WZ",                  39.9   ), # wrong cross section 
# #                     ("ZZ/", "ZZ_TuneCUETP8M1",                      "ZZ",                  10.32  ), # wrong cross section 
#                ]
# 
# 
#     print "\n>>> integrated luminosity L = %s pb" % lumi
#     print ">>> "
#     print ">>>    %15s %12s %12s %12s %12s %12s %12s" % ( " ", "cutflow N_1", "cutflow N_6", "tree N", "hist N", "sigma [pb]", "scale" )
#     for s, i in zip(samplesB,range(len(samplesB))):
# 
#         file1 = TFile( DIR + s[0] + "TauTauAnalysis.%s.root" % s[1] )
#         N_1 = file1.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
#         N_6 = file1.Get("histogram_mutau/cutflow_mutau").GetBinContent(6)
#     
# #         file2 = TFile( DIR + s[0] + "%s_mutau.root" % s[1] )
#         tree  = file1.Get("tree_mutau")
#     
#         hist = TH1F("hist","hist",40,-20,20)
#         tree.Draw("weight >> hist","( channel == 1 )*weight","goff")
#         
#         scale = lumi * s[3] * 1000 / N_1
#         print ">>>    %-15s %12i %12i %12i %12i %12.5g %12.5g" % ( s[2], N_1, N_6, tree.GetEntries(), hist.Integral(), s[3], scale )
# 
# 
# 
# 
# 
# def signalEfficiency():
#     print ">>>\n>>> signalEfficiency()"
# 
#     # bin 1: no cuts
#     # bin 2: JSON / gen weight
#     # bin 3: triggers
#     # bin 4: MET filters
#     # bin 5: lepton selection
#     # bin 6: lepton-tau pair selection
#     # bin 7: no cuts gen weighted
#     
#     cuts = [    "no cuts",
#                 "JSON/weight",
#                 "triggers",
#                 "MET filters",
#                 "lepton",
#                 "lepton-tau",
#                 "no cuts (weighted)",
#             ]
#     
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     efficiencies = [ ]
#     for i, cut in zip(range(1,len(cuts)+1),cuts):
#         N = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i)
#         N_tot = 0
#         if i is 1:
#             N = 1
#             N_tot = 1
#         else:
#             N_tot = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i-1)
#             
#         if N and N_tot:
#             efficiencies.append(( cut, N / N_tot ))
#         else:
#             print ">>> Warning: GetBinContent(%i) = %s, GetBinContent(%i) = %s " % (i,N,i-1,N_tot)
#     
#     for cut, efficiency in efficiencies:
#         print ">>> %s: %5.2f%%" % (cut,efficiency*100)
# 
# 
# 
# 
# 
# def ptSignalAcceptence():
#     print ">>>\n>>> ptSignalAcceptence()"
# 
#     cut = 23. 
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     pt_taus = file.Get("checks/pt_gentaus")
#     pt_tau1 = file.Get("checks/pt_gentau1")
#     pt_tau2 = file.Get("checks/pt_gentau2")
#     pt_muon = file.Get("checks/pt_genmuon")
#     
#     bincut_taus = pt_taus.FindBin(cut)
#     bincut_tau1 = pt_tau1.FindBin(cut)
#     bincut_tau2 = pt_tau2.FindBin(cut)
#     bincut_muon = pt_muon.FindBin(cut)
#     N_taus = pt_taus.Integral()
#     N_tau1 = pt_tau1.Integral()
#     N_tau2 = pt_tau2.Integral()
#     N_muon = pt_muon.Integral()
#     
#     eff_taus = pt_taus.Integral(bincut_taus, pt_taus.GetNbinsX()) / N_taus
#     eff_tau1 = pt_tau1.Integral(bincut_tau1, pt_tau1.GetNbinsX()) / N_tau1
#     eff_tau2 = pt_tau2.Integral(bincut_tau2, pt_tau2.GetNbinsX()) / N_tau2
#     eff_muon = pt_muon.Integral(bincut_muon, pt_muon.GetNbinsX()) / N_muon
#     
#     print ">>> efficiency of pt cut of %s on signal's gen tau and reco muon:" % cut
#     print ">>> gen tau:  %5.2f%%" % (100*eff_taus)
#     print ">>> gen tau1: %5.2f%%" % (100*eff_tau1)
#     print ">>> gen tau2: %5.2f%%" % (100*eff_tau2)
#     print ">>> gen muon: %5.2f%%" % (100*eff_muon)
# 
#     print ">>> check: bincut_taus = %3i,  N_taus =%7i" % (bincut_taus,N_taus)
#     print ">>> check: bincut_tau2 = %3i,  N_tau1 =%7i" % (bincut_tau1,N_tau1)
#     print ">>> check: bincut_tau3 = %3i,  N_tau2 =%7i" % (bincut_tau2,N_tau2)
#     print ">>> check: bincut_muon = %3i,  N_muon =%7i" % (bincut_muon,N_muon)
#     
#     # DRAW
#     canvas = TCanvas("canvas","canvas",100,100,800,600) # 600,600
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     pt_taus.SetLineWidth(3)
#     pt_muon.SetLineWidth(3)
#     pt_taus.SetLineColor(kAzure+4)
#     pt_muon.SetLineColor(kRed+3)
#     pt_taus.Scale(1/N_taus)
#     pt_muon.Scale(1/N_muon/3)
#     #pt_taus.Rebin(2)
#     #pt_muon.Rebin(2)
#     pt_taus.Draw("hist")
#     pt_muon.Draw("histsame")
#     pt_taus.SetTitle("")
#     pt_taus.GetXaxis().SetRangeUser(0,100)
#     pt_taus.GetXaxis().SetTitle("p_{T} of generator level particle")
#     pt_taus.GetYaxis().SetTitle("A.U.")
#     #pt_taus.GetYaxis().SetTitleSize(0)
#     pt_taus.GetXaxis().SetTitleSize(0.05)
#     pt_taus.GetYaxis().SetTitleSize(0.05)
#     pt_taus.GetXaxis().SetTitleOffset(1.14)
#     pt_taus.GetYaxis().SetTitleOffset(1.17)
#     pt_taus.GetXaxis().SetLabelSize(0.045)
#     pt_taus.GetYaxis().SetLabelSize(0.040)
#     #pt_taus.GetYaxis().SetLabelSize(0)    
#     legend = TLegend(0.56,0.68,0.80,0.84)
#     legend.AddEntry(pt_taus, " gen #tau", 'l')
#     legend.AddEntry(pt_muon, " gen #mu from #tau", 'l')
#     legend.SetTextSize(0.055)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     #gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/pt.png")
#     canvas.Close()
#     
#     
# 
#     
# def DYAcceptence():
#     print ">>>\n>>> DYAcceptence()"
# 
#     DIR2 = "/shome/ineuteli/analysis/SFrameAnalysis/TauTauResonances/"
# 
# #     file = TFile( DIR2 + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
#     file = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-10to50_TuneCUETP8M1%s.root" % mylabel )
#     pt = file.Get("checks/pt_muon")
#     d0 = file.Get("checks/d0_muon")
#     dz = file.Get("checks/dz_muon")
#     d0_cut = file.Get("checks/d0_muon_cut")
#     dz_cut = file.Get("checks/dz_muon_cut")
# #     file2 = TFile( DIR2 + "TauTauAnalysis.DYJets_M-50.UZH.root" )
#     file2 = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1%s.root" % mylabel )
#     pt2 = file2.Get("checks/pt_muon")
#     d02 = file2.Get("checks/d0_muon")
#     dz2 = file2.Get("checks/dz_muon")
#     d02_cut = file2.Get("checks/d0_muon_cut")
#     dz2_cut = file2.Get("checks/dz_muon_cut")
#     var_dict = { "pt_muon":"muon p_{T}", "d0_muon":"muon d0", "dz_muon":"muon |dz|",
#                  "d0_muon_cut":"muon d0", "dz_muon_cut":"muon |dz|" }
#     
#     print ">>>\n>>> overflow DY check"
#     print ">>> DY M-10to50 pt overflow:              %9i /%9i = %5.1f%%" % ( pt.GetBinContent(pt.GetNbinsX()+1),   pt.GetEntries(),  pt.GetBinContent(pt.GetNbinsX()+1)   /  pt.GetEntries()*100 )
#     print ">>> DY M-50     pt overflow:              %9i /%9i = %5.1f%%" % ( pt2.GetBinContent(pt2.GetNbinsX()+1), pt2.GetEntries(), pt2.GetBinContent(pt2.GetNbinsX()+1) / pt2.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow:              %9i /%9i = %5.1f%%" % ( d0.GetBinContent(d0.GetNbinsX()+1),   d0.GetEntries(),  d0.GetBinContent(d0.GetNbinsX()+1)   / d0.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow:              %9i /%9i = %5.1f%%" % ( d02.GetBinContent(d02.GetNbinsX()+1), d02.GetEntries(), d02.GetBinContent(d02.GetNbinsX()+1) / d02.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d0_cut.GetBinContent(d0_cut.GetNbinsX()+1),   d0_cut.GetEntries(),  d0_cut.GetBinContent(d0_cut.GetNbinsX()+1)   / d0_cut.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d02_cut.GetBinContent(d02_cut.GetNbinsX()+1), d02_cut.GetEntries(), d02_cut.GetBinContent(d02_cut.GetNbinsX()+1) / d02_cut.GetEntries()*100 )
#     print ">>> DY M-10to50 dz overflow:              %9i /%9i = %5.1f%%" % ( dz.GetBinContent(dz.GetNbinsX()+1),   dz.GetEntries(),  dz.GetBinContent(dz.GetNbinsX()+1)   / dz.GetEntries()*100  )
#     print ">>> DY M-50     dz overflow:              %9i /%9i = %5.1f%%" % ( dz2.GetBinContent(dz2.GetNbinsX()+1), dz2.GetEntries(), dz2.GetBinContent(dz2.GetNbinsX()+1) / dz2.GetEntries()*100 )
#     print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz_cut.GetBinContent(dz_cut.GetNbinsX()+1),   dz_cut.GetEntries(),  dz_cut.GetBinContent(dz_cut.GetNbinsX()+1)   / dz_cut.GetEntries()*100  )
#     print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1), dz2_cut.GetEntries(), dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1) / dz2_cut.GetEntries()*100 )
#     
#     for var, hist, hist2 in [ ("pt_muon",pt,pt2), ("d0_muon",d0,d02), ("dz_muon",dz,dz2), ("d0_muon_cut",d0_cut,d02_cut), ("dz_muon_cut",dz_cut,dz2_cut) ]:
#         canvas = TCanvas("canvas","canvas",100,100,800,600)
#         canvas.SetBottomMargin(0.12)
#         canvas.SetRightMargin(0.05)
#         canvas.SetLeftMargin(0.05)
#         canvas.SetTopMargin(0.05)
#         hist.SetLineWidth(3)
#         hist.SetLineStyle(1)
#         hist.SetLineColor(kAzure+4)
#         hist2.SetLineWidth(3)
#         hist2.SetLineStyle(7)
#         hist2.SetLineColor(kRed+3)
#         hist.Draw("hist")
#         hist2.Draw("histsame")
#         hist.Scale(1/hist.Integral())
#         hist2.Scale(1/hist2.Integral())
#         hist.SetTitle("")
#         #hist.GetXaxis().SetRangeUser(0,100)
#         hist.GetXaxis().SetTitle(var_dict[var]) #replace
#         hist.GetYaxis().SetTitleSize(0)
#         hist.GetXaxis().SetTitleSize(0.05)
#         hist.GetXaxis().SetTitleOffset(1.15)
#         hist.GetXaxis().SetLabelSize(0.045)
#         hist.GetYaxis().SetLabelSize(0)
#         hist.GetYaxis().SetRangeUser(0,max(hist.GetMaximum(),hist2.GetMaximum())*1.12)
#         h = 0.18
#         w = 0.25
#         legend = TLegend(0.64,0.7,0.64-w,0.7-h)
#         legend.AddEntry(hist, " DY 10 < m < 50", 'l')
#         legend.AddEntry(hist2," DY 50 > m", 'l')
#         legend.SetTextSize(0.042)
#         legend.SetBorderSize(0)
#         legend.SetFillStyle(0)
#         legend.Draw()
#         gStyle.SetOptStat(0)
#         canvas.SaveAs("plots_check/%s.png" % var)
#         canvas.Close()
#         
#     vetos   = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
#     isocuts = "iso_1 < 0.15 && iso_2 == 1"
#     cuts    = [ ("SS",         "channel==1 && q_1*q_2<0"),
#                 ("iso",        "channel==1 && %s && q_1*q_2<0" % (isocuts)),
#                 #("isow",       "(channel==1 && %s && q_1*q_2<0)*idisoweight_1*trigweight_1" % (isocuts)),
#                 ("vetos",      "channel==1 && %s && %s && q_1*q_2<0" % (isocuts, vetos)),
#                 ("category 1", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets == 1 && nfjets  > 0" % (isocuts, vetos)),
#                 ("category 2", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets  > 1 && nfjets == 0 && dphi_ll_bj > 2 && met < 60" % (isocuts, vetos)),
#                ]
#     # TODO weights?
#     #  trigweight_1 * idisoweight_1 * trigweight_2 * idisoweight_2
#     
#     tree  = file.Get("tree_mutau")
#     tree2 = file2.Get("tree_mutau")
#     iso_1  = TH1F("iso_1", "iso_1", 100, -10, 10)
#     iso_12 = TH1F("iso_12", "iso_12", 100, -10, 10)
#     tree.Draw( "iso_1 >> iso_1",   "channel==1", "gOff")
#     tree2.Draw("iso_1 >> iso_12",  "channel==1", "gOff")
#     N_tot = iso_1.Integral()
#     N_tot2 = iso_12.Integral()
# 
#     print ">>>\n>>> cuts on DY:"
#     for label, cut in cuts: 
#         iso_1.Reset()
#         iso_12.Reset()
#         tree.Draw("iso_1 >> iso_1",   cut, "gOff")
#         tree2.Draw("iso_1 >> iso_12", cut, "gOff")
#         N  = iso_1.Integral() #GetEntries
#         N2 = iso_12.Integral()
#         print ">>> %s:" % label
#         if N_tot:  print ">>>   DY M-10to50: %4.1f%% (%6i,%6i)" % ( N/N_tot*100.0,   N,  N_tot  )
#         if N_tot2: print ">>>   DY M-50:     %4.1f%% (%6i,%6i)" % ( N2/N_tot2*100.0, N2, N_tot2 )
#         if "category" not in label and "isow" not in label:
#             N_tot  = N
#             N_tot2 = N2
#         
#     file.Close()
#     file2.Close()
#     
#     
#     
#     
#     
#     
# def deltaR():
#     print ">>>\n>>> deltaR()"
#     
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     DeltaR_tautau  = file.Get("checks/DeltaR_tautau")
#     DeltaR_taumu   = file.Get("checks/DeltaR_taumu")
#     
#     fileH = TFile( DIR + "gen_plots/root_files/HTT.root" )
#     treeH = fileH.Get("Events")
#     DeltaR_Htautau = TH1F("DeltaR_Htautau", "DeltaR_Htautau", 100, 0, 4)
#     treeH.Draw("dR_ll >> DeltaR_Htautau")
#     
#     cut = 0.5
#     bincut_tautau = DeltaR_tautau.FindBin(cut)
#     bincut_taumu  = DeltaR_taumu.FindBin(cut)
#     N_tautau = DeltaR_tautau.Integral()
#     N_taumu  = DeltaR_taumu.Integral()
#     eff_tautau = DeltaR_tautau.Integral(bincut_tautau, DeltaR_tautau.GetNbinsX()) / N_tautau
#     eff_taumu  = DeltaR_taumu.Integral( bincut_taumu,  DeltaR_taumu.GetNbinsX())  / N_taumu
#     print ">>> efficiency of DeltaR cut of %s on signal's gen tau and reco muon:" % cut
#     print ">>> gen tautau:  %5.2f%%" % (100*eff_tautau)
#     print ">>> gen taumu:   %5.2f%%" % (100*eff_taumu)
#     print ">>> check: bincut_tautau = %3i,  N_tautau =%7i" % (bincut_tautau, N_tautau)
#     print ">>> check: bincut_taumu  = %3i,  N_taumu  =%7i" % (bincut_taumu,  N_taumu)
#     
# #     for DR, hist in [ ("DeltaR_tautau",DeltaR_tautau), ("DeltaR_taumu",DeltaR_taumu) ]:
# #         canvas = TCanvas("canvas","canvas",100,100,800,600)
# #         canvas.SetBottomMargin(0.12)
# #         canvas.SetRightMargin(0.05)
# #         canvas.SetLeftMargin(0.05)
# #         canvas.SetTopMargin(0.05)
# #         hist.SetLineWidth(3)
# #         hist.SetLineColor(kAzure+4)
# #         hist.Draw("hist")
# #         hist.Scale(1/hist.Integral())
# #         hist.SetTitle("")
# #         #hist.GetXaxis().SetRangeUser(0,100)
# #         hist.GetXaxis().SetTitle(DR.replace("Delta","#Delta ").replace("_tautau","_{#tau#tau}").replace("_taumu","_{#tau#mu}"))
# #         hist.GetYaxis().SetTitleSize(0)
# #         hist.GetXaxis().SetTitleSize(0.05)
# #         hist.GetXaxis().SetTitleOffset(1.15)
# #         hist.GetXaxis().SetLabelSize(0.045)
# #         hist.GetYaxis().SetLabelSize(0)
# #         gStyle.SetOptStat(0)
# #         canvas.SaveAs("plots_check/%s.png" % DR)
# #         canvas.Close()
#         
#     canvas = TCanvas("canvas","canvas",100,100,800,600)
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     DeltaR_tautau.SetLineWidth(3)
#     DeltaR_tautau.SetLineStyle(1)
#     DeltaR_tautau.SetLineColor(kAzure+4)
#     DeltaR_taumu.SetLineWidth(3)
#     DeltaR_taumu.SetLineStyle(7)
#     DeltaR_taumu.SetLineColor(kRed+3)
#     DeltaR_Htautau.SetLineWidth(3)
#     DeltaR_Htautau.SetLineStyle(1)
#     DeltaR_Htautau.SetLineColor(kOrange) #kYellow
#     DeltaR_tautau.Draw(  "hist")
#     DeltaR_Htautau.Draw( "histsame")
#     DeltaR_tautau.Draw(  "histsame")
#     DeltaR_taumu.Draw(   "histsame")
#     DeltaR_tautau.Scale(  1/DeltaR_tautau.GetMaximum()) # Integral
#     DeltaR_taumu.Scale(   1/DeltaR_taumu.GetMaximum())
#     DeltaR_Htautau.Scale( 1/DeltaR_Htautau.GetMaximum())
#     DeltaR_tautau.SetTitle("")
#     DeltaR_tautau.GetXaxis().SetRangeUser(0,4)
#     DeltaR_tautau.GetXaxis().SetTitle("#DeltaR")
#     DeltaR_tautau.GetYaxis().SetTitle("A.U.")
#     DeltaR_tautau.GetXaxis().SetTitleSize(0.06)
#     DeltaR_tautau.GetYaxis().SetTitleSize(0.06)
#     DeltaR_tautau.GetXaxis().SetTitleOffset(0.9)
#     DeltaR_tautau.GetXaxis().SetLabelSize(0.045)
#     DeltaR_tautau.GetYaxis().SetLabelSize(0.045)
#     DeltaR_tautau.GetYaxis().SetRangeUser(0,DeltaR_tautau.GetMaximum()*1.12)
#     h = 0.18
#     w = 0.25
#     legend = TLegend(0.61,0.75,0.61-w,0.75-h)
#     legend.AddEntry(DeltaR_tautau,  " signal X #rightarrow #tau#tau", 'l')
#     legend.AddEntry(DeltaR_taumu,   " signal X #rightarrow #tau#tau #rightarrow #mu#tau_{h}", 'l')
#     legend.AddEntry(DeltaR_Htautau, " SM Higgs #rightarrow #tau#tau", 'l')
#     legend.SetTextSize(0.042)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/DeltaR.png")
#     canvas.Close()
#     file.Close()
#     fileH.Close()
#     
# 
#     # MASS
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     M_tautau  = file.Get("checks/M_tautau")
#     
#     canvas = TCanvas("canvas","canvas",100,100,800,600)
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     M_tautau.SetLineWidth(3)
#     M_tautau.SetLineStyle(1)
#     M_tautau.SetLineColor(kAzure+4)
#     M_tautau.Draw("hist")
#     M_tautau.Scale(1/M_tautau.GetMaximum()) # Integral
#     M_tautau.SetTitle("")
#     M_tautau.GetXaxis().SetTitle("M_{#tau#tau}")
#     M_tautau.GetYaxis().SetTitle("A.U.")
#     M_tautau.GetXaxis().SetTitleSize(0.06)
#     M_tautau.GetYaxis().SetTitleSize(0.06)
#     M_tautau.GetXaxis().SetTitleOffset(0.9)
#     M_tautau.GetXaxis().SetLabelSize(0.045)
#     M_tautau.GetYaxis().SetLabelSize(0.045)
#     M_tautau.GetYaxis().SetRangeUser(0,M_tautau.GetMaximum()*1.12)
#     h = 0.18
#     w = 0.25
#     legend = TLegend(0.85,0.75,0.85-w,0.75-h)
#     legend.AddEntry(M_tautau, " signal X #rightarrow #tau#tau", 'l')
#     legend.SetTextSize(0.042)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/M_tautau.png")
#     canvas.Close()
#     file.Close()
#     fileH.Close()
#     
#     
#     
#     
#     
#     
#     
#     
#     
# def deltaR2():
#     print ">>>\n>>> deltaR2()"
#     
#     #DIRT = "/shome/ineuteli/analysis/SFrameAnalysis/TauTauResonances/"
#     #file = TFile( DIRT + "TauTauAnalysis.Signal.UZH.root" )
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     DeltaR1 = file.Get("checks/DeltaR_gentau_recotau_std")
#     DeltaR2 = file.Get("checks/DeltaR_gentau_recotau_bst")
#         
#     cut = 0.2
#     bincut1 = DeltaR1.FindBin(cut)
#     bincut2 = DeltaR2.FindBin(cut)
#     N1 = DeltaR1.Integral()
#     N2 = DeltaR2.Integral()
#     eff1 = DeltaR1.Integral(1, bincut1) / N1
#     eff2 = DeltaR2.Integral(1, bincut2) / N2
#     print ">>> percentage of gen-reco tau pairs with DeltaR < %s:" % cut
#     print ">>> standard tau ID:  %5.2f%%" % (100*eff1)
#     print ">>> boosted tau ID:   %5.2f%%" % (100*eff2)
#     print ">>> check: bincut1 = %2i, N1 =%8i" % (bincut1, N1)
#     print ">>> check: bincut2 = %2i, N2 =%8i" % (bincut2, N2)
#     print ">>> check: edges bin1 = [%3.2f, %3.2f]" % (DeltaR1.GetBinLowEdge(bincut1), DeltaR1.GetBinLowEdge(bincut1)+DeltaR1.GetBinWidth(bincut1))
#     print ">>> check: edges bin2 = [%3.2f, %3.2f]" % (DeltaR2.GetBinLowEdge(bincut2), DeltaR2.GetBinLowEdge(bincut2)+DeltaR2.GetBinWidth(bincut2))
# 
#         
#     canvas = TCanvas("canvas","canvas",100,100,800,600)
#     canvas.SetBottomMargin(0.14)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     DeltaR1.SetLineWidth(3)
#     DeltaR1.SetLineStyle(1)
#     DeltaR1.SetLineColor(kAzure+4)
#     DeltaR2.SetLineWidth(3)
#     DeltaR2.SetLineStyle(7)
#     DeltaR2.SetLineColor(kRed+3)
#     DeltaR1.Draw("hist")
#     DeltaR2.Draw("histsame")
#     DeltaR1.Scale(1/DeltaR1.Integral()) # Integral / GetMaximum
#     DeltaR2.Scale(1/DeltaR2.Integral())
#     DeltaR1.SetTitle("")
#     DeltaR1.GetXaxis().SetRangeUser(0,4)
#     DeltaR1.GetXaxis().SetTitle("#DeltaR( #tau^{gen}_{h}, #tau^{reco}_{h})")
#     DeltaR1.GetYaxis().SetTitle("A.U.")
#     DeltaR1.GetXaxis().SetTitleSize(0.06)
#     DeltaR1.GetYaxis().SetTitleSize(0.06)
#     DeltaR1.GetXaxis().SetTitleOffset(0.85)
#     DeltaR1.GetXaxis().SetLabelSize(0.045)
#     DeltaR1.GetYaxis().SetLabelSize(0.045)
#     DeltaR1.GetYaxis().SetRangeUser(0,DeltaR1.GetMaximum()*1.12)
#     h = 0.18
#     w = 0.25
#     legend = TLegend(0.61,0.75,0.61-w,0.75-h)
#     legend.AddEntry(DeltaR1, " standard tau ID", 'l')
#     legend.AddEntry(DeltaR2, " boosted tau ID", 'l')
#     legend.SetTextSize(0.042)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/DeltaR_genrecotau.png")
#     canvas.Close()
#     file.Close()
#     
#     
#     
#     
#     
# def Delta_eta_phi():
#     print ">>>\n>>> Delta_eta_phi()"
# 
#     CMS_lumi.cmsTextSize = 0.50
#     CMS_lumi.lumiTextSize = 0.45
#     CMS_lumi.relPosX = 0.115
#     gStyle.SetPalette(1) # for rainbow colors
# 
#     for sample in ["HTT", "LowMassDiTau"]:
# 
#         fileH = TFile( DIR + "gen_plots/root_files/%s.root" % sample )
#         treeH = fileH.Get("Events")
#         Delta_eta_phi = TH2F("Delta_eta_phi", "Delta_eta_phi", 100, 0, 3.2, 100, 0, 3.2)
#         treeH.Draw("abs(dphi_ll):abs(deta_ll) >> Delta_eta_phi") #abs(deta):abs(dphi) #deta:dphi
#     
#         canvas = TCanvas("canvas","canvas",100,100,800,800)
#         canvas.SetBottomMargin(0.12)
#         canvas.SetRightMargin(0.12)
#         canvas.SetLeftMargin(0.12)
#         canvas.SetTopMargin(0.05)
#         Delta_eta_phi.SetTitle("")
#         Delta_eta_phi.Draw("colz")
#         canvas.SaveAs("plots_check/Delta_eta_phi_%s.png" % sample)
#         CMS_lumi.CMS_lumi(canvas,14,0)
#         canvas.Close()
#         fileH.Close()
# 
#     
#     
#     
#     
#     
# def eta():
#     print ">>>\n>>> eta()"
#     
#     fileH = TFile( DIR + "gen_plots/root_files/LowMassDiTau.root" )
#     treeH = fileH.Get("Events")
#     eta_l = TH1F("eta_l", "eta_l", 100, -5.5, 5.5)
#     eta_b = TH1F("eta_b", "eta_b", 100, -5.5, 5.5)
#     treeH.Draw("jeteta_l >> eta_l") #abs(jeteta_l)
#     treeH.Draw("jeteta_b >> eta_b") #abs(jeteta_b)
#         
#     canvas = TCanvas("canvas","canvas",100,100,800,600)
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     eta_l.SetLineWidth(3)
#     eta_l.SetLineStyle(1)
#     eta_l.SetLineColor(kAzure+4)
#     eta_b.SetLineWidth(3)
#     eta_b.SetLineStyle(2)
#     eta_b.SetLineColor(kRed+3)
#     eta_l.Draw("hist")
#     eta_b.Draw("histsame")
#     eta_l.Scale(1/eta_l.GetMaximum())
#     eta_b.Scale(1/eta_b.GetMaximum())
#     eta_l.SetTitle("")
#     #eta_l.GetXaxis().SetRangeUser(0,5)
#     eta_l.GetXaxis().SetTitle("quark #eta") #|#eta|
#     eta_l.GetYaxis().SetTitle("A.U.")
#     eta_l.GetXaxis().SetTitleSize(0.06)
#     eta_l.GetYaxis().SetTitleSize(0.06)
#     eta_l.GetXaxis().SetTitleOffset(0.9)
#     eta_l.GetXaxis().SetLabelSize(0.045)
#     eta_l.GetYaxis().SetLabelSize(0.045)
#     eta_l.GetYaxis().SetRangeUser(0,eta_l.GetMaximum()*1.08)
#     h = 0.12
#     #legend = TLegend(0.8,0.65,0.52,0.45)
#     legend = TLegend(0.8,0.35,0.42,0.35-h)
#     legend.AddEntry(eta_l," light quark", 'l')
#     legend.AddEntry(eta_b," b quark", 'l')
#     legend.SetTextSize(0.045)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/eta.png")
#     canvas.Close()
#     fileH.Close()
#     
#     
#     
# def checkStackIntegral():
#     print ">>>\n>>> checkStackIntegral"
# 
#     file_DY = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1%s.root" % mylabel )
#     file_WJ = TFile( DIR + "WJ/TauTauAnalysis.WJetsToLNu_TuneCUETP8M1%s.root" % mylabel )
#     tree_DY = file_DY.Get("tree_mutau")
#     tree_WJ = file_WJ.Get("tree_mutau")
# 
#     h1 = TH1F("h1","h1",100,0,70)
#     h2 = TH1F("h2","h2",100,0,70)
#     tree_DY.Draw("m_vis >> h1","weight","goff")
#     tree_WJ.Draw("m_vis >> h2","weight","goff")
# 
#     stack = THStack("stack","stack")
#     stack.Add(h1)
#     stack.Add(h2)
#     #stack.Draw()
#     print ">>> hist  integral = %11.2f" % (h1.Integral())
#     print ">>> stack integral = %11.2f" % (stack.GetStack().Last().Integral())
#     h1.Scale(5)
#     print ">>> hist  integral = %11.2f" % (h1.Integral())
#     print ">>> stack integral = %11.2f" % (stack.GetStack().Last().Integral())
#     #stack.Draw()
#     
#     
#     
# def countEvent():
#     print ">>>\n>>> countEvent()"
# 
#     vetos   = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
#     isocuts = "iso_1 < 0.15 && iso_2 == 1"
#     cuts    = [ ("category 1", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets == 1 && nfjets  > 0" % (isocuts, vetos)),
#                 ("category 2", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets  > 1 && nfjets == 0 && dphi_ll_bj > 2 && met < 50" % (isocuts, vetos)),
#                ]
# 
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )    
#     tree = file.Get("tree_mutau")
#     
#     for label, cut in cuts:
#         hist = TH1F("hist", "hist", 35, 0, 70)
#         canvas = TCanvas("canvas","canvas",100,100,400,300)
#         tree.Draw("m_vis >> hist", cut)
#         print ">>> %s: signal MC sample has %3i events" % (label,hist.Integral())
#         canvas.SaveAs("plots_check/%s.png" % label.replace(" ","_"))
#         ROOT.gDirectory.Delete(hist.GetName())
#         canvas.Close()
#         
#     
#     
# def DeltaR_vs_pt_tt():
#     print ">>>\n>>> DeltaR_vs_pt_tt"
#     
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     hist = file.Get("checks/DeltaR_pt_tt_vis_ltau")
#     prof = hist.ProfileX()
#     
#     canvas = TCanvas("canvas","canvas",100,100,800,800)
#     canvas.SetBottomMargin(0.10)
#     canvas.SetRightMargin(0.12)
#     canvas.SetLeftMargin(0.10)
#     canvas.SetTopMargin(0.05)
#     hist.SetTitle("")
#     hist.Draw("colz")
#     prof.Draw("same")
#     prof.SetLineWidth(3)
#     prof.SetLineStyle(1)
#     prof.SetLineColor(kRed+3)
#     hist.GetXaxis().SetTitleOffset(1.2)
#     hist.GetYaxis().SetTitleOffset(1.1)
#     hist.GetXaxis().SetTitle("generator level p_{T}^{l#tau_{h}}")
#     hist.GetYaxis().SetTitle("generator level #DeltaR_{l#tau_{h}}")
#     legend = TLegend(0.90,0.75,0.50,0.90)
#     legend.AddEntry(prof,"average #DeltaR", 'l')
#     legend.SetTextSize(0.045)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     canvas.SaveAs("plots_check/DeltaR_pt_tt_vis_ltau.png")
#     CMS_lumi.CMS_lumi(canvas,14,0)
#     canvas.Close()
#     file.Close()
# 
#     
#     
#     
#     
# def pt_tt():
#     print ">>>\n>>> pt_tt()"
#     
#     file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
#     hist1 = file.Get("checks/pt_tt_gen")
#     hist2 = file.Get("checks/pt_tt_vis_ltau")
#         
#     canvas = TCanvas("canvas","canvas",100,100,800,600)
#     canvas.SetBottomMargin(0.12)
#     canvas.SetRightMargin(0.05)
#     canvas.SetLeftMargin(0.12)
#     canvas.SetTopMargin(0.05)
#     hist1.SetLineWidth(3)
#     hist1.SetLineStyle(1)
#     hist1.SetLineColor(kAzure+4)
#     hist2.SetLineWidth(3)
#     hist2.SetLineStyle(2)
#     hist2.SetLineColor(kRed+3)
#     hist1.Draw("hist")
#     hist2.Draw("histsame")
#     hist1.Scale(1/hist1.GetMaximum())
#     hist2.Scale(1/hist2.GetMaximum())
#     hist1.SetTitle("")
#     #hist1.GetXaxis().SetRangeUser(0,5)
#     hist1.GetXaxis().SetTitle("generator level p_{T}^{#tau#tau}")
#     hist1.GetYaxis().SetTitle("A.U.")
#     hist1.GetXaxis().SetTitleSize(0.06)
#     hist1.GetYaxis().SetTitleSize(0.06)
#     hist1.GetXaxis().SetTitleOffset(0.9)
#     hist1.GetXaxis().SetLabelSize(0.045)
#     hist1.GetYaxis().SetLabelSize(0.045)
#     hist1.GetYaxis().SetRangeUser(0,hist1.GetMaximum()*1.08)
#     legend = TLegend(0.90,0.60,0.55,0.80)
#     legend.AddEntry(hist1,"#tau#tau", 'l')
#     legend.AddEntry(hist2,"lepton + #tau_{h} (visible)", 'l')
#     legend.SetTextSize(0.045)
#     legend.SetBorderSize(0)
#     legend.SetFillStyle(0)
#     legend.Draw()
#     gStyle.SetOptStat(0)
#     canvas.SaveAs("plots_check/pt_tt.png")
#     canvas.Close()
#     file.Close()