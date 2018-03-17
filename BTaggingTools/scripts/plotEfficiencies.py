#! /usr/bin/env python

import os, sys
#sys.path.append('../plots')
#import PlotTools.PlotTools
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
import ROOT
from ROOT import TFile, TH1F, TH2F, kRed, kBlue, THStack, TCanvas, TLegend, kAzure, kRed, kYellow, kOrange, gPad, gROOT, gStyle
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

NEW_DIR = "../efficiencies"
OLD_DIR = "../efficiencies"
OUT_DIR = "plot_bTagEffs"

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



def plotEfficiencies2D(filename,prefix,workingpoint,label=""):
    print ">>>\n>>> plotEfficiencies2D - %s" % (filename)
    
    file = TFile(filename,'READ')
    dirname  = "bTagEff"
    histnames = [
        "%s_%s_%s_eff" % (prefix,"udsg",workingpoint),
        "%s_%s_%s_eff" % (prefix,  "b" ,workingpoint),
    ]
    
    for histname in histnames:
        print ">>>   %s" % (histname)
        
        flavor = "b"
        if "udsg" in histname: flavor = "light"
        if "_c_" in histname:  flavor = "c"
        
        range = [0.25,0.70]
        if flavor == "light": range = [0.0,0.10]
        
        hist = file.Get("%s/%s"%(dirname,histname))
        
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.11)
        canvas.SetLeftMargin(0.10)
        canvas.SetTopMargin(0.08)
        hist.Draw("colz")
        hist.SetTitle("")
        hist.GetZaxis().SetRangeUser(*range)
        #hist.GetXaxis().SetRangeUser(0,100)
        #hist.GetYaxis().SetRangeUser(0,200)
        hist.GetXaxis().SetTitle("%s jet p_{T}" % (flavor))
        hist.GetYaxis().SetTitle("%s jet #eta" % (flavor))
        hist.GetYaxis().CenterTitle()
        hist.GetXaxis().SetLabelSize(0.042)
        hist.GetYaxis().SetLabelSize(0.042)
        hist.GetXaxis().SetTitleSize(0.05)
        hist.GetYaxis().SetTitleSize(0.05)
        hist.GetXaxis().SetTitleOffset(1.10)
        hist.GetYaxis().SetTitleOffset(0.99)
        gStyle.SetOptStat(0)
        CMS_lumi.CMS_lumi(canvas,13,0)
        canvas.SaveAs("%s/%s%s.png" % (OUT_DIR,histname,label))
        canvas.Close()
        
    file.Close()




def compareProjectedEfficiencies(filename1,filename2,prefix,workingpoint,**kwargs):
    print ">>>\n>>> compareProjectedEfficiencies"
    print ">>>   %s vs. %s" % (filename1,filename2)
    
    file1 = TFile(filename1,'READ') # old file
    file2 = TFile(filename2,'READ') # new file
    
    label   = kwargs.get('label',"")
    dirname = kwargs.get('dirname',"bTagEff")
    compare = kwargs.get('compare',"")
    
    title1 = "VH #rightarrow #tau#taubb analysis"
    title2 = "X #rightarrow #tau#tau analysis"
    dirname1 = dirname
    dirname2 = dirname
    
    if compare == "mutau-etau":        
        title1 = "#mu#tau"
        title2 = "e#tau"
        dirname1 = "%s_mutau" % (dirname)
        dirname2 = "%s_etau"  % (dirname)
        label+="_mutau-etau"
     
    histnames = [
        "%s_%s_%s_eff" % (prefix,"udsg",workingpoint),
        "%s_%s_%s_eff" % (prefix,  "b" ,workingpoint),
    ]
    
    etabins_dict = {   
        "central": ["|#eta|<1.5",    2,3],
        "forward": ["1.5<|#eta|<2.5",1,4],
    }
    
    for histname in histnames:
      for etarange in ["central", "forward"]:
        print ">>>   %s - %s" % (histname,etarange)
    
        etabins = etabins_dict[etarange]
        flavor = "b"
        if "udsg" in histname: flavor = "light"
        if "_c_"  in histname: flavor = "c"
    
        range = [0.10,0.80]
        legendCoordinates = [0.52,0.72,0.90,0.86]
        if flavor == "light":
            range = [0.0,0.10]
            legendCoordinates = [0.20,0.65,0.60,0.80]
    
        hist1_2D = file1.Get("%s/%s"%(dirname1,histname))
        hist2_2D = file2.Get("%s/%s"%(dirname2,histname)) # old first
        hist1    = None
        hist2    = None
        if etarange == "central":
            hist1    = hist1_2D.ProjectionX("%s_1"%(histname),etabins[1],etabins[2]) # ProfileX
            hist2    = hist2_2D.ProjectionX("%s_2"%(histname),etabins[1],etabins[2])
        else:
            hist1   = hist1_2D.ProjectionX("%s_11"%(histname),1,1) # ProfileX
            hist2   = hist2_2D.ProjectionX("%s_21"%(histname),4,4)
            hist1.Add(hist1_2D.ProjectionX("%s_12"%(histname),1,1))
            hist2.Add(hist2_2D.ProjectionX("%s_22"%(histname),4,4))
        
        hist1.Scale(0.5)
        hist2.Scale(0.5)
        #print ">>>   hist1_2D.GetNbinsY() - %s" % (hist1_2D.GetNbinsY())
        #print ">>>   hist2_2D.GetNbinsY() - %s" % (hist2_2D.GetNbinsY())
    
        canvas = TCanvas("canvas","canvas",100,100,800,600)
        canvas.SetBottomMargin(0.12)
        canvas.SetRightMargin(0.04)
        canvas.SetLeftMargin(0.10)
        canvas.SetTopMargin(0.08)
        hist1.SetLineWidth(3)
        hist1.SetLineStyle(1)
        hist1.SetLineColor(kAzure+4)
        hist2.SetLineWidth(3)
        hist2.SetLineStyle(2)
        hist2.SetLineColor(kRed+3)
        hist1.Draw("histE")
        hist2.Draw("histsameE")
        hist1.SetTitle("")
        hist1.GetXaxis().SetTitle("%s jet p_{T}" % (flavor))
        hist1.GetYaxis().SetTitle("b tagging efficiency of %s jet" % (flavor))
        hist1.GetXaxis().SetLabelSize(0.042)
        hist1.GetYaxis().SetLabelSize(0.040)
        hist1.GetXaxis().SetTitleSize(0.05)
        hist1.GetYaxis().SetTitleSize(0.05)
        hist1.GetXaxis().SetTitleOffset(1.10)
        hist1.GetYaxis().SetTitleOffset(0.99)
        hist1.GetYaxis().SetRangeUser(*range)
        legend = TLegend(*legendCoordinates)
        legend.SetHeader(etabins[0])
        legend.AddEntry(hist1,title1,'l')
        legend.AddEntry(hist2,title2,'l')
        legend.SetTextSize(0.040)
        legend.SetBorderSize(0)
        legend.SetFillStyle(0)
        legend.Draw()
        gStyle.SetOptStat(0)
        CMS_lumi.CMS_lumi(canvas,13,0)
        canvas.SaveAs("%s/%s_vs_pt_%s%s.png" % (OUT_DIR,histname,etarange,label))
        canvas.Close()
        ROOT.gDirectory.Delete(hist1.GetName())
        ROOT.gDirectory.Delete(hist2.GetName())
        
    file1.Close()
    file2.Close()



def histname(prefix,flavor,workingpoint,eff=True,all=False,dirname=""):
    if "light" in flavor: flavor = "udsg"
    name = "%s_%s_%s" % (prefix,flavor,workingpoint)
    if   eff: name += "_eff"
    elif all: name = "%s_%s_all" % (prefix,flavor)
    if dir: name = dir.rstrip("/")+"/"+name
    return name



def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    


def main():
    
    oldfilename = "%s/bTagEffs_36p8_vMediumAk4_LooseAk8_lepVeto.root" % OLD_DIR
    newfilename = "%s/bTagEffs_HTT_baseline.root" % NEW_DIR
    makeDirectory(OUT_DIR)
    
    compareProjectedEfficiencies(oldfilename,newfilename,"jet_ak4","Medium")
    compareProjectedEfficiencies("bTagEffs_mutau.root","bTagEffs_etau.root","jet_ak4","Medium",compare="mutau-etau")
    # for filename, label in [ (oldfilename,"_old"), (newfilename,"_new") ]:
    #     plotEfficiencies2D(filename,"jet_ak4","Medium",label=label)
    
    
    
    
    
if __name__ == '__main__':
    print ""
    main()
    print ">>>\n>>> done\n"


