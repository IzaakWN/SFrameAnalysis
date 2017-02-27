
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

// Local include(s):
#include "../include/ElectronNtupleObject.h"

namespace Ntuple {

  ElectronNtupleObject::ElectronNtupleObject( SCycleBaseNTuple* parent )
    : SInputVariables< SCycleBaseNTuple >( parent ) {
      m_connectsucceeded.resize(kEnd);
  }

  void ElectronNtupleObject::setConnectSucceeded(const unsigned int index, const bool success) {
    if (m_connectsucceeded.size() < index+1)  m_connectsucceeded.resize(index+1);
    m_connectsucceeded.at(index) = success;
  }

  void ElectronNtupleObject::ConnectVariables( const TString& treeName,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
   
     ElectronNtupleObject::ConnectVariables( treeName, Ntuple::ElectronAll, prefix, ntupleType);
                                         
  }                                         

  void ElectronNtupleObject::ConnectVariables( const TString& treeName,
                                         UInt_t detail_level,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
                                         
    // get instance of NtupleObjectNames
    NtupleObjectNames m_objectNames(ntupleType);
    

    // particle vector size
    ConnectVariable( treeName, prefix + m_objectNames.getName("N"), N );
    
    // connect variables that are defined in Particle.cxx
    ConnectVariable( treeName, prefix + m_objectNames.getName("e"), e );
    ConnectVariable( treeName, prefix + m_objectNames.getName("pt"), pt );
    ConnectVariable( treeName, prefix + m_objectNames.getName("eta"), eta );
    ConnectVariable( treeName, prefix + m_objectNames.getName("phi"), phi );
    ConnectVariable( treeName, prefix + m_objectNames.getName("m"), m );
        
    

    // connect object specific variables
if(  ((detail_level & Ntuple::ElectronAdvancedID) == Ntuple::ElectronAdvancedID)  ) {
     setConnectSucceeded(21, ConnectVariable( treeName, prefix + m_objectNames.getName("passConversionVeto"), passConversionVeto)); 
    setConnectSucceeded(22, ConnectVariable( treeName, prefix + m_objectNames.getName("full5x5_sigmaIetaIeta"), full5x5_sigmaIetaIeta)); 
    setConnectSucceeded(23, ConnectVariable( treeName, prefix + m_objectNames.getName("dEtaIn"), dEtaIn)); 
    setConnectSucceeded(24, ConnectVariable( treeName, prefix + m_objectNames.getName("dPhiIn"), dPhiIn)); 
    setConnectSucceeded(25, ConnectVariable( treeName, prefix + m_objectNames.getName("hOverE"), hOverE)); 
    setConnectSucceeded(26, ConnectVariable( treeName, prefix + m_objectNames.getName("relIsoWithDBeta"), relIsoWithDBeta)); 
    setConnectSucceeded(27, ConnectVariable( treeName, prefix + m_objectNames.getName("ooEmooP"), ooEmooP)); 
    setConnectSucceeded(28, ConnectVariable( treeName, prefix + m_objectNames.getName("expectedMissingInnerHits"), expectedMissingInnerHits)); 
    setConnectSucceeded(29, ConnectVariable( treeName, prefix + m_objectNames.getName("d0"), d0)); 
    setConnectSucceeded(30, ConnectVariable( treeName, prefix + m_objectNames.getName("dz"), dz)); 
    setConnectSucceeded(31, ConnectVariable( treeName, prefix + m_objectNames.getName("d0_allvertices"), d0_allvertices)); 
    setConnectSucceeded(32, ConnectVariable( treeName, prefix + m_objectNames.getName("dz_allvertices"), dz_allvertices)); 
    setConnectSucceeded(33, ConnectVariable( treeName, prefix + m_objectNames.getName("dr03EcalRecHitSumEt"), dr03EcalRecHitSumEt)); 
    setConnectSucceeded(34, ConnectVariable( treeName, prefix + m_objectNames.getName("dr03HcalDepth1TowerSumEt"), dr03HcalDepth1TowerSumEt)); 
    setConnectSucceeded(35, ConnectVariable( treeName, prefix + m_objectNames.getName("rho"), rho)); 
    setConnectSucceeded(36, ConnectVariable( treeName, prefix + m_objectNames.getName("ecalDriven"), ecalDriven)); 
    setConnectSucceeded(37, ConnectVariable( treeName, prefix + m_objectNames.getName("dEtaInSeed"), dEtaInSeed)); 
    setConnectSucceeded(38, ConnectVariable( treeName, prefix + m_objectNames.getName("full5x5_e2x5Max"), full5x5_e2x5Max)); 
    setConnectSucceeded(39, ConnectVariable( treeName, prefix + m_objectNames.getName("full5x5_e5x5"), full5x5_e5x5)); 
    setConnectSucceeded(40, ConnectVariable( treeName, prefix + m_objectNames.getName("full5x5_e1x5"), full5x5_e1x5)); 
    setConnectSucceeded(41, ConnectVariable( treeName, prefix + m_objectNames.getName("dr03TkSumPt"), dr03TkSumPt)); 
    setConnectSucceeded(42, ConnectVariable( treeName, prefix + m_objectNames.getName("hadronicOverEm"), hadronicOverEm)); 
} // end of detail level AdvancedID

if(  ((detail_level & Ntuple::ElectronBasic) == Ntuple::ElectronBasic)  ) {
     setConnectSucceeded(1, ConnectVariable( treeName, prefix + m_objectNames.getName("pdgId"), pdgId)); 
    setConnectSucceeded(2, ConnectVariable( treeName, prefix + m_objectNames.getName("charge"), charge)); 
    setConnectSucceeded(3, ConnectVariable( treeName, prefix + m_objectNames.getName("et"), et)); 
} // end of detail level Basic

if(  ((detail_level & Ntuple::ElectronBoostedID) == Ntuple::ElectronBoostedID)  ) {
     setConnectSucceeded(43, ConnectVariable( treeName, prefix + m_objectNames.getName("isVetoElectronBoosted"), isVetoElectronBoosted)); 
    setConnectSucceeded(44, ConnectVariable( treeName, prefix + m_objectNames.getName("isMediumElectronBoosted"), isMediumElectronBoosted)); 
    setConnectSucceeded(45, ConnectVariable( treeName, prefix + m_objectNames.getName("isTightElectronBoosted"), isTightElectronBoosted)); 
    setConnectSucceeded(46, ConnectVariable( treeName, prefix + m_objectNames.getName("isHeepElectronBoosted"), isHeepElectronBoosted)); 
    setConnectSucceeded(47, ConnectVariable( treeName, prefix + m_objectNames.getName("isLooseElectronBoosted"), isLooseElectronBoosted)); 
} // end of detail level BoostedID

if(  ((detail_level & Ntuple::ElectronBoostedIsolation) == Ntuple::ElectronBoostedIsolation)  ) {
     setConnectSucceeded(48, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRhoCorrRelIso03Boost"), pfRhoCorrRelIso03Boost)); 
    setConnectSucceeded(49, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRhoCorrRelIso04Boost"), pfRhoCorrRelIso04Boost)); 
    setConnectSucceeded(50, ConnectVariable( treeName, prefix + m_objectNames.getName("pfDeltaCorrRelIsoBoost"), pfDeltaCorrRelIsoBoost)); 
    setConnectSucceeded(51, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRelIsoBoost"), pfRelIsoBoost)); 
    setConnectSucceeded(52, ConnectVariable( treeName, prefix + m_objectNames.getName("photonIsoBoost"), photonIsoBoost)); 
    setConnectSucceeded(53, ConnectVariable( treeName, prefix + m_objectNames.getName("neutralHadIsoBoost"), neutralHadIsoBoost)); 
    setConnectSucceeded(54, ConnectVariable( treeName, prefix + m_objectNames.getName("chargedHadIsoBoost"), chargedHadIsoBoost)); 
    setConnectSucceeded(55, ConnectVariable( treeName, prefix + m_objectNames.getName("SemileptonicPFIso"), SemileptonicPFIso)); 
    setConnectSucceeded(56, ConnectVariable( treeName, prefix + m_objectNames.getName("SemileptonicCorrPFIso"), SemileptonicCorrPFIso)); 
} // end of detail level BoostedIsolation

if(  ((detail_level & Ntuple::ElectronID) == Ntuple::ElectronID)  ) {
     setConnectSucceeded(4, ConnectVariable( treeName, prefix + m_objectNames.getName("isVetoElectron"), isVetoElectron)); 
    setConnectSucceeded(5, ConnectVariable( treeName, prefix + m_objectNames.getName("isMediumElectron"), isMediumElectron)); 
    setConnectSucceeded(6, ConnectVariable( treeName, prefix + m_objectNames.getName("isTightElectron"), isTightElectron)); 
    setConnectSucceeded(7, ConnectVariable( treeName, prefix + m_objectNames.getName("isMVAMediumElectron"), isMVAMediumElectron)); 
    setConnectSucceeded(8, ConnectVariable( treeName, prefix + m_objectNames.getName("isMVATightElectron"), isMVATightElectron)); 
    setConnectSucceeded(9, ConnectVariable( treeName, prefix + m_objectNames.getName("isHeepElectron"), isHeepElectron)); 
    setConnectSucceeded(10, ConnectVariable( treeName, prefix + m_objectNames.getName("isLooseElectron"), isLooseElectron)); 
} // end of detail level ID

if(  ((detail_level & Ntuple::ElectronIsolation) == Ntuple::ElectronIsolation)  ) {
     setConnectSucceeded(13, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRhoCorrRelIso03"), pfRhoCorrRelIso03)); 
    setConnectSucceeded(14, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRhoCorrRelIso04"), pfRhoCorrRelIso04)); 
    setConnectSucceeded(15, ConnectVariable( treeName, prefix + m_objectNames.getName("pfDeltaCorrRelIso"), pfDeltaCorrRelIso)); 
    setConnectSucceeded(16, ConnectVariable( treeName, prefix + m_objectNames.getName("pfRelIso"), pfRelIso)); 
    setConnectSucceeded(17, ConnectVariable( treeName, prefix + m_objectNames.getName("photonIso"), photonIso)); 
    setConnectSucceeded(18, ConnectVariable( treeName, prefix + m_objectNames.getName("neutralHadIso"), neutralHadIso)); 
    setConnectSucceeded(19, ConnectVariable( treeName, prefix + m_objectNames.getName("chargedHadIso"), chargedHadIso)); 
    setConnectSucceeded(20, ConnectVariable( treeName, prefix + m_objectNames.getName("trackIso"), trackIso)); 
} // end of detail level Isolation

if(  ((detail_level & Ntuple::ElectronSuperCluster) == Ntuple::ElectronSuperCluster)  ) {
     setConnectSucceeded(11, ConnectVariable( treeName, prefix + m_objectNames.getName("superCluster_eta"), superCluster_eta)); 
    setConnectSucceeded(12, ConnectVariable( treeName, prefix + m_objectNames.getName("superCluster_e"), superCluster_e)); 
}


        
    // save actual detail_level
    detailLevel = detail_level;

    return;

  }

} // namespace Ntuple
