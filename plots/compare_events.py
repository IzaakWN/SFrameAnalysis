#! /usr/bin/env python

import os, sys
sys.path.append('../plots')
import PlotTools.PlotTools
import PlotTools.CMS_lumi as CMS_lumi, PlotTools.tdrstyle as tdrstyle
from PlotTools.SampleTools import getEfficienciesFromHistogram, getEfficienciesFromTree, printComparingCutflow
from math import log, floor, ceil
import re
import ROOT
from ROOT import TFile, TH1F, TH2F, kRed, kBlue, THStack, TCanvas, TLegend, kAzure, kRed, kGreen, kYellow, kOrange, gPad, gROOT, gStyle
ROOT.gROOT.SetBatch(ROOT.kTRUE)
gStyle.SetOptStat(0)

SFRAME_DIR = "SFrameAnalysis_Moriond"
DIR = "/shome/ineuteli/analysis/%s/AnalysisOutput/" % (SFRAME_DIR)
MORIOND_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
EM_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputEM"
MM_DIR = "/scratch/ineuteli/SFrameAnalysis/AnalysisOutputMM"
OUT_DIR = "events"
mylabel = "_ICHEP"

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



def compareEvents():
    print ">>>\n>>> compareEvents()"
    
#     filename1 = "%s/events_emu_Olga.txt"%(OUT_DIR)
#     filename2 = "%s/runnumber_2j.txt"%(OUT_DIR)
    filenames = [
        ( "emu",    "events_emu_Olga.txt",      "runnumber_2j.txt"              ),
#         ( "ST",     "events_emu_Olga_T_W.txt",  "runnumber_ST_tW_top_2j.txt"    ),
    ]
    
    hist1 = TH1F("hist1","hist1",100,-5,5)
    hist2 = TH1F("hist2","hist2",100,-5,5)
    
    Nmax1 = 10000
    Nmax2 = 100
    
    for samplename, filename1, filename2 in filenames:    
        print ">>> comparing %d events of  %s"%(Nmax1,filename1)
        print ">>>        to %d events of  %s"%(Nmax2,filename2)
        print ">>> "
        filename1 = "%s/%s"%(OUT_DIR,filename1)
        filename2 = "%s/%s"%(OUT_DIR,filename2)
        overlap1in2 = 0
        overlap2in1 = 0
        skipped1 = 0
        skipped2 = 0
        with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
          for i, line1 in enumerate(file1):
            if i>Nmax1: break
            if line1[0]=="#":
                skipped1 += 1
                continue
            line1 = line1.replace('\n','')
            #print ">>> %d: %s"%(i,line1)
            run1,lum1,evt1,jpt_11,jeta_11,jphi_11,jpt_21,jeta_21,jphi_21 = readLineOlga(line1)
            #print ">>> run1, lum1, evt1 = %s, %4s, %9s"%(run1,lum1,evt1)
            file2.seek(0)
            for j, line2 in enumerate(file2):
                if j>Nmax2: break
                if line2[0]=="#":
                    skipped2 += 1
                    continue
                values = readLineIzaak(line2)
                if not values:
                    skipped2 += 1
                    continue
                run2,lum2,evt2,jpt_12,jeta_12,jphi_12,jpt_22,jeta_22,jphi_22 = values
                #print ">>>   run2, lum2, evt2 = %s, %4s, %9s"%(run2,lum2,evt2)
            
                if run1 == run2 and evt1 == evt2: #run1 == run2 andand lum1 == lum2:
                    print ">>> MATCH!"
                    print ">>>   run1, lum1, evt1 = %s, %4s, %9s"%(run1,lum1,evt1)
                    print ">>>   run2, lum2, evt2 = %s, %4s, %9s"%(run2,lum2,evt2)
                    overlap1in2 += 1
                    overlap2in1 += 1
                    jpt_1_error  = 100*(jpt_11-jpt_12)/max(jpt_11,.0001)
                    jpt_2_error  = 100*(jpt_21-jpt_22)/max(jpt_21,.0001)
                    jeta_1_error = 100*(jeta_11-jeta_12)/max(jeta_11,.0001)
                    jeta_2_error = 100*(jeta_21-jeta_22)/max(jeta_21,.0001)
                    jphi_1_error = 100*(jphi_11-jphi_12)/max(jphi_11,.0001)
                    jphi_2_error = 100*(jphi_21-jphi_22)/max(jphi_21,.0001)
                    hist1.Fill(jpt_1_error)
                    hist2.Fill(jpt_2_error)
                    print ">>>   jpt_1 = %8.4f,  jeta_1 = %7.4f,  jphi_1 = %7.4f"%(jpt_11,jeta_11,jphi_11)
                    print ">>>   jpt_1 = %8.4f,  jeta_1 = %7.4f,  jphi_1 = %7.4f"%(jpt_12,jeta_12,jphi_12)
                    print ">>>          %9.3f%%,          %8.3f%%           %8.3f%%"%(jpt_1_error,
                                                                                      jeta_1_error,
                                                                                      jphi_1_error)
                    print ">>>   jpt_2 = %8.4f,  jeta_2 = %7.4f,  jphi_2 = %7.4f"%(jpt_21,jeta_21,jphi_21)
                    print ">>>   jpt_2 = %8.4f,  jeta_2 = %7.4f,  jphi_2 = %7.4f"%(jpt_22,jeta_22,jphi_22)
#                     print ">>>          %9.3f%%,          %8.3%%            %8.3f%%"%(jpt_2_error,
#                                                                                       jeta_2_error,
#                                                                                       jphi_2_error)
                    print ">>>"
                    continue
    
        maxD = int(max(floor(log(Nmax1+1,10))+1,floor(log(Nmax2,10))+1))
        print ">>> "
        print ">>> overlap set 1 in set 2: %d/%s (%5.4g%%)"%(overlap1in2,str(Nmax1).ljust(maxD),100*overlap1in2/Nmax1)
        print ">>> overlap set 2 in set 1: %d/%s (%5.4g%%)"%(overlap2in1,str(Nmax2).ljust(maxD),100*overlap2in1/Nmax2)
        print ">>> skipped1 = %s, skipped2 = %s" % (skipped1,skipped2)
    
        canvas  = TCanvas("canvas","canvas",100,100,800,600)
        hist1.SetLineColor(kBlue)
        hist2.SetLineColor(kRed)
        hist1.Draw("HIST")
        hist2.Draw("HIST SAME")
        x1 = 0.60
        w  = 0.24
        y1 = 0.60
        h  = 0.20
        legend = TLegend(x1,y1,x1+w,y1-h)
        legend.SetFillStyle(0)
        legend.SetBorderSize(0)
        legend.SetTextSize(0.041)
        legend.SetTextFont(42)
        legend.AddEntry(hist1, "jpt_1",'L')
        legend.AddEntry(hist2, "jpt_2",'L')
        legend.Draw()
        canvas.SaveAs("%s/compare_pt_error_%s.png"%(OUT_DIR,samplename))

    



def readLineIzaak(line):
    numbers = re.findall("[-+]?\d+(?:\.\d+)?",line)
    #print numbers
    if len(numbers)!=10: return False
    row, run, lum, evt, jpt_1, jeta_1, jphi_1, jpt_2, jeta_2, jphi_2 = numbers
    return [ int(run),int(lum),int(evt),
             float(jpt_1),float(jeta_1),float(jphi_2),float(jpt_2),float(jeta_2),float(jphi_2) ]

def readLineOlga(line):
    #print ">>>   %s"%line.split(' ')
    line = line.replace('\n','').split(' ')
    run,   evt,    lum    = line[0:3]
    #pt_1,  eta_1,  phi_1  = line[3:6]
    #pt_2,  eta_2,  phi_2  = line[6:9]
    jpt_1, jeta_1, jphi_1 = line[9:12]
    jpt_2, jeta_2, jphi_2 = line[12:15]
    return [ int(run),int(lum),int(evt),
             float(jpt_1),float(jeta_1),float(jphi_2),float(jpt_2),float(jeta_2),float(jphi_2) ]
    



def writeRunNumbers():
    print ">>>\n>>> writeRunNumbers()"
    
    channel     = "emu"
    emu_check   = "channel>0 && njets>1 && pt_1>25 && pt_2>25 && abs(eta_1)<2.1 && abs(eta_2)<2.1 && iso_1<0.10 && q_1*q_2<0 && 70<m_vis&&m_vis<110"
    DIR         = MORIOND_DIR
    
    if "emu" in channel:
        DIR = DIR.replace("AnalysisOutput","AnalysisOutputEM")
    
    cuts = [    
                ("2j0b",    "%s && %s"  % ("ncbtag==0",emu_check)),
                ("2j",      "%s"        % (emu_check)),
    ]
    
    samples = [
                    #("SingleMuon",  "SingleMuon_Run2016",                   "SingleMuon"     ),
                    ("MuonEG",  "MuonEG_Run2016",                           "MuonEG"         ),
                    ("ST/",     "ST_tW_top_5f_inclusiveDecays",             "ST_tW_top"      ),
                    #("ST/",     "ST_tW_antitop_5f_inclusiveDecays",         "ST_tW_antitop"  ),
                    #("ST/",     "ST_t-channel_top_4f_inclusiveDecays",      "ST_t_top"       ),
                    #("ST/",     "ST_t-channel_antitop_4f_inclusiveDecays",  "ST_t_antitop"   ),

    ]
    
    scanvariables = "run:lum:evt:jpt_1:jeta_1:jphi_1:jpt_2:jeta_2:jphi_2"
    scanvariables = "run:lum:evt:jpt_1:jeta_1:jphi_1:jpt_2:jeta_2:jphi_2"
    scanvariables = scanvariables.replace("jpt_1", "jpt_1_jer" ).replace(
                                          "jeta_1","jeta_1_jer").replace(
                                          #"jphi_1","jphi_1_jer").replace(
                                          "jpt_2", "jpt_2_jer" ).replace(
                                          "jeta_2","jeta_2_jer")#.replace(
                                          #"jphi_2","jphi_2_jer")
    
    for sampledir, sample, samplename in samples:
        print ">>>\n>>> writing run, lumi, event number for %s" % (sample)
        
        file    = TFile( "%s/%s/TauTauAnalysis.%s_Moriond.root" % (DIR, sampledir,sample))
        tree    = file.Get("tree_%s"%channel)
        
        for cutname, cut in cuts:
            print ">>> cut \"%s\": \"%s\"" % (cutname,cut)
            
            txtname = "%s/runnumber_%s_%s.txt" % (OUT_DIR,samplename,cutname.replace(', ','-').replace(' ','_').replace(':','-').replace('(','').replace(')','').replace('#','').replace('<','lt').replace('>','gt')) 
            #print ">>> %d entries passing the cut"%(tree.GetEntries(cut))
            tree.GetPlayer().SetScanRedirect(True)
            tree.GetPlayer().SetScanFileName(txtname)
            N = tree.Scan(scanvariables, cut, "precision=10") #, "colsize=20"
            
            with open(txtname,'r') as txtfile0: data = txtfile0.read()
            with open(txtname,'w') as txtfile1: txtfile1.write(("# %d events with \"%s\" selections:\n#   %s\n\n"%(N,cutname,cut))+data)
            
            
    
    print ">>>"

                



def makeDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR





def main():
    print ""
    
    makeDirectory(OUT_DIR)
    
    # MAIN CHECKS
#     writeRunNumbers()
    compareEvents()
    
    print ">>>\n>>> done\n"
    
    
    
    
    
if __name__ == '__main__':
    main()
