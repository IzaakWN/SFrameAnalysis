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
    std::string m_inputRootFile;
    TH2D* pt_abseta_ratio;
    
    //void  SetAxisBins(TGraphAsymmErrors*);
    //bool  check_SameBinning(TGraphAsymmErrors*, TGraphAsymmErrors*);
    //std::string FindEtaLabel(double, std::string);
    //int FindPtBin( std::map<std::string, TGraphAsymmErrors *>, std::string, double);
  
  public:
    ScaleFactor(){};
    ScaleFactor(TString file);
    ~ ScaleFactor(){};
    void init_ScaleFactor(TString file);
    //void init_ScaleFactor(TString,std::string);
    //double get_EfficiencyData(     double, double); //pt, eta
    //double get_EfficiencyMC(       double, double);
    float get_ScaleFactor( double pt, double eta); 
    //double get_EfficiencyDataError(double, double);
    //double get_EfficiencyMCError(  double, double);
    //double get_ScaleFactorError(   double, double);

};


#endif


