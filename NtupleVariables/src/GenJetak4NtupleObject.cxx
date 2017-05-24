
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

// Local include(s):
#include "../include/GenJetak4NtupleObject.h"

namespace Ntuple {

  GenJetak4NtupleObject::GenJetak4NtupleObject( SCycleBaseNTuple* parent )
    : SInputVariables< SCycleBaseNTuple >( parent ) {
      m_connectsucceeded.resize(kEnd);
  }

  void GenJetak4NtupleObject::setConnectSucceeded(const unsigned int index, const bool success) {
    if (m_connectsucceeded.size() < index+1)  m_connectsucceeded.resize(index+1);
    m_connectsucceeded.at(index) = success;
  }

  void GenJetak4NtupleObject::ConnectVariables( const TString& treeName,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
   
     GenJetak4NtupleObject::ConnectVariables( treeName, Ntuple::GenJetak4All, prefix, ntupleType);
                                         
  }                                         

  void GenJetak4NtupleObject::ConnectVariables( const TString& treeName,
                                         UInt_t detail_level,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
                                         
    // get instance of NtupleObjectNames
    NtupleObjectNames m_objectNames(ntupleType);
    
    
    // connect variables that are defined in Particle.cxx
        
    

    // connect object specific variables
if(  ((detail_level & Ntuple::GenJetak4Truth) == Ntuple::GenJetak4Truth)  ) {
     setConnectSucceeded(1, ConnectVariable( treeName, prefix + m_objectNames.getName("genJetAK4_pt"), genJetAK4_pt)); 
    setConnectSucceeded(2, ConnectVariable( treeName, prefix + m_objectNames.getName("genJetAK4_phi"), genJetAK4_phi)); 
    setConnectSucceeded(3, ConnectVariable( treeName, prefix + m_objectNames.getName("genJetAK4_eta"), genJetAK4_eta)); 
    setConnectSucceeded(4, ConnectVariable( treeName, prefix + m_objectNames.getName("genJetAK4_e"), genJetAK4_e)); 
}


        
    // save actual detail_level
    detailLevel = detail_level;

    return;

  }

} // namespace Ntuple
