// $Id: CycleCreators.py 344 2012-12-13 13:10:53Z krasznaa $

#include "../include/TauTauAnalysis.h"

ClassImp( TauTauAnalysis );





TauTauAnalysis::TauTauAnalysis() : SCycleBase(),
    m_eventInfo( this ),
    m_jetAK4( this ),
    m_genJetAK4( this ),
    m_electron( this ),
    m_muon( this ),
    m_tau( this ),
    m_missingEt( this ),
    m_puppimissingEt( this ),
    //m_mvamissingEt( this ),
    m_genParticle( this ),
    m_PileupReweightingTool( this ),
    m_BTaggingScaleTool( this ),
    m_ScaleFactorTool( this ),
    m_RecoilCorrector( this ),
    m_JetCorrectionTool( this ),
    m_SVFitTool( this )
{

  m_logger << INFO << "Hello!" << SLogger::endmsg;
  SetLogName( GetName() );
  
  // channels
  channels_.push_back("mutau");
  channels_.push_back("etau");
  //channels_.push_back("emu");
  
  // read configuration details from XML file
  DeclareProperty( "RecoTreeName",          m_recoTreeName          = "tree" );
  DeclareProperty( "JetAK4Name",            m_jetAK4Name            = "jetAK4" );
  DeclareProperty( "genJetAK4Name",         m_genJetAK4Name         = "genJetAK4" );
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
  DeclareProperty( "doJEC",                 m_doJEC                 = false );
  DeclareProperty( "doTES",                 m_doTES                 = false );
  DeclareProperty( "TESshift",              m_TESshift              = 0.0 );
  DeclareProperty( "doEES",                 m_doEES                 = false );
  DeclareProperty( "EESshift",              m_EESshift              = 0.0 );
  DeclareProperty( "EESshiftEndCap",        m_EESshiftEndCap        = m_EESshift*2.5 );
  DeclareProperty( "doLTF",                 m_doLTF                 = false );
  DeclareProperty( "LTFshift",              m_LTFshift              = 0.0 );
  DeclareProperty( "doTight",               m_doTight               = m_doEES or m_doTES or m_doLTF ); // fill branches with less events
  // for SUSY https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016
  // for comparison https://twiki.cern.ch/twiki/bin/viewauth/CMS/MSSMAHTauTauSummer2016#Baseline
  // for us https://twiki.cern.ch/twiki/bin/view/CMS/SMTauTau2016#Baseline_sync_selection
  DeclareProperty( "AK4JetPtCut",           m_AK4jetPtCut           = 20.   );
  DeclareProperty( "AK4JetEtaCut",          m_AK4jetEtaCut          = 4.7   );
  DeclareProperty( "CSVWorkingPoint",       m_CSVWorkingPoint       = 0.8484 ); // 0.8 is Medium
  
  DeclareProperty( "ElectronPtCut",         m_electronPtCut         = 25.   ); // Cross trigger Ele24
  DeclareProperty( "ElectronEtaCut",        m_electronEtaCut        = 2.1   );
  DeclareProperty( "ElectronD0Cut",         m_electronD0Cut         = 0.045 );
  DeclareProperty( "ElectronDzCut",         m_electronDzCut         = 0.2   );
  DeclareProperty( "ElectronIsoCut",        m_electronIsoCut        = 0.1   );
  
  DeclareProperty( "MuonPtCut",             m_muonPtCut             = 20.   ); // Cross trigger Mu19
  DeclareProperty( "MuonEtaCut",            m_muonEtaCut            = 2.4   ); // 2.4; 2.1
  DeclareProperty( "MuonD0Cut",             m_muonD0Cut             = 0.045 );
  DeclareProperty( "MuonDzCut",             m_muonDzCut             = 0.2   );
  DeclareProperty( "MuonIsoCut",            m_muonIsoCut            = 0.15  );
  
  DeclareProperty( "TauPtCut",              m_tauPtCut              = 20.  ); // 20; 30
  DeclareProperty( "TauEtaCut",             m_tauEtaCut             = 2.3  );
  DeclareProperty( "TauDzCut",              m_tauDzCut              = 0.2  );
  
  // Moriond: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt 
  DeclareProperty( "JSONName",              m_jsonName              = std::string (std::getenv("SFRAME_DIR")) + "/../GoodRunsLists/JSON/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt" ); // Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt
  
}





TauTauAnalysis::~TauTauAnalysis() {
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "Tschoe!" << SLogger::endmsg;
  std::cout << " " << std::endl;
}





void TauTauAnalysis::BeginCycle() throw( SError ) {
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "BeginCycle" << SLogger::endmsg;
  
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
  
  m_triggers_mutau.clear();
  m_triggers_etau.clear();
  //m_triggerNames_mutau.clear();
  //m_triggerNames_eletau.clear();
  
  // MARK: Triggers
  // https://indico.cern.ch/event/598433/#day-2017-02-15
  // https://indico.cern.ch/event/598433/contributions/2475199/attachments/1413150/2162337/Davignon_TauTriggerRecommendations_HTTMeeting_15_02_17_v2.pdf slide 11
  // https://hypernews.cern.ch/HyperNews/CMS/get/AUX/2017/02/10/17:01:24-67933-2016triggerGrandTable.pdf
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Trigger_Information
  // https://indico.cern.ch/event/605295/contributions/2454799/attachments/1402337/2141040/leptonSF_260117.pdf (emu)
  
  // 2016 JSON run 271036 to 284044
  int firstRun = 271000;
  int lastRun  = 285000;
  std::vector<std::string> IsoMu22 = {"hltL3crIsoL1sMu18L1f0L2f10QL3f20QL3trkIsoFiltered0p09", "hltL3fL1sMu20L1f0Tkf22QL3trkIsoFiltered0p09",
                                      "hltL3crIsoL1sSingleMu20erL1f0L2f10QL3f22QL3trkIsoFiltered0p09", "hltL3fL1sMu20erL1f0Tkf22QL3trkIsoFiltered0p09"};
  // muon triggers
  m_triggers_mutau.push_back(new LeptonTrigger("HLT_IsoMu22_v",         firstRun, 276863,22.0+1,IsoMu22));
  m_triggers_mutau.push_back(new LeptonTrigger("HLT_IsoTkMu22_v",       firstRun, 276863,22.0+1,IsoMu22));
  m_triggers_mutau.push_back(new LeptonTrigger("HLT_IsoMu22_eta2p1_v",    274890,lastRun,22.0+1,IsoMu22));
  m_triggers_mutau.push_back(new LeptonTrigger("HLT_IsoTkMu22_eta2p1_v",  274890,lastRun,22.0+1,IsoMu22));
  m_triggers_mutau.push_back(new CrossTrigger("HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v",firstRun,lastRun,19.+1,0,
                                                "hltL3crIsoL1sSingleMu18erIorSingleMu20erL1f0L2f10QL3f19QL3trkIsoFiltered0p09"));
  
  // electron triggers
  m_triggers_etau.push_back(new LeptonTrigger("HLT_Ele25_eta2p1_WPTight_Gsf_v",     firstRun,lastRun,25.+1,
                                            {"hltEle25erWPTightGsfTrackIsoFilter","hltEle45WPLooseGsfTrackIsoL1TauJetSeededFilter"}));
  m_triggers_etau.push_back(new LeptonTrigger("HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded", 275392, 278270,25.+1,
                                            {"hltEle25erWPTightGsfTrackIsoFilter","hltEle45WPLooseGsfTrackIsoL1TauJetSeededFilter"}));
  m_triggers_etau.push_back(new CrossTrigger("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v", firstRun, 276214,24.+0,20.,
                                            "hltEle25erWPTightGsfTrackIsoFilter"));
  m_triggers_etau.push_back(new CrossTrigger("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v", 276215, 278269,24.+0,20.,
                                            "hltEle25erWPTightGsfTrackIsoFilter"));
  m_triggers_etau.push_back(new CrossTrigger("HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v", 278271,lastRun,24.+0,20.,
                                            "hltEle25erWPTightGsfTrackIsoFilter"));
  
  
  m_logger << INFO << "\nmutau triggers: " << SLogger::endmsg;
  for (auto const& trigger: m_triggers_mutau){
    m_logger << INFO << "  " << trigger->start << " - " << trigger->end << "  " << trigger->name << SLogger::endmsg;
  }
  m_logger << INFO << "\netau triggers: " << SLogger::endmsg;
  for (auto const& trigger: m_triggers_etau){
    m_logger << INFO << "  " << trigger->start << " - " << trigger->end << "  " << trigger->name << SLogger::endmsg;
  }
  m_logger << INFO << " " << SLogger::endmsg;
  
  return;

}





void TauTauAnalysis::EndCycle() throw( SError ) {
   m_logger << INFO << " " << SLogger::endmsg;
   m_logger << INFO << "EndInputData" << SLogger::endmsg;
   m_logger << INFO << "events in mu_tau: "  << mu_tau << SLogger::endmsg;
   m_logger << INFO << "events in ele_tau: " << ele_tau << SLogger::endmsg;
   m_logger << INFO << " " << SLogger::endmsg;
   return;
}





void TauTauAnalysis::BeginInputData( const SInputData& id ) throw( SError ) {
  //std::cout << "BeginInputData" << std::endl;
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "BeginInputData" << SLogger::endmsg;
  
  m_logger << INFO << "RecoTreeName:        " <<    m_recoTreeName      << SLogger::endmsg;
  m_logger << INFO << "JetAK4Name:          " <<    m_jetAK4Name        << SLogger::endmsg;
  m_logger << INFO << "ElectronName:        " <<    m_electronName      << SLogger::endmsg;
  m_logger << INFO << "MuonName:            " <<    m_muonName          << SLogger::endmsg;
  m_logger << INFO << "TauName:             " <<    m_tauName           << SLogger::endmsg;
  m_logger << INFO << "GenParticleName:     " <<    m_genParticleName   << SLogger::endmsg;
  
  m_doJEC = m_doJEC and !(m_doTES or m_doEES or m_doLTF or m_isData);
  m_logger << INFO << "IsData:              " <<    (m_isData   ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "IsSignal:            " <<    (m_isSignal ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doSVFit:             " <<    (m_doSVFit  ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doRecoilCorr:        " <<    (m_doRecoilCorr ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doZpt:               " <<    (m_doZpt    ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTTpt:              " <<    (m_doTTpt   ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doJEC:               " <<    (m_doJEC    ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTES:               " <<    (m_doTES    ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "TESshift:            " <<    m_TESshift << SLogger::endmsg;
  m_logger << INFO << "doEES:               " <<    (m_doEES    ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "EESshift:            " <<    m_EESshift          << SLogger::endmsg;
  m_logger << INFO << "EESshiftEndCap:      " <<    m_EESshiftEndCap    << SLogger::endmsg;
  m_logger << INFO << "doLTF:               " <<    (m_doLTF    ?   "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "LTFshift:            " <<    m_TESshift          << SLogger::endmsg;

  m_logger << INFO << "ElectronPtCut:       " <<    m_electronPtCut     << SLogger::endmsg;
  m_logger << INFO << "ElectronEtaCut:      " <<    m_electronEtaCut    << SLogger::endmsg;
  m_logger << INFO << "ElectronD0Cut:       " <<    m_electronD0Cut     << SLogger::endmsg;
  m_logger << INFO << "ElectronDzCut:       " <<    m_electronDzCut     << SLogger::endmsg;
  m_logger << INFO << "ElectronIsoCut:      " <<    m_electronIsoCut    << SLogger::endmsg;
  
  m_logger << INFO << "MuonPtCut:           " <<    m_muonPtCut         << SLogger::endmsg;
  m_logger << INFO << "MuonEtaCut:          " <<    m_muonEtaCut        << SLogger::endmsg;
  m_logger << INFO << "MuonD0Cut:           " <<    m_muonD0Cut         << SLogger::endmsg;
  m_logger << INFO << "MuonDzCut:           " <<    m_muonDzCut         << SLogger::endmsg;
  m_logger << INFO << "MuonIsoCut:          " <<    m_muonIsoCut        << SLogger::endmsg;
  
  m_logger << INFO << "TauPtCut:            " <<    m_tauPtCut          << SLogger::endmsg;
  m_logger << INFO << "TauEtaCut:           " <<    m_tauEtaCut         << SLogger::endmsg;
  m_logger << INFO << "TauDzCut:            " <<    m_tauDzCut          << SLogger::endmsg;
    
  m_logger << INFO << "JSONName:            " <<    m_jsonName          << SLogger::endmsg;
  

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
  for(int chi = 0; chi < (int)channels_.size(); chi++){
    
    TString treeName = "tree_" + channels_[chi];
    const char* ch = channels_[chi].c_str();
    
    DeclareVariable( b_channel[ch],         "channel",          treeName);
    DeclareVariable( b_isData[ch],          "isData",           treeName);
    
    DeclareVariable( b_weight[ch],          "weight",           treeName);
    DeclareVariable( b_genweight[ch],       "genweight",        treeName);
    DeclareVariable( b_puweight[ch],        "puweight",         treeName);
    DeclareVariable( b_weightbtag[ch],      "weightbtag",       treeName);
    DeclareVariable( b_zptweight[ch],       "zptweight",        treeName);
    DeclareVariable( b_ttptweight[ch],      "ttptweight",       treeName);
    DeclareVariable( b_trigweight_1[ch],    "trigweight_1",     treeName);
    DeclareVariable( b_trigweight_or_1[ch], "trigweight_or_1",  treeName);
    DeclareVariable( b_idisoweight_1[ch],   "idisoweight_1",    treeName);
    DeclareVariable( b_trigweight_2[ch],    "trigweight_2",     treeName);
    DeclareVariable( b_idisoweight_2[ch],   "idisoweight_2",    treeName);
    
    DeclareVariable( b_triggers[ch],        "triggers",         treeName);
    DeclareVariable( b_run[ch],             "run",              treeName);
    DeclareVariable( b_evt[ch],             "evt",              treeName);
    DeclareVariable( b_lum[ch],             "lum",              treeName);
    
    DeclareVariable( b_npv[ch],             "npv",              treeName);
    DeclareVariable( b_npu[ch],             "npu",              treeName);
    DeclareVariable( b_NUP[ch],             "NUP",              treeName);
    DeclareVariable( b_rho[ch],             "rho",              treeName);
    
    DeclareVariable( b_njets[ch],           "njets",            treeName);
    DeclareVariable( b_nfjets[ch],          "nfjets",           treeName);
    DeclareVariable( b_ncjets[ch],          "ncjets",           treeName);
    DeclareVariable( b_nbtag[ch],           "nbtag",            treeName);
    DeclareVariable( b_ncbtag[ch],          "ncbtag",           treeName);
    DeclareVariable( b_njets20[ch],         "njets20",          treeName);
    DeclareVariable( b_nfjets20[ch],        "nfjets20",         treeName);
    DeclareVariable( b_ncjets20[ch],        "ncjets20",         treeName);
    DeclareVariable( b_nbtag20[ch],         "nbtag20",          treeName);
    DeclareVariable( b_ncbtag20[ch],        "ncbtag20",         treeName);
    
    if (m_doJEC){
      DeclareVariable( b_ncjets_jesUp[ch],          "ncjets_jesUp",         treeName);
      DeclareVariable( b_ncjets_jesDown[ch],        "ncjets_jesDown",       treeName);
      DeclareVariable( b_ncjets_jer[ch],            "ncjets_jer",           treeName);
      DeclareVariable( b_ncjets_jerUp[ch],          "ncjets_jerUp",         treeName);
      DeclareVariable( b_ncjets_jerDown[ch],        "ncjets_jerDown",       treeName);
      DeclareVariable( b_ncbtag_jesUp[ch],          "ncbtag_jesUp",         treeName);
      DeclareVariable( b_ncbtag_jesDown[ch],        "ncbtag_jesDown",       treeName);
      DeclareVariable( b_ncbtag_jer[ch],            "ncbtag_jer",           treeName);
      DeclareVariable( b_ncbtag_jerUp[ch],          "ncbtag_jerUp",         treeName);
      DeclareVariable( b_ncbtag_jerDown[ch],        "ncbtag_jerDown",       treeName);
      DeclareVariable( b_nfjets_jesUp[ch],          "nfjets_jesUp",         treeName);
      DeclareVariable( b_nfjets_jesDown[ch],        "nfjets_jesDown",       treeName);
      DeclareVariable( b_nfjets_jer[ch],            "nfjets_jer",           treeName);
      DeclareVariable( b_nfjets_jerUp[ch],          "nfjets_jerUp",         treeName);
      DeclareVariable( b_nfjets_jerDown[ch],        "nfjets_jerDown",       treeName);
      DeclareVariable( b_dphi_ll_bj_jesUp[ch],      "dphi_ll_bj_jesUp",     treeName);
      DeclareVariable( b_dphi_ll_bj_jesDown[ch],    "dphi_ll_bj_jesDown",   treeName);
      DeclareVariable( b_dphi_ll_bj_jer[ch],        "dphi_ll_bj_jer",       treeName);
      DeclareVariable( b_dphi_ll_bj_jerUp[ch],      "dphi_ll_bj_jerUp",     treeName);
      DeclareVariable( b_dphi_ll_bj_jerDown[ch],    "dphi_ll_bj_jerDown",   treeName);
            
      DeclareVariable( b_met_jesUp[ch],             "met_jesUp",            treeName);
      DeclareVariable( b_met_jesDown[ch],           "met_jesDown",          treeName);
      DeclareVariable( b_met_jer[ch],               "met_jer",              treeName);
      DeclareVariable( b_met_jerUp[ch],             "met_jerUp",            treeName);
      DeclareVariable( b_met_jerDown[ch],           "met_jerDown",          treeName);
      DeclareVariable( b_met_UncEnUp[ch],           "met_UncEnUp",          treeName);
      DeclareVariable( b_met_UncEnDown[ch],         "met_UncEnDown",        treeName);
      DeclareVariable( b_pfmt_1_jesUp[ch],          "pfmt_1_jesUp",         treeName);
      DeclareVariable( b_pfmt_1_jesDown[ch],        "pfmt_1_jesDown",       treeName);
      DeclareVariable( b_pfmt_1_jer[ch],            "pfmt_1_jer",           treeName);
      DeclareVariable( b_pfmt_1_jerUp[ch],          "pfmt_1_jerUp",         treeName);
      DeclareVariable( b_pfmt_1_jerDown[ch],        "pfmt_1_jerDown",       treeName);
      DeclareVariable( b_pfmt_1_UncEnUp[ch],        "pfmt_1_UncEnUp",       treeName);
      DeclareVariable( b_pfmt_1_UncEnDown[ch],      "pfmt_1_UncEnDown",     treeName);
      
      DeclareVariable( b_weightbtag_bcUp[ch],       "weightbtag_bcUp",      treeName);
      DeclareVariable( b_weightbtag_bcDown[ch],     "weightbtag_bcDown",    treeName);
      DeclareVariable( b_weightbtag_udsgUp[ch],     "weightbtag_udsgUp",    treeName);
      DeclareVariable( b_weightbtag_udsgDown[ch],   "weightbtag_udsgDown",  treeName);
    }
    
    DeclareVariable( b_pt_1[ch],                "pt_1",                 treeName);
    DeclareVariable( b_eta_1[ch],               "eta_1",                treeName);
    DeclareVariable( b_phi_1[ch],               "phi_1",                treeName);
    DeclareVariable( b_m_1[ch],                 "m_1",                  treeName);
    DeclareVariable( b_q_1[ch],                 "q_1",                  treeName);
    DeclareVariable( b_d0_1[ch],                "d0_1",                 treeName);
    DeclareVariable( b_dz_1[ch],                "dz_1",                 treeName);
    //DeclareVariable( b_mt_1[ch],                "mt_1",                 treeName);
    DeclareVariable( b_pfmt_1[ch],              "pfmt_1",               treeName);
    DeclareVariable( b_puppimt_1[ch],           "puppimt_1",            treeName);
    DeclareVariable( b_iso_1[ch],               "iso_1",                treeName);
    DeclareVariable( b_id_e_mva_nt_loose_1[ch], "id_e_mva_nt_loose_1",  treeName);
    DeclareVariable( b_gen_match_1[ch],         "gen_match_1",          treeName);
    
    DeclareVariable( b_pt_2[ch],            "pt_2",             treeName);
    DeclareVariable( b_eta_2[ch],           "eta_2",            treeName);
    DeclareVariable( b_phi_2[ch],           "phi_2",            treeName);
    DeclareVariable( b_m_2[ch],             "m_2",              treeName);
    DeclareVariable( b_q_2[ch],             "q_2",              treeName);
    DeclareVariable( b_d0_2[ch],            "d0_2",             treeName);
    DeclareVariable( b_dz_2[ch],            "dz_2",             treeName);
    //DeclareVariable( b_mt_2[ch],            "mt_2",             treeName);
    DeclareVariable( b_pfmt_2[ch],          "pfmt_2",           treeName);
    DeclareVariable( b_puppimt_2[ch],       "puppimt_2",        treeName);
    DeclareVariable( b_iso_2[ch],           "iso_2",            treeName);
    DeclareVariable( b_iso_2_medium[ch],    "iso_2_medium",     treeName);
    DeclareVariable( b_gen_match_2[ch],     "gen_match_2",      treeName);
    DeclareVariable( b_pol_2[ch],           "pol_2",            treeName);
    
    DeclareVariable( b_againstElectronVLooseMVA6_2[ch],  "againstElectronVLooseMVA6_2",  treeName);
    DeclareVariable( b_againstElectronLooseMVA6_2[ch],   "againstElectronLooseMVA6_2",   treeName);
    DeclareVariable( b_againstElectronMediumMVA6_2[ch],  "againstElectronMediumMVA6_2",  treeName);
    DeclareVariable( b_againstElectronTightMVA6_2[ch],   "againstElectronTightMVA6_2",   treeName);
    DeclareVariable( b_againstElectronVTightMVA6_2[ch],  "againstElectronVTightMVA6_2",  treeName);
    DeclareVariable( b_againstMuonLoose3_2[ch],          "againstMuonLoose3_2",          treeName);
    DeclareVariable( b_againstMuonTight3_2[ch],          "againstMuonTight3_2",          treeName);
    DeclareVariable( b_byCombinedIsolationDeltaBetaCorrRaw3Hits_2[ch], "byCombinedIsolationDeltaBetaCorrRaw3Hits_2", treeName);
    DeclareVariable( b_byIsolationMVA3newDMwLTraw_2[ch], "byIsolationMVA3newDMwLTraw_2", treeName);
    DeclareVariable( b_byIsolationMVA3oldDMwLTraw_2[ch], "byIsolationMVA3oldDMwLTraw_2", treeName);
    DeclareVariable( b_chargedIsoPtSum_2[ch],            "chargedIsoPtSum_2",            treeName);
    DeclareVariable( b_neutralIsoPtSum_2[ch],            "neutralIsoPtSum_2",            treeName);
    DeclareVariable( b_puCorrPtSum_2[ch],                "puCorrPtSum_2",                treeName);
    DeclareVariable( b_decayModeFindingOldDMs_2[ch],     "decayModeFindingOldDMs_2",     treeName);
    DeclareVariable( b_decayMode_2[ch],                  "decayMode_2",                  treeName);
    
    DeclareVariable( b_dilepton_veto[ch],   "dilepton_veto",    treeName);
    DeclareVariable( b_extraelec_veto[ch],  "extraelec_veto",   treeName);
    DeclareVariable( b_extramuon_veto[ch],  "extramuon_veto",   treeName);
    DeclareVariable( b_lepton_vetos[ch],    "lepton_vetos",     treeName);
    DeclareVariable( b_iso_cuts[ch],        "iso_cuts",         treeName);
    DeclareVariable( b_trigger_cuts[ch],    "trigger_cuts",     treeName);
    
    DeclareVariable( b_jpt_1[ch],           "jpt_1",            treeName);
    DeclareVariable( b_jeta_1[ch],          "jeta_1",           treeName);
    DeclareVariable( b_jphi_1[ch],          "jphi_1",           treeName);
    DeclareVariable( b_jpt_2[ch],           "jpt_2",            treeName);
    DeclareVariable( b_jeta_2[ch],          "jeta_2",           treeName);
    DeclareVariable( b_jphi_2[ch],          "jphi_2",           treeName);
    
    DeclareVariable( b_bpt_1[ch],           "bpt_1",            treeName);
    DeclareVariable( b_beta_1[ch],          "beta_1",           treeName);
    DeclareVariable( b_bphi_1[ch],          "bphi_1",           treeName);
    DeclareVariable( b_bcsv_1[ch],          "bcsv_1",           treeName);
    DeclareVariable( b_bpt_2[ch],           "bpt_2",            treeName);
    DeclareVariable( b_beta_2[ch],          "beta_2",           treeName);
    DeclareVariable( b_bphi_2[ch],          "bphi_2",           treeName);
    DeclareVariable( b_bcsv_2[ch],          "bcsv_2",           treeName);
    
    DeclareVariable( b_met[ch],             "met",              treeName);
    DeclareVariable( b_met_old[ch],         "met_old",          treeName);
    DeclareVariable( b_metphi[ch],          "metphi",           treeName);
    DeclareVariable( b_puppimet[ch],        "puppimet",         treeName);
    DeclareVariable( b_puppimetphi[ch],     "puppimetphi",      treeName);
    //DeclareVariable( b_mvamet[ch],          "mvamet",           treeName);
    //DeclareVariable( b_mvamet_old[ch],      "mvamet_old",       treeName);
    //DeclareVariable( b_mvametphi[ch],       "mvametphi",        treeName);
    
    DeclareVariable( b_metcov00[ch],        "metcov00",         treeName);
    DeclareVariable( b_metcov01[ch],        "metcov01",         treeName);
    DeclareVariable( b_metcov10[ch],        "metcov10",         treeName);
    DeclareVariable( b_metcov11[ch],        "metcov11",         treeName);
    //DeclareVariable( b_mvacov00[ch],        "mvacov00",         treeName);
    //DeclareVariable( b_mvacov01[ch],        "mvacov01",         treeName);
    //DeclareVariable( b_mvacov10[ch],        "mvacov10",         treeName);
    //DeclareVariable( b_mvacov11[ch],        "mvacov11",         treeName);
    
    DeclareVariable( b_m_vis[ch],           "m_vis",            treeName);
    DeclareVariable( b_pt_tt[ch],           "pt_tt",            treeName);
    DeclareVariable( b_pt_tt_vis[ch],       "pt_tt_vis",        treeName);
    DeclareVariable( b_R_pt_m_vis[ch],      "R_pt_m_vis",       treeName);
    DeclareVariable( b_R_pt_m_vis2[ch],     "R_pt_m_vis2",      treeName);
    
    DeclareVariable( b_m_sv[ch],            "m_sv",             treeName);
    //DeclareVariable( b_m_sv_pfmet[ch],      "m_sv_pfmet",       treeName);
    DeclareVariable( b_pt_tt_sv[ch],        "pt_tt_sv",         treeName);
    DeclareVariable( b_R_pt_m_sv[ch],       "R_pt_m_sv",        treeName);
    
    DeclareVariable( b_dR_ll[ch],           "dR_ll",            treeName);
    DeclareVariable( b_dphi_ll_bj[ch],      "dphi_ll_bj",       treeName);
    DeclareVariable( b_mt_tot[ch],          "mt_tot",           treeName);
    DeclareVariable( b_ht[ch],              "ht",               treeName);
    
    if(m_doRecoilCorr || m_doZpt){
      DeclareVariable( b_m_genboson[ch],    "m_genboson",       treeName);
      DeclareVariable( b_pt_genboson[ch],   "pt_genboson",      treeName);
    }    
    if(m_doTTpt){
      DeclareVariable( b_pt_top_1[ch],          "pt_top_1",         treeName);
      DeclareVariable( b_pt_top_2[ch],          "pt_top_2",         treeName);
      DeclareVariable( b_ttptweight_runI[ch],   "ttptweight_runI",  treeName);
    }    
    
    DeclareVariable( b_pzetamiss[ch],       "pzetamiss",        treeName);
    DeclareVariable( b_pzetavis[ch],        "pzetavis",         treeName);
    DeclareVariable( b_pzeta_disc[ch],      "pzeta_disc",       treeName);
    DeclareVariable( b_vbf_mjj[ch],         "vbf_mjj",          treeName);
    DeclareVariable( b_vbf_deta[ch],        "vbf_deta",         treeName);
    DeclareVariable( b_vbf_jdphi[ch],       "vbf_jdphi",        treeName);
    DeclareVariable( b_vbf_ncentral[ch],    "vbf_ncentral",     treeName);
    DeclareVariable( b_vbf_ncentral20[ch],  "vbf_ncentral20",   treeName);
    
  }
  
  
  // MARK Histograms
  m_logger << INFO << "Declaring histograms" << SLogger::endmsg;
  
  for (auto ch: channels_){
    TString hname = "cutflow_" + ch;
    TString dirname = "histogram_" + ch;
    TString tch = ch;
    Book( TH1F(hname, hname, 20, 0.5, 20.5 ), dirname);
    //Book( TH1F("btagweight", "btagweight", 6, 0, 6), dirname);
  }
  
  makeHistogramsForChecks();
  
  
  m_BTaggingScaleTool.BeginInputData( id );
  m_BTaggingScaleTool.bookHistograms(); // to measure b tag efficiencies for our selections
  m_ScaleFactorTool.BeginInputData( id );
  m_RecoilCorrector.BeginInputData( id );
  m_JetCorrectionTool.BeginInputData( id );
  m_SVFitTool.BeginInputData( id );
  
  return;

}





void TauTauAnalysis::EndInputData( const SInputData& ) throw( SError ) {
  //std::cout << "EndInputData" << std::endl;
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "EndInputData" << SLogger::endmsg;
  m_logger << INFO << " " << SLogger::endmsg;
  
  std::vector<std::string> kCutNameLep{ "start", "match", "ID", "iso", "pt" };
  //std::vector<std::string> kCutNameTau{ "start", "match", "DecayMode", "iso", "pt" };
  std::vector<std::string> kCutNameTau{ "start", "at least one reco tau", "2.3 eta and 18 pt reco cut", "tau ID", "2.3 eta and 18 pt gen cut", "match", "DecayMode", "iso", "pt" };
  std::vector<std::string> kCutNameJet{ "start", "one eta<2.3 jet && hadronic" };
  
  for(auto ch: channels_) {
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
    
    // if(m_isSignal and ch == "mutau"){
    //   printCutFlow(ch,"lepton","lepton_"+ch,dirname,kCutNameLep);
    //   printCutFlow(ch,"tau standard ID","tauh1_"+ch,dirname,kCutNameTau);
    //   printCutFlow(ch,"tau boosted ID","tauh2_"+ch,dirname,kCutNameTau);
    //   printCutFlow(ch,"jet","jet_"+ch,dirname,kCutNameJet);
    // }
    
    m_logger << INFO << " " << SLogger::endmsg;
    
  }

  return;
}



void TauTauAnalysis::printCutFlow(const std::string& ch, const std::string& name, const TString hname, const TString dirname, std::vector<std::string> cutName){
 //std::cout << "printCutFlow" << std::endl;
  
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
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "Connecting input variables" << SLogger::endmsg;
  
  if (m_isData) {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis, (m_jetAK4Name + "_").c_str() );
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoTrigger|Ntuple::EventInfoMETFilters, "" );
  }
  else {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis|Ntuple::JetTruth|Ntuple::JetJER, (m_jetAK4Name + "_").c_str() );
    m_genJetAK4.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::GenJetak4Truth,"");
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoBasic|Ntuple::EventInfoTrigger|Ntuple::EventInfoMETFilters|Ntuple::EventInfoTruth, "" );
    m_genParticle.ConnectVariables( m_recoTreeName.c_str(), Ntuple::GenParticleBasic|Ntuple::GenParticleTauDecayAnalysis, (m_genParticleName + "_").c_str() );
  }
  m_electron.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::ElectronBasic|Ntuple::ElectronID|Ntuple::ElectronAdvancedID|Ntuple::ElectronBoostedIsolation|Ntuple::ElectronSuperCluster, (m_electronName + "_").c_str() );
  m_muon.ConnectVariables(          m_recoTreeName.c_str(), Ntuple::MuonBasic|Ntuple::MuonID|Ntuple::MuonIsolation|Ntuple::MuonTrack|Ntuple::MuonBoostedIsolation, (m_muonName + "_").c_str() );
  m_tau.ConnectVariables(           m_recoTreeName.c_str(), Ntuple::TauBasic|Ntuple::TauID|Ntuple::TauAdvancedID, (m_tauName + "_").c_str() );

  m_missingEt.ConnectVariables(     m_recoTreeName.c_str(), Ntuple::MissingEtBasic|Ntuple::MissingEtAnalysis|Ntuple::MissingEtAnalysisSyst|Ntuple::MissingEtCovAnalysis, (m_missingEtName + "_").c_str() );
  m_puppimissingEt.ConnectVariables(m_recoTreeName.c_str(), Ntuple::MissingEtBasic, (m_missingEtName + "_puppi_").c_str() );
  //m_mvamissingEt.ConnectVariables(  m_recoTreeName.c_str(), Ntuple::MissingEtBasic|Ntuple::MissingEtMVAAnalysis|Ntuple::MissingEtCovAnalysis, (m_missingEtName + "_mva_").c_str() );
  
  m_logger << INFO << "Connecting input variables completed" << SLogger::endmsg;
  
  return;

}





void TauTauAnalysis::ExecuteEvent( const SInputData&, Double_t ) throw( SError ) {
  //std::cout << "ExecuteEvent" << std::endl;
  //m_logger << VERBOSE << "ExecuteEvent" << SLogger::endmsg;
  
  b_weight_     =  1.;
  b_puweight_   =  1.; 
  b_genweight_  =  1.;
  b_npu_        = -1.;
  m_muonEtaCut_variable = m_muonEtaCut;
  
  UZH::MissingEt met(      &m_missingEt, 0 );
  UZH::MissingEt puppiMet( &m_puppimissingEt, 0 );
    
  
  // Cut 0: no cuts
  for (auto ch: channels_){
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCuts, 1);
    b_channel[ch] = 0;
  }
  
  
  // Cut 1: check for data if run/lumiblock in JSON
  if (!m_isData){
    getEventWeight();
    for (auto ch: channels_){
      fillCutflow("cutflow_" + ch, "histogram_" + ch, kJSON, 1);
      fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCutsWeighted, b_genweight_);
    }
  }
  else{
    for (auto ch: channels_){
      fillCutflow("cutflow_" + ch, "histogram_" + ch, kJSON, 1);
      fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCutsWeighted, 1);
      Hist("runnumber", "histogram_mutau")->Fill(m_eventInfo.runNumber);
    }
    if(!(isGoodEvent(m_eventInfo.runNumber, m_eventInfo.lumiBlock))) throw SError( SError::SkipEvent );
  }
  
  
  // Cut 2: pass trigger
  //std::cout << ">>> ExecuteEvent - Cut 2" << std::endl;
  m_firedTriggers_mutau.clear();
  m_firedTriggers_etau.clear();
  m_firedTriggers_emu.clear();
  m_trigger_Flags = passTrigger(m_eventInfo.runNumber); //"mt22-et25";
  if(m_trigger_Flags != "none"){ m_logger << VERBOSE << "Trigger pass" << SLogger::endmsg; //std::cout << m_trigger_Flags << "\n" << std::endl; //
    for (auto trigger: m_firedTriggers_mutau){ 
           if(trigger->name=="HLT_IsoMu22_v"          ) Hist("triggers", "histogram_mutau")->Fill(1);
      else if(trigger->name=="HLT_IsoTkMu22_v"        ) Hist("triggers", "histogram_mutau")->Fill(2);
      else if(trigger->name=="HLT_IsoMu22_eta2p1_v"   ) Hist("triggers", "histogram_mutau")->Fill(3);
      else if(trigger->name=="HLT_IsoTkMu22_eta2p1_v" ) Hist("triggers", "histogram_mutau")->Fill(4);
      else if(trigger->name=="HLT_IsoMu19_eta2p1_LooseIsoPFTau20_SingleL1_v" ) Hist("triggers", "histogram_mutau")->Fill(5);
    }
    for (auto trigger: m_firedTriggers_etau){
           if(trigger->name=="HLT_Ele25_eta2p1_WPTight_Gsf_v"                   ) Hist("triggers", "histogram_etau")->Fill(1);
      else if(trigger->name=="HLT_Ele45_WPLoose_Gsf_L1JetTauSeeded"             ) Hist("triggers", "histogram_etau")->Fill(2);
      else if(trigger->name=="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_SingleL1_v" ) Hist("triggers", "histogram_etau")->Fill(3);
      else if(trigger->name=="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau20_v"   ) Hist("triggers", "histogram_etau")->Fill(4);
      else if(trigger->name=="HLT_Ele24_eta2p1_WPLoose_Gsf_LooseIsoPFTau30_v"   ) Hist("triggers", "histogram_etau")->Fill(5);
    }
  }
  else{
    Hist("triggers", "histogram_mutau")->Fill(0);
    throw SError( SError::SkipEvent );
  }
  
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
  //int lepton_N_pt23 = 0;
  //int lepton_N_2p4  = 0;
  //Hist("lepton_N", "histogram_mutau")->Fill(m_muon.N);
  for( int i = 0; i < m_muon.N; ++i ){
    UZH::Muon mymuon( &m_muon, i );
    
    if (mymuon.pt() < m_muonPtCut) continue;
    if (fabs(mymuon.eta()) > m_muonEtaCut_variable) continue;
    if (fabs(mymuon.d0_allvertices()) > m_muonD0Cut) continue;
    if (fabs(mymuon.dz_allvertices()) > m_muonDzCut) continue;
    if(m_isData and m_eventInfo.runNumber < 278820)
      {  if(mymuon.isMediumMuon()   < 0.5) continue; } // for period B-F
    else if(mymuon.isMediumMuonGH() < 0.5) continue;   // for period GH and MC (see AN)
    goodMuons.push_back(mymuon);
  }
  
  // Cut 4: lepton (electron)
  //std::cout << ">>> ExecuteEvent - Cut 4 - electron" << std::endl;
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
//     std::cout << ">>> passConversionVeto()=" << myelectron.passConversionVeto();
//     std::cout << ", expectedMissingInnerHits()=" << myelectron.expectedMissingInnerHits();
//     std::cout << ", isMVATightElectron()=" << myelectron.isMVATightElectron() << std::endl;
    if (myelectron.isMVATightElectron() < 0.5) continue;
    if (myelectron.passConversionVeto()!=1) continue;
    if (myelectron.expectedMissingInnerHits()>1) continue;
    //if (myelectron.SemileptonicPFIso() / myelectron.pt() > m_electronIsoCut) continue;
    
    goodElectrons.push_back(myelectron);
  }
  
  if(goodMuons.size()!=0){
    fillCutflow("cutflow_mutau", "histogram_mutau", kLepton, 1);
  }
  if(goodElectrons.size()!=0){
    fillCutflow("cutflow_etau", "histogram_etau", kLepton, 1);
  }
  else if(goodMuons.size()==0) throw SError( SError::SkipEvent );
  
  
  // Cut 5: lepton - tau pair
  
  // For tau
  //std::cout << ">>> ExecuteEvent - Cut 5 - tau" << std::endl;
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
    
    // TES corrections and shifts
    Float_t taupt = mytau.pt();
    Int_t genmatch_2 = -1;
    if(!m_isData) genMatch(mytau.eta(), mytau.phi());
    if(genmatch_2==5){
      //printRow({"tau & met","DM","tau.pt()","tau.eta()","tau.phi()","tau.e()","met.et()","met.phi()"});
      //printRow({"before"},{mytau.decayMode()},{mytau.pt(),mytau.eta(),mytau.phi(),mytau.e(),met.et(),met.phi()});
      TLorentzVector tau_tlv = mytau.tlv();
      TLorentzVector met_tlv;
      met_tlv.SetPxPyPzE(met.et()*TMath::Cos(met.phi()), met.phi()*TMath::Sin(met.phi()), 0, met.et());
      switch ( mytau.decayMode() ) {
        case  0: shiftLeptonAndMET(-0.018,tau_tlv,met_tlv,true); break; // 1 charged pion
        case  1: shiftLeptonAndMET( 0.010,tau_tlv,met_tlv,true); break; // 1 charged pion + 1 neutral pion
        case 10: shiftLeptonAndMET( 0.004,tau_tlv,met_tlv,true); break; // 3 charged pion
      }
      mytau.e(tau_tlv.E()); mytau.pt(tau_tlv.Pt()); taupt = mytau.pt();
      met.et(met_tlv.E());  met.phi(met_tlv.Pt());
      //printRow({"after"},{mytau.decayMode()},{mytau.pt(),mytau.eta(),mytau.phi(),mytau.e(),met.et(),met.phi()});
      if(m_doTES) taupt *= (1+m_TESshift);
    }
    else if(m_doLTF && genmatch_2<5){
        taupt *= (1+m_LTFshift);
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
  if(m_trigger_Flags.find("mt") != std::string::npos){
    for(int imuon=0; imuon < (int)goodMuons.size(); imuon++){
      for(int itau=0; itau < (int)goodTaus.size(); itau++){
        
        Float_t dR = goodMuons[imuon].tlv().DeltaR(goodTaus[itau].tlv());
        if(dR < 0.5) continue; // remove or lower for boosted ID
        
        // ADDED YUTA for TES studies (because otherwise too heavy
//         if(!( goodMuons[imuon].SemileptonicPFIso()/goodMuons[imuon].pt() < 0.15 && 
//               goodTaus[itau].byTightIsolationMVArun2v1DBoldDMwLT() > 0.5 && 
//               goodTaus[itau].againstElectronVLooseMVA6() > 0.5 && 
//               goodTaus[itau].againstMuonTight3() > 0.5                             )) continue;
        
        Float_t mupt = goodMuons[imuon].pt();
        Float_t reliso = goodMuons[imuon].SemileptonicPFIso() / mupt;
        Float_t taupt = goodTaus[itau].pt();
        
        if(m_doTES && goodTausGen[itau]==5) taupt *= (1+m_TESshift);
        if(m_doLTF && goodTausGen[itau]<5)  taupt *= (1+m_LTFshift);
        
        Float_t tauiso = goodTaus[itau].byIsolationMVArun2v1DBoldDMwLTraw();
        ltau_pair pair = {imuon, reliso, mupt, itau, tauiso, taupt, dR};
        mutau_pair.push_back(pair);
  }}}
  
  // For ele-tau
  //std::cout << ">>> ExecuteEvent - Cut 6 - etau" << std::endl;
  std::vector<ltau_pair> eletau_pair;
  if(m_trigger_Flags.find("et") != std::string::npos){
    for(int ielectron=0; ielectron < (int)goodElectrons.size(); ielectron++){
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
        
        Float_t reliso = goodElectrons[ielectron].relIsoWithDBeta(); //SemileptonicPFIso() / elept;
        Float_t tauiso = goodTaus[itau].byIsolationMVArun2v1DBoldDMwLTraw();
        
        ltau_pair pair = {ielectron, reliso, elept, itau, tauiso, taupt}; //, dR};
        eletau_pair.push_back(pair);
  }}}
  
  if(mutau_pair.size()==0 && eletau_pair.size()==0){
    throw SError( SError::SkipEvent );
  }
  
  
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
    
    // For Jets: cut and filter our selected muon and tau
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
    bool isolated = mutau_pair[0].lep_iso<0.15 and goodTaus[mutau_pair[0].itau].byTightIsolationMVArun2v1DBoldDMwLT()==1;
    fillCutflow("cutflow_mutau", "histogram_mutau", kTriggerMatched, 1);
    if(!m_isData and isolated){
      m_BTaggingScaleTool.fillEfficiencies(goodJetsAK4); // to measure b tag efficiencies for our selections
      m_BTaggingScaleTool.fillEfficiencies(goodJetsAK4,"mutau");
    }
    if(!m_doTight or isolated){
      FillBranches( "mutau", goodJetsAK4, goodTaus[mutau_pair[0].itau], genmatch_2, goodMuons[mutau_pair[0].ilepton], dummyElectron, met, puppiMet );//, MvaMet);
      mu_tau++;
    }
    // bool match = triggerMatches(m_firedTriggers_mutau, goodMuons[mutau_pair[0].ilepton].pt(), goodMuons[mutau_pair[0].ilepton].eta(), goodMuons[mutau_pair[0].ilepton].phi(),
    //                                                    goodTaus[mutau_pair[0].itau].pt(),    goodTaus[mutau_pair[0].itau].eta(),    goodTaus[mutau_pair[0].itau].phi()     );
  }
  
  
  // For ele-tau
  if(eletau_pair.size()!=0){
    fillCutflow("cutflow_etau", "histogram_etau", kLepTau, 1);
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
    
    // For Jets: cut and filter our selected muon and tau
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
    bool isolated = eletau_pair[0].lep_iso<0.15 and goodTaus[eletau_pair[0].itau].byTightIsolationMVArun2v1DBoldDMwLT()==1;
    fillCutflow("cutflow_etau", "histogram_etau", kTriggerMatched, 1);
    if(!m_isData and isolated){
      if(mutau_pair.size()==0) m_BTaggingScaleTool.fillEfficiencies(goodJetsAK4); // to measure b tag efficiencies for our selections
      m_BTaggingScaleTool.fillEfficiencies(goodJetsAK4,"etau");
    }
    if(!m_doTight or isolated){
      FillBranches( "etau", goodJetsAK4, goodTaus[eletau_pair[0].itau], genmatch_2, dummyMuon, goodElectrons[eletau_pair[0].ilepton], met, puppiMet );//, MvaMet);
      ele_tau++;
    }
    // bool match = triggerMatches(m_firedTriggers_etau, goodElectrons[eletau_pair[0].ilepton].pt(), goodElectrons[eletau_pair[0].ilepton].eta(), goodElectrons[eletau_pair[0].ilepton].phi(),
    //                                                   goodTaus[eletau_pair[0].itau].pt(),         goodTaus[eletau_pair[0].itau].eta(),         goodTaus[eletau_pair[0].itau].phi()          );
  }
      
  return;
  
}



bool TauTauAnalysis::isGoodEvent(int runNumber, int lumiSection) {
//   std::cout << "isGoodEvent" << std::endl;
  
  bool isGood = true;
  if (m_isData) {
    isGood = m_grl.HasRunLumiBlock( runNumber, lumiSection );
    //if( !isGood )
      //m_logger << WARNING << "Bad event! Run: " << runNumber <<  " - Lumi Section: " << lumiSection << SLogger::endmsg;
      //throw SError( SError::SkipEvent );
    //else m_logger << VERBOSE << "Good event! Run: " << runNumber <<  " - Lumi Section: " << lumiSection << SLogger::endmsg;
  }
  
  return isGood;
}





TString TauTauAnalysis::passTrigger(int runNumber) {
  //std::cout << "TauTauAnalysis::passTrigger" << std::endl;
  
  // triggerFlag = mt22-mt24-mtx-mt-et25-et45-etx-et-e12mu23-e23mu8-em-
  std::string triggerFlags = ""; // std::to_string(pt)
  for (std::map<std::string,bool>::iterator it = (m_eventInfo.trigDecision)->begin(); it != (m_eventInfo.trigDecision)->end(); ++it){
    if (it->second){ 
    
    // if ((it->first).find("Ele") != std::string::npos or (it->first).find("Mu") != std::string::npos)
    //  std::cout << it->first << " triggered " << std::endl;
    
      // mutau
      for( auto const& trigger: m_triggers_mutau ){
        if ((it->first).find(trigger->name) != std::string::npos){
          //if (it->second){  and (!m_isData or (trigger->start <= runNumber and runNumber <= trigger->end))){
          //std::cout << trigger->name << ": " << it->first << std::endl;
          m_firedTriggers_mutau.push_back(trigger);
          if(      trigger->name.find("Mu22") != std::string::npos and triggerFlags.find("mt22") == std::string::npos ){ triggerFlags += "mt22-"; }
          else if( trigger->name.find("Mu24") != std::string::npos and triggerFlags.find("mt24") == std::string::npos ){ triggerFlags += "mt24-"; }
          else if( trigger->name.find("Tau")  != std::string::npos and triggerFlags.find("mtx")  == std::string::npos ){ triggerFlags += "mtx-";  }     
      }}
    
      // etau
      for( auto const& trigger: m_triggers_etau ){
        if ((it->first).find(trigger->name) != std::string::npos){
          //if (it->second){ // and (!m_isData or (trigger->start <= runNumber and runNumber <= trigger->end))){
          //std::cout << trigger->name << ": " << it->first << std::endl;
          m_firedTriggers_etau.push_back(trigger);
          if(      trigger->name.find("Ele25") != std::string::npos and triggerFlags.find("et25") == std::string::npos ){ triggerFlags += "et25-"; }
          else if( trigger->name.find("Ele45") != std::string::npos and triggerFlags.find("et45") == std::string::npos ){ triggerFlags += "et45-"; }
          else if( trigger->name.find("Tau")   != std::string::npos and triggerFlags.find("etx")  == std::string::npos ){ triggerFlags += "etx-";  }
      }}
      
  }}
  
  if( triggerFlags == "" ) triggerFlags = "none";
  return triggerFlags;
  
}




bool TauTauAnalysis::triggerMatches(const std::vector<Trigger*> firedTriggers, const Float_t pt1, const Float_t eta1, const Float_t phi1, const Float_t pt2, const Float_t eta2, const Float_t phi2){
  //std::cout << "TauTauAnalysis::TrigMatch" << std::endl;
  //const UZH::Basic& lepton1, const UZH::Basic& lepton2
  
  //bool flag_match = false;
  for(auto const& trigger: firedTriggers){
    //std::cout << ">>> TauTauAnalysis::triggerMatches: " << trigger->name << std::endl;
    if(trigger->matchesTriggerObject(m_eventInfo, pt1, eta1, phi1, pt2, eta2, phi2)){
      //std::cout << ">>> TauTauAnalysis::triggerMatches: match with " << trigger->name << "!" << std::endl;
      return true;
    }
  }
  //std::cout << "matching -> " << flag_match << std::endl;
  return false;
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





void TauTauAnalysis::FillBranches(const std::string& channel, std::vector<UZH::Jet> &Jets,
                                  const UZH::Tau& tau, const int gen_match_2, const UZH::Muon& muon, const UZH::Electron& electron,
                                  const UZH::MissingEt& met, const UZH::MissingEt& puppimet){//, const UZH::MissingEt& mvamet){
//   std::cout << "FillBranches" << std::endl;
  
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
  
  Int_t njets       =  0;  Int_t njets20     =  0;
  Int_t nfjets      =  0;  Int_t nfjets20    =  0;
  Int_t ncjets      =  0;  Int_t ncjets20    =  0;
  Int_t nbtag       =  0;  Int_t nbtag20     =  0;
  Int_t nfbtag      =  0;  Int_t nfbtag20    =  0;
  Int_t ncbtag      =  0;  Int_t ncbtag20    =  0;

  Int_t ibjet1      = -1;
  Int_t ibjet2      = -1;
  Int_t icjet1      = -1; // central jet that is not the same as leading b jet for dphi_ll_bj
  Float_t ht        =  0; // total scalar energy HT
  
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Other_common_selections
  for( int ijet = 0; ijet < (int)Jets.size(); ++ijet ){ // already pT > 20 GeV jets
    ht += Jets.at(ijet).e();
    bool isBTagged = getBTagWeight_promote_demote(Jets.at(ijet)); // (Jets.at(ijet).csv()) > 0.8 // medium
    
    if(fabs(Jets.at(ijet).eta()) < 2.4 && isBTagged){
      nbtag++;
      if      (ibjet1 < 0) ibjet1 = ijet;
      else if (ibjet2 < 0) ibjet2 = ijet;
    }
    if(fabs(Jets.at(ijet).eta()) < 2.4){        // CENTRAL 20 GeV
      if(isBTagged) ncbtag20++;                 //  btag
      ncjets20++;                               //  jets
      if(icjet1 < 0 && (icjet1 != ibjet1 || ibjet1 < 0 )) icjet1 = ijet;
      if(Jets.at(ijet).pt() > 30){              // CENTRAL 30 GeV
        if(isBTagged) ncbtag++;                 //  btag
        ncjets++;                               //  jets
    }}
    else if(fabs(Jets.at(ijet).eta()) > 2.4){   // FORWARD 20 GeV
      if(isBTagged) nfbtag20++;                 //  btag
      nfjets20++;                               //  jets
      if(Jets.at(ijet).pt() > 30){              // FORWARD 30 GeV
        if(isBTagged) nfbtag++;                 //  btag
        nfjets++;                               //  jets
    }}
  }
  njets20 = ncjets20 + nfjets20;
  nbtag20 = ncbtag20 + nfbtag20;
  njets   = ncjets + nfjets;
  nbtag   = ncbtag + nfbtag;
  
  if(njets20 > 1){
    b_jpt_1[ch]     = Jets.at(0).pt();
    b_jeta_1[ch]    = Jets.at(0).eta();
    b_jphi_1[ch]    = Jets.at(0).phi();
    b_jpt_2[ch]     = Jets.at(1).pt();
    b_jeta_2[ch]    = Jets.at(1).eta();
    b_jphi_2[ch]    = Jets.at(1).phi();    
  }
  else if(njets20 == 1){
    b_jpt_1[ch]     = Jets.at(0).pt();
    b_jeta_1[ch]    = Jets.at(0).eta();
    b_jphi_1[ch]    = Jets.at(0).phi();
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
    b_vbf_mjj[ch]   = (Jets.at(0).tlv() + Jets.at(1).tlv()).M();
    b_vbf_deta[ch]  = Jets.at(0).eta() - Jets.at(1).eta();
    b_vbf_jdphi[ch] = deltaPhi(Jets.at(0).phi(), Jets.at(1).phi());
    Float_t min_eta = Jets.at(0).eta();
    Float_t max_eta = Jets.at(1).eta();
    if(min_eta > max_eta){
      min_eta = Jets.at(1).eta(); 
      max_eta = Jets.at(0).eta(); 
    }
    int ncentral    = 0;
    int ncentral20  = 0;
    for( int ijet = 0; ijet < (int)Jets.size(); ++ijet ){
      Float_t jeteta = Jets.at(ijet).eta();
      Float_t jetpt  = Jets.at(ijet).pt();
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
    b_bpt_1[ch]     = Jets.at(ibjet1).pt();
    b_beta_1[ch]    = Jets.at(ibjet1).eta();
    b_bphi_1[ch]    = Jets.at(ibjet1).phi();
    b_bcsv_1[ch]    = Jets.at(ibjet1).csv();
  }
  if (ibjet2 < 0){
    b_bpt_2[ch]     = -1;
    b_beta_2[ch]    = -9;
    b_bphi_2[ch]    = -9;
    b_bcsv_2[ch]    = -1;
  }
  else{
    b_bpt_2[ch]     = Jets.at(ibjet2).pt();
    b_beta_2[ch]    = Jets.at(ibjet2).eta();
    b_bphi_2[ch]    = Jets.at(ibjet2).phi();
    b_bcsv_2[ch]    = Jets.at(ibjet2).csv();
  }
  
  b_njets[ch]       = njets;    b_njets20[ch]     = njets20;
  b_nfjets[ch]      = nfjets;   b_nfjets20[ch]    = nfjets20;
  b_ncjets[ch]      = ncjets;   b_ncjets20[ch]    = ncjets20;
  b_nbtag[ch]       = nbtag;    b_nbtag20[ch]     = nbtag20;
  b_ncbtag[ch]      = ncbtag;   b_ncbtag20[ch]    = ncbtag20;
  
  
  
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
  b_decayMode_2[ch]                     = tau.decayMode(); // 0, 1, 10
  
  b_id_e_mva_nt_loose_1[ch]             = -1;
  extraLeptonVetos(channel, muon, electron); // sets global b_dilepton_veto_, b_extraelec_veto_, b_extramuon_veto_
  b_dilepton_veto[ch]                   = b_dilepton_veto_;
  b_extraelec_veto[ch]                  = b_extraelec_veto_;
  b_extramuon_veto[ch]                  = b_extramuon_veto_;
  b_lepton_vetos[ch]                    = ( b_dilepton_veto_ or b_extraelec_veto_ or b_extramuon_veto_ );
  
  
  
  ///////////////////
  // MARK: Leptons //
  ///////////////////
  
  b_idisoweight_1[ch]       = 1.;
  b_trigweight_1[ch]        = 1.;
  b_trigweight_or_1[ch]     = 1.;
  b_trigweight_2[ch]        = 1.;
  b_triggers[ch]            = 0.;
  
  TLorentzVector lep_tlv;
  if(channel=="mutau"){
    b_channel[ch]           = 1;
    b_pt_1[ch]              = muon.tlv().Pt();
    b_eta_1[ch]             = muon.tlv().Eta();
    b_phi_1[ch]             = muon.tlv().Phi();
    b_m_1[ch]               = muon.tlv().M();
    b_q_1[ch]               = muon.charge();
    b_d0_1[ch]              = muon.d0();
    b_dz_1[ch]              = muon.dz();
    b_iso_1[ch]             = muon.SemileptonicPFIso() / muon.pt();
    b_iso_cuts[ch]          = ( b_iso_1[ch]<0.15 and b_iso_2[ch]==1 );
    b_lepton_vetos[ch]      = ( b_lepton_vetos[ch]==1 or tau.againstElectronVLooseMVA6()<0.5 or tau.againstMuonTight3()<0.5 ); // veto if againstLepton == 0
    lep_tlv.SetPtEtaPhiM(b_pt_1[ch], b_eta_1[ch], b_phi_1[ch], b_m_1[ch]);
    b_triggers[ch]          = 1*(m_trigger_Flags.find("mt2")!=std::string::npos) +
                              2*(m_trigger_Flags.find("mtx")!=std::string::npos);
    b_trigger_cuts[ch]      = abs(b_eta_1[ch])<2.1 and ( (b_pt_1[ch]> 23 and (m_trigger_Flags.find("mt2")!=std::string::npos))
                                                      or (b_pt_1[ch]<=23 and  b_triggers[ch]>1) );
    if(!m_isData){
      b_trigweight_1[ch]    = m_ScaleFactorTool.get_ScaleFactor_Mu22Trig( b_pt_1[ch],fabs(b_eta_1[ch]));//,b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],m_trigger_Flags);
      b_trigweight_2[ch]    = m_ScaleFactorTool.get_ScaleFactor_MuTauTrig(b_pt_1[ch],fabs(b_eta_1[ch]),b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],gen_match_2,m_trigger_Flags);
      b_trigweight_or_1[ch] = m_ScaleFactorTool.get_ScaleFactor_MuTauTrig_OR(b_pt_1[ch],fabs(b_eta_1[ch]),b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],gen_match_2,m_trigger_Flags);
      b_idisoweight_1[ch]   = m_ScaleFactorTool.get_ScaleFactor_MuIdIso(  b_pt_1[ch],fabs(b_eta_1[ch]));
    }
  }
  else{
    b_channel[ch]           = 2;
    b_pt_1[ch]              = electron.tlv().Pt();
    b_eta_1[ch]             = electron.tlv().Eta();
    b_phi_1[ch]             = electron.tlv().Phi();
    b_m_1[ch]               = electron.tlv().M();
    b_q_1[ch]               = electron.charge();
    b_d0_1[ch]              = electron.d0();
    b_dz_1[ch]              = electron.dz();
    b_id_e_mva_nt_loose_1[ch] = electron.isMVATightElectron(); // Moriond
    b_iso_1[ch]             = electron.relIsoWithDBeta();
    b_iso_cuts[ch]          = ( b_iso_1[ch]<0.10 and b_iso_2[ch]==1 );
    b_lepton_vetos[ch]      = ( b_lepton_vetos[ch] or tau.againstElectronTightMVA6() < 0.5 or tau.againstMuonLoose3() < 0.5 );
    lep_tlv.SetPtEtaPhiM(b_pt_1[ch], b_eta_1[ch], b_phi_1[ch], b_m_1[ch]);
    b_triggers[ch]          = 1*(m_trigger_Flags.find("et2")!=std::string::npos or m_trigger_Flags.find("et4")!=std::string::npos) +
                              2*(m_trigger_Flags.find("etx")!=std::string::npos);
    b_trigger_cuts[ch]      = abs(b_eta_1[ch])<2.1 and ( (b_pt_1[ch]> 26 and (b_triggers[ch]==1 or b_triggers[ch]==3))
                                                      or (b_pt_1[ch]<=26 and  b_triggers[ch]>1) );
    if(!m_isData){
      b_trigweight_1[ch]    = m_ScaleFactorTool.get_ScaleFactor_EleTrig(   b_pt_1[ch],fabs(b_eta_1[ch]));//,b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],m_trigger_Flags);
      b_trigweight_2[ch]    = m_ScaleFactorTool.get_ScaleFactor_EleTauTrig(b_pt_1[ch],fabs(b_eta_1[ch]),b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],gen_match_2,m_trigger_Flags);
      b_trigweight_or_1[ch] = m_ScaleFactorTool.get_ScaleFactor_EleTauTrig_OR(b_pt_1[ch],fabs(b_eta_1[ch]),b_pt_2[ch],fabs(b_eta_2[ch]),b_decayMode_2[ch],gen_match_2,m_trigger_Flags);
      b_idisoweight_1[ch]   = m_ScaleFactorTool.get_ScaleFactor_EleIdIso(  b_pt_1[ch],fabs(b_eta_1[ch]));
    }
  }
  
  
  ///////////////////////
  // MARK: Reweighting //
  ///////////////////////
  
  b_idisoweight_2[ch]                   = 1.;
  //b_trigweight_2[ch]                    = 1.;
  b_zptweight[ch]                       = 1.;
  b_ttptweight[ch]                      = 1.;
  b_weightbtag[ch]                      = 1.;
  b_gen_match_1[ch]                     = -1;
  b_gen_match_2[ch]                     = gen_match_2;
  
  if (!m_isData){
    b_gen_match_1[ch]                   = genMatch(b_eta_1[ch], b_phi_1[ch]);
    b_idisoweight_2[ch]                 = genMatchSF(channel, gen_match_2, b_eta_2[ch]); // leptons faking taus and real taus ID eff
    if(m_doZpt)  b_zptweight[ch]        = m_RecoilCorrector.ZptWeight( boson_tlv.M(), boson_tlv.Pt() );
    if(m_doTTpt) b_ttptweight[ch]       = genMatchSF(channel, -36); // 6*-6 = -36
    b_weightbtag[ch]                    = b_weightbtag_; // do not apply b tag weight when using promote-demote method !!!
    //b_weightbtag[ch]                  = m_BTaggingScaleTool.getScaleFactor_veto(Jets); // getScaleFactor_veto for AK4, getScaleFactor for AK8
    b_weight[ch] *= b_idisoweight_1[ch] * b_idisoweight_2[ch] * b_zptweight[ch] * b_ttptweight[ch]; // * b_trigweight_2[ch] * b_weightbtag[ch]
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
  float fmet      = met.et();        float fmetphi      = met.phi();
  float fpuppimet = puppimet.et();   float fpuppimetphi = puppimet.phi();
  met_tlv.SetPxPyPzE(fmet*TMath::Cos(fmetphi), fmet*TMath::Sin(fmetphi), 0, fmet);
  TLorentzVector met_tlv_corrected;
  if(m_doRecoilCorr){
    met_tlv_corrected    = m_RecoilCorrector.CorrectPFMETByMeanResolution(  met_tlv.Px(),       met_tlv.Py(),
                                                                            boson_tlv.Px(),     boson_tlv.Py(),
                                                                            boson_tlv_vis.Px(), boson_tlv_vis.Py(),
                                                                            m_jetAK4.N ); //m_eventInfo.lheNj
    // mvamet_tlv_corrected = m_RecoilCorrector.CorrectMVAMETByMeanResolution( mvamet_tlv.Px(),   mvamet_tlv.Py(),
    //                                                                         boson_tlv.Px(),     boson_tlv.Py(),
    //                                                                         boson_tlv_vis.Px(), boson_tlv_vis.Py(),
    //                                                                         m_jetAK4.N ); //m_eventInfo.lheNj
    fmet    = met_tlv_corrected.E();         fmetphi = met_tlv_corrected.Phi();
    b_m_genboson[ch]  = boson_tlv.M();
    b_pt_genboson[ch] = boson_tlv.Pt();
  }else{
    met_tlv_corrected    = met_tlv;
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
  
  if(!m_isData){
    //std::cout << ">>> before: tau pt = " << tau_tlv.Pt()  << ", m   = " << tau_tlv.M() << std::endl;
    //std::cout << ">>> before: lep pt = " << lep_tlv.Pt()  << ", m   = " << lep_tlv.M() << std::endl;
    //std::cout << ">>> before: met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    if(m_doTES && gen_match_2==5){ // TES
      // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016#Tau_Energy_Scale_TES
      shiftLeptonAndMET(m_TESshift,tau_tlv,met_tlv_corrected);
      b_pt_2[ch]    = tau_tlv.Pt();
      b_m_2[ch]     = tau_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
    }
    if(m_doLTF && gen_match_2<5){ // Lepton to tau fake (LTF)
      // https://twiki.cern.ch/twiki/bin/viewauth/CMS/SMTauTau2016#Electron_to_Tau_Fake
      shiftLeptonAndMET(m_LTFshift,tau_tlv,met_tlv_corrected);
      b_pt_2[ch]    = tau_tlv.Pt();
      b_m_2[ch]     = tau_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
    }
    if(m_doEES && channel=="etau"){ // Electron Energy Scale
      if(fabs(electron.tlv().Eta())<1.479) shiftLeptonAndMET(m_EESshift,      lep_tlv,met_tlv_corrected);
      else                                 shiftLeptonAndMET(m_EESshiftEndCap,lep_tlv,met_tlv_corrected);
      b_pt_1[ch]    = lep_tlv.Pt();
      b_m_1[ch]     = lep_tlv.M();
      fmet          = met_tlv_corrected.E();
      fmetphi       = met_tlv_corrected.Phi();
    }
    //std::cout << ">>> after:  tau pt = " << tau_tlv.Pt()  << ", m   = " << tau_tlv.M() << std::endl;
    //std::cout << ">>> after:  lep pt = " << lep_tlv.Pt()  << ", m   = " << lep_tlv.M() << std::endl;      
    //std::cout << ">>> after:  met    = " << met_tlv_corrected.E() << ", phi = " << met_tlv_corrected.Phi() << std::endl;
    //std::cout << ">>> " << std::endl;
  }
  
  if (m_doJEC){
    
    b_weightbtag_bcUp[ch]     = m_BTaggingScaleTool.getScaleFactor(Jets,+1., 0.);
    b_weightbtag_bcDown[ch]   = m_BTaggingScaleTool.getScaleFactor(Jets,-1., 0.);
    b_weightbtag_udsgUp[ch]   = m_BTaggingScaleTool.getScaleFactor(Jets, 0.,+1.);
    b_weightbtag_udsgDown[ch] = m_BTaggingScaleTool.getScaleFactor(Jets, 0.,-1.);
    
    // double b_weightbtag_bcUp_     = m_BTaggingScaleTool.getScaleFactor(Jets,+1., 0.);
    // double b_weightbtag_bcDown_   = m_BTaggingScaleTool.getScaleFactor(Jets,-1., 0.);
    // double b_weightbtag_udsgUp_   = m_BTaggingScaleTool.getScaleFactor(Jets, 0.,+1.);
    // double b_weightbtag_udsgDown_ = m_BTaggingScaleTool.getScaleFactor(Jets, 0.,-1.);
    // TString tch = ch;
    // if(b_iso_cuts[ch]==1 and b_lepton_vetos[ch]==0){
    //   Hist("btagweight", "histogram_"+tch)->Fill( 0., b_weightbtag_          );
    //   Hist("btagweight", "histogram_"+tch)->Fill( 1., b_weightbtag_bcUp_     );
    //   Hist("btagweight", "histogram_"+tch)->Fill( 2., b_weightbtag_bcDown_   );
    //   Hist("btagweight", "histogram_"+tch)->Fill( 3., b_weightbtag_udsgUp_   );
    //   Hist("btagweight", "histogram_"+tch)->Fill( 4., b_weightbtag_udsgDown_ );
    // }
    
    if(Jets.size()>0) // njets
        FillBranches_JEC( ch, Jets, (lep_tlv+tau_tlv).Phi() );
    
    // no need to substract shifts from met, use shifts available in ntuple instead:
    TLorentzVector met_jesUp, met_jesDown, met_jer, met_jerUp, met_jerDown, met_UncEnUp, met_UncEnDown;
    met_jesUp.SetPtEtaPhiE(    met.et()*met.JetEnUp(),          0.,met.phi(),met.et()*met.JetEnUp());
    met_jesDown.SetPtEtaPhiE(  met.et()*met.JetEnDown(),        0.,met.phi(),met.et()*met.JetEnDown());
    met_jer.SetPtEtaPhiE(      met.et(),                        0.,met.phi(),met.et());
    met_jerUp.SetPtEtaPhiE(    met.et()*met.JetResUp(),         0.,met.phi(),met.et()*met.JetResUp());
    met_jerDown.SetPtEtaPhiE(  met.et()*met.JetResDown(),       0.,met.phi(),met.et()*met.JetResDown());
    met_UncEnUp.SetPtEtaPhiE(  met.et()*met.UnclusteredEnUp(),  0.,met.phi(),met.et()*met.UnclusteredEnUp());
    met_UncEnDown.SetPtEtaPhiE(met.et()*met.UnclusteredEnDown(),0.,met.phi(),met.et()*met.UnclusteredEnDown());
    //printRow({"met","jer","jerUp","jerDown","jesUp","jesDown"});
    //printRow({},{},{met.et(),met_jer.Pt(),met_jerUp.Pt(),met_jerDown.Pt(),met_jesUp.Pt(),met_jesDown.Pt()});  
    
    b_met_jesUp[ch]           = met_jesUp.Et();
    b_met_jesDown[ch]         = met_jesDown.Et();
    b_met_jer[ch]             = met_jer.Et();
    b_met_jerUp[ch]           = met_jerUp.Et();
    b_met_jerDown[ch]         = met_jerDown.Et();
    b_met_UncEnUp[ch]         = met_UncEnUp.Et();
    b_met_UncEnDown[ch]       = met_UncEnDown.Et();
    
    b_pfmt_1_jesUp[ch]        = TMath::Sqrt( 2*lep_tlv.Pt()*met_jesUp.Et()    *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_jesUp.Phi()     ))));
    b_pfmt_1_jesDown[ch]      = TMath::Sqrt( 2*lep_tlv.Pt()*met_jesDown.Et()  *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_jesDown.Phi()   ))));
    b_pfmt_1_jer[ch]          = TMath::Sqrt( 2*lep_tlv.Pt()*met_jer.Et()      *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_jer.Phi()       ))));
    b_pfmt_1_jerUp[ch]        = TMath::Sqrt( 2*lep_tlv.Pt()*met_jerUp.Et()    *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_jerUp.Phi()     ))));
    b_pfmt_1_jerDown[ch]      = TMath::Sqrt( 2*lep_tlv.Pt()*met_jerDown.Et()  *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_jerDown.Phi()   ))));
    b_pfmt_1_UncEnUp[ch]      = TMath::Sqrt( 2*lep_tlv.Pt()*met_UncEnUp.Et()  *( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_UncEnUp.Phi()   ))));
    b_pfmt_1_UncEnDown[ch]    = TMath::Sqrt( 2*lep_tlv.Pt()*met_UncEnDown.Et()*( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(),met_UncEnDown.Phi() ))));
  }
  
  b_met[ch]         = fmet;
  b_metphi[ch]      = fmetphi;
  b_puppimet[ch]    = fpuppimet;
  b_puppimetphi[ch] = fpuppimetphi;
  b_met_old[ch]     = met.et();
  
  b_metcov00[ch]    = met.cov00();
  b_metcov01[ch]    = met.cov10(); // not a typo. This is same for 10
  b_metcov10[ch]    = met.cov10();
  b_metcov11[ch]    = met.cov11();
  
  b_pfmt_1[ch]      = TMath::Sqrt(2*lep_tlv.Pt()*fmet*(      1-TMath::Cos(deltaPhi(lep_tlv.Phi(), fmetphi     ))));
  b_puppimt_1[ch]   = TMath::Sqrt(2*lep_tlv.Pt()*fpuppimet*( 1-TMath::Cos(deltaPhi(lep_tlv.Phi(), fpuppimetphi))));
  
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
  b_mt_tot[ch]      = TMath::Sqrt(TMath::Power(b_pfmt_1[ch],2) + TMath::Power(b_pfmt_2[ch],2) + 2*lep_tlv.Pt()*b_pt_2[ch]*(1-TMath::Cos(deltaPhi(lep_tlv.Phi(), b_phi_2[ch]))));
  b_ht[ch]          = ht + lep_tlv.E() + tau_tlv.E();
  
  // Delta phi( lep+tau, bj+j ) if there is one central b jet and on central jet
  // icjet1 = index of central jet that is not the same as leading b jet
  if(icjet1 != -1 && ibjet1 != -1)
    b_dphi_ll_bj[ch] = fabs(deltaPhi( (lep_tlv+tau_tlv).Phi(), (Jets.at(ibjet1).tlv()+Jets.at(icjet1).tlv()).Phi() ));
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
  bool doSVFit = m_doSVFit && b_iso_cuts[ch]==1 && b_lepton_vetos[ch]==0; //&& b_iso_1[ch]<0.30 && b_iso_2_medium[ch]==1 && b_lepton_vetos[ch]==0;
  if(m_doTight) doSVFit = doSVFit && ncbtag>0 && b_iso_1[ch]<0.15 && b_iso_2[ch]==1;
  //bool doSVfit= false;
    
  double m_sv = -1;
  double pt_tt_sv = -1;
  double R_pt_m_sv = -1;
  if ( doSVFit ){
    //std::cout << ">>> SVFit...";
    m_SVFitTool.addMeasuredLeptonTau(channel,lep_tlv, tau_tlv, tau.decayMode());
    m_SVFitTool.getSVFitMassAndPT(m_sv,pt_tt_sv,met_tlv_corrected.Px(),met_tlv_corrected.Py(),met.cov00(),met.cov10(),met.cov11());
    if(m_sv > 0) R_pt_m_sv = pt_tt_sv/m_sv;
    //std::cout << " done" << std::endl;
  }
  b_m_sv[ch]        = m_sv;
  b_pt_tt_sv[ch]    = pt_tt_sv;
  b_R_pt_m_sv[ch]   = R_pt_m_sv;
  
}



void TauTauAnalysis::FillBranches_JEC( const char* ch, const std::vector<UZH::Jet>& Jets, const float phi_ll ){ //const UZH::MissingEt& met, const TLorentzVector& lep_tlv,
  //std::cout << "FillBranches_JEC " << ch << std::endl;
  // TODO: use jet_jer as main jets
  
  Int_t nfjets_jer     = 0;  Int_t ncjets_jer     = 0;  Int_t ncbtag_jer     = 0;
  Int_t nfjets_jerUp   = 0;  Int_t ncjets_jerUp   = 0;  Int_t ncbtag_jerUp   = 0;
  Int_t nfjets_jerDown = 0;  Int_t ncjets_jerDown = 0;  Int_t ncbtag_jerDown = 0;
  Int_t nfjets_jesUp   = 0;  Int_t ncjets_jesUp   = 0;  Int_t ncbtag_jesUp   = 0;
  Int_t nfjets_jesDown = 0;  Int_t ncjets_jesDown = 0;  Int_t ncbtag_jesDown = 0;
  
  // for dphi_ll_bj: get two leading central jets, on of which b tagged
  TLorentzVector bjet_jesUp,   jet2_jesUp;
  TLorentzVector bjet_jesDown, jet2_jesDown;
  TLorentzVector bjet_jer,     jet2_jer;
  TLorentzVector bjet_jerUp,   jet2_jerUp;
  TLorentzVector bjet_jerDown, jet2_jerDown;
  
  //printRow({"ijet","jet pt","jer","jerUp","jerDown","jesUp","jesDown"});
  for( int ijet = 0; ijet < (int)Jets.size(); ++ijet ){ // already pT > 20 GeV jets
      UZH::Jet jet = Jets.at(ijet);
      
      std::vector<TLorentzVector> jets_jes = m_JetCorrectionTool.GetCorrectedJet(jet);
      std::vector<TLorentzVector> jets_jer = m_JetCorrectionTool.GetCorrectedJetJER(jet,m_genJetAK4);
      
      TLorentzVector jet_jer(jets_jer.at(0)), jet_jerUp(jets_jer.at(1)), jet_jerDown(jets_jer.at(2)),
                                              jet_jesUp(jets_jes.at(0)), jet_jesDown(jets_jes.at(1));
      
      //printRow({},{ijet},{jet.pt(),jet_jer.Pt(),jet_jerUp.Pt(),jet_jerDown.Pt(),jet_jesUp.Pt(),jet_jesDown.Pt()});
      bool isBTagged = jet.isTagged(); // tagged in promote-demote
      
      // count jets
      countJets( jet_jesUp,   ncjets_jesUp,   nfjets_jesUp,   ncbtag_jesUp,   bjet_jesUp,   jet2_jesUp,   isBTagged );
      countJets( jet_jesDown, ncjets_jesDown, nfjets_jesDown, ncbtag_jesDown, bjet_jesDown, jet2_jesDown, isBTagged );
      countJets( jet_jer,     ncjets_jer,     nfjets_jer,     ncbtag_jer,     bjet_jer,     jet2_jer,     isBTagged );
      countJets( jet_jerUp,   ncjets_jerUp,   nfjets_jerUp,   ncbtag_jerUp,   bjet_jerUp,   jet2_jerUp,   isBTagged );
      countJets( jet_jerDown, ncjets_jerDown, nfjets_jerDown, ncbtag_jerDown, bjet_jerDown, jet2_jerDown, isBTagged );
  }
  
  //printRow({" ","jer","jerUp","jerDown","jesUp","jesDown"});
  //printRow({"ncjets"},{ncjets_jer,ncjets_jerUp,ncjets_jerDown,ncjets_jesUp,ncjets_jesDown});
  //printRow({"nfjets"},{nfjets_jer,nfjets_jerUp,nfjets_jerDown,nfjets_jesUp,nfjets_jesDown});
  //printRow({"ncbtag"},{ncbtag_jer,ncbtag_jerUp,ncbtag_jerDown,ncbtag_jesUp,ncbtag_jesDown});
  
  b_nfjets_jesUp[ch]   = nfjets_jesUp;      b_ncjets_jesUp[ch]   = ncjets_jesUp;     b_ncbtag_jesUp[ch]   = ncbtag_jesUp;  
  b_nfjets_jesDown[ch] = nfjets_jesDown;    b_ncjets_jesDown[ch] = ncjets_jesDown;   b_ncbtag_jesDown[ch] = ncbtag_jesDown;
  b_nfjets_jer[ch]     = nfjets_jer;        b_ncjets_jer[ch]     = ncjets_jer;       b_ncbtag_jer[ch]     = ncbtag_jer;    
  b_nfjets_jerUp[ch]   = nfjets_jerUp;      b_ncjets_jerUp[ch]   = ncjets_jerUp;     b_ncbtag_jerUp[ch]   = ncbtag_jerUp;  
  b_nfjets_jerDown[ch] = nfjets_jerDown;    b_ncjets_jerDown[ch] = ncjets_jerDown;   b_ncbtag_jerDown[ch] = ncbtag_jerDown;
  
  b_dphi_ll_bj_jesUp[ch]    = fabs(deltaPhi( phi_ll, (bjet_jesUp  +jet2_jesUp  ).Phi() ));
  b_dphi_ll_bj_jesDown[ch]  = fabs(deltaPhi( phi_ll, (bjet_jesDown+jet2_jesDown).Phi() ));
  b_dphi_ll_bj_jer[ch]      = fabs(deltaPhi( phi_ll, (bjet_jer    +jet2_jer    ).Phi() ));
  b_dphi_ll_bj_jerUp[ch]    = fabs(deltaPhi( phi_ll, (bjet_jerUp  +jet2_jerUp  ).Phi() ));
  b_dphi_ll_bj_jerDown[ch]  = fabs(deltaPhi( phi_ll, (bjet_jerDown+jet2_jerDown).Phi() ));
  
}





void TauTauAnalysis::countJets(const TLorentzVector& jet_tlv, Int_t& ncjets, Int_t& nfjets, Int_t& ncbtags, TLorentzVector& bjet_tlv, TLorentzVector& jet2_tlv, const bool isBTagged){ //, const int ijet , Int_t& icjet1, Int_t& ibjet1
  //std::cout << "countJets" << std::endl;
  if(jet_tlv.Pt()<30) return;
  Float_t abseta = fabs(jet_tlv.Eta());
  if(abseta < 2.4){         // CENTRAL 30 GeV
    if(isBTagged) ncbtags++;
    ncjets++;
    if(bjet_tlv.Pt()<30 and isBTagged)  bjet_tlv.SetPtEtaPhiM(jet_tlv.Pt(),jet_tlv.Eta(),jet_tlv.Phi(),jet_tlv.M());
    else if(jet2_tlv.Pt()<30)           jet2_tlv.SetPtEtaPhiM(jet_tlv.Pt(),jet_tlv.Eta(),jet_tlv.Phi(),jet_tlv.M());
  }
  else if(abseta > 2.4){    // FORWARD 30 GeV
    nfjets++;
  }
}





void TauTauAnalysis::genFilterZtautau(){
  //std::cout << "genFilterZtautau" << std::endl;
    
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    
    if( fabs(mygoodGenPart.pdgId())==15 ){
      if( mygoodGenPart.mother()[0]==25 ){ GenEvent_Htata_filter = true; }
      if( mygoodGenPart.mother()[0]==23 ){ GenEvent_Ztata_filter = true; }
    } 
  }
}





void TauTauAnalysis::setGenBosonTLVs(){
//   std::cout << "setGenBosonTLVs" << std::endl;
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





double TauTauAnalysis::getGenBosonPt(){
//   std::cout << "getGenBosonPt" << std::endl;
  
  double pt = -1;
  for ( int p = 0; p < (m_genParticle.N); ++p ) {
    UZH::GenParticle mygoodGenPart( &m_genParticle, p );
    if( fabs(mygoodGenPart.pdgId()) == 23 and mygoodGenPart.pt() > 0 ){
        return mygoodGenPart.pt();
    }
  }
  
  return pt;
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
  
  for ( int itau = 0; itau < (int)m_genParticle.tauvispt->size(); ++itau ) {
    Float_t dr = deltaR(lep_eta - m_genParticle.tauviseta->at(itau),
			deltaPhi(lep_phi, m_genParticle.tauvisphi->at(itau)));
    if(dr < min_dR){
      min_dR = dr;
      id = 5;
    }    
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





void TauTauAnalysis::printRow(const std::vector<std::string> svec, const std::vector<int> ivec, const std::vector<double> dvec, const std::vector<float> fvec, const int w){
    for(auto const& el: svec) std::cout << std::setw(w) << el;
    for(auto const& el: ivec) std::cout << std::setw(w) << el;
    for(auto const& el: fvec) std::cout << std::setw(w) << el;
    for(auto const& el: dvec) std::cout << std::setw(w) << el;
    std::cout << std::endl;
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
  //                        https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeVMoriond17#Muon_to_tau_fake_rate (Moriond)
  //                        https://twiki.cern.ch/twiki/bin/view/CMS/TauIDRecommendation13TeV#Muon_to_tau_fake_rate (Moriond - better?)
  // tau reweighting:       old: https://indico.cern.ch/event/563239/contributions/2279020/attachments/1325496/1989607/lepTauFR_tauIDmeeting_20160822.pdf
  //                        new: https://indico.cern.ch/event/566825/contributions/2398691/attachments/1385164/2107478/HIG-16-043-preapproval-rehearsal.pdf#page=14
  //                             http://cms.cern.ch/iCMS/jsp/db_notes/noteInfo.jsp?cmsnoteid=CMS%20AN-2016/355
  //                             https://twiki.cern.ch/twiki/bin/viewauth/CMS/TauIDRecommendation13TeVMoriond17#Muon_to_tau_fake_rate
  // top pt reweighting:    https://twiki.cern.ch/twiki/bin/view/CMS/MSSMAHTauTauEarlyRun2#Top_quark_pT_reweighting
  //                        new? https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting#MC_SFs_Reweighting
  //
  // mutau: againstElectronVLooseMVA6 againstMuonTight3
  // etau:  againstElectronTightMVA6  againstMuonLoose3

  
  float eta = fabs(tau_eta);
  
  // electron -> tau
  if      (genmatch_2 == 3) {
    if (channel=="mutau"){       // for VLoose
        if      ( eta < 1.460 ) return 1.213;
        else if ( eta > 1.558 ) return 1.375;
    }
    else if (channel=="etau"){ // for Tight
        if      ( eta < 1.460 ) return 1.40;
        else if ( eta > 1.558 ) return 1.90;
    }
  }
  // muon -> tau
  else if (genmatch_2 == 4) {
    if (channel=="etau"){      // for Loose
        if      ( eta < 0.4 ) return 1.012;
        else if ( eta < 0.8 ) return 1.007;
        else if ( eta < 1.2 ) return 0.870;
        else if ( eta < 1.7 ) return 1.154;
        else                  return 2.281;
    }
    else if (channel=="mutau"){  // for Tight
        if      ( eta < 0.4 ) return 1.263;
        else if ( eta < 0.8 ) return 1.364;
        else if ( eta < 1.2 ) return 0.854;
        else if ( eta < 1.7 ) return 1.712;
        else                  return 2.324;
    }
  }
  // real tau
  else if (genmatch_2 == 5) {
    return 0.95;
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
    if(qq==-36){
      const char* ch = channel.c_str();
      b_pt_top_1[ch] = pt_top_1;
      b_pt_top_2[ch] = pt_top_2;
      b_ttptweight_runI[ch] = TMath::Sqrt(TMath::Exp(0.156-0.00137*TMath::Min(pt_top_1,400.0))*TMath::Exp(0.156-0.00137*TMath::Min(pt_top_2,400.0)));
      return TMath::Sqrt(TMath::Exp(0.0615-0.0005*TMath::Min(pt_top_1,400.0))*TMath::Exp(0.0615-0.0005*TMath::Min(pt_top_2,400.0)));
    }else{
      std::cout << ">>> TauTauAnalysis::genMatchSF: genmatch_2 = 66, qq = " << qq << " != -36 !!!" << std::endl;
    }
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
    
    // dilepton veto: match with other muons
    if( mymuon.pt() > 15 && mymuon.isGlobalMuon()
                         && mymuon.isTrackerMuon() 
                         && mymuon.isPFMuon() ){
      passedMuons.push_back(mymuon);
    }
    
    // extra muon veto
    if(m_isData and m_eventInfo.runNumber < 278820)
      {  if(mymuon.isMediumMuon()   < 0.5) continue; } // for period B-F
    else if(mymuon.isMediumMuonGH() < 0.5) continue;   // for period GH and MC (see AN)
    if(mymuon.pt()!=muon.pt() and mymuon.eta()!=muon.eta() and mymuon.phi()!=muon.phi()){
      b_extramuon_veto_ = true;
    }
  }
  
  std::vector<UZH::Electron> passedElectrons;
  for( int i = 0; i < m_electron.N; ++i ){
    UZH::Electron myelectron( &m_electron, i );
    
    if(myelectron.pt() < 10) continue;
    if(fabs(myelectron.eta()) > 2.5) continue;
    if(fabs(myelectron.dz_allvertices()) > 0.2) continue;
    if(fabs(myelectron.d0_allvertices()) > 0.045) continue;
    if(myelectron.relIsoWithDBeta() > 0.3) continue; //SemileptonicPFIso() / myelectron.pt()
    if(!myelectron.isMVATightElectron()) continue; // Moriond //isMVAMediumElectron
    
    // dilepton veto: match with other muons
    if(myelectron.pt() > 15 && myelectron.isMVATightElectron())
      passedElectrons.push_back(myelectron);
    
    // extra electron veto
    if(myelectron.passConversionVeto() &&
       myelectron.isMVATightElectron() && 
       myelectron.expectedMissingInnerHits() <= 1){
      if( myelectron.pt() != electron.pt() && myelectron.eta() != electron.eta() && myelectron.phi() != electron.phi())
        b_extraelec_veto_ = true;
    }
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
  else if(channel=="etau"){
    for(int ielectron = 0; ielectron < (int)passedElectrons.size(); ielectron++){
      for(int jelectron = 0; jelectron < ielectron; jelectron++){
        //if(ielectron < jelectron) continue;
        if(passedElectrons[ielectron].charge() * passedElectrons[jelectron].charge() < 0 &&
           passedElectrons[ielectron].tlv().DeltaR(passedElectrons[jelectron].tlv()) > 0.15)
          b_dilepton_veto_ = true;
  }}}
}





bool TauTauAnalysis::getBTagWeight_promote_demote( UZH::Jet& jet ) {
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
  
  //std::cout << "Jet b tagged:" << isBTagged << " -> ";
  
  TRandom3* generator = new TRandom3( (int) ((jet.eta()+5)*100000) );
  double rand = generator->Uniform(1.);
  
  double BTag_SF  = m_BTaggingScaleTool.getScaleFactor_noWeight(jet);
  double BTag_eff = m_BTaggingScaleTool.getEfficiency(jet,"jet_ak4");
  double BTag_SFweight  = m_BTaggingScaleTool.getScaleFactor(jet);
  b_weightbtag_ *= BTag_SFweight;
  
  if (BTag_SF == 1) return isBTagged; // no correction
  else if(BTag_SF > 1){
    if(isBTagged) return isBTagged;
    float mistagPercentage = (1.0 - BTag_SF) / (1.0 - (1.0/BTag_eff)); // fraction of jets to be promoted
    if( rand < mistagPercentage ) isBTagged = true; // PROMOTE
  }
  else{
    if(!isBTagged) return isBTagged;
    if( rand < 1 - BTag_SF ) isBTagged = false; // DEMOTE: 1-SF fraction of jets to be demoted
  }
  
  jet.setTagged(isBTagged);
  //std::cout << jet.isTagged() << ", " << isBTagged << std:;endl;
  return isBTagged;
}

