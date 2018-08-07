/*
 * @short: provide Z pt weights at drawing level for checks
 * @author: Izaak Neutelings (June 2018)
 *
 */

#include "TROOT.h"
#include "TFile.h"
#include "TH2.h"
#include "TH2F.h"
#include <iostream>
#include <algorithm>
using namespace std;

TString filename_check = "$SFRAME_DIR/../plots/Zpt/Zpt_weights_2017_Izaak.root";
TString histname_gen   = "zptmass_weights";
TString histname_reco  = histname_gen+"_reco";
TH2F* histZpt;
TH2F* histZpt_reco;


void loadZptWeights(TString filename=filename_check){  
  std::cout << ">>> loadZptWeights: opening " << filename_check << std::endl;
  if(!histZpt){
    TFile *file_gen = new TFile(filename);
    histZpt = (TH2F*) file_gen->Get(histname_gen);
    histZpt->SetDirectory(0);
    file_gen->Close();
  }else{
    std::cout << ">>>   already opened" << std::endl;
  }
}


void loadZptWeights_reco(TString filename=filename_check){  
  std::cout << ">>> loadZptWeights_reco: opening " << filename_check << std::endl;
  TFile *file_reco = new TFile(filename);
  histZpt_reco = (TH2F*) file_reco->Get(histname_reco);
  histZpt_reco->SetDirectory(0);
  file_reco->Close();  
}


Float_t getZpt_gen(Float_t m_genboson, Float_t pt_genboson){
  Int_t xbin   = histZpt->GetXaxis()->FindBin(m_genboson);
  Int_t ybin   = histZpt->GetYaxis()->FindBin(pt_genboson);
  Float_t weight = 1.0;
  while(xbin<1) xbin++; while(xbin>histZpt->GetXaxis()->GetNbins()) xbin--;
  while(ybin<1) ybin++; while(ybin>histZpt->GetYaxis()->GetNbins()) ybin--;
  weight = histZpt->GetBinContent(xbin,ybin);
  if(weight==0.0) return 1.;
  return histZpt->GetBinContent(xbin,ybin);
}


Float_t getZpt_reco(Float_t mass_reco, Float_t pt_reco){
  Int_t xbin = histZpt_reco->GetXaxis()->FindBin(mass_reco);
  Int_t ybin = histZpt_reco->GetYaxis()->FindBin(pt_reco);
  while(xbin<1) xbin++; while(xbin>histZpt_reco->GetXaxis()->GetNbins()) xbin--;
  while(ybin<1) ybin++; while(ybin>histZpt_reco->GetYaxis()->GetNbins()) ybin--;
  return histZpt_reco->GetBinContent(xbin,ybin);
}


void zptweight_check(){
  std::cout << ">>> initializing zptweights_check.C ... " << std::endl;
}

