
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

// Local include(s):
#include "../include/JetNtupleObject.h"

namespace Ntuple {

  JetNtupleObject::JetNtupleObject( SCycleBaseNTuple* parent )
    : SInputVariables< SCycleBaseNTuple >( parent ) {
      m_connectsucceeded.resize(kEnd);
  }

  void JetNtupleObject::setConnectSucceeded(const unsigned int index, const bool success) {
    if (m_connectsucceeded.size() < index+1)  m_connectsucceeded.resize(index+1);
    m_connectsucceeded.at(index) = success;
  }

  void JetNtupleObject::ConnectVariables( const TString& treeName,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
   
     JetNtupleObject::ConnectVariables( treeName, Ntuple::JetAll, prefix, ntupleType);
                                         
  }                                         

  void JetNtupleObject::ConnectVariables( const TString& treeName,
                                         UInt_t detail_level,
                                         const TString& prefix,
                                         const TString& ntupleType ) throw( SError ) {
                                         
    // get instance of NtupleObjectNames
    NtupleObjectNames m_objectNames(ntupleType);
    

    // particle vector size
    ConnectVariable( treeName, prefix + m_objectNames.getName("N"), N );
    
    // connect variables that are defined in Particle.cxx
    ConnectVariable( treeName, prefix + m_objectNames.getName("e"), e );
    ConnectVariable( treeName, prefix + m_objectNames.getName("pt"), pt );
    ConnectVariable( treeName, prefix + m_objectNames.getName("eta"), eta );
    ConnectVariable( treeName, prefix + m_objectNames.getName("phi"), phi );
    ConnectVariable( treeName, prefix + m_objectNames.getName("m"), m );
        
    

    // connect object specific variables
if(  ((detail_level & Ntuple::JetAnalysis) == Ntuple::JetAnalysis)  ) {
     setConnectSucceeded(3, ConnectVariable( treeName, prefix + m_objectNames.getName("IDLoose"), IDLoose)); 
    setConnectSucceeded(4, ConnectVariable( treeName, prefix + m_objectNames.getName("IDTight"), IDTight)); 
    setConnectSucceeded(5, ConnectVariable( treeName, prefix + m_objectNames.getName("jec"), jec)); 
    setConnectSucceeded(6, ConnectVariable( treeName, prefix + m_objectNames.getName("jecUp"), jecUp)); 
    setConnectSucceeded(7, ConnectVariable( treeName, prefix + m_objectNames.getName("jecDown"), jecDown)); 
    setConnectSucceeded(8, ConnectVariable( treeName, prefix + m_objectNames.getName("muf"), muf)); 
    setConnectSucceeded(9, ConnectVariable( treeName, prefix + m_objectNames.getName("phf"), phf)); 
    setConnectSucceeded(10, ConnectVariable( treeName, prefix + m_objectNames.getName("emf"), emf)); 
    setConnectSucceeded(11, ConnectVariable( treeName, prefix + m_objectNames.getName("nhf"), nhf)); 
    setConnectSucceeded(12, ConnectVariable( treeName, prefix + m_objectNames.getName("chf"), chf)); 
    setConnectSucceeded(13, ConnectVariable( treeName, prefix + m_objectNames.getName("area"), area)); 
    setConnectSucceeded(14, ConnectVariable( treeName, prefix + m_objectNames.getName("cm"), cm)); 
    setConnectSucceeded(15, ConnectVariable( treeName, prefix + m_objectNames.getName("nm"), nm)); 
    setConnectSucceeded(16, ConnectVariable( treeName, prefix + m_objectNames.getName("che"), che)); 
    setConnectSucceeded(17, ConnectVariable( treeName, prefix + m_objectNames.getName("ne"), ne)); 
    setConnectSucceeded(18, ConnectVariable( treeName, prefix + m_objectNames.getName("hf_hf"), hf_hf)); 
    setConnectSucceeded(19, ConnectVariable( treeName, prefix + m_objectNames.getName("hf_emf"), hf_emf)); 
    setConnectSucceeded(20, ConnectVariable( treeName, prefix + m_objectNames.getName("hof"), hof)); 
    setConnectSucceeded(21, ConnectVariable( treeName, prefix + m_objectNames.getName("chm"), chm)); 
    setConnectSucceeded(22, ConnectVariable( treeName, prefix + m_objectNames.getName("neHadMult"), neHadMult)); 
    setConnectSucceeded(23, ConnectVariable( treeName, prefix + m_objectNames.getName("phoMult"), phoMult)); 
    setConnectSucceeded(24, ConnectVariable( treeName, prefix + m_objectNames.getName("nemf"), nemf)); 
    setConnectSucceeded(25, ConnectVariable( treeName, prefix + m_objectNames.getName("cemf"), cemf)); 
} // end of detail level Analysis

if(  ((detail_level & Ntuple::JetBasic) == Ntuple::JetBasic)  ) {
     setConnectSucceeded(1, ConnectVariable( treeName, prefix + m_objectNames.getName("csv"), csv)); 
    setConnectSucceeded(2, ConnectVariable( treeName, prefix + m_objectNames.getName("charge"), charge)); 
} // end of detail level Basic

if(  ((detail_level & Ntuple::JetJER) == Ntuple::JetJER)  ) {
     setConnectSucceeded(56, ConnectVariable( treeName, prefix + m_objectNames.getName("jer_sf"), jer_sf)); 
    setConnectSucceeded(57, ConnectVariable( treeName, prefix + m_objectNames.getName("jer_sf_up"), jer_sf_up)); 
    setConnectSucceeded(58, ConnectVariable( treeName, prefix + m_objectNames.getName("jer_sf_down"), jer_sf_down)); 
    setConnectSucceeded(59, ConnectVariable( treeName, prefix + m_objectNames.getName("jer_sigma_pt"), jer_sigma_pt)); 
} // end of detail level JER

if(  ((detail_level & Ntuple::JetSoftdropSubjets) == Ntuple::JetSoftdropSubjets)  ) {
     setConnectSucceeded(43, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_N"), subjet_softdrop_N)); 
    setConnectSucceeded(44, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_pt"), subjet_softdrop_pt)); 
    setConnectSucceeded(45, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_eta"), subjet_softdrop_eta)); 
    setConnectSucceeded(46, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_phi"), subjet_softdrop_phi)); 
    setConnectSucceeded(47, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_e"), subjet_softdrop_e)); 
    setConnectSucceeded(48, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_m"), subjet_softdrop_m)); 
    setConnectSucceeded(49, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_csv"), subjet_softdrop_csv)); 
    setConnectSucceeded(50, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_charge"), subjet_softdrop_charge)); 
} // end of detail level SoftdropSubjets

if(  ((detail_level & Ntuple::JetSoftdropSubjetsTruth) == Ntuple::JetSoftdropSubjetsTruth)  ) {
     setConnectSucceeded(51, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_partonFlavour"), subjet_softdrop_partonFlavour)); 
    setConnectSucceeded(52, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_hadronFlavour"), subjet_softdrop_hadronFlavour)); 
    setConnectSucceeded(53, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_genParton_pdgID"), subjet_softdrop_genParton_pdgID)); 
    setConnectSucceeded(54, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_nbHadrons"), subjet_softdrop_nbHadrons)); 
    setConnectSucceeded(55, ConnectVariable( treeName, prefix + m_objectNames.getName("subjet_softdrop_ncHadrons"), subjet_softdrop_ncHadrons)); 
} // end of detail level SoftdropSubjetsTruth

if(  ((detail_level & Ntuple::JetSubstructure) == Ntuple::JetSubstructure)  ) {
     setConnectSucceeded(26, ConnectVariable( treeName, prefix + m_objectNames.getName("tau1"), tau1)); 
    setConnectSucceeded(27, ConnectVariable( treeName, prefix + m_objectNames.getName("tau2"), tau2)); 
    setConnectSucceeded(28, ConnectVariable( treeName, prefix + m_objectNames.getName("tau3"), tau3)); 
    setConnectSucceeded(29, ConnectVariable( treeName, prefix + m_objectNames.getName("pruned_mass"), pruned_mass)); 
    setConnectSucceeded(30, ConnectVariable( treeName, prefix + m_objectNames.getName("pruned_massCorr"), pruned_massCorr)); 
    setConnectSucceeded(31, ConnectVariable( treeName, prefix + m_objectNames.getName("softdrop_mass"), softdrop_mass)); 
    setConnectSucceeded(32, ConnectVariable( treeName, prefix + m_objectNames.getName("softdrop_massCorr"), softdrop_massCorr)); 
    setConnectSucceeded(33, ConnectVariable( treeName, prefix + m_objectNames.getName("pruned_jec"), pruned_jec)); 
    setConnectSucceeded(34, ConnectVariable( treeName, prefix + m_objectNames.getName("pruned_jecUp"), pruned_jecUp)); 
    setConnectSucceeded(35, ConnectVariable( treeName, prefix + m_objectNames.getName("pruned_jecDown"), pruned_jecDown)); 
    setConnectSucceeded(36, ConnectVariable( treeName, prefix + m_objectNames.getName("softdrop_jec"), softdrop_jec)); 
    setConnectSucceeded(37, ConnectVariable( treeName, prefix + m_objectNames.getName("Hbbtag"), Hbbtag)); 
} // end of detail level Substructure

if(  ((detail_level & Ntuple::JetTruth) == Ntuple::JetTruth)  ) {
     setConnectSucceeded(38, ConnectVariable( treeName, prefix + m_objectNames.getName("partonFlavour"), partonFlavour)); 
    setConnectSucceeded(39, ConnectVariable( treeName, prefix + m_objectNames.getName("hadronFlavour"), hadronFlavour)); 
    setConnectSucceeded(40, ConnectVariable( treeName, prefix + m_objectNames.getName("genParton_pdgID"), genParton_pdgID)); 
    setConnectSucceeded(41, ConnectVariable( treeName, prefix + m_objectNames.getName("nbHadrons"), nbHadrons)); 
    setConnectSucceeded(42, ConnectVariable( treeName, prefix + m_objectNames.getName("ncHadrons"), ncHadrons)); 
}


        
    // save actual detail_level
    detailLevel = detail_level;

    return;

  }

} // namespace Ntuple
