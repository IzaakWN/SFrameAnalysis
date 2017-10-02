import sys
sys.path.append('../plots')
import CMS_lumi, tdrstyle
import ROOT
from ROOT import TFile, TH1F, TH2F, kRed, kBlue, THStack, TCanvas, TLegend, kAzure, kRed, kYellow, kOrange, gPad, gROOT, gStyle
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

DIR = "/shome/ineuteli/analysis/SFrameAnalysis/AnalysisOutput/"
mylabel = "_ICHEP"

# CMS style
lumi = 12.9 #24.5
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize  = 0.65
CMS_lumi.lumiTextSize = 0.60
CMS_lumi.relPosX = 0.105
CMS_lumi.outOfFrame = True
CMS_lumi.lumi_13TeV = "%s fb^{-1}" % lumi
tdrstyle.setTDRStyle()




def simplePlot():
    print ">>>\n>>> simplePlot()"
    
    file1_DY = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1.root" )
    file1_WJ = TFile( DIR + "WJ/TauTauAnalysis.WJetsToLNu_TuneCUETP8M1.root" )
    N_tot_DY = file1_DY.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
    N_tot_WJ = file1_WJ.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
    N_DY = file1_DY.Get("histogram_mutau/cutflow_mutau").GetBinContent(6)
    N_WJ = file1_WJ.Get("histogram_mutau/cutflow_mutau").GetBinContent(6)

    file2_DY = TFile( DIR + "DY/DYJetsToLL_M-50_TuneCUETP8M1_mutau.root" )
    file2_WJ = TFile( DIR + "WJ/WJetsToLNu_TuneCUETP8M1_mutau.root" )
    tree_DY = file2_DY.Get("tree")
    tree_WJ = file2_WJ.Get("tree")

    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_and_data_samples
    lumi     = 24.5
    sigma_DY = 5765.4
    sigma_WJ = 61526.7
    scale_DY = lumi * sigma_DY * 1000 / N_tot_DY
    scale_WJ = lumi * sigma_WJ * 1000 / N_tot_WJ
    
    print
    print ">>> "
    print ">>>     %15s %15s %15s %15s" % ( "cutflow N_1", "cutflow N_2", "tree N", "scale" )
    print ">>> DY: %15i %15i %15i %15.5g" % ( N_tot_DY, N_DY, tree_DY.GetEntries(), scale_DY )
    print ">>> WJ: %15i %15i %15i %15.5g" % ( N_tot_WJ, N_WJ, tree_WJ.GetEntries(), scale_WJ )
    print ">>> "

    h1 = TH1F("h1","h1",50,0,50)
    h2 = TH1F("h2","h2",50,0,50)
    tree_DY.Draw("npv >> h1","weight","goff")
    tree_WJ.Draw("npv >> h2","weight","goff")
    #tree_DY.Draw("npv >> h1")
    #tree_WJ.Draw("npv >> h2")
    h1.Scale(scale_DY)
    h2.Scale(scale_WJ)

    h1.SetFillColor(kRed)
    h2.SetFillColor(kBlue)

    stack = THStack("stack","stack")
    stack.Add(h1)
    stack.Add(h2)
    stack.Draw('hist')

    wait = raw_input("Press enter to continue")
    print





def numbers():
    print ">>>\n>>> numbers()"

    ROOT.gROOT.SetBatch(ROOT.kTRUE)
    lumi  = 24.5
    DIR = "/shome/ineuteli/analysis/SFrameAnalysis/AnalysisOutput/"
    samplesB = [
#                     ("TT/", "TT_TuneCUETP8M1",                      "ttbar",              831.76  ),
                    ("DY/", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell-Yan 10-50",  18610.0   ),
#                     ("DY/", "DYJetsToLL_M-50_TuneCUETP8M1",         "Drell-Yan 50",      5765.4   ),
#                     ("WJ/", "WJetsToLNu_TuneCUETP8M1",              "WJ",               61526.7   ),
#                     ("WZ/", "WZ_TuneCUETP8M1",                      "WZ",                  39.9   ), # wrong cross section 
#                     ("ZZ/", "ZZ_TuneCUETP8M1",                      "ZZ",                  10.32  ), # wrong cross section 
               ]


    print "\n>>> integrated luminosity L = %s pb" % lumi
    print ">>> "
    print ">>>    %15s %12s %12s %12s %12s %12s %12s" % ( " ", "cutflow N_1", "cutflow N_6", "tree N", "hist N", "sigma [pb]", "scale" )
    for s, i in zip(samplesB,range(len(samplesB))):

        file1 = TFile( DIR + s[0] + "TauTauAnalysis.%s.root" % s[1] )
        N_1 = file1.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
        N_6 = file1.Get("histogram_mutau/cutflow_mutau").GetBinContent(6)
    
#         file2 = TFile( DIR + s[0] + "%s_mutau.root" % s[1] )
        tree  = file1.Get("tree_mutau")
    
        hist = TH1F("hist","hist",40,-20,20)
        tree.Draw("weight >> hist","( channel == 1 )*weight","goff")
        
        scale = lumi * s[3] * 1000 / N_1
        print ">>>    %-15s %12i %12i %12i %12i %12.5g %12.5g" % ( s[2], N_1, N_6, tree.GetEntries(), hist.Integral(), s[3], scale )





def signalEfficiency():
    print ">>>\n>>> signalEfficiency()"

    # bin 1: no cuts
    # bin 2: JSON / gen weight
    # bin 3: triggers
    # bin 4: MET filters
    # bin 5: lepton selection
    # bin 6: lepton-tau pair selection
    # bin 7: no cuts gen weighted
    
    cuts = [    "no cuts",
                "JSON/weight",
                "triggers",
                "MET filters",
                "lepton",
                "lepton-tau",
                "no cuts (weighted)",
            ]
    
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    efficiencies = [ ]
    for i, cut in zip(range(1,len(cuts)+1),cuts):
        N = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i)
        N_tot = 0
        if i is 1:
            N = 1
            N_tot = 1
        else:
            N_tot = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(i-1)
            
        if N and N_tot:
            efficiencies.append(( cut, N / N_tot ))
        else:
            print ">>> Warning: GetBinContent(%i) = %s, GetBinContent(%i) = %s " % (i,N,i-1,N_tot)
    
    for cut, efficiency in efficiencies:
        print ">>> %s: %5.2f%%" % (cut,efficiency*100)





def ptSignalAcceptence():
    print ">>>\n>>> ptSignalAcceptence()"

    cut = 23. 
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    pt_taus = file.Get("checks/pt_gentaus")
    pt_tau1 = file.Get("checks/pt_gentau1")
    pt_tau2 = file.Get("checks/pt_gentau2")
    pt_muon = file.Get("checks/pt_genmuon")
    
    bincut_taus = pt_taus.FindBin(cut)
    bincut_tau1 = pt_tau1.FindBin(cut)
    bincut_tau2 = pt_tau2.FindBin(cut)
    bincut_muon = pt_muon.FindBin(cut)
    N_taus = pt_taus.Integral()
    N_tau1 = pt_tau1.Integral()
    N_tau2 = pt_tau2.Integral()
    N_muon = pt_muon.Integral()
    
    eff_taus = pt_taus.Integral(bincut_taus, pt_taus.GetNbinsX()) / N_taus
    eff_tau1 = pt_tau1.Integral(bincut_tau1, pt_tau1.GetNbinsX()) / N_tau1
    eff_tau2 = pt_tau2.Integral(bincut_tau2, pt_tau2.GetNbinsX()) / N_tau2
    eff_muon = pt_muon.Integral(bincut_muon, pt_muon.GetNbinsX()) / N_muon
    
    print ">>> efficiency of pt cut of %s on signal's gen tau and reco muon:" % cut
    print ">>> gen tau:  %5.2f%%" % (100*eff_taus)
    print ">>> gen tau1: %5.2f%%" % (100*eff_tau1)
    print ">>> gen tau2: %5.2f%%" % (100*eff_tau2)
    print ">>> gen muon: %5.2f%%" % (100*eff_muon)

    print ">>> check: bincut_taus = %3i,  N_taus =%7i" % (bincut_taus,N_taus)
    print ">>> check: bincut_tau2 = %3i,  N_tau1 =%7i" % (bincut_tau1,N_tau1)
    print ">>> check: bincut_tau3 = %3i,  N_tau2 =%7i" % (bincut_tau2,N_tau2)
    print ">>> check: bincut_muon = %3i,  N_muon =%7i" % (bincut_muon,N_muon)
    
    # DRAW
    canvas = TCanvas("canvas","canvas",100,100,800,600) # 600,600
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.12)
    canvas.SetTopMargin(0.05)
    pt_taus.SetLineWidth(3)
    pt_muon.SetLineWidth(3)
    pt_taus.SetLineColor(kAzure+4)
    pt_muon.SetLineColor(kRed+3)
    pt_taus.Scale(1/N_taus)
    pt_muon.Scale(1/N_muon/3)
    #pt_taus.Rebin(2)
    #pt_muon.Rebin(2)
    pt_taus.Draw("hist")
    pt_muon.Draw("histsame")
    pt_taus.SetTitle("")
    pt_taus.GetXaxis().SetRangeUser(0,100)
    pt_taus.GetXaxis().SetTitle("p_{T} of generator level particle")
    pt_taus.GetYaxis().SetTitle("A.U.")
    #pt_taus.GetYaxis().SetTitleSize(0)
    pt_taus.GetXaxis().SetTitleSize(0.05)
    pt_taus.GetYaxis().SetTitleSize(0.05)
    pt_taus.GetXaxis().SetTitleOffset(1.14)
    pt_taus.GetYaxis().SetTitleOffset(1.17)
    pt_taus.GetXaxis().SetLabelSize(0.045)
    pt_taus.GetYaxis().SetLabelSize(0.040)
    #pt_taus.GetYaxis().SetLabelSize(0)    
    legend = TLegend(0.56,0.68,0.80,0.84)
    legend.AddEntry(pt_taus, " gen #tau", 'l')
    legend.AddEntry(pt_muon, " gen #mu from #tau", 'l')
    legend.SetTextSize(0.055)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    #gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/pt.png")
    canvas.Close()
    
    

    
def DYAcceptence():
    print ">>>\n>>> DYAcceptence()"

    DIR2 = "/shome/ineuteli/analysis/SFrameAnalysis/TauTauResonances/"

#     file = TFile( DIR2 + "TauTauAnalysis.DYJets_M-10to50.UZH.root" )
    file = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-10to50_TuneCUETP8M1%s.root" % mylabel )
    pt = file.Get("checks/pt_muon")
    d0 = file.Get("checks/d0_muon")
    dz = file.Get("checks/dz_muon")
    d0_cut = file.Get("checks/d0_muon_cut")
    dz_cut = file.Get("checks/dz_muon_cut")
#     file2 = TFile( DIR2 + "TauTauAnalysis.DYJets_M-50.UZH.root" )
    file2 = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1%s.root" % mylabel )
    pt2 = file2.Get("checks/pt_muon")
    d02 = file2.Get("checks/d0_muon")
    dz2 = file2.Get("checks/dz_muon")
    d02_cut = file2.Get("checks/d0_muon_cut")
    dz2_cut = file2.Get("checks/dz_muon_cut")
    var_dict = { "pt_muon":"muon p_{T}", "d0_muon":"muon d0", "dz_muon":"muon |dz|",
                 "d0_muon_cut":"muon d0", "dz_muon_cut":"muon |dz|" }
    
    print ">>>\n>>> overflow DY check"
    print ">>> DY M-10to50 pt overflow:              %9i /%9i = %5.1f%%" % ( pt.GetBinContent(pt.GetNbinsX()+1),   pt.GetEntries(),  pt.GetBinContent(pt.GetNbinsX()+1)   /  pt.GetEntries()*100 )
    print ">>> DY M-50     pt overflow:              %9i /%9i = %5.1f%%" % ( pt2.GetBinContent(pt2.GetNbinsX()+1), pt2.GetEntries(), pt2.GetBinContent(pt2.GetNbinsX()+1) / pt2.GetEntries()*100 )
    print ">>> DY M-10to50 d0 overflow:              %9i /%9i = %5.1f%%" % ( d0.GetBinContent(d0.GetNbinsX()+1),   d0.GetEntries(),  d0.GetBinContent(d0.GetNbinsX()+1)   / d0.GetEntries()*100  )
    print ">>> DY M-50     d0 overflow:              %9i /%9i = %5.1f%%" % ( d02.GetBinContent(d02.GetNbinsX()+1), d02.GetEntries(), d02.GetBinContent(d02.GetNbinsX()+1) / d02.GetEntries()*100 )
    print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d0_cut.GetBinContent(d0_cut.GetNbinsX()+1),   d0_cut.GetEntries(),  d0_cut.GetBinContent(d0_cut.GetNbinsX()+1)   / d0_cut.GetEntries()*100  )
    print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( d02_cut.GetBinContent(d02_cut.GetNbinsX()+1), d02_cut.GetEntries(), d02_cut.GetBinContent(d02_cut.GetNbinsX()+1) / d02_cut.GetEntries()*100 )
    print ">>> DY M-10to50 dz overflow:              %9i /%9i = %5.1f%%" % ( dz.GetBinContent(dz.GetNbinsX()+1),   dz.GetEntries(),  dz.GetBinContent(dz.GetNbinsX()+1)   / dz.GetEntries()*100  )
    print ">>> DY M-50     dz overflow:              %9i /%9i = %5.1f%%" % ( dz2.GetBinContent(dz2.GetNbinsX()+1), dz2.GetEntries(), dz2.GetBinContent(dz2.GetNbinsX()+1) / dz2.GetEntries()*100 )
    print ">>> DY M-10to50 d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz_cut.GetBinContent(dz_cut.GetNbinsX()+1),   dz_cut.GetEntries(),  dz_cut.GetBinContent(dz_cut.GetNbinsX()+1)   / dz_cut.GetEntries()*100  )
    print ">>> DY M-50     d0 overflow after pT cut: %9i /%9i = %5.1f%%" % ( dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1), dz2_cut.GetEntries(), dz2_cut.GetBinContent(dz2_cut.GetNbinsX()+1) / dz2_cut.GetEntries()*100 )
    
    for var, hist, hist2 in [ ("pt_muon",pt,pt2), ("d0_muon",d0,d02), ("dz_muon",dz,dz2), ("d0_muon_cut",d0_cut,d02_cut), ("dz_muon_cut",dz_cut,dz2_cut) ]:
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.05)
        canvas.SetLeftMargin(0.05)
        canvas.SetTopMargin(0.05)
        hist.SetLineWidth(3)
        hist.SetLineStyle(1)
        hist.SetLineColor(kAzure+4)
        hist2.SetLineWidth(3)
        hist2.SetLineStyle(7)
        hist2.SetLineColor(kRed+3)
        hist.Draw("hist")
        hist2.Draw("histsame")
        hist.Scale(1/hist.Integral())
        hist2.Scale(1/hist2.Integral())
        hist.SetTitle("")
        #hist.GetXaxis().SetRangeUser(0,100)
        hist.GetXaxis().SetTitle(var_dict[var]) #replace
        hist.GetYaxis().SetTitleSize(0)
        hist.GetXaxis().SetTitleSize(0.05)
        hist.GetXaxis().SetTitleOffset(1.15)
        hist.GetXaxis().SetLabelSize(0.045)
        hist.GetYaxis().SetLabelSize(0)
        hist.GetYaxis().SetRangeUser(0,max(hist.GetMaximum(),hist2.GetMaximum())*1.12)
        h = 0.18
        w = 0.25
        legend = TLegend(0.64,0.7,0.64-w,0.7-h)
        legend.AddEntry(hist, " DY 10 < m < 50", 'l')
        legend.AddEntry(hist2," DY 50 > m", 'l')
        legend.SetTextSize(0.042)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.Draw()
        gStyle.SetOptStat(0)
        canvas.SaveAs("plots_check/%s.png" % var)
        canvas.Close()
        
    vetos   = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
    isocuts = "iso_1 < 0.15 && iso_2 == 1"
    cuts    = [ ("SS",         "channel==1 && q_1*q_2<0"),
                ("iso",        "channel==1 && %s && q_1*q_2<0" % (isocuts)),
                #("isow",       "(channel==1 && %s && q_1*q_2<0)*idisoweight_1*trigweight_1" % (isocuts)),
                ("vetos",      "channel==1 && %s && %s && q_1*q_2<0" % (isocuts, vetos)),
                ("category 1", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets == 1 && nfjets  > 0" % (isocuts, vetos)),
                ("category 2", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets  > 1 && nfjets == 0 && dphi_ll_bj > 2 && met < 60" % (isocuts, vetos)),
               ]
    # TODO weights?
    #  trigweight_1 * idisoweight_1 * trigweight_2 * idisoweight_2
    
    tree  = file.Get("tree_mutau")
    tree2 = file2.Get("tree_mutau")
    iso_1  = TH1F("iso_1", "iso_1", 100, -10, 10)
    iso_12 = TH1F("iso_12", "iso_12", 100, -10, 10)
    tree.Draw( "iso_1 >> iso_1",   "channel==1", "gOff")
    tree2.Draw("iso_1 >> iso_12",  "channel==1", "gOff")
    N_tot = iso_1.Integral()
    N_tot2 = iso_12.Integral()

    print ">>>\n>>> cuts on DY:"
    for label, cut in cuts: 
        iso_1.Reset()
        iso_12.Reset()
        tree.Draw("iso_1 >> iso_1",   cut, "gOff")
        tree2.Draw("iso_1 >> iso_12", cut, "gOff")
        N  = iso_1.Integral() #GetEntries
        N2 = iso_12.Integral()
        print ">>> %s:" % label
        if N_tot:  print ">>>   DY M-10to50: %4.1f%% (%6i,%6i)" % ( N/N_tot*100.0,   N,  N_tot  )
        if N_tot2: print ">>>   DY M-50:     %4.1f%% (%6i,%6i)" % ( N2/N_tot2*100.0, N2, N_tot2 )
        if "category" not in label and "isow" not in label:
            N_tot  = N
            N_tot2 = N2
        
    file.Close()
    file2.Close()
    
    
    
    
    
    
def deltaR():
    print ">>>\n>>> deltaR()"
    
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    DeltaR_tautau  = file.Get("checks/DeltaR_tautau")
    DeltaR_taumu   = file.Get("checks/DeltaR_taumu")
    
    fileH = TFile( DIR + "gen_plots/root_files/HTT.root" )
    treeH = fileH.Get("Events")
    DeltaR_Htautau = TH1F("DeltaR_Htautau", "DeltaR_Htautau", 100, 0, 4)
    treeH.Draw("dR_ll >> DeltaR_Htautau")
    
    cut = 0.5
    bincut_tautau = DeltaR_tautau.FindBin(cut)
    bincut_taumu  = DeltaR_taumu.FindBin(cut)
    N_tautau = DeltaR_tautau.Integral()
    N_taumu  = DeltaR_taumu.Integral()
    eff_tautau = DeltaR_tautau.Integral(bincut_tautau, DeltaR_tautau.GetNbinsX()) / N_tautau
    eff_taumu  = DeltaR_taumu.Integral( bincut_taumu,  DeltaR_taumu.GetNbinsX())  / N_taumu
    print ">>> efficiency of DeltaR cut of %s on signal's gen tau and reco muon:" % cut
    print ">>> gen tautau:  %5.2f%%" % (100*eff_tautau)
    print ">>> gen taumu:   %5.2f%%" % (100*eff_taumu)
    print ">>> check: bincut_tautau = %3i,  N_tautau =%7i" % (bincut_tautau, N_tautau)
    print ">>> check: bincut_taumu  = %3i,  N_taumu  =%7i" % (bincut_taumu,  N_taumu)
    
#     for DR, hist in [ ("DeltaR_tautau",DeltaR_tautau), ("DeltaR_taumu",DeltaR_taumu) ]:
#         canvas = TCanvas("canvas","canvas",100,100,800,600)
#         canvas.SetBottomMargin(0.12)
#         canvas.SetRightMargin(0.05)
#         canvas.SetLeftMargin(0.05)
#         canvas.SetTopMargin(0.05)
#         hist.SetLineWidth(3)
#         hist.SetLineColor(kAzure+4)
#         hist.Draw("hist")
#         hist.Scale(1/hist.Integral())
#         hist.SetTitle("")
#         #hist.GetXaxis().SetRangeUser(0,100)
#         hist.GetXaxis().SetTitle(DR.replace("Delta","#Delta ").replace("_tautau","_{#tau#tau}").replace("_taumu","_{#tau#mu}"))
#         hist.GetYaxis().SetTitleSize(0)
#         hist.GetXaxis().SetTitleSize(0.05)
#         hist.GetXaxis().SetTitleOffset(1.15)
#         hist.GetXaxis().SetLabelSize(0.045)
#         hist.GetYaxis().SetLabelSize(0)
#         gStyle.SetOptStat(0)
#         canvas.SaveAs("plots_check/%s.png" % DR)
#         canvas.Close()
        
    canvas = TCanvas("canvas","canvas",100,100,800,600)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.12)
    canvas.SetTopMargin(0.05)
    DeltaR_tautau.SetLineWidth(3)
    DeltaR_tautau.SetLineStyle(1)
    DeltaR_tautau.SetLineColor(kAzure+4)
    DeltaR_taumu.SetLineWidth(3)
    DeltaR_taumu.SetLineStyle(7)
    DeltaR_taumu.SetLineColor(kRed+3)
    DeltaR_Htautau.SetLineWidth(3)
    DeltaR_Htautau.SetLineStyle(1)
    DeltaR_Htautau.SetLineColor(kOrange) #kYellow
    DeltaR_tautau.Draw(  "hist")
    DeltaR_Htautau.Draw( "histsame")
    DeltaR_tautau.Draw(  "histsame")
    DeltaR_taumu.Draw(   "histsame")
    DeltaR_tautau.Scale(  1/DeltaR_tautau.GetMaximum()) # Integral
    DeltaR_taumu.Scale(   1/DeltaR_taumu.GetMaximum())
    DeltaR_Htautau.Scale( 1/DeltaR_Htautau.GetMaximum())
    DeltaR_tautau.SetTitle("")
    DeltaR_tautau.GetXaxis().SetRangeUser(0,4)
    DeltaR_tautau.GetXaxis().SetTitle("#DeltaR")
    DeltaR_tautau.GetYaxis().SetTitle("A.U.")
    DeltaR_tautau.GetXaxis().SetTitleSize(0.06)
    DeltaR_tautau.GetYaxis().SetTitleSize(0.06)
    DeltaR_tautau.GetXaxis().SetTitleOffset(0.9)
    DeltaR_tautau.GetXaxis().SetLabelSize(0.045)
    DeltaR_tautau.GetYaxis().SetLabelSize(0.045)
    DeltaR_tautau.GetYaxis().SetRangeUser(0,DeltaR_tautau.GetMaximum()*1.12)
    h = 0.18
    w = 0.25
    legend = TLegend(0.61,0.75,0.61-w,0.75-h)
    legend.AddEntry(DeltaR_tautau,  " signal X #rightarrow #tau#tau", 'l')
    legend.AddEntry(DeltaR_taumu,   " signal X #rightarrow #tau#tau #rightarrow #mu#tau_{h}", 'l')
    legend.AddEntry(DeltaR_Htautau, " SM Higgs #rightarrow #tau#tau", 'l')
    legend.SetTextSize(0.042)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/DeltaR.png")
    canvas.Close()
    file.Close()
    fileH.Close()
    

    # MASS
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    M_tautau  = file.Get("checks/M_tautau")
    
    canvas = TCanvas("canvas","canvas",100,100,800,600)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.12)
    canvas.SetTopMargin(0.05)
    M_tautau.SetLineWidth(3)
    M_tautau.SetLineStyle(1)
    M_tautau.SetLineColor(kAzure+4)
    M_tautau.Draw("hist")
    M_tautau.Scale(1/M_tautau.GetMaximum()) # Integral
    M_tautau.SetTitle("")
    M_tautau.GetXaxis().SetTitle("M_{#tau#tau}")
    M_tautau.GetYaxis().SetTitle("A.U.")
    M_tautau.GetXaxis().SetTitleSize(0.06)
    M_tautau.GetYaxis().SetTitleSize(0.06)
    M_tautau.GetXaxis().SetTitleOffset(0.9)
    M_tautau.GetXaxis().SetLabelSize(0.045)
    M_tautau.GetYaxis().SetLabelSize(0.045)
    M_tautau.GetYaxis().SetRangeUser(0,M_tautau.GetMaximum()*1.12)
    h = 0.18
    w = 0.25
    legend = TLegend(0.85,0.75,0.85-w,0.75-h)
    legend.AddEntry(M_tautau, " signal X #rightarrow #tau#tau", 'l')
    legend.SetTextSize(0.042)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/M_tautau.png")
    canvas.Close()
    file.Close()
    fileH.Close()
    
    
    
    
    
    
    
    
    
def deltaR2():
    print ">>>\n>>> deltaR2()"
    
    #DIRT = "/shome/ineuteli/analysis/SFrameAnalysis/TauTauResonances/"
    #file = TFile( DIRT + "TauTauAnalysis.Signal.UZH.root" )
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    DeltaR1 = file.Get("checks/DeltaR_gentau_recotau_std")
    DeltaR2 = file.Get("checks/DeltaR_gentau_recotau_bst")
        
    cut = 0.2
    bincut1 = DeltaR1.FindBin(cut)
    bincut2 = DeltaR2.FindBin(cut)
    N1 = DeltaR1.Integral()
    N2 = DeltaR2.Integral()
    eff1 = DeltaR1.Integral(1, bincut1) / N1
    eff2 = DeltaR2.Integral(1, bincut2) / N2
    print ">>> percentage of gen-reco tau pairs with DeltaR < %s:" % cut
    print ">>> standard tau ID:  %5.2f%%" % (100*eff1)
    print ">>> boosted tau ID:   %5.2f%%" % (100*eff2)
    print ">>> check: bincut1 = %2i, N1 =%8i" % (bincut1, N1)
    print ">>> check: bincut2 = %2i, N2 =%8i" % (bincut2, N2)
    print ">>> check: edges bin1 = [%3.2f, %3.2f]" % (DeltaR1.GetBinLowEdge(bincut1), DeltaR1.GetBinLowEdge(bincut1)+DeltaR1.GetBinWidth(bincut1))
    print ">>> check: edges bin2 = [%3.2f, %3.2f]" % (DeltaR2.GetBinLowEdge(bincut2), DeltaR2.GetBinLowEdge(bincut2)+DeltaR2.GetBinWidth(bincut2))

        
    canvas = TCanvas("canvas","canvas",100,100,800,600)
    canvas.SetBottomMargin(0.14)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.12)
    canvas.SetTopMargin(0.05)
    DeltaR1.SetLineWidth(3)
    DeltaR1.SetLineStyle(1)
    DeltaR1.SetLineColor(kAzure+4)
    DeltaR2.SetLineWidth(3)
    DeltaR2.SetLineStyle(7)
    DeltaR2.SetLineColor(kRed+3)
    DeltaR1.Draw("hist")
    DeltaR2.Draw("histsame")
    DeltaR1.Scale(1/DeltaR1.Integral()) # Integral / GetMaximum
    DeltaR2.Scale(1/DeltaR2.Integral())
    DeltaR1.SetTitle("")
    DeltaR1.GetXaxis().SetRangeUser(0,4)
    DeltaR1.GetXaxis().SetTitle("#DeltaR( #tau^{gen}_{h}, #tau^{reco}_{h})")
    DeltaR1.GetYaxis().SetTitle("A.U.")
    DeltaR1.GetXaxis().SetTitleSize(0.06)
    DeltaR1.GetYaxis().SetTitleSize(0.06)
    DeltaR1.GetXaxis().SetTitleOffset(0.85)
    DeltaR1.GetXaxis().SetLabelSize(0.045)
    DeltaR1.GetYaxis().SetLabelSize(0.045)
    DeltaR1.GetYaxis().SetRangeUser(0,DeltaR1.GetMaximum()*1.12)
    h = 0.18
    w = 0.25
    legend = TLegend(0.61,0.75,0.61-w,0.75-h)
    legend.AddEntry(DeltaR1, " standard tau ID", 'l')
    legend.AddEntry(DeltaR2, " boosted tau ID", 'l')
    legend.SetTextSize(0.042)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/DeltaR_genrecotau.png")
    canvas.Close()
    file.Close()
    
    
    
    
    
def Delta_eta_phi():
    print ">>>\n>>> Delta_eta_phi()"

    CMS_lumi.cmsTextSize = 0.50
    CMS_lumi.lumiTextSize = 0.45
    CMS_lumi.relPosX = 0.115
    gStyle.SetPalette(1) # for rainbow colors

    for sample in ["HTT", "LowMassDiTau"]:

        fileH = TFile( DIR + "gen_plots/root_files/%s.root" % sample )
        treeH = fileH.Get("Events")
        Delta_eta_phi = TH2F("Delta_eta_phi", "Delta_eta_phi", 100, 0, 3.2, 100, 0, 3.2)
        treeH.Draw("abs(dphi_ll):abs(deta_ll) >> Delta_eta_phi") #abs(deta):abs(dphi) #deta:dphi
    
        canvas = TCanvas("canvas","canvas",100,100,800,800)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.12)
        canvas.SetLeftMargin(0.12)
        canvas.SetTopMargin(0.05)
        Delta_eta_phi.SetTitle("")
        Delta_eta_phi.Draw("colz")
        canvas.SaveAs("plots_check/Delta_eta_phi_%s.png" % sample)
        CMS_lumi.CMS_lumi(canvas,14,0)
        canvas.Close()
        fileH.Close()

    
    
    
    
    
def eta():
    print ">>>\n>>> eta()"
    
    fileH = TFile( DIR + "gen_plots/root_files/LowMassDiTau.root" )
    treeH = fileH.Get("Events")
    eta_l = TH1F("eta_l", "eta_l", 100, -5.5, 5.5)
    eta_b = TH1F("eta_b", "eta_b", 100, -5.5, 5.5)
    treeH.Draw("jeteta_l >> eta_l") #abs(jeteta_l)
    treeH.Draw("jeteta_b >> eta_b") #abs(jeteta_b)
        
    canvas = TCanvas("canvas","canvas",100,100,800,600)
    canvas.SetBottomMargin(0.12)
    canvas.SetRightMargin(0.05)
    canvas.SetLeftMargin(0.12)
    canvas.SetTopMargin(0.05)
    eta_l.SetLineWidth(3)
    eta_l.SetLineStyle(1)
    eta_l.SetLineColor(kAzure+4)
    eta_b.SetLineWidth(3)
    eta_b.SetLineStyle(2)
    eta_b.SetLineColor(kRed+3)
    eta_l.Draw("hist")
    eta_b.Draw("histsame")
    eta_l.Scale(1/eta_l.GetMaximum())
    eta_b.Scale(1/eta_b.GetMaximum())
    eta_l.SetTitle("")
    #eta_l.GetXaxis().SetRangeUser(0,5)
    eta_l.GetXaxis().SetTitle("quark #eta") #|#eta|
    eta_l.GetYaxis().SetTitle("A.U.")
    eta_l.GetXaxis().SetTitleSize(0.06)
    eta_l.GetYaxis().SetTitleSize(0.06)
    eta_l.GetXaxis().SetTitleOffset(0.9)
    eta_l.GetXaxis().SetLabelSize(0.045)
    eta_l.GetYaxis().SetLabelSize(0.045)
    eta_l.GetYaxis().SetRangeUser(0,eta_l.GetMaximum()*1.08)
    h = 0.12
    #legend = TLegend(0.8,0.65,0.52,0.45)
    legend = TLegend(0.8,0.35,0.42,0.35-h)
    legend.AddEntry(eta_l," light quark", 'l')
    legend.AddEntry(eta_b," b quark", 'l')
    legend.SetTextSize(0.045)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/eta.png")
    canvas.Close()
    fileH.Close()
    
    
    
def checkStackIntegral():
    print ">>>\n>>> checkStackIntegral"

    file_DY = TFile( DIR + "DY/TauTauAnalysis.DYJetsToLL_M-50_TuneCUETP8M1%s.root" % mylabel )
    file_WJ = TFile( DIR + "WJ/TauTauAnalysis.WJetsToLNu_TuneCUETP8M1%s.root" % mylabel )
    tree_DY = file_DY.Get("tree_mutau")
    tree_WJ = file_WJ.Get("tree_mutau")

    h1 = TH1F("h1","h1",100,0,70)
    h2 = TH1F("h2","h2",100,0,70)
    tree_DY.Draw("m_vis >> h1","weight","goff")
    tree_WJ.Draw("m_vis >> h2","weight","goff")

    stack = THStack("stack","stack")
    stack.Add(h1)
    stack.Add(h2)
    #stack.Draw()
    print ">>> hist  integral = %11.2f" % (h1.Integral())
    print ">>> stack integral = %11.2f" % (stack.GetStack().Last().Integral())
    h1.Scale(5)
    print ">>> hist  integral = %11.2f" % (h1.Integral())
    print ">>> stack integral = %11.2f" % (stack.GetStack().Last().Integral())
    #stack.Draw()
    
    
    
def countEvent():
    print ">>>\n>>> countEvent()"

    vetos   = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
    isocuts = "iso_1 < 0.15 && iso_2 == 1"
    cuts    = [ ("category 1", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets == 1 && nfjets  > 0" % (isocuts, vetos)),
                ("category 2", "channel==1 && %s && %s && q_1*q_2<0 && ncbtag > 0 && ncjets  > 1 && nfjets == 0 && dphi_ll_bj > 2 && met < 50" % (isocuts, vetos)),
               ]

    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )    
    tree = file.Get("tree_mutau")
    
    for label, cut in cuts:
        hist = TH1F("hist", "hist", 35, 0, 70)
        canvas = TCanvas("canvas","canvas",100,100,400,300)
        tree.Draw("m_vis >> hist", cut)
        print ">>> %s: signal MC sample has %3i events" % (label,hist.Integral())
        canvas.SaveAs("plots_check/%s.png" % label.replace(" ","_"))
        ROOT.gDirectory.Delete(hist.GetName())
        canvas.Close()
        
    
    
def DeltaR_vs_pt_tt():
    print ">>>\n>>> DeltaR_vs_pt_tt"
    
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    hist = file.Get("checks/DeltaR_pt_tt_vis_ltau")
    prof = hist.ProfileX()
    
    canvas = TCanvas("canvas","canvas",100,100,800,800)
    canvas.SetBottomMargin(0.10)
    canvas.SetRightMargin(0.12)
    canvas.SetLeftMargin(0.10)
    canvas.SetTopMargin(0.05)
    hist.SetTitle("")
    hist.Draw("colz")
    prof.Draw("same")
    prof.SetLineWidth(3)
    prof.SetLineStyle(1)
    prof.SetLineColor(kRed+3)
    hist.GetXaxis().SetTitleOffset(1.2)
    hist.GetYaxis().SetTitleOffset(1.1)
    hist.GetXaxis().SetTitle("generator level p_{T}^{l#tau_{h}}")
    hist.GetYaxis().SetTitle("generator level #DeltaR_{l#tau_{h}}")
    legend = TLegend(0.90,0.75,0.50,0.90)
    legend.AddEntry(prof,"average #DeltaR", 'l')
    legend.SetTextSize(0.045)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    canvas.SaveAs("plots_check/DeltaR_pt_tt_vis_ltau.png")
    CMS_lumi.CMS_lumi(canvas,14,0)
    canvas.Close()
    file.Close()

    
    
    
    
def pt_tt():
    print ">>>\n>>> pt_tt()"
    
    file = TFile( DIR + "signal/TauTauAnalysis.LowMass_30GeV_DiTauResonance%s.root" % mylabel )
    hist1 = file.Get("checks/pt_tt_gen")
    hist2 = file.Get("checks/pt_tt_vis_ltau")
        
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
    hist1.Scale(1/hist1.GetMaximum())
    hist2.Scale(1/hist2.GetMaximum())
    hist1.SetTitle("")
    #hist1.GetXaxis().SetRangeUser(0,5)
    hist1.GetXaxis().SetTitle("generator level p_{T}^{#tau#tau}")
    hist1.GetYaxis().SetTitle("A.U.")
    hist1.GetXaxis().SetTitleSize(0.06)
    hist1.GetYaxis().SetTitleSize(0.06)
    hist1.GetXaxis().SetTitleOffset(0.9)
    hist1.GetXaxis().SetLabelSize(0.045)
    hist1.GetYaxis().SetLabelSize(0.045)
    hist1.GetYaxis().SetRangeUser(0,hist1.GetMaximum()*1.08)
    legend = TLegend(0.90,0.60,0.55,0.80)
    legend.AddEntry(hist1,"#tau#tau", 'l')
    legend.AddEntry(hist2,"lepton + #tau_{h} (visible)", 'l')
    legend.SetTextSize(0.045)
    legend.SetBorderSize(0)
    legend.SetFillStyle(0)
    legend.Draw()
    gStyle.SetOptStat(0)
    canvas.SaveAs("plots_check/pt_tt.png")
    canvas.Close()
    file.Close()
        
        
        
        
def main():
    print ""
        
    #simplePlot()
    #numbers()
    #signalEfficiency()
    #DYAcceptence()
    ptSignalAcceptence()
    #deltaR()
    #deltaR2()
    #Delta_eta_phi()
    #eta()
    #countEvent()
    DeltaR_vs_pt_tt()
    pt_tt()
    #checkStackIntegral()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()


