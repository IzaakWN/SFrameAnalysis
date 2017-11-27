
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

// Local include(s):
#include "../include/GenParticleNtupleObject.h"

namespace Ntuple {
  
  GenParticleNtupleObject::GenParticleNtupleObject( SCycleBaseNTuple* parent ) : SInputVariables< SCycleBaseNTuple >( parent ) {
      m_connectsucceeded.resize(kEnd);
  }
  
  void GenParticleNtupleObject::setConnectSucceeded(const unsigned int index, const bool success) {
    if (m_connectsucceeded.size() < index+1)  m_connectsucceeded.resize(index+1);
    m_connectsucceeded.at(index) = success;
  }
  
  void GenParticleNtupleObject::ConnectVariables( const TString& treeName,
                                           const TString& prefix,
                                           const TString& ntupleType ) throw( SError ) {
     GenParticleNtupleObject::ConnectVariables( treeName, Ntuple::GenParticleAll, prefix, ntupleType);
  }
  
  void GenParticleNtupleObject::ConnectVariables( const TString& treeName,
                                           UInt_t detail_level,
                                           const TString& prefix,
                                           const TString& ntupleType ) throw( SError ) {
    
    // get instance of NtupleObjectNames
    NtupleObjectNames m_objectNames(ntupleType);
    
    
    // particle vector size
    ConnectVariable( treeName, prefix + m_objectNames.getName("N"), N );
    
    // connect variables that are defined in Particle.cxx
    ConnectVariable( treeName, prefix + m_objectNames.getName("pt"), pt );
    ConnectVariable( treeName, prefix + m_objectNames.getName("eta"), eta );
    ConnectVariable( treeName, prefix + m_objectNames.getName("phi"), phi );
    ConnectVariable( treeName, prefix + m_objectNames.getName("m"), m );
    ConnectVariable( treeName, prefix + m_objectNames.getName("e"), e );
    
    
    // connect object specific variables
    
    if(  ((detail_level & Ntuple::GenParticleBasic) == Ntuple::GenParticleBasic)  ) {
      setConnectSucceeded(1, ConnectVariable( treeName, prefix + m_objectNames.getName("pdgId"), pdgId));
      setConnectSucceeded(2, ConnectVariable( treeName, prefix + m_objectNames.getName("status"), status));
      setConnectSucceeded(3, ConnectVariable( treeName, prefix + m_objectNames.getName("mother"), mother));
      setConnectSucceeded(4, ConnectVariable( treeName, prefix + m_objectNames.getName("nMoth"), nMoth));
      setConnectSucceeded(5, ConnectVariable( treeName, prefix + m_objectNames.getName("nDau"), nDau));
      setConnectSucceeded(6, ConnectVariable( treeName, prefix + m_objectNames.getName("dau"), dau));
      setConnectSucceeded(7, ConnectVariable( treeName, prefix + m_objectNames.getName("isPrompt"), isPrompt));
      setConnectSucceeded(8, ConnectVariable( treeName, prefix + m_objectNames.getName("isDirectPromptTauDecayProduct"), isDirectPromptTauDecayProduct));
      setConnectSucceeded(9, ConnectVariable( treeName, prefix + m_objectNames.getName("fromHardProcessFinalState"), fromHardProcessFinalState));
      setConnectSucceeded(10, ConnectVariable( treeName, prefix + m_objectNames.getName("isDirectHardProcessTauDecayProductFinalState"), isDirectHardProcessTauDecayProductFinalState));
    } // end of detail level Basic
    
    if(  ((detail_level & Ntuple::GenParticleTauDecayAnalysis) == Ntuple::GenParticleTauDecayAnalysis)  ) {
      setConnectSucceeded(11, ConnectVariable( treeName, prefix + m_objectNames.getName("tauvispt"), tauvispt));
      setConnectSucceeded(12, ConnectVariable( treeName, prefix + m_objectNames.getName("tauviseta"), tauviseta));
      setConnectSucceeded(13, ConnectVariable( treeName, prefix + m_objectNames.getName("tauvisphi"), tauvisphi));
      setConnectSucceeded(14, ConnectVariable( treeName, prefix + m_objectNames.getName("tauvismass"), tauvismass));
      setConnectSucceeded(15, ConnectVariable( treeName, prefix + m_objectNames.getName("taudecay"), taudecay));
    } // end of detail level TauDecayAnalysis
    
    
    // save actual detail_level
    detailLevel = detail_level;
    
    return;
    
  }

} // namespace Ntuple

