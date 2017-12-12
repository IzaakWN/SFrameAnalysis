#include "../include/PUWeight.h"

#include "TFile.h"

#include <iostream>



// Get MC pile-up scenario from string representation
PUWeight::Scenario PUWeight::toScenario(const std::string& str) {
  PUWeight::Scenario sc = Winter17_25ns;
  if(      str == "Winter17_25ns"  ) sc = Winter17_25ns;
  else if( str == "PUS25ns"        ) sc = Winter15_25ns;
  else if( str == "Moriond17_25ns" ) sc = Moriond17_25ns;
  else {
    std::cerr << "\n\nERROR unknown scenario '" << str << "'" << std::endl;
    throw std::exception();
  }
 
  return sc;
}



// MC pile-up scenario to string representation
std::string PUWeight::toString(const PUWeight::Scenario sc) {
  std::string str;
  if(       sc == Winter17_25ns  ) str = "Winter17_25ns";
  else if ( sc == Winter15_25ns  ) str = "Winter15_25ns";
  else if ( sc == Moriond17_25ns ) str = "Moriond17_25ns";
  else {
    std::cerr << "\n\nERROR unknown scenario '" << sc << "'" << std::endl;
    throw std::exception();
  }

  return str;
}



// Constructor. Initializes default behaviour to return PU weight of 1
PUWeight::PUWeight() : isInit_(false), nPUMax_(0) { }



// Initialise weights for a given MC pile-up scenario. Can only be called once.
void PUWeight::initPUWeights(const std::string& dataRootFileName, const std::string& dataRootHistName, const std::string& mcScenario) {

  // if( isInit_ ) {
  //   std::cerr << "\n\nERROR in PUWeight: weights already initialised" << std::endl;
  //   throw std::exception();
  // }
  
  // Get data distribution from file
  TFile file(dataRootFileName.c_str(), "READ");
  TH1* h = NULL;
  file.GetObject(dataRootHistName.c_str(),h);
  if( h == NULL ) {
    std::cerr << "\n\nERROR in PUWeight: Histogram " << dataRootHistName << " does not exist in file '" << dataRootFileName << "'\n.";
    throw std::exception();
  }
  h->SetDirectory(0);
  file.Close();
  
  PUWeight::Scenario sc = toScenario(mcScenario);
  
  // Computing weights
  puWeigths_ = generateWeights(sc,h);
  nPUMax_ = puWeigths_.size();
  
  // Clean up
  delete h;
  
  isInit_ = true;
}



// Get weight factor dependent on number of added PU interactions
double PUWeight::getPUWeight(const int nPU) const {

  double w = 1.;
  if( isInit_ ) {
    if( nPU >= nPUMax_ ) {
      //std::cerr << "WARNING: Number of PU vertices = " << nPU << " out of histogram binning." << std::endl;
      // In case nPU is out-of data-profile binning,
      // use weight from last bin
      w = puWeigths_.back();
    } else {
      w = puWeigths_.at(nPU);
    }
  }

  return w;
}



// Generate weights for given data PU distribution
// Scenarios from: https://twiki.cern.ch/twiki/bin/view/CMS/Pileup_MC_Gen_Scenarios
// Code adapted from: https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupReweighting
std::vector<double> PUWeight::generateWeights(const PUWeight::Scenario sc, const TH1* data_npu_estimated) const {
  
  // Store probabilites for each pu bin
  unsigned int nPUMax = 0;
  double *npuProbs = 0; // gives memory leaks for Winter17_25ns?
  std::vector<double> v_npuProbs;
  
  
  if( sc == Winter17_25ns ) {
    
    // Get data distribution from file
    TString mcPath = "$SFRAME_DIR/../PileupReweightingTool/histograms/";
    TString mcFileName = mcPath + "MC_PileUp_Winter17_PU25ns_V1.root";
    TString mcHistName = "pileup";
    TFile file(mcFileName, "READ");
    TH1* mcHist = NULL;
    file.GetObject(mcHistName,mcHist);
    if( mcHist == NULL ) {
      std::cerr << "\n\nERROR in PUWeight: Histogram " << mcHistName << " does not exist in file '" << mcFileName << "'\n.";
      throw std::exception();
    }
    
    nPUMax = 100;
    double npuWinter17_25ns[nPUMax];
    for(unsigned int npu = 0; npu < nPUMax; ++npu) {
      const double npuProb = mcHist->GetBinContent(mcHist->GetXaxis()->FindBin(npu));
      npuWinter17_25ns[npu] = npuProb;
      v_npuProbs.push_back(npuProb);
    }
    
    file.Close();
    npuProbs = npuWinter17_25ns;
    
  }
//   else if( sc == Winter15_25ns ) {
//     std::cout<<"\n  in Winter15_25ns\n";
//     nPUMax = 52;
//     double npuWinter15_25ns[52] = {
//       0.000829312873542,
//       0.00124276120498,
//       0.00339329181587,
//       0.00408224735376,
//       0.00383036590008,
//       0.00659159288946,
//       0.00816022734493,
//       0.00943640833116,
//       0.0137777376066,
//       0.017059392038,
//       0.0213193035468,
//       0.0247343174676,
//       0.0280848773878,
//       0.0323308476564,
//       0.0370394341409,
//       0.0456917721191,
//       0.0558762890594,
//       0.0576956187107,
//       0.0625325287017,
//       0.0591603758776,
//       0.0656650815128,
//       0.0678329011676,
//       0.0625142146389,
//       0.0548068448797,
//       0.0503893295063,
//       0.040209818868,
//       0.0374446988111,
//       0.0299661572042,
//       0.0272024759921,
//       0.0219328403791,
//       0.0179586571619,
//       0.0142926728247,
//       0.00839941654725,
//       0.00522366397213,
//       0.00224457976761,
//       0.000779274977993,
//       0.000197066585944,
//       7.16031761328e-05,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0,
//       0.0
//     };
//     // double npuWinter15_25ns[52] = {
//     //                         4.8551E-07,
//     //                         1.74806E-06,
//     //                         3.30868E-06,
//     //                         1.62972E-05,
//     //                         4.95667E-05,
//     //                         0.000606966,
//     //                         0.003307249,
//     //                         0.010340741,
//     //                         0.022852296,
//     //                         0.041948781,
//     //                         0.058609363,
//     //                         0.067475755,
//     //                         0.072817826,
//     //                         0.075931405,
//     //                         0.076782504,
//     //                         0.076202319,
//     //                         0.074502547,
//     //                         0.072355135,
//     //                         0.069642102,
//     //                         0.064920999,
//     //                         0.05725576,
//     //                         0.047289348,
//     //                         0.036528446,
//     //                         0.026376131,
//     //                         0.017806872,
//     //                         0.011249422,
//     //                         0.006643385,
//     //                         0.003662904,
//     //                         0.001899681,
//     //                         0.00095614,
//     //                         0.00050028,
//     //                         0.000297353,
//     //                         0.000208717,
//     //                         0.000165856,
//     //                         0.000139974,
//     //                         0.000120481,
//     //                         0.000103826,
//     //                         8.88868E-05,
//     //                         7.53323E-05,
//     //                         6.30863E-05,
//     //                         5.21356E-05,
//     //                         4.24754E-05,
//     //                         3.40876E-05,
//     //                         2.69282E-05,
//     //                         2.09267E-05,
//     //                         1.5989E-05,
//     //                         4.8551E-06,
//     //                         2.42755E-06,
//     //                         4.8551E-07,
//     //                         2.42755E-07,
//     //                         1.21378E-07,
//     //                         4.8551E-08};
//     npuProbs = npuWinter15_25ns;
//   }
//   else if( sc == Moriond17_25ns ) {
//     std::cout<<"\n  in Moriond17_25ns\n";
//     
//     // Get data distribution from file
//     TString mcPath = "$SFRAME_DIR/../PileupReweightingTool/histograms/";
//     TString mcFileName = mcPath + "MC_PileUp_Moriond17_PU25ns_V1.root";
//     TString mcHistName = "pileup";
//     TFile file(mcFileName, "READ");
//     TH1* mcHist = NULL;
//     file.GetObject(mcHistName,mcHist);
//     if( mcHist == NULL ) {
//       std::cerr << "\n\nERROR in PUWeight: Histogram " << mcHistName << " does not exist in file '" << mcFileName << "'\n.";
//       throw std::exception();
//     }
//     
//     nPUMax = 800;
//     double npuMoriond17_25ns[nPUMax];
//     for(unsigned int npu = 0; npu < nPUMax; ++npu) {
//       const double npuProb = mcHist->GetBinContent(mcHist->GetXaxis()->FindBin(npu));
//       npuMoriond17_25ns[npu] = npuProb;
//     }
//     file.Close();
//     npuProbs = npuMoriond17_25ns;
//     
//   }
  
//   for(unsigned int npu = 0; npu < nPUMax; ++npu) {
//      std::cout<<"  npuProbs["<<npu<<"] = "<<npuProbs[npu]<<"\n";
//      std::cout<<"  v_npuProbs["<<npu<<"] = "<<v_npuProbs[npu]<<"\n";
//   }
  
  // Check that binning of data-profile matches MC scenario
  if( nPUMax != static_cast<unsigned int>(data_npu_estimated->GetNbinsX()) ) {
    std::cerr << "\n\nERROR number of bins (" << data_npu_estimated->GetNbinsX() << ") in data PU-profile does not match number of bins (" << nPUMax << ") in MC scenario " << toString(sc) << std::endl;
    throw std::exception();
  }
    
  if(v_npuProbs.size()!=nPUMax)
    std::cout << "PUWeight::generateWeights - Warning! Vector is has a size ("<<v_npuProbs.size()<<") different from the expected number "<<nPUMax<<"!\n";
  
  std::vector<double> result(nPUMax,0.);
  double s = 0.;
  for(unsigned int npu = 0; npu < nPUMax; ++npu) {
    const double npu_estimated = data_npu_estimated->GetBinContent(data_npu_estimated->GetXaxis()->FindBin(npu));
    result[npu] = npu_estimated / v_npuProbs[npu]; //npuProbs[npu];
    s += npu_estimated;
    //std::cout<<"  result["<<npu<<"] = npu_estimated / npuProbs["<<npu<<"]   = "<<npu_estimated<<" / "<<npuProbs[npu]<<" = "<<npu_estimated/npuProbs[npu]<<"\n";
    //std::cout<<"  result["<<npu<<"] = npu_estimated / v_npuProbs["<<npu<<"] = "<<npu_estimated<<" / "<<v_npuProbs[npu]<<" = "<<result[npu]<<", s="<<s<<"\n";
  }
  // normalize weights such that the total sum of weights over thw whole sample is 1.0, i.e., sum_i  result[i] * npu_probs[i] should be 1.0 (!)
  for(unsigned int npu = 0; npu < nPUMax; ++npu) {
    result[npu] /= s;
    std::cout<<"  result["<<npu<<"] = "<<result[npu]<<"\n"; 
  }
  
  return result;
}
