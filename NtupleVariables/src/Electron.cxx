
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#include "../include/Electron.h"

using namespace std;
using namespace UZH;

Electron::Electron() { }
Electron::~Electron() { }

Electron::Electron( const Ntuple::ElectronNtupleObject* ana, const Int_t idx ) : Basic( idx ), Particle() {
  
  m_ana = ana;
  
  // copy variables defined in Particle.h
   m_pt = &((*ana->pt)[idx]); 
   m_eta = &((*ana->eta)[idx]); 
   m_phi = &((*ana->phi)[idx]); 
   m_m = &((*ana->m)[idx]); 
   m_e = &((*ana->e)[idx]); 
  
  m_lvl = ana->detailLevel;
  
  // copy rest of variables
  /*${ {AllNoBools:
  printf("acc#name#\n");if (ana->m_connectsucceeded[#index#]) {printf("?\n"); m_#name# = &((*ana->#name#)[idx]);}
  else {printf("fak\n"); m_#name# = new #type#(); *m_#name# = #default#; } }}
  */
  
  if(  ((ana->detailLevel & Ntuple::ElectronAdvancedID) == Ntuple::ElectronAdvancedID)  ) {
    if (ana->m_connectsucceeded[21]) m_passConversionVeto = &((*ana->passConversionVeto)[idx]); else m_passConversionVeto = 0; 
    if (ana->m_connectsucceeded[22]) m_full5x5_sigmaIetaIeta = &((*ana->full5x5_sigmaIetaIeta)[idx]); else m_full5x5_sigmaIetaIeta = 0; 
    if (ana->m_connectsucceeded[23]) m_dEtaIn = &((*ana->dEtaIn)[idx]); else m_dEtaIn = 0; 
    if (ana->m_connectsucceeded[24]) m_dPhiIn = &((*ana->dPhiIn)[idx]); else m_dPhiIn = 0; 
    if (ana->m_connectsucceeded[25]) m_hOverE = &((*ana->hOverE)[idx]); else m_hOverE = 0; 
    if (ana->m_connectsucceeded[26]) m_relIsoWithDBeta = &((*ana->relIsoWithDBeta)[idx]); else m_relIsoWithDBeta = 0; 
    if (ana->m_connectsucceeded[27]) m_ooEmooP = &((*ana->ooEmooP)[idx]); else m_ooEmooP = 0; 
    if (ana->m_connectsucceeded[28]) m_expectedMissingInnerHits = &((*ana->expectedMissingInnerHits)[idx]); else m_expectedMissingInnerHits = 0; 
    if (ana->m_connectsucceeded[29]) m_d0 = &((*ana->d0)[idx]); else m_d0 = 0; 
    if (ana->m_connectsucceeded[30]) m_dz = &((*ana->dz)[idx]); else m_dz = 0; 
    if (ana->m_connectsucceeded[31]) m_d0_allvertices = &((*ana->d0_allvertices)[idx]); else m_d0_allvertices = 0; 
    if (ana->m_connectsucceeded[32]) m_dz_allvertices = &((*ana->dz_allvertices)[idx]); else m_dz_allvertices = 0; 
    if (ana->m_connectsucceeded[33]) m_dr03EcalRecHitSumEt = &((*ana->dr03EcalRecHitSumEt)[idx]); else m_dr03EcalRecHitSumEt = 0; 
    if (ana->m_connectsucceeded[34]) m_dr03HcalDepth1TowerSumEt = &((*ana->dr03HcalDepth1TowerSumEt)[idx]); else m_dr03HcalDepth1TowerSumEt = 0; 
    if (ana->m_connectsucceeded[35]) m_rho = &((*ana->rho)[idx]); else m_rho = 0; 
    if (ana->m_connectsucceeded[36]) m_ecalDriven = ((*ana->ecalDriven)[idx]); else m_ecalDriven = 0; 
    if (ana->m_connectsucceeded[37]) m_dEtaInSeed = &((*ana->dEtaInSeed)[idx]); else m_dEtaInSeed = 0; 
    if (ana->m_connectsucceeded[38]) m_full5x5_e2x5Max = &((*ana->full5x5_e2x5Max)[idx]); else m_full5x5_e2x5Max = 0; 
    if (ana->m_connectsucceeded[39]) m_full5x5_e5x5 = &((*ana->full5x5_e5x5)[idx]); else m_full5x5_e5x5 = 0; 
    if (ana->m_connectsucceeded[40]) m_full5x5_e1x5 = &((*ana->full5x5_e1x5)[idx]); else m_full5x5_e1x5 = 0; 
    if (ana->m_connectsucceeded[41]) m_dr03TkSumPt = &((*ana->dr03TkSumPt)[idx]); else m_dr03TkSumPt = 0; 
    if (ana->m_connectsucceeded[42]) m_hadronicOverEm = &((*ana->hadronicOverEm)[idx]); else m_hadronicOverEm = 0; 
  } // end of detail level AdvancedID
  
  if(  ((ana->detailLevel & Ntuple::ElectronBasic) == Ntuple::ElectronBasic)  ) {
    if (ana->m_connectsucceeded[1]) m_pdgId = &((*ana->pdgId)[idx]); else m_pdgId = 0; 
    if (ana->m_connectsucceeded[2]) m_charge = &((*ana->charge)[idx]); else m_charge = 0; 
    if (ana->m_connectsucceeded[3]) m_et = &((*ana->et)[idx]); else m_et = 0; 
  } // end of detail level Basic
  
  if(  ((ana->detailLevel & Ntuple::ElectronBoostedIsolation) == Ntuple::ElectronBoostedIsolation)  ) {
    if (ana->m_connectsucceeded[43]) m_SemileptonicPFIso = &((*ana->SemileptonicPFIso)[idx]); else m_SemileptonicPFIso = 0; 
    if (ana->m_connectsucceeded[44]) m_SemileptonicCorrPFIso = &((*ana->SemileptonicCorrPFIso)[idx]); else m_SemileptonicCorrPFIso = 0; 
  } // end of detail level BoostedIsolation
  
  if(  ((ana->detailLevel & Ntuple::ElectronID) == Ntuple::ElectronID)  ) {
    if (ana->m_connectsucceeded[4]) m_isVetoElectron = &((*ana->isVetoElectron)[idx]); else m_isVetoElectron = 0; 
    if (ana->m_connectsucceeded[5]) m_isMediumElectron = &((*ana->isMediumElectron)[idx]); else m_isMediumElectron = 0; 
    if (ana->m_connectsucceeded[6]) m_isTightElectron = &((*ana->isTightElectron)[idx]); else m_isTightElectron = 0; 
    if (ana->m_connectsucceeded[7]) m_isMVAMediumElectron = &((*ana->isMVAMediumElectron)[idx]); else m_isMVAMediumElectron = 0; 
    if (ana->m_connectsucceeded[8]) m_isMVATightElectron = &((*ana->isMVATightElectron)[idx]); else m_isMVATightElectron = 0; 
    if (ana->m_connectsucceeded[9]) m_isHeepElectron = &((*ana->isHeepElectron)[idx]); else m_isHeepElectron = 0; 
    if (ana->m_connectsucceeded[10]) m_isLooseElectron = &((*ana->isLooseElectron)[idx]); else m_isLooseElectron = 0; 
  } // end of detail level ID
  
  if(  ((ana->detailLevel & Ntuple::ElectronIsolation) == Ntuple::ElectronIsolation)  ) {
    if (ana->m_connectsucceeded[13]) m_pfRhoCorrRelIso03 = &((*ana->pfRhoCorrRelIso03)[idx]); else m_pfRhoCorrRelIso03 = 0; 
    if (ana->m_connectsucceeded[14]) m_pfRhoCorrRelIso04 = &((*ana->pfRhoCorrRelIso04)[idx]); else m_pfRhoCorrRelIso04 = 0; 
    if (ana->m_connectsucceeded[15]) m_pfDeltaCorrRelIso = &((*ana->pfDeltaCorrRelIso)[idx]); else m_pfDeltaCorrRelIso = 0; 
    if (ana->m_connectsucceeded[16]) m_pfRelIso = &((*ana->pfRelIso)[idx]); else m_pfRelIso = 0; 
    if (ana->m_connectsucceeded[17]) m_photonIso = &((*ana->photonIso)[idx]); else m_photonIso = 0; 
    if (ana->m_connectsucceeded[18]) m_neutralHadIso = &((*ana->neutralHadIso)[idx]); else m_neutralHadIso = 0; 
    if (ana->m_connectsucceeded[19]) m_chargedHadIso = &((*ana->chargedHadIso)[idx]); else m_chargedHadIso = 0; 
    if (ana->m_connectsucceeded[20]) m_trackIso = &((*ana->trackIso)[idx]); else m_trackIso = 0; 
  } // end of detail level Isolation
  
  if(  ((ana->detailLevel & Ntuple::ElectronSuperCluster) == Ntuple::ElectronSuperCluster)  ) {
    if (ana->m_connectsucceeded[11]) m_superCluster_eta = &((*ana->superCluster_eta)[idx]); else m_superCluster_eta = 0; 
    if (ana->m_connectsucceeded[12]) m_superCluster_e = &((*ana->superCluster_e)[idx]); else m_superCluster_e = 0; 
  } // end of detail level SuperCluster
  
  //Set("clusterEuncorrected", cluster_e());
  //Set("EtCone20uncorrected", etcone20());
  
}


ostream& operator<<( ostream& out, const Electron& rhs ) {

  out << "Electron -" << ( Basic) rhs; 
  out << "Electron -" << ( Particle ) rhs; 
  
  if( ((rhs.getLvl() & Ntuple::ElectronAdvancedID) == Ntuple::ElectronAdvancedID) ) {
    out << " passConversionVeto " << rhs.passConversionVeto(); 
    out << " full5x5_sigmaIetaIeta " << rhs.full5x5_sigmaIetaIeta(); 
    out << " dEtaIn " << rhs.dEtaIn(); 
    out << " dPhiIn " << rhs.dPhiIn(); 
    out << " hOverE " << rhs.hOverE(); 
    out << " relIsoWithDBeta " << rhs.relIsoWithDBeta(); 
    out << " ooEmooP " << rhs.ooEmooP(); 
    out << " expectedMissingInnerHits " << rhs.expectedMissingInnerHits(); 
    out << " d0 " << rhs.d0(); 
    out << " dz " << rhs.dz(); 
    out << " d0_allvertices " << rhs.d0_allvertices(); 
    out << " dz_allvertices " << rhs.dz_allvertices(); 
    out << " dr03EcalRecHitSumEt " << rhs.dr03EcalRecHitSumEt(); 
    out << " dr03HcalDepth1TowerSumEt " << rhs.dr03HcalDepth1TowerSumEt(); 
    out << " rho " << rhs.rho(); 
    out << " ecalDriven " << rhs.ecalDriven(); 
    out << " dEtaInSeed " << rhs.dEtaInSeed(); 
    out << " full5x5_e2x5Max " << rhs.full5x5_e2x5Max(); 
    out << " full5x5_e5x5 " << rhs.full5x5_e5x5(); 
    out << " full5x5_e1x5 " << rhs.full5x5_e1x5(); 
    out << " dr03TkSumPt " << rhs.dr03TkSumPt(); 
    out << " hadronicOverEm " << rhs.hadronicOverEm(); 
  } // end of detail level AdvancedID
  
  if( ((rhs.getLvl() & Ntuple::ElectronBasic) == Ntuple::ElectronBasic) ) {
    out << " pdgId " << rhs.pdgId(); 
    out << " charge " << rhs.charge(); 
    out << " et " << rhs.et(); 
  } // end of detail level Basic
  
  if( ((rhs.getLvl() & Ntuple::ElectronBoostedIsolation) == Ntuple::ElectronBoostedIsolation) ) {
    out << " SemileptonicPFIso " << rhs.SemileptonicPFIso(); 
    out << " SemileptonicCorrPFIso " << rhs.SemileptonicCorrPFIso(); 
  } // end of detail level BoostedIsolation
  
  if( ((rhs.getLvl() & Ntuple::ElectronID) == Ntuple::ElectronID) ) {
    out << " isVetoElectron " << rhs.isVetoElectron(); 
    out << " isMediumElectron " << rhs.isMediumElectron(); 
    out << " isTightElectron " << rhs.isTightElectron(); 
    out << " isMVAMediumElectron " << rhs.isMVAMediumElectron(); 
    out << " isMVATightElectron " << rhs.isMVATightElectron(); 
    out << " isHeepElectron " << rhs.isHeepElectron(); 
    out << " isLooseElectron " << rhs.isLooseElectron(); 
  } // end of detail level ID
  
  if( ((rhs.getLvl() & Ntuple::ElectronIsolation) == Ntuple::ElectronIsolation) ) {
    out << " pfRhoCorrRelIso03 " << rhs.pfRhoCorrRelIso03(); 
    out << " pfRhoCorrRelIso04 " << rhs.pfRhoCorrRelIso04(); 
    out << " pfDeltaCorrRelIso " << rhs.pfDeltaCorrRelIso(); 
    out << " pfRelIso " << rhs.pfRelIso(); 
    out << " photonIso " << rhs.photonIso(); 
    out << " neutralHadIso " << rhs.neutralHadIso(); 
    out << " chargedHadIso " << rhs.chargedHadIso(); 
    out << " trackIso " << rhs.trackIso(); 
  } // end of detail level Isolation
  
  if( ((rhs.getLvl() & Ntuple::ElectronSuperCluster) == Ntuple::ElectronSuperCluster) ) {
    out << " superCluster_eta " << rhs.superCluster_eta(); 
    out << " superCluster_e " << rhs.superCluster_e(); 
  } // end of detail level SuperCluster
  
  return out;
}


bool sortElectronPt::operator()( const Electron& e1, const Electron& e2 ) {
  return ( e1.pt() > e2.pt() ) ? true : false;
}

bool operator<<( const Electron& e1, const Electron& e2 ) {
  sortElectronPt sort;
  return sort( e1, e2 );
}


TLorentzVector* Electron::getTLV() const {
  TLorentzVector* tlv = new TLorentzVector();
  tlv->SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}

TLorentzVector Electron::tlv() const {
  TLorentzVector tlv;
  tlv.SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}

