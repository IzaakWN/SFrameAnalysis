// Dear emacs, this is -*- c++ -*-
// $Id: GenJetak4NtupleObject.h 37457 2010-07-05 12:04:33Z mann $

// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 


#ifndef SFRAME_NtupleVARIABLES_GenJetak4NtupleObject_H
#define SFRAME_NtupleVARIABLES_GenJetak4NtupleObject_H

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
   *  @short Class that can read the variables produced by GenJetak4NtupleObject
   *
   *         This class can be used to read the offline muon information from
   *         an ntuple produced by the SingleTopDPDMaker code.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
   *
   */
  
  enum GenJetak4Details {
    GenJetak4Truth = 1,
    GenJetak4All = 1,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class GenJetak4NtupleObject : public SInputVariables< SCycleBaseNTuple > {
    
    public:
    
    // constructor specifying the parent of the object
    GenJetak4NtupleObject( SCycleBaseNTuple* parent );
    
    // remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  
    
    // connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "GenJetak4_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "GenJetak4_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    int getDetailLevel() const { return detailLevel; }
    enum ConnectionIndex { 
      kgenJetAK4_pt = 1,
      kgenJetAK4_phi = 2,
      kgenJetAK4_eta = 3,
      kgenJetAK4_e = 4,
      kEnd
    }; 
    
    
    // vectors of properties defined in Particle.h 
    // vectors of object specific variables
    std::vector< float >  *genJetAK4_pt;
    std::vector< float >  *genJetAK4_phi;
    std::vector< float >  *genJetAK4_eta;
    std::vector< float >  *genJetAK4_e;
    
    std::vector<int> m_connectsucceeded;
    
    // save actual detail level and group
    Int_t detailLevel;
    std::string detailGroup;
    
  }; // class GenJetak4NtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_GenJetak4NtupleObject_H
