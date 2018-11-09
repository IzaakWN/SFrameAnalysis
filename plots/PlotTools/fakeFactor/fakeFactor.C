/*
 * @short: provide fake factor weights at drawing level
 * @author: Izaak Neutelings (October 2018)
 *
 * source: https://indico.cern.ch/event/754296/contributions/3147076/attachments/1719573/2775452/Htt_Meeting_180920.pdf
 *         https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauJet2TauFakes
 *
 */
 
#include <iostream>
#include <algorithm>
//#include <string>
#include <iomanip> // for setw
#include "TROOT.h"
//#include "TSystem.h"
#include "TMath.h"
#include "TFile.h"
#include "TGraphAsymmErrors.h"
#include "TF1.h"
#include "TH2.h"
#include "TH2F.h"
//gROOT->ProcessLine(".include /shome/ineuteli/analysis/CMSSW_9_4_6/src/");
//gSystem->Load("/shome/ineuteli/analysis/CMSSW_9_4_6/lib/slc6_amd64_gcc630/libHTTutilitiesJet2TauFakes.so")
#include "/shome/ineuteli/analysis/CMSSW_9_4_6/src/HTTutilities/Jet2TauFakes/interface/FakeFactor.h"
//#include "HTTutilities/Jet2TauFakes/interface/FakeFactor.h"
using namespace std;
TString inputdir = "/shome/ineuteli/analysis/CMSSW_9_4_6/src/HTTutilities/Jet2TauFakes/data/SM2017";
FakeFactor* fakeFactors;
std::vector<string> inputNames;
//TFile *file;


// Class to contain fractions for some binning
class Fractions {
    TString name;
    std::vector<Float_t> xbins, fracs;
  public:
    Fractions(TString,std::vector<Float_t>,std::vector<Float_t>);
    Float_t get(Float_t);
};

Fractions::Fractions(TString name_in, std::vector<Float_t> xbins_in, std::vector<Float_t> fracs_in) {
  if(!std::is_sorted(xbins_in.begin(),xbins_in.end())){
    std::cout << ">>> Warning! Fractions::set: xbins is not sorted !" << std::endl;
  }
  if(xbins_in.size()!=fracs_in.size()+1)
    std::cout << ">>> Warning! Fractions::set: xbins.size() = "<<xbins_in.size()<<" != "<<fracs_in.size()<<"+1 = fracs.size()+1 !!! " << std::endl;
  name  = name_in;
  xbins = xbins_in;
  fracs = fracs_in;
}

Float_t Fractions::get(Float_t xval) {
  if(xval<=xbins[0]) { return fracs[0]; }
  for(unsigned int i=1; i<xbins.size(); i++){ if(xval<xbins[i]) return fracs[i-1]; }
  return fracs[fracs.size()-1];
}
std::map<TString,Fractions*> fractions;



void loadFakeFactor(TString channel="tt", TString WP="tight"){
  
  TString filename = inputdir+"/"+WP+"/"+"vloose"+"/"+channel+"/"+"fakeFactors.root";
  std::cout << ">>> opening "<<filename<<std::endl;
  TFile* file = new TFile(filename);
  fakeFactors = (FakeFactor*) file->Get("ff_comb");
  inputNames  = fakeFactors->inputs();
  file->Close();
  
  //for(auto const& x: inputNames)
  //  std::cout << x << "\n";
  
  // test
  //std::vector<string> inputNames( fakeFactors->inputs() );
  //std::vector<double> inputs( inputNames.size() );
  //inputs[0] = 30;   //tau_pt;
  //inputs[1] = 0;    //tau_decayMode;
  //inputs[2] = 1;    //njet
  //inputs[3] = 40;   //mvis;
  //inputs[4] = 10;   //mt;
  //inputs[5] = 0.00; //muon_iso;
  //inputs[6] = 0.4;  //frac_qcd
  //inputs[7] = 0.3;  //frac_ew
  //inputs[8] = 0.2;  //frac_tt
  //
  //std::cout << "test fakeFactors->value(inputs): " << fakeFactors->value(inputs) << std::endl;
  
  //delete fakeFactors;
  //file->Close();
}



void setFraction(TString process, TString var, Int_t nbins, Float_t xmin, Float_t xmax, std::vector<Float_t> fracs){
  if(fracs.size()!=(unsigned)nbins)
    std::cout << ">>> Warning! fakeFactor::setFraction: fracs.size() = "<<fracs.size()<<" != "<<nbins<<" = nbins!!! " << std::endl;
  
  TString name = process+var;
  std::map<TString,Fractions*>::iterator itr = fractions.find(process);
  if(itr!=fractions.end())
    delete itr->second;
  
  std::vector<Float_t> xbins;
  Float_t step = (xmax-xmin)/nbins;
  for(int i=0; i<=nbins; i++){
    //std::cout << xmin+i*step << ", ";
    xbins.push_back(xmin+i*step);
  }
  //std::cout << std::endl;
  fractions[process] = new Fractions(name,xbins,fracs);
  //std::cout << 0 << ": " << fractions[process]->get(0) << std::endl;
}



// TAUTAU
Float_t getFakeFactor(Float_t pt_1, Int_t dm_1, Int_t id_1,
                      Float_t pt_2, Int_t dm_2, Int_t id_2, Int_t njets, Float_t m_vis){
  Float_t fakeFactor = 0.0;
  std::vector<double> inputs( inputNames.size() );
  if(id_1<2 or id_2<2 or (id_1<16 and id_2<16)){
    return 0.0;
  }else if(id_1>id_2){ // subleading tau's iso is inverted
    inputs[0] = pt_1;
    inputs[1] = pt_2;
    inputs[2] = dm_1;
    inputs[3] = njets;
    inputs[4] = m_vis;
    inputs[5] = fractions["QCD_2"]->get(m_vis);
    inputs[6] = fractions["EWJ_2"]->get(m_vis);
    inputs[7] = fractions["TTJ_2"]->get(m_vis);
  }else{ // leading tau's iso is inverted
    inputs[0] = pt_2;
    inputs[1] = pt_1;
    inputs[2] = dm_2;
    inputs[3] = njets;
    inputs[4] = m_vis;
    inputs[5] = fractions["QCD_1"]->get(m_vis);
    inputs[6] = fractions["EWJ_1"]->get(m_vis);
    inputs[7] = fractions["TTJ_1"]->get(m_vis);
  }
  fakeFactor  = 0.5*fakeFactors->value(inputs);
  
  return fakeFactor;
}



// LTAU
Float_t getFakeFactor(Float_t pt, Int_t dm, Int_t id, Float_t iso_lep, Int_t njets, Float_t m_vis, Float_t mt){
  Float_t fakeFactor = 0.0;
  std::vector<double> inputs( inputNames.size() );
  if(id<2 or id>=16){
    return 0.0;
  }else{ // subleading tau's iso is inverted
    inputs[0] = pt;
    inputs[1] = dm;
    inputs[2] = njets;
    inputs[3] = m_vis;
    inputs[4] = mt;
    inputs[5] = iso_lep;
    inputs[6] = fractions["QCD"]->get(m_vis); //->GetBinContent(fractions["QCD"]->FindBin(m_vis));
    inputs[7] = fractions["EWJ"]->get(m_vis); //->GetBinContent(fractions["EWJ"]->FindBin(m_vis));
    inputs[8] = fractions["TTJ"]->get(m_vis); //->GetBinContent(fractions["TTJ"]->FindBin(m_vis));
  }
  fakeFactor  = fakeFactors->value(inputs);
  
  return fakeFactor;
}



void closeFakeFactor(){
  delete fakeFactors;
  inputNames.clear();
}



void fakeFactor(){
  std::cout << ">>> initializing fakeFactor.C ... " << std::endl;
  //loadFakeFactor();
  //file->Close();
}


