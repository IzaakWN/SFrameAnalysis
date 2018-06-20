#include "../interface/ScaleFactorJSON.h"
// http://jsoncpp.sourceforge.net/old.html


ScaleFactorJSON::ScaleFactorJSON(TString jsonFileName, TString jsonWP) {
    
    // Expand $SFRAME_DIR
    std::string match = "$SFRAME_DIR";
    std::string replacement = std::getenv("SFRAME_DIR");
    jsonFileName.Replace(0,match.length(),replacement);
    
    m_jsonFileName = jsonFileName;
    m_jsonWP       = jsonWP;
    init_ScaleFactor(jsonFileName,jsonWP);
}


void ScaleFactorJSON::init_ScaleFactor(TString jsonFileName, TString jsonWP){
    
    Json::Value WPmap;
    //Json::Reader reader;
    //bool parsingSuccessful = reader.parse( jsonFileName.Data(), WPmap );
    //if(!parsingSuccessful){
    //  std::cout << "ERROR! ScaleFactorJSON::init_ScaleFactor: Failed to parse JSON file\n" << reader.getFormattedErrorMessages();
    //  exit(1);
    //}
    std::ifstream jsonFile(jsonFileName, std::ifstream::binary);
    jsonFile >> WPmap;
    Json::Value etaPtMap = WPmap[jsonWP]["abseta_pt"];
    fillPtEtaHist(etaPtMap);
    jsonFile.close();
}


void ScaleFactorJSON::fillPtEtaHist(const Json::Value etaPtMap){
    //std::cout << "fillPtEtaHist" << std::endl;
    
    // CREATE histogram
    Json::ValueConstIterator it0 = etaPtMap.begin();
    Json::Value firstPtMap = etaPtMap[it0.key().asString()];
    Int_t nEtaBins   = etaPtMap.size();
    Int_t nPtBins    = firstPtMap.size();
    Float_t* etaBins = getBins(etaPtMap);
    Float_t* ptBins  = getBins(firstPtMap);
    pt_abseta_ratio  = new TH2F(m_jsonWP,"pt vs. eta ratio",nPtBins,ptBins,nEtaBins,etaBins);
    
    //std::cout << "etaBins:";
    //for(int i=0; i<nEtaBins+1; i++)
    //  std::cout << " "<<etaBins[i];
    //std::cout << std::endl;
    //std::cout << "ptBins:";
    //for(int i=0; i<nPtBins+1; i++)
    //  std::cout << " "<<ptBins[i];
    //std::cout << std::endl;
    
    // MAP keys to bins, and check consistency
    std::map<std::string,Int_t> etaBinMap;
    std::map<std::string,Int_t> ptBinMap;
    int i = 0;
    for( auto it1=etaPtMap.begin(); it1!=etaPtMap.end(); it1++ ){
      std::string etaKey = it1.key().asString();
      const Json::Value etaMap = etaPtMap[etaKey];
      Float_t* etaRange = getRangeFromKey(etaKey);
      Int_t etaBin = pt_abseta_ratio->GetYaxis()->FindBin(etaRange[0]);
      //std::cout << "etaKey " << etaKey << " has bin " << etaBin << std::endl;
      etaBinMap[etaKey] = etaBin;
      for( auto it2=etaMap.begin(); it2!=etaMap.end(); it2++ ){
        std::string ptKey = it2.key().asString();   
        //const Json::Value ptMap = etaMap[ptKey];
        Float_t* ptRange = getRangeFromKey(ptKey);
        Int_t ptBin = pt_abseta_ratio->GetXaxis()->FindBin(ptRange[0]);
        //std::cout << "  ptKey " << ptKey << " has bin " << ptBin << std::endl;
        if(i==0){
          ptBinMap[ptKey] = ptBin;
        }else if(ptBinMap.count(ptKey)==0){
          std::cout << "ERROR! ScaleFactorJSON::fillPtEtaHist: different pt binnings! See "<<ptKey<<std::endl;
          exit(1);
        }
      }
      i++;
    }
    
    // FILL histogram
    for( auto it1=etaPtMap.begin(); it1!=etaPtMap.end(); it1++ ){
      std::string etaKey = it1.key().asString();
      const Json::Value etaMap = etaPtMap[etaKey];
      Int_t biny = etaBinMap[etaKey];
      
      for( auto it2=etaMap.begin(); it2!=etaMap.end(); it2++ ){
        std::string ptKey = it2.key().asString();   
        const Json::Value ptMap = etaMap[ptKey];
        Int_t binx = ptBinMap[ptKey];
        Float_t value = ptMap["value"].asFloat();
        Float_t error = ptMap["error"].asFloat();
        //std::cout << "  "<<etaKey<<", "<<ptKey<<": (binx,biny)=("<<binx<<","<<biny
        //                 <<") gets filled with (value,error)=("<<value<<","<<error<<")"<< std::endl;
        pt_abseta_ratio->SetBinContent(binx,biny,value);
        pt_abseta_ratio->SetBinError(binx,biny,error);
      }
    }
    
    return;
}


Float_t* ScaleFactorJSON::getBins(const Json::Value map){ //, Float_t* bins, Int_t nBins){
    //std::cout << "getBins" << std::endl;
    int nBins = map.size()+1;
    static Float_t* bins; bins = (Float_t*) malloc(nBins*sizeof(int));
    int i = 0;
    Float_t maxBin = -9999;
    for( auto it=map.begin(); it!=map.end(); it++ ){
      std::string key = it.key().asString();
      //std::cout << "  key " << it.key() << std::endl;
      Float_t* range = getRangeFromKey(key);
      bins[i] = range[0];
      if(range[1]>maxBin) maxBin = range[1];
      i++;
    }
    bins[nBins-1] = maxBin;
    std::sort(bins,bins+nBins);
    //std::cout << "bins:";
    //for(int i=0; i<nBins; i++)
    //  std::cout << " "<<bins[i];
    //std::cout << std::endl;
    return bins;
}


Float_t* ScaleFactorJSON::getRangeFromKey(std::string key){
    //std::cout << "getBins" << std::endl;
    static Float_t bins[2]; //bins = (Float_t*) malloc(2*sizeof(int));
    std::string pattern = "([0-9]+\\.?[0-9]*),([0-9]+\\.?[0-9]*)";
    std::regex expr(pattern);
    std::smatch smatch;
    std::regex_search(key,smatch,expr);
    //std::cout << "match: ";
    //for(auto m: smatch)
    //  std::cout << " "<<m;
    //std::cout << std::endl;
    if(smatch.size()<2){
      std::cout << "Warning! Did not find enough values in key "<<key<<"!" << std::endl;
      exit(1);
    }
    std::stringstream stream1(smatch[1]);
    std::stringstream stream2(smatch[2]);
    stream1 >> bins[0];
    stream2 >> bins[1];
    return bins;
}


float ScaleFactorJSON::get_ScaleFactor(double pt, double eta){
	int binPt  = pt_abseta_ratio->GetXaxis()->FindBin(pt);
	int binEta = pt_abseta_ratio->GetYaxis()->FindBin(fabs(eta));
    
	if(binPt==0) binPt=1;
	else if(binPt>pt_abseta_ratio->GetXaxis()->GetNbins()) binPt--;
	if(binEta==0) binEta=1;
	else if(binEta>pt_abseta_ratio->GetYaxis()->GetNbins()) binEta--;
    
	float SF   = pt_abseta_ratio->GetBinContent(binPt,binEta);
	//std::cout << "ScaleFactor::get_ScaleFactor: (pt,eta)=("<<pt<<","<<eta
	//          <<"), (binPt,binEta)=("<<binPt<<","<<binEta<<") SF="<<SF<<std::endl;
	return SF;
}


