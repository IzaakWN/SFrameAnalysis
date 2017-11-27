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
  
  /*
   *  @short Class that can read the variables produced by TauNtupleObject
   *
   *         This class can be used to read the offline muon information from
   *         an ntuple produced by the SingleTopDPDMaker code.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
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
      kfootprintCorrectiondR03 = 17,
      kneutralIsoPtSumdR03 = 18,
      kneutralIsoPtSumWeight = 19,
      kneutralIsoPtSumWeightdR03 = 20,
      kphotonPtSumOutsideSignalConedR03 = 21,
      kchargedPionPt = 22,
      kneutralPionPt = 23,
      kbyIsolationMVArun2v1DBdR03oldDMwLTraw = 24,
      kbyIsolationMVArun2v1DBnewDMwLTraw = 25,
      kbyIsolationMVArun2v1DBoldDMwLTraw = 26,
      kbyIsolationMVArun2v1PWdR03oldDMwLTraw = 27,
      kbyIsolationMVArun2v1PWnewDMwLTraw = 28,
      kbyIsolationMVArun2v1PWoldDMwLTraw = 29,
      kbyLooseIsolationMVArun2v1DBdR03oldDMwLT = 30,
      kbyLooseIsolationMVArun2v1DBnewDMwLT = 31,
      kbyLooseIsolationMVArun2v1DBoldDMwLT = 32,
      kbyLooseIsolationMVArun2v1PWdR03oldDMwLT = 33,
      kbyLooseIsolationMVArun2v1PWnewDMwLT = 34,
      kbyLooseIsolationMVArun2v1PWoldDMwLT = 35,
      kbyMediumIsolationMVArun2v1DBdR03oldDMwLT = 36,
      kbyMediumIsolationMVArun2v1DBnewDMwLT = 37,
      kbyMediumIsolationMVArun2v1DBoldDMwLT = 38,
      kbyMediumIsolationMVArun2v1PWdR03oldDMwLT = 39,
      kbyMediumIsolationMVArun2v1PWnewDMwLT = 40,
      kbyMediumIsolationMVArun2v1PWoldDMwLT = 41,
      kbyTightIsolationMVArun2v1DBdR03oldDMwLT = 42,
      kbyTightIsolationMVArun2v1DBnewDMwLT = 43,
      kbyTightIsolationMVArun2v1DBoldDMwLT = 44,
      kbyTightIsolationMVArun2v1PWdR03oldDMwLT = 45,
      kbyTightIsolationMVArun2v1PWnewDMwLT = 46,
      kbyTightIsolationMVArun2v1PWoldDMwLT = 47,
      kbyVLooseIsolationMVArun2v1DBdR03oldDMwLT = 48,
      kbyVLooseIsolationMVArun2v1DBnewDMwLT = 49,
      kbyVLooseIsolationMVArun2v1DBoldDMwLT = 50,
      kbyVLooseIsolationMVArun2v1PWdR03oldDMwLT = 51,
      kbyVLooseIsolationMVArun2v1PWnewDMwLT = 52,
      kbyVLooseIsolationMVArun2v1PWoldDMwLT = 53,
      kbyVTightIsolationMVArun2v1DBdR03oldDMwLT = 54,
      kbyVTightIsolationMVArun2v1DBnewDMwLT = 55,
      kbyVTightIsolationMVArun2v1DBoldDMwLT = 56,
      kbyVTightIsolationMVArun2v1PWdR03oldDMwLT = 57,
      kbyVTightIsolationMVArun2v1PWnewDMwLT = 58,
      kbyVTightIsolationMVArun2v1PWoldDMwLT = 59,
      kbyVVTightIsolationMVArun2v1DBdR03oldDMwLT = 60,
      kbyVVTightIsolationMVArun2v1DBnewDMwLT = 61,
      kbyVVTightIsolationMVArun2v1DBoldDMwLT = 62,
      kbyVVTightIsolationMVArun2v1PWdR03oldDMwLT = 63,
      kbyVVTightIsolationMVArun2v1PWnewDMwLT = 64,
      kbyVVTightIsolationMVArun2v1PWoldDMwLT = 65,
      kagainstElectronMVA6raw = 66,
      kagainstElectronMVA6category = 67,
      kagainstElectronVLooseMVA6 = 68,
      kagainstElectronLooseMVA6 = 69,
      kagainstElectronMediumMVA6 = 70,
      kagainstElectronTightMVA6 = 71,
      kagainstElectronVTightMVA6 = 72,
      kagainstMuonLoose3 = 73,
      kagainstMuonTight3 = 74,
      kbyPhotonPtSumOutsideSignalCone = 75,
      kfootprintCorrection = 76,
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
    std::vector< floatingnumber >  *e;
     
    // vectors of object specific variables
    std::vector< floatingnumber >  *decayModeFindingNewDMs;
    std::vector< floatingnumber >  *decayModeFinding;
    std::vector< floatingnumber >  *byLooseCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< floatingnumber >  *byMediumCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< floatingnumber >  *byTightCombinedIsolationDeltaBetaCorr3Hits;
    std::vector< floatingnumber >  *byCombinedIsolationDeltaBetaCorrRaw3Hits;
    std::vector< floatingnumber >  *chargedIsoPtSum;
    std::vector< floatingnumber >  *neutralIsoPtSum;
    std::vector< floatingnumber >  *puCorrPtSum;
    std::vector< floatingnumber >  *chargedIsoPtSumdR03;
    std::vector< floatingnumber >  *footprintCorrectiondR03;
    std::vector< floatingnumber >  *neutralIsoPtSumdR03;
    std::vector< floatingnumber >  *neutralIsoPtSumWeight;
    std::vector< floatingnumber >  *neutralIsoPtSumWeightdR03;
    std::vector< floatingnumber >  *photonPtSumOutsideSignalConedR03;
    std::vector< floatingnumber >  *chargedPionPt;
    std::vector< floatingnumber >  *neutralPionPt;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBdR03oldDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBnewDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1DBoldDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1PWdR03oldDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1PWnewDMwLTraw;
    std::vector< floatingnumber >  *byIsolationMVArun2v1PWoldDMwLTraw;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byLooseIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byMediumIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byTightIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byVLooseIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byVTightIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1DBdR03oldDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1DBnewDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1DBoldDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1PWdR03oldDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1PWnewDMwLT;
    std::vector< floatingnumber >  *byVVTightIsolationMVArun2v1PWoldDMwLT;
    std::vector< floatingnumber >  *againstElectronMVA6raw;
    std::vector< floatingnumber >  *againstElectronMVA6category;
    std::vector< floatingnumber >  *againstElectronVLooseMVA6;
    std::vector< floatingnumber >  *againstElectronLooseMVA6;
    std::vector< floatingnumber >  *againstElectronMediumMVA6;
    std::vector< floatingnumber >  *againstElectronTightMVA6;
    std::vector< floatingnumber >  *againstElectronVTightMVA6;
    std::vector< floatingnumber >  *againstMuonLoose3;
    std::vector< floatingnumber >  *againstMuonTight3;
    std::vector< floatingnumber >  *byPhotonPtSumOutsideSignalCone;
    std::vector< floatingnumber >  *footprintCorrection;
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
