
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_Electron_H__
#define __UZHTOP_Electron_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "ElectronNtupleObject.h"



namespace Ntuple {
  class ElectronNtupleObject;
}

namespace UZH {
  
  /**
   *  @short Class that maps ElectronNtupleObjects to Electron Particle class
   *
   *         This class can be used to map the offline Electron information from
   *         ElectronNtupleObjects to UZH::Electron class. All particles inherit 
   *         from UZH::Particle.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class Electron : public Basic 
   , public Particle 
  {
  public:
  
    /// default c'tor
    Electron();
    /// default d'tor
    ~Electron();
    
    /// c'tor with index
    Electron( const Ntuple::ElectronNtupleObject* ana, const Int_t idx );
    
    TLorentzVector* getTLV() const;
    TLorentzVector tlv() const;
    
    
    
    // variable definitions
    
    
        int* m_passConversionVeto;
    floatingnumber* m_full5x5_sigmaIetaIeta;
    floatingnumber* m_dEtaIn;
    floatingnumber* m_dPhiIn;
    floatingnumber* m_hOverE;
    floatingnumber* m_relIsoWithDBeta;
    floatingnumber* m_ooEmooP;
    int* m_expectedMissingInnerHits;
    floatingnumber* m_d0;
    floatingnumber* m_dz;
    floatingnumber* m_d0_allvertices;
    floatingnumber* m_dz_allvertices;
    floatingnumber* m_dr03EcalRecHitSumEt;
    floatingnumber* m_dr03HcalDepth1TowerSumEt;
    floatingnumber* m_rho;
    bool m_ecalDriven;
    floatingnumber* m_dEtaInSeed;
    floatingnumber* m_full5x5_e2x5Max;
    floatingnumber* m_full5x5_e5x5;
    floatingnumber* m_full5x5_e1x5;
    floatingnumber* m_dr03TkSumPt;
    floatingnumber* m_hadronicOverEm;
    int* m_pdgId;
    floatingnumber* m_charge;
    floatingnumber* m_et;
    int* m_isVetoElectronBoosted;
    int* m_isMediumElectronBoosted;
    int* m_isTightElectronBoosted;
    int* m_isHeepElectronBoosted;
    int* m_isLooseElectronBoosted;
    floatingnumber* m_pfRhoCorrRelIso03Boost;
    floatingnumber* m_pfRhoCorrRelIso04Boost;
    floatingnumber* m_pfDeltaCorrRelIsoBoost;
    floatingnumber* m_pfRelIsoBoost;
    floatingnumber* m_photonIsoBoost;
    floatingnumber* m_neutralHadIsoBoost;
    floatingnumber* m_chargedHadIsoBoost;
    floatingnumber* m_SemileptonicPFIso;
    floatingnumber* m_SemileptonicCorrPFIso;
    int* m_isVetoElectron;
    int* m_isMediumElectron;
    int* m_isTightElectron;
    int* m_isMVAMediumElectron;
    int* m_isMVATightElectron;
    int* m_isHeepElectron;
    int* m_isLooseElectron;
    floatingnumber* m_pfRhoCorrRelIso03;
    floatingnumber* m_pfRhoCorrRelIso04;
    floatingnumber* m_pfDeltaCorrRelIso;
    floatingnumber* m_pfRelIso;
    floatingnumber* m_photonIso;
    floatingnumber* m_neutralHadIso;
    floatingnumber* m_chargedHadIso;
    floatingnumber* m_trackIso;
    floatingnumber* m_superCluster_eta;
    floatingnumber* m_superCluster_e;

    
    
    /// delta(R) function using the cluster eta/phi position of the electrons
    // floatingnumber DeltaRcluster( const Particle* p ) const;
    
    /// delta(R) function using the track eta/phi position of the electrons
    // floatingnumber DeltaRtrack( const Particle* p ) const;
    

    
    

    // check level given here must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
        int passConversionVeto() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpassConversionVeto)) std::cout<<"passConversionVeto not connected!"<<std::endl;*/ return *(m_passConversionVeto); } 
    floatingnumber full5x5_sigmaIetaIeta() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kfull5x5_sigmaIetaIeta)) std::cout<<"full5x5_sigmaIetaIeta not connected!"<<std::endl;*/ return *(m_full5x5_sigmaIetaIeta); } 
    floatingnumber dEtaIn() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdEtaIn)) std::cout<<"dEtaIn not connected!"<<std::endl;*/ return *(m_dEtaIn); } 
    floatingnumber dPhiIn() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdPhiIn)) std::cout<<"dPhiIn not connected!"<<std::endl;*/ return *(m_dPhiIn); } 
    floatingnumber hOverE() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::khOverE)) std::cout<<"hOverE not connected!"<<std::endl;*/ return *(m_hOverE); } 
    floatingnumber relIsoWithDBeta() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::krelIsoWithDBeta)) std::cout<<"relIsoWithDBeta not connected!"<<std::endl;*/ return *(m_relIsoWithDBeta); } 
    floatingnumber ooEmooP() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kooEmooP)) std::cout<<"ooEmooP not connected!"<<std::endl;*/ return *(m_ooEmooP); } 
    int expectedMissingInnerHits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kexpectedMissingInnerHits)) std::cout<<"expectedMissingInnerHits not connected!"<<std::endl;*/ return *(m_expectedMissingInnerHits); } 
    floatingnumber d0() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kd0)) std::cout<<"d0 not connected!"<<std::endl;*/ return *(m_d0); } 
    floatingnumber dz() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdz)) std::cout<<"dz not connected!"<<std::endl;*/ return *(m_dz); } 
    floatingnumber d0_allvertices() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kd0_allvertices)) std::cout<<"d0_allvertices not connected!"<<std::endl;*/ return *(m_d0_allvertices); } 
    floatingnumber dz_allvertices() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdz_allvertices)) std::cout<<"dz_allvertices not connected!"<<std::endl;*/ return *(m_dz_allvertices); } 
    floatingnumber dr03EcalRecHitSumEt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdr03EcalRecHitSumEt)) std::cout<<"dr03EcalRecHitSumEt not connected!"<<std::endl;*/ return *(m_dr03EcalRecHitSumEt); } 
    floatingnumber dr03HcalDepth1TowerSumEt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdr03HcalDepth1TowerSumEt)) std::cout<<"dr03HcalDepth1TowerSumEt not connected!"<<std::endl;*/ return *(m_dr03HcalDepth1TowerSumEt); } 
    floatingnumber rho() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::krho)) std::cout<<"rho not connected!"<<std::endl;*/ return *(m_rho); } 
    bool ecalDriven() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kecalDriven)) std::cout<<"ecalDriven not connected!"<<std::endl;*/ return (m_ecalDriven); } 
    floatingnumber dEtaInSeed() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdEtaInSeed)) std::cout<<"dEtaInSeed not connected!"<<std::endl;*/ return *(m_dEtaInSeed); } 
    floatingnumber full5x5_e2x5Max() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kfull5x5_e2x5Max)) std::cout<<"full5x5_e2x5Max not connected!"<<std::endl;*/ return *(m_full5x5_e2x5Max); } 
    floatingnumber full5x5_e5x5() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kfull5x5_e5x5)) std::cout<<"full5x5_e5x5 not connected!"<<std::endl;*/ return *(m_full5x5_e5x5); } 
    floatingnumber full5x5_e1x5() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kfull5x5_e1x5)) std::cout<<"full5x5_e1x5 not connected!"<<std::endl;*/ return *(m_full5x5_e1x5); } 
    floatingnumber dr03TkSumPt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kdr03TkSumPt)) std::cout<<"dr03TkSumPt not connected!"<<std::endl;*/ return *(m_dr03TkSumPt); } 
    floatingnumber hadronicOverEm() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::khadronicOverEm)) std::cout<<"hadronicOverEm not connected!"<<std::endl;*/ return *(m_hadronicOverEm); } 
    int pdgId() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpdgId)) std::cout<<"pdgId not connected!"<<std::endl;*/ return *(m_pdgId); } 
    floatingnumber charge() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kcharge)) std::cout<<"charge not connected!"<<std::endl;*/ return *(m_charge); } 
    floatingnumber et() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::ket)) std::cout<<"et not connected!"<<std::endl;*/ return *(m_et); } 
    int isVetoElectronBoosted() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisVetoElectronBoosted)) std::cout<<"isVetoElectronBoosted not connected!"<<std::endl;*/ return *(m_isVetoElectronBoosted); } 
    int isMediumElectronBoosted() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisMediumElectronBoosted)) std::cout<<"isMediumElectronBoosted not connected!"<<std::endl;*/ return *(m_isMediumElectronBoosted); } 
    int isTightElectronBoosted() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisTightElectronBoosted)) std::cout<<"isTightElectronBoosted not connected!"<<std::endl;*/ return *(m_isTightElectronBoosted); } 
    int isHeepElectronBoosted() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisHeepElectronBoosted)) std::cout<<"isHeepElectronBoosted not connected!"<<std::endl;*/ return *(m_isHeepElectronBoosted); } 
    int isLooseElectronBoosted() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisLooseElectronBoosted)) std::cout<<"isLooseElectronBoosted not connected!"<<std::endl;*/ return *(m_isLooseElectronBoosted); } 
    floatingnumber pfRhoCorrRelIso03Boost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRhoCorrRelIso03Boost)) std::cout<<"pfRhoCorrRelIso03Boost not connected!"<<std::endl;*/ return *(m_pfRhoCorrRelIso03Boost); } 
    floatingnumber pfRhoCorrRelIso04Boost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRhoCorrRelIso04Boost)) std::cout<<"pfRhoCorrRelIso04Boost not connected!"<<std::endl;*/ return *(m_pfRhoCorrRelIso04Boost); } 
    floatingnumber pfDeltaCorrRelIsoBoost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfDeltaCorrRelIsoBoost)) std::cout<<"pfDeltaCorrRelIsoBoost not connected!"<<std::endl;*/ return *(m_pfDeltaCorrRelIsoBoost); } 
    floatingnumber pfRelIsoBoost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRelIsoBoost)) std::cout<<"pfRelIsoBoost not connected!"<<std::endl;*/ return *(m_pfRelIsoBoost); } 
    floatingnumber photonIsoBoost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kphotonIsoBoost)) std::cout<<"photonIsoBoost not connected!"<<std::endl;*/ return *(m_photonIsoBoost); } 
    floatingnumber neutralHadIsoBoost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kneutralHadIsoBoost)) std::cout<<"neutralHadIsoBoost not connected!"<<std::endl;*/ return *(m_neutralHadIsoBoost); } 
    floatingnumber chargedHadIsoBoost() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kchargedHadIsoBoost)) std::cout<<"chargedHadIsoBoost not connected!"<<std::endl;*/ return *(m_chargedHadIsoBoost); } 
    floatingnumber SemileptonicPFIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kSemileptonicPFIso)) std::cout<<"SemileptonicPFIso not connected!"<<std::endl;*/ return *(m_SemileptonicPFIso); } 
    floatingnumber SemileptonicCorrPFIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kSemileptonicCorrPFIso)) std::cout<<"SemileptonicCorrPFIso not connected!"<<std::endl;*/ return *(m_SemileptonicCorrPFIso); } 
    int isVetoElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisVetoElectron)) std::cout<<"isVetoElectron not connected!"<<std::endl;*/ return *(m_isVetoElectron); } 
    int isMediumElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisMediumElectron)) std::cout<<"isMediumElectron not connected!"<<std::endl;*/ return *(m_isMediumElectron); } 
    int isTightElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisTightElectron)) std::cout<<"isTightElectron not connected!"<<std::endl;*/ return *(m_isTightElectron); } 
    int isMVAMediumElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisMVAMediumElectron)) std::cout<<"isMVAMediumElectron not connected!"<<std::endl;*/ return *(m_isMVAMediumElectron); } 
    int isMVATightElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisMVATightElectron)) std::cout<<"isMVATightElectron not connected!"<<std::endl;*/ return *(m_isMVATightElectron); } 
    int isHeepElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisHeepElectron)) std::cout<<"isHeepElectron not connected!"<<std::endl;*/ return *(m_isHeepElectron); } 
    int isLooseElectron() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kisLooseElectron)) std::cout<<"isLooseElectron not connected!"<<std::endl;*/ return *(m_isLooseElectron); } 
    floatingnumber pfRhoCorrRelIso03() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRhoCorrRelIso03)) std::cout<<"pfRhoCorrRelIso03 not connected!"<<std::endl;*/ return *(m_pfRhoCorrRelIso03); } 
    floatingnumber pfRhoCorrRelIso04() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRhoCorrRelIso04)) std::cout<<"pfRhoCorrRelIso04 not connected!"<<std::endl;*/ return *(m_pfRhoCorrRelIso04); } 
    floatingnumber pfDeltaCorrRelIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfDeltaCorrRelIso)) std::cout<<"pfDeltaCorrRelIso not connected!"<<std::endl;*/ return *(m_pfDeltaCorrRelIso); } 
    floatingnumber pfRelIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kpfRelIso)) std::cout<<"pfRelIso not connected!"<<std::endl;*/ return *(m_pfRelIso); } 
    floatingnumber photonIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kphotonIso)) std::cout<<"photonIso not connected!"<<std::endl;*/ return *(m_photonIso); } 
    floatingnumber neutralHadIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kneutralHadIso)) std::cout<<"neutralHadIso not connected!"<<std::endl;*/ return *(m_neutralHadIso); } 
    floatingnumber chargedHadIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::kchargedHadIso)) std::cout<<"chargedHadIso not connected!"<<std::endl;*/ return *(m_chargedHadIso); } 
    floatingnumber trackIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::ktrackIso)) std::cout<<"trackIso not connected!"<<std::endl;*/ return *(m_trackIso); } 
    floatingnumber superCluster_eta() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::ksuperCluster_eta)) std::cout<<"superCluster_eta not connected!"<<std::endl;*/ return *(m_superCluster_eta); } 
    floatingnumber superCluster_e() const { /*if(!m_ana->getConnectSucceeded(Ntuple::ElectronNtupleObject::ksuperCluster_e)) std::cout<<"superCluster_e not connected!"<<std::endl;*/ return *(m_superCluster_e); } 
    
        void passConversionVeto( const int& val){ *(m_passConversionVeto)=val; } 
    void full5x5_sigmaIetaIeta( const floatingnumber& val){ *(m_full5x5_sigmaIetaIeta)=val; } 
    void dEtaIn( const floatingnumber& val){ *(m_dEtaIn)=val; } 
    void dPhiIn( const floatingnumber& val){ *(m_dPhiIn)=val; } 
    void hOverE( const floatingnumber& val){ *(m_hOverE)=val; } 
    void relIsoWithDBeta( const floatingnumber& val){ *(m_relIsoWithDBeta)=val; } 
    void ooEmooP( const floatingnumber& val){ *(m_ooEmooP)=val; } 
    void expectedMissingInnerHits( const int& val){ *(m_expectedMissingInnerHits)=val; } 
    void d0( const floatingnumber& val){ *(m_d0)=val; } 
    void dz( const floatingnumber& val){ *(m_dz)=val; } 
    void d0_allvertices( const floatingnumber& val){ *(m_d0_allvertices)=val; } 
    void dz_allvertices( const floatingnumber& val){ *(m_dz_allvertices)=val; } 
    void dr03EcalRecHitSumEt( const floatingnumber& val){ *(m_dr03EcalRecHitSumEt)=val; } 
    void dr03HcalDepth1TowerSumEt( const floatingnumber& val){ *(m_dr03HcalDepth1TowerSumEt)=val; } 
    void rho( const floatingnumber& val){ *(m_rho)=val; } 
    void ecalDriven( const bool& val){ (m_ecalDriven)=val; } 
    void dEtaInSeed( const floatingnumber& val){ *(m_dEtaInSeed)=val; } 
    void full5x5_e2x5Max( const floatingnumber& val){ *(m_full5x5_e2x5Max)=val; } 
    void full5x5_e5x5( const floatingnumber& val){ *(m_full5x5_e5x5)=val; } 
    void full5x5_e1x5( const floatingnumber& val){ *(m_full5x5_e1x5)=val; } 
    void dr03TkSumPt( const floatingnumber& val){ *(m_dr03TkSumPt)=val; } 
    void hadronicOverEm( const floatingnumber& val){ *(m_hadronicOverEm)=val; } 
    void pdgId( const int& val){ *(m_pdgId)=val; } 
    void charge( const floatingnumber& val){ *(m_charge)=val; } 
    void et( const floatingnumber& val){ *(m_et)=val; } 
    void isVetoElectronBoosted( const int& val){ *(m_isVetoElectronBoosted)=val; } 
    void isMediumElectronBoosted( const int& val){ *(m_isMediumElectronBoosted)=val; } 
    void isTightElectronBoosted( const int& val){ *(m_isTightElectronBoosted)=val; } 
    void isHeepElectronBoosted( const int& val){ *(m_isHeepElectronBoosted)=val; } 
    void isLooseElectronBoosted( const int& val){ *(m_isLooseElectronBoosted)=val; } 
    void pfRhoCorrRelIso03Boost( const floatingnumber& val){ *(m_pfRhoCorrRelIso03Boost)=val; } 
    void pfRhoCorrRelIso04Boost( const floatingnumber& val){ *(m_pfRhoCorrRelIso04Boost)=val; } 
    void pfDeltaCorrRelIsoBoost( const floatingnumber& val){ *(m_pfDeltaCorrRelIsoBoost)=val; } 
    void pfRelIsoBoost( const floatingnumber& val){ *(m_pfRelIsoBoost)=val; } 
    void photonIsoBoost( const floatingnumber& val){ *(m_photonIsoBoost)=val; } 
    void neutralHadIsoBoost( const floatingnumber& val){ *(m_neutralHadIsoBoost)=val; } 
    void chargedHadIsoBoost( const floatingnumber& val){ *(m_chargedHadIsoBoost)=val; } 
    void SemileptonicPFIso( const floatingnumber& val){ *(m_SemileptonicPFIso)=val; } 
    void SemileptonicCorrPFIso( const floatingnumber& val){ *(m_SemileptonicCorrPFIso)=val; } 
    void isVetoElectron( const int& val){ *(m_isVetoElectron)=val; } 
    void isMediumElectron( const int& val){ *(m_isMediumElectron)=val; } 
    void isTightElectron( const int& val){ *(m_isTightElectron)=val; } 
    void isMVAMediumElectron( const int& val){ *(m_isMVAMediumElectron)=val; } 
    void isMVATightElectron( const int& val){ *(m_isMVATightElectron)=val; } 
    void isHeepElectron( const int& val){ *(m_isHeepElectron)=val; } 
    void isLooseElectron( const int& val){ *(m_isLooseElectron)=val; } 
    void pfRhoCorrRelIso03( const floatingnumber& val){ *(m_pfRhoCorrRelIso03)=val; } 
    void pfRhoCorrRelIso04( const floatingnumber& val){ *(m_pfRhoCorrRelIso04)=val; } 
    void pfDeltaCorrRelIso( const floatingnumber& val){ *(m_pfDeltaCorrRelIso)=val; } 
    void pfRelIso( const floatingnumber& val){ *(m_pfRelIso)=val; } 
    void photonIso( const floatingnumber& val){ *(m_photonIso)=val; } 
    void neutralHadIso( const floatingnumber& val){ *(m_neutralHadIso)=val; } 
    void chargedHadIso( const floatingnumber& val){ *(m_chargedHadIso)=val; } 
    void trackIso( const floatingnumber& val){ *(m_trackIso)=val; } 
    void superCluster_eta( const floatingnumber& val){ *(m_superCluster_eta)=val; } 
    void superCluster_e( const floatingnumber& val){ *(m_superCluster_e)=val; } 
    
    
  private:
    const Ntuple::ElectronNtupleObject* m_ana;
    
  }; // class Electron

  typedef std::vector< Electron > ElectronVec;
  typedef std::vector< Electron >::iterator ElectronVecIt;
  typedef std::vector< Electron >::const_iterator ElectronVecConstIt;

  
  /// sort Electrons by pT
  bool operator<( const Electron& e1, const Electron& e2 );

  /// function class to sort Electron vector contents by pT
  class sortElectronPt {
    public:
      bool operator()( const Electron& e1,
                       const Electron& e2 );
  };
  

} // end of namespace UZH

/// output stream operator overloaded for Electron objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::Electron& rhs );


#endif //__UZH_Electron_H__
