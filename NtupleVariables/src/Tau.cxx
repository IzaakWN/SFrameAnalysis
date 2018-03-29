
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#include "../include/Tau.h"

using namespace std;
using namespace UZH;

Tau::Tau() { }
Tau::~Tau() { }

Tau::Tau( const Ntuple::TauNtupleObject* ana, const Int_t idx ) : Basic( idx ), Particle() {
  
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
  
  if(  ((ana->detailLevel & Ntuple::TauAdvancedID) == Ntuple::TauAdvancedID)  ) {
    if (ana->m_connectsucceeded[9]) m_againstElectronVLooseMVA6 = ((*ana->againstElectronVLooseMVA6)[idx]); else m_againstElectronVLooseMVA6 = 0; 
    if (ana->m_connectsucceeded[10]) m_againstElectronLooseMVA6 = ((*ana->againstElectronLooseMVA6)[idx]); else m_againstElectronLooseMVA6 = 0; 
    if (ana->m_connectsucceeded[11]) m_againstElectronMediumMVA6 = ((*ana->againstElectronMediumMVA6)[idx]); else m_againstElectronMediumMVA6 = 0; 
    if (ana->m_connectsucceeded[12]) m_againstElectronTightMVA6 = ((*ana->againstElectronTightMVA6)[idx]); else m_againstElectronTightMVA6 = 0; 
    if (ana->m_connectsucceeded[13]) m_againstElectronVTightMVA6 = ((*ana->againstElectronVTightMVA6)[idx]); else m_againstElectronVTightMVA6 = 0; 
    if (ana->m_connectsucceeded[14]) m_againstMuonLoose3 = ((*ana->againstMuonLoose3)[idx]); else m_againstMuonLoose3 = 0; 
    if (ana->m_connectsucceeded[15]) m_againstMuonTight3 = ((*ana->againstMuonTight3)[idx]); else m_againstMuonTight3 = 0; 
    if (ana->m_connectsucceeded[16]) m_againstElectronMVA6raw = &((*ana->againstElectronMVA6raw)[idx]); else m_againstElectronMVA6raw = 0; 
    if (ana->m_connectsucceeded[17]) m_againstElectronMVA6category = &((*ana->againstElectronMVA6category)[idx]); else m_againstElectronMVA6category = 0; 
    if (ana->m_connectsucceeded[18]) m_byCombinedIsolationDeltaBetaCorrRaw3Hits = &((*ana->byCombinedIsolationDeltaBetaCorrRaw3Hits)[idx]); else m_byCombinedIsolationDeltaBetaCorrRaw3Hits = 0; 
    if (ana->m_connectsucceeded[19]) m_byLooseCombinedIsolationDeltaBetaCorr3Hits = ((*ana->byLooseCombinedIsolationDeltaBetaCorr3Hits)[idx]); else m_byLooseCombinedIsolationDeltaBetaCorr3Hits = 0; 
    if (ana->m_connectsucceeded[20]) m_byMediumCombinedIsolationDeltaBetaCorr3Hits = ((*ana->byMediumCombinedIsolationDeltaBetaCorr3Hits)[idx]); else m_byMediumCombinedIsolationDeltaBetaCorr3Hits = 0; 
    if (ana->m_connectsucceeded[21]) m_byTightCombinedIsolationDeltaBetaCorr3Hits = ((*ana->byTightCombinedIsolationDeltaBetaCorr3Hits)[idx]); else m_byTightCombinedIsolationDeltaBetaCorr3Hits = 0; 
    if (ana->m_connectsucceeded[22]) m_byIsolationMVArun2v1DBdR03oldDMwLTraw = &((*ana->byIsolationMVArun2v1DBdR03oldDMwLTraw)[idx]); else m_byIsolationMVArun2v1DBdR03oldDMwLTraw = 0; 
    if (ana->m_connectsucceeded[23]) m_byIsolationMVArun2v1DBnewDMwLTraw = &((*ana->byIsolationMVArun2v1DBnewDMwLTraw)[idx]); else m_byIsolationMVArun2v1DBnewDMwLTraw = 0; 
    if (ana->m_connectsucceeded[24]) m_byIsolationMVArun2v1DBoldDMwLTraw = &((*ana->byIsolationMVArun2v1DBoldDMwLTraw)[idx]); else m_byIsolationMVArun2v1DBoldDMwLTraw = 0; 
    if (ana->m_connectsucceeded[25]) m_byIsolationMVArun2v1PWnewDMwLTraw = &((*ana->byIsolationMVArun2v1PWnewDMwLTraw)[idx]); else m_byIsolationMVArun2v1PWnewDMwLTraw = 0; 
    if (ana->m_connectsucceeded[26]) m_byVLooseIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byVLooseIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byVLooseIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[27]) m_byVLooseIsolationMVArun2v1DBnewDMwLT = ((*ana->byVLooseIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byVLooseIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[28]) m_byVLooseIsolationMVArun2v1DBoldDMwLT = ((*ana->byVLooseIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byVLooseIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[29]) m_byVLooseIsolationMVArun2v1PWnewDMwLT = ((*ana->byVLooseIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byVLooseIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[30]) m_byLooseIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byLooseIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byLooseIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[31]) m_byLooseIsolationMVArun2v1DBnewDMwLT = ((*ana->byLooseIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byLooseIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[32]) m_byLooseIsolationMVArun2v1DBoldDMwLT = ((*ana->byLooseIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byLooseIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[33]) m_byLooseIsolationMVArun2v1PWnewDMwLT = ((*ana->byLooseIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byLooseIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[34]) m_byMediumIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byMediumIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byMediumIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[35]) m_byMediumIsolationMVArun2v1DBnewDMwLT = ((*ana->byMediumIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byMediumIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[36]) m_byMediumIsolationMVArun2v1DBoldDMwLT = ((*ana->byMediumIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byMediumIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[37]) m_byMediumIsolationMVArun2v1PWnewDMwLT = ((*ana->byMediumIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byMediumIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[38]) m_byTightIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byTightIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byTightIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[39]) m_byTightIsolationMVArun2v1DBnewDMwLT = ((*ana->byTightIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byTightIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[40]) m_byTightIsolationMVArun2v1DBoldDMwLT = ((*ana->byTightIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byTightIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[41]) m_byTightIsolationMVArun2v1PWnewDMwLT = ((*ana->byTightIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byTightIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[42]) m_byVTightIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byVTightIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byVTightIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[43]) m_byVTightIsolationMVArun2v1DBnewDMwLT = ((*ana->byVTightIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byVTightIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[44]) m_byVTightIsolationMVArun2v1DBoldDMwLT = ((*ana->byVTightIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byVTightIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[45]) m_byVTightIsolationMVArun2v1PWnewDMwLT = ((*ana->byVTightIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byVTightIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[46]) m_byVVTightIsolationMVArun2v1DBdR03oldDMwLT = ((*ana->byVVTightIsolationMVArun2v1DBdR03oldDMwLT)[idx]); else m_byVVTightIsolationMVArun2v1DBdR03oldDMwLT = 0; 
    if (ana->m_connectsucceeded[47]) m_byVVTightIsolationMVArun2v1DBnewDMwLT = ((*ana->byVVTightIsolationMVArun2v1DBnewDMwLT)[idx]); else m_byVVTightIsolationMVArun2v1DBnewDMwLT = 0; 
    if (ana->m_connectsucceeded[48]) m_byVVTightIsolationMVArun2v1DBoldDMwLT = ((*ana->byVVTightIsolationMVArun2v1DBoldDMwLT)[idx]); else m_byVVTightIsolationMVArun2v1DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[49]) m_byVVTightIsolationMVArun2v1PWnewDMwLT = ((*ana->byVVTightIsolationMVArun2v1PWnewDMwLT)[idx]); else m_byVVTightIsolationMVArun2v1PWnewDMwLT = 0; 
    if (ana->m_connectsucceeded[57]) m_chargedIsoPtSum = &((*ana->chargedIsoPtSum)[idx]); else m_chargedIsoPtSum = 0; 
    if (ana->m_connectsucceeded[58]) m_neutralIsoPtSum = &((*ana->neutralIsoPtSum)[idx]); else m_neutralIsoPtSum = 0; 
    if (ana->m_connectsucceeded[59]) m_puCorrPtSum = &((*ana->puCorrPtSum)[idx]); else m_puCorrPtSum = 0; 
    if (ana->m_connectsucceeded[60]) m_chargedIsoPtSumdR03 = &((*ana->chargedIsoPtSumdR03)[idx]); else m_chargedIsoPtSumdR03 = 0; 
    if (ana->m_connectsucceeded[61]) m_neutralIsoPtSumdR03 = &((*ana->neutralIsoPtSumdR03)[idx]); else m_neutralIsoPtSumdR03 = 0; 
    if (ana->m_connectsucceeded[62]) m_photonPtSumOutsideSignalCone = &((*ana->photonPtSumOutsideSignalCone)[idx]); else m_photonPtSumOutsideSignalCone = 0; 
    if (ana->m_connectsucceeded[63]) m_photonPtSumOutsideSignalConedR03 = &((*ana->photonPtSumOutsideSignalConedR03)[idx]); else m_photonPtSumOutsideSignalConedR03 = 0; 
    if (ana->m_connectsucceeded[64]) m_byPhotonPtSumOutsideSignalCone = &((*ana->byPhotonPtSumOutsideSignalCone)[idx]); else m_byPhotonPtSumOutsideSignalCone = 0; 
    if (ana->m_connectsucceeded[65]) m_chargedPionPt = &((*ana->chargedPionPt)[idx]); else m_chargedPionPt = 0; 
    if (ana->m_connectsucceeded[66]) m_neutralPionPt = &((*ana->neutralPionPt)[idx]); else m_neutralPionPt = 0; 
    if (ana->m_connectsucceeded[67]) m_nPhoton = &((*ana->nPhoton)[idx]); else m_nPhoton = 0; 
    if (ana->m_connectsucceeded[68]) m_ptWeightedDetaStrip = &((*ana->ptWeightedDetaStrip)[idx]); else m_ptWeightedDetaStrip = 0; 
    if (ana->m_connectsucceeded[69]) m_ptWeightedDphiStrip = &((*ana->ptWeightedDphiStrip)[idx]); else m_ptWeightedDphiStrip = 0; 
    if (ana->m_connectsucceeded[70]) m_ptWeightedDrSignal = &((*ana->ptWeightedDrSignal)[idx]); else m_ptWeightedDrSignal = 0; 
    if (ana->m_connectsucceeded[71]) m_ptWeightedDrIsolation = &((*ana->ptWeightedDrIsolation)[idx]); else m_ptWeightedDrIsolation = 0; 
    if (ana->m_connectsucceeded[72]) m_leadingTrackChi2 = &((*ana->leadingTrackChi2)[idx]); else m_leadingTrackChi2 = 0; 
    if (ana->m_connectsucceeded[73]) m_leadingTrackPt = &((*ana->leadingTrackPt)[idx]); else m_leadingTrackPt = 0; 
    if (ana->m_connectsucceeded[74]) m_eRatio = &((*ana->eRatio)[idx]); else m_eRatio = 0; 
    if (ana->m_connectsucceeded[75]) m_dxy_Sig = &((*ana->dxy_Sig)[idx]); else m_dxy_Sig = 0; 
    if (ana->m_connectsucceeded[76]) m_ip3d = &((*ana->ip3d)[idx]); else m_ip3d = 0; 
    if (ana->m_connectsucceeded[77]) m_ip3d_Sig = &((*ana->ip3d_Sig)[idx]); else m_ip3d_Sig = 0; 
    if (ana->m_connectsucceeded[78]) m_hasSecondaryVertex = ((*ana->hasSecondaryVertex)[idx]); else m_hasSecondaryVertex = 0; 
    if (ana->m_connectsucceeded[79]) m_decayDistMag = &((*ana->decayDistMag)[idx]); else m_decayDistMag = 0; 
    if (ana->m_connectsucceeded[80]) m_flightLenthSig = &((*ana->flightLenthSig)[idx]); else m_flightLenthSig = 0; 
  } // end of detail level AdvancedID
  
  if(  ((ana->detailLevel & Ntuple::TauAdvancedIDv2) == Ntuple::TauAdvancedIDv2)  ) {
    if (ana->m_connectsucceeded[50]) m_byIsolationMVArun2v2DBoldDMwLTraw = &((*ana->byIsolationMVArun2v2DBoldDMwLTraw)[idx]); else m_byIsolationMVArun2v2DBoldDMwLTraw = 0; 
    if (ana->m_connectsucceeded[51]) m_byVLooseIsolationMVArun2v2DBoldDMwLT = ((*ana->byVLooseIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byVLooseIsolationMVArun2v2DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[52]) m_byLooseIsolationMVArun2v2DBoldDMwLT = ((*ana->byLooseIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byLooseIsolationMVArun2v2DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[53]) m_byMediumIsolationMVArun2v2DBoldDMwLT = ((*ana->byMediumIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byMediumIsolationMVArun2v2DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[54]) m_byTightIsolationMVArun2v2DBoldDMwLT = ((*ana->byTightIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byTightIsolationMVArun2v2DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[55]) m_byVTightIsolationMVArun2v2DBoldDMwLT = ((*ana->byVTightIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byVTightIsolationMVArun2v2DBoldDMwLT = 0; 
    if (ana->m_connectsucceeded[56]) m_byVVTightIsolationMVArun2v2DBoldDMwLT = ((*ana->byVVTightIsolationMVArun2v2DBoldDMwLT)[idx]); else m_byVVTightIsolationMVArun2v2DBoldDMwLT = 0; 
  } // end of detail level AdvancedIDv2
  
  if(  ((ana->detailLevel & Ntuple::TauBasic) == Ntuple::TauBasic)  ) {
    if (ana->m_connectsucceeded[1]) m_pdgId = &((*ana->pdgId)[idx]); else m_pdgId = 0; 
    if (ana->m_connectsucceeded[2]) m_charge = &((*ana->charge)[idx]); else m_charge = 0; 
    if (ana->m_connectsucceeded[3]) m_d0 = &((*ana->d0)[idx]); else m_d0 = 0; 
    if (ana->m_connectsucceeded[4]) m_dz = &((*ana->dz)[idx]); else m_dz = 0; 
  } // end of detail level Basic
  
  if(  ((ana->detailLevel & Ntuple::TauID) == Ntuple::TauID)  ) {
    if (ana->m_connectsucceeded[5]) m_TauType = &((*ana->TauType)[idx]); else m_TauType = 0; 
    if (ana->m_connectsucceeded[6]) m_decayMode = &((*ana->decayMode)[idx]); else m_decayMode = 0; 
    if (ana->m_connectsucceeded[7]) m_decayModeFindingNewDMs = ((*ana->decayModeFindingNewDMs)[idx]); else m_decayModeFindingNewDMs = 0; 
    if (ana->m_connectsucceeded[8]) m_decayModeFinding = ((*ana->decayModeFinding)[idx]); else m_decayModeFinding = 0; 
  } // end of detail level ID
  
}


ostream& operator<<( ostream& out, const Tau& rhs ) {

  out << "Tau -" << ( Basic) rhs; 
  
  if( ((rhs.getLvl() & Ntuple::TauAdvancedID) == Ntuple::TauAdvancedID) ) {
    out << " againstElectronVLooseMVA6 " << rhs.againstElectronVLooseMVA6(); 
    out << " againstElectronLooseMVA6 " << rhs.againstElectronLooseMVA6(); 
    out << " againstElectronMediumMVA6 " << rhs.againstElectronMediumMVA6(); 
    out << " againstElectronTightMVA6 " << rhs.againstElectronTightMVA6(); 
    out << " againstElectronVTightMVA6 " << rhs.againstElectronVTightMVA6(); 
    out << " againstMuonLoose3 " << rhs.againstMuonLoose3(); 
    out << " againstMuonTight3 " << rhs.againstMuonTight3(); 
    out << " againstElectronMVA6raw " << rhs.againstElectronMVA6raw(); 
    out << " againstElectronMVA6category " << rhs.againstElectronMVA6category(); 
    out << " byCombinedIsolationDeltaBetaCorrRaw3Hits " << rhs.byCombinedIsolationDeltaBetaCorrRaw3Hits(); 
    out << " byLooseCombinedIsolationDeltaBetaCorr3Hits " << rhs.byLooseCombinedIsolationDeltaBetaCorr3Hits(); 
    out << " byMediumCombinedIsolationDeltaBetaCorr3Hits " << rhs.byMediumCombinedIsolationDeltaBetaCorr3Hits(); 
    out << " byTightCombinedIsolationDeltaBetaCorr3Hits " << rhs.byTightCombinedIsolationDeltaBetaCorr3Hits(); 
    out << " byIsolationMVArun2v1DBdR03oldDMwLTraw " << rhs.byIsolationMVArun2v1DBdR03oldDMwLTraw(); 
    out << " byIsolationMVArun2v1DBnewDMwLTraw " << rhs.byIsolationMVArun2v1DBnewDMwLTraw(); 
    out << " byIsolationMVArun2v1DBoldDMwLTraw " << rhs.byIsolationMVArun2v1DBoldDMwLTraw(); 
    out << " byIsolationMVArun2v1PWnewDMwLTraw " << rhs.byIsolationMVArun2v1PWnewDMwLTraw(); 
    out << " byVLooseIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byVLooseIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byVLooseIsolationMVArun2v1DBnewDMwLT " << rhs.byVLooseIsolationMVArun2v1DBnewDMwLT(); 
    out << " byVLooseIsolationMVArun2v1DBoldDMwLT " << rhs.byVLooseIsolationMVArun2v1DBoldDMwLT(); 
    out << " byVLooseIsolationMVArun2v1PWnewDMwLT " << rhs.byVLooseIsolationMVArun2v1PWnewDMwLT(); 
    out << " byLooseIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byLooseIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byLooseIsolationMVArun2v1DBnewDMwLT " << rhs.byLooseIsolationMVArun2v1DBnewDMwLT(); 
    out << " byLooseIsolationMVArun2v1DBoldDMwLT " << rhs.byLooseIsolationMVArun2v1DBoldDMwLT(); 
    out << " byLooseIsolationMVArun2v1PWnewDMwLT " << rhs.byLooseIsolationMVArun2v1PWnewDMwLT(); 
    out << " byMediumIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byMediumIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byMediumIsolationMVArun2v1DBnewDMwLT " << rhs.byMediumIsolationMVArun2v1DBnewDMwLT(); 
    out << " byMediumIsolationMVArun2v1DBoldDMwLT " << rhs.byMediumIsolationMVArun2v1DBoldDMwLT(); 
    out << " byMediumIsolationMVArun2v1PWnewDMwLT " << rhs.byMediumIsolationMVArun2v1PWnewDMwLT(); 
    out << " byTightIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byTightIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byTightIsolationMVArun2v1DBnewDMwLT " << rhs.byTightIsolationMVArun2v1DBnewDMwLT(); 
    out << " byTightIsolationMVArun2v1DBoldDMwLT " << rhs.byTightIsolationMVArun2v1DBoldDMwLT(); 
    out << " byTightIsolationMVArun2v1PWnewDMwLT " << rhs.byTightIsolationMVArun2v1PWnewDMwLT(); 
    out << " byVTightIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byVTightIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byVTightIsolationMVArun2v1DBnewDMwLT " << rhs.byVTightIsolationMVArun2v1DBnewDMwLT(); 
    out << " byVTightIsolationMVArun2v1DBoldDMwLT " << rhs.byVTightIsolationMVArun2v1DBoldDMwLT(); 
    out << " byVTightIsolationMVArun2v1PWnewDMwLT " << rhs.byVTightIsolationMVArun2v1PWnewDMwLT(); 
    out << " byVVTightIsolationMVArun2v1DBdR03oldDMwLT " << rhs.byVVTightIsolationMVArun2v1DBdR03oldDMwLT(); 
    out << " byVVTightIsolationMVArun2v1DBnewDMwLT " << rhs.byVVTightIsolationMVArun2v1DBnewDMwLT(); 
    out << " byVVTightIsolationMVArun2v1DBoldDMwLT " << rhs.byVVTightIsolationMVArun2v1DBoldDMwLT(); 
    out << " byVVTightIsolationMVArun2v1PWnewDMwLT " << rhs.byVVTightIsolationMVArun2v1PWnewDMwLT(); 
    out << " chargedIsoPtSum " << rhs.chargedIsoPtSum(); 
    out << " neutralIsoPtSum " << rhs.neutralIsoPtSum(); 
    out << " puCorrPtSum " << rhs.puCorrPtSum(); 
    out << " chargedIsoPtSumdR03 " << rhs.chargedIsoPtSumdR03(); 
    out << " neutralIsoPtSumdR03 " << rhs.neutralIsoPtSumdR03(); 
    out << " photonPtSumOutsideSignalCone " << rhs.photonPtSumOutsideSignalCone(); 
    out << " photonPtSumOutsideSignalConedR03 " << rhs.photonPtSumOutsideSignalConedR03(); 
    out << " byPhotonPtSumOutsideSignalCone " << rhs.byPhotonPtSumOutsideSignalCone(); 
    out << " chargedPionPt " << rhs.chargedPionPt(); 
    out << " neutralPionPt " << rhs.neutralPionPt(); 
    out << " nPhoton " << rhs.nPhoton(); 
    out << " ptWeightedDetaStrip " << rhs.ptWeightedDetaStrip(); 
    out << " ptWeightedDphiStrip " << rhs.ptWeightedDphiStrip(); 
    out << " ptWeightedDrSignal " << rhs.ptWeightedDrSignal(); 
    out << " ptWeightedDrIsolation " << rhs.ptWeightedDrIsolation(); 
    out << " leadingTrackChi2 " << rhs.leadingTrackChi2(); 
    out << " leadingTrackPt " << rhs.leadingTrackPt(); 
    out << " eRatio " << rhs.eRatio(); 
    out << " dxy_Sig " << rhs.dxy_Sig(); 
    out << " ip3d " << rhs.ip3d(); 
    out << " ip3d_Sig " << rhs.ip3d_Sig(); 
    out << " hasSecondaryVertex " << rhs.hasSecondaryVertex(); 
    out << " decayDistMag " << rhs.decayDistMag(); 
    out << " flightLenthSig " << rhs.flightLenthSig(); 
  } // end of detail level AdvancedID
  
  if( ((rhs.getLvl() & Ntuple::TauAdvancedIDv2) == Ntuple::TauAdvancedIDv2) ) {
    out << " byIsolationMVArun2v2DBoldDMwLTraw " << rhs.byIsolationMVArun2v2DBoldDMwLTraw(); 
    out << " byVLooseIsolationMVArun2v2DBoldDMwLT " << rhs.byVLooseIsolationMVArun2v2DBoldDMwLT(); 
    out << " byLooseIsolationMVArun2v2DBoldDMwLT " << rhs.byLooseIsolationMVArun2v2DBoldDMwLT(); 
    out << " byMediumIsolationMVArun2v2DBoldDMwLT " << rhs.byMediumIsolationMVArun2v2DBoldDMwLT(); 
    out << " byTightIsolationMVArun2v2DBoldDMwLT " << rhs.byTightIsolationMVArun2v2DBoldDMwLT(); 
    out << " byVTightIsolationMVArun2v2DBoldDMwLT " << rhs.byVTightIsolationMVArun2v2DBoldDMwLT(); 
    out << " byVVTightIsolationMVArun2v2DBoldDMwLT " << rhs.byVVTightIsolationMVArun2v2DBoldDMwLT(); 
  } // end of detail level AdvancedIDv2
  
  if( ((rhs.getLvl() & Ntuple::TauBasic) == Ntuple::TauBasic) ) {
    out << " pdgId " << rhs.pdgId(); 
    out << " charge " << rhs.charge(); 
    out << " d0 " << rhs.d0(); 
    out << " dz " << rhs.dz(); 
  } // end of detail level Basic
  
  if( ((rhs.getLvl() & Ntuple::TauID) == Ntuple::TauID) ) {
    out << " TauType " << rhs.TauType(); 
    out << " decayMode " << rhs.decayMode(); 
    out << " decayModeFindingNewDMs " << rhs.decayModeFindingNewDMs(); 
    out << " decayModeFinding " << rhs.decayModeFinding(); 
  } // end of detail level ID
  
  return out;
}


bool sortTauPt::operator()( const Tau& e1, const Tau& e2 ) {
  return ( e1.pt() > e2.pt() ) ? true : false;
}

bool operator<<( const Tau& e1, const Tau& e2 ) {
  sortTauPt sort;
  return sort( e1, e2 );
}


TLorentzVector* Tau::getTLV() const {
  TLorentzVector* tlv = new TLorentzVector();
  tlv->SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}

TLorentzVector Tau::tlv() const {
  TLorentzVector tlv;
  tlv.SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;
}

