#ifndef ScaleFactorJSON_h
#define ScaleFactorJSON_h

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <map>
#include <cmath>
#include <string>
#include <regex>
#include "../interface/json.h"
#include "TH1.h"
#include "TH2.h"
#include "TAxis.h"


class ScaleFactorJSON {

  private: 
    //std::map<std::string, TGraphAsymmErrors *> eff_data;
    //std::map<std::string, TGraphAsymmErrors *> eff_mc;
    
    //TH1D* etaBinsH;
    std::string m_jsonFileName;
    TString m_jsonWP;
    TH2F* pt_abseta_ratio;
    Float_t* getBins(const Json::Value map);
    void getBins(const Json::Value map, Float_t* bins, Int_t nBins);
    void fillPtEtaHist(const Json::Value map); //TH2F* pt_abseta_ratio
    Float_t* getRangeFromKey(std::string key);
    
  public:
    ScaleFactorJSON(){};
    ScaleFactorJSON(TString file, TString WP = "");
    ~ ScaleFactorJSON(){};
    void init_ScaleFactor(TString file, TString WP = "");
    float get_ScaleFactor( double pt, double eta);

};


#endif


