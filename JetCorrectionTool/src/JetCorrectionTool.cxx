#include "../interface/JetCorrectionTool.h"
#include <cstdlib>
#include <fstream>
#include <limits>
#include <TFile.h>
#include "../src/EnergyScaleCorrection_class.cc"
//#include "../TauTauResonances/include/TauTauAnalysis.h" // for printRow



JetCorrectionTool::JetCorrectionTool(SCycleBase* parent, const char* name ): SToolBase( parent ), m_name( name ) {
  SetLogName( name );
  
  // Electrons
  DeclareProperty( m_name+"_CorrectionFileName",     m_CorrectionFileName     = "$SFRAME_DIR/../JetCorrectionTool/data/Electron/ScalesSmearings/Winter_2016_reReco_v1_ele" );
  
  // Jet
  DeclareProperty( m_name+"_JetResFileName",         m_JetResFileName         = "$SFRAME_DIR/../JetCorrectionTool/data/Jet/Spring16_25nsV10_MC_SF_AK8PFchs.txt" );
  DeclareProperty( m_name+"_JetResFileNameAK4",      m_JetResFileNameAK4      = "$SFRAME_DIR/../JetCorrectionTool/data/Jet/Spring16_25nsV10_MC_SF_AK4PFchs.txt" );
  
  // Mass
  //DeclareProperty(  m_name+"_MassFileName", m_MassFileName = std::string (std::getenv("SFRAME_DIR")) + "/../CorrectionTool/data/Mass/puppiCorr.root" );
  //DeclareProperty(  m_name+"_MassGenHistName", m_MassGenHistName = "puppiJECcorr_gen" );
  //DeclareProperty(  m_name+"_MassBarrelHistName", m_MassBarrelHistName = "puppiJECcorr_reco_0eta1v3" );
  //DeclareProperty(  m_name+"_MassEndcapHistName", m_MassEndcapHistName = "puppiJECcorr_reco_1v3eta2v5" );
  DeclareProperty( m_name+"_MassGenFileName",        m_MassGenFileName        = "$SFRAME_DIR/../JetCorrectionTool/data/Mass/genCorr.root" );
  DeclareProperty( m_name+"_MassGenBarrelHistName",  m_MassGenBarrelHistName  = "gC_forCorr" );
  DeclareProperty( m_name+"_MassGenEndcapHistName",  m_MassGenEndcapHistName  = "gF_forCorr" );
  DeclareProperty( m_name+"_MassRecoFileName",       m_MassRecoFileName       = "$SFRAME_DIR/../JetCorrectionTool/data/Mass/recoCorr.root" );
  DeclareProperty( m_name+"_MassRecoBarrelHistName", m_MassRecoBarrelHistName = "gC_forCorr" );
  DeclareProperty( m_name+"_MassRecoEndcapHistName", m_MassRecoEndcapHistName = "gF_forCorr" );
  DeclareProperty( m_name+"_MassResFileName",        m_MassResFileName        = "$SFRAME_DIR/../JetCorrectionTool/data/Mass/puppiSoftdropResol.root" );
  DeclareProperty( m_name+"_MassResBarrelHistName",  m_MassResBarrelHistName  = "massResolution_0eta1v3" );
  DeclareProperty( m_name+"_MassResEndcapHistName",  m_MassResEndcapHistName  = "massResolution_1v3eta2v5" );
}



JetCorrectionTool::~JetCorrectionTool() {
  delete trandom;
  delete eScaler;
}



void JetCorrectionTool::BeginInputData( const SInputData& ) throw( SError ) {

  // Electrons
  m_logger << INFO << SLogger::endmsg;
  m_logger << INFO << "CorrectionFileName:      " << m_CorrectionFileName     << SLogger::endmsg;
  
  // Jets
  m_logger << INFO << "JetResFileName:          " << m_JetResFileName         << SLogger::endmsg;
  m_logger << INFO << "JetResFileName AK4:      " << m_JetResFileNameAK4      << SLogger::endmsg;
  
  // Mass
  m_logger << INFO << "MassGenFileName:         " << m_MassGenFileName        << SLogger::endmsg;
  m_logger << INFO << "MassGenBarrelHistName:   " << m_MassGenBarrelHistName  << SLogger::endmsg;
  m_logger << INFO << "MassGenEndcapHistName:   " << m_MassGenEndcapHistName  << SLogger::endmsg;
  m_logger << INFO << "MassRecoFileName:        " << m_MassRecoFileName       << SLogger::endmsg;
  m_logger << INFO << "MassRecoBarrelHistName:  " << m_MassRecoBarrelHistName << SLogger::endmsg;
  m_logger << INFO << "MassRecoEndcapHistName:  " << m_MassRecoEndcapHistName << SLogger::endmsg;
  m_logger << INFO << "MassResFileName:         " << m_MassResFileName        << SLogger::endmsg;
  m_logger << INFO << "MassResBarrelHistName:   " << m_MassResBarrelHistName  << SLogger::endmsg;
  m_logger << INFO << "MassResEndcapHistName:   " << m_MassResEndcapHistName  << SLogger::endmsg;
  
  // Expand $SFRAME_DIR
  std::string match = "$SFRAME_DIR";
  std::string replacement = std::getenv("SFRAME_DIR");
  m_CorrectionFileName.replace(0,match.length(),replacement);
  m_JetResFileName.replace(    0,match.length(),replacement);
  m_JetResFileNameAK4.replace( 0,match.length(),replacement);
  
  
  // ********** Open files **********
  
  // Jets
  std::ifstream JetResFile(m_JetResFileName);
  std::string line;
  getline(JetResFile, line);
  float minEta, maxEta, none, res, resDown, resUp;
  while(JetResFile >> minEta >> maxEta >> none >> res >> resDown >> resUp) {
      float* array = new float[6]{minEta, maxEta, none, res, resDown, resUp};
      JetRes.push_back(array);
  }
  m_logger << VERBOSE << "JetResFile opened, found " << JetRes.size() << " lines" << SLogger::endmsg;
  // Jets Ak4
  std::ifstream JetResFileAK4(m_JetResFileNameAK4);
  std::string lineak4;
  getline(JetResFileAK4, lineak4);
  float minEtaak4, maxEtaak4, noneak4, resak4, resDownak4, resUpak4;
  while(JetResFileAK4 >> minEtaak4 >> maxEtaak4 >> noneak4 >> resak4 >> resDownak4 >> resUpak4) {
      float* arrayAK4 = new float[6]{minEtaak4, maxEtaak4, noneak4, resak4, resDownak4, resUpak4};
      JetResAK4.push_back(arrayAK4);
  }
  m_logger << VERBOSE << "JetResFile AK4 opened, found " << JetResAK4.size() << " lines" << SLogger::endmsg;
  
  // Gen
  auto MassGenFile = TFile::Open(m_MassGenFileName.c_str(), "READ");
  if(MassGenFile) {
      MassGenBarrel = (TGraph*)MassGenFile->Get(m_MassGenBarrelHistName.c_str());
      MassGenEndcap = (TGraph*)MassGenFile->Get(m_MassGenEndcapHistName.c_str());
      //MassGenBarrel->SetDirectory(0);
      //MassGenEndcap->SetDirectory(0);
      MassGenFile->Close();
  }
  else m_logger << WARNING << "‎File " << m_MassGenFileName << " does not exist. Please check." << SLogger::endmsg;
  m_logger << VERBOSE << "MassGenFile opened" << SLogger::endmsg;
  
  // Reco
  auto MassRecoFile = TFile::Open(m_MassRecoFileName.c_str(), "READ");
  if(MassRecoFile) {
      MassRecoBarrel = (TGraph*)MassRecoFile->Get(m_MassRecoBarrelHistName.c_str());
      MassRecoEndcap = (TGraph*)MassRecoFile->Get(m_MassRecoEndcapHistName.c_str());
      //MassRecoBarrel->SetDirectory(0);
      //MassrecoEndcap->SetDirectory(0);
      MassRecoFile->Close();
  }
  else m_logger << WARNING << "‎File " << m_MassRecoFileName << " does not exist. Please check." << SLogger::endmsg;
  m_logger << VERBOSE << "MassRecoFile opened" << SLogger::endmsg;
  
  // Mass resolution
  auto MassResFile = TFile::Open(m_MassResFileName.c_str(), "READ");
  if(MassResFile) {
      MassResBarrel = (TF1*)MassResFile->Get(m_MassResBarrelHistName.c_str());
      MassResEndcap = (TF1*)MassResFile->Get(m_MassResEndcapHistName.c_str());
      //MassGen->SetDirectory(0);
      //MassBarrel->SetDirectory(0);
      //MassEndcap->SetDirectory(0);
      MassResFile->Close();
  }
  else m_logger << WARNING << "‎File " << m_MassResFileName << " does not exist. Please check." << SLogger::endmsg;
  m_logger << VERBOSE << "MassResFile opened" << SLogger::endmsg;
  
  trandom = new TRandom3();
  
  eScaler = new EnergyScaleCorrection_class(m_CorrectionFileName);
  eScaler->doScale = true;
  eScaler->doSmearings = true;
  
  return;
}



// Electron
double JetCorrectionTool::GetCorrectedEnergy(double energy, bool isMC, int runNumber, bool isEBEle, double R9Ele, double etaSCEle, double EtEle) {
    
    double scale_corr(1.), sigma(1.), Ecorr(1.);
    
    // Scale the Data
    if(!isMC) {
        scale_corr = eScaler->ScaleCorrection(runNumber, isEBEle, R9Ele, etaSCEle, EtEle);
        //At this point, the new data energy will be:
        energy = energy * scale_corr;
    }

    // Smear the MC
    if(isMC) {
        sigma = eScaler->getSmearingSigma(runNumber, isEBEle, R9Ele, etaSCEle, EtEle, 0, 0);
        //Put the last two inputs at 0,0 for the nominal value of sigma
        //Now smear the MC energy
        energy = energy * trandom->Gaus(1, sigma);
    }
    
    // Slew rate
    if(!isMC && isEBEle) {
        if(energy > 200 && energy <= 300)  Ecorr = 1.0199;
        else if(energy > 300 && energy <= 400) Ecorr = 1.052;
        else if(energy > 400 && energy <= 500) Ecorr = 1.015;
        energy = energy * Ecorr;
    }
    
    return energy;
}



// Jet
// JER form here:  https://github.com/cms-jet/JERDatabase
TLorentzVector JetCorrectionTool::GetCorrectedJet(TLorentzVector jet, float jec, float jecUp, float jecDown, int sigmaScale, int sigmaRes, bool is_ak8) {
  //std::cout<< "JetCorrectionTool::GetCorrectedJet"<< std::endl;
  if(!(jet.Pt() > 0.)) return jet;
  if (is_ak8){
    //if(sigmaRes !=0) {
    //std::cout <<"ak8"<< std::endl;
    float eta( jet.Eta() );
    int etaBin(-1);
    for(unsigned int i=0; i<JetRes.size()-1; i++) if(eta > JetRes[i][0] && eta < JetRes[i+1][1]) etaBin = i;
    if(etaBin < 0) {
      m_logger << WARNING << "Eta bin not found for jet with eta = " << eta << SLogger::endmsg;
      return jet;
    }
    
    if (sigmaRes!=0){
      //std::cout <<"jet pt "<< jet.Pt()<< " sigmaRes "<< sigmaRes <<std::endl;
      float res(JetRes[etaBin][3]), resUp(JetRes[etaBin][5]-JetRes[etaBin][3]),
                                    resDown(JetRes[etaBin][3]-JetRes[etaBin][4]);
      // https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution
      float jer2(res + sigmaRes*(sigmaRes > 0 ? resUp : resDown));
      //std::cout <<"1) jer2 "<< jer2 <<std::endl;

      jer2 = std::max(jer2, float(1.)); // truncated to 0
      //    float jer2(sigmaRes > 0 ? resUp : resDown);
      //std::cout <<"2) jer2 "<< jer2 <<std::endl;
      float coeff = trandom->Gaus( 1., sqrt(jer2*jer2-1.)*(res-1.));
      //std::cout <<"coeff "<< jer2 <<std::endl;


      jet *= coeff;
      //}
    }
    
    if(sigmaScale > 0){
      //    std::cout <<"jet pt "<< jet.Pt()<<std::endl;
      jet *= jecUp/jec;
      //std::cout <<"jec up jet pt : "<< jet.Pt()<< " jec UP "<<  "  "<< jecUp<<std::endl;
    }
    if(sigmaScale < 0){
      //std::cout <<"jec down jet pt :jec DoWN "<< jet.Pt() <<""<<jecDown <<std::endl;
      jet *= jecDown/jec;
    }
  
  }else{
    //std::cout<< "ak4"<< std::endl;
    float eta( jet.Eta() );
    int etaBin(-1);
    for(unsigned int i=0; i<JetResAK4.size()-1; i++) if(eta > JetResAK4[i][0] && eta < JetResAK4[i+1][1]) etaBin = i;
    if(etaBin < 0) {
        m_logger << WARNING << "Eta bin not found for jet with eta = " << eta << SLogger::endmsg;
        return jet;
    }
    if (sigmaRes!=0){
      float res(JetResAK4[etaBin][3]), resUp(JetResAK4[etaBin][5]-JetResAK4[etaBin][3]),
                                       resDown(JetResAK4[etaBin][3]-JetResAK4[etaBin][4]);
      float jer2(res + sigmaRes*(sigmaRes > 0 ? resUp : resDown));
      jer2 = std::max(jer2, float(1.)); // truncated to 0
      float coeff = trandom->Gaus( 1., sqrt(jer2*jer2-1.)*(res-1.));
      jet *= coeff;
    }
    if (sigmaScale > 0){
      //    std::cout <<"Initial jet.pt()  " << jet.Pt() << std::endl;
      jet *= jecUp/jec;
      //std::cout <<" Final jec up jet pt : "<< jet.Pt()<< " jecUP "<< jecUp << " jec " << jec <<  std::endl;
      //    std::cout <<"jet. eta() " <<jet.Eta() << std::endl;
    }
    if(sigmaScale < 0) jet *= jecDown/jec;
  }
  return jet;
}



std::vector<TLorentzVector> JetCorrectionTool::GetCorrectedJet(const UZH::Jet& jet, int sigmaRes, bool is_ak8) {
  //std::cout<< "JetCorrectionTool::GetCorrectedJet"<< std::endl;
  if(!(jet.pt() > 0.)) return {jet.tlv(),jet.tlv()};
  
  TLorentzVector jet_tlv_jesUp;
  TLorentzVector jet_tlv_jesDown;
  jet_tlv_jesUp.SetPtEtaPhiE(  jet.pt(), jet.eta(), jet.phi(), jet.e());
  jet_tlv_jesDown.SetPtEtaPhiE(jet.pt(), jet.eta(), jet.phi(), jet.e());
  
  float eta = jet.eta();
  int etaBin = -1;
  
  if (sigmaRes!=0){
    
    std::vector<float*> JetRes0;
    if (is_ak8) JetRes0 = JetRes;
    else        JetRes0 = JetResAK4;
    
    std::cout<< "JetCorrectionTool::GetCorrectedJet: ak8"<< std::endl;
    for(unsigned int i=0; i<JetRes0.size()-1; i++) if(eta > JetRes0[i][0] && eta < JetRes0[i+1][1]) etaBin = i;
    if(etaBin < 0) {
      m_logger << WARNING << "Eta bin not found for jet with eta = " << eta << SLogger::endmsg;
      return {jet.tlv(),jet.tlv()};
    }
    float res(JetRes0[etaBin][3]), resUp(  JetRes0[etaBin][5]-JetRes0[etaBin][3]),
                                   resDown(JetRes0[etaBin][3]-JetRes0[etaBin][4]);
    float jer2_Up(std::max(res+sigmaRes*resUp,float(1.))), jer2_Down(std::max(res+sigmaRes*resDown,float(1.)));
    jet_tlv_jesUp   *= trandom->Gaus(1., sqrt(jer2_Up  *jer2_Up  -1.)*(res-1.));
    jet_tlv_jesDown *= trandom->Gaus(1., sqrt(jer2_Down*jer2_Down-1.)*(res-1.));
  }
  
  //std::cout <<"jet pt "<< jet.Pt()<<std::endl;
  jet_tlv_jesUp   *= jet.jecUp()/jet.jec();
  jet_tlv_jesDown *= jet.jecDown()/jet.jec();
  //std::cout <<"jec up jet pt : "<< jet.Pt()<< " jec UP "<<  "  "<< jecUp<<std::endl;
  //std::cout <<"jec down jet pt :jec DoWN "<< jet.Pt() <<""<<jecDown <<std::endl;
  
  return {jet_tlv_jesUp,jet_tlv_jesDown};
}



TLorentzVector JetCorrectionTool::GetCorrectedJetJER( TLorentzVector jet,TLorentzVector genJet, float jer, float jerUp, float jerDown, int sigmaRes, bool isGenJetMatched, double random ) {
  //std::cout<< "JetCorrectionTool::GetCorrectedJetJER"<< std::endl;
  if(!(jet.Pt() > 0.)) return jet;
  //std::cout <<"Initial jet.pt()  " << jet.Pt() << " gen jet pt " << genJet.Pt() << std::endl;
  double jer_sf=1;
  if (sigmaRes==0) jer_sf=jer;
  if (sigmaRes >0) jer_sf=jerUp;
  if (sigmaRes<0)  jer_sf=jerDown;
 
  double smearFactor=1.;
  if (isGenJetMatched){
    double dPt = jet.Pt() - genJet.Pt();
    smearFactor = 1 + (jer_sf - 1.) * dPt / jet.Pt();
    jet *= smearFactor;
  }else if (jer_sf>1){
    smearFactor = 1. + random * std::sqrt(jer_sf * jer_sf - 1); //trandom->Gaus(0.,sigma)
    jet *= smearFactor;
  }
  else std::cout << "Warning! JetCorrectionTool::GetCorrectedJetJER: no match and SF = " << jer_sf << " <= 1 !" << std::endl;

  // std::cout <<"Initial jet.pt()  " << jet.Pt() << " smearFactor "<<smearFactor << std::endl;
    /* 
   }else{
   //std::cout<< "ak4"<< std::endl;
   float eta( jet.Eta() );
   int etaBin(-1);
   for(unsigned int i=0; i<JetResAK4.size()-1; i++) if(eta > JetResAK4[i][0] && eta < JetResAK4[i+1][1]) etaBin = i;
   if(etaBin < 0) {
   m_logger << WARNING << "Eta bin not found for jet with eta = " << eta << SLogger::endmsg;
   return jet;
    }
    
    //    std::cout <<"Initial jet.pt()  " << jet.Pt() << std::endl;
    float res(JetResAK4[etaBin][3]), resUp(JetResAK4[etaBin][5]-JetResAK4[etaBin][3]), resDown(JetResAK4[etaBin][3]-JetResAK4[etaBin][4]);
    // https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution
    float jer2(res + sigmaRes*(sigmaRes > 0 ? resUp : resDown));
    jer2 = std::max(jer2, float(1.)); // truncated to 0
    //    float jer2(sigmaRes > 0 ? resUp : resDown);
    float coeff = trandom->Gaus( 1., sqrt(jer2*jer2-1.)*(res-1.));
    jet *= coeff;
    //}
    }
    */
  
  return jet;
}



TLorentzVector JetCorrectionTool::GetCorrectedJetJER(const UZH::Jet& jet, const Ntuple::GenJetak4NtupleObject& m_genJetAK4) {
  //std::cout<< "JetCorrectionTool::GetCorrectedJetJER"<< std::endl;
  if(!(jet.pt() > 0.)) return jet.tlv();
  
  // match jet to genJets to find real jet pt
  bool matched = false;
  float dR  = 0.2; // (jet cone size)/ 2 = 0.2 for 0.4 jets
  float dpt = 3*jet.pt()*jet.jer_sigma_pt();
  double genjetpt = 0; // only used if matched
  for (unsigned int j=0; j<(*m_genJetAK4.genJetAK4_pt).size(); ++j){
      UZH::GenJetak4 genjet( &m_genJetAK4, j );
      TLorentzVector genjet_tlv;
      genjet_tlv.SetPtEtaPhiE(genjet.genJetAK4_pt(), genjet.genJetAK4_eta(), genjet.genJetAK4_phi(), genjet.genJetAK4_e());
      if (genjet_tlv.DeltaR(jet.tlv()) < dR){
        if (fabs(jet.pt()-genjet_tlv.Pt()) < dpt){
          matched = true;
          dR = genjet_tlv.DeltaR( jet.tlv() );
          genjetpt = genjet.genJetAK4_pt();
        }
      }
  }
  
  TLorentzVector jet_tlv_jer;
  jet_tlv_jer.SetPtEtaPhiE(    jet.pt(), jet.eta(), jet.phi(), jet.e());
  double random = trandom->Gaus(0.,jet.jer_sigma_pt());
  
  //std::cout << ">>> JetCorrectionTool::GetCorrectedJetJER: jet matches with genJet = " << matched << std::endl;
  if (matched){
    dpt = jet.pt()-genjetpt;
    jet_tlv_jer *= 1 + (jet.jer_sf()-1.)*dpt/jet.pt();
  }else{
    if (jet.jer_sf()>1) jet_tlv_jer *= std::max(0.0,1. + random*std::sqrt(jet.jer_sf() *jet.jer_sf() - 1));
    else std::cout << "Warning! JetCorrectionTool::GetCorrectedJetJER: SF = " << jet.jer_sf() << " <= 1 !" << std::endl;
  }
  
  return jet_tlv_jer;
}



std::vector<TLorentzVector> JetCorrectionTool::GetCorrectedJetJERShifted(const UZH::Jet& jet, const Ntuple::GenJetak4NtupleObject& m_genJetAK4) {
  //std::cout<< "JetCorrectionTool::GetCorrectedJetJER"<< std::endl;
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution#Smearing_procedures
  if(!(jet.pt() > 0.)) return {jet.tlv(),jet.tlv(),jet.tlv()};
  
  // match jet to genJets to find real jet pt
  bool matched = false;
  float dR  = 0.2; // (jet cone size)/ 2 = 0.2 for 0.4 jets
  float dpt = 3*jet.pt()*jet.jer_sigma_pt();
  double genjetpt = 0; // only used if matched
  for (unsigned int j=0; j<(*m_genJetAK4.genJetAK4_pt).size(); ++j){
      UZH::GenJetak4 genjet( &m_genJetAK4, j );
      TLorentzVector genjet_tlv;
      genjet_tlv.SetPtEtaPhiE(genjet.genJetAK4_pt(), genjet.genJetAK4_eta(), genjet.genJetAK4_phi(), genjet.genJetAK4_e());
      if (genjet_tlv.DeltaR(jet.tlv()) < dR){
        if (fabs(jet.pt()-genjet_tlv.Pt()) < dpt){
          matched = true;
          dR = genjet_tlv.DeltaR( jet.tlv() );
          genjetpt = genjet.genJetAK4_pt();
        }      
      }
  }
  
  TLorentzVector jet_tlv_jer;
  TLorentzVector jet_tlv_jerUp;
  TLorentzVector jet_tlv_jerDown;
  jet_tlv_jer.SetPtEtaPhiE(    jet.pt(), jet.eta(), jet.phi(), jet.e());
  jet_tlv_jerUp.SetPtEtaPhiE(  jet.pt(), jet.eta(), jet.phi(), jet.e());
  jet_tlv_jerDown.SetPtEtaPhiE(jet.pt(), jet.eta(), jet.phi(), jet.e());
  
  if (matched){
    dpt = jet.pt()-genjetpt;
    jet_tlv_jer     *= 1 + (jet.jer_sf()     -1.)*dpt/jet.pt();
    jet_tlv_jerUp   *= 1 + (jet.jer_sf_up()  -1.)*dpt/jet.pt();
    jet_tlv_jerDown *= 1 + (jet.jer_sf_down()-1.)*dpt/jet.pt();    
  }else{
    double random = trandom->Gaus(0.,jet.jer_sigma_pt());
    if (jet.jer_sf()>1)      jet_tlv_jer     *= std::max(0.0,1. + random*std::sqrt(jet.jer_sf()     *jet.jer_sf()     -1));
    else std::cout << "Warning! JetCorrectionTool::GetCorrectedJetJER: SF = " << jet.jer_sf() << " <= 1 !\n";
    if (jet.jer_sf_up()>1)   jet_tlv_jerUp   *= std::max(0.0,1. + random*std::sqrt(jet.jer_sf_up()  *jet.jer_sf_up()  -1));
    else std::cout << "Warning! JetCorrectionTool::GetCorrectedJetJER: SF up = " << jet.jer_sf_up() << " <= 1 !\n";
    if (jet.jer_sf_down()>1) jet_tlv_jerDown *= std::max(0.0,1. + random*std::sqrt(jet.jer_sf_down()*jet.jer_sf_down()-1));
    else std::cout << "Warning! JetCorrectionTool::GetCorrectedJetJER: SF down = " << jet.jer_sf_down() << " <= 1 !\n";
  
    //if(jet_tlv_jerDown.Pt()<jet_tlv_jer.Pt() and jet_tlv_jerUp.Pt()<jet_tlv_jer.Pt()){
    //  std::cout << "!!! GetCorrectedJetJERShifted: JER UP/DOWN both have pt < JER central pt:\n";
    //  TauTauAnalysis::printRow({"pt original","pt jer","pt jerUp","pt jerDown","jer_sf","jer_sf_up","jer_sf_down","random","jer_sigma_pt"},{},{},{},14);
    //  TauTauAnalysis::printRow({},{},{jet.pt(),jet_tlv_jer.Pt(),jet_tlv_jerUp.Pt(),jet_tlv_jerDown.Pt(),jet.jer_sf(),jet.jer_sf_up(),jet.jer_sf_down(),random,jet.jer_sigma_pt()},{},14); }
  }
  
  return {jet_tlv_jer,jet_tlv_jerUp,jet_tlv_jerDown};
}



// Mass
double JetCorrectionTool::GetCorrectedMass(double mass, double pt, double eta, bool mc, int sigmaScale, int sigmaRes) {
  if(!MassGenBarrel || !MassGenEndcap || !MassRecoBarrel || !MassRecoEndcap || !MassResBarrel || !MassResEndcap) return -1.;
  float resolutionFactor(0.);
  
  // Base correction
  if( fabs(eta) <= 1.3 ) {
      mass *= MassGenBarrel->Eval( pt );
      mass *= MassRecoBarrel->Eval( pt );
  }
  else {
      mass *= MassGenEndcap->Eval( pt );
      mass *= MassRecoEndcap->Eval( pt );
  }
  
  if(mc) {
      
      // Scale correction
      float jms = 0.999;
      float jmsUnc = 0.004;
      mass *= jms + sigmaScale*jmsUnc;
      
      // Resolution correction
      float jmr = 1.079;
      float jmrUnc = 0.105;
      float jmr2(jmr + sigmaRes*jmrUnc);
      jmr2 = std::max(jmr2, float(1.)); // truncated to 0
      
      if( fabs(eta) <= 1.3 ) resolutionFactor = MassResBarrel->Eval( pt );
      else resolutionFactor = MassResBarrel->Eval( pt );
      
      mass = trandom->Gaus( mass, sqrt(jmr2*jmr2-1.)*(resolutionFactor-1.)*mass);
  }
  
  if(mass<=0.) mass = 0.;
  
  return mass;
}


