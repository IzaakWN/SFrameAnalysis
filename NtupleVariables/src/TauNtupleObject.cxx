
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

// Local include(s):
#include "../include/TauNtupleObject.h"

namespace Ntuple {
  
  TauNtupleObject::TauNtupleObject( SCycleBaseNTuple* parent ) : SInputVariables< SCycleBaseNTuple >( parent ) {
      m_connectsucceeded.resize(kEnd);
  }
  
  void TauNtupleObject::setConnectSucceeded(const unsigned int index, const bool success) {
    if (m_connectsucceeded.size() < index+1)  m_connectsucceeded.resize(index+1);
    m_connectsucceeded.at(index) = success;
  }
  
  void TauNtupleObject::ConnectVariables( const TString& treeName,
                                           const TString& prefix,
                                           const TString& ntupleType ) throw( SError ) {
     TauNtupleObject::ConnectVariables( treeName, Ntuple::TauAll, prefix, ntupleType);
  }
  
  void TauNtupleObject::ConnectVariables( const TString& treeName,
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
    
    
    // connect object specific variables
    
    if(  ((detail_level & Ntuple::TauAdvancedID) == Ntuple::TauAdvancedID)  ) {
      setConnectSucceeded(7, ConnectVariable( treeName, prefix + m_objectNames.getName("decayModeFindingNewDMs"), decayModeFindingNewDMs));
      setConnectSucceeded(8, ConnectVariable( treeName, prefix + m_objectNames.getName("decayModeFinding"), decayModeFinding));
      setConnectSucceeded(9, ConnectVariable( treeName, prefix + m_objectNames.getName("byLooseCombinedIsolationDeltaBetaCorr3Hits"), byLooseCombinedIsolationDeltaBetaCorr3Hits));
      setConnectSucceeded(10, ConnectVariable( treeName, prefix + m_objectNames.getName("byMediumCombinedIsolationDeltaBetaCorr3Hits"), byMediumCombinedIsolationDeltaBetaCorr3Hits));
      setConnectSucceeded(11, ConnectVariable( treeName, prefix + m_objectNames.getName("byTightCombinedIsolationDeltaBetaCorr3Hits"), byTightCombinedIsolationDeltaBetaCorr3Hits));
      setConnectSucceeded(12, ConnectVariable( treeName, prefix + m_objectNames.getName("byCombinedIsolationDeltaBetaCorrRaw3Hits"), byCombinedIsolationDeltaBetaCorrRaw3Hits));
      setConnectSucceeded(13, ConnectVariable( treeName, prefix + m_objectNames.getName("chargedIsoPtSum"), chargedIsoPtSum));
      setConnectSucceeded(14, ConnectVariable( treeName, prefix + m_objectNames.getName("neutralIsoPtSum"), neutralIsoPtSum));
      setConnectSucceeded(15, ConnectVariable( treeName, prefix + m_objectNames.getName("puCorrPtSum"), puCorrPtSum));
      setConnectSucceeded(16, ConnectVariable( treeName, prefix + m_objectNames.getName("chargedIsoPtSumdR03"), chargedIsoPtSumdR03));
      setConnectSucceeded(17, ConnectVariable( treeName, prefix + m_objectNames.getName("neutralIsoPtSumdR03"), neutralIsoPtSumdR03));
      setConnectSucceeded(18, ConnectVariable( treeName, prefix + m_objectNames.getName("photonPtSumOutsideSignalConedR03"), photonPtSumOutsideSignalConedR03));
      setConnectSucceeded(19, ConnectVariable( treeName, prefix + m_objectNames.getName("chargedPionPt"), chargedPionPt));
      setConnectSucceeded(20, ConnectVariable( treeName, prefix + m_objectNames.getName("neutralPionPt"), neutralPionPt));
      setConnectSucceeded(21, ConnectVariable( treeName, prefix + m_objectNames.getName("byIsolationMVArun2v1DBdR03oldDMwLTraw"), byIsolationMVArun2v1DBdR03oldDMwLTraw));
      setConnectSucceeded(22, ConnectVariable( treeName, prefix + m_objectNames.getName("byIsolationMVArun2v1DBnewDMwLTraw"), byIsolationMVArun2v1DBnewDMwLTraw));
      setConnectSucceeded(23, ConnectVariable( treeName, prefix + m_objectNames.getName("byIsolationMVArun2v1DBoldDMwLTraw"), byIsolationMVArun2v1DBoldDMwLTraw));
      setConnectSucceeded(24, ConnectVariable( treeName, prefix + m_objectNames.getName("byIsolationMVArun2v1PWnewDMwLTraw"), byIsolationMVArun2v1PWnewDMwLTraw));
      setConnectSucceeded(25, ConnectVariable( treeName, prefix + m_objectNames.getName("byLooseIsolationMVArun2v1DBdR03oldDMwLT"), byLooseIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(26, ConnectVariable( treeName, prefix + m_objectNames.getName("byLooseIsolationMVArun2v1DBnewDMwLT"), byLooseIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(27, ConnectVariable( treeName, prefix + m_objectNames.getName("byLooseIsolationMVArun2v1DBoldDMwLT"), byLooseIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(28, ConnectVariable( treeName, prefix + m_objectNames.getName("byLooseIsolationMVArun2v1PWnewDMwLT"), byLooseIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(29, ConnectVariable( treeName, prefix + m_objectNames.getName("byMediumIsolationMVArun2v1DBdR03oldDMwLT"), byMediumIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(30, ConnectVariable( treeName, prefix + m_objectNames.getName("byMediumIsolationMVArun2v1DBnewDMwLT"), byMediumIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(31, ConnectVariable( treeName, prefix + m_objectNames.getName("byMediumIsolationMVArun2v1DBoldDMwLT"), byMediumIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(32, ConnectVariable( treeName, prefix + m_objectNames.getName("byMediumIsolationMVArun2v1PWnewDMwLT"), byMediumIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(33, ConnectVariable( treeName, prefix + m_objectNames.getName("byTightIsolationMVArun2v1DBdR03oldDMwLT"), byTightIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(34, ConnectVariable( treeName, prefix + m_objectNames.getName("byTightIsolationMVArun2v1DBnewDMwLT"), byTightIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(35, ConnectVariable( treeName, prefix + m_objectNames.getName("byTightIsolationMVArun2v1DBoldDMwLT"), byTightIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(36, ConnectVariable( treeName, prefix + m_objectNames.getName("byTightIsolationMVArun2v1PWnewDMwLT"), byTightIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(37, ConnectVariable( treeName, prefix + m_objectNames.getName("byVLooseIsolationMVArun2v1DBdR03oldDMwLT"), byVLooseIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(38, ConnectVariable( treeName, prefix + m_objectNames.getName("byVLooseIsolationMVArun2v1DBnewDMwLT"), byVLooseIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(39, ConnectVariable( treeName, prefix + m_objectNames.getName("byVLooseIsolationMVArun2v1DBoldDMwLT"), byVLooseIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(40, ConnectVariable( treeName, prefix + m_objectNames.getName("byVLooseIsolationMVArun2v1PWnewDMwLT"), byVLooseIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(41, ConnectVariable( treeName, prefix + m_objectNames.getName("byVTightIsolationMVArun2v1DBdR03oldDMwLT"), byVTightIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(42, ConnectVariable( treeName, prefix + m_objectNames.getName("byVTightIsolationMVArun2v1DBnewDMwLT"), byVTightIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(43, ConnectVariable( treeName, prefix + m_objectNames.getName("byVTightIsolationMVArun2v1DBoldDMwLT"), byVTightIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(44, ConnectVariable( treeName, prefix + m_objectNames.getName("byVTightIsolationMVArun2v1PWnewDMwLT"), byVTightIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(45, ConnectVariable( treeName, prefix + m_objectNames.getName("byVVTightIsolationMVArun2v1DBdR03oldDMwLT"), byVVTightIsolationMVArun2v1DBdR03oldDMwLT));
      setConnectSucceeded(46, ConnectVariable( treeName, prefix + m_objectNames.getName("byVVTightIsolationMVArun2v1DBnewDMwLT"), byVVTightIsolationMVArun2v1DBnewDMwLT));
      setConnectSucceeded(47, ConnectVariable( treeName, prefix + m_objectNames.getName("byVVTightIsolationMVArun2v1DBoldDMwLT"), byVVTightIsolationMVArun2v1DBoldDMwLT));
      setConnectSucceeded(48, ConnectVariable( treeName, prefix + m_objectNames.getName("byVVTightIsolationMVArun2v1PWnewDMwLT"), byVVTightIsolationMVArun2v1PWnewDMwLT));
      setConnectSucceeded(49, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronMVA6raw"), againstElectronMVA6raw));
      setConnectSucceeded(50, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronMVA6category"), againstElectronMVA6category));
      setConnectSucceeded(51, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronVLooseMVA6"), againstElectronVLooseMVA6));
      setConnectSucceeded(52, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronLooseMVA6"), againstElectronLooseMVA6));
      setConnectSucceeded(53, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronMediumMVA6"), againstElectronMediumMVA6));
      setConnectSucceeded(54, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronTightMVA6"), againstElectronTightMVA6));
      setConnectSucceeded(55, ConnectVariable( treeName, prefix + m_objectNames.getName("againstElectronVTightMVA6"), againstElectronVTightMVA6));
      setConnectSucceeded(56, ConnectVariable( treeName, prefix + m_objectNames.getName("againstMuonLoose3"), againstMuonLoose3));
      setConnectSucceeded(57, ConnectVariable( treeName, prefix + m_objectNames.getName("againstMuonTight3"), againstMuonTight3));
      setConnectSucceeded(58, ConnectVariable( treeName, prefix + m_objectNames.getName("byPhotonPtSumOutsideSignalCone"), byPhotonPtSumOutsideSignalCone));
    } // end of detail level AdvancedID
    
    if(  ((detail_level & Ntuple::TauBasic) == Ntuple::TauBasic)  ) {
      setConnectSucceeded(1, ConnectVariable( treeName, prefix + m_objectNames.getName("pdgId"), pdgId));
      setConnectSucceeded(2, ConnectVariable( treeName, prefix + m_objectNames.getName("charge"), charge));
      setConnectSucceeded(3, ConnectVariable( treeName, prefix + m_objectNames.getName("d0"), d0));
      setConnectSucceeded(4, ConnectVariable( treeName, prefix + m_objectNames.getName("dz"), dz));
    } // end of detail level Basic
    
    if(  ((detail_level & Ntuple::TauID) == Ntuple::TauID)  ) {
      setConnectSucceeded(5, ConnectVariable( treeName, prefix + m_objectNames.getName("TauType"), TauType));
      setConnectSucceeded(6, ConnectVariable( treeName, prefix + m_objectNames.getName("decayMode"), decayMode));
    } // end of detail level ID
    
    
    // save actual detail_level
    detailLevel = detail_level;
    
    return;
    
  }

} // namespace Ntuple
