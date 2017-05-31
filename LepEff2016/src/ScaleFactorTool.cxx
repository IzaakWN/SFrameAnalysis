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
  
  DeclareProperty( m_name+"_Mu22Trig",          m_File_Mu22Trig          = "$SFRAME_DIR/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu22OR_eta2p1_eff.root"                 );
  DeclareProperty( m_name+"_Mu24Trig",          m_File_Mu24Trig          = "$SFRAME_DIR/../LepEff2016/data/Muon/Run2016BtoH/Muon_IsoMu24_OR_TkIsoMu24_2016BtoH_eff.root" );
  DeclareProperty( m_name+"_MuTauTrig_MuLeg",   m_File_MuTauTrig_MuLeg   = "$SFRAME_DIR/../LepEff2016/data/Muon/Run2016BtoH/Muon_Mu19leg_2016BtoH_eff.root"              );
  DeclareProperty( m_name+"_MuTauTrig_TauLeg",  m_File_MuTauTrig_TauLeg  = "$SFRAME_DIR/../LepEff2016/data/Muon/Run2016BtoH/Muon_Tau20LooseIsoPF.root"                   );
  DeclareProperty( m_name+"_MuIdIso",           m_File_MuIdIso           = "$SFRAME_DIR/../LepEff2016/data/Muon/Run2016BtoH/Muon_IdIso_IsoLt0p15_2016BtoH_eff.root"      );
  
  DeclareProperty( m_name+"_EleTrig",           m_File_EleTrig           = "$SFRAME_DIR/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele25_eta2p1_WPTight_eff.root"  );
  DeclareProperty( m_name+"_EleTauTrig_EleLeg", m_File_EleTauTrig_EleLeg = "$SFRAME_DIR/../LepEff2016/data/Electron/Run2016BtoH/Electron_Ele24_eff.root"                 );
  DeclareProperty( m_name+"_EleTauTrig_TauLeg", m_File_EleTauTrig_TauLeg = "$SFRAME_DIR/../LepEff2016/data/Electron/Run2016BtoH/Electron_TauWPLooseIsoPF.root"           );
  DeclareProperty( m_name+"_EleIdIso",          m_File_EleIdIso          = "$SFRAME_DIR/../LepEff2016/data/Electron/Run2016BtoH/Electron_IdIso_IsoLt0p1_eff.root"        );
}



void ScaleFactorTool::BeginInputData( const SInputData& ) throw( SError ) {
  
  m_logger << INFO << SLogger::endmsg;
  m_logger << INFO << "Initializing ScaleFactor for lepons"     << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu22 Trig:      "        << m_File_Mu22Trig          << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu24 Trig:      "        << m_File_Mu24Trig          << SLogger::endmsg;
  m_logger << INFO << "Efficiency file MuTau Trig Mu Leg:  "    << m_File_MuTauTrig_MuLeg   << SLogger::endmsg;
  m_logger << INFO << "Efficiency file MuTau Trig Tau Leg: "    << m_File_MuTauTrig_TauLeg  << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Mu IdIso:       "        << m_File_MuIdIso           << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Ele Trig:       "        << m_File_EleTrig           << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleTau Trig Ele Leg: "   << m_File_EleTauTrig_EleLeg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file EleTau Trig Tau Leg: "   << m_File_EleTauTrig_TauLeg << SLogger::endmsg;
  m_logger << INFO << "Efficiency file Ele IdIso:      "        << m_File_EleIdIso          << SLogger::endmsg;
  
  m_ScaleFactor_Mu22Trig          = new ScaleFactor( m_File_Mu22Trig );
  m_ScaleFactor_Mu24Trig          = new ScaleFactor( m_File_Mu24Trig );
  m_ScaleFactor_MuTauTrig_MuLeg   = new ScaleFactor(    m_File_MuTauTrig_MuLeg  );
  m_ScaleFactor_MuTauTrig_TauLeg  = new ScaleFactorTau( m_File_MuTauTrig_TauLeg );
  m_logger << INFO << "Scale factor Mu22, Mu24, MuTau triggers initialised" << SLogger:: endmsg;
     
  m_ScaleFactor_EleTrig           = new ScaleFactor( m_File_EleTrig );
  m_ScaleFactor_EleTauTrig_EleLeg = new ScaleFactor(    m_File_EleTauTrig_EleLeg );
  m_ScaleFactor_EleTauTrig_TauLeg = new ScaleFactorTau( m_File_EleTauTrig_TauLeg );
  m_logger << INFO << "Scale factor Ele, EleTau Trig initialised" << SLogger:: endmsg;
  
  m_ScaleFactor_MuIdIso           = new ScaleFactor( m_File_MuIdIso  );
  m_ScaleFactor_EleIdIso          = new ScaleFactor( m_File_EleIdIso );
  m_logger << INFO << "Scale factor Mu & Ele IdIso initialised" << SLogger:: endmsg;
    
  return;
}



ScaleFactorTool::~ScaleFactorTool(){
  //delete  eff_mc[etaLabel]; delete eff_data[etaLabel]
}



double ScaleFactorTool::get_Efficiency_MuTauTrig_MC(double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau, std::string triggerFlags){
  
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
      // Case 3: P = min[eff(L), eff(l)]*eff_tau
      return std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau);
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      // Case 3: P = min[eff(L), eff(l)]*eff_tau
      return std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau);
    }else{
      // Case 2: P = max[ 1.e-2, [eff(l)-eff(L)*eff(tau) ]
      return std::max(0.01,(m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1)-m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau));
    }
  }else{ // no cross-trigger
    if( triggerFlags.find("mt24") != std::string::npos ){
      // Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
      return std::max(0.01, m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau));
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      // Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
      return std::max(0.01, m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_MuTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_Efficiency_MuTauTrig_Data(double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau, std::string triggerFlags){
  
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
      // Case 3: P = min[eff(L), eff(l)]*eff_tau
      return std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau);
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      // Case 3: P = min[eff(L), eff(l)]*eff_tau
      return std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau);
    }else{
      // Case 2: P = max[ 1.e-2, [eff(l)-eff(L)*eff(tau) ]
      return std::max(0.01,(m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1)-m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau));
    }
  }else{ // no cross-trigger  
    if( triggerFlags.find("mt24") != std::string::npos ){
      // Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
      return std::max(0.01, m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu24Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau));
    }else if( triggerFlags.find("mt22") != std::string::npos ){
      // Case 1: P = max[ 1.e-2, eff_L-eff(tau)*min[eff(L),eff(l)] ]
      return std::max(0.01, m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_Mu22Trig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_MuTauTrig_MuLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_MuTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_MuTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_ScaleFactor_MuTauTrig(double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2, std::string triggerFlags){
  // numerical protection: SF = min(1.e+1, P_data / P_MC)
  //bool isRealTau = genmatch_2==5;
  return std::min(10.0, get_Efficiency_MuTauTrig_Data(pt1,eta1,pt2,eta2,dm,genmatch_2==5,triggerFlags)/get_Efficiency_MuTauTrig_MC(pt1,eta1,pt2,eta2,dm,genmatch_2==5,triggerFlags));
}



double ScaleFactorTool::get_ScaleFactor_MuTauTrig_OR(double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2, std::string triggerFlags){
  if( pt1>23 and triggerFlags.find("mt22")!=std::string::npos ){
    return m_ScaleFactor_Mu22Trig->get_ScaleFactor(pt1,eta1);
  }else{ //if(triggerFlags.find("mtx")!=std::string::npos){
    // if(pt1<21){
    //   double sf1 = m_ScaleFactor_MuTauTrig_MuLeg->get_ScaleFactor(pt1,eta1);
    //   double sf2 = m_ScaleFactor_MuTauTrig_TauLeg->get_ScaleFactor(pt2,eta2,dm,genmatch_2==5);
    //   std::cout << ">>> triggerFlags="<<triggerFlags<< std::endl;
    //   std::cout << ">>> m_ScaleFactor_MuTauTrig_MuLeg->get_ScaleFactor("<<pt1<<","<<eta1<<")="<<sf1<<std::endl;
    //   std::cout << ">>> m_ScaleFactor_MuTauTrig_TauLeg->get_ScaleFactor("<<pt2<<","<<eta2<<","<<dm<<","<<(genmatch_2==5)<<")="<<sf2<<std::endl;
    //   std::cout << ">>> product="<<sf1*sf2<<std::endl;
    // }
    return  m_ScaleFactor_MuTauTrig_MuLeg->get_ScaleFactor(pt1,eta1)
           *m_ScaleFactor_MuTauTrig_TauLeg->get_ScaleFactor(pt2,eta2,dm,genmatch_2==5);
  }
}



double ScaleFactorTool::get_ScaleFactor_Mu22Trig(double pt1, double eta1){
  return m_ScaleFactor_Mu22Trig->get_ScaleFactor(pt1,eta1);
}



double ScaleFactorTool::get_ScaleFactor_MuIdIso(double pt, double eta){
  return m_ScaleFactor_MuIdIso->get_ScaleFactor(pt,eta);
}



double ScaleFactorTool::get_Efficiency_EleTauTrig_MC(double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau, std::string triggerFlags){
  
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
      // Case 1: P = max[ 1.e-2, eff(L)-eff(tau)*min(eff(L),eff(l)) ]
      return std::min(m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau);
    }else{
      // Case 2: P = max[ 1.e-2, eff(l)-eff(L)*eff(tau) ]
      return std::max(0.01,(m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1)
                            -m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau));
    }
  }else{ // no cross-trigger
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      // Case 3: P = min[eff(L), eff(l)]*eff(tau)
      return std::max(0.01, m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1)
                            -std::min(m_ScaleFactor_EleTrig->get_EfficiencyMC(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyMC(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyMC(pt2,eta2,dm,isRealTau));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_Efficiency_EleTauTrig_Data(double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau, std::string triggerFlags){
  
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
  //  Case 2: P = max[ 1.e-2, (eff(l)-eff(L))*eff(tau) ]
  //  Case 3: P = min[eff(L), eff(l)]*eff(tau)
  //  SF = min[1.e+1, P_data / P_MC]
  
  if( triggerFlags.find("etx") != std::string::npos ){ // cross-trigger
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      // Case 3: P = min[eff(L), eff(l)]*eff(tau)
      return std::min(m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1))*m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau);
    }else{
      // Case 2: P = max[ 1.e-2, (eff(l)-eff(L))*eff(tau) ]
      return std::max(0.01,( m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1)
                            -m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau));
    }
  }else{ // no cross-trigger
    if( triggerFlags.find("et25") != std::string::npos or triggerFlags.find("et45") != std::string::npos ){
      // Case 1: P = max[ 1.e-2, eff(L)-eff(tau)*min(eff(L),eff(l)) ]
      return std::max(0.01, m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1)
                            -std::min(m_ScaleFactor_EleTrig->get_EfficiencyData(pt1,eta1),m_ScaleFactor_EleTauTrig_EleLeg->get_EfficiencyData(pt1,eta1))
                            *m_ScaleFactor_EleTauTrig_TauLeg->get_EfficiencyData(pt2,eta2,dm,isRealTau));
    }
  }
  
  std::cout << ">>> ScaleFactorTool::get_Efficiency_EleTauTrig_MC - no trigger fired? triggerFlags=" << triggerFlags << std::endl;
  return 0.;
}



double ScaleFactorTool::get_ScaleFactor_EleTauTrig(double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2, std::string triggerFlags){
  // numerical protection: SF = min(1.e+1, P_data / P_MC)
  return std::min(10.0, get_Efficiency_EleTauTrig_Data(pt1,eta1,pt2,eta2,dm,genmatch_2==5,triggerFlags)/get_Efficiency_EleTauTrig_MC(pt1,eta1,pt2,eta2,dm,genmatch_2==5,triggerFlags));
}



double ScaleFactorTool::get_ScaleFactor_EleTauTrig_OR(double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2, std::string triggerFlags){
  if( pt1>26 and (triggerFlags.find("et25")!=std::string::npos or triggerFlags.find("et45")!=std::string::npos) ){
    return m_ScaleFactor_EleTrig->get_ScaleFactor(pt1,eta1);
  }else{ //if(triggerFlags.find("etx")!=std::string::npos){
    return  m_ScaleFactor_EleTauTrig_EleLeg->get_ScaleFactor(pt1,eta1)
           *m_ScaleFactor_EleTauTrig_TauLeg->get_ScaleFactor(pt2,eta2,dm,genmatch_2==5);
  }
}



double ScaleFactorTool::get_ScaleFactor_EleTrig(double pt1, double eta1){
  return m_ScaleFactor_EleTrig->get_ScaleFactor(pt1,eta1);
}



double ScaleFactorTool::get_ScaleFactor_EleIdIso(double pt, double eta){
  return m_ScaleFactor_EleIdIso->get_ScaleFactor(pt,eta);
}
