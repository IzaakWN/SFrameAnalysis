#ifndef ScaleFactorTau_h
#define ScaleFactorTau_h

#include "TROOT.h"
#include "TFile.h"
#include "TH1.h"
#include "TGraphAsymmErrors.h"
#include <iostream>
#include <map>
#include <cmath>
#include <string>





class ScaleFactorTau {
    // based on SFreader https://github.com/rmanzoni/triggerSF/blob/moriond17/getSF.py
    
	private: 
	std::map<std::string,TGraphAsymmErrors*> eff_data_fakeTau;
	std::map<std::string,TGraphAsymmErrors*> eff_data_realTau;
	std::map<std::string,TGraphAsymmErrors*> eff_mc_fakeTau;
	std::map<std::string,TGraphAsymmErrors*> eff_mc_realTau;
    
	//TH1D * etaBinsH;
    TGraphAsymmErrors* makeGraph(TGraphAsymmErrors*);
	void SetAxisBins(TGraphAsymmErrors*);
	bool check_SameBinning(TGraphAsymmErrors*, TGraphAsymmErrors*);
	std::string FindEtaLabel(std::map<std::string,TGraphAsymmErrors*> eff_map, double, int);
    int FindPtBin( std::map<std::string, TGraphAsymmErrors *>, std::string, double);
    
	public:
		ScaleFactorTau(){ };
		ScaleFactorTau(TString);
		~ ScaleFactorTau(){ };
		void init_ScaleFactor(TString);
		void getGraph(TFile*, std::map<std::string,TGraphAsymmErrors*>&, std::string, std::string);
		double get_EfficiencyData(double pt, double eta, int dm, bool isReal=true); //pt, eta
		double get_EfficiencyMC(  double pt, double eta, int dm, bool isReal=true);
		double get_ScaleFactor(   double pt, double eta, int dm, bool isReal=true);
        // double get_EfficiencyDataError(double, double);
        // double get_EfficiencyMCError(double, double);
        // double get_ScaleFactorError(double, double);
    
};


#endif


