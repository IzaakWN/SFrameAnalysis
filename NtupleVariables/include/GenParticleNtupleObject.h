// Dear emacs, this is -*- c++ -*-
// $Id: GenParticleNtupleObject.h 37457 2010-07-05 12:04:33Z mann $

// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 


#ifndef SFRAME_NtupleVARIABLES_GenParticleNtupleObject_H
#define SFRAME_NtupleVARIABLES_GenParticleNtupleObject_H

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
   *  @short Class that can read the variables produced by GenParticleNtupleObject
   *
   *         This class can be used to read the offline muon information from
   *         an ntuple produced by the SingleTopDPDMaker code.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
   *
   */
  
  enum GenParticleDetails {
    GenParticleTauDecayAnalysis = 1,
    GenParticleBasic = 2,
    GenParticleAll = 3,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class GenParticleNtupleObject : public SInputVariables< SCycleBaseNTuple > {
    
    public:
    
    // constructor specifying the parent of the object
    GenParticleNtupleObject( SCycleBaseNTuple* parent );
    
    // remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  
    
    // connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "GenParticle_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "GenParticle_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    int getDetailLevel() const { return detailLevel; }
    
    // particle vector size
    Int_t N;
    
    enum ConnectionIndex { 
      kpdgId = 1,
      kstatus = 2,
      kmother = 3,
      knMoth = 4,
      knDau = 5,
      kdau = 6,
      kisPrompt = 7,
      kisDirectPromptTauDecayProduct = 8,
      kfromHardProcessFinalState = 9,
      kisDirectHardProcessTauDecayProductFinalState = 10,
      ktauvispt = 11,
      ktauviseta = 12,
      ktauvisphi = 13,
      ktauvismass = 14,
      ktaudecay = 15,
      kEnd
    }; 
    
    
    // vectors of properties defined in Particle.h
    std::vector< floatingnumber >  *pt;
    std::vector< floatingnumber >  *eta;
    std::vector< floatingnumber >  *phi;
    std::vector< floatingnumber >  *m;
    
    // vectors of object specific variables
    std::vector< int >  *pdgId;
    std::vector< int >  *status;
    std::vector< std::vector<int> >  *mother;
    std::vector< int >  *nMoth;
    std::vector< int >  *nDau;
    std::vector< std::vector<int> >  *dau;
    std::vector< int >  *isPrompt;
    std::vector< int >  *isDirectPromptTauDecayProduct;
    std::vector< int >  *fromHardProcessFinalState;
    std::vector< int >  *isDirectHardProcessTauDecayProductFinalState;
    std::vector< floatingnumber >  *tauvispt;
    std::vector< floatingnumber >  *tauviseta;
    std::vector< floatingnumber >  *tauvisphi;
    std::vector< floatingnumber >  *tauvismass;
    std::vector< int >  *taudecay;
    
    std::vector<int> m_connectsucceeded;
    
    // save actual detail level and group
    Int_t detailLevel;
    std::string detailGroup;
    
  }; // class GenParticleNtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_GenParticleNtupleObject_H
