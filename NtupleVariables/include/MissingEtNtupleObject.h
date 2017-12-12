// Dear emacs, this is -*- c++ -*-
// $Id: MissingEtNtupleObject.h 37457 2010-07-05 12:04:33Z mann $

// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 


#ifndef SFRAME_NtupleVARIABLES_MissingEtNtupleObject_H
#define SFRAME_NtupleVARIABLES_MissingEtNtupleObject_H

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
   *  @short Class that can read the variables produced by MissingEtNtupleObject
   *
   *        This class can be used to read the offline muon information from
   *        an ntuple produced by the SingleTopDPDMaker code.
   *
   *  @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
   *
   */
  
  enum MissingEtDetails {
    MissingEtCovAnalysis = 1,
    MissingEtBasic = 2,
    MissingEtAnalysis = 4,
    MissingEtAnalysisSyst = 8,
    MissingEtAll = 15,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class MissingEtNtupleObject : public SInputVariables< SCycleBaseNTuple > {
    
    public:
    
    // constructor specifying the parent of the object
    MissingEtNtupleObject( SCycleBaseNTuple* parent );
    
    // remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  
    
    // connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "MissingEt_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "MissingEt_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    int getDetailLevel() const { return detailLevel; }
    enum ConnectionIndex { 
      ksumEt = 3,
      kcorrPx = 4,
      kcorrPy = 5,
      ksignificance = 6,
      kJetEnUp = 10,
      kJetEnDown = 11,
      kJetResUp = 12,
      kJetResDown = 13,
      kUnclusteredEnUp = 14,
      kUnclusteredEnDown = 15,
      ket = 1,
      kphi = 2,
      kcov00 = 7,
      kcov10 = 8,
      kcov11 = 9,
      kEnd
    }; 
    
    
    // vectors of properties defined in Particle.h
    // vectors of object specific variables
    std::vector< floatingnumber >  *sumEt;
    std::vector< floatingnumber >  *corrPx;
    std::vector< floatingnumber >  *corrPy;
    std::vector< floatingnumber >  *significance;
    std::vector< floatingnumber >  *JetEnUp;
    std::vector< floatingnumber >  *JetEnDown;
    std::vector< floatingnumber >  *JetResUp;
    std::vector< floatingnumber >  *JetResDown;
    std::vector< floatingnumber >  *UnclusteredEnUp;
    std::vector< floatingnumber >  *UnclusteredEnDown;
    std::vector< floatingnumber >  *et;
    std::vector< floatingnumber >  *phi;
    std::vector< floatingnumber >  *cov00;
    std::vector< floatingnumber >  *cov10;
    std::vector< floatingnumber >  *cov11;
    
    std::vector<int> m_connectsucceeded;
    
    // save actual detail level and group
    Int_t detailLevel;
    std::string detailGroup;
    
  }; // class MissingEtNtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_MissingEtNtupleObject_H
