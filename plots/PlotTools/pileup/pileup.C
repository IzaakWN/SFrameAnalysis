/*
 * @short: provide Z pt weights at drawing level
 *         root file from Cecile
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

TString filename_data2017 = "$SFRAME_DIR/../plots/PlotTools/pileup/Data_PileUp_2017_69p2.root";
TString filename_MC2017 = "$SFRAME_DIR/../plots/PlotTools/pileup/MC_PileUp_Winter17_PU25ns_V2_fromMC.root";
TH1F* hist_PU_data;
TH1F* hist_PU_MC;
//TH1F* hist_PU_weights;



void readPUFile(TString filename_data=filename_data2017,TString filename_MC=filename_MC2017){
  
  std::cout << ">>> opening " << filename_data2017 << std::endl;
  TFile *file_data = new TFile(filename_data2017);
  hist_PU_data = (TH1F*) file_data->Get("pileup");
  hist_PU_data->SetDirectory(0);
  file_data->Close();
  
  std::cout << ">>> opening " << filename_MC2017 << std::endl;
  TFile *file_MC = new TFile(filename_MC2017);
  hist_PU_MC = (TH1F*) file_MC->Get("pileup");
  hist_PU_MC->SetDirectory(0);
  file_MC->Close();
  
  hist_PU_data->Scale(1./hist_PU_data->Integral());
  hist_PU_MC->Scale(1./hist_PU_MC->Integral());
  
}



Float_t getPUWeight(Int_t npu){
  
  float data = hist_PU_data->GetBinContent(hist_PU_data->FindBin(npu));
  float mc   = hist_PU_MC->GetBinContent(hist_PU_MC->FindBin(npu));
  //std::cout << data << " " << mc << " " << npu << " -> " << data/mc << std::endl;
  
  if(mc > 0.){
    return data/mc;
    //    std::cout << "pu weight =" << data/mc << std::endl;
  }//else{
    //std::cout << "No predefined pileup weights" << std::endl;
  //  }
  return 1;

}



void pileup(){
  std::cout << ">>> initializing pileup.C ... " << std::endl;
  readPUFile();
}


