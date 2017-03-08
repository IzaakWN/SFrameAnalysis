#include "../interface/ScaleFactorTool.h"
#include <cstdlib>
#include <limits>
#include <TFile.h>



ScaleFactorTool::ScaleFactorTool(SCycleBase* parent, const char* name ):
 SToolBase( parent ), m_name( name ) 
{
  SetLogName( name );
  // leptons: https://github.com/CMS-HTT/LeptonEfficiencies
  // tau leg: https://github.com/rmanzoni/triggerSF/tree/moriond17
  // Mail Valeria Botta, 20/02/2017
  //   Electron_Ele24_eff.root         = Ele leg in cross trigger
  //   Muon_Mu19leg_2016BtoH_eff.root  = Mu  leg in cross trigger
  //   Muon_Mu22OR_eta2p1*             = IsoMu22, TkIsoMu22 (with and without |eta|< 2.1)
  
  DeclareProperty( m_name+"_Mu22Trig",          m_File_Mu22Trig          = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu22OR_eta2p1_eff.root"                 );
  DeclareProperty( m_name+"_Mu24Trig",          m_File_Mu24Trig          = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_IsoMu24_OR_TkIsoMu24_2016BtoH_eff.root" );
  DeclareProperty( m_name+"_MuTauTrig_MuLeg",   m_File_MuTauTrig_MuLeg   = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu19leg_2016BtoH_eff.root"              );
  DeclareProperty( m_name+"_MuTauTrig_TauLeg",  m_File_MuTauTrig_TauLeg  = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_Tau20LooseIsoPF.root"                   );
  DeclareProperty( m_name+"_MuIdIso",           m_File_MuIdIso           = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_IdIso_IsoLt0p15_2016BtoH_eff.root"      );
  DeclareProperty( m_name+"_EleTrig",           m_File_EleTrig           = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele25_eta2p1_WPTight_eff.root"  );
  DeclareProperty( m_name+"_EleTauTrig_EleLeg", m_File_EleTauTrig_EleLeg = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele24_eff.root"                 );
  DeclareProperty( m_name+"_EleTauTrig_TauLeg", m_File_EleTauTrig_TauLeg = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_TauWPLooseIsoPF.root"           );
  DeclareProperty( m_name+"_EleIdIso",          m_File_EleIdIso          = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_IdIso_IsoLt0p1_eff.root"        );

  DeclareProperty( m_name+"_EleMuTrig_Ele12Leg", m_File_EleMuTrig_Ele12Leg = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele12leg_eff.root"            );
  DeclareProperty( m_name+"_EleMuTrig_Ele23Leg", m_File_EleMuTrig_Ele23Leg = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele23leg_eff.root"            );
  DeclareProperty( m_name+"_EleMuTrig_Mu8Leg",   m_File_EleMuTrig_Mu8Leg   = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu8leg_2016BtoH_eff.root"             );
  DeclareProperty( m_name+"_EleMuTrig_Mu23Leg",  m_File_EleMuTrig_Mu23Leg  = std::string(std::getenv("SFRAME_DIR")) + "/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu23leg_2016BtoH_eff.root"            );
}



void ScaleFactorTool::BeginInputData( const SInputData& ) throw( SError ) {
  
  m_logger << INFO << "Initializing ScaleFactor for lepons"     << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu22 Trig: "             << m_File_Mu22Trig          << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu24 Trig: "             << m_File_Mu24Trig          << SLogger::endmsg;
  m_logger << INFO << "Efficiency file MuTau Trig Mu Leg: "     << m_File_MuTauTrig_MuLeg   << SLogger::endmsg;
  m_logger << INFO << "Efficiency file MuTau Trig Tau Leg: "    << m_File_MuTauTrig_TauLeg  << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu IdIso: "              << m_File_MuIdIso           << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Ele Trig: "              << m_File_EleTrig           << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleTau Trig Ele Leg: "   << m_File_EleTauTrig_EleLeg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleTau Trig Tau Leg: "   << m_File_EleTauTrig_TauLeg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Ele IdIso: "             << m_File_EleIdIso          << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleMu Trig Ele12 Leg: "  << m_File_EleMuTrig_Ele12Leg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleMu Trig Ele23 Leg: "  << m_File_EleMuTrig_Ele23Leg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleMu Trig Mu8 Leg: "    << m_File_EleMuTrig_Mu8Leg   << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleMu Trig Mu23 Leg: "   << m_File_EleMuTrig_Mu23Leg  << SLogger::endmsg;
  
  m_ScaleFactor_Mu22Trig          = new ScaleFactor( m_File_Mu22Trig );
  m_logger << INFO << "Scale factor Mu22 Trig initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_Mu24Trig          = new ScaleFactor( m_File_Mu24Trig );
  m_logger << INFO << "Scale factor Mu24 Trig initialised" << SLogger:: endmsg;
   
  m_ScaleFactor_MuTauTrig_MuLeg   = new ScaleFactor( m_File_MuTauTrig_MuLeg );
  m_logger << INFO << "Scale factor MuTau Trig Mu Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_MuTauTrig_TauLeg  = new ScaleFactorTau( m_File_MuTauTrig_TauLeg );
  m_logger << INFO << "Scale factor MuTau Trig Tau Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_MuIdIso           = new ScaleFactor( m_File_MuIdIso );
  m_logger << INFO << "Scale factor Mu IdIso initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleTrig           = new ScaleFactor( m_File_EleTrig );
  m_logger << INFO << "Scale factor Ele Trig initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleTauTrig_EleLeg = new ScaleFactor( m_File_EleTauTrig_EleLeg );
  m_logger << INFO << "Scale factor EleTau Trig Ele Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleTauTrig_TauLeg = new ScaleFactorTau( m_File_EleTauTrig_TauLeg );
  m_logger << INFO << "Scale factor EleTau Trig Tau Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleIdIso          = new ScaleFactor( m_File_EleIdIso );
  m_logger << INFO << "Scale factor Ele IdIso initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleMuTrig_Ele12Leg = new ScaleFactor( m_File_EleMuTrig_Ele12Leg );
  m_logger << INFO << "Scale factor EleMu Trig Ele 12 Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleMuTrig_Ele23Leg = new ScaleFactor( m_File_EleMuTrig_Ele23Leg );
  m_logger << INFO << "Scale factor EleMu Trig Ele 23 Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleMuTrig_Mu8Leg   = new ScaleFactor( m_File_EleMuTrig_Mu8Leg );
  m_logger << INFO << "Scale factor EleMu Trig Mu 8 Leg initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_EleMuTrig_Mu23Leg  = new ScaleFactor( m_File_EleMuTrig_Mu23Leg );
  m_logger << INFO << "Scale factor EleMu Trig Mu 23 Leg initialised" << SLogger:: endmsg;
  
  return;
}



ScaleFactorTool::~ScaleFactorTool(){
  //delete  eff_mc[etaLabel]; delete eff_data[etaLabel]
}



double ScaleFactorTool::get_Efficiency_MuTauTrig_MC(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  
  // assume:
  //  - eff(X) = eff(l*tau) = eff(l)*eff(tau)
  //  - single lepton (L) fired  =>  lepton leg (l) of cross-trigger fired
  //  - eff(L) < eff(l)
  //  - eff(L22) > eff(L24)
  //  - Mu24 fired  =>  Mu22 fired
  //
  //  1)  P( L AND !X) = eff(L)*[1-eff(tau)]
  //  2)  P(!L AND  X) = [eff(l)-eff(L)]*eff(tau)
  //  3)  P( L AND  X) = eff(L)*eff(tau)
  // https://indico.cern.ch/event/605406/contributions/2487049/attachments/1417489/2170776/Triggers_v1.pdf
  //
  // numerical protection:
  //  Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
  //  Case 2: P = max[ 1.e-2, [eff(l)-eff(L)*eff(tau) ]
  //  Case 3: P = min[eff(L), eff(l)]*eff_tau
  //  SF = min(1.e+1, P_data / P_MC)

  if( triggerFlags.find("mtx") != std::string::npos ){ // cross-trigger
    if( triggerFlags.find("mt24") != std::string::npos ){
      return std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm);
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      return std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm);
    }else{
      return std::max(0.01,(m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1)-m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm));
    }
  }else{ // no cross-trigger  
    if( triggerFlags.find("mt24") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm)));
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm)));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_MuTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_Efficiency_MuTauTrig_Data(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  
  // assume:
  //  - eff(X) = eff(l*tau) = eff(l)*eff(tau)
  //  - single lepton (L) fired  =>  lepton leg (l) of cross-trigger fired
  //  - eff(L) < eff(l)
  //  - eff(L22) > eff(L24)
  //  - Mu24 fired  =>  Mu22 fired
  //
  //  1)  P( L AND !X) = eff(L)*[1-eff(tau)]
  //  2)  P(!L AND  X) = [eff(l)-eff(L)]*eff(tau)
  //  3)  P( L AND  X) = eff(L)*eff(tau)
  // https://indico.cern.ch/event/605406/contributions/2487049/attachments/1417489/2170776/Triggers_v1.pdf
  //
  // numerical protection:
  //  Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
  //  Case 2: P = max[ 1.e-2, [eff(l)-eff(L)*eff(tau) ]
  //  Case 3: P = min[eff(L), eff(l)]*eff_tau
  //  SF = min[1.e+1, P_data / P_MC]

  if( triggerFlags.find("mtx") != std::string::npos ){ // cross-trigger
    if( triggerFlags.find("mt24") != std::string::npos ){
      return std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm);
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      return std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm);
    }else{
      return std::max(0.01,(m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1)-m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm));
    }
  }else{ // no cross-trigger  
    if( triggerFlags.find("mt24") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm)));
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm)));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_MuTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_ScaleFactor_MuTauTrig(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  // numerical protection: SF = min(1.e+1, P_data / P_MC)
  return std::min(10.0, get_Efficiency_MuTauTrig_Data(pt1,eta1,pt2,eta2,dm,triggerFlags)/get_Efficiency_MuTauTrig_MC(pt1,eta1,pt2,eta2,dm,triggerFlags));
}



double ScaleFactorTool::get_ScaleFactor_MuIdIso(double pt, double eta){
  return m_ScaleFactor_MuIdIso->get_ScaleFactor(pt,eta);
}



double ScaleFactorTool::get_Efficiency_EleTauTrig_MC(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  
  // assume:
  //  - eff(X) = eff(l*tau) = eff(l)*eff(tau)
  //  - single lepton (L) fired  =>  lepton leg (l) of cross-trigger fired
  //  - eff(L) < eff(l)
  //  - eff(L22) > eff(L24)
  //  - Ele45 covered in Ele25 efficiencies
  //
  //  1)  P( L AND !X) = eff(L)*[1-eff(tau)]
  //  2)  P(!L AND  X) = [eff(l)-eff(L)]*eff(tau)
  //  3)  P( L AND  X) = eff(L)*eff(tau)
  // https://indico.cern.ch/event/605406/contributions/2487049/attachments/1417489/2170776/Triggers_v1.pdf
  //
  // numerical protection:
  //  Case 1: P = max[ 1.e-2, eff(L)-eff(tau)*min(eff(L),eff(l)) ]
  //  Case 2: P = max[ 1.e-2, eff(l)-eff(L)*eff(tau) ]
  //  Case 3: P = min[eff(L), eff(l)]*eff(tau)
  //  SF = min(1.e+1, P_data / P_MC)

  if( triggerFlags.find("etx") != std::string::npos ){ // cross-trigger
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      return std::min(m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm);
    }else{
      return std::max(0.01,(m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1)-m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm));
    }
  }else{ // no cross-trigger  
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm)));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_Efficiency_EleTauTrig_Data(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  
  // assume:
  //  - eff(X) = eff(l*tau) = eff(l)*eff(tau)
  //  - single lepton (L) fired  =>  lepton leg (l) of cross-trigger fired
  //  - eff(L) < eff(l)
  //  - eff(L22) > eff(L24)
  //  - Ele45 covered in Ele25 efficiencies
  //
  //  1)  P( L AND !X) = eff(L)*[1-eff(tau)]
  //  2)  P(!L AND  X) = [eff(l)-eff(L)]*eff(tau)
  //  3)  P( L AND  X) = eff(L)*eff(tau)
  // https://indico.cern.ch/event/605406/contributions/2487049/attachments/1417489/2170776/Triggers_v1.pdf
  //
  // numerical protection:
  //  Case 1: P = max[ 1.e-2, eff(L)-eff(tau)*min(eff(L),eff(l)) ]
  //  Case 2: P = max[ 1.e-2, eff(l)-eff(L)*eff(tau) ]
  //  Case 3: P = min[eff(L), eff(l)]*eff(tau)
  //  SF = min[1.e+1, P_data / P_MC]

  if( triggerFlags.find("etx") != std::string::npos ){ // cross-trigger
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      return std::min(m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm);
    }else{
      return std::max(0.01,(m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1)-m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm));
    }
  }else{ // no cross-trigger  
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      return std::max(0.01,( m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm)));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}




double ScaleFactorTool::get_ScaleFactor_EleTauTrig(double pt1, double eta1, double pt2, double eta2, int dm, std::string triggerFlags){
  // numerical protection: SF = min(1.e+1, P_data / P_MC)
  return std::min(10.0, get_Efficiency_EleTauTrig_Data(pt1,eta1,pt2,eta2,dm,triggerFlags)/get_Efficiency_EleTauTrig_MC(pt1,eta1,pt2,eta2,dm,triggerFlags));
}



double ScaleFactorTool::get_ScaleFactor_EleIdIso(double pt, double eta){
  return m_ScaleFactor_EleIdIso->get_ScaleFactor(pt,eta);
}



double ScaleFactorTool::get_Efficiency_EleMuTrig_MC(double pt1, double eta1, double pt2, double eta2, std::string triggerFlags){

  // assume:
  //  - eff(X1) = eff(Ele12Mu23) = eff(Ele12)*eff(Mu23)
  //  - eff(X2) = eff(Ele23Mu8)  = eff(Ele23)*eff(Mu8)
  //  - Ele23 fired  => Ele12 fired
  //  - eff(Ele23) < eff(Ele12)
  //  - Mu23 fired  => Mu8 fired
  //  - eff(Mu23)  < eff(Mu8)
  //
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Muon_efficiencies
  //
  //  P( X1  OR  X2) = eff(Ele12)*eff(Mu23) + eff(Ele23)*eff(Mu8) - eff(Ele23)*eff(Mu23)
  //  P( X1 AND  X2) = eff(Ele23)*eff(Mu23)
  //  P( X1 AND !X2) = eff(Ele12)*eff(Mu23)*[eff(Ele8)-eff(Ele23)] 
  //  P(!X1 AND  X2) = eff(Ele23)*eff(Mu8) *[eff(Mu12)-eff(Mu8)  ]
  //
  // numerical protection:
  //  P( X1 AND  X2) = eff(Ele23)*eff(Mu23)
  //  P( X1 AND !X2) = max[1.e-2, eff(Ele12)*eff(Mu23)*[eff(Ele8)-eff(Ele23)]]
  //  P(!X1 AND  X2) = max[1.e-2, eff(Ele23)*eff(Mu8) *[eff(Mu12)-eff(Mu8)  ]]
  //
  
  if( triggerFlags.find("e12m23") != std::string::npos ){
    if( triggerFlags.find("e23m8") != std::string::npos )
      return m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyMC(pt2,eta2);
    else
      return std::max(0.01, (m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyData(pt1,eta1) - m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyMC(pt1,eta1))
                           * m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyMC(pt2,eta2));
  }else{
    if( triggerFlags.find("e23m8") != std::string::npos )
      return std::max(0.01, (m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyMC(pt2,eta2)   - m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyMC(pt2,eta2))
                           * m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyMC(pt2,eta2));
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleMuTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_Efficiency_EleMuTrig_Data(double pt1, double eta1, double pt2, double eta2, std::string triggerFlags){

  // assume:
  //  - eff(X1) = eff(Ele12Mu23) = eff(Ele12)*eff(Mu23)
  //  - eff(X2) = eff(Ele23Mu8)  = eff(Ele23)*eff(Mu8)
  //  - Ele23 fired  => Ele12 fired
  //  - eff(Ele23) < eff(Ele12)
  //  - Mu23 fired  => Mu8 fired
  //  - eff(Mu23)  < eff(Mu8)
  //
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Muon_efficiencies
  //
  // P( X1  OR  X2) = eff(Ele12)*eff(Mu23) + eff(Ele23)*eff(Mu8) - eff(Ele23)*eff(Mu23)
  // P( X1 AND  X2) = eff(Ele23)*eff(Mu23)
  // P( X1 AND !X2) = eff(Ele12)*eff(Mu23)*[eff(Ele8)-eff(Ele23)] 
  // P(!X1 AND  X2) = eff(Ele23)*eff(Mu8) *[eff(Mu12)-eff(Mu8)  ]
  //
  // numerical protection:
  //  P( X1 AND  X2) = eff(Ele23)*eff(Mu23)
  //  P( X1 AND !X2) = max[1.e-2, eff(Ele12)*eff(Mu23)*[eff(Ele8)-eff(Ele23)]]
  //  P(!X1 AND  X2) = max[1.e-2, eff(Ele23)*eff(Mu8) *[eff(Mu12)-eff(Mu8)  ]]
  //
  
  if( triggerFlags.find("e12m23") != std::string::npos ){
    if( triggerFlags.find("e23m8") != std::string::npos )
      return m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyData(pt2,eta2);
    else
      return std::max(0.01, (m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyData(pt1,eta1) - m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyData(pt1,eta1))
                           * m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyData(pt2,eta2));
  }else{
    if( triggerFlags.find("e23m8") != std::string::npos )
      return std::max(0.01, (m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyData(pt2,eta2)   - m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyData(pt2,eta2))
                           * m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyData(pt2,eta2));
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleMuTrig_Data - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_ScaleFactor_EleMuTrig(double pt1, double eta1, double pt2, double eta2, std::string triggerFlags){
  return std::min(10.0, get_Efficiency_EleMuTrig_Data(pt1,eta1,pt2,eta2,triggerFlags)/get_Efficiency_EleMuTrig_MC(pt1,eta1,pt2,eta2,triggerFlags));
}



double ScaleFactorTool::get_Efficiency_EleMuTrig_OR_MC(double pt1, double eta1, double pt2, double eta2){
  //  P( X1 OR X2) = eff(Ele12)*eff(Mu23) + eff(Ele23)*eff(Mu8) - eff(Ele23)*eff(Mu23)
  return   m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyMC(pt2,eta2)
         + m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyMC(pt2,eta2)
         - m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyMC(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyMC(pt2,eta2);
}



double ScaleFactorTool::get_Efficiency_EleMuTrig_OR_Data(double pt1, double eta1, double pt2, double eta2){
  //  P( X1 OR X2) = eff(Ele12)*eff(Mu23) + eff(Ele23)*eff(Mu8) - eff(Ele23)*eff(Mu23)
  return   m_ScaleFactor_EleMuTrig_Ele12Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyData(pt2,eta2)
         + m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu8Leg->get_EfficiencyData(pt2,eta2)
         - m_ScaleFactor_EleMuTrig_Ele23Leg->get_EfficiencyData(pt1,eta1) * m_ScaleFactor_EleMuTrig_Mu23Leg->get_EfficiencyData(pt2,eta2);
}



double ScaleFactorTool::get_ScaleFactor_EleMuTrig_OR(double pt1, double eta1, double pt2, double eta2){
  return std::min(10.0, get_Efficiency_EleMuTrig_OR_Data(pt1,eta1,pt2,eta2)
                         / std::max(0.01, get_Efficiency_EleMuTrig_OR_MC(pt1,eta1,pt2,eta2)));
}


