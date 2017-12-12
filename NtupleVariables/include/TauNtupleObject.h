// Dear emacs, this is -*- c++ -*-
// $Id: TauNtupleObject.h 37457 2010-07-05 12:04:33Z mann $

// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 


#ifndef SFRAME_NtupleVARIABLES_TauNtupleObject_H
#define SFRAME_NtupleVARIABLES_TauNtupleObject_H

// Local include(s):
#include "NtupleObjectNames.h"

// STL include(s):
#include <vector>
#include <string>

// ROOT include(s):
#include <TString.h>

// SFrame include(s):
#include "core/include/SError.h"
#include "core/include/SCycleBaseNTuple.h"
#include "plug-ins/include/SInputVariables.h"

namespace Ntuple {
  
  /**
   *  @short Class that can read the variables produced by TauNtupleObject
   *
   *        This class can be used to read the offline muon information from
   *        an ntuple produced by the SingleTopDPDMaker code.
   *
   *  @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
   *
   */
  
  enum TauDetails {
    TauBasic = 1,
    TauID = 2,
    TauAdvancedID = 4,
    TauAll = 7,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class TauNtupleObject : public SInputVariables< SCycleBaseNTuple > {
    
    public:
    
    // constructor specifying the parent of the object
    TauNtupleObject( SCycleBaseNTuple* parent );
    
    // remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  
    
    // connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "Tau_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "Tau_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    int getDetailLevel() const { return detailLevel; }
    
    // particle vector size
    Int_t N;
    
    enum ConnectionIndex { 
      kdecayModeFindingNewDMs = 7,
      kdecayModeFinding = 8,
      kbyLooseCombinedIsolationDeltaBetaCorr3Hits = 9,
      kbyMediumCombinedIsolationDeltaBetaCorr3Hits = 10,
      kbyTightCombinedIsolationDeltaBetaCorr3Hits = 11,
      kbyCombinedIsolationDeltaBetaCorrRaw3Hits = 12,
      kchargedIsoPtSum = 13,
      kneutralIsoPtSum = 14,
      kpuCorrPtSum = 15,
      kchargedIsoPtSumdR03 = 16,
      kneutralIsoPtSumdR03 = 17,
      kphotonPtSumOutsideSignalConedR03 = 18,
      kchargedPionPt = 19,
      kneutralPionPt = 20,
      kbyIsolationMVArun2v1DBdR03oldDMwLTraw = 21,
      kbyIsolationMVArun2v1DBnewDMwLTraw = 22,
      kbyIsolationMVArun2v1DBoldDMwLTraw = 23,
      kbyIsolationMVArun2v1PWnewDMwLTraw = 24,
      kbyLooseIsolationMVArun2v1DBdR03oldDMwLT = 25,
      kbyLooseIsolationMVArun2v1DBnewDMwLT = 26,
      kbyLooseIsolationMVArun2v1DBoldDMwLT = 27,
      kbyLooseIsolationMVArun2v1PWnewDMwLT = 28,
      kbyMediumIsolationMVArun2v1DBdR03oldDMwLT = 29,
      kbyMediumIsolationMVArun2v1DBnewDMwLT = 30,
      kbyMediumIsolationMVArun2v1DBoldDMwLT = 31,
      kbyMediumIsolationMVArun2v1PWnewDMwLT = 32,
      kbyTightIsolationMVArun2v1DBdR03oldDMwLT = 33,
      kbyTightIsolationMVArun2v1DBnewDMwLT = 34,
      kbyTightIsolationMVArun2v1DBoldDMwLT = 35,
      kbyTightIsolationMVArun2v1PWnewDMwLT = 36,
      kbyVLooseIsolationMVArun2v1DBdR03oldDMwLT = 37,
      kbyVLooseIsolationMVArun2v1DBnewDMwLT = 38,
      kbyVLooseIsolationMVArun2v1DBoldDMwLT = 39,
      kbyVLooseIsolationMVArun2v1PWnewDMwLT = 40,
      kbyVTightIsolationMVArun2v1DBdR03oldDMwLT = 41,
      kbyVTightIsolationMVArun2v1DBnewDMwLT = 42,
      kbyVTightIsolationMVArun2v1DBoldDMwLT = 43,
      kbyVTightIsolationMVArun2v1PWnewDMwLT = 44,
      kbyVVTightIsolationMVArun2v1DBdR03oldDMwLT = 45,
      kbyVVTightIsolationMVArun2v1DBnewDMwLT = 46,
      kbyVVTightIsolationMVArun2v1DBoldDMwLT = 47,
      kbyVVTightIsolationMVArun2v1PWnewDMwLT = 48,
      kagainstElectronMVA6raw = 49,
      kagainstElectronMVA6category = 50,
      kagainstElectronVLooseMVA6 = 51,
      kagainstElectronLooseMVA6 = 52,
      kagainstElectronMediumMVA6 = 53,
      kagainstElectronTightMVA6 = 54,
      kagainstElectronVTightMVA6 = 55,
      kagainstMuonLoose3 = 56,
      kagainstMuonTight3 = 57,
      kbyPhotonPtSumOutsideSignalCone = 58,
      kpdgId = 1,
      kcharge = 2,
      kd0 = 3,
      kdz = 4,
      kTauType = 5,
      kdecayMode = 6,
      kEnd
    }; 
    
    
    // vectors of properties defined in Particle.h
    std::vector< floatingnumber >  *pt;
    std::vector< floatingnumber >  *eta;
    std::vector< floatingnumber >  *phi;
    std::vector< floatingnumber >  *m;
    
    // vectors of object specific variables
    std::vector< bool >  *decayModeFindingNewDMs;
    std::vector< bool >  *decayModeFinding;
    std::vector< bool >  *byLooseCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< bool >  *byMediumCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< bool >  *byTightCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< bool >  *byCombinedIsolationDeltaBetaCorrRaw3Hits;
    std::vector< floatingnumber >  *chargedIsoPtSum;
    std::vector< floatingnumber >  *neutralIsoPtSum;
    std::vector< floatingnumber >  *puCorrPtSum;
    std::vector< floatingnumber >  *chargedIsoPtSumdR03;
    std::vector< floatingnumber >  *neutralIsoPtSumdR03;
    std::vector< floatingnumber >  *photonPtSumOutsideSignalConedR03;
    std::vector< floatingnumber >  *chargedPionPt;
    std::vector< floatingnumber >  *neutralPionPt;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBdR03oldDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBnewDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBoldDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1PWnewDMwLTraw;
    std::vector< bool >  *byLooseIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byLooseIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byLooseIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byLooseIsolationMVArun2v1PWnewDMwLT;
    std::vector< bool >  *byMediumIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byMediumIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byMediumIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byMediumIsolationMVArun2v1PWnewDMwLT;
    std::vector< bool >  *byTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< bool >  *byVLooseIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byVLooseIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byVLooseIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byVLooseIsolationMVArun2v1PWnewDMwLT;
    std::vector< bool >  *byVTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byVTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byVTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byVTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< bool >  *byVVTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< bool >  *byVVTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< bool >  *byVVTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< bool >  *byVVTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *againstElectronMVA6raw;
    std::vector< floatingnumber >  *againstElectronMVA6category;
    std::vector< bool >  *againstElectronVLooseMVA6;
    std::vector< bool >  *againstElectronLooseMVA6;
    std::vector< bool >  *againstElectronMediumMVA6;
    std::vector< bool >  *againstElectronTightMVA6;
    std::vector< bool >  *againstElectronVTightMVA6;
    std::vector< bool >  *againstMuonLoose3;
    std::vector< bool >  *againstMuonTight3;
    std::vector< floatingnumber >  *byPhotonPtSumOutsideSignalCone;
    std::vector< int >  *pdgId;
    std::vector< floatingnumber >  *charge;
    std::vector< floatingnumber >  *d0;
    std::vector< floatingnumber >  *dz;
    std::vector< int >  *TauType;
    std::vector< int >  *decayMode;
    
    std::vector<int> m_connectsucceeded;
    
    // save actual detail level and group
    Int_t detailLevel;
    std::string detailGroup;
    
  }; // class TauNtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_TauNtupleObject_H
