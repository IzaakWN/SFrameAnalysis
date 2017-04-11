#include "../interface/ScaleFactorTau.h"



ScaleFactorTau::ScaleFactorTau(TString inputRootFile) {
    init_ScaleFactor(inputRootFile);
}



void ScaleFactorTau::init_ScaleFactor(TString inputRootFile){
	// TODO: pass isoLabel as variable
    
	TFile* fileIn = new TFile(inputRootFile, "read");
	// if root file not found
	if (fileIn->IsZombie() ) { std::cout << "ERROR in ScaleFactorTau::init_ScaleFactor(TString inputRootFile) from NTupleMaker/src/ScaleFactor.cc : ‎File " <<inputRootFile << " does not exist. Please check. " <<std::endl; exit(1); };
	
	std::string isoLabel = "LooseIso"; // HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v
	//std::string graphName;
	std::vector<std::string> etaLabels = {"endcap","barrel"};
    
    for(auto const& etaLabel: etaLabels){
      
      getGraph(fileIn,eff_data_realTau,etaLabel,"data_genuine_"+etaLabel+"_"+isoLabel);
      getGraph(fileIn,eff_data_fakeTau,etaLabel,"data_fake_"   +etaLabel+"_"+isoLabel);
      getGraph(fileIn,eff_mc_realTau,  etaLabel,"mc_genuine_"  +etaLabel+"_"+isoLabel);
      getGraph(fileIn,eff_mc_fakeTau,  etaLabel,"mc_fake_"     +etaLabel+"_"+isoLabel);
      
    }
    
    // for(auto const& label: eff_data_realTau)
    //   std::cout << "ScaleFactorTau::init_ScaleFactor: eff_data_realTau - eta label \"" << label.first << "\"" << std::endl;
    // std::cout << "ScaleFactorTau::init_ScaleFactor: eff_data_realTau.size() = " << eff_data_realTau.size() << std::endl;
    // for(auto const& label: eff_data_fakeTau)
    //   std::cout << "ScaleFactorTau::init_ScaleFactor: eff_data_fakeTau - eta label \"" << label.first << "\"" << std::endl;
    // std::cout << "ScaleFactorTau::init_ScaleFactor: eff_data_fakeTau.size() = " << eff_data_fakeTau.size() << std::endl;
    // for(auto const& label: eff_mc_realTau)
    //   std::cout << "ScaleFactorTau::init_ScaleFactor: eff_mc_realTau - eta label \"" << label.first << "\"" << std::endl;
    // std::cout << "ScaleFactorTau::init_ScaleFactor: eff_mc_realTau.size() = " << eff_mc_realTau.size() << std::endl;
    // for(auto const& label: eff_mc_fakeTau)
    //   std::cout << "ScaleFactorTau::init_ScaleFactor: eff_mc_fakeTau - eta label \"" << label.first << "\"" << std::endl;
    // std::cout << "ScaleFactorTau::init_ScaleFactor: eff_mc_fakeTau.size() = " << eff_mc_fakeTau.size() << std::endl;
	
	return;
}



void ScaleFactorTau::getGraph(TFile* fileIn, std::map<std::string,TGraphAsymmErrors*>& eff_map, std::string etaLabel0, std::string graphName0){
    
    bool foundGraph = false;
	std::string etaLabel = etaLabel0;
	std::string graphName = graphName0;
	std::vector<std::string> dmValues = {"0","1","10"};
    
    if (fileIn->GetListOfKeys()->Contains(TString(graphName))){
      eff_map[etaLabel] = makeGraph((TGraphAsymmErrors*)fileIn->Get(TString(graphName)));
      SetAxisBins(eff_map[etaLabel]);
      foundGraph = true;
      //std::cout << "ScaleFactorTau::getGraph: found \"" << graphName << "\" saved as \"" << etaLabel << "\"" << std::endl;
    }else{
      for(auto const& dm: dmValues){
        graphName = graphName0+"_dm"+dm;
        etaLabel  = etaLabel0 +"_dm"+dm;
        if (fileIn->GetListOfKeys()->Contains(TString(graphName))){
          eff_map[etaLabel] = makeGraph((TGraphAsymmErrors*)fileIn->Get(TString(graphName)));
          SetAxisBins(eff_map[etaLabel]);
          foundGraph = true;
          //std::cout << "ScaleFactorTau::getGraph: found \"" << graphName << "\" saved as \"" << etaLabel << "\"" << std::endl;
        }else{
          foundGraph = false;
          std::cout << "WARNING! ScaleFactorTau::getGraph: no \"" << etaLabel << "\" for \"" << graphName << "\"" << std::endl;
        }
      }
    }
    
    if(not foundGraph){
      std::cout << "WARNING! ScaleFactorTau::getGraph: no \"" << etaLabel0 << "\" for \"" << graphName0 << "\"" << std::endl;
      exit(1);
    }
    
    //for(auto const& label: eff_map)
    //  std::cout << "ScaleFactorTau::getGraph: eff_map - eta label \"" << label.first << "\"" << std::endl;
    //std::cout << "ScaleFactorTau::getGraph: eff_map.size() = " << eff_map.size() << std::endl;
    
}



TGraphAsymmErrors* ScaleFactorTau::makeGraph(TGraphAsymmErrors* graph){
    // make graph without empty bins
    // based on prepareGraph https://github.com/rmanzoni/triggerSF/blob/moriond17/getSF.py
    
	int N = graph->GetN();
	double ptBins[N+1]  = { };
	double effBins[N+1] = { };
	for (int i=0; i<N; i++){
	  ptBins[i]  = graph->GetX()[i];
	  effBins[i] = graph->GetY()[i];
	}
	
	// trim off zero values at the end of the pt spectrum
	int N_new = N;
	double eff_last = effBins[N_new-1];
	while( eff_last == 0. ){
	  N_new -= 1;
      eff_last = effBins[N_new-1];
	} 
	
	if ( N_new < 2 ){
      std::cout << "ERROR! ScaleFactorTau::makeGraph: graph only contains zero values " << std::endl; exit(1); }
    
	TGraphAsymmErrors* newgraph = new TGraphAsymmErrors(N_new, ptBins, effBins);
	return newgraph;
}



void ScaleFactorTau::SetAxisBins(TGraphAsymmErrors* graph) {
	int N = graph->GetN();
	double axisBins[N+1] = {};
	for (int i=0; i<N; i++) { axisBins[i] = (graph->GetX()[i] - graph->GetErrorXlow(i)); }
	axisBins[N] = (graph->GetX()[N-1] + graph->GetErrorXhigh(N-1));
	graph->GetXaxis()->Set(N, axisBins);
	return;
}



bool ScaleFactorTau::check_SameBinning(TGraphAsymmErrors* graph1, TGraphAsymmErrors* graph2){
	bool haveSameBins = false;
	int n1 = graph1->GetXaxis()->GetNbins();
	int n2 = graph2->GetXaxis()->GetNbins();
	//std::cout << "ScaleFactorTau::check_SameBinning: n1=" << n1 << ", n2=" << n2 << std::endl;
	if (n1 != n2 ) {return false;}
	else {
		haveSameBins = true;
		const int nbins = n1;
		double x1, x2;
		for (int i=0; i<nbins; i++){ 
			x1 = (graph1->GetXaxis()->GetXbins())->GetArray()[i];
			x2 = (graph2->GetXaxis()->GetXbins())->GetArray()[i]; 
			haveSameBins = haveSameBins and (x1 == x2) ;
		}
	}
    
	return haveSameBins;
}



std::string ScaleFactorTau::FindEtaLabel(std::map<std::string,TGraphAsymmErrors*> eff_map, double eta, int dm){
    
	std::string etaLabel;
	if(fabs(eta)<1.5) etaLabel = "barrel";
	else              etaLabel = "endcap";
	std::map<std::string, TGraphAsymmErrors*>::iterator it;
    
    // for(auto const& label: eff_map){
    //   std::cout << "ScaleFactorTau::FindEtaLabel: eta label \""<< label.first << "\"" << std::endl;
    // }
    
    it = eff_map.find(etaLabel); // look without dm
    if(it == eff_map.end()){     // otherwise look with dm
      switch(dm){
        case  0: etaLabel+="_dm0";  break;
        case  1: etaLabel+="_dm1";  break;
        case 10: etaLabel+="_dm10"; break;
      }
      it = eff_map.find(etaLabel); // look with dm (cpp.sh/3vxxr§)
      if(it == eff_map.end()){
        std::cout << "ERROR in ScaleFactorTau::FindEtaLabel: no object corresponding to eta label \""<< etaLabel << "\"" << std::endl; exit(1);
      }
	}
	
    return etaLabel;
}



int ScaleFactorTau::FindPtBin( std::map<std::string, TGraphAsymmErrors*> eff_map, std::string EtaLabel, double Pt){

    int Npoints = eff_map[EtaLabel]->GetN();
	double ptMAX = (eff_map[EtaLabel]->GetX()[Npoints-1])+(eff_map[EtaLabel]->GetErrorXhigh(Npoints-1));
	double ptMIN = (eff_map[EtaLabel]->GetX()[0])-(eff_map[EtaLabel]->GetErrorXlow(0));
	// if pt is overflow, return last pt bin
 	if (Pt >= ptMAX ) return Npoints; 
	// if pt is underflow, return nonsense number and warning
	else if (Pt < ptMIN){
 	  std::cout<< "WARNING in ScaleFactorTau::FindPtBin: pT too low (pt = " << Pt << "), min value is " << ptMIN << ". Returned efficiency =1. Weight will be 1. " << std::endl;
	  return -99;}
	// if pt is in range
	else {return eff_map[EtaLabel]->GetXaxis()->FindFixBin(Pt);} 
}



double ScaleFactorTau::get_EfficiencyData(double pt, double eta, int dm, bool isReal){
    
    double eff;
    std::map<std::string, TGraphAsymmErrors*> eff_map;
    if (isReal) eff_map = eff_data_realTau;
    else        eff_map = eff_data_fakeTau;
	std::string label = FindEtaLabel(eff_map,eta,dm);
    
	int ptbin = FindPtBin(eff_map, label, pt); 
	if (ptbin == -99){eff =1;} // if pt is underflow 
	else eff = eff_map[label]->GetY()[ptbin-1];
    
	if (eff>1.){std::cout << "WARNING in ScaleFactorTau::get_EfficiencyData: Efficiency in data > 1. Set eff = 1."      << std::endl; eff=1.;} 
	if (eff<0.){std::cout << "WARNING in ScaleFactorTau::get_EfficiencyData: Negative efficiency in data. Set eff = 0." << std::endl; eff=0.;}

	return eff;
	
}


double ScaleFactorTau::get_EfficiencyMC(double pt, double eta, int dm, bool isReal) {

	double eff;
    std::map<std::string, TGraphAsymmErrors*> eff_map;
    if (isReal) eff_map = eff_mc_realTau;
    else        eff_map = eff_mc_fakeTau;
	std::string label = FindEtaLabel(eff_map,eta,dm);

	int ptbin = FindPtBin(eff_map, label, pt); 
	if (ptbin == -99){eff =1;} // if pt is underflow 
	else eff = eff_map[label]->GetY()[ptbin-1];

	if (eff>1.){std::cout << "WARNING in ScaleFactorTau::get_EfficiencyMC: Efficiency in MC > 1. Set eff = 1."      << std::endl; eff=1.;} 		
	if (eff<0.){std::cout << "WARNING in ScaleFactorTau::get_EfficiencyMC: Negative efficiency in MC. Set eff = 0." << std::endl; eff=0.;}

	return eff;

}



double ScaleFactorTau::get_ScaleFactor(double pt, double eta, int dm, bool isReal){
	
	double efficiency_data = get_EfficiencyData(pt,eta,dm,isReal);
	double efficiency_mc = get_EfficiencyMC(pt,eta,dm,isReal);
	double SF;
    
	if(efficiency_mc!=0){ SF = efficiency_data/efficiency_mc; }
	else{
	  SF=0.; std::cout << "WARNING in ScaleFactorTau::get_ScaleFactor: MC efficiency = 0. Scale Factor set to 0.";
	}
    
	return SF;
}



// double ScaleFactorTau::get_EfficiencyDataError(double pt, double eta){
// 
// 	double eff_error;
// 	std::string label = FindEtaLabel(eta,"data");
// 	int ptbin = FindPtBin(eff_data, label, pt); 
// 	if (ptbin == -99){eff_error =0.;} // if pt is underflow 
// 	else eff_error= eff_data[label]->GetErrorYhigh(ptbin-1); 
//         // errors are supposed to be symmetric, can use GetErrorYhigh or GetErrorYlow
// 
// 	double effData = get_EfficiencyData(pt,eta);
// 	if (eff_error > effData) eff_error = 0.5*effData;
// 	return eff_error;
// }
// 	
// 	
// 
// double ScaleFactorTau::get_EfficiencyMCError(double pt, double eta){
// 
// 	double eff_error;
// 	std::string label = FindEtaLabel(eta,"mc");
// 	int ptbin = FindPtBin(eff_mc, label, pt); 
// 	if (ptbin == -99){eff_error =0.;} // if pt is underflow 
// 	else eff_error= eff_mc[label]->GetErrorYhigh(ptbin-1); 
// 	// errors are supposed to be symmetric, can use GetErrorYhigh or GetErrorYlow
// 
// 	double effMC = get_EfficiencyMC(pt,eta);
// 	if (eff_error > effMC ) eff_error = 0.5*effMC;
// 	return eff_error;
// }
// 
// 
// 
// double ScaleFactorTau::get_ScaleFactorError(double pt, double eta){
// 
// 	double SF_error = 0.;
// 	
// 	double effData = get_EfficiencyData(pt, eta);
// 	double effMC = get_EfficiencyMC(pt, eta);
// 	double errData = get_EfficiencyDataError(pt, eta);
// 	double errMC =  get_EfficiencyMCError(pt, eta);
// 
// 	if (errData == 0) {std::cout<<"WARNING in ScaleFactorTau::get_ScaleFactorError(double pt, double eta) from LepEffInterface/src/ScaleFactor.cc: uncertainty on data point = 0, can not calculate uncertainty on scale factor. Uncertainty set to 0." << std::endl;}
// 	if (errMC == 0)   {std::cout<<"WARNING in ScaleFactorTau::get_ScaleFactorError(double pt, double eta) from LepEffInterface/src/ScaleFactor.cc: uncertainty on MC = 0, can not calculate uncerttainty on scale factor. Uncertainty set to 0." << std::endl;}
// 	if (effData == 0) {std::cout<<"WARNING in ScaleFactorTau::get_ScaleFactorError(double pt, double eta) from LepEffInterface/src/ScaleFactor.cc: efficiency in data = 0, can not calculate uncertainty on scale factor. Uncertainty set to 0." << std::endl;}
// 	if (effMC == 0)   {std::cout<<"WARNING in ScaleFactorTau::get_ScaleFactorError(double pt, double eta) from LepEffInterface/src/ScaleFactor.cc: efficiency in MC = 0, can not calculate uncertainty on scale factor. Uncertainty set to 0." << std::endl;}
// 	else {	
// 	SF_error = pow((errData/effData),2) + pow((errMC/effMC),2);
// 	SF_error = pow(SF_error, 0.5)*(effData/effMC);
// 	}
// 	return SF_error;
// }
	

