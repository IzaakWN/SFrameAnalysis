#include "../interface/SVFitTool.h"
#include <cstdlib>
#include <limits>
#include <TFile.h>

// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#SVfit
// https://github.com/veelken/SVfit_standalone



SVFitTool::SVFitTool(SCycleBase* parent, const char* name ): SToolBase( parent ), m_name( name ) 
{
  SetLogName( name );
  DeclareProperty( m_name+"ResoFile ", m_ResoFilePath = std::string (std::getenv("SFRAME_DIR")) + "/../SVFitTools/data/svFitVisMassAndPtResolutionPDF.root" ); 
}



void SVFitTool::BeginInputData( const SInputData& ) throw( SError ) {

  m_logger << INFO << "Initializing Mass and pT resolution for SVFit" << SLogger::endmsg;
  m_logger << INFO << "SVFit Mass and pT resolution File: " << m_ResoFilePath << SLogger::endmsg;
  TString resoFilePath(m_ResoFilePath);
  m_ResoFile = new TFile( resoFilePath, "read" );
  return;
}



SVFitTool::~SVFitTool(){
}



void SVFitTool::addMeasuredLeptonTau( const UZH::Electron& electron, const UZH::Tau& tau){
  //std::cout << "addMeasuredLeptonTau" << std::endl;
  m_measuredTauLeptons.clear();
  // add lepton first, tau second !
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToElecDecay,
                                                                     electron.pt(), electron.eta(), electron.phi(), 0.51100e-3 ));
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToHadDecay,
                                                                     tau.pt(), tau.eta(), tau.phi(), tau.tlv().M(), tau.decayMode() ));
}



void SVFitTool::addMeasuredLeptonTau( const UZH::Muon& muon, const UZH::Tau& tau){
  //std::cout << "addMeasuredLeptonTau" << std::endl;
  m_measuredTauLeptons.clear();
  // add lepton first, tau second !
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToMuDecay,
                                                                     muon.pt(), muon.eta(), muon.phi(), 105.658e-3 ));
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToHadDecay,
                                                                     tau.pt(), tau.eta(), tau.phi(), tau.tlv().M(), tau.decayMode() ));
}



void SVFitTool::addMeasuredLeptonTau( const UZH::Electron& electron, const UZH::Muon& muon){
  //std::cout << "addMeasuredLeptonTau" << std::endl;
  m_measuredTauLeptons.clear();
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToElecDecay,
                                                                     electron.pt(), electron.eta(), electron.phi(), 0.51100e-3 ));
  m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToMuDecay,
                                                                     muon.pt(), muon.eta(), muon.phi(), 105.658e-3 ));
}



void SVFitTool::addMeasuredLeptonTau( const std::string& channel, const TLorentzVector lep, const TLorentzVector tau, int tauDecayMode){
  //std::cout << "addMeasuredLeptonTau" << std::endl;
  //std::cout << "addMeasuredLeptonTau - tauDecayMode = " << tauDecayMode << std::endl;
  
  m_measuredTauLeptons.clear();
  
  // add lepton first, tau second !
  if(channel=="etau" or channel=="eletau"){
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToElecDecay,
                                                                       lep.Pt(), lep.Eta(), lep.Phi(), 0.51100e-3 ));
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToHadDecay,
                                                                       tau.Pt(), tau.Eta(), tau.Phi(), tau.M(), tauDecayMode ));
  }
  else if(channel=="mutau"){
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToMuDecay,
                                                                       lep.Pt(), lep.Eta(), lep.Phi(),  105.658e-3));
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToHadDecay,
                                                                       tau.Pt(), tau.Eta(), tau.Phi(), tau.M(), tauDecayMode));
  }
  else if(channel=="emu"){
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToElecDecay,
                                                                       lep.Pt(), lep.Eta(), lep.Phi(), 0.51100e-3 ));
    m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToMuDecay,
                                                                       lep.Pt(), lep.Eta(), lep.Phi(), 105.658e-3 ));
  }
  else
  {
    std::cout << ">>> Warning! Could not do addMeasuredLeptonTau: channel != eletau of mutau !" << std::endl;
  }
}



// void SVFitTool::addMeasuredElectronTau( TLorentzVector ele, TLorentzVector tau ){
//   m_measuredTauLeptons.clear();
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton(svFitStandalone::kTauToElecDecay, ele.pt(), ele.eta(), ele.phi(), 0.51100e-3));
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton(svFitStandalone::kTauToHadDecay,  tau.pt(), tau.eta(), tau.phi(), tau.mass()));
// }
// 
// 
// 
// void SVFitTool::addMeasuredMuonTau( TLorentzVector mu, TLorentzVector tau ){
//   m_measuredTauLeptons.clear();
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton(svFitStandalone::kTauToMuDecay,  mu.pt(),  mu.eta(),  mu.phi(),  105.658e-3));
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton(svFitStandalone::kTauToHadDecay, tau.pt(), tau.eta(), tau.phi(), tau.mass()));
// }



// void SVFitTool::addMeasuredTauToElectron( const double pt, const double eta, const double phi ){
//   //m_measuredTauLeptons.clear();
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToElecDecay,
//                                                                      pt, eta, phi, 0.51100e-3 ));
// }
// 
// 
// 
// void SVFitTool::addMeasuredTauToMuon(     const double pt, const double eta, const double phi ){
//   //m_measuredTauLeptons.clear();
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToMuDecay,
//                                                                      pt, eta, phi, 105.658e-3 ));
// }
// 
// 
// 
// void SVFitTool::addMeasuredTauToHadrons(  const double pt, const double eta, const double phi, const double mass ){
//   //m_measuredTauLeptons.clear();
//   m_measuredTauLeptons.push_back(svFitStandalone::MeasuredTauLepton( svFitStandalone::kTauToHadDecay,
//                                                                      pt, eta, phi, mass ));
// }



double SVFitTool::getSVFitMass( const double measuredMETx, const double measuredMETy,
                                const double covMET00, const double covMET01, const double covMET11,
                                unsigned int verbosity ){
  //std::cout << "getSVFitMass" << std::endl;
  
  if( m_measuredTauLeptons.size() != 2 ) return -1;
  
  TMatrixD covMET(2, 2);
  covMET[0][0] = covMET00;
  covMET[1][0] = covMET01;
  covMET[0][1] = covMET01;
  covMET[1][1] = covMET11;
  
  SVfitStandaloneAlgorithm algo(m_measuredTauLeptons, measuredMETx, measuredMETy, covMET, 0);
  
  algo.addLogM(true, 1.);
  TH1::AddDirectory(false);  
  algo.shiftVisPt(true, m_ResoFile);
  algo.integrateMarkovChain();
  
  double mass = algo.mass(); // full mass of tau lepton pair in units of GeV
  //double pt = algo.pt();
  //double transverseMass = algo.transverseMass(); // transverse mass of tau lepton pair in units of GeV
  if( !algo.isValidSolution() ){
    std::cout << ">>> Warning! SVFit: failed to find valid solution!" << std::endl;
    mass = -1;
  }
  
  //m_measuredTauLeptons.clear();
  return mass;
}



void SVFitTool::getSVFitMassAndPT(  double& mass, double& pt,
                                    const double measuredMETx, const double measuredMETy,
                                    const double covMET00, const double covMET01, const double covMET11,
                                    unsigned int verbosity ){
  //std::cout << "getSVFitMass" << std::endl;
  
  if( m_measuredTauLeptons.size() != 2 ){
    std::cout << ">>> Warning! Could not do getSVFitMassAndPT: m_measuredTauLeptons.size() != 2" << std::endl;
    mass = -1; pt = -1; return;
  }
  
  TMatrixD covMET(2, 2);
  covMET[0][0] = covMET00;
  covMET[1][0] = covMET01;
  covMET[0][1] = covMET01;
  covMET[1][1] = covMET11;
  
  SVfitStandaloneAlgorithm algo(m_measuredTauLeptons, measuredMETx, measuredMETy, covMET, 0);
  
  algo.addLogM(true, 1.);
  TH1::AddDirectory(false);  
  algo.shiftVisPt(true, m_ResoFile);
  algo.integrateMarkovChain();
  
  mass = algo.mass(); // full mass of tau lepton pair in units of GeV
  pt = algo.pt();     // see SVfitStandaloneAlgorithm.h
  if( !algo.isValidSolution() ){
    std::cout << ">>> Warning! SVFit: failed to find valid solution!" << std::endl;
    mass = -1;
  }
  
  //m_measuredTauLeptons.clear();
  return;
}






