/*
 * @short: provide fake rate weights at drawing level
 *         root file from Cecile
 * @author: Izaak Neutelings (April 2018)
 */

#include "TROOT.h"
#include "TMath.h"
#include "TFile.h"
//#include "TH1.h"
//#include "TH1F.h"
#include "TGraphAsymmErrors.h"
#include "TF1.h"
#include <iostream>
#include <algorithm>
//#include <string>
//using namespace std;

Float_t zero = 0.0;
TString filename = "$SFRAME_DIR/../plots/PlotTools/fakeRate/fakeRate2017_histograms_Cecile.root";
TString ID = "MVArerun";
std::map<Int_t,TGraphAsymmErrors*> weights; // DM -> TF1(pt) -> weight
//std::map<TString,map<Int_t,TH1F*>> weights; // WP -> DM -> TF1(pt) -> weight
//std::vector<TString> workingPoints = { "L", "M", "T", "VT", "VVT" };
std::vector<Int_t> decayModes = { 0, 1, 10 };



void readFile(){
  
  std::cout << ">>> opening "<<filename<<std::endl;
  TFile *file = new TFile(filename);
  //for(TString wp: workingPoints){
    TString wp = "T";
    for(Int_t dm: decayModes){
      //std::cout << ">>> loading in wp "<<std::setw(3)<<wp<<", dm "<<std::setw(2)<<dm;
      //std::cout << ">>> loading in dm "<<std::setw(2)<<dm;
      TString dmname   = "_dm"; dmname += dm;
      TString nom      = "h_"+ID+wp+dmname;
      TString denom    = "h_"+ID+"VL"+dmname;
      TString histname = nom+"_"+denom;
      //std::cout << ": " << histname << std::endl;
      //weights[wp][dm] = (TF1*) file->Get(functionname);
      //weights[wp][dm] = (TH1F*) file->Get(histname);
      weights[dm] = (TGraphAsymmErrors*) file->Get(histname);
    }
  //}
}



Float_t getFakeRate(Float_t pt, Int_t dm){
  Float_t fakeRate = 0.0;
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    fakeRate = weights[dm]->Eval(pt);
    //fakeRate = weights[dm]->GetBinContent(weights[dm]->GetXaxis()->FindBin(pt));
  }//else{
    //std::cout << ">>> WARNING! getFakeRate: weird decayMode="<<dm<<"!"<<std::endl;
  //}
  //std::cout << ">>> getFakeRate: pt="<<pt<<", decayMode="<<dm<<", FR="<<fakeRate<<std::endl;
  return fakeRate; // TMath::Max(zero,fakeRate);
}



//Float_t getFakeRate(Float_t pt, Int_t dm, Int_t passVL, Int_t passL, Int_t passM, Int_t passT, Int_t passVT, Int_t passVVT){
//  
//  if(passVL==0 or passVT==1) return 0.0;
//  
//  Float_t fakeRate = 1.0;
//  TString wp = "L";
//  if(passL==1){
//    if(     passM==0)   wp = "M";
//    else if(passT==0)   wp = "T";
//    else if(passVT==0)  wp = "VT";
//    else if(passVVT==0) wp = "VVT";
//    else std::cout << ">>> WARNING! getFakeRate: Event impossibly fails all WPs except VL!"<<std::endl;
//  }
//  
//  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
//    fakeRate = weights[wp][dm]->Eval(pt);
//  }else{
//    std::cout << ">>> WARNING! getFakeRate: weird decayMode="<<dm<<"!"<<std::endl;
//  }
//  //sstd::cout << ">>> getFakeRate: pt="<<pt<<", decayMode="<<dm<<", FR="<<fakeRate<<std::endl;
//  return TMath::Max(zero,fakeRate);
//}



void fakeRate(){
  std::cout << std::endl;
  std::cout << "Initialize fakeRate.C ... " << std::endl;
  std::cout << std::endl;
  readFile();
}


