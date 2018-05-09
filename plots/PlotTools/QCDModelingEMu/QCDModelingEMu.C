/*
  functionmacro.C : provide QCD weights at drawing level
  modified from : https://github.com/CMS-HTT/QCDModelingEMu

  4 April 2017 Y.T
 */


#include "TMath.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include <iostream>
#include "TROOT.h"

TH2F* h_weight[3];
Int_t nBinsQCD;
Float_t qcdMin;
Float_t qcdMax;



void readFile_QCDModelingEMu(){
  
  TFile *file = new TFile("/shome/ineuteli/analysis/SFrameAnalysis_Moriond/plots/PlotTools/QCDModelingEMu/data/QCD_weight_emu_2016BtoH.root");
  
  for(int dr=0; dr < 3; dr++){
    
    TString wname = "QCDratio_CR1_dR";
    if(dr==0) wname += "Lt2";
    else if(dr==1) wname += "2to4";
    else if(dr==2) wname += "Gt4";
    
    //std::cout << wname << " is read" << std::endl;

    h_weight[dr] = (TH2F*) gROOT->FindObject(wname);

    if(dr==0){
      nBinsQCD = h_weight[dr]->GetNbinsX();
      qcdMin = h_weight[dr]->GetXaxis()->GetBinLowEdge(1);
      qcdMax = h_weight[dr]->GetXaxis()->GetBinLowEdge(1+nBinsQCD);
    }
  }    
  
  //std::cout << "nBinsQCD, pt_min, pt_max = " << nBinsQCD << " " << qcdMin << " " << qcdMax << std::endl;
  //delete file;
}



float getQCDWeight(Double_t pt_1, Double_t pt_2, Double_t dr_tt){
  float ptlead  = pt_1;
  float pttrail = pt_2;
  
  if (ptlead<pttrail){
    ptlead  = pt_2;
    pttrail = pt_1;
  }
  
  if (ptlead>qcdMax)  ptlead = qcdMax-0.1;  
  if (ptlead<qcdMin)  ptlead = qcdMin+0.1; 
  if (pttrail>qcdMax) pttrail = qcdMax-0.1;  
  if (pttrail<qcdMin) pttrail = qcdMin+0.1; 
  
  float qcdweight = 1;
  
  int bin = -1;
  if(dr_tt < 2) bin = 0;
  else if(dr_tt >= 2 && dr_tt < 4) bin = 1;
  else if(dr_tt >= 4) bin = 2;
  else{
    std::cout << "Invalid dR ... !   ... return 1" << std::endl;
    return 1;
  }
  
  qcdweight = h_weight[bin]->GetBinContent(h_weight[bin]->FindBin(pttrail,ptlead));  
  //std::cout << "(pt_1, pt_2, dr, weight) = " << pt_1 << " " << pt_2 << " " << dr_tt << " " << qcdweight << std::endl;
  return qcdweight;

}



void QCDModelingEMu(){
  //std::cout << std::endl;
  //std::cout << "Initialize functionmacro.C ... " << std::endl;
  //std::cout << std::endl;
  readFile_QCDModelingEMu();
}


