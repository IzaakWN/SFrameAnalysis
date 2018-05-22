/*
 * @short: provide fake rate weights at drawing level
 *         root file from Cecile
 * @author: Izaak Neutelings (April 2018)
 *
 */

#include "TROOT.h"
#include "TMath.h"
#include "TFile.h"
//#include "TH1.h"
//#include "TH1F.h"
#include "TGraphAsymmErrors.h"
#include "TF1.h"
#include "TH2.h"
#include "TH2F.h"
#include <iostream>
#include <algorithm>
//#include <string>
using namespace std;

Float_t zero = 0.0;
//TString filename = "$SFRAME_DIR/../plots/PlotTools/fakeRate/fakeRate2017_histograms_Cecile.root";
TString filename = "$SFRAME_DIR/../plots/fakeRate/fakeRate2017_Izaak.root";
TString ID = "MVArerun";
std::map<Int_t,TGraphAsymmErrors*> fakeRates;   // DM -> TGAE(pt) -> weight
std::map<Int_t,TH2F*>              fakeRates2D; // DM -> TH2F(pt,mass) -> weight
std::map<Int_t,Float_t> flatFakeRates = {{0,12636./36903.},{1,15510./68038.},{10,4801./30212.}};
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
      //fakeRates[wp][dm] = (TF1*) file->Get(functionname);
      //fakeRates[wp][dm] = (TH1F*) file->Get(histname);
      fakeRates[dm]    = (TGraphAsymmErrors*) file->Get(histname);
      fakeRates2D[dm]  = (TH2F*) file->Get(histname+"_mass");
    }
  //}
}



// NOMINAL fake rate vs. pt
Float_t getFakeRate(Float_t pt, Int_t dm){
  Float_t fakeRate = 0.0;
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    fakeRate = fakeRates[dm]->Eval(pt);
    //fakeRate = fakeRates[dm]->GetBinContent(fakeRate[dm]->GetXaxis()->FindBin(pt));
  }//else{
    //std::cout << ">>> WARNING! getFakeRate: weird decayMode="<<dm<<"!"<<std::endl;
  //}
  //std::cout << ">>> getFakeRate: pt="<<pt<<", decayMode="<<dm<<", FR="<<fakeRate<<std::endl;
  return fakeRate; // TMath::Max(zero,fakeRate);
}

// NOMINAL fake rate vs. mass vs. pt
Float_t getFakeRate(Float_t pt, Float_t mass, Int_t dm){
  Float_t fakeRate = 0.0;
  if(dm==0) return getFakeRate(pt,dm);
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    Int_t ipt = TMath::Min(fakeRates2D[dm]->GetXaxis()->FindBin(pt),   fakeRates2D[dm]->GetXaxis()->GetNbins()-1);
    Int_t im  = TMath::Min(fakeRates2D[dm]->GetYaxis()->FindBin(mass), fakeRates2D[dm]->GetYaxis()->GetNbins()-1);
    fakeRate  = fakeRates2D[dm]->GetBinContent(ipt,im);
    while(fakeRate==0.0 and ipt>0){
      ipt -= 1;
      fakeRate = fakeRates2D[dm]->GetBinContent(ipt,im);
    }
  }
  return fakeRate;
}

// DOWN fake rate vs. pt
Float_t getFakeRateDown(Float_t pt, Int_t dm){
  Float_t fakeRate = 0.0;
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    fakeRate = flatFakeRates[dm];
  }
  return fakeRate;
}

// DOWN fake rate vs. mass vs. pt
Float_t getFakeRateDown(Float_t pt, Float_t mass, Int_t dm){
  return getFakeRateDown(pt,dm);
}

// UP fake rate vs. mass
Float_t getFakeRateUp(Float_t pt, Int_t dm){
  Float_t fakeRate = 0.0;
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    fakeRate = fakeRates[dm]->Eval(pt);
    fakeRate = 2*fakeRate - flatFakeRates[dm];
  }
  return fakeRate;
}

// UP fake rate vs. mass vs. pt
Float_t getFakeRateUp(Float_t pt, Float_t mass, Int_t dm){
  Float_t fakeRate = 0.0;
  if(std::find(decayModes.begin(),decayModes.end(),dm)!=decayModes.end()){
    fakeRate = getFakeRate(pt,mass,dm);
    fakeRate = 2*fakeRate - flatFakeRates[dm];
  }
  return fakeRate;
}



void fakeRate(){
  //std::cout << std::endl;
  std::cout << ">>> initializing fakeRate.C ... " << std::endl;
  //std::cout << std::endl;
  readFile();
}


