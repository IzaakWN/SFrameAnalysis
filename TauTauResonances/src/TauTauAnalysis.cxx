// $Id: CycleCreators.py 344 2012-12-13 13:10:53Z krasznaa $

// Local include(s):
#include "../include/TauTauAnalysis.h"
// External include(s):
#include "../GoodRunsLists/include/TGoodRunsListReader.h"

#include <TMath.h>
#include "TRandom3.h"

ClassImp( TauTauAnalysis );





TauTauAnalysis::TauTauAnalysis() : SCycleBase()
   , m_jetAK4( this )
   , m_eventInfo( this )
   , m_electron( this )
   , m_muon( this )
   , m_tau( this )
   , m_missingEt( this )
   , m_puppimissingEt( this )
   //, m_mvamissingEt( this )
   , m_genParticle( this )
   , m_PileupReweightingTool( this )
   , m_BTaggingScaleTool( this )
   , m_ScaleFactorTool( this )
   , m_RecoilCorrector( this )
   , m_SVFitTool( this )
{

  m_logger << INFO << "Hello!" << SLogger::endmsg;
  SetLogName( GetName() );
  
  // read configuration details from XML file
  DeclareProperty("RecoTreeName", m_recoTreeName = "physics" );

  // channels
  channels_.push_back("mutau");
  channels_.push_back("eletau");
  
  for(unsigned int ch=0;ch< channels_.size();ch++){
    m_outputTreeName_ch_.push_back("");
  }
  
  DeclareProperty( "OutputTreeName_mutau" , m_outputTreeName_ch_[0]);
  DeclareProperty( "OutputTreeName_eletau", m_outputTreeName_ch_[1]);

  DeclareProperty( "JetAK4Name",            m_jetAK4Name            = "jetAK4" );
  DeclareProperty( "ElectronName",          m_electronName          = "el" );
  DeclareProperty( "MuonName",              m_muonName              = "mu" );
  DeclareProperty( "TauName",               m_tauName               = "tau" );
  DeclareProperty( "MissingEtName",         m_missingEtName         = "MET" );
  DeclareProperty( "GenParticleName",       m_genParticleName       = "genParticle" );
  
  DeclareProperty( "IsData",                m_isData                = false );
  DeclareProperty( "doSVFit",               m_doSVFit               = false );
  DeclareProperty( "IsSignal",              m_isSignal              = false );
  DeclareProperty( "doRecoilCorr",          m_doRecoilCorr          = false );
  DeclareProperty( "doZpt",                 m_doZpt                 = false );
  DeclareProperty( "doTTpt",                m_doTTpt                = false );
  DeclareProperty( "doTES",                 m_doTES                 = false );
  DeclareProperty( "TESshift",              m_TESshift              = 0.0 );
  DeclareProperty( "doEES",                 m_doEES                 = false );
  DeclareProperty( "EESshift",              m_EESshift              = 0.0 );
  DeclareProperty( "EESshiftEndCap",        m_EESshiftEndCap        = m_EESshift*2.5 );
  DeclareProperty( "doLTF",                 m_doLTF                 = false );
  DeclareProperty( "LTFshift",              m_LTFshift              = 0.0 );

  // for SUSY https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016
  // for comparison https://twiki.cern.ch/twiki/bin/viewauth/CMS/MSSMAHTauTauSummer2016#Baseline
  // for us https://twiki.cern.ch/twiki/bin/view/CMS/SMTauTau2016#Baseline_sync_selection
  DeclareProperty( "AK4JetPtCut",           m_AK4jetPtCut           = 20.   );
  DeclareProperty( "AK4JetEtaCut",          m_AK4jetEtaCut          = 4.7   );
  DeclareProperty( "CSVWorkingPoint",       m_CSVWorkingPoint       = 0.8   ); // 0.8 is Medium

  DeclareProperty( "ElectronPtCut",         m_electronPtCut         = 26.   );
  DeclareProperty( "ElectronEtaCut",        m_electronEtaCut        = 2.1   );
  DeclareProperty( "ElectronD0Cut",         m_electronD0Cut         = 0.045 );
  DeclareProperty( "ElectronDzCut",         m_electronDzCut         = 0.2   );
  DeclareProperty( "ElectronIsoCut",        m_electronIsoCut        = 0.1   );
  
  DeclareProperty( "MuonPtCut",             m_muonPtCut             = 23.   ); // 23
  DeclareProperty( "MuonEtaCut",            m_muonEtaCut            = 2.4   ); // 2.4; 2.1
  DeclareProperty( "MuonD0Cut",             m_muonD0Cut             = 0.045 );
  DeclareProperty( "MuonDzCut",             m_muonDzCut             = 0.2   );
  DeclareProperty( "MuonIsoCut",            m_muonIsoCut            = 0.15  );

  DeclareProperty( "TauPtCut",              m_tauPtCut              = 20.  ); // 20; 30
  DeclareProperty( "TauEtaCut",             m_tauEtaCut             = 2.3  );
  DeclareProperty( "TauDzCut",              m_tauDzCut              = 0.2  );

  // ICHEP: https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2689.html
//   DeclareProperty( "JSONName",             m_jsonName              = std::string (std::getenv("SFRAME_DIR")) + "/../GoodRunsLists/JSON/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt" );
  DeclareProperty( "JSONName",              m_jsonName              = std::string (std::getenv("SFRAME_DIR")) + "/../GoodRunsLists/JSON/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_ICHEP.txt" );
  
}





TauTauAnalysis::~TauTauAnalysis() {
  
  m_logger << INFO << "Tschoe!" << SLogger::endmsg;
  
}





void TauTauAnalysis::BeginCycle() throw( SError ) {
  
  m_logger << INFO << "BeginCycle ... " << SLogger::endmsg;
  
  mu_tau    = 0;
  ele_tau   = 0;

  // Load GRL:
  if (m_isData) {
    m_logger << INFO << "Loading GoodRunsList from file: " << m_jsonName << SLogger::endmsg;
    Root::TGoodRunsListReader reader( TString( m_jsonName.c_str() ) );
    if( ! reader.Interpret() ) {
      m_logger << FATAL << "Couldn't read in the GRL!" << SLogger::endmsg;
      throw SError( ( "Couldn't read in file: " + m_jsonName ).c_str(), SError::SkipCycle );
    }
    m_grl = reader.GetMergedGoodRunsList();
    m_grl.Summary();
    m_grl.SetName( "MyGoodRunsList" );
    
    AddConfigObject( &m_grl );
  }
  
  m_triggerNames_mutau.clear();
  m_triggerNames_eletau.clear();
  
  
  // TRIGGERS
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016
  // https://hypernews.cern.ch/HyperNews/CMS/get/AUX/2017/02/10/17:01:24-67933-2016triggerGrandTable.pdf
  // https://indico.cern.ch/event/598433/#day-2017-02-15
  
  // muon triggers
  m_triggerNames_mutau.push_back("HLT_IsoMu22_v");          // not pre-scaled  run < 276864
  m_triggerNames_mutau.push_back("HLT_IsoTkMu22_v");        // not pre-scaled  run < 276864
  // m_triggerNames_mutau.push_back("HLT_IsoMu20_v");          // not pre-scaled  run > 274889
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu20_v");        // not pre-scaled  run > 274889
  // m_triggerNames_mutau.push_back("HLT_IsoMu24_v");          // not pre-scaled  entire run
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu24_v");        // not pre-scaled  entire run
  // m_triggerNames_mutau.push_back("HLT_IsoMu18_v");
  // m_triggerNames_mutau.push_back("HLT_IsoMu22_v3");
  // m_triggerNames_mutau.push_back("HLT_IsoMu22_eta2p1_v2");
  // m_triggerNames_mutau.push_back("HLT_IsoMu27_v4");
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu18_v3");
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu22_eta2p1_v2");
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu22_v3");
  // m_triggerNames_mutau.push_back("HLT_IsoTkMu27_v4");
  // m_triggerNames_mutau.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_SingleL1_v5");  // pre-scaled
  // m_triggerNames_mutau.push_back("HLT_IsoMu17_eta2p1_LooseIsoPFTau20_v5");           // pre-scaled
  // m_triggerNames_mutau.push_back("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v2");  // not pre-scaled  entire run
  // m_triggerNames_mutau.push_back("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_v2");           // not pre-scaled  entire run
  // m_triggerNames_mutau.push_back("HLT_IsoMu21_eta2p1_LooseIsoPFTau20_SingleL1_v2");  // not pre-scaled  entire run
  
  
  // electron triggers
  m_triggerNames_eletau.push_back("HLT_Ele25_eta2p1_WPTight_Gsf_v");                    // not pre-scaled  entire run
  // m_triggerNames_eletau.push_back("HLT_Ele23_WPLoose_Gsf_v4");
  // m_triggerNames_eletau.push_back("HLT_Ele24_eta2p1_WPLoose_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele25_WPTight_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele25_eta2p1_WPLoose_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele25_eta2p1_WPTight_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele27_WPLoose_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele27_WPTight_Gsf_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele27_eta2p1_WPLoose_Gsf_v3");
  // m_triggerNames_eletau.push_back("HLT_Ele27_eta2p1_WPTight_Gsf_v3");
  // m_triggerNames_eletau.push_back("HLT_Ele32_eta2p1_WPTight_Gsf_v3");
  // m_triggerNames_eletau.push_back("HLT_Ele22_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v3");
  // m_triggerNames_eletau.push_back("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2");  // pre-scaled            run < 276215
  // m_triggerNames_eletau.push_back("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v2");           // pre-scaled  276215 <= run < 278270
  // m_triggerNames_eletau.push_back("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v");            // pre-scaled            run > 278270
  // m_triggerNames_eletau.push_back("HLT_Ele27_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2");
  // m_triggerNames_eletau.push_back("HLT_Ele32_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v2");
  
  
  return;

}





struct ltau_pair
{
  Int_t ilepton;
  Float_t lep_iso;
  Float_t lep_pt;
  Int_t itau;
  Float_t tau_iso;
  Float_t tau_pt;
  Float_t dR;

  //overload comparators
  bool operator<(const ltau_pair& another) const {
//     if (dR > 0.3 && another.dR > 0.3 && dR != another.dR)
//       return dR < another.dR;           // take pair with lowest dR, if dR > 0.3
    if (lep_iso != another.lep_iso)
      return lep_iso < another.lep_iso; // take pair with best (lowest) leption iso
    if (lep_pt != another.lep_pt)
      return lep_pt > another.lep_pt;   // take pair with highest lepton pt
    if (tau_iso != another.tau_iso)
      return tau_iso > another.tau_iso; // take pair with best (highest) tau iso
    if (tau_pt != another.tau_pt)
      return tau_pt > another.tau_pt;   // take pair with highest tau pt
    return ilepton < another.ilepton;
  }

};





void TauTauAnalysis::EndCycle() throw( SError ) {
   std::cout << "events in mu_tau " <<mu_tau <<std::endl;
   std::cout << "events in ele_tau " <<ele_tau <<std::endl;
   return;
}





void TauTauAnalysis::BeginInputData( const SInputData& id ) throw( SError ) {
  std::cout << "BeginInputData" << std::endl;

  m_logger << INFO << "RecoTreeName:        " <<            m_recoTreeName << SLogger::endmsg;
  m_logger << INFO << "JetAK4Name:          " <<            m_jetAK4Name << SLogger::endmsg;
  m_logger << INFO << "ElectronName:        " <<            m_electronName << SLogger::endmsg;
  m_logger << INFO << "MuonName:            " <<            m_muonName << SLogger::endmsg;
  m_logger << INFO << "TauName:             " <<            m_tauName << SLogger::endmsg;
  m_logger << INFO << "GenParticleName:     " <<            m_genParticleName << SLogger::endmsg;
  
  m_logger << INFO << "IsData:              " <<            (m_isData ?     "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "IsSignal:            " <<            (m_isSignal ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doSVFit:             " <<            (m_doSVFit ?    "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doRecoilCorr:        " <<            (m_doRecoilCorr ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doZpt:               " <<            (m_doZpt ?      "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTTpt:              " <<            (m_doTTpt ?     "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTES:               " <<            (m_doTES ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "TESshift:            " <<            m_TESshift << SLogger::endmsg;
  m_logger << INFO << "doEES:               " <<            (m_doEES ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "EESshift:            " <<            m_EESshift << SLogger::endmsg;
  m_logger << INFO << "EESshiftEndCap:      " <<            m_EESshiftEndCap << SLogger::endmsg;
  m_logger << INFO << "doLTF:               " <<            (m_doTES ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "LTFshift:            " <<            m_TESshift << SLogger::endmsg;

  m_logger << INFO << "ElectronPtCut:       " <<            m_electronPtCut << SLogger::endmsg;
  m_logger << INFO << "ElectronEtaCut:      " <<            m_electronEtaCut << SLogger::endmsg;
  m_logger << INFO << "ElectronD0Cut:       " <<            m_electronD0Cut << SLogger::endmsg;
  m_logger << INFO << "ElectronDzCut:       " <<            m_electronDzCut << SLogger::endmsg;
  m_logger << INFO << "ElectronIsoCut:      " <<            m_electronIsoCut << SLogger::endmsg;
  
  m_logger << INFO << "MuonPtCut:           " <<            m_muonPtCut << SLogger::endmsg;
  m_logger << INFO << "MuonEtaCut:          " <<            m_muonEtaCut << SLogger::endmsg;
  m_logger << INFO << "MuonD0Cut:           " <<            m_muonD0Cut << SLogger::endmsg;
  m_logger << INFO << "MuonDzCut:           " <<            m_muonDzCut << SLogger::endmsg;
  m_logger << INFO << "MuonIsoCut:          " <<            m_muonIsoCut << SLogger::endmsg;
  
  m_logger << INFO << "TauPtCut:            " <<            m_tauPtCut << SLogger::endmsg;
  m_logger << INFO << "TauEtaCut:           " <<            m_tauEtaCut << SLogger::endmsg;
  m_logger << INFO << "TauDzCut:            " <<            m_tauDzCut << SLogger::endmsg;
    
  m_logger << INFO << "JSONName:            " <<            m_jsonName << SLogger::endmsg;
  

  if (!m_isData) m_PileupReweightingTool.BeginInputData( id );
  
  
  if (m_isData) {
    TObject* grl;
    if( ! ( grl = GetConfigObject( "MyGoodRunsList" ) ) ) {
      m_logger << FATAL << "Can't access the GRL!" << SLogger::endmsg;
      throw SError( "Can't access the GRL!", SError::SkipCycle );
    }
    m_grl = *( dynamic_cast< Root::TGoodRunsList* >( grl ) );
  }
  
  
  // MARK Branches
  m_logger << INFO << "Declaring variables for branches" << SLogger::endmsg;
  for(int ch = 0; ch < (int)channels_.size(); ch++){
    
    const char* treeName = m_outputTreeName_ch_[ch].c_str();
    
    DeclareVariable( b_weight[channels_[ch]],         "weight",         treeName);
    DeclareVariable( b_genweight[channels_[ch]],      "genweight",      treeName);
    DeclareVariable( b_puweight[channels_[ch]],       "puweight",       treeName);
    DeclareVariable( b_weightbtag[channels_[ch]],     "weightbtag",     treeName);
    DeclareVariable( b_zptweight[channels_[ch]],      "zptweight",      treeName);
    DeclareVariable( b_ttptweight[channels_[ch]],     "ttptweight",     treeName);
    DeclareVariable( b_channel[channels_[ch]],        "channel",        treeName);
    DeclareVariable( b_isData[channels_[ch]],         "isData",         treeName);
    DeclareVariable( b_run[channels_[ch]],            "run",            treeName);
    DeclareVariable( b_evt[channels_[ch]],            "evt",            treeName);
    DeclareVariable( b_lum[channels_[ch]],            "lum",            treeName);
    
    DeclareVariable( b_npv[channels_[ch]],            "npv",            treeName);
    DeclareVariable( b_npu[channels_[ch]],            "npu",            treeName);
    DeclareVariable( b_NUP[channels_[ch]],            "NUP",            treeName);
    DeclareVariable( b_rho[channels_[ch]],            "rho",            treeName);
    
    DeclareVariable( b_njets[channels_[ch]],          "njets",          treeName);
    DeclareVariable( b_nfjets[channels_[ch]],         "nfjets",         treeName);
    DeclareVariable( b_ncjets[channels_[ch]],         "ncjets",         treeName);
    DeclareVariable( b_nbtag[channels_[ch]],          "nbtag",          treeName);
    DeclareVariable( b_nfbtag[channels_[ch]],         "nfbtag",         treeName);
    DeclareVariable( b_ncbtag[channels_[ch]],         "ncbtag",         treeName);
    DeclareVariable( b_njets20[channels_[ch]],        "njets20",        treeName);
    DeclareVariable( b_nfjets20[channels_[ch]],       "nfjets20",       treeName);
    DeclareVariable( b_ncjets20[channels_[ch]],       "ncjets20",       treeName);
    DeclareVariable( b_nbtag20[channels_[ch]],        "nbtag20",        treeName);
    DeclareVariable( b_nfbtag20[channels_[ch]],       "nfbtag20",       treeName);
    DeclareVariable( b_ncbtag20[channels_[ch]],       "ncbtag20",       treeName);
    
    DeclareVariable( b_pt_1[channels_[ch]],           "pt_1",           treeName);
    DeclareVariable( b_eta_1[channels_[ch]],          "eta_1",          treeName);
    DeclareVariable( b_phi_1[channels_[ch]],          "phi_1",          treeName);
    DeclareVariable( b_m_1[channels_[ch]],            "m_1",            treeName);
    DeclareVariable( b_q_1[channels_[ch]],            "q_1",            treeName);
    DeclareVariable( b_d0_1[channels_[ch]],           "d0_1",           treeName);
    DeclareVariable( b_dz_1[channels_[ch]],           "dz_1",           treeName);
    //DeclareVariable( b_mt_1[channels_[ch]],           "mt_1",           treeName);
    DeclareVariable( b_pfmt_1[channels_[ch]],         "pfmt_1",         treeName);
    DeclareVariable( b_puppimt_1[channels_[ch]],      "puppimt_1",      treeName);
    DeclareVariable( b_iso_1[channels_[ch]],          "iso_1",          treeName);
    DeclareVariable( b_id_e_mva_nt_loose_1[channels_[ch]],      "id_e_mva_nt_loose_1",     treeName);
    DeclareVariable( b_id_e_mva_nt_loose_1_old[channels_[ch]],  "id_e_mva_nt_loose_1_old", treeName);
    DeclareVariable( b_gen_match_1[channels_[ch]],    "gen_match_1",    treeName);
    DeclareVariable( b_trigweight_1[channels_[ch]],   "trigweight_1",   treeName);
    DeclareVariable( b_idisoweight_1[channels_[ch]],  "idisoweight_1",  treeName);
    
    DeclareVariable( b_pt_2[channels_[ch]],           "pt_2",           treeName);
    DeclareVariable( b_eta_2[channels_[ch]],          "eta_2",          treeName);
    DeclareVariable( b_phi_2[channels_[ch]],          "phi_2",          treeName);
    DeclareVariable( b_m_2[channels_[ch]],            "m_2",            treeName);
    DeclareVariable( b_q_2[channels_[ch]],            "q_2",            treeName);
    DeclareVariable( b_d0_2[channels_[ch]],           "d0_2",           treeName);
    DeclareVariable( b_dz_2[channels_[ch]],           "dz_2",           treeName);
    //DeclareVariable( b_mt_2[channels_[ch]],           "mt_2",           treeName);
    DeclareVariable( b_pfmt_2[channels_[ch]],         "pfmt_2",         treeName);
    DeclareVariable( b_puppimt_2[channels_[ch]],      "puppimt_2",      treeName);
    DeclareVariable( b_iso_2[channels_[ch]],          "iso_2",          treeName);
    DeclareVariable( b_iso_2_medium[channels_[ch]],   "iso_2_medium",   treeName);
    DeclareVariable( b_gen_match_2[channels_[ch]],    "gen_match_2",    treeName);
    DeclareVariable( b_trigweight_2[channels_[ch]],   "trigweight_2",   treeName);
    DeclareVariable( b_idisoweight_2[channels_[ch]],  "idisoweight_2",  treeName);
    DeclareVariable( b_pol_2[channels_[ch]],          "pol_2",          treeName);
    
    DeclareVariable( b_againstElectronVLooseMVA6_2[channels_[ch]],  "againstElectronVLooseMVA6_2",  treeName);
    DeclareVariable( b_againstElectronLooseMVA6_2[channels_[ch]],   "againstElectronLooseMVA6_2",   treeName);
    DeclareVariable( b_againstElectronMediumMVA6_2[channels_[ch]],  "againstElectronMediumMVA6_2",  treeName);
    DeclareVariable( b_againstElectronTightMVA6_2[channels_[ch]],   "againstElectronTightMVA6_2",   treeName);
    DeclareVariable( b_againstElectronVTightMVA6_2[channels_[ch]],  "againstElectronVTightMVA6_2",  treeName);
    DeclareVariable( b_againstMuonLoose3_2[channels_[ch]],          "againstMuonLoose3_2",          treeName);
    DeclareVariable( b_againstMuonTight3_2[channels_[ch]],          "againstMuonTight3_2",          treeName);
    DeclareVariable( b_byCombinedIsolationDeltaBetaCorrRaw3Hits_2[channels_[ch]], "byCombinedIsolationDeltaBetaCorrRaw3Hits_2", treeName);
    DeclareVariable( b_byIsolationMVA3newDMwLTraw_2[channels_[ch]], "byIsolationMVA3newDMwLTraw_2", treeName);
    DeclareVariable( b_byIsolationMVA3oldDMwLTraw_2[channels_[ch]], "byIsolationMVA3oldDMwLTraw_2", treeName);
    DeclareVariable( b_chargedIsoPtSum_2[channels_[ch]],            "chargedIsoPtSum_2",            treeName);
    DeclareVariable( b_neutralIsoPtSum_2[channels_[ch]],            "neutralIsoPtSum_2",            treeName);
    DeclareVariable( b_puCorrPtSum_2[channels_[ch]],                "puCorrPtSum_2",                treeName);
    DeclareVariable( b_decayModeFindingOldDMs_2[channels_[ch]],     "decayModeFindingOldDMs_2",     treeName);
    DeclareVariable( b_decayMode_2[channels_[ch]],                  "decayMode_2",                treeName);
    
    DeclareVariable( b_dilepton_veto[channels_[ch]],                "dilepton_veto",                treeName);
    DeclareVariable( b_extraelec_veto[channels_[ch]],               "extraelec_veto",               treeName);
    DeclareVariable( b_extramuon_veto[channels_[ch]],               "extramuon_veto",               treeName);
    DeclareVariable( b_lepton_vetos[channels_[ch]],                 "lepton_vetos",                 treeName);
    DeclareVariable( b_iso_cuts[channels_[ch]],                     "iso_cuts",                     treeName);
    
    DeclareVariable( b_jpt_1[channels_[ch]],        "jpt_1",            treeName);
    DeclareVariable( b_jeta_1[channels_[ch]],       "jeta_1",           treeName);
    DeclareVariable( b_jphi_1[channels_[ch]],       "jphi_1",           treeName);
    DeclareVariable( b_jpt_2[channels_[ch]],        "jpt_2",            treeName);
    DeclareVariable( b_jeta_2[channels_[ch]],       "jeta_2",           treeName);
    DeclareVariable( b_jphi_2[channels_[ch]],       "jphi_2",           treeName);
    
    DeclareVariable( b_bpt_1[channels_[ch]],        "bpt_1",            treeName);
    DeclareVariable( b_beta_1[channels_[ch]],       "beta_1",           treeName);
    DeclareVariable( b_bphi_1[channels_[ch]],       "bphi_1",           treeName);
    DeclareVariable( b_bcsv_1[channels_[ch]],       "bcsv_1",           treeName);
    DeclareVariable( b_bpt_2[channels_[ch]],        "bpt_2",            treeName);
    DeclareVariable( b_beta_2[channels_[ch]],       "beta_2",           treeName);
    DeclareVariable( b_bphi_2[channels_[ch]],       "bphi_2",           treeName);
    DeclareVariable( b_bcsv_2[channels_[ch]],       "bcsv_2",           treeName);
    
    DeclareVariable( b_met[channels_[ch]],          "met",              treeName);
    DeclareVariable( b_met_old[channels_[ch]],      "met_old",          treeName);
    DeclareVariable( b_metphi[channels_[ch]],       "metphi",           treeName);
    DeclareVariable( b_puppimet[channels_[ch]],     "puppimet",         treeName);
    DeclareVariable( b_puppimetphi[channels_[ch]],  "puppimetphi",      treeName);
    //DeclareVariable( b_mvamet[channels_[ch]],       "mvamet",           treeName);
    //DeclareVariable( b_mvamet_old[channels_[ch]],   "mvamet_old",       treeName);
    //DeclareVariable( b_mvametphi[channels_[ch]],    "mvametphi",        treeName);
    
    DeclareVariable( b_metcov00[channels_[ch]],     "metcov00",         treeName);
    DeclareVariable( b_metcov01[channels_[ch]],     "metcov01",         treeName);
    DeclareVariable( b_metcov10[channels_[ch]],     "metcov10",         treeName);
    DeclareVariable( b_metcov11[channels_[ch]],     "metcov11",         treeName);
    //DeclareVariable( b_mvacov00[channels_[ch]],     "mvacov00",         treeName);
    //DeclareVariable( b_mvacov01[channels_[ch]],     "mvacov01",         treeName);
    //DeclareVariable( b_mvacov10[channels_[ch]],     "mvacov10",         treeName);
    //DeclareVariable( b_mvacov11[channels_[ch]],     "mvacov11",         treeName);
    
    DeclareVariable( b_m_vis[channels_[ch]],        "m_vis",            treeName);
    DeclareVariable( b_pt_tt[channels_[ch]],        "pt_tt",            treeName);
    DeclareVariable( b_pt_tt_vis[channels_[ch]],    "pt_tt_vis",        treeName);
    DeclareVariable( b_R_pt_m_vis[channels_[ch]],   "R_pt_m_vis",       treeName);
    DeclareVariable( b_R_pt_m_vis2[channels_[ch]],  "R_pt_m_vis2",      treeName);
    
    DeclareVariable( b_m_sv[channels_[ch]],         "m_sv",             treeName);
    //DeclareVariable( b_m_sv_pfmet[channels_[ch]],   "m_sv_pfmet",       treeName);
    DeclareVariable( b_pt_tt_sv[channels_[ch]],     "pt_tt_sv",         treeName);
    DeclareVariable( b_R_pt_m_sv[channels_[ch]],    "R_pt_m_sv",        treeName);
    
    DeclareVariable( b_dR_ll[channels_[ch]],        "dR_ll",            treeName);
    DeclareVariable( b_dR_ll_gen[channels_[ch]],    "dR_ll_gen",        treeName);
    DeclareVariable( b_dphi_ll_bj[channels_[ch]],   "dphi_ll_bj",       treeName);
    DeclareVariable( b_mt_tot[channels_[ch]],       "mt_tot",           treeName);
    DeclareVariable( b_ht[channels_[ch]],           "ht",               treeName);
    
    DeclareVariable( b_m_genboson[channels_[ch]],   "m_genboson",       treeName);
    DeclareVariable( b_pt_genboson[channels_[ch]],  "pt_genboson",      treeName);
    
    DeclareVariable( b_pzetamiss[channels_[ch]],    "pzetamiss",        treeName);
    DeclareVariable( b_pzetavis[channels_[ch]],     "pzetavis",         treeName);
    DeclareVariable( b_pzeta_disc[channels_[ch]],   "pzeta_disc",       treeName);
    DeclareVariable( b_vbf_mjj[channels_[ch]],      "vbf_mjj",          treeName);
    DeclareVariable( b_vbf_deta[channels_[ch]],     "vbf_deta",         treeName);
    DeclareVariable( b_vbf_jdphi[channels_[ch]],    "vbf_jdphi",        treeName);
    DeclareVariable( b_vbf_ncentral[channels_[ch]], "vbf_ncentral",     treeName);
    DeclareVariable( b_vbf_ncentral20[channels_[ch]], "vbf_ncentral20", treeName);

  }
  
  
  // MARK Histograms
  m_logger << INFO << "Declaring histograms" << SLogger::endmsg;
  
  // histograms - cutflow
  for (auto ch: channels_){
    TString hname = "cutflow_" + ch;
    TString dirname = "histogram_" + ch;
    TString tch = ch;
    std::cout << hname << " " << dirname << std::endl;
    Book( TH1F(hname, hname, 20, 0.5, 20.5 ), dirname);
    Book( TH1F("lepton_"+tch, "lepton_"+tch, 20, 0.5, 20.5 ), dirname);
    Book( TH1F("tauh1_"+tch,  "tauh1_"+tch,  20, 0.5, 20.5 ), dirname);
    Book( TH1F("tauh2_"+tch,  "tauh2_"+tch,  20, 0.5, 20.5 ), dirname);
    Book( TH1F("jet_"+tch,    "jet_"+tch,    20, 0.5, 20.5 ), dirname);
    //Book( TH1F("N_match0p30_bst_std_"+tch, "N_match0p30_bst_std_"+tch, 5, 0,  5 ), dirname);
  }
  
  // histograms - checks
//   if(m_isSignal){
//   
//     // gen level distributions checks
//     Book( TH1F("pt_gentaus",      "gen taus pt",      150, 0, 150 ), "checks");
//     Book( TH1F("pt_gentau1",      "gen tau 1 pt",     150, 0, 150 ), "checks");
//     Book( TH1F("pt_gentau2",      "gen tau 2 pt",     150, 0, 150 ), "checks");
//     Book( TH1F("pt_genmuon",      "gen muon pt",      100, 0, 100 ), "checks");
//     Book( TH1F("pt_tt_gen",       "gen pt_tt",        150, 0, 200 ), "checks");
//     Book( TH1F("DeltaR_tautau",   "DeltaR_tautau",    150, 0,   5 ), "checks");
//     Book( TH1F("DeltaR_taumu",    "DeltaR_taumu",     150, 0,   5 ), "checks");
//     Book( TH1F("M_tautau",        "M_tautau",         200, 0,  60 ), "checks");
//     
//     // cutflow checks
//     Book( TH1F("N_tauh_gen",      "N_tauh_gen",         5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_gen",       "N_tau_gen",          5, 0,   5 ), "checks");
//     Book( TH1F("N_tauh_18_2p3_gen", "N_tauh_18_2p3_gen", 5, 0,  5 ), "checks");
//     Book( TH1F("N_tau_reco",      "N_tau_reco",         5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_reco_18_2p3", "N_tau_reco_18_2p3", 5, 0,   5 ), "checks");
//     Book( TH1F("tau_type",        "tau_type",           5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_std",       "N_tau_std",          5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_bst",       "N_tau_bst",          5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_18_2p3_std", "N_tau_18_2p3_std",  5, 0,   5 ), "checks");
//     Book( TH1F("N_tau_18_2p3_1ctauh_std", "N_tau_18_2p3_1ctauh_std",  5, 0,   5 ), "checks");
//     Book( TH1F("gen_match_tau_std", "gen_match_tau_std", 8, 0,  8 ), "checks");
//     Book( TH1F("gen_match_tau_bst", "gen_match_tau_bst", 8, 0,  8 ), "checks");
//     Book( TH1F("N_gen_match0p30_tau_std", "N_gen_match0p30_tau_std", 5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_tau_bst", "N_gen_match0p30_tau_bst", 5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_1bst_tau_std", "N_gen_match0p30_1bst_tau_std", 5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_1bst_18_2p3_tau_std", "N_gen_match0p30_1bst_18_2p3_tau_std", 5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_1ctauh_tau_std",  "N_gen_match0p30_1ctauh_tau_std", 5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_0tauh_tau_std",   "N_gen_match0p30_0tauh_tau_std",  5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match_tau_1cjet_bst",       "N_gen_match_tau_1cjet_bst",      5, 0,  5 ), "checks");
//     Book( TH1F("N_gen_match0p30_18_2p3_tau_std",  "N_gen_match0p30_18_2p3_tau_std", 5, 0,  5 ), "checks");
//     Book( TH1F("DeltaR_gen_reco_tau_std", "DeltaR_gen_reco_tau_std", 100, 0, 5 ), "checks");
//     Book( TH1F("DeltaR_gen_reco_tau_bst", "DeltaR_gen_reco_tau_bst", 100, 0, 5 ), "checks");
//     Book( TH1F("DeltaR_gen_reco_tau_min_1ctauh_std",  "DeltaR_gen_reco_tau_min_1ctauh_std", 100, 0, 5 ), "checks");
//     Book( TH1F("DeltaR_gen_reco_tau_min_0tauh_std",   "DeltaR_gen_reco_tau_min_0tauh_std", 100, 0, 5 ), "checks");
//     Book( TH1F("eta_tau_reco",    "eta_tau_reco",     100, -5, 5 ), "checks");
//     Book( TH1F("pt_tau_reco",     "pt_tau_reco",      100, 0, 100 ), "checks");
//     Book( TH1F("DeltaDeltaR",     "DeltaDeltaR",      100, -1,  5 ), "checks"); // abs(dR_TLV - dR_function)
//     Book( TH1F("decayModeFinding", "decayModeFinding",   2,  0,  2 ), "checks");
//     
//     // boosted regime checks
//     Book( TH1F("pt_tt_vis",         "pt_tt_vis",      100, 0, 200 ), "checks");
//     Book( TH1F("pt_tt_vis_ltau",    "pt_tt_vis_ltau", 100, 0, 200 ), "checks");
//     Book( TH2F("DeltaR_pt_tt_vis_ltau",     "DeltaR_pt_tt_vis_ltau",     100, 0, 200, 100, 0,   5 ), "checks");
//     Book( TH2F("DeltaR_pt_tt_vis_ltau_std", "DeltaR_pt_tt_vis_ltau_std", 100, 0, 200, 100, 0,   5 ), "checks");
//     Book( TH2F("DeltaR_pt_tt_vis_ltau_bst", "DeltaR_pt_tt_vis_ltau_bst", 100, 0, 200, 100, 0,   5 ), "checks");
//     
//   }
  
  m_BTaggingScaleTool.BeginInputData( id );
  m_ScaleFactorTool.BeginInputData( id );
  m_RecoilCorrector.BeginInputData( id );
  m_SVFitTool.BeginInputData( id );

  return;

}





void TauTauAnalysis::EndInputData( const SInputData& ) throw( SError ) {
  std::cout << "EndInputData" << std::endl;

  std::vector<std::string> kCutNameLep{ "start", "match", "ID",        "iso", "pt" };
  //std::vector<std::string> kCutNameTau{ "start", "match", "DecayMode", "iso", "pt" };
  std::vector<std::string> kCutNameTau{ "start", "at least one reco tau", "2.3 eta and 18 pt reco cut", "tau ID", "2.3 eta and 18 pt gen cut", "match", "DecayMode", "iso", "pt" };
  std::vector<std::string> kCutNameJet{ "start", "one eta<2.3 jet && hadronic" };
  
  for(auto ch: channels_) {
    m_logger << INFO << " " << SLogger::endmsg;
    m_logger << INFO << "cut flow for " << ch << SLogger::endmsg;
    m_logger << INFO << Form( "Cut\t%25.25s\tEvents\tRelEff\tAbsEff", "Name" ) << SLogger::endmsg;
  
    TString hname = "cutflow_" + ch;
    TString dirname = "histogram_" + ch;
    Double_t ntot = Hist(hname, dirname)->GetBinContent( 1 );
    m_logger << INFO << Form( "\t%25.25s\t%6.0f", "start", ntot ) << SLogger::endmsg;
    for( Int_t ibin = 1; ibin < kNumCuts; ++ibin ) {
      Int_t    icut    = ibin;
      Double_t nevents = Hist(hname, dirname)->GetBinContent( ibin+1 );
      Double_t releff  = 100. * nevents / Hist(hname, dirname)->GetBinContent( ibin );
      Double_t abseff  = 100. * nevents / ntot;
      m_logger << INFO  << Form( "C%d\t%25.25s\t%6.0f\t%6.2f\t%6.2f", icut-1, kCutName[icut].c_str(), nevents, releff, abseff ) << SLogger::endmsg;
    }
    
//     if(m_isSignal and ch == "mutau"){
//       printCutFlow(ch,"lepton","lepton_"+ch,dirname,kCutNameLep);
//       printCutFlow(ch,"tau standard ID","tauh1_"+ch,dirname,kCutNameTau);
//       printCutFlow(ch,"tau boosted ID","tauh2_"+ch,dirname,kCutNameTau);
//       printCutFlow(ch,"jet","jet_"+ch,dirname,kCutNameJet);
//     }

    std::cout << std::endl;
  }

   return;
}
void TauTauAnalysis::printCutFlow(const std::string& ch, const std::string& name, const TString hname, const TString dirname, std::vector<std::string> cutName){
//   std::cout << "printCutFlow" << std::endl;
    
    Double_t ntot = Hist(hname, dirname)->GetBinContent( 1 );
    m_logger << INFO << " " << SLogger::endmsg;
    m_logger << INFO << name << " cut flow for " << ch << SLogger::endmsg;
    m_logger << INFO << Form( "Cut\t%25.25s\tEvents\tRelEff\tAbsEff", "Name" ) << SLogger::endmsg;
    m_logger << INFO << Form( "\t%25.25s\t%6.0f", "start", ntot ) << SLogger::endmsg;
    for( Int_t ibin = 1; ibin < (int) cutName.size(); ++ibin ){
      Int_t    icut    = ibin;
      Double_t nevents = Hist(hname, dirname)->GetBinContent( ibin+1 );
      Double_t releff  = 100. * nevents / Hist(hname, dirname)->GetBinContent( ibin );
      Double_t abseff  = 100. * nevents / ntot;
      m_logger << INFO  << Form( "C%d\t%25.25s\t%6.0f\t%6.2f\t%6.2f", icut-1, cutName[icut].c_str(), nevents, releff, abseff ) << SLogger::endmsg;
    }
}





void TauTauAnalysis::BeginInputFile( const SInputData& ) throw( SError ) {
//   std::cout << "BeginInputFile" << std::endl;

  m_logger << INFO << "Connecting input variables" << SLogger::endmsg;
  if (m_isData) {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis, (m_jetAK4Name + "_").c_str() );
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoTrigger|Ntuple::EventInfoMETFilters, "" );
  }
  else {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis|Ntuple::JetTruth, (m_jetAK4Name + "_").c_str() );
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoBasic|Ntuple::EventInfoTrigger|Ntuple::EventInfoMETFilters|Ntuple::EventInfoTruth, "" );
    m_genParticle.ConnectVariables( m_recoTreeName.c_str(), Ntuple::GenParticleBasic|Ntuple::GenParticleTauDecayAnalysis, (m_genParticleName + "_").c_str() );
  }
  m_electron.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::ElectronBasic|Ntuple::ElectronID|Ntuple::ElectronAdvancedID|Ntuple::ElectronBoostedIsolation|Ntuple::ElectronSuperCluster, (m_electronName + "_").c_str() );
  m_muon.ConnectVariables(          m_recoTreeName.c_str(), Ntuple::MuonBasic|Ntuple::MuonID|Ntuple::MuonIsolation|Ntuple::MuonTrack|Ntuple::MuonBoostedIsolation, (m_muonName + "_").c_str() );
  m_tau.ConnectVariables(           m_recoTreeName.c_str(), Ntuple::TauBasic|Ntuple::TauID|Ntuple::TauAdvancedID, (m_tauName + "_").c_str() );

  m_missingEt.ConnectVariables(     m_recoTreeName.c_str(), Ntuple::MissingEtBasic|Ntuple::MissingEtAnalysis|Ntuple::MissingEtCovAnalysis , (m_missingEtName + "_").c_str() );
  m_puppimissingEt.ConnectVariables(m_recoTreeName.c_str(), Ntuple::MissingEtBasic, (m_missingEtName + "_puppi_").c_str() );
  //m_mvamissingEt.ConnectVariables(  m_recoTreeName.c_str(), Ntuple::MissingEtBasic|Ntuple::MissingEtMVAAnalysis|Ntuple::MissingEtCovAnalysis, (m_missingEtName + "_mva_").c_str() );
  
  m_logger << INFO << "Connecting input variables completed" << SLogger::endmsg;
  
  return;

}





void TauTauAnalysis::ExecuteEvent( const SInputData&, Double_t ) throw( SError ) {
  //std::cout << "ExecuteEvent" << std::endl;
  m_logger << VERBOSE << "ExecuteEvent" << SLogger::endmsg;
  
  b_weight_     =  1.;
  b_genweight_  =  1.;
  b_npu_        = -1.;
  
  
  // Cut 0: no cuts
  for (auto ch: channels_){
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCuts, 1);
    b_channel[ch] = 0;
  }
  // if (m_isSignal){
  // checks();
  // visiblePTCheck();
  // for (auto ch: channels_){
  //   cutflowCheck(ch);
  // }
  // }
  
  
  // Cut 1: check for data if run/lumiblock in JSON
  if (m_isData) {
    if(!(isGoodEvent(m_eventInfo.runNumber, m_eventInfo.lumiBlock))) throw SError( SError::SkipEvent );
  }
  else{
    getEventWeight();
    //genFilterZtautau(); // checks Z-tautau not cut away
  }
  
  for (auto ch: channels_){
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kJSON, 1);
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCutsWeighted, b_genweight_);
  }
  
  

  // Cut 2: pass trigger
  //std::cout << ">>> ExecuteEvent - Cut 2" << std::endl;
  TString trigger_result = "both";
  if(m_isData) trigger_result = passTrigger(m_eventInfo.runNumber, m_eventInfo.lumiBlock);
  //trigger_result = passTrigger();
  if(trigger_result != "none") m_logger << VERBOSE << "Trigger pass" << SLogger::endmsg;
  else throw SError( SError::SkipEvent );
  
  for (auto ch: channels_){
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kTrigger, 1);
  }
  
  
  
  // Cut 3: pass MET filters
  //std::cout << ">>> ExecuteEvent - Cut 4" << std::endl;
  //if (passMETFilters()) m_logger << VERBOSE << "passMETFilters" << SLogger::endmsg;
  //else throw SError( SError::SkipEvent );
  
  for (auto ch: channels_){
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kMetFilters, 1);
  }
  
  
  
  // Cut 4: lepton (muon)
  //std::cout << ">>> ExecuteEvent - Cut 4 - muon" << std::endl;
  std::vector<UZH::Muon> goodMuons;
  for( int i = 0; i < m_muon.N; ++i ){
    UZH::Muon mymuon( &m_muon, i );
    
    if (mymuon.pt() < m_muonPtCut) {continue;}
    if (fabs(mymuon.eta()) > m_muonEtaCut) {continue;}
    if (fabs(mymuon.d0_allvertices()) > m_muonD0Cut) {continue;}
    if (fabs(mymuon.dz_allvertices()) > m_muonDzCut) {continue;}
    if (mymuon.isMediumMuon() < 0.5) {continue;}
    //if (mymuon.SemileptonicPFIso() / mymuon.pt() > m_muonIsoCut) continue;
    
    goodMuons.push_back(mymuon);
  }
   
  // Cut 4: lepton (electron)
  //std::cout << ">>> ExecuteEvent - Cut 2 - electron" << std::endl;
  std::vector<UZH::Electron> goodElectrons;
  for ( int i = 0; i < m_electron.N; ++i ) {
    UZH::Electron myelectron( &m_electron, i );
    
    Float_t elept = myelectron.pt();
    if(m_doEES){
      if(fabs(myelectron.eta())<1.479) elept *= (1+m_EESshift);
      else                             elept *= (1+m_EESshiftEndCap);
    }
    
    if (elept < m_electronPtCut) continue;
    if (fabs(myelectron.eta()) > m_electronEtaCut) continue;
    if (fabs(myelectron.d0_allvertices()) > m_electronD0Cut) continue;
    if (fabs(myelectron.dz_allvertices()) > m_electronDzCut) continue;
    if (myelectron.passConversionVeto()!=1) continue;
    if (myelectron.expectedMissingInnerHits()>1) continue;
    //if (myelectron.isMVATightElectron() < 0.5) continue; // Moriond
    if (isNonTrigElectronID(myelectron) < 0.5) continue; // ICHEP
    //if (myelectron.SemileptonicPFIso() / myelectron.pt() > m_electronIsoCut) continue;
	
    goodElectrons.push_back(myelectron);
  }
  
  
  if(goodMuons.size()!=0){
    fillCutflow("cutflow_mutau", "histogram_mutau", kLepton, 1);
  }
  if(goodElectrons.size()!=0){
    fillCutflow("cutflow_eletau", "histogram_eletau", kLepton, 1);
  }
  else if(goodMuons.size()==0) throw SError( SError::SkipEvent );
  
  
  
  // Cut 6: lepton - tau pair
  
  // For tau
  //std::cout << ">>> ExecuteEvent - Cut 6 - tau" << std::endl;
  std::vector<UZH::Tau> goodTaus;
  std::vector<int> goodTausGen;
  
  for ( int i = 0; i <   (m_tau.N); ++i ) {
    UZH::Tau mytau( &m_tau, i );
    if(mytau.TauType()!=1) continue; // 1 for standard ID, 2 for boosted ID
    if(fabs(mytau.eta()) > m_tauEtaCut) continue;
    if(fabs(mytau.dz()) > m_tauDzCut) continue;
    if(mytau.decayModeFinding() < 0.5) continue;
    if(fabs(mytau.charge()) != 1) continue; // remove for boosted ID
    //if(mytau.byTightIsolationMVArun2v1DBoldDMwLT() < 0.5) continue;
    
    // TES + genmatch_2
    Float_t taupt = mytau.pt();
    Int_t genmatch_2 = -1;
    if(m_doTES || m_doLTF){
      genmatch_2 = genMatch(mytau.eta(), mytau.phi());
      if(m_doTES && genmatch_2==5) taupt *= (1+m_TESshift);
      if(m_doLTF && genmatch_2<5)  taupt *= (1+m_LTFshift);
    }
    if(taupt < m_tauPtCut) continue;
    
    goodTaus.push_back(mytau);
    goodTausGen.push_back(genmatch_2);
  }
  
  if(goodTaus.size()==0) throw SError( SError::SkipEvent );
  
  
  // First, select muon with highest isolation, and then, highest pT
  
  // For mu-tau
  //std::cout << ">>> ExecuteEvent - Cut 6 - mutau" << std::endl;
  std::vector<ltau_pair> mutau_pair;
  bool passedDeltaRCut = false; // check
  for(int imuon=0; imuon < (int)goodMuons.size(); imuon++){
    if(trigger_result == "ele") break; // trigger
    for(int itau=0; itau < (int)goodTaus.size(); itau++){
      
      Float_t dR = goodMuons[imuon].tlv().DeltaR(goodTaus[itau].tlv());
      if(dR < 0.5) continue; // remove or lower for boosted ID
      //if(dR > 0.5) passedDeltaRCut = true; // check
      //Hist("DeltaR_taumu_reco", "checks" )->Fill( dR ); // check
      
      Float_t mupt = goodMuons[imuon].pt();
      Float_t reliso = goodMuons[imuon].SemileptonicPFIso() / mupt;
      Float_t taupt = goodTaus[itau].pt();
      
      if(m_doTES && goodTausGen[itau]==5) taupt *= (1+m_TESshift);
      if(m_doLTF && goodTausGen[itau]<5)  taupt *= (1+m_LTFshift);
      
      Float_t tauiso = goodTaus[itau].byIsolationMVArun2v1DBoldDMwLTraw();
      ltau_pair pair = {imuon, reliso, mupt, itau, tauiso, taupt, dR};
      mutau_pair.push_back(pair);
    }
  }
  
  // check delta R cut 
  //if(mutau_pair.size()!=0){
  //  fillCutflow("cutflow_mutau", "histogram_mutau", kDeltaR_before, 1);
  //  if(passedDeltaRCut) fillCutflow("cutflow_mutau", "histogram_mutau", kDeltaR, 1);
  //}
  
  // For ele-tau
  //std::cout << ">>> ExecuteEvent - Cut 6 - etau" << std::endl;
  std::vector<ltau_pair> eletau_pair;
  
  for(int ielectron=0; ielectron < (int)goodElectrons.size(); ielectron++){
    if(trigger_result == "mu") break; // trigger
    for(int itau=0; itau < (int)goodTaus.size(); itau++){
      
      Float_t dR = goodElectrons[ielectron].tlv().DeltaR(goodTaus[itau].tlv());
      if(dR < 0.5) continue; // remove or lower for boosted ID
      
      Float_t elept = goodElectrons[ielectron].pt();
      Float_t taupt = goodTaus[itau].pt();
      
      if(m_doTES && goodTausGen[itau]==5) taupt *= (1+m_TESshift);
      if(m_doLTF && goodTausGen[itau]<5)  taupt *= (1+m_LTFshift);
      if(m_doEES){
        if(fabs(goodElectrons[ielectron].eta())<1.479) elept *= (1+m_EESshift);
        else                                           elept *= (1+m_EESshiftEndCap);
      }
      
      Float_t reliso = goodElectrons[ielectron].SemileptonicPFIso() / elept;
      Float_t tauiso = goodTaus[itau].byIsolationMVArun2v1DBoldDMwLTraw();
      
      ltau_pair pair = {ielectron, reliso, elept, itau, tauiso, taupt}; //, dR};
      eletau_pair.push_back(pair);
    }
  }
    
  if(mutau_pair.size()==0 && eletau_pair.size()==0){
    throw SError( SError::SkipEvent );
  }
  
  UZH::MissingEt Met( &m_missingEt, 0 );
  UZH::MissingEt PuppiMet( &m_puppimissingEt, 0 );
  
  // This depends on the channel
  UZH::Muon dummyMuon;
  UZH::Electron dummyElectron;
  
  // For mu-tau
  if(mutau_pair.size()!=0){
    
    fillCutflow("cutflow_mutau", "histogram_mutau", kLepTau, 1);
    sort(mutau_pair.begin(), mutau_pair.end());
    
    // UZH::MissingEt MvaMet;
    // for ( int i = 0; i < (Met.Nmva()); ++i ) {
    //   UZH::MissingEt myMvaMet( &m_mvamissingEt, i );
    //   
    //   bool flag_lep = false;
    //   bool flag_tau = false;
    //   
    //   for(int ipf=0; ipf < (int) myMvaMet.recoil_pt().size(); ipf++){
    //     Float_t recoil_pt = myMvaMet.recoil_pt().at(ipf);
    //     Float_t recoil_eta = myMvaMet.recoil_eta().at(ipf);
    //     Float_t recoil_phi = myMvaMet.recoil_phi().at(ipf);
    //     Int_t recoil_pdgId = abs(myMvaMet.recoil_pdgId().at(ipf));
    //     
    //     if(recoil_pt == goodMuons[mutau_pair[0].ilepton].pt() && 
    //        recoil_eta == goodMuons[mutau_pair[0].ilepton].eta() && 
    //        recoil_phi == goodMuons[mutau_pair[0].ilepton].phi() &&
    //        recoil_pdgId == 13) flag_lep = true;
    //     
    //     if(recoil_pt == goodTaus[mutau_pair[0].itau].pt() && 
    //        recoil_eta == goodTaus[mutau_pair[0].itau].eta() && 
    //        recoil_phi == goodTaus[mutau_pair[0].itau].phi() && 
    //        recoil_pdgId == 15) flag_tau = true;
    //   }
    //   
    //   if(flag_lep==true && flag_tau==true) MvaMet = myMvaMet;
    //   
    // }
    
    // For Jets
    std::vector<UZH::Jet> goodJetsAK4;
    for ( int i = 0; i < (m_jetAK4.N); ++i ) {
      UZH::Jet myjetak4( &m_jetAK4, i );
      
      Float_t dr_mj = deltaR(myjetak4.eta() - goodMuons[mutau_pair[0].ilepton].eta(), 
                      deltaPhi(myjetak4.phi(), goodMuons[mutau_pair[0].ilepton].phi()));
      if(dr_mj < 0.5) continue;
      
      Float_t dr_tj = deltaR(myjetak4.eta() - goodTaus[mutau_pair[0].itau].eta(), 
			          deltaPhi(myjetak4.phi(), goodTaus[mutau_pair[0].itau].phi()));
      if(dr_tj < 0.5) continue;
      
      if (fabs(myjetak4.eta()) > m_AK4jetEtaCut) continue;
      if (myjetak4.pt() < m_AK4jetPtCut) continue;
      if (!LooseJetID(myjetak4)) continue; // !myjetak4.IDLoose()
      
      goodJetsAK4.push_back(myjetak4);
    }
    
    //std::cout << ">>> ExecuteEvent - FillBranches mutau" << std::endl;
    Int_t genmatch_2 = goodTausGen[mutau_pair[0].itau];
    if( !m_isData && genmatch_2<0)
      genmatch_2 = genMatch(goodTaus[mutau_pair[0].itau].eta(), goodTaus[mutau_pair[0].itau].phi());
    FillBranches( "mutau", goodJetsAK4, goodTaus[mutau_pair[0].itau], genmatch_2, goodMuons[mutau_pair[0].ilepton], dummyElectron, Met, PuppiMet );//, MvaMet);
    mu_tau++;
    
  }
  
  
  // For ele-tau
  if(eletau_pair.size()!=0){
    fillCutflow("cutflow_eletau", "histogram_eletau", kLepTau, 1);
    sort(eletau_pair.begin(), eletau_pair.end());
    
    // UZH::MissingEt MvaMet;
    // for ( int i = 0; i < (Met.Nmva()); ++i ) {
    //   UZH::MissingEt myMvaMet( &m_mvamissingEt, i );
    //   
    //   bool flag_lep = false;
    //   bool flag_tau = false;
    //   
    //   for(int ipf=0; ipf < (int) myMvaMet.recoil_pt().size(); ipf++){
    //     Float_t recoil_pt = myMvaMet.recoil_pt().at(ipf);
    //     Float_t recoil_eta = myMvaMet.recoil_eta().at(ipf);
    //     Float_t recoil_phi = myMvaMet.recoil_phi().at(ipf);
    //     Int_t recoil_pdgId = abs(myMvaMet.recoil_pdgId().at(ipf));
    //     
    //     if(recoil_pt == goodElectrons[eletau_pair[0].ilepton].pt() && 
    //        recoil_eta == goodElectrons[eletau_pair[0].ilepton].eta() && 
    //        recoil_phi == goodElectrons[eletau_pair[0].ilepton].phi() && 
    //        recoil_pdgId == 11) flag_lep = true;
    //     
    //     if(recoil_pt == goodTaus[eletau_pair[0].itau].pt() && 
    //        recoil_eta == goodTaus[eletau_pair[0].itau].eta() && 
    //        recoil_phi == goodTaus[eletau_pair[0].itau].phi() && 
    //        recoil_pdgId == 15) flag_tau = true;
    //   }
    //   
    //   if(flag_lep==true && flag_tau==true) MvaMet = myMvaMet;
    // 
    // }
    
    
    // For Jets
    std::vector<UZH::Jet> goodJetsAK4;
    for ( int i = 0; i < (m_jetAK4.N); ++i ) {
      UZH::Jet myjetak4( &m_jetAK4, i );
      
      Float_t dr_ej = deltaR(myjetak4.eta() - goodElectrons[eletau_pair[0].ilepton].eta(), 
			          deltaPhi(myjetak4.phi(), goodElectrons[eletau_pair[0].ilepton].phi()));
      if(dr_ej < 0.5) continue;
      
      Float_t dr_tj = deltaR(myjetak4.eta() - goodTaus[eletau_pair[0].itau].eta(), 
			          deltaPhi(myjetak4.phi(), goodTaus[eletau_pair[0].itau].phi()));
      if(dr_tj < 0.5) continue;
      
      if (fabs(myjetak4.eta()) > m_AK4jetEtaCut) continue;
      if (myjetak4.pt() < m_AK4jetPtCut) continue;
      if (!LooseJetID(myjetak4)) continue;
      
      goodJetsAK4.push_back(myjetak4);
    }
    
    //std::cout << ">>> ExecuteEvent - FillBranches eletau" << std::endl;
    Int_t genmatch_2 = goodTausGen[eletau_pair[0].itau];
    if( !m_isData && !m_doTES && !m_doLTF)
      genmatch_2 = genMatch(goodTaus[eletau_pair[0].itau].eta(), goodTaus[eletau_pair[0].itau].phi());
    FillBranches( "eletau", goodJetsAK4, goodTaus[eletau_pair[0].itau], genmatch_2, dummyMuon, goodElectrons[eletau_pair[0].ilepton], Met, PuppiMet );//, MvaMet);
    ele_tau++;
    
  }
  
  return;
  
}





bool TauTauAnalysis::isGoodEvent(int runNumber, int lumiSection) {
//   std::cout << "isGoodEvent" << std::endl;
  
  bool isGood = true;
  if (m_isData) {
    isGood = m_grl.HasRunLumiBlock( runNumber, lumiSection );
    if( !isGood ) {
      m_logger << WARNING << "Bad event! Run: " << runNumber <<  " - Lumi Section: " << lumiSection << SLogger::endmsg;
      // throw SError( SError::SkipEvent );
    }
    else m_logger << VERBOSE << "Good event! Run: " << runNumber <<  " - Lumi Section: " << lumiSection << SLogger::endmsg;
  }
  
  return isGood;
  
}





TString TauTauAnalysis::passTrigger(int runNumber, int lumiSection) {
//   std::cout << "TauTauAnalysis" << std::endl;
  
  bool flag_mu_trigger = false;
  bool flag_ele_trigger = false;

  for (std::map<std::string,bool>::iterator it = (m_eventInfo.trigDecision)->begin(); it != (m_eventInfo.trigDecision)->end(); ++it){
    for (unsigned int t = 0; t < m_triggerNames_mutau.size(); ++t ){
      if ((it->first).find(m_triggerNames_mutau[t]) != std::string::npos) {
        if (it->second == true) {
          m_logger << VERBOSE << "Trigger pass: " << (it->first) << SLogger::endmsg;
          flag_mu_trigger = true;
          //return true;
        }
      }
    }
  }

  for (std::map<std::string,bool>::iterator it = (m_eventInfo.trigDecision)->begin(); it != (m_eventInfo.trigDecision)->end(); ++it){
    for (unsigned int t = 0; t < m_triggerNames_eletau.size(); ++t ){
      if ((it->first).find(m_triggerNames_eletau[t]) != std::string::npos) {
        if (it->second == true) {
          m_logger << VERBOSE << "Trigger pass: " << (it->first) << SLogger::endmsg;
	      flag_ele_trigger = true;
	      //return true;
        }
      }
    }
  }

  if(flag_mu_trigger == true  && flag_ele_trigger == true ) return "both";
  if(flag_mu_trigger == true  && flag_ele_trigger == false) return "mu";
  if(flag_mu_trigger == false && flag_ele_trigger == true ) return "ele";

  return "none";
  
}





bool TauTauAnalysis::passMETFilters() {
//   std::cout << "passMETFilters" << std::endl;
  
  bool passMetFilters = true;
  
  // using only what's recommended in https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2
  if( !(m_eventInfo.PV_filter) ) {
    passMetFilters = false;
    m_logger << VERBOSE << "PV_filter" << SLogger::endmsg;
  }
  if( !(m_eventInfo.passFilter_CSCHalo) ) {
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_CSCHalo" << SLogger::endmsg;
  }
  if( !(m_eventInfo.passFilter_HBHELoose) ) {
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_HBHELoose" << SLogger::endmsg;
  }
  if( !(m_eventInfo.passFilter_HBHEIso) ) {
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_HBHEIso" << SLogger::endmsg;
  }
  if( !(m_eventInfo.passFilter_EEBadSc) ) {
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_EEBadSc" << SLogger::endmsg;
  }
 
  if( !(m_eventInfo.passFilter_globalTightHalo2016) ){
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_EEBadSc" << SLogger::endmsg;
  }

  if( !(m_eventInfo.passFilter_chargedHadronTrackResolution) ){
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_EEBadSc" << SLogger::endmsg;
  }

  if( !(m_eventInfo.passFilter_muonBadTrack) ) {        
    passMetFilters = false;
    m_logger << VERBOSE << "passFilter_EEBadSc" << SLogger::endmsg;
  } 
  
  return passMetFilters;
  
}





void TauTauAnalysis::getEventWeight() {
//   std::cout << "getEventWeight" << std::endl;
  
  double weight = 1.;
  b_npu_ = -1.;
  for( unsigned int v = 0; v < (m_eventInfo.actualIntPerXing)->size(); ++v ){
    
    if ( (*m_eventInfo.bunchCrossing)[v] == 0 ) {
      b_npu_ = (*m_eventInfo.actualIntPerXing)[v]; // averageIntPerXing
      b_puweight_ = m_PileupReweightingTool.getPileUpweight( b_npu_ );
      m_logger << VERBOSE << "Weight: " << b_puweight_ << " for true: " << b_npu_ << SLogger::endmsg;
      break;
    }
  }
  
  b_genweight_ = (m_eventInfo.genEventWeight < 0) ? -1 : 1; 
  b_weight_ *= b_puweight_*b_genweight_;
  
}





void TauTauAnalysis::fillCutflow(TString histName, TString dirName, const Int_t id, const Double_t weight){
//   std::cout << "fillCutflow" << std::endl;
  Hist( histName, dirName )->Fill( id+1, weight );
}





void TauTauAnalysis::FillBranches(const std::string& channel, const std::vector<UZH::Jet> &Jet,
                                  const UZH::Tau& tau, const int gen_match_2, const UZH::Muon& muon, const UZH::Electron& electron,
                                  const UZH::MissingEt& met, const UZH::MissingEt& puppimet){//, const UZH::MissingEt& mvamet){
  //std::cout << "FillBranches" << std::endl;
  
  const char* ch = channel.c_str();
  b_weightbtag_ = 1.;
  if(m_doRecoilCorr || m_doZpt) setGenBosonTLVs(); // only for HTT, DY and WJ
  
  b_weight[ch]      = b_weight_;
  b_genweight[ch]   = b_genweight_;
  b_puweight[ch]    = b_puweight_;
  b_evt[ch]         = m_eventInfo.eventNumber;
  b_run[ch]         = m_eventInfo.runNumber;
  b_lum[ch]         = m_eventInfo.lumiBlock;
  b_isData[ch]      = (Int_t) m_isData;
  
  b_npu[ch]         = b_npu_; // for MC defined in getEventWeight
  b_npv[ch]         = m_eventInfo.PV_N;
  b_NUP[ch]         = m_eventInfo.lheNj;
  b_rho[ch]         = m_eventInfo.rho;
  
  Int_t njets       =  0;
  Int_t nfjets      =  0;
  Int_t ncjets      =  0;
  Int_t nbtag       =  0;
  Int_t nfbtag      =  0;
  Int_t ncbtag      =  0;
  Int_t njets20     =  0;
  Int_t nfjets20    =  0;
  Int_t ncjets20    =  0;
  Int_t nbtag20     =  0;
  Int_t nfbtag20    =  0;
  Int_t ncbtag20    =  0;
  Int_t ibjet1      = -1;
  Int_t ibjet2      = -1;
  Int_t icjet1      = -1; // central jet that is not the same as leading b jet for dphi_ll_bj
  Float_t ht        =  0; // total scalar energy HT
  
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Other_common_selections
  for( int ijet = 0; ijet < (int)Jet.size(); ++ijet ){
    ht += Jet.at(ijet).e();
    bool isBTagged = getBTagWeight_promote_demote(Jet.at(ijet)); // (Jet.at(ijet).csv()) > 0.8 //csv > 0.8 is medium
    if(Jet.at(ijet).pt() > 30) njets++;
    if(fabs(Jet.at(ijet).eta()) < 2.4 && isBTagged){
      nbtag++;
      if      (ibjet1 < 0) ibjet1 = ijet;
      else if (ibjet2 < 0) ibjet2 = ijet;
    }
    if(fabs(Jet.at(ijet).eta()) < 2.4){         // CENTRAL 20 GeV
      if(isBTagged) ncbtag20++;                 //  btag
      ncjets20++;                               //  jets
      if(icjet1 < 0 && (icjet1 != ibjet1 || ibjet1 < 0 )) icjet1 = ijet;
      if(Jet.at(ijet).pt() > 30){               // CENTRAL 30 GeV
        if(isBTagged) ncbtag++;                 //  btag
        ncjets++;                               //  jets
    }}
    else if(fabs(Jet.at(ijet).eta()) > 2.4){    // FORWARD 20 GeV
      if(isBTagged) nfbtag20++;                 //  btag
      nfjets20++;                               //  jets
      if(Jet.at(ijet).pt() > 30){               // FORWARD 30 GeV
        if(isBTagged) nfbtag++;                 //  btag
        nfjets++;                               //  jets
    }}
  }
  njets20 = ncjets20 + nfjets20;
  nbtag20 = ncbtag20 + nfbtag20;
  njets = ncjets + nfjets;
  nbtag = ncbtag + nfbtag;
  
  if(njets20 > 1){
    b_jpt_1[ch]     = Jet.at(0).pt();
    b_jeta_1[ch]    = Jet.at(0).eta();
    b_jphi_1[ch]    = Jet.at(0).phi();
    b_jpt_2[ch]     = Jet.at(1).pt();
    b_jeta_2[ch]    = Jet.at(1).eta();
    b_jphi_2[ch]    = Jet.at(1).phi();    
  }
  else if(njets20 == 1){
    b_jpt_1[ch]     = Jet.at(0).pt();
    b_jeta_1[ch]    = Jet.at(0).eta();
    b_jphi_1[ch]    = Jet.at(0).phi();
    b_jpt_2[ch]     = -1;
    b_jeta_2[ch]    = -9;
    b_jphi_2[ch]    = -9;
  }
  else{
    b_jpt_1[ch]     = -1;
    b_jeta_1[ch]    = -9;
    b_jphi_1[ch]    = -9;
    b_jpt_2[ch]     = -1;
    b_jeta_2[ch]    = -9;
    b_jphi_2[ch]    = -9;
  }

  // VBF
  if(njets>=2){
    b_vbf_mjj[ch]   = (Jet.at(0).tlv() + Jet.at(1).tlv()).M();
    b_vbf_deta[ch]  = Jet.at(0).eta() - Jet.at(1).eta();
    b_vbf_jdphi[ch] = deltaPhi(Jet.at(0).phi(), Jet.at(1).phi());
    Float_t min_eta = Jet.at(0).eta();
    Float_t max_eta = Jet.at(1).eta();
    if(min_eta > max_eta){
      min_eta = Jet.at(1).eta(); 
      max_eta = Jet.at(0).eta(); 
    }
    int ncentral    = 0;
    int ncentral20  = 0;
    for( int ijet = 0; ijet < (int)Jet.size(); ++ijet ){
      Float_t jeteta = Jet.at(ijet).eta();
      Float_t jetpt  = Jet.at(ijet).pt();
      if(min_eta < jeteta && jeteta < max_eta){
	    if(jetpt > 30.) ncentral++;
	    if(jetpt > 20.) ncentral20++;
    }}
    b_vbf_ncentral[ch]   = ncentral;
    b_vbf_ncentral20[ch] = ncentral20;
  }else{
    b_vbf_mjj[ch]   = -99;
    b_vbf_deta[ch]  = -99;
    b_vbf_jdphi[ch] = -99;
    b_vbf_ncentral[ch]   = -99;
    b_vbf_ncentral20[ch] = -99;
  }
  
  if(ibjet1 < 0){
    b_bpt_1[ch]     = -1;
    b_beta_1[ch]    = -9;
    b_bphi_1[ch]    = -9;
    b_bcsv_1[ch]    = -1;
  }else{
    b_bpt_1[ch]     = Jet.at(ibjet1).pt();
    b_beta_1[ch]    = Jet.at(ibjet1).eta();
    b_bphi_1[ch]    = Jet.at(ibjet1).phi();
    b_bcsv_1[ch]    = Jet.at(ibjet1).csv();
  }
  if (ibjet2 < 0){
    b_bpt_2[ch]     = -1;
    b_beta_2[ch]    = -9;
    b_bphi_2[ch]    = -9;
    b_bcsv_2[ch]    = -1;
  }
  else{
    b_bpt_2[ch]     = Jet.at(ibjet2).pt();
    b_beta_2[ch]    = Jet.at(ibjet2).eta();
    b_bphi_2[ch]    = Jet.at(ibjet2).phi();
    b_bcsv_2[ch]    = Jet.at(ibjet2).csv();
  }
  
  b_njets[ch]       = njets;
  b_nfjets[ch]      = nfjets;
  b_ncjets[ch]      = ncjets;
  b_nbtag[ch]       = nbtag;
  b_nfbtag[ch]      = nfbtag;
  b_ncbtag[ch]      = ncbtag;
  b_njets20[ch]     = njets20;
  b_nfjets20[ch]    = nfjets20;
  b_ncjets20[ch]    = ncjets20;
  b_nbtag20[ch]     = nbtag20;
  b_nfbtag20[ch]    = nfbtag20;
  b_ncbtag20[ch]    = ncbtag20;
  
  
  ////////////////
  // MARK: Taus //
  ////////////////
  
  b_pt_2[ch]        = tau.tlv().Pt();
  b_eta_2[ch]       = tau.tlv().Eta();
  b_phi_2[ch]       = tau.tlv().Phi();
  b_m_2[ch]         = tau.tlv().M();
  b_q_2[ch]         = tau.charge();
  b_d0_2[ch]        = tau.d0();
  b_dz_2[ch]        = tau.dz();
  b_iso_2[ch]       = tau.byTightIsolationMVArun2v1DBoldDMwLT();
  b_iso_2_medium[ch] = tau.byMediumIsolationMVArun2v1DBoldDMwLT();
  
  b_pol_2[ch]       = -9;
  if (tau.chargedPionPt() > 0 && tau.neutralPionPt() > 0)
    b_pol_2[ch]     = (tau.chargedPionPt() - tau.neutralPionPt()) / (tau.chargedPionPt() + tau.neutralPionPt());
  
  b_againstElectronVLooseMVA6_2[ch]     = tau.againstElectronVLooseMVA6();
  b_againstElectronLooseMVA6_2[ch]      = tau.againstElectronLooseMVA6();
  b_againstElectronMediumMVA6_2[ch]     = tau.againstElectronMediumMVA6();
  b_againstElectronTightMVA6_2[ch]      = tau.againstElectronTightMVA6();
  b_againstElectronVTightMVA6_2[ch]     = tau.againstElectronVTightMVA6();
  b_againstMuonLoose3_2[ch]             = tau.againstMuonLoose3();
  b_againstMuonTight3_2[ch]             = tau.againstMuonTight3();
  b_byCombinedIsolationDeltaBetaCorrRaw3Hits_2[ch] = tau.byCombinedIsolationDeltaBetaCorrRaw3Hits();
  b_byIsolationMVA3newDMwLTraw_2[ch]    = tau.byIsolationMVArun2v1DBnewDMwLTraw();
  b_byIsolationMVA3oldDMwLTraw_2[ch]    = tau.byIsolationMVArun2v1DBoldDMwLTraw();
  b_chargedIsoPtSum_2[ch]               = tau.chargedIsoPtSum();
  b_neutralIsoPtSum_2[ch]               = tau.neutralIsoPtSum();
  b_puCorrPtSum_2[ch]                   = tau.puCorrPtSum();
  b_decayModeFindingOldDMs_2[ch]        = tau.decayModeFinding();
  b_decayMode_2[ch]                     = tau.decayMode();
  
  b_id_e_mva_nt_loose_1[ch]             = -1;
  b_id_e_mva_nt_loose_1_old[ch]         = -1;
  extraLeptonVetos(channel, muon, electron);
  b_dilepton_veto[ch]                   = (int) b_dilepton_veto_;
  b_extraelec_veto[ch]                  = (int) b_extraelec_veto_;
  b_extramuon_veto[ch]                  = (int) b_extramuon_veto_;
  b_lepton_vetos[ch]                    = ( b_dilepton_veto_ || b_extraelec_veto_ || b_extramuon_veto_ );
  
  
  ///////////////////
  // MARK: Leptons //
  ///////////////////
  
  b_idisoweight_1[ch]                   = 1.;
  b_trigweight_1[ch]                    = 1.;
  
  TLorentzVector lep_tlv;
  if(channel=="mutau"){
    b_pt_1[ch]              = muon.tlv().Pt();
    b_eta_1[ch]             = muon.tlv().Eta();
    b_phi_1[ch]             = muon.tlv().Phi();
    b_m_1[ch]               = muon.tlv().M();
    b_q_1[ch]               = muon.charge();
    b_d0_1[ch]              = muon.d0();
    b_dz_1[ch]              = muon.dz();
    b_iso_1[ch]             = muon.SemileptonicPFIso() / muon.pt();
    b_iso_cuts[ch]          = ( b_iso_1[ch] < 0.15 && b_iso_2[ch] == 1 )
    b_channel[ch]           = 1;
    b_lepton_vetos[ch]      = ( b_lepton_vetos[ch] || tau.againstElectronVLooseMVA6() < 0.5 || tau.againstMuonTight3() < 0.5 );
    lep_tlv.SetPtEtaPhiM(b_pt_1[ch], b_eta_1[ch], b_phi_1[ch], b_m_1[ch]);
    if (!m_isData){
      b_trigweight_1[ch]    = m_ScaleFactorTool.get_Efficiency_MuTrig(lep_tlv.Pt(),fabs(lep_tlv.Eta()));
      b_idisoweight_1[ch]   = m_ScaleFactorTool.get_ScaleFactor_MuIdIso(lep_tlv.Pt(),fabs(lep_tlv.Eta()));
    }
  }
  else{
    b_pt_1[ch]              = electron.tlv().Pt();
    b_eta_1[ch]             = electron.tlv().Eta();
    b_phi_1[ch]             = electron.tlv().Phi();
    b_m_1[ch]               = electron.tlv().M();
    b_q_1[ch]               = electron.charge();
    b_d0_1[ch]              = electron.d0();
    b_dz_1[ch]              = electron.dz();
    b_iso_1[ch]             = electron.SemileptonicPFIso() / electron.pt();
    b_iso_cuts[ch]          = ( b_iso_1[ch] < 0.10 && b_iso_2[ch] == 1 )
    //b_id_e_mva_nt_loose_1[ch]     = electron.isMVATightElectron(); // Moriond
    //b_id_e_mva_nt_loose_1_old[ch] = isNonTrigElectronID(electron); // Moriond - 90% efficiency working point
    b_id_e_mva_nt_loose_1[ch]     = isNonTrigElectronID(electron); // ICHEP - 90% efficiency working point
    b_id_e_mva_nt_loose_1_old[ch] = electron.nonTrigMVAID();       // ICHEP
    b_channel[ch]           = 2;
    b_lepton_vetos[ch]      = ( b_lepton_vetos[ch] || tau.againstElectronTightMVA6() < 0.5 || tau.againstMuonLoose3() < 0.5 );
    lep_tlv.SetPtEtaPhiM(b_pt_1[ch], b_eta_1[ch], b_phi_1[ch], b_m_1[ch]);
    if (!m_isData){
      b_trigweight_1[ch]    = m_ScaleFactorTool.get_Efficiency_EleTrig(lep_tlv.Pt(),fabs(lep_tlv.Eta()));
      b_idisoweight_1[ch]   = m_ScaleFactorTool.get_ScaleFactor_EleIdIso(lep_tlv.Pt(),fabs(lep_tlv.Eta()));
    }
  }
  
  
  ///////////////////////
  // MARK: Reweighting //
  ///////////////////////
  
  b_idisoweight_2[ch]                   = 1.;
  b_trigweight_2[ch]                    = 1.;
  b_zptweight[ch]                       = 1.;
  b_ttptweight[ch]                      = 1.;
  b_weightbtag[ch]                      = 1.;
  b_gen_match_1[ch]                     = -1;
  b_gen_match_2[ch]                     = gen_match_2;
  if (m_isData) b_gen_match_1[ch]       = -1;
  else{
    b_gen_match_1[ch]                   = genMatch(b_eta_1[ch], b_phi_1[ch]);
    b_idisoweight_2[ch]                 = genMatchSF(channel, gen_match_2, b_eta_2[ch]); // leptons faking taus and real taus ID eff
    if(m_doZpt)  b_zptweight[ch]        = m_RecoilCorrector.ZptWeight( boson_tlv.M(), boson_tlv.Pt() );
    if(m_doTTpt) b_ttptweight[ch]       = genMatchSF(channel, -36); // 6*-6 = -36
    b_weightbtag[ch]                    = b_weightbtag_; // do not apply b tag weight when using promote-demote method !!!
    //b_weightbtag[ch]                  = m_BTaggingScaleTool.getScaleFactor_veto(Jet); // getScaleFactor_veto for AK4, getScaleFactor for AK8
    b_weight[ch] *= b_trigweight_1[ch] * b_idisoweight_1[ch] * b_trigweight_2[ch] * b_idisoweight_2[ch] * b_zptweight[ch] * b_ttptweight[ch]; // * b_weightbtag[ch]
    // check boosted tau ID matching standard ID
    // if (b_gen_match_2[ch] == 5 && m_isSignal){
    //   int nMatch = 0;
    //   for( int i = 0; i < (m_tau.N); ++i ){
    //     UZH::Tau mytau( &m_tau, i );
    //     if(mytau.TauType()==1) if(tau.tlv().DeltaR(mytau.tlv()) < 0.3) nMatch++;
    //   }
    //   TString tch = ch; 
    //   Hist("N_match0p30_bst_std_"+tch, "histogram_"+tch)->Fill( nMatch );
    // }
  }
  
  
  
  //////////////////////////////
  // MARK: Recoil corrections //
  //////////////////////////////
  //std::cout << ">>> Recoil corrections " << std::endl;
  
  TLorentzVector met_tlv;
  //TLorentzVector mvamet_tlv;
  float fmet      = met.et();        float fmetphi      = met.phi();
  //float fmvamet   = mvamet.et();     float fmvametphi   = mvamet.phi();
  float fpuppimet = puppimet.et();   float fpuppimetphi = puppimet.phi();
  met_tlv.SetPxPyPzE(fmet*TMath::Cos(fmetphi), fmet*TMath::Sin(fmetphi), 0, fmet);
  //mvamet_tlv.SetPxPyPzE(fmvamet*TMath::Cos(fmvametphi), fmvamet*TMath::Sin(fmvametphi), 0, fmvamet);
  TLorentzVector met_tlv_corrected;
  //TLorentzVector mvamet_tlv_corrected;
  if(m_doRecoilCorr){
    met_tlv_corrected    = m_RecoilCorrector.CorrectPFMETByMeanResolution(  met_tlv.Px(),         met_tlv.Py(),
					                                                        boson_tlv.Px(),     boson_tlv.Py(),
					                                                        boson_tlv_vis.Px(), boson_tlv_vis.Py(),
					                                                        m_jetAK4.N ); //m_eventInfo.lheNj
    // mvamet_tlv_corrected = m_RecoilCorrector.CorrectMVAMETByMeanResolution( mvamet_tlv.Px(),   mvamet_tlv.Py(),
    // 					                                                    boson_tlv.Px(),     boson_tlv.Py(),
	// 				                                                        boson_tlv_vis.Px(), boson_tlv_vis.Py(),
	// 				                                                        m_jetAK4.N ); //m_eventInfo.lheNj
    fmet    = met_tlv_corrected.E();         fmetphi = met_tlv_corrected.Phi();
    //fmvamet = mvamet_tlv_corrected.E();   fmvametphi = mvamet_tlv_corrected.Phi();
    b_m_genboson[ch]  = boson_tlv.M();
    b_pt_genboson[ch] = boson_tlv.Pt();
  }else{
    met_tlv_corrected    = met_tlv;
    //mvamet_tlv_corrected = mvamet_tlv;
  }
  //if( fmvamet < 1e-10 ){
  //  std::cout << ">>> Warning! Set low valued fmvamet = " << fmvamet << " to 0" << std::endl;
  //  fmvamet = 0.0;
  //}
  
  
  //////////////////
  // MARK: Shifts //
  //////////////////
  // apply shifts to tau_tlv_shifted, lep_tlv_shifted, met_tlv_corrected
  //std::cout << ">>> Shifts " << std::endl;
  
  TLorentzVector tau_tlv; //_shifted
  tau_tlv.SetPtEtaPhiM(b_pt_2[ch], b_eta_2[ch], b_phi_2[ch], b_m_2[ch]);
  //TLorentzVector lep_tlv_shifted;
  //lep_tlv_shifted.SetPtEtaPhiM(b_pt_1[ch], b_eta_1[ch], b_phi_1[ch], b_m_1[ch]);
  
  if(!m_isData){
    //std::cout << ">>> before: tau pt = " << tau_tlv.Pt()  << ", m   = " << tau_tlv.M() << std::endl;
    //std::cout << ">>> before: met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    if(m_doTES && gen_match_2==5){ // TES
      // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016#Tau_Energy_Scale_TES
      shiftLeptonAndMET(m_TESshift,tau_tlv,met_tlv_corrected,true); // shiftEnergy = true
      b_pt_2[ch]    = tau_tlv.Pt();
      b_m_2[ch]     = tau_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
      //std::cout << ">>> after:  tau pt = " << tau_tlv.Pt()  << ", m   = " << tau_tlv.M() << std::endl;
      //std::cout << ">>> after:  met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    }
    if(m_doLTF && gen_match_2<5){ // Lepton to tau fake (LTF)
      // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016#Electron_to_Tau_Fake
      shiftLeptonAndMET(m_LTFshift,tau_tlv,met_tlv_corrected);
      b_pt_2[ch]    = tau_tlv.Pt();
      b_m_2[ch]     = tau_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
      //std::cout << ">>> after:  tau pt = " << tau_tlv.Pt()  << ", m   = " << tau_tlv.M() << std::endl;
      //std::cout << ">>> after:  met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    }
    if(m_doEES && channel=="eletau"){ // Electron Energy Scale
      //std::cout << ">>> before: lep pt = " << lep_tlv.Pt()  << ", m   = " << lep_tlv.M() << std::endl;
      if(fabs(electron.tlv().Eta())<1.479) shiftLeptonAndMET(m_EESshift,      lep_tlv,met_tlv_corrected,true);
      else                                 shiftLeptonAndMET(m_EESshiftEndCap,lep_tlv,met_tlv_corrected,true);
      b_pt_1[ch]    = lep_tlv.Pt();
      b_m_1[ch]     = lep_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
      //std::cout << ">>> after:  lep pt = " << lep_tlv.Pt()  << ", m   = " << lep_tlv.M() << std::endl;      
      //std::cout << ">>> after:  met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    }
    //std::cout << ">>> " << std::endl;
  }
  
  b_met[ch]         = fmet;
  b_metphi[ch]      = fmetphi;
  b_puppimet[ch]    = fpuppimet;
  b_puppimetphi[ch] = fpuppimetphi;
  //b_mvamet[ch]      = fmvamet;
  //b_mvametphi[ch]   = fmvametphi;
  b_met_old[ch]     = met.et();
  //b_mvamet_old[ch]  = mvamet.et();
  
  b_metcov00[ch]    = met.cov00();
  b_metcov01[ch]    = met.cov10(); // not a typo. This is same for 10
  b_metcov10[ch]    = met.cov10();
  b_metcov11[ch]    = met.cov11();
  //b_mvacov00[ch]    = mvamet.cov00();
  //b_mvacov01[ch]    = mvamet.cov10(); // not a typo. This is same for 10
  //b_mvacov10[ch]    = mvamet.cov10();
  //b_mvacov11[ch]    = mvamet.cov11();
  
  //b_mt_1[ch]        = TMath::Sqrt(2*lep_tlv.Pt()*fmvamet*(   1-TMath::Cos(deltaPhi(lep_tlv.Phi(), fmvametphi  ))));
  b_pfmt_1[ch]      = TMath::Sqrt(2*lep_tlv.Pt()*fmet*(      1-TMath::Cos(deltaPhi(lep_tlv.Phi(), fmetphi     ))));
  b_puppimt_1[ch]   = TMath::Sqrt(2*lep_tlv.Pt()*fpuppimet*( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(), fpuppimetphi))));
  
  //b_mt_2[ch]        = TMath::Sqrt(2*b_pt_2[ch]*fmvamet*(   1-TMath::Cos(deltaPhi(b_phi_2[ch], fmvametphi   ))));
  b_pfmt_2[ch]      = TMath::Sqrt(2*b_pt_2[ch]*fmet*(      1-TMath::Cos(deltaPhi(b_phi_2[ch], fmetphi      ))));
  b_puppimt_2[ch]   = TMath::Sqrt(2*b_pt_2[ch]*fpuppimet*( 1-TMath::Cos(deltaPhi(b_phi_2[ch], fpuppimetphi ))));
  
  b_m_vis[ch]       = (lep_tlv + tau_tlv).M();
  b_pt_tt[ch]       = (lep_tlv + tau_tlv + met_tlv_corrected).Pt();
  b_pt_tt_vis[ch]   = (lep_tlv + tau_tlv).Pt();
  b_R_pt_m_vis[ch]  = -1;
  if(b_m_vis[ch] > 0){
    b_R_pt_m_vis[ch] = b_pt_tt[ch]/b_m_vis[ch];
    b_R_pt_m_vis2[ch] = b_pt_tt_vis[ch]/b_m_vis[ch];
  }
  
  b_dR_ll[ch]       = tau_tlv.DeltaR(lep_tlv);
  b_dR_ll_gen[ch]   = b_dR_ll_gen_;
  b_mt_tot[ch]      = TMath::Sqrt(TMath::Power(b_pfmt_1[ch],2) + TMath::Power(b_pfmt_2[ch],2) + 2*lep_tlv.Pt()*b_pt_2[ch]*(1-TMath::Cos(deltaPhi(lep_tlv.Phi(), b_phi_2[ch]))));
  b_ht[ch]          = ht + lep_tlv.E() + tau_tlv.E();
  
  // Delta phi( lep+tau, bj+j ) if there is one central b jet and on central jet
  // icjet1 = index of central jet that is not the same as leading b jet
  if(icjet1 != -1 && ibjet1 != -1)
    b_dphi_ll_bj[ch] = fabs(deltaPhi( (lep_tlv+tau_tlv).Phi(), (Jet.at(ibjet1).tlv()+Jet.at(icjet1).tlv()).Phi() ));
  else
    b_dphi_ll_bj[ch] = -1;
  
  TVector3 leg1(lep_tlv.Px(), lep_tlv.Py(), 0.);
  TVector3 leg2(tau_tlv.Px(), tau_tlv.Py(), 0.);
  TVector3 metleg(met_tlv_corrected.Px(), met_tlv_corrected.Py(), 0.);
  TVector3 zetaAxis = (leg1.Unit() + leg2.Unit()).Unit();
  Float_t pZetaVis_ = leg1*zetaAxis + leg2*zetaAxis;
  Float_t pZetaMET_ = metleg*zetaAxis;
  b_pzetamiss[ch]   = pZetaMET_;
  b_pzetavis[ch]    = pZetaVis_;
  b_pzeta_disc[ch]  = pZetaMET_ - 0.5*pZetaVis_;
  
  
  //////////////////
  // MARK: SVFit  //
  //////////////////
  //std::cout << ">>> SVFit" << std::endl;
  // apply some extra cuts to save time
  bool doSVFit = m_doSVFit && b_iso_1[ch]<0.30 && b_iso_2_medium[ch]==1 && b_lepton_vetos[ch]==0;
  if(m_doEES || m_doTES || m_doLTF) doSVFit = doSVFit && ncbtag>0 && b_iso_1[ch]<0.15 && b_iso_2[ch]==1;
  //bool doSVfit= false;
  
  double m_sv = -1;
  double pt_tt_sv = -1;
  double R_pt_m_sv = -1;
  if ( doSVFit ){
    //std::cout << ">>> SVFit" << std::endl;
    // TODO: return TLV
    m_SVFitTool.addMeasuredLeptonTau(channel,lep_tlv, tau_tlv, tau.decayMode());
    m_SVFitTool.getSVFitMassAndPT(m_sv,pt_tt_sv,met_tlv_corrected.Px(),met_tlv_corrected.Py(), met.cov00(),met.cov10(),met.cov11());
    if(m_sv > 0) R_pt_m_sv = pt_tt_sv/m_sv;
  }
  b_m_sv[ch] = m_sv;
  b_pt_tt_sv[ch] = pt_tt_sv;
  b_R_pt_m_sv[ch] = R_pt_m_sv;
  
}




void TauTauAnalysis::genFilterZtautau(){
//   std::cout << "genFilterZtautau" << std::endl;
    
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    
    if( fabs(mygoodGenPart.pdgId()) == 15 ){
      if( mygoodGenPart.mother()[0]==25 ){ GenEvent_Htata_filter = true; }
      if( mygoodGenPart.mother()[0]==23 ){ GenEvent_Ztata_filter = true; }
    } 
  }
}





void TauTauAnalysis::setGenBosonTLVs(){
//   std::cout << "recoilCorrection" << std::endl;
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Computation_of_generator_Z_W_Hig
// TODO: check case of more than one boson
  
  boson_tlv     = TLorentzVector();
  boson_tlv_vis = TLorentzVector();
  
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    float pdg = fabs(mygoodGenPart.pdgId());
    bool isNeutrino = (pdg == 12 || pdg == 14 || pdg == 16);
    
    if( (mygoodGenPart.fromHardProcessFinalState() && (pdg == 11 || pdg == 13 || isNeutrino)) ||
        mygoodGenPart.isDirectHardProcessTauDecayProductFinalState() ){
      boson_tlv += mygoodGenPart.tlv();
      if(!isNeutrino)
        boson_tlv_vis += mygoodGenPart.tlv();
    }
  }
}





int TauTauAnalysis::genMatch(Float_t lep_eta, Float_t lep_phi) {
  //std::cout << "cutflowCheck" << std::endl;
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_Matching
//  1: prompt electron
//  2: prompt muon
//  3: tau -> e
//  4. tau -> mu
//  5: tau -> hadr.
//  6: fake jet / PU
  
  Float_t min_dR = 1000;
  int id = 6;
  
  // check for lepton matching, first
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    
    Float_t pt      = mygoodGenPart.pt();
    Float_t eta     = mygoodGenPart.eta();
    Float_t phi     = mygoodGenPart.phi();
    Int_t pdgId     = abs(mygoodGenPart.pdgId());
    Int_t isPrompt  = mygoodGenPart.isPrompt();
    Int_t isDirectPromptTauDecayProduct = mygoodGenPart.isDirectPromptTauDecayProduct();
    
    if(mygoodGenPart.status()!=1) continue;
    if( !((pdgId==11 || pdgId==13) && (isPrompt > 0.5 || isDirectPromptTauDecayProduct > 0.5) && pt > 8) ) continue;
    
    Float_t dr = deltaR(lep_eta-eta, deltaPhi(lep_phi, phi));
    if(dr < min_dR){
      min_dR = dr;
      if(pdgId==11 && isPrompt > 0.5) id = 1;
      if(pdgId==13 && isPrompt > 0.5) id = 2;
      if(pdgId==11 && isDirectPromptTauDecayProduct > 0.5) id = 3;
      if(pdgId==13 && isDirectPromptTauDecayProduct > 0.5) id = 4;      
    }
  }
  
  // Retrieve visible pT of the taus ! 
  // Should be done in Ntuplizer level from next time.
  std::map<int, TLorentzVector> gennus;
  std::map<int, TLorentzVector> gentaus;
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    
    Float_t pt = mygoodGenPart.pt();
    Float_t eta = mygoodGenPart.eta();
    Float_t phi = mygoodGenPart.phi();
    Float_t energy = mygoodGenPart.e();
    Int_t pdgId = mygoodGenPart.pdgId();
    Int_t abspdgId = abs(mygoodGenPart.pdgId());
    Int_t isPrompt = mygoodGenPart.isPrompt();

    Int_t mother = -999;
    if(mygoodGenPart.nMoth() !=0){
      mother = abs(mygoodGenPart.mother()[0]);
    }

    // save gen tau neutrino
    if(mygoodGenPart.status()==1 && abspdgId==16 && mother==15){
      TLorentzVector genNeutrino;
      genNeutrino.SetPtEtaPhiE(pt,eta,phi,energy);
      gennus[pdgId] = genNeutrino;
      //std::cout << "Neutrino : " << pdgId << " " << genNeutrino.Pt() << std::endl;
    }

    // skip if not tau
    if(!(mygoodGenPart.status()==2 && abspdgId==15 && isPrompt > 0.5)) continue;

    bool isleptonic = false;
    for(int daughter=0; daughter < (int)mygoodGenPart.nDau(); daughter++){
      //std::cout << "\t" << "parent " << pdgId << "(pt = " << pt << ") daughter : " << mygoodGenPart.dau()[daughter] << std::endl;
      Int_t daughter_pdgId = abs(mygoodGenPart.dau()[daughter]);
      if(daughter_pdgId==11 || daughter_pdgId==13) isleptonic = true;
      if(daughter_pdgId==15){
        std::cout << "Tau decays into taus !!!" << std::endl;
        isleptonic = true;
      }
    }

    if(isleptonic==false){
      TLorentzVector genPt;
      genPt.SetPtEtaPhiE(pt,eta,phi,energy);
      gentaus[pdgId] = genPt;
    }
  }
  
  
  // if tau decays hadronically: loop over gentaus, gennus
  // substract gennu pt from gentau pt
  for(std::map<int, TLorentzVector>::iterator it = gentaus.begin(); it!=gentaus.end(); ++it){
    Int_t pdg = (*it).first;
    for(std::map<int, TLorentzVector>::iterator itn = gennus.begin(); itn!=gennus.end(); ++itn){
      Int_t nu = (*itn).first;
      if(pdg==15){
        if(nu==16) (*it).second -= (*itn).second;
      }else if(pdg==-15){
        if(nu==-16) (*it).second -= (*itn).second;
      }else{
	  std::cout << "Impossible !!!" << std::endl;
      }
    }
  }
  
  
  // match lepton gentaus
  for(std::map<int, TLorentzVector>::iterator it = gentaus.begin(); it!=gentaus.end(); ++it){
    //    Int_t pdg = (*it).first;
    Float_t dr = deltaR(lep_eta - (*it).second.Eta(), 
			            deltaPhi(lep_phi, (*it).second.Phi()));
    if(dr < min_dR){
      min_dR = dr;
      id = 5;
    }
    //std::cout << "Last Tau = " << pdg << " " << (*it).second.Pt() << std::endl;
  }

  if(min_dR > 0.2) id = 6;
  
  return id;

}





Float_t TauTauAnalysis::deltaPhi(Float_t p1, Float_t p2){
//std::cout << "deltaPhi" << std::endl;

  Float_t res = p1 - p2;
  while(res > TMath::Pi()){
    res -= 2*TMath::Pi();
  }
  while(res < -TMath::Pi()){
    res += 2*TMath::Pi();
  }
  
  return res;
}





Float_t TauTauAnalysis::deltaR(Float_t deta, Float_t dphi){
//   std::cout << "deltaR" << std::endl;
  return TMath::Sqrt(TMath::Power(deta,2) + TMath::Power(dphi,2));
}





bool TauTauAnalysis::isNonTrigElectronID(const UZH::Electron& electron)
{
//std::cout << "isNonTrigElectronID" << std::endl;
// 90% efficiency working point
// https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentificationRun2#Non_triggering_electron_MVA_deta
// https://github.com/gitytakahas/EXOVVNtuplizerRunII/blob/80X_ntuplizer/Ntuplizer/plugins/ElectronsNtuplizer.cc#L66-L98
  Float_t eta = fabs(electron.superCluster_eta());
  Float_t pt  = electron.pt();
  //Float_t mva = electron.isMVATightElectron(); // Moriond
  Float_t mva = electron.nonTrigMVAID(); // ICHEP
  
  // assume pt > 5.0 GeV
  if(pt <= 10.){
    if(eta < 0.8)           return mva > -0.083313;
    else if(eta < 1.479)    return mva > -0.235222;
    else                    return mva > -0.67099;
  }
  else if(pt > 10.){
    if(eta < 0.8)           return mva > 0.913286;
    else if(eta < 1.479)    return mva > 0.805013;
    else                    return mva > 0.358969;
  }
  else{
    std::cout << ">>> Does not happen" << std::endl;
    return false;
  } 
}





bool TauTauAnalysis::LooseJetID(const UZH::Jet& jet)
{
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data
  Float_t eta = fabs(jet.eta());
  Float_t NHF  = jet.nhf();  //neutralHadronEnergyFraction();
  Float_t NEMF = jet.nemf(); //neutralEmEnergyFraction();
  Float_t NM   = jet.nm();   //neutralMultiplicity();
  Float_t CM   = jet.cm();   //chargedMultiplicity();

  if(eta <= 2.4){      // eta < 2.4
    Float_t CHF  = jet.chf();  //chargedHadronEnergyFraction();
    Float_t CEMF = jet.cemf(); //chargedEmEnergyFraction();
    return NHF < 0.99 && NEMF < 0.99 && NM+CM > 1 &&
           CHF > 0    && CEMF < 0.99 &&    CM > 0;
  }
  else if(eta <= 2.7){ // eta < 2.7  
    return NHF < 0.99 && NEMF < 0.99 && NM+CM > 1;
  }
  else if(eta <= 3.0){ // eta < 3.0  
    return NEMF < 0.90 && NM > 2;
  }
  else if(eta  < 4.7){ // eta < 4.7 = m_AK4jetEtaCut  
    return NEMF < 0.90 && NM > 10;
  } 
  return false;
}





float TauTauAnalysis::genMatchSF(const std::string& channel, const int genmatch_2, const float tau_eta){
  //std::cout << "genMatchSF" << std::endl;
  // matching ID code:      https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_Matching
  // tau reweighting:       old: https://indico.cern.ch/event/563239/contributions/2279020/attachments/1325496/1989607/lepTauFR_tauIDmeeting_20160822.pdf
  //                        new: https://indico.cern.ch/event/566825/contributions/2398691/attachments/1385164/2107478/HIG-16-043-preapproval-rehearsal.pdf#page=14
  // top pt reweighting:    https://twiki.cern.ch/twiki/bin/view/CMS/MSSMAHTauTauEarlyRun2#Top_quark_pT_reweighting
  
  float eta = fabs(tau_eta);
  
  // electron -> tau
  if      (genmatch_2 == 3) {
    if (channel=="mutau"){       // for VLoose
        if      ( eta < 1.460 ) return 1.317;
        else if ( eta > 1.558 ) return 1.547;
    }
    else if (channel=="eletau"){ // for Tight
        if      ( eta < 1.460 ) return 1.486;
        else if ( eta > 1.558 ) return 1.560;
    }
  }
  // muon -> tau        for Tight
  else if (genmatch_2 == 4) {
    if (channel=="mutau"){       // for Tight
        if      ( eta < 0.4 ) return 1.470;
        else if ( eta < 0.8 ) return 1.367;
        else if ( eta < 1.2 ) return 1.251;
        else if ( eta < 1.7 ) return 1.770;
        else                  return 1.713;
    }
    else if (channel=="eletau"){ // for Loose
        if      ( eta < 0.4 ) return 1.146;
        else if ( eta < 0.8 ) return 1.084;
        else if ( eta < 1.2 ) return 1.218;
        else if ( eta < 1.7 ) return 1.490;
        else                  return 2.008;
    }
  }
  // real tau
  else if (genmatch_2 == 5) {
    return 0.90;
  }
  // real top
  else if (genmatch_2 == -36) {
    double pt_top_1 = 0;
    double pt_top_2 = 0;
    int qq = 0;
    for ( int p = 0; p < (m_genParticle.N); ++p ) {
      UZH::GenParticle top( &m_genParticle, p );
      if( abs(top.pdgId()) == 6 ){
        if(qq==0) { pt_top_1 = top.pt(); qq = top.pdgId(); }
        else if(qq*top.pdgId()<0) { pt_top_2 = top.pt(); qq*=top.pdgId(); break; }
      }
    }
    if(qq==-36)
      return TMath::Sqrt(TMath::Exp(0.156-0.00137*TMath::Min(pt_top_1,400.0))*TMath::Exp(0.156-0.00137*TMath::Min(pt_top_2,400.0)));
    else
      std::cout << ">>> TauTauAnalysis::genMatchSF: genmatch_2 = 66, qq = " << qq << " != -36 !!!" << std::endl;
  }
  
  return 1.0;
}




void TauTauAnalysis::shiftLeptonAndMET(const float shift, TLorentzVector& lep_shifted, TLorentzVector& met_shifted, bool shiftEnergy){
  //std::cout << "shiftLeptonAndMET" << std::endl;
  
  //std::cout << ">>> after:  lep_shifted pt = " << lep_shifted.Pt()  << ", m   = " << lep_shifted.M() << std::endl;
  TLorentzVector Delta_lep_tlv(lep_shifted.Px()*shift, lep_shifted.Py()*shift, 0, 0); // (dpx,dpy,0,0)
  if(shiftEnergy) lep_shifted.SetPtEtaPhiM((1.+shift)*lep_shifted.Pt(),lep_shifted.Eta(),lep_shifted.Phi(),(1.+shift)*lep_shifted.M());
  else            lep_shifted.SetPtEtaPhiM((1.+shift)*lep_shifted.Pt(),lep_shifted.Eta(),lep_shifted.Phi(),           lep_shifted.M());
  TLorentzVector met_diff;
  met_diff.SetPtEtaPhiM(met_shifted.Pt(),met_shifted.Eta(),met_shifted.Phi(),0.); // MET(px,dpy,0,0) - (dpx,dpy,0,0)
  met_diff -= Delta_lep_tlv;
  met_shifted.SetPtEtaPhiM(met_diff.Pt(),met_diff.Eta(),met_diff.Phi(),0.); // keep E = |p| !
  //std::cout << ">>> after:  lep_shifted pt = " << lep_shifted.Pt()  << ", m   = " << lep_shifted.M() << ", shift = " << shift << std::endl;
  
}




void TauTauAnalysis::extraLeptonVetos(const std::string& channel, const UZH::Muon& muon, const UZH::Electron& electron){
  //std::cout << "extraLeptonVetos" << std::endl;
  
  b_dilepton_veto_  = false;
  b_extraelec_veto_ = false;
  b_extramuon_veto_ = false;
  
  // extra leptons
  // https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2016#Baseline_mu_tau_h
  // https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2016#Baseline_e_tau_h
  // https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2016#Third_lepton_vetoes
  
  std::vector<UZH::Muon> passedMuons;
  for( int i = 0; i < m_muon.N; ++i ){
    UZH::Muon mymuon( &m_muon, i );  
    
    if(mymuon.pt() < 10) continue;
    if(fabs(mymuon.eta()) > 2.4) continue;
    if(fabs(mymuon.dz_allvertices()) > 0.2) continue;
    if(fabs(mymuon.d0_allvertices()) > 0.045) continue;
    if(mymuon.SemileptonicPFIso() / mymuon.pt() > 0.3) continue;
    
    // extra muon veto
    if(mymuon.isMediumMuon() > 0.5){
	  if(mymuon.pt() != muon.pt() && mymuon.eta() != muon.eta() && mymuon.phi() != muon.phi())
	    b_extramuon_veto_ = true;
    }
    
    // dilepton veto: match with other muons
    if( mymuon.pt() > 15 && mymuon.isGlobalMuon()
                         && mymuon.isTrackerMuon() 
                         && mymuon.isPFMuon() ){
      passedMuons.push_back(mymuon);
    }
  }
  
  std::vector<UZH::Electron> passedElectrons;
  for( int i = 0; i < m_electron.N; ++i ){
    UZH::Electron myelectron( &m_electron, i );
    
    if(myelectron.pt() < 10) continue;
    if(fabs(myelectron.eta()) > 2.5) continue;
    if(fabs(myelectron.dz_allvertices()) > 0.2) continue;
    if(fabs(myelectron.d0_allvertices()) > 0.045) continue;
    if(myelectron.SemileptonicPFIso() / myelectron.pt() > 0.3) continue;
    //if(!myelectron.isMVATightElectron()) continue; // Moriond
    if(!isNonTrigElectronID(myelectron)) continue; // ICHEP
    
    // extra electron veto
    if(myelectron.passConversionVeto() &&
       myelectron.expectedMissingInnerHits() <= 1){
      if( myelectron.pt() != electron.pt() && myelectron.eta() != electron.eta() && myelectron.phi() != electron.phi())
        b_extraelec_veto_ = true;
    }
    
    // dilepton veto: match with other muons
    if(myelectron.pt() > 15)
      passedElectrons.push_back(myelectron);
  }
  
  
  // dilepton veto
  if(channel=="mutau"){
    bool _flag = false;
    for(int imuon = 0; imuon < (int)passedMuons.size(); imuon++){
      for(int jmuon = 0; jmuon < imuon; jmuon++){
        //if(imuon < jmuon) continue;
        if(passedMuons[imuon].charge() * passedMuons[jmuon].charge() < 0 &&
           passedMuons[imuon].tlv().DeltaR(passedMuons[jmuon].tlv()) > 0.15)
          b_dilepton_veto_ = true;
  }}}
  else if(channel=="eletau"){
    for(int ielectron = 0; ielectron < (int)passedElectrons.size(); ielectron++){
      for(int jelectron = 0; jelectron < ielectron; jelectron++){
        //if(ielectron < jelectron) continue;
	    if(passedElectrons[ielectron].charge() * passedElectrons[jelectron].charge() < 0 &&
	       passedElectrons[ielectron].tlv().DeltaR(passedElectrons[jelectron].tlv()) > 0.15)
          b_dilepton_veto_ = true;
  }}}
}





bool TauTauAnalysis::getBTagWeight_promote_demote( const UZH::Jet& jet ) {
  //std::cout << "getBTagSF_promote_demote" << std::endl;
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#B_tag_scale_factors
  // example: https://github.com/rappoccio/usercode/blob/Dev_53x/EDSHyFT/plugins/BTagSFUtil_tprime.h
  //
  // instead of calculating the event weights,
  // scale factors are used to update the b-tagging status on a jet-by-jet basis
  // advantage: 1) no need to apply event weights
  //            2) reproducibility with seed
  
  bool isBTagged = (jet.csv() > m_CSVWorkingPoint);
  if (m_isData) return isBTagged;
  
  //if (isBTagged) std::cout << "Jet b tagged" << std::endl;
  //else           std::cout << "Jet b not tagged" << std::endl;
  
  TRandom3* generator = new TRandom3( (int) ((jet.eta()+5)*100000) );
  double rand = generator->Uniform(1.);
  
  double BTag_SF  = m_BTaggingScaleTool.getScaleFactor_noWeight(jet);
  double BTag_eff = m_BTaggingScaleTool.getEfficiency(jet,"jet_ak4");
  double BTag_SFweight  = m_BTaggingScaleTool.getScaleFactor_veto(jet);
  b_weightbtag_ *= BTag_SFweight;
  
  if (BTag_SF == 1) return isBTagged; // no correction
  else if(BTag_SF > 1){
    if(isBTagged) return isBTagged;
    float mistagPercentage = (1.0 - BTag_SF) / (1.0 - (1.0/BTag_eff)); // fraction of jets to be promoted
    if( rand < mistagPercentage ) isBTagged = true; // PROMOTE
  }
  else{//(BTag_SF < 1)
    if(!isBTagged) return isBTagged;
    if( rand < 1 - BTag_SF ) isBTagged = false; // DEMOTE: 1-SF fraction of jets to be demoted
  }
  
  return isBTagged;
}





void TauTauAnalysis::checks() {
  //std::cout << "checks" << std::endl;

  /// GEN TAUS
  std::vector<UZH::GenParticle> taus;
  std::vector<UZH::GenParticle> muons;
//   std::vector<UZH::GenParticle> quarks;
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    Int_t pdgID = fabs(mygoodGenPart.pdgId());
    if( pdgID == 15 && fabs(mygoodGenPart.mother()[0]) != 15){ // X -> TT 7000021
      taus.push_back(mygoodGenPart);
      
      /// GEN MUON
      //for(int daughter=0; daughter < (int)mygoodGenPart.nDau(); daughter++){
      //  Int_t daughter_pdgId = abs(mygoodGenPart.dau()[daughter]);
      //  if(daughter_pdgId==13){ muons.push_back(mygoodGenPart); break; }
      //}
    }
    else if ( pdgID == 13 && mygoodGenPart.isDirectPromptTauDecayProduct()){
      muons.push_back(mygoodGenPart);
    }
//     else if ( pdgID < 5 ) quarks.push_back(mygoodGenPart);
//     if (muons.size() > 1) break;
  }
  
  if(taus.size() < 2) std::cout << "Warning: taus.size() < 2" << std::endl;
  else{
    //else std::cout << "taus.size() = 2" << std::endl;
    float pt_tau1 = taus.at(0).pt();
    float pt_tau2 = taus.at(1).pt();
    if(pt_tau1 < pt_tau2){
      float pt = pt_tau1;
      pt_tau1 = pt_tau2;
      pt_tau2 = pt;
    }
    
    b_dR_ll_gen_ = taus.at(0).tlv().DeltaR(taus.at(1).tlv());
    Hist("pt_gentaus",      "checks" )->Fill( pt_tau1 );
    Hist("pt_gentaus",      "checks" )->Fill( pt_tau2 );
    Hist("pt_gentau1",      "checks" )->Fill( pt_tau1 );
    Hist("pt_gentau2",      "checks" )->Fill( pt_tau2 );
    Hist("pt_tt_gen",       "checks" )->Fill( (taus.at(0).tlv()+taus.at(1).tlv()).Pt() );
    Hist("DeltaR_tautau",   "checks" )->Fill( b_dR_ll_gen_ );
    Hist("M_tautau",        "checks" )->Fill( (taus.at(0).tlv()+taus.at(1).tlv()).M() );
    
    if (muons.size()<1) return;
    for( int i = 0; i < (int)muons.size(); ++i ){
      Hist("pt_genmuon", "checks" )->Fill( muons.at(i).pt() );
    }
    
    // find hadronic tau
    int itau_h = -1; // hadronic tau index
    int ntau_h = 0; // hadronic tau number
    for( int i = 0; i < 2; ++i ){
      bool isLeptonic = false;
      for(int daughter=0; daughter < (int)taus.at(i).nDau(); daughter++){
        Int_t pdgID = abs(taus.at(i).dau()[daughter]);
        if(pdgID > 10 && pdgID < 15 ){ // find leptons
          isLeptonic = true;
          break;
        }
      }
      if (!isLeptonic){ // save hadronic tau index 
          itau_h = i;
          ntau_h += 1;
          //std::cout << ">>> assigning indixes itau_h = " << itau_h << std::endl;
      }
    }
    
    if (ntau_h == 1 && itau_h > -1 && muons.size() == 1){
      //TLorentzVector muon;
      //muon.SetPtEtaPhiE(muons.at(0).pt(),muons.at(0).eta(),muons.at(0).phi(),muons.at(0).e());
      Hist("DeltaR_taumu",    "checks" )->Fill( taus.at(itau_h).tlv().DeltaR(muons.at(0).tlv()) );
    }
    
  }

}



void TauTauAnalysis::cutflowCheck(const std::string& ch){
  //std::cout << "cutflowCheck" << std::endl;
  
// int genMatch(eta,phi) returns:
//  1: prompt electron
//  2: prompt muon
//  3: tau -> e
//  4. tau -> mu
//  5: tau -> hadr.
//  6: fake jet / PU
// https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_Matching
  
  
  if( ch == "eletau" ) return;
  
   
  // GET GEN PARTICLES
  int ntauh_18_2p3 = 0;
  int ntau = 0;
  std::vector<UZH::GenParticle> genTauhs;
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle myGenPart( &m_genParticle, p );
    Int_t pdgId = abs(myGenPart.pdgId());
    
    // only look at taus
    if(!(myGenPart.status()==2 && pdgId==15 && myGenPart.isPrompt() > 0.5)) continue;
    ntau++;
    bool isHadronic = true;
    for(int daughter=0; daughter < (int)myGenPart.nDau(); daughter++){
      //std::cout << "\t" << "parent " << pdgId << "(pt = " << pt << ") daughter : " << mygoodGenPart.dau()[daughter] << std::endl;
      Int_t daughter_pdgId = abs(myGenPart.dau()[daughter]);
      if(daughter_pdgId==11 || daughter_pdgId==13) isHadronic = false;
    }
    
    // save hadronic taus
    if(isHadronic){
      genTauhs.push_back(myGenPart);
      if(abs(myGenPart.eta())<2.3 && myGenPart.pt()>18) ntauh_18_2p3++;
    }
  }
  
  Hist("N_tau_gen", "checks")->Fill( ntau );
  Hist("N_tauh_gen", "checks")->Fill( genTauhs.size() );
  Hist("N_tauh_18_2p3_gen", "checks")->Fill( ntauh_18_2p3 );
  
  
  // LEPTON MATCHING
  std::vector<UZH::Muon> matchedMuons;
  for( int i = 0; i < m_muon.N; ++i ){
    UZH::Muon mymuon( &m_muon, i );
    if( genMatch(mymuon.eta(),mymuon.phi()) == 4 ) matchedMuons.push_back(mymuon);
  }
  
  
  // TAU MATCHING
  std::vector<UZH::Tau> matchedTaus_std;
  std::vector<UZH::Tau> matchedTaus_bst;
  int ntau_reco         = 0;    // count reco taus
  int ntau_reco_18_2p3  = 0;    // count reco taus
  int ntau1             = 0;    // count standard IDs 
  int ntau2             = 0;    // count boosted IDs
  int ntau1_18_2p3      = 0;    // count standard IDs with pt and eta cut
  int ntau2_18_2p3      = 0;    // count standard IDs with pt and eta cut
  int N_match0p30_std   = 0;      // count dR < 0.3 matches gen tau - standard ID
  int N_match0p30_bst   = 0;      // count dR < 0.3 matches gen tau - boosted ID
  int N_match0p30_18_2p3_std = 0; // count dR < 0.3 matches gen tau - standard ID with cuts on both
  int N_match0p30_18_2p3_bst = 0; // count dR < 0.3 matches gen tau - boosted ID with cuts on both
  double dR_min_std     = 99;   // minimum DeltaR
  for( int i = 0; i < (m_tau.N); ++i ){
    UZH::Tau mytau( &m_tau, i );
    
    int gen_match = genMatch(mytau.eta(),mytau.phi());
    ntau_reco++;
    if(abs(mytau.eta())<2.3 && mytau.pt()>18) ntau_reco_18_2p3++;
    Hist("tau_type", "checks")->Fill( mytau.TauType() );
    Hist("eta_tau_reco", "checks")->Fill( mytau.eta() );
    Hist("pt_tau_reco",  "checks")->Fill( mytau.pt() );
    Hist("decayModeFinding", "checks")->Fill( mytau.decayModeFinding() );
    
    // standard ID
    if(mytau.TauType()==1){
      ntau1++;
      if(abs(mytau.eta())<2.3 && mytau.pt()>18) ntau1_18_2p3++;
      Hist("gen_match_tau_std", "checks")->Fill( gen_match );
      for(int itau=0; itau<(int)genTauhs.size(); itau++){
        float dR = genTauhs[itau].tlv().DeltaR(mytau.tlv());
        Hist("DeltaR_gen_reco_tau_std", "checks")->Fill( dR );
        Hist("DeltaDeltaR", "checks")->Fill(abs( dR - deltaR(mytau.eta()-genTauhs[itau].eta(), deltaPhi(mytau.phi(), genTauhs[itau].phi())) ));
        if(dR<0.3){
          N_match0p30_std++;
          matchedTaus_std.push_back(mytau);
          if(abs(mytau.eta())<2.3 && mytau.pt()>18 && abs(genTauhs[itau].eta())<2.3 && genTauhs[itau].pt()>18) N_match0p30_18_2p3_std++;
        }
        if(dR<dR_min_std) dR_min_std = dR;
      }
      //if( gen_match == 5 )
      //  matchedTaus_std.push_back(mytau);
    }
    
    // boosted ID
    else if(mytau.TauType()==2){
      ntau2++;
      if(abs(mytau.eta())<2.3 && mytau.pt()>18) ntau2_18_2p3++;
      Hist("gen_match_tau_bst", "checks")->Fill( gen_match );
      for(int itau=0; itau<(int)genTauhs.size(); itau++){
        float dR = genTauhs[itau].tlv().DeltaR(mytau.tlv());
        Hist("DeltaR_gen_reco_tau_bst", "checks")->Fill( dR );
        if(dR<0.3){
          N_match0p30_bst++;
          matchedTaus_bst.push_back(mytau);
          if(abs(mytau.eta())<2.3 && mytau.pt()>18 && abs(genTauhs[itau].eta())<2.3 && genTauhs[itau].pt()>18) N_match0p30_18_2p3_bst++;
        }
      }
      //if( gen_match == 5 )
      //  matchedTaus_bst.push_back(mytau);
    }
  }
  
  Hist("N_tau_reco", "checks")->Fill( ntau_reco );
  Hist("N_tau_reco_18_2p3", "checks")->Fill( ntau_reco_18_2p3 );
  Hist("N_tau_std",  "checks")->Fill( ntau1 );
  Hist("N_tau_bst",  "checks")->Fill( ntau2 );
  Hist("N_tau_18_2p3_std", "checks")->Fill( ntau1_18_2p3 );
  Hist("N_gen_match0p30_tau_std", "checks")->Fill( N_match0p30_std );
  Hist("N_gen_match0p30_tau_bst", "checks")->Fill( N_match0p30_bst );

  if(ntauh_18_2p3>0){
    Hist("N_tau_18_2p3_1ctauh_std", "checks")->Fill( ntau1_18_2p3 );
    Hist("DeltaR_gen_reco_tau_min_1ctauh_std", "checks")->Fill( dR_min_std );
    Hist("N_gen_match0p30_1ctauh_tau_std",     "checks")->Fill( N_match0p30_std );
    Hist("N_gen_match0p30_18_2p3_tau_std",     "checks")->Fill( N_match0p30_18_2p3_std );
  }
  else if(genTauhs.size() == 0){
    Hist("DeltaR_gen_reco_tau_min_0tauh_std", "checks")->Fill( dR_min_std );
    Hist("N_gen_match0p30_0tauh_tau_std",     "checks")->Fill( N_match0p30_std );
  }
  
  if(N_match0p30_bst>0){
    Hist("N_gen_match0p30_1bst_tau_std",     "checks")->Fill( N_match0p30_std );
  }
  if(N_match0p30_18_2p3_bst>0){
    Hist("N_gen_match0p30_1bst_18_2p3_tau_std",     "checks")->Fill( N_match0p30_18_2p3_std );
  }
  
  // JET COUNTING
  int ncjets = 0;
  for ( int i = 0; i < (m_jetAK4.N); ++i ) {
    UZH::Jet myjetak4( &m_jetAK4, i );
    if(abs(myjetak4.eta())<2.3) ncjets++;
  }
  if(ncjets>0) Hist("N_gen_match_tau_1cjet_bst", "checks")->Fill( N_match0p30_std );
  
  
  
  // MUON event cutflow
  fillCutflow("lepton_"+ch, "histogram_"+ch, 0);
  if( matchedMuons.size()>0 ){
    UZH::Muon muon = matchedMuons.at(0);
    
    // MATCH
    fillCutflow("lepton_"+ch, "histogram_"+ch, 1);
    
    // ID
    if(muon.isMediumMuon() < 0.5)
      goto next1;
    fillCutflow("lepton_"+ch, "histogram_"+ch, 2);
    
    // ISO
    if(muon.SemileptonicPFIso() / muon.pt() > 0.15)
      goto next1;
    fillCutflow("lepton_"+ch, "histogram_"+ch, 3);
    
    // PT
    if(muon.pt() < 23) // m_muonPtCut
      goto next1;
    fillCutflow("lepton_"+ch, "histogram_"+ch, 4);
    
  }
  next1: { }
  
  
  // STANDARD TAUS event cutflow
  fillCutflow("tauh1_"+ch, "histogram_"+ch, 0);
  if( ntau_reco>0 ){
    
    // TAUS
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 1);
      
    // RECO 18 PT 2.3 ETA CUT
    if(ntau_reco_18_2p3<1)
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 2);
    
    // STANDARD TAU ID
    if(ntau1<1)
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 3);
    
    // GEN 18 PT 2.3 ETA CUT
    if(ntauh_18_2p3<1)
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 4);
    
    // MATCH gen and reco passing 18 pt 2.3 eta cut
    if(N_match0p30_18_2p3_std<1)
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 5);
    UZH::Tau tau1 = matchedTaus_std.at(0);
    
    // DECAYMODE
    if(tau1.decayModeFinding() < 0.5) // m_tauPtCut
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 6);
    
    // ISO
    if(tau1.byTightIsolationMVArun2v1DBoldDMwLT() != 1)
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 7);
    
    // PT
    if(tau1.pt() < 20) // m_tauPtCut
      goto next2;
    fillCutflow("tauh1_"+ch, "histogram_"+ch, 8);
    
  }
  next2: { }
  
    
  // BOOSTED TAUS event cutflow
  fillCutflow("tauh2_"+ch, "histogram_"+ch, 0);
  if( ntau_reco>0 ){
    
    // TAUS
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 1);
      
    // RECO 18 PT 2.3 ETA CUT
    if(ntau_reco_18_2p3<1)
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 2);
    
    // BOOSTED TAU ID
    if(ntau2<1)
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 3);
    
    // GEN 18 PT 2.3 ETA CUT
    if(ntauh_18_2p3<1)
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 4);
    
    // MATCH gen and reco passing 18 pt 2.3 eta cut
    if(N_match0p30_18_2p3_bst<1)
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 5);
    UZH::Tau tau2 = matchedTaus_bst.at(0);
    
    // DECAYMODE
    if(tau2.decayModeFinding() < 0.5) // m_tauPtCut
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 6);
    
    // ISO
    if(tau2.byTightIsolationMVArun2v1DBoldDMwLT() != 1)
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 7);
    
    // PT
    if(tau2.pt() < 20) // m_tauPtCut
      goto next3;
    fillCutflow("tauh2_"+ch, "histogram_"+ch, 8);
    
  }
  next3: { }
  
  // JET event cutflow
  fillCutflow("jet_"+ch, "histogram_"+ch, 0);
  if( ncjets>0 && genTauhs.size()>0 ){
    
    // ETA && DECAYMODE
    fillCutflow("jet_"+ch, "histogram_"+ch, 1);
    
  }
  //next4: { }
  
  return;
}





void TauTauAnalysis::visiblePTCheck(){
  //std::cout << "visiblePTCheck" << std::endl;
  
  // count number of tau IDs
  int ntau_std = 0;
  int ntau_bst = 0;
  for( int i = 0; i < (m_tau.N); ++i ){
    UZH::Tau mytau( &m_tau, i );
    if(mytau.TauType() == 1) ntau_std++;
    else if(mytau.TauType() == 2) ntau_bst++;
  }
   
      
  // retrieve visible pT of the taus
  std::map<int, TLorentzVector> gennus;
  std::map<int, TLorentzVector> genleptons;
  std::map<int, TLorentzVector> gentauhs;
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    
    Float_t pt = mygoodGenPart.pt();
    Float_t eta = mygoodGenPart.eta();
    Float_t phi = mygoodGenPart.phi();
    Float_t energy = mygoodGenPart.e();
    Int_t pdgId = mygoodGenPart.pdgId();
    Int_t abspdgId = abs(mygoodGenPart.pdgId());
    Int_t isPrompt = mygoodGenPart.isPrompt();
    Int_t isDirectPromptTauDecayProduct = mygoodGenPart.isDirectPromptTauDecayProduct();
    
    Int_t mother = -999;
    if(mygoodGenPart.nMoth() !=0){
      mother = abs(mygoodGenPart.mother()[0]);
    }
    
    // save gen tau neutrino + gen leptons from tau decay
    if(mygoodGenPart.status()==1 && abspdgId==16 && mother==15){ 
      TLorentzVector genNeutrino;
      genNeutrino.SetPtEtaPhiE(pt,eta,phi,energy);
      gennus[pdgId] = genNeutrino;
      continue;
    }
    else if( mygoodGenPart.status()==1 && (abspdgId==11 || abspdgId==13) && (isDirectPromptTauDecayProduct > 0.5) ){
      TLorentzVector genLeptons;
      genLeptons.SetPtEtaPhiE(pt,eta,phi,energy);
      genleptons[pdgId] = genLeptons;
      continue;
    }
    
    // skip if not tau
    if(!(mygoodGenPart.status()==2 && abspdgId==15 && isPrompt > 0.5)) continue;
    
    bool isleptonic = false;
    for(int daughter=0; daughter < (int)mygoodGenPart.nDau(); daughter++){
      //std::cout << "\t" << "parent " << pdgId << "(pt = " << pt << ") daughter : " << mygoodGenPart.dau()[daughter] << std::endl;
      Int_t daughter_pdgId = abs(mygoodGenPart.dau()[daughter]);
      if(daughter_pdgId==11 || daughter_pdgId==13) isleptonic = true;
      if(daughter_pdgId==15){
        std::cout << "Tau decays into taus !!!" << std::endl;
        isleptonic = true;
      }
    }
    
    if(isleptonic==false){
      TLorentzVector genPt;
      genPt.SetPtEtaPhiE(pt,eta,phi,energy);
      gentauhs[pdgId] = genPt;
    }
  }
  
  // if tau decays hadronically: loop over gentaus, gennus
  // substract gennu pt from gentau pt
  for(std::map<int, TLorentzVector>::iterator it = gentauhs.begin(); it!=gentauhs.end(); ++it){
    Int_t pdg = (*it).first;
    for(std::map<int, TLorentzVector>::iterator itn = gennus.begin(); itn!=gennus.end(); ++itn){
      Int_t nu = (*itn).first;
      if(pdg==15){
        if(nu==16) (*it).second -= (*itn).second;
      }else if(pdg==-15){
        if(nu==-16) (*it).second -= (*itn).second;
      }else{
	  std::cout << ">>> Warning! gentauhs has a \'first\' != -15 or 15 !" << std::endl;
      }
    }
  }
  
  float pt_tt_vis = -1;
  float DeltaR_vis = -1;
  
  // semileptonic channel
  if(gentauhs.size()==1 && genleptons.size()==1){
    pt_tt_vis = (gentauhs.begin()->second + genleptons.begin()->second).Pt();
    DeltaR_vis = gentauhs.begin()->second.DeltaR(genleptons.begin()->second);
    Hist("pt_tt_vis_ltau", "checks")->Fill( pt_tt_vis );
    Hist("DeltaR_pt_tt_vis_ltau",     "checks")->Fill( pt_tt_vis, DeltaR_vis );
    if (ntau_std > 0) Hist("DeltaR_pt_tt_vis_ltau_std", "checks")->Fill( pt_tt_vis, DeltaR_vis );
    if (ntau_bst > 0) Hist("DeltaR_pt_tt_vis_ltau_bst", "checks")->Fill( pt_tt_vis, DeltaR_vis );
    if(gentauhs.begin()->first * genleptons.begin()->first > 0){
      std::cout << ">>> Warning! gentauhs.begin()->first * genleptons.begin()->first > 0" << std::endl;
    }
  }
  // all hadronic channel
  else if(gentauhs.size()==2){
    TLorentzVector tlv_tt;
    int charge = 1;
    for(std::map<int, TLorentzVector>::iterator it = gentauhs.begin(); it!=gentauhs.end(); ++it){
      tlv_tt += (*it).second;
      charge *= (*it).first;
    }
    pt_tt_vis = tlv_tt.Pt();
    if(charge > 0){
      std::cout << ">>> Warning! All hadronic channel's charge*charge > 0" << std::endl;
    }
  }
  // dilepton channel
  else if(genleptons.size()==2){
    TLorentzVector tlv_tt;
    int charge = 1;
    for(std::map<int, TLorentzVector>::iterator it = genleptons.begin(); it!=genleptons.end(); ++it){
      tlv_tt += (*it).second;
      charge *= (*it).first;
    }
    pt_tt_vis = tlv_tt.Pt();
    if(charge > 0){
      std::cout << ">>> Warning! Dileptonic channel's charge*charge > 0" << std::endl;
    }
  }
  else if( (gentauhs.size()+genleptons.size())!=2 ){
    std::cout << ">>> Warning! (gentauhs.size()+genleptons.size()) != 2" << std::endl;
    std::cout << ">>>           gentauhs.size() = " << gentauhs.size() << ", genleptons.size() = " << genleptons.size() << std::endl;
  }
  
  Hist("pt_tt_vis", "checks")->Fill( pt_tt_vis );
  
}






