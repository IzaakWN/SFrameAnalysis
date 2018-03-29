
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_Tau_H__
#define __UZHTOP_Tau_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "TauNtupleObject.h"


namespace Ntuple {
  class TauNtupleObject;
}

namespace UZH {
  
  /**
   *  @short Class that maps TauNtupleObjects to Tau Particle class
   *
   *        This class can be used to map the offline Tau information from
   *        TauNtupleObjects to UZH::Tau class. All particles inherit 
   *        from UZH::Particle.
   *
   *  @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class Tau : public Basic , public Particle  {
    
    public:
    
    // default constructor
    Tau();
    
    // default destructor
    ~Tau();
    
    // constructor with index
    Tau( const Ntuple::TauNtupleObject* ana, const Int_t idx );
    
    TLorentzVector* getTLV() const;
    TLorentzVector tlv() const;
    
    // variable definitions
    bool m_againstElectronVLooseMVA6;
    bool m_againstElectronLooseMVA6;
    bool m_againstElectronMediumMVA6;
    bool m_againstElectronTightMVA6;
    bool m_againstElectronVTightMVA6;
    bool m_againstMuonLoose3;
    bool m_againstMuonTight3;
    floatingnumber* m_againstElectronMVA6raw;
    floatingnumber* m_againstElectronMVA6category;
    floatingnumber* m_byCombinedIsolationDeltaBetaCorrRaw3Hits;
    bool m_byLooseCombinedIsolationDeltaBetaCorr3Hits;
    bool m_byMediumCombinedIsolationDeltaBetaCorr3Hits;
    bool m_byTightCombinedIsolationDeltaBetaCorr3Hits;
    floatingnumber* m_byIsolationMVArun2v1DBdR03oldDMwLTraw;
    floatingnumber* m_byIsolationMVArun2v1DBnewDMwLTraw;
    floatingnumber* m_byIsolationMVArun2v1DBoldDMwLTraw;
    floatingnumber* m_byIsolationMVArun2v1PWnewDMwLTraw;
    bool m_byVLooseIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byVLooseIsolationMVArun2v1DBnewDMwLT;
    bool m_byVLooseIsolationMVArun2v1DBoldDMwLT;
    bool m_byVLooseIsolationMVArun2v1PWnewDMwLT;
    bool m_byLooseIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byLooseIsolationMVArun2v1DBnewDMwLT;
    bool m_byLooseIsolationMVArun2v1DBoldDMwLT;
    bool m_byLooseIsolationMVArun2v1PWnewDMwLT;
    bool m_byMediumIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byMediumIsolationMVArun2v1DBnewDMwLT;
    bool m_byMediumIsolationMVArun2v1DBoldDMwLT;
    bool m_byMediumIsolationMVArun2v1PWnewDMwLT;
    bool m_byTightIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byTightIsolationMVArun2v1DBnewDMwLT;
    bool m_byTightIsolationMVArun2v1DBoldDMwLT;
    bool m_byTightIsolationMVArun2v1PWnewDMwLT;
    bool m_byVTightIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byVTightIsolationMVArun2v1DBnewDMwLT;
    bool m_byVTightIsolationMVArun2v1DBoldDMwLT;
    bool m_byVTightIsolationMVArun2v1PWnewDMwLT;
    bool m_byVVTightIsolationMVArun2v1DBdR03oldDMwLT;
    bool m_byVVTightIsolationMVArun2v1DBnewDMwLT;
    bool m_byVVTightIsolationMVArun2v1DBoldDMwLT;
    bool m_byVVTightIsolationMVArun2v1PWnewDMwLT;
    floatingnumber* m_chargedIsoPtSum;
    floatingnumber* m_neutralIsoPtSum;
    floatingnumber* m_puCorrPtSum;
    floatingnumber* m_chargedIsoPtSumdR03;
    floatingnumber* m_neutralIsoPtSumdR03;
    floatingnumber* m_photonPtSumOutsideSignalCone;
    floatingnumber* m_photonPtSumOutsideSignalConedR03;
    floatingnumber* m_byPhotonPtSumOutsideSignalCone;
    floatingnumber* m_chargedPionPt;
    floatingnumber* m_neutralPionPt;
    int* m_nPhoton;
    floatingnumber* m_ptWeightedDetaStrip;
    floatingnumber* m_ptWeightedDphiStrip;
    floatingnumber* m_ptWeightedDrSignal;
    floatingnumber* m_ptWeightedDrIsolation;
    floatingnumber* m_leadingTrackChi2;
    floatingnumber* m_leadingTrackPt;
    floatingnumber* m_eRatio;
    floatingnumber* m_dxy_Sig;
    floatingnumber* m_ip3d;
    floatingnumber* m_ip3d_Sig;
    bool m_hasSecondaryVertex;
    floatingnumber* m_decayDistMag;
    floatingnumber* m_flightLenthSig;
    floatingnumber* m_byIsolationMVArun2v2DBoldDMwLTraw;
    bool m_byVLooseIsolationMVArun2v2DBoldDMwLT;
    bool m_byLooseIsolationMVArun2v2DBoldDMwLT;
    bool m_byMediumIsolationMVArun2v2DBoldDMwLT;
    bool m_byTightIsolationMVArun2v2DBoldDMwLT;
    bool m_byVTightIsolationMVArun2v2DBoldDMwLT;
    bool m_byVVTightIsolationMVArun2v2DBoldDMwLT;
    int* m_pdgId;
    floatingnumber* m_charge;
    floatingnumber* m_d0;
    floatingnumber* m_dz;
    int* m_TauType;
    int* m_decayMode;
    bool m_decayModeFindingNewDMs;
    bool m_decayModeFinding;
    
    // there must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
    bool againstElectronVLooseMVA6() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronVLooseMVA6)) std::cout<<"againstElectronVLooseMVA6 not connected!"<<std::endl;*/ return (m_againstElectronVLooseMVA6); } 
    bool againstElectronLooseMVA6() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronLooseMVA6)) std::cout<<"againstElectronLooseMVA6 not connected!"<<std::endl;*/ return (m_againstElectronLooseMVA6); } 
    bool againstElectronMediumMVA6() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronMediumMVA6)) std::cout<<"againstElectronMediumMVA6 not connected!"<<std::endl;*/ return (m_againstElectronMediumMVA6); } 
    bool againstElectronTightMVA6() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronTightMVA6)) std::cout<<"againstElectronTightMVA6 not connected!"<<std::endl;*/ return (m_againstElectronTightMVA6); } 
    bool againstElectronVTightMVA6() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronVTightMVA6)) std::cout<<"againstElectronVTightMVA6 not connected!"<<std::endl;*/ return (m_againstElectronVTightMVA6); } 
    bool againstMuonLoose3() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstMuonLoose3)) std::cout<<"againstMuonLoose3 not connected!"<<std::endl;*/ return (m_againstMuonLoose3); } 
    bool againstMuonTight3() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstMuonTight3)) std::cout<<"againstMuonTight3 not connected!"<<std::endl;*/ return (m_againstMuonTight3); } 
    floatingnumber againstElectronMVA6raw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronMVA6raw)) std::cout<<"againstElectronMVA6raw not connected!"<<std::endl;*/ return *(m_againstElectronMVA6raw); } 
    floatingnumber againstElectronMVA6category() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kagainstElectronMVA6category)) std::cout<<"againstElectronMVA6category not connected!"<<std::endl;*/ return *(m_againstElectronMVA6category); } 
    floatingnumber byCombinedIsolationDeltaBetaCorrRaw3Hits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyCombinedIsolationDeltaBetaCorrRaw3Hits)) std::cout<<"byCombinedIsolationDeltaBetaCorrRaw3Hits not connected!"<<std::endl;*/ return *(m_byCombinedIsolationDeltaBetaCorrRaw3Hits); } 
    bool byLooseCombinedIsolationDeltaBetaCorr3Hits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseCombinedIsolationDeltaBetaCorr3Hits)) std::cout<<"byLooseCombinedIsolationDeltaBetaCorr3Hits not connected!"<<std::endl;*/ return (m_byLooseCombinedIsolationDeltaBetaCorr3Hits); } 
    bool byMediumCombinedIsolationDeltaBetaCorr3Hits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumCombinedIsolationDeltaBetaCorr3Hits)) std::cout<<"byMediumCombinedIsolationDeltaBetaCorr3Hits not connected!"<<std::endl;*/ return (m_byMediumCombinedIsolationDeltaBetaCorr3Hits); } 
    bool byTightCombinedIsolationDeltaBetaCorr3Hits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightCombinedIsolationDeltaBetaCorr3Hits)) std::cout<<"byTightCombinedIsolationDeltaBetaCorr3Hits not connected!"<<std::endl;*/ return (m_byTightCombinedIsolationDeltaBetaCorr3Hits); } 
    floatingnumber byIsolationMVArun2v1DBdR03oldDMwLTraw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyIsolationMVArun2v1DBdR03oldDMwLTraw)) std::cout<<"byIsolationMVArun2v1DBdR03oldDMwLTraw not connected!"<<std::endl;*/ return *(m_byIsolationMVArun2v1DBdR03oldDMwLTraw); } 
    floatingnumber byIsolationMVArun2v1DBnewDMwLTraw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyIsolationMVArun2v1DBnewDMwLTraw)) std::cout<<"byIsolationMVArun2v1DBnewDMwLTraw not connected!"<<std::endl;*/ return *(m_byIsolationMVArun2v1DBnewDMwLTraw); } 
    floatingnumber byIsolationMVArun2v1DBoldDMwLTraw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyIsolationMVArun2v1DBoldDMwLTraw)) std::cout<<"byIsolationMVArun2v1DBoldDMwLTraw not connected!"<<std::endl;*/ return *(m_byIsolationMVArun2v1DBoldDMwLTraw); } 
    floatingnumber byIsolationMVArun2v1PWnewDMwLTraw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyIsolationMVArun2v1PWnewDMwLTraw)) std::cout<<"byIsolationMVArun2v1PWnewDMwLTraw not connected!"<<std::endl;*/ return *(m_byIsolationMVArun2v1PWnewDMwLTraw); } 
    bool byVLooseIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVLooseIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byVLooseIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byVLooseIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byVLooseIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVLooseIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byVLooseIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byVLooseIsolationMVArun2v1DBnewDMwLT); } 
    bool byVLooseIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVLooseIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byVLooseIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVLooseIsolationMVArun2v1DBoldDMwLT); } 
    bool byVLooseIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVLooseIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byVLooseIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byVLooseIsolationMVArun2v1PWnewDMwLT); } 
    bool byLooseIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byLooseIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byLooseIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byLooseIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byLooseIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byLooseIsolationMVArun2v1DBnewDMwLT); } 
    bool byLooseIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byLooseIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byLooseIsolationMVArun2v1DBoldDMwLT); } 
    bool byLooseIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byLooseIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byLooseIsolationMVArun2v1PWnewDMwLT); } 
    bool byMediumIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byMediumIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byMediumIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byMediumIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byMediumIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byMediumIsolationMVArun2v1DBnewDMwLT); } 
    bool byMediumIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byMediumIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byMediumIsolationMVArun2v1DBoldDMwLT); } 
    bool byMediumIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byMediumIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byMediumIsolationMVArun2v1PWnewDMwLT); } 
    bool byTightIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byTightIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byTightIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byTightIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byTightIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byTightIsolationMVArun2v1DBnewDMwLT); } 
    bool byTightIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byTightIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byTightIsolationMVArun2v1DBoldDMwLT); } 
    bool byTightIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byTightIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byTightIsolationMVArun2v1PWnewDMwLT); } 
    bool byVTightIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVTightIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byVTightIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byVTightIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byVTightIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVTightIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byVTightIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byVTightIsolationMVArun2v1DBnewDMwLT); } 
    bool byVTightIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVTightIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byVTightIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVTightIsolationMVArun2v1DBoldDMwLT); } 
    bool byVTightIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVTightIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byVTightIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byVTightIsolationMVArun2v1PWnewDMwLT); } 
    bool byVVTightIsolationMVArun2v1DBdR03oldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVVTightIsolationMVArun2v1DBdR03oldDMwLT)) std::cout<<"byVVTightIsolationMVArun2v1DBdR03oldDMwLT not connected!"<<std::endl;*/ return (m_byVVTightIsolationMVArun2v1DBdR03oldDMwLT); } 
    bool byVVTightIsolationMVArun2v1DBnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVVTightIsolationMVArun2v1DBnewDMwLT)) std::cout<<"byVVTightIsolationMVArun2v1DBnewDMwLT not connected!"<<std::endl;*/ return (m_byVVTightIsolationMVArun2v1DBnewDMwLT); } 
    bool byVVTightIsolationMVArun2v1DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVVTightIsolationMVArun2v1DBoldDMwLT)) std::cout<<"byVVTightIsolationMVArun2v1DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVVTightIsolationMVArun2v1DBoldDMwLT); } 
    bool byVVTightIsolationMVArun2v1PWnewDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVVTightIsolationMVArun2v1PWnewDMwLT)) std::cout<<"byVVTightIsolationMVArun2v1PWnewDMwLT not connected!"<<std::endl;*/ return (m_byVVTightIsolationMVArun2v1PWnewDMwLT); } 
    floatingnumber chargedIsoPtSum() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kchargedIsoPtSum)) std::cout<<"chargedIsoPtSum not connected!"<<std::endl;*/ return *(m_chargedIsoPtSum); } 
    floatingnumber neutralIsoPtSum() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kneutralIsoPtSum)) std::cout<<"neutralIsoPtSum not connected!"<<std::endl;*/ return *(m_neutralIsoPtSum); } 
    floatingnumber puCorrPtSum() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kpuCorrPtSum)) std::cout<<"puCorrPtSum not connected!"<<std::endl;*/ return *(m_puCorrPtSum); } 
    floatingnumber chargedIsoPtSumdR03() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kchargedIsoPtSumdR03)) std::cout<<"chargedIsoPtSumdR03 not connected!"<<std::endl;*/ return *(m_chargedIsoPtSumdR03); } 
    floatingnumber neutralIsoPtSumdR03() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kneutralIsoPtSumdR03)) std::cout<<"neutralIsoPtSumdR03 not connected!"<<std::endl;*/ return *(m_neutralIsoPtSumdR03); } 
    floatingnumber photonPtSumOutsideSignalCone() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kphotonPtSumOutsideSignalCone)) std::cout<<"photonPtSumOutsideSignalCone not connected!"<<std::endl;*/ return *(m_photonPtSumOutsideSignalCone); } 
    floatingnumber photonPtSumOutsideSignalConedR03() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kphotonPtSumOutsideSignalConedR03)) std::cout<<"photonPtSumOutsideSignalConedR03 not connected!"<<std::endl;*/ return *(m_photonPtSumOutsideSignalConedR03); } 
    floatingnumber byPhotonPtSumOutsideSignalCone() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyPhotonPtSumOutsideSignalCone)) std::cout<<"byPhotonPtSumOutsideSignalCone not connected!"<<std::endl;*/ return *(m_byPhotonPtSumOutsideSignalCone); } 
    floatingnumber chargedPionPt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kchargedPionPt)) std::cout<<"chargedPionPt not connected!"<<std::endl;*/ return *(m_chargedPionPt); } 
    floatingnumber neutralPionPt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kneutralPionPt)) std::cout<<"neutralPionPt not connected!"<<std::endl;*/ return *(m_neutralPionPt); } 
    int nPhoton() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::knPhoton)) std::cout<<"nPhoton not connected!"<<std::endl;*/ return *(m_nPhoton); } 
    floatingnumber ptWeightedDetaStrip() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kptWeightedDetaStrip)) std::cout<<"ptWeightedDetaStrip not connected!"<<std::endl;*/ return *(m_ptWeightedDetaStrip); } 
    floatingnumber ptWeightedDphiStrip() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kptWeightedDphiStrip)) std::cout<<"ptWeightedDphiStrip not connected!"<<std::endl;*/ return *(m_ptWeightedDphiStrip); } 
    floatingnumber ptWeightedDrSignal() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kptWeightedDrSignal)) std::cout<<"ptWeightedDrSignal not connected!"<<std::endl;*/ return *(m_ptWeightedDrSignal); } 
    floatingnumber ptWeightedDrIsolation() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kptWeightedDrIsolation)) std::cout<<"ptWeightedDrIsolation not connected!"<<std::endl;*/ return *(m_ptWeightedDrIsolation); } 
    floatingnumber leadingTrackChi2() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kleadingTrackChi2)) std::cout<<"leadingTrackChi2 not connected!"<<std::endl;*/ return *(m_leadingTrackChi2); } 
    floatingnumber leadingTrackPt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kleadingTrackPt)) std::cout<<"leadingTrackPt not connected!"<<std::endl;*/ return *(m_leadingTrackPt); } 
    floatingnumber eRatio() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::keRatio)) std::cout<<"eRatio not connected!"<<std::endl;*/ return *(m_eRatio); } 
    floatingnumber dxy_Sig() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdxy_Sig)) std::cout<<"dxy_Sig not connected!"<<std::endl;*/ return *(m_dxy_Sig); } 
    floatingnumber ip3d() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kip3d)) std::cout<<"ip3d not connected!"<<std::endl;*/ return *(m_ip3d); } 
    floatingnumber ip3d_Sig() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kip3d_Sig)) std::cout<<"ip3d_Sig not connected!"<<std::endl;*/ return *(m_ip3d_Sig); } 
    bool hasSecondaryVertex() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::khasSecondaryVertex)) std::cout<<"hasSecondaryVertex not connected!"<<std::endl;*/ return (m_hasSecondaryVertex); } 
    floatingnumber decayDistMag() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdecayDistMag)) std::cout<<"decayDistMag not connected!"<<std::endl;*/ return *(m_decayDistMag); } 
    floatingnumber flightLenthSig() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kflightLenthSig)) std::cout<<"flightLenthSig not connected!"<<std::endl;*/ return *(m_flightLenthSig); } 
    floatingnumber byIsolationMVArun2v2DBoldDMwLTraw() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyIsolationMVArun2v2DBoldDMwLTraw)) std::cout<<"byIsolationMVArun2v2DBoldDMwLTraw not connected!"<<std::endl;*/ return *(m_byIsolationMVArun2v2DBoldDMwLTraw); } 
    bool byVLooseIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVLooseIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byVLooseIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVLooseIsolationMVArun2v2DBoldDMwLT); } 
    bool byLooseIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyLooseIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byLooseIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byLooseIsolationMVArun2v2DBoldDMwLT); } 
    bool byMediumIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyMediumIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byMediumIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byMediumIsolationMVArun2v2DBoldDMwLT); } 
    bool byTightIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyTightIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byTightIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byTightIsolationMVArun2v2DBoldDMwLT); } 
    bool byVTightIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVTightIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byVTightIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVTightIsolationMVArun2v2DBoldDMwLT); } 
    bool byVVTightIsolationMVArun2v2DBoldDMwLT() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kbyVVTightIsolationMVArun2v2DBoldDMwLT)) std::cout<<"byVVTightIsolationMVArun2v2DBoldDMwLT not connected!"<<std::endl;*/ return (m_byVVTightIsolationMVArun2v2DBoldDMwLT); } 
    int pdgId() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kpdgId)) std::cout<<"pdgId not connected!"<<std::endl;*/ return *(m_pdgId); } 
    floatingnumber charge() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kcharge)) std::cout<<"charge not connected!"<<std::endl;*/ return *(m_charge); } 
    floatingnumber d0() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kd0)) std::cout<<"d0 not connected!"<<std::endl;*/ return *(m_d0); } 
    floatingnumber dz() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdz)) std::cout<<"dz not connected!"<<std::endl;*/ return *(m_dz); } 
    int TauType() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kTauType)) std::cout<<"TauType not connected!"<<std::endl;*/ return *(m_TauType); } 
    int decayMode() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdecayMode)) std::cout<<"decayMode not connected!"<<std::endl;*/ return *(m_decayMode); } 
    bool decayModeFindingNewDMs() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdecayModeFindingNewDMs)) std::cout<<"decayModeFindingNewDMs not connected!"<<std::endl;*/ return (m_decayModeFindingNewDMs); } 
    bool decayModeFinding() const { /*if(!m_ana->getConnectSucceeded(Ntuple::TauNtupleObject::kdecayModeFinding)) std::cout<<"decayModeFinding not connected!"<<std::endl;*/ return (m_decayModeFinding); } 
        
    void againstElectronVLooseMVA6( const bool& val){ (m_againstElectronVLooseMVA6)=val; } 
    void againstElectronLooseMVA6( const bool& val){ (m_againstElectronLooseMVA6)=val; } 
    void againstElectronMediumMVA6( const bool& val){ (m_againstElectronMediumMVA6)=val; } 
    void againstElectronTightMVA6( const bool& val){ (m_againstElectronTightMVA6)=val; } 
    void againstElectronVTightMVA6( const bool& val){ (m_againstElectronVTightMVA6)=val; } 
    void againstMuonLoose3( const bool& val){ (m_againstMuonLoose3)=val; } 
    void againstMuonTight3( const bool& val){ (m_againstMuonTight3)=val; } 
    void againstElectronMVA6raw( const floatingnumber& val){ *(m_againstElectronMVA6raw)=val; } 
    void againstElectronMVA6category( const floatingnumber& val){ *(m_againstElectronMVA6category)=val; } 
    void byCombinedIsolationDeltaBetaCorrRaw3Hits( const floatingnumber& val){ *(m_byCombinedIsolationDeltaBetaCorrRaw3Hits)=val; } 
    void byLooseCombinedIsolationDeltaBetaCorr3Hits( const bool& val){ (m_byLooseCombinedIsolationDeltaBetaCorr3Hits)=val; } 
    void byMediumCombinedIsolationDeltaBetaCorr3Hits( const bool& val){ (m_byMediumCombinedIsolationDeltaBetaCorr3Hits)=val; } 
    void byTightCombinedIsolationDeltaBetaCorr3Hits( const bool& val){ (m_byTightCombinedIsolationDeltaBetaCorr3Hits)=val; } 
    void byIsolationMVArun2v1DBdR03oldDMwLTraw( const floatingnumber& val){ *(m_byIsolationMVArun2v1DBdR03oldDMwLTraw)=val; } 
    void byIsolationMVArun2v1DBnewDMwLTraw( const floatingnumber& val){ *(m_byIsolationMVArun2v1DBnewDMwLTraw)=val; } 
    void byIsolationMVArun2v1DBoldDMwLTraw( const floatingnumber& val){ *(m_byIsolationMVArun2v1DBoldDMwLTraw)=val; } 
    void byIsolationMVArun2v1PWnewDMwLTraw( const floatingnumber& val){ *(m_byIsolationMVArun2v1PWnewDMwLTraw)=val; } 
    void byVLooseIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byVLooseIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byVLooseIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byVLooseIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byVLooseIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byVLooseIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byVLooseIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byVLooseIsolationMVArun2v1PWnewDMwLT)=val; } 
    void byLooseIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byLooseIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byLooseIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byLooseIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byLooseIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byLooseIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byLooseIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byLooseIsolationMVArun2v1PWnewDMwLT)=val; } 
    void byMediumIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byMediumIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byMediumIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byMediumIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byMediumIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byMediumIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byMediumIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byMediumIsolationMVArun2v1PWnewDMwLT)=val; } 
    void byTightIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byTightIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byTightIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byTightIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byTightIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byTightIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byTightIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byTightIsolationMVArun2v1PWnewDMwLT)=val; } 
    void byVTightIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byVTightIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byVTightIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byVTightIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byVTightIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byVTightIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byVTightIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byVTightIsolationMVArun2v1PWnewDMwLT)=val; } 
    void byVVTightIsolationMVArun2v1DBdR03oldDMwLT( const bool& val){ (m_byVVTightIsolationMVArun2v1DBdR03oldDMwLT)=val; } 
    void byVVTightIsolationMVArun2v1DBnewDMwLT( const bool& val){ (m_byVVTightIsolationMVArun2v1DBnewDMwLT)=val; } 
    void byVVTightIsolationMVArun2v1DBoldDMwLT( const bool& val){ (m_byVVTightIsolationMVArun2v1DBoldDMwLT)=val; } 
    void byVVTightIsolationMVArun2v1PWnewDMwLT( const bool& val){ (m_byVVTightIsolationMVArun2v1PWnewDMwLT)=val; } 
    void chargedIsoPtSum( const floatingnumber& val){ *(m_chargedIsoPtSum)=val; } 
    void neutralIsoPtSum( const floatingnumber& val){ *(m_neutralIsoPtSum)=val; } 
    void puCorrPtSum( const floatingnumber& val){ *(m_puCorrPtSum)=val; } 
    void chargedIsoPtSumdR03( const floatingnumber& val){ *(m_chargedIsoPtSumdR03)=val; } 
    void neutralIsoPtSumdR03( const floatingnumber& val){ *(m_neutralIsoPtSumdR03)=val; } 
    void photonPtSumOutsideSignalCone( const floatingnumber& val){ *(m_photonPtSumOutsideSignalCone)=val; } 
    void photonPtSumOutsideSignalConedR03( const floatingnumber& val){ *(m_photonPtSumOutsideSignalConedR03)=val; } 
    void byPhotonPtSumOutsideSignalCone( const floatingnumber& val){ *(m_byPhotonPtSumOutsideSignalCone)=val; } 
    void chargedPionPt( const floatingnumber& val){ *(m_chargedPionPt)=val; } 
    void neutralPionPt( const floatingnumber& val){ *(m_neutralPionPt)=val; } 
    void nPhoton( const int& val){ *(m_nPhoton)=val; } 
    void ptWeightedDetaStrip( const floatingnumber& val){ *(m_ptWeightedDetaStrip)=val; } 
    void ptWeightedDphiStrip( const floatingnumber& val){ *(m_ptWeightedDphiStrip)=val; } 
    void ptWeightedDrSignal( const floatingnumber& val){ *(m_ptWeightedDrSignal)=val; } 
    void ptWeightedDrIsolation( const floatingnumber& val){ *(m_ptWeightedDrIsolation)=val; } 
    void leadingTrackChi2( const floatingnumber& val){ *(m_leadingTrackChi2)=val; } 
    void leadingTrackPt( const floatingnumber& val){ *(m_leadingTrackPt)=val; } 
    void eRatio( const floatingnumber& val){ *(m_eRatio)=val; } 
    void dxy_Sig( const floatingnumber& val){ *(m_dxy_Sig)=val; } 
    void ip3d( const floatingnumber& val){ *(m_ip3d)=val; } 
    void ip3d_Sig( const floatingnumber& val){ *(m_ip3d_Sig)=val; } 
    void hasSecondaryVertex( const bool& val){ (m_hasSecondaryVertex)=val; } 
    void decayDistMag( const floatingnumber& val){ *(m_decayDistMag)=val; } 
    void flightLenthSig( const floatingnumber& val){ *(m_flightLenthSig)=val; } 
    void byIsolationMVArun2v2DBoldDMwLTraw( const floatingnumber& val){ *(m_byIsolationMVArun2v2DBoldDMwLTraw)=val; } 
    void byVLooseIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byVLooseIsolationMVArun2v2DBoldDMwLT)=val; } 
    void byLooseIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byLooseIsolationMVArun2v2DBoldDMwLT)=val; } 
    void byMediumIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byMediumIsolationMVArun2v2DBoldDMwLT)=val; } 
    void byTightIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byTightIsolationMVArun2v2DBoldDMwLT)=val; } 
    void byVTightIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byVTightIsolationMVArun2v2DBoldDMwLT)=val; } 
    void byVVTightIsolationMVArun2v2DBoldDMwLT( const bool& val){ (m_byVVTightIsolationMVArun2v2DBoldDMwLT)=val; } 
    void pdgId( const int& val){ *(m_pdgId)=val; } 
    void charge( const floatingnumber& val){ *(m_charge)=val; } 
    void d0( const floatingnumber& val){ *(m_d0)=val; } 
    void dz( const floatingnumber& val){ *(m_dz)=val; } 
    void TauType( const int& val){ *(m_TauType)=val; } 
    void decayMode( const int& val){ *(m_decayMode)=val; } 
    void decayModeFindingNewDMs( const bool& val){ (m_decayModeFindingNewDMs)=val; } 
    void decayModeFinding( const bool& val){ (m_decayModeFinding)=val; } 
    
    
    private:
    
    const Ntuple::TauNtupleObject* m_ana;
    
  }; // class Tau
  
  typedef std::vector< Tau > TauVec;
  typedef std::vector< Tau >::iterator TauVecIt;
  typedef std::vector< Tau >::const_iterator TauVecConstIt;
  
  // sort Taus by pT
  bool operator<( const Tau& e1, const Tau& e2 );
  
  // function class to sort Tau vector contents by pT
  class sortTauPt {
    public:
      bool operator()( const Tau& e1, const Tau& e2 );
  };
  
} // end of namespace UZH

// output stream operator overloaded for Tau objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::Tau& rhs );

#endif //__UZH_Tau_H__
