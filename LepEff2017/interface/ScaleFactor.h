#ifndef ScaleFactor_h
#define ScaleFactor_h

#include <iostream>
#include <map>
#include <cmath>
#include <string>
#include "TROOT.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TGraphAsymmErrors.h"



class ScaleFactor {

  private: 
    //std::map<std::string, TGraphAsymmErrors *> eff_data;
    //std::map<std::string, TGraphAsymmErrors *> eff_mc;
    
    //TH1D* etaBinsH;
    std::string m_rootFile;
    std::string m_histName;
    TH2F* m_eta_pt_ratio;
    
    //void  SetAxisBins(TGraphAsymmErrors*);
    //bool  check_SameBinning(TGraphAsymmErrors*, TGraphAsymmErrors*);
    //std::string FindEtaLabel(double, std::string);
    //int FindPtBin( std::map<std::string, TGraphAsymmErrors *>, std::string, double);
  
  public:
    ScaleFactor(){};
    ScaleFactor(TString file, TString hist, bool abseta=false);
    ~ ScaleFactor(){};
    void init_ScaleFactor(TString file, TString hist);
    //void init_ScaleFactor(TString,std::string);
    //double get_EfficiencyData(     double, double); //pt, eta
    //double get_EfficiencyMC(       double, double);
    float get_ScaleFactor( double pt, double eta); 
    //double get_EfficiencyDataError(double, double);
    //double get_EfficiencyMCError(  double, double);
    //double get_ScaleFactorError(   double, double);
    void checkEtaPtAxes(TH2F* eta_pt_hist);
    bool m_abseta;

};


#endif


