// $Id: CycleCreators.py 344 2012-12-13 13:10:53Z krasznaa $

#include "../include/DiMuonAnalysis.h"

ClassImp( DiMuonAnalysis );





DiMuonAnalysis::DiMuonAnalysis() : SCycleBase(),
    m_eventInfo( this ),
    m_jetAK4( this ),
    m_genJetAK4( this ),
    m_muon( this ),
    m_electron( this ),
    m_tau( this ),
    m_missingEt( this ),
    m_puppimissingEt( this ),
    m_genParticle( this ),
    m_PileupReweightingTool( this ),
    m_BTaggingScaleTool( this ),
    m_ScaleFactorTool( this ),
    m_RochesterTool(this),
    m_RecoilCorrector( this ),
    m_JetCorrectionTool( this )
{
  
  m_logger << INFO << "Hello!" << SLogger::endmsg;
  SetLogName( GetName() );
  
  // channels
  channels_.push_back("mumu");
  
  // read configuration details from XML file
  DeclareProperty( "RecoTreeName",          m_recoTreeName          = "tree"            );
  DeclareProperty( "JetAK4Name",            m_jetAK4Name            = "jetAK4"          );
  DeclareProperty( "genJetAK4Name",         m_genJetAK4Name         = "genJetAK4"       );
  DeclareProperty( "MuonName",              m_muonName              = "mu"              );
  DeclareProperty( "ElectronName",          m_electronName          = "el"              );
  DeclareProperty( "TauName",               m_tauName               = "tau"             );
  DeclareProperty( "MissingEtName",         m_missingEtName         = "MET"             );
  DeclareProperty( "GenParticleName",       m_genParticleName       = "genParticle"     );
  
  DeclareProperty( "IsData",                m_isData                = false             );
  DeclareProperty( "IsSignal",              m_isSignal              = false             );
  DeclareProperty( "doRecoilCorr",          m_doRecoilCorr          = false             );
  DeclareProperty( "doZpt",                 m_doZpt                 = false             );
  DeclareProperty( "doTTpt",                m_doTTpt                = false             );
  DeclareProperty( "RCset",                 m_RCset                 = 0                 );
  DeclareProperty( "RCerror",               m_RCerror               = 0                 );
  DeclareProperty( "TESshift",              m_TESshift              = 0.0               );
  DeclareProperty( "doTES",                 m_doTES                 = false             );
  DeclareProperty( "doTight",               m_doTight               = false             ); // fill branches with less events
  DeclareProperty( "noTight",               m_noTight               = false             ); // override doTight
  
  DeclareProperty( "AK4JetPtCut",           m_AK4jetPtCut           = 20.               );
  DeclareProperty( "AK4JetEtaCut",          m_AK4jetEtaCut          = 4.7               );
  
  DeclareProperty( "CSVWorkingPoint",       m_CSVWorkingPoint       = 0.8838            );
  DeclareProperty( "deepCSVWorkingPoint",   m_deepCSVWorkingPoint   = 0.4941            );
  
  DeclareProperty( "MuonPtCut",             m_muonPtCut             = 15.               );
  DeclareProperty( "SecondMuonPtCut",       m_secondMuonPtCut       = 25.               );
  DeclareProperty( "MuonEtaCut",            m_muonEtaCut            = 2.4               );
  DeclareProperty( "MuonD0Cut",             m_muonD0Cut             = 0.045             );
  DeclareProperty( "MuonDzCut",             m_muonDzCut             = 0.2               );
  DeclareProperty( "MuonIsoCut",            m_muonIsoCut            = 0.15              );
  
  DeclareProperty( "TauPtCut",              m_tauPtCut              = 20.               );
  DeclareProperty( "TauEtaCut",             m_tauEtaCut             = 2.3               );
  DeclareProperty( "TauDzCut",              m_tauDzCut              = 0.2               );
  
  //DeclareProperty( "JSONName",              m_jsonName              = std::string(std::getenv("SFRAME_DIR"))+"/../GoodRunsLists/JSON/Cert_294927-305636_13TeV_PromptReco_Collisions17_JSON.txt" ); // 35.88/fb
  DeclareProperty( "JSONName",              m_jsonName              = std::string(std::getenv("SFRAME_DIR"))+"/../GoodRunsLists/JSON/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt" ); // 41.86 /fb
  DeclareProperty( "dataPUFileName",        m_dataPUFileName        = "$SFRAME_DIR/../PileupReweightingTool/histograms/Data_PileUp_2017_69p2.root"     );
  
}





DiMuonAnalysis::~DiMuonAnalysis(){
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "Tschoe!" << SLogger::endmsg;
  std::cout << " " << std::endl;
}





void DiMuonAnalysis::BeginCycle() throw( SError ){
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "BeginCycle" << SLogger::endmsg;
  
  dimuon_events = 0;

  // Load GRL:
  if (m_isData){
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
  
  m_triggers.clear();
  
  // MARK: Triggers
  // 2017: run 294927 to 306126
  m_triggers.push_back( "HLT_IsoMu24_v"                                           );
  m_triggers.push_back( "HLT_IsoMu27_v"                                           );
  //m_triggers.push_back( "HLT_IsoTkMu27_v"                                         );
  //m_triggers.push_back( "HLT_IsoMu27_eta2p1"                                      );
  //m_triggers.push_back( "HLT_IsoTkMu27_eta2p1"                                    );
  
  m_logger << INFO << "\nmuon triggers: " << SLogger::endmsg;
  for (auto const& trigger: m_triggers) m_logger << INFO << "  " << trigger << SLogger::endmsg;
  m_logger << INFO << " " << SLogger::endmsg;
  
  return;
  
}





void DiMuonAnalysis::EndCycle() throw( SError ) {
   m_logger << INFO << " " << SLogger::endmsg;
   m_logger << INFO << "EndCycle" << SLogger::endmsg;
   m_logger << INFO << " " << SLogger::endmsg;
   return;
}





void DiMuonAnalysis::BeginInputData( const SInputData& id ) throw( SError ) {
  //std::cout << "BeginInputData" << std::endl;
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "BeginInputData" << SLogger::endmsg;
  
  m_logger << INFO << "RecoTreeName:        " << m_recoTreeName        << SLogger::endmsg;
  m_logger << INFO << "JetAK4Name:          " << m_jetAK4Name          << SLogger::endmsg;
  m_logger << INFO << "MuonName:            " << m_muonName            << SLogger::endmsg;
  m_logger << INFO << "ElectronName:        " << m_electronName        << SLogger::endmsg;
  m_logger << INFO << "TauName:             " << m_tauName             << SLogger::endmsg;
  m_logger << INFO << "GenParticleName:     " << m_genParticleName     << SLogger::endmsg;
  
  m_doTES   = m_TESshift != 0.0 and !m_isData;
  m_doTight = m_doTight or m_doTES; // need fail region for EES, JTF
  m_doTight = m_doTight and !m_noTight;        // noTight overrides doTight
  m_logger << INFO << "IsData:              " << (m_isData       ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "IsSignal:            " << (m_isSignal     ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doRecoilCorr:        " << (m_doRecoilCorr ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doZpt:               " << (m_doZpt        ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTTpt:              " << (m_doTTpt       ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "RCset:               " << m_RCset               << SLogger::endmsg;
  m_logger << INFO << "RCerror:             " << m_RCerror             << SLogger::endmsg;
  m_logger << INFO << "doTES:               " << (m_doTES        ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "TESshift:            " << m_TESshift            << SLogger::endmsg;
  m_logger << INFO << "noTight:             " << (m_noTight      ? "TRUE" : "FALSE") << SLogger::endmsg;
  m_logger << INFO << "doTight:             " << (m_doTight      ? "TRUE" : "FALSE") << SLogger::endmsg;
  
  m_logger << INFO << "MuonPtCut:           " << m_muonPtCut           << SLogger::endmsg;
  m_logger << INFO << "SecondMuonPtCut:     " << m_secondMuonPtCut     << SLogger::endmsg;
  m_logger << INFO << "MuonEtaCut:          " << m_muonEtaCut          << SLogger::endmsg;
  m_logger << INFO << "MuonD0Cut:           " << m_muonD0Cut           << SLogger::endmsg;
  m_logger << INFO << "MuonDzCut:           " << m_muonDzCut           << SLogger::endmsg;
  m_logger << INFO << "MuonIsoCut:          " << m_muonIsoCut          << SLogger::endmsg;
  
  m_logger << INFO << "TauPtCut:            " << m_tauPtCut            << SLogger::endmsg;
  m_logger << INFO << "TauEtaCut:           " << m_tauEtaCut           << SLogger::endmsg;
  m_logger << INFO << "TauDzCut:            " << m_tauDzCut            << SLogger::endmsg;
  
  m_logger << INFO << "JSONName:            " << m_jsonName            << SLogger::endmsg;
  m_logger << INFO << "dataPUFileName:      " << m_dataPUFileName      << SLogger::endmsg;
  
  
  // MARK Branches
  m_logger << INFO << "Declaring variables for branches" << SLogger::endmsg;
  for(int chi = 0; chi < (int)channels_.size(); chi++){
    
    TString treeName = "tree_" + channels_[chi];
    const char* ch = channels_[chi].c_str();
    
    DeclareVariable( b_channel[ch],             "channel",              treeName);
    DeclareVariable( b_isData[ch],              "isData",               treeName);
    
    DeclareVariable( b_weight[ch],              "weight",               treeName);
    DeclareVariable( b_genweight[ch],           "genweight",            treeName);
    DeclareVariable( b_puweight[ch],            "puweight",             treeName);
    DeclareVariable( b_weightbtag[ch],          "weightbtag",           treeName);
    DeclareVariable( b_zptweight[ch],           "zptweight",            treeName);
    DeclareVariable( b_ttptweight[ch],          "ttptweight",           treeName);
    DeclareVariable( b_ttptweight_runI[ch],     "ttptweight_runI",      treeName);
    DeclareVariable( b_trigweight_1[ch],        "trigweight_1",         treeName);
    DeclareVariable( b_idisoweight_1[ch],       "idisoweight_1",        treeName);
    DeclareVariable( b_idisoweight_2[ch],       "idisoweight_2",        treeName);
    
    DeclareVariable( b_run[ch],                 "run",                  treeName);
    DeclareVariable( b_evt[ch],                 "evt",                  treeName);
    DeclareVariable( b_lum[ch],                 "lum",                  treeName);
    
    DeclareVariable( b_npv[ch],                 "npv",                  treeName);
    DeclareVariable( b_npu[ch],                 "npu",                  treeName);
    DeclareVariable( b_NUP[ch],                 "NUP",                  treeName);
    DeclareVariable( b_rho[ch],                 "rho",                  treeName);
    
    DeclareVariable( b_pt_1[ch],                "pt_1",                 treeName);
    DeclareVariable( b_eta_1[ch],               "eta_1",                treeName);
    DeclareVariable( b_phi_1[ch],               "phi_1",                treeName);
    DeclareVariable( b_m_1[ch],                 "m_1",                  treeName);
    DeclareVariable( b_q_1[ch],                 "q_1",                  treeName);
    DeclareVariable( b_d0_1[ch],                "d0_1",                 treeName);
    DeclareVariable( b_dz_1[ch],                "dz_1",                 treeName);
    DeclareVariable( b_pfmt_1[ch],              "pfmt_1",               treeName);
    DeclareVariable( b_iso_1[ch],               "iso_1",                treeName);
    
    DeclareVariable( b_pt_2[ch],                "pt_2",                 treeName);
    DeclareVariable( b_eta_2[ch],               "eta_2",                treeName);
    DeclareVariable( b_phi_2[ch],               "phi_2",                treeName);
    DeclareVariable( b_m_2[ch],                 "m_2",                  treeName);
    DeclareVariable( b_q_2[ch],                 "q_2",                  treeName);
    DeclareVariable( b_d0_2[ch],                "d0_2",                 treeName);
    DeclareVariable( b_dz_2[ch],                "dz_2",                 treeName);
    DeclareVariable( b_pfmt_2[ch],              "pfmt_2",               treeName);
    DeclareVariable( b_iso_2[ch],               "iso_2",                treeName);
    
    DeclareVariable( b_m_3[ch],                 "m_3",                  treeName);
    DeclareVariable( b_pt_3[ch],                "pt_3",                 treeName);
    DeclareVariable( b_eta_3[ch],               "eta_3",                treeName);
    DeclareVariable( b_decayMode_3[ch],         "decayMode_3",          treeName);
    DeclareVariable( b_gen_match_3[ch],         "gen_match_3",          treeName);
    DeclareVariable( b_againstLepton_3[ch],     "againstLepton_3",      treeName);
    
    DeclareVariable( b_byIsolationMVArun2v1DBoldDMwLTraw_3[ch],            "byIsolationMVArun2v1DBoldDMwLTraw_3",            treeName);
    DeclareVariable( b_byIsolationMVArun2v2DBoldDMwLTraw_3[ch],            "byIsolationMVArun2v2DBoldDMwLTraw_3",            treeName);
    DeclareVariable( b_byIsolationMVArun2v1DBnewDMwLTraw_3[ch],            "byIsolationMVArun2v1DBnewDMwLTraw_3",            treeName);

    DeclareVariable( b_byVLooseIsolationMVArun2v1DBoldDMwLT_3[ch],         "byVLooseIsolationMVArun2v1DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byLooseIsolationMVArun2v1DBoldDMwLT_3[ch],          "byLooseIsolationMVArun2v1DBoldDMwLT_3",          treeName);
    DeclareVariable( b_byMediumIsolationMVArun2v1DBoldDMwLT_3[ch],         "byMediumIsolationMVArun2v1DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byTightIsolationMVArun2v1DBoldDMwLT_3[ch],          "byTightIsolationMVArun2v1DBoldDMwLT_3",          treeName);
    DeclareVariable( b_byVTightIsolationMVArun2v1DBoldDMwLT_3[ch],         "byVTightIsolationMVArun2v1DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byVVTightIsolationMVArun2v1DBoldDMwLT_3[ch],        "byVVTightIsolationMVArun2v1DBoldDMwLT_3",        treeName);
    
    DeclareVariable( b_byVLooseIsolationMVArun2v2DBoldDMwLT_3[ch],         "byVLooseIsolationMVArun2v2DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byLooseIsolationMVArun2v2DBoldDMwLT_3[ch],          "byLooseIsolationMVArun2v2DBoldDMwLT_3",          treeName);
    DeclareVariable( b_byMediumIsolationMVArun2v2DBoldDMwLT_3[ch],         "byMediumIsolationMVArun2v2DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byTightIsolationMVArun2v2DBoldDMwLT_3[ch],          "byTightIsolationMVArun2v2DBoldDMwLT_3",          treeName);
    DeclareVariable( b_byVTightIsolationMVArun2v2DBoldDMwLT_3[ch],         "byVTightIsolationMVArun2v2DBoldDMwLT_3",         treeName);
    DeclareVariable( b_byVVTightIsolationMVArun2v2DBoldDMwLT_3[ch],        "byVVTightIsolationMVArun2v2DBoldDMwLT_3",        treeName);
    
    DeclareVariable( b_byVLooseIsolationMVArun2v1DBnewDMwLT_3[ch],         "byVLooseIsolationMVArun2v1DBnewDMwLT_3",         treeName);
    DeclareVariable( b_byLooseIsolationMVArun2v1DBnewDMwLT_3[ch],          "byLooseIsolationMVArun2v1DBnewDMwLT_3",          treeName);
    DeclareVariable( b_byMediumIsolationMVArun2v1DBnewDMwLT_3[ch],         "byMediumIsolationMVArun2v1DBnewDMwLT_3",         treeName);
    DeclareVariable( b_byTightIsolationMVArun2v1DBnewDMwLT_3[ch],          "byTightIsolationMVArun2v1DBnewDMwLT_3",          treeName);
    DeclareVariable( b_byVTightIsolationMVArun2v1DBnewDMwLT_3[ch],         "byVTightIsolationMVArun2v1DBnewDMwLT_3",         treeName);
    DeclareVariable( b_byVVTightIsolationMVArun2v1DBnewDMwLT_3[ch],        "byVVTightIsolationMVArun2v1DBnewDMwLT_3",        treeName);
    
    DeclareVariable( b_byCombinedIsolationDeltaBetaCorrRaw3Hits_3[ch],     "byCombinedIsolationDeltaBetaCorrRaw3Hits_3",     treeName);
    DeclareVariable( b_byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch], "byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3", treeName);
    DeclareVariable( b_byVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch],  "byVLooseCombinedIsolationDeltaBetaCorr3Hits_3",  treeName);
    DeclareVariable( b_byLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch],   "byLooseCombinedIsolationDeltaBetaCorr3Hits_3",   treeName);
    DeclareVariable( b_byMediumCombinedIsolationDeltaBetaCorr3Hits_3[ch],  "byMediumCombinedIsolationDeltaBetaCorr3Hits_3",  treeName);
    DeclareVariable( b_byTightCombinedIsolationDeltaBetaCorr3Hits_3[ch],   "byTightCombinedIsolationDeltaBetaCorr3Hits_3",   treeName);
    
    DeclareVariable( b_extraelec_veto[ch],      "extraelec_veto",       treeName);
    DeclareVariable( b_extramuon_veto[ch],      "extramuon_veto",       treeName);
    
    DeclareVariable( b_jpt_1[ch],               "jpt_1",                treeName);
    DeclareVariable( b_jeta_1[ch],              "jeta_1",               treeName);
    DeclareVariable( b_jphi_1[ch],              "jphi_1",               treeName);
    DeclareVariable( b_jpt_2[ch],               "jpt_2",                treeName);
    DeclareVariable( b_jeta_2[ch],              "jeta_2",               treeName);
    DeclareVariable( b_jphi_2[ch],              "jphi_2",               treeName);
    
    DeclareVariable( b_bpt_1[ch],               "bpt_1",                treeName);
    DeclareVariable( b_beta_1[ch],              "beta_1",               treeName);
    DeclareVariable( b_bphi_1[ch],              "bphi_1",               treeName);
    DeclareVariable( b_bcsv_1[ch],              "bcsv_1",               treeName);
    DeclareVariable( b_bdeepcsv_1[ch],          "bdeepcsv_1",           treeName);
    DeclareVariable( b_bpt_2[ch],               "bpt_2",                treeName);
    DeclareVariable( b_beta_2[ch],              "beta_2",               treeName);
    DeclareVariable( b_bphi_2[ch],              "bphi_2",               treeName);
    DeclareVariable( b_bcsv_2[ch],              "bcsv_2",               treeName);
    DeclareVariable( b_bdeepcsv_2[ch],          "bdeepcsv_2",           treeName);
    
    DeclareVariable( b_njets[ch],               "njets",                treeName);
    DeclareVariable( b_nfjets[ch],              "nfjets",               treeName);
    DeclareVariable( b_ncjets[ch],              "ncjets",               treeName);
    DeclareVariable( b_nbtag[ch],               "nbtag",                treeName);
    DeclareVariable( b_njets20[ch],             "njets20",              treeName);
    DeclareVariable( b_nfjets20[ch],            "nfjets20",             treeName);
    DeclareVariable( b_ncjets20[ch],            "ncjets20",             treeName);
    DeclareVariable( b_nbtag20[ch],             "nbtag20",              treeName);
    
    DeclareVariable( b_met[ch],                 "met",                  treeName);
    DeclareVariable( b_metphi[ch],              "metphi",               treeName);
    
    //if (m_doJEC){
    //  DeclareVariable( b_njets_jesUp[ch],           "njets_jesUp",          treeName);
    //  DeclareVariable( b_njets_jesDown[ch],         "njets_jesDown",        treeName);
    //  DeclareVariable( b_njets_jerUp[ch],           "njets_jerUp",          treeName);
    //  DeclareVariable( b_njets_jerDown[ch],         "njets_jerDown",        treeName);
    //  DeclareVariable( b_njets20_jesUp[ch],         "njets20_jesUp",        treeName);
    //  DeclareVariable( b_njets20_jesDown[ch],       "njets20_jesDown",      treeName);
    //  DeclareVariable( b_njets20_jerUp[ch],         "njets20_jerUp",        treeName);
    //  DeclareVariable( b_njets20_jerDown[ch],       "njets20_jerDown",      treeName);
    //  DeclareVariable( b_ncjets_jesUp[ch],          "ncjets_jesUp",         treeName);
    //  DeclareVariable( b_ncjets_jesDown[ch],        "ncjets_jesDown",       treeName);
    //  DeclareVariable( b_ncjets_jerUp[ch],          "ncjets_jerUp",         treeName);
    //  DeclareVariable( b_ncjets_jerDown[ch],        "ncjets_jerDown",       treeName);
    //  DeclareVariable( b_nbtag_jesUp[ch],           "nbtag_jesUp",          treeName);
    //  DeclareVariable( b_nbtag_jesDown[ch],         "nbtag_jesDown",        treeName);
    //  DeclareVariable( b_nbtag_jerUp[ch],           "nbtag_jerUp",          treeName);
    //  DeclareVariable( b_nbtag_jerDown[ch],         "nbtag_jerDown",        treeName);
    //  DeclareVariable( b_nfjets_jesUp[ch],          "nfjets_jesUp",         treeName);
    //  DeclareVariable( b_nfjets_jesDown[ch],        "nfjets_jesDown",       treeName);
    //  DeclareVariable( b_nfjets_jerUp[ch],          "nfjets_jerUp",         treeName);
    //  DeclareVariable( b_nfjets_jerDown[ch],        "nfjets_jerDown",       treeName);
    //  
    //  DeclareVariable( b_jpt_1_jesUp[ch],           "jpt_1_jesUp",          treeName);
    //  DeclareVariable( b_jpt_1_jesDown[ch],         "jpt_1_jesDown",        treeName);
    //  DeclareVariable( b_jpt_1_jerUp[ch],           "jpt_1_jerUp",          treeName);
    //  DeclareVariable( b_jpt_1_jerDown[ch],         "jpt_1_jerDown",        treeName);
    //  DeclareVariable( b_jeta_1_jesUp[ch],          "jeta_1_jesUp",         treeName);
    //  DeclareVariable( b_jeta_1_jesDown[ch],        "jeta_1_jesDown",       treeName);
    //  DeclareVariable( b_jeta_1_jerUp[ch],          "jeta_1_jerUp",         treeName);
    //  DeclareVariable( b_jeta_1_jerDown[ch],        "jeta_1_jerDown",       treeName);
    //  DeclareVariable( b_jpt_2_jesUp[ch],           "jpt_2_jesUp",          treeName);
    //  DeclareVariable( b_jpt_2_jesDown[ch],         "jpt_2_jesDown",        treeName);
    //  DeclareVariable( b_jpt_2_jerUp[ch],           "jpt_2_jerUp",          treeName);
    //  DeclareVariable( b_jpt_2_jerDown[ch],         "jpt_2_jerDown",        treeName);
    //  DeclareVariable( b_jeta_2_jesUp[ch],          "jeta_2_jesUp",         treeName);
    //  DeclareVariable( b_jeta_2_jesDown[ch],        "jeta_2_jesDown",       treeName);
    //  DeclareVariable( b_jeta_2_jerUp[ch],          "jeta_2_jerUp",         treeName);
    //  DeclareVariable( b_jeta_2_jerDown[ch],        "jeta_2_jerDown",       treeName);
    //  
    //  DeclareVariable( b_met_jesUp[ch],             "met_jesUp",            treeName);
    //  DeclareVariable( b_met_jesDown[ch],           "met_jesDown",          treeName);
    //  DeclareVariable( b_met_jerUp[ch],             "met_jerUp",            treeName);
    //  DeclareVariable( b_met_jerDown[ch],           "met_jerDown",          treeName);
    //  DeclareVariable( b_met_UncEnUp[ch],           "met_UncEnUp",          treeName);
    //  DeclareVariable( b_met_UncEnDown[ch],         "met_UncEnDown",        treeName);
    //  
    //  DeclareVariable( b_pfmt_1_jesUp[ch],          "pfmt_1_jesUp",         treeName);
    //  DeclareVariable( b_pfmt_1_jesDown[ch],        "pfmt_1_jesDown",       treeName);
    //  DeclareVariable( b_pfmt_1_jerUp[ch],          "pfmt_1_jerUp",         treeName);
    //  DeclareVariable( b_pfmt_1_jerDown[ch],        "pfmt_1_jerDown",       treeName);
    //  DeclareVariable( b_pfmt_1_UncEnUp[ch],        "pfmt_1_UncEnUp",       treeName);
    //  DeclareVariable( b_pfmt_1_UncEnDown[ch],      "pfmt_1_UncEnDown",     treeName);
    //  
    //  DeclareVariable( b_weightbtag_bcUp[ch],       "weightbtag_bcUp",      treeName);
    //  DeclareVariable( b_weightbtag_bcDown[ch],     "weightbtag_bcDown",    treeName);
    //  DeclareVariable( b_weightbtag_udsgUp[ch],     "weightbtag_udsgUp",    treeName);
    //  DeclareVariable( b_weightbtag_udsgDown[ch],   "weightbtag_udsgDown",  treeName);
    //}
    
    DeclareVariable( b_dR_ll[ch],               "dR_ll",                treeName);
    DeclareVariable( b_pt_ll[ch],               "pt_ll",                treeName);
    DeclareVariable( b_deta_ll[ch],             "deta_ll",              treeName);
    DeclareVariable( b_dphi_ll[ch],             "dphi_ll",              treeName);
    DeclareVariable( b_ht[ch],                  "ht",                   treeName);
    DeclareVariable( b_m_vis[ch],               "m_vis",                treeName);
    DeclareVariable( b_m_mutau_1[ch],           "m_mutau_1",            treeName);
    DeclareVariable( b_m_mutau_2[ch],           "m_mutau_2",            treeName);
    
    DeclareVariable( b_m_genboson[ch],          "m_genboson",           treeName);
    DeclareVariable( b_pt_genboson[ch],         "pt_genboson",          treeName);
    DeclareVariable( b_pt_top_1[ch],            "pt_top_1",             treeName);
    DeclareVariable( b_pt_top_2[ch],            "pt_top_2",             treeName);
    
    DeclareVariable( b_pzetamiss[ch],           "pzetamiss",            treeName);
    DeclareVariable( b_pzetavis[ch],            "pzetavis",             treeName);
    DeclareVariable( b_dzeta[ch],               "dzeta",                treeName);
    
  }
  
  
  // MARK Histograms
  m_logger << INFO << "Declaring histograms" << SLogger::endmsg;
  
  for (auto ch: channels_){
    TString hname = "cutflow_" + ch;
    TString dirname = "histogram_" + ch;
    TString tch = ch;
    Book( TH1F(hname, hname, 12, 0.5, 12.5 ), dirname);
  }
  
  //Book( TH1F("muonSF", "muon SF", 100, 0, 2 ), "checks");
  
  if (!m_isData){
    m_PileupReweightingTool.BeginInputData( id, m_dataPUFileName );
  }else{
    TObject* grl;
    if(!(grl = GetConfigObject( "MyGoodRunsList" ))) {
      m_logger << FATAL << "Can't access the GRL!" << SLogger::endmsg;
      throw SError( "Can't access the GRL!", SError::SkipCycle );
    }
    m_grl = *( dynamic_cast< Root::TGoodRunsList* >( grl ) );
  }
  
  m_BTaggingScaleTool.BeginInputData( id, "mumu" );
  m_BTaggingScaleTool.bookHistograms(); // to measure b tag efficiencies for our selections
  m_ScaleFactorTool.BeginInputData( id );
  m_RochesterTool.BeginInputData( id );
  m_RecoilCorrector.BeginInputData( id );
  m_JetCorrectionTool.BeginInputData( id );
  
  return;
  
}





void DiMuonAnalysis::EndInputData( const SInputData& ) throw( SError ) {
  //std::cout << "EndInputData" << std::endl;
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "EndInputData" << SLogger::endmsg;
  m_logger << INFO << " " << SLogger::endmsg;
  
  for(auto ch: channels_) {
    m_logger << INFO << "cut flow for " << ch << SLogger::endmsg;
    m_logger << INFO << Form( "Cut\t%25.25s\tEvents\tRelEff\tAbsEff", "Name" ) << SLogger::endmsg;
    
    TString hname = "cutflow_" + ch;
    TString dirname = "histogram_" + ch;
    Double_t ntot = Hist(hname, dirname)->GetBinContent( 1 );
    Hist(hname, dirname)->GetXaxis()->SetBinLabel(1,kCutName[0].c_str());
    Hist(hname, dirname)->GetXaxis()->SetLabelSize(0.044);
    m_logger << INFO << Form( "\t%25.25s\t%6.0f", "start", ntot ) << SLogger::endmsg;
    for( Int_t ibin = 1; ibin < kNumCuts; ++ibin ) {
      Int_t    icut    = ibin;
      Double_t nevents = Hist(hname, dirname)->GetBinContent( ibin+1 );
      Double_t releff  = 100. * nevents / Hist(hname, dirname)->GetBinContent( ibin );
      Double_t abseff  = 100. * nevents / ntot;
      m_logger << INFO  << Form( "C%d\t%25.25s\t%6.0f\t%6.2f\t%6.2f", icut-1, kCutName[icut].c_str(), nevents, releff, abseff ) << SLogger::endmsg;
      Hist(hname, dirname)->GetXaxis()->SetBinLabel(ibin+1, kCutName[icut].c_str());
    }
    
    m_logger << INFO << " " << SLogger::endmsg;
    
  }

  return;
}



void DiMuonAnalysis::printCutFlow(const std::string& ch, const std::string& name, const TString hname, const TString dirname, std::vector<std::string> cutName){
 //std::cout << "printCutFlow" << std::endl;
  
  Double_t ntot = Hist(hname, dirname)->GetBinContent( 1 );
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << name << " cut flow for " << ch << SLogger::endmsg;
  m_logger << INFO << Form( "Cut\t%25.25s\tEvents\tRelEff\tAbsEff", "Name" ) << SLogger::endmsg;
  m_logger << INFO << Form( "\t%25.25s\t%6.0f", "start", ntot ) << SLogger::endmsg;
  for( Int_t ibin=1; ibin<(int)cutName.size(); ++ibin ){
    Int_t    icut    = ibin;
    Double_t nevents = Hist(hname, dirname)->GetBinContent( ibin+1 );
    Double_t releff  = 100. * nevents / Hist(hname, dirname)->GetBinContent( ibin );
    Double_t abseff  = 100. * nevents / ntot;
    m_logger << INFO  << Form( "C%d\t%25.25s\t%6.0f\t%6.2f\t%6.2f", icut-1, cutName[icut].c_str(), nevents, releff, abseff ) << SLogger::endmsg;
  }
}





void DiMuonAnalysis::BeginInputFile( const SInputData& ) throw( SError ) {
//   std::cout << "BeginInputFile" << std::endl;
  m_logger << INFO << " " << SLogger::endmsg;
  m_logger << INFO << "Connecting input variables" << SLogger::endmsg;
  
  if (m_isData) {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis, (m_jetAK4Name + "_").c_str() );
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoBasic|Ntuple::EventInfoTrigger, "" );
  }else {
    m_jetAK4.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::JetBasic|Ntuple::JetAnalysis|Ntuple::JetTruth|Ntuple::JetJER, (m_jetAK4Name + "_").c_str() );
    m_genJetAK4.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::GenJetak4Truth,"");
    m_eventInfo.ConnectVariables(   m_recoTreeName.c_str(), Ntuple::EventInfoBasic|Ntuple::EventInfoTrigger|Ntuple::EventInfoTruth, "" );
    m_genParticle.ConnectVariables( m_recoTreeName.c_str(), Ntuple::GenParticleBasic|Ntuple::GenParticleTauDecayAnalysis, (m_genParticleName + "_").c_str() );
  }
  m_muon.ConnectVariables(          m_recoTreeName.c_str(), Ntuple::MuonBasic|Ntuple::MuonID|Ntuple::MuonIsolation|Ntuple::MuonTrack|Ntuple::MuonBoostedIsolation, (m_muonName + "_").c_str() );
  m_electron.ConnectVariables(      m_recoTreeName.c_str(), Ntuple::ElectronBasic|Ntuple::ElectronID|Ntuple::ElectronAdvancedID|Ntuple::ElectronBoostedIsolation|Ntuple::ElectronSuperCluster, (m_electronName + "_").c_str() );
  m_tau.ConnectVariables(           m_recoTreeName.c_str(), Ntuple::TauBasic|Ntuple::TauID|Ntuple::TauAdvancedID|Ntuple::TauAdvancedIDv2, (m_tauName + "_").c_str() );
  
  m_missingEt.ConnectVariables(     m_recoTreeName.c_str(), Ntuple::MissingEtBasic|Ntuple::MissingEtAnalysis|Ntuple::MissingEtAnalysisSyst|Ntuple::MissingEtCovAnalysis, (m_missingEtName + "_").c_str() );
  m_puppimissingEt.ConnectVariables(m_recoTreeName.c_str(), Ntuple::MissingEtBasic, (m_missingEtName + "_puppi_").c_str() );
  
  m_logger << INFO << "Connecting input variables completed" << SLogger::endmsg;
  
  return;

}





void DiMuonAnalysis::ExecuteEvent( const SInputData&, Double_t ) throw( SError ) {
  //std::cout << "\nExecuteEvent" << std::endl;
  //m_logger << VERBOSE << "ExecuteEvent" << SLogger::endmsg;
  
  b_weight_     =  1.;
  b_puweight_   =  1.;
  b_genweight_  = (m_isData) ? 1 : m_eventInfo.genEventWeight;
  b_npu_        = -1.;
  
  
  // MARK: Cut 0: no cuts
  for (auto ch: channels_){
    b_channel[ch] = 0;
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCuts, 1);
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCutsUnweighted, 1 );
    fillCutflow("cutflow_" + ch, "histogram_" + ch, kBeforeCutsWeighted, b_genweight_);
  }
  if (m_isData){
    if(m_eventInfo.PV_N<=0) throw SError( SError::SkipEvent );
  }else{
    for (auto ch: channels_)
      fillCutflow("cutflow_"+ch, "histogram_"+ch, kJSON, 1);
    getEventWeight();
  }
  for (auto ch: channels_){
    b_channel[ch] = 0;
    fillCutflow("cutflow_"+ch, "histogram_"+ch, kNo0PUUnweighted, 1);
    fillCutflow("cutflow_"+ch, "histogram_"+ch, kNo0PUWeighted, b_genweight_);
  }
  
  
  // MARK: Cut 1: JSON
  if (m_isData){
    if(!(isGoodEvent(m_eventInfo.runNumber, m_eventInfo.lumiBlock))) throw SError( SError::SkipEvent );
    for (auto ch: channels_){
      fillCutflow("cutflow_"+ch, "histogram_"+ch, kJSON, 1);
    }
  }
  
  
  // MARK: Cut 2: trigger
  //std::cout << ">>> ExecuteEvent - Cut 2" << std::endl;
  m_trigger_Flags = passTrigger();
  if(m_trigger_Flags=="none"){
    throw SError( SError::SkipEvent );
  }
  
  for (auto ch: channels_){
    fillCutflow("cutflow_"+ch, "histogram_"+ch, kTrigger, 1);
  }
  
  
  // MARK: Cut 3: muon 1
  //std::cout << ">>> ExecuteEvent - Cut 3: muon 1" << std::endl;
  int secondMuon = 0;
  std::vector<UZH::Muon> goodMuons;
  for( int i = 0; i < m_muon.N; ++i ){
    UZH::Muon mymuon( &m_muon, i );
    
    //if(mymuon.pt() < m_muonPtCut*0.80) continue;
    //float sf = m_RochesterTool.correct(mymuon,m_genParticle,m_isData,m_RCset,0,m_RCerror); // Rochester correction to muon object
    //Hist("muonSF", "checks")->Fill(sf);
    if(mymuon.pt() < m_muonPtCut) continue;
    if(fabs(mymuon.eta()) > m_muonEtaCut) continue;
    if(fabs(mymuon.d0_allvertices()) > m_muonD0Cut) continue;
    if(fabs(mymuon.dz_allvertices()) > m_muonDzCut) continue;
    if(mymuon.isMediumMuonGH() < 0.5) continue;
    if(mymuon.SemileptonicPFIso()/mymuon.pt() > m_muonIsoCut) continue; // tight
    goodMuons.push_back(mymuon);
    if(mymuon.pt()>m_secondMuonPtCut) secondMuon++;
  }
  
  if(goodMuons.size()>0){
    fillCutflow("cutflow_mumu", "histogram_mumu", kMuon, 1);
    //std::cout << ">>> ExecuteEvent - Cut 4: muon 2" << std::endl;
    if(goodMuons.size()>1 and secondMuon>0)
      fillCutflow("cutflow_mumu", "histogram_mumu", kSecondMuon, 1);
    else throw SError( SError::SkipEvent );
  }
  else throw SError( SError::SkipEvent );
  
  // MARK: Cut 5: muon pair
  //std::cout << ">>> ExecuteEvent - Cut 5: mumu" << std::endl;
  std::vector<lepton_pair> muon_pairs;
  for(int imuon=0; imuon<(int)goodMuons.size(); imuon++){
    for(int jmuon=imuon+1; jmuon<(int)goodMuons.size(); jmuon++){
      
      Float_t M  = goodMuons[imuon].M(goodMuons[jmuon]);
      if(M<70 or 110<M) continue;
      if(goodMuons[imuon].charge()*goodMuons[jmuon].charge()>0) continue; // require OS
      if(goodMuons[imuon].pt()<m_secondMuonPtCut and goodMuons[jmuon].pt()<m_secondMuonPtCut) continue;
      Float_t dR = goodMuons[imuon].DeltaR(goodMuons[jmuon]);
      if(dR<0.4) continue; // remove or lower for boosted ID
      
      Float_t pt_1  = goodMuons[imuon].pt();
      Float_t pt_2  = goodMuons[jmuon].pt();
      Float_t iso_1 = goodMuons[imuon].SemileptonicPFIso() / pt_1;
      Float_t iso_2 = goodMuons[jmuon].SemileptonicPFIso() / pt_2;
      
      lepton_pair pair;
      if(pt_1>pt_2){
        pair = {imuon, pt_1, iso_1, jmuon, pt_2, iso_2};
      }else{
        //std::cout<<">>> Warning! Muon piar: muon1 pt < muon2 pt ! Swapping..."<<std::endl;
        pair = {jmuon, pt_2, iso_2, imuon, pt_1, iso_1};
      }
      muon_pairs.push_back(pair);
    }
  }
  
  if(muon_pairs.size()==0)
    throw SError( SError::SkipEvent );
  
  UZH::MissingEt met( &m_missingEt, 0 );
  fillCutflow("cutflow_mumu", "histogram_mumu", kMuonPair, 1);
  sort(muon_pairs.begin(), muon_pairs.end());
  
  // For Jets: cut and filter our selected muon and tau
  std::vector<UZH::Jet> goodJetsAK4;
  for ( int i = 0; i < (m_jetAK4.N); i++ ) {
    UZH::Jet jet( &m_jetAK4, i );
    if(fabs(jet.eta()) > m_AK4jetEtaCut) continue;
    if(jet.pt() < m_AK4jetPtCut*0.5) continue; // loosen pt cut for smearing
    if(!LooseJetID(jet)) continue;
    if(jet.DeltaR(goodMuons[muon_pairs[0].i_1]) < 0.5) continue;
    if(jet.DeltaR(goodMuons[muon_pairs[0].i_2]) < 0.5) continue;
    goodJetsAK4.push_back(jet);
  }
  
  if(!m_isData){
    m_BTaggingScaleTool.fillEfficiencies(goodJetsAK4, "mumu"); // to measure b tag efficiencies for our selections
    m_BTaggingScaleTool.fillEfficienciesDeepCSV(goodJetsAK4, "mumu");
  }
  FillBranches( "mumu", goodMuons[muon_pairs[0].i_1], goodMuons[muon_pairs[0].i_2], goodJetsAK4, met );
  dimuon_events++;
  
}





bool DiMuonAnalysis::isGoodEvent(int runNumber, int lumiSection) {
  //std::cout << "isGoodEvent" << std::endl;
  if(m_isData)
    return m_grl.HasRunLumiBlock( runNumber, lumiSection );
  return false;
}





TString DiMuonAnalysis::passTrigger() {
  //std::cout << "DiMuonAnalysis::passTrigger" << std::endl;
  
  //std::string triggerFlags = "";
  for (std::map<std::string,bool>::iterator it = (m_eventInfo.trigDecision)->begin(); it != (m_eventInfo.trigDecision)->end(); ++it){
    if (it->second){
      for( auto const& trigger: m_triggers ){
        if ((it->first).find(trigger) != std::string::npos)
          return "mu27";
      }
    }
  }
  
  //if( triggerFlags == "" ) triggerFlags = "none";
  return "none";
}




void DiMuonAnalysis::getEventWeight() {
  //std::cout << "getEventWeight" << std::endl;
  
  b_npu_ = -1.;
  for( unsigned int v = 0; v < (m_eventInfo.actualIntPerXing)->size(); ++v ){
    if ( (*m_eventInfo.bunchCrossing)[v] == 0 ) {
      b_npu_ = (*m_eventInfo.actualIntPerXing)[v]; // averageIntPerXing
      if(b_npu_<=0)
        throw SError( SError::SkipEvent );
      b_puweight_ = m_PileupReweightingTool.getPileUpWeight( b_npu_ );
      break;
    }
  }
  
  b_weight_ *= b_puweight_*b_genweight_;
  
}





void DiMuonAnalysis::fillCutflow(TString histName, TString dirName, const Int_t id, const Double_t weight){
  //std::cout << "fillCutflow" << std::endl;
  Hist( histName, dirName )->Fill( id+1, weight );
}





void DiMuonAnalysis::FillBranches(const std::string& channel, const UZH::Muon& muon1, const UZH::Muon& muon2,
                                  std::vector<UZH::Jet> &Jets, UZH::MissingEt& met){
  //std::cout << "\nFillBranches";// << std::endl;
  
  const char* ch = channel.c_str();
  if(m_doRecoilCorr || m_doZpt){
    setGenBosonTLVs(); // only for HTT, DY and WJ
    b_m_genboson[ch]  = boson_tlv.M();
    b_pt_genboson[ch] = boson_tlv.Pt();
  }
  
  
  b_channel[ch]      = 4;
  b_weight[ch]       = b_weight_;
  b_genweight[ch]    = b_genweight_;
  b_puweight[ch]     = b_puweight_;
  b_evt[ch]          = m_eventInfo.eventNumber;
  b_run[ch]          = m_eventInfo.runNumber;
  b_lum[ch]          = m_eventInfo.lumiBlock;
  b_isData[ch]       = (Int_t) m_isData;
  
  b_npu[ch]          = b_npu_; // for MC defined in getEventWeight
  b_npv[ch]          = m_eventInfo.PV_N;
  b_NUP[ch]          = m_eventInfo.lheNj;
  b_rho[ch]          = m_eventInfo.rho;
  
  
  
  ///////////////////
  // MARK: Leptons //
  ///////////////////
  
  b_pt_1[ch]                = muon1.pt();
  b_eta_1[ch]               = muon1.eta();
  b_phi_1[ch]               = muon1.phi();
  b_m_1[ch]                 = muon1.m();
  b_q_1[ch]                 = muon1.charge();
  b_d0_1[ch]                = muon1.d0();
  b_dz_1[ch]                = muon1.dz();
  b_iso_1[ch]               = muon1.SemileptonicPFIso() / muon1.pt();
  
  b_pt_2[ch]                = muon2.pt();
  b_eta_2[ch]               = muon2.eta();
  b_phi_2[ch]               = muon2.phi();
  b_m_2[ch]                 = muon2.m();
  b_q_2[ch]                 = muon2.charge();
  b_d0_2[ch]                = muon2.d0();
  b_dz_2[ch]                = muon2.dz();
  b_iso_2[ch]               = muon2.SemileptonicPFIso() / muon2.pt();
  
  extraLeptonVetos(channel, muon1, muon2);
  b_extraelec_veto[ch]      = (Int_t) b_extraelec_veto_;
  b_extramuon_veto[ch]      = (Int_t) b_extramuon_veto_;
  b_lepton_vetos[ch]        = ( b_extraelec_veto_ or b_extramuon_veto_ );
  
  TLorentzVector muon1_tlv = muon1.tlv();
  TLorentzVector muon2_tlv = muon2.tlv();
  
  
  
  ////////////////
  // MARK: Taus //
  ////////////////
  
  float maxPt    = -1.;
  int maxIndex   = -1;
  int genmatch_3 = -9;
  UZH::Tau tau;
  for(int i=0; i<(m_tau.N); ++i){
    UZH::Tau tau( &m_tau, i );
    //if(tau.byIsolationMVArun2v1DBoldDMwLTraw()<maxIso) continue;
    if(tau.pt()<maxPt) continue;
    if(tau.DeltaR(muon1)<0.5) continue;
    if(tau.DeltaR(muon2)<0.5) continue;
    if(abs(tau.eta()) > m_tauEtaCut) continue;
    if(tau.TauType() != 1) continue; // 1 for standard ID, 2 for boosted ID
    if(fabs(tau.dz()) > m_tauDzCut) continue;
    if(tau.decayModeFinding() < 0.5 and tau.decayMode()!=11) continue;
    if(fabs(tau.charge()) != 1) continue; // remove for boosted ID
    if(tau.againstElectronVLooseMVA6()<0.5 or tau.againstMuonTight3()<0.5) continue; // same WPs as mutau; needs SFs!
    if(tau.pt() < m_tauPtCut) continue;
    maxIndex   = i;
    maxPt      = tau.pt(); // preference for highest pt
  }
  if(maxIndex>0){
    tau = UZH::Tau( &m_tau, maxIndex );
    if(!m_isData) genmatch_3 = genMatch(tau.eta(),tau.phi());
    b_gen_match_3[ch]                                    = genmatch_3;
    b_m_3[ch]                                            = tau.m();
    b_pt_3[ch]                                           = tau.pt();
    b_eta_3[ch]                                          = tau.eta();
    b_decayMode_3[ch]                                    = tau.decayMode(); // 0, 1, 10
    b_againstLepton_3[ch]                                = tau.againstElectronVLooseMVA6() > 0.5 and tau.againstMuonTight3() > 0.5;
    b_byIsolationMVArun2v1DBoldDMwLTraw_3[ch]            = tau.byIsolationMVArun2v1DBoldDMwLTraw();
    b_byIsolationMVArun2v2DBoldDMwLTraw_3[ch]            = tau.byIsolationMVArun2v2DBoldDMwLTraw();
    b_byIsolationMVArun2v1DBnewDMwLTraw_3[ch]            = tau.byIsolationMVArun2v1DBnewDMwLTraw();
    b_byCombinedIsolationDeltaBetaCorrRaw3Hits_3[ch]     = tau.byCombinedIsolationDeltaBetaCorrRaw3Hits();
    b_byVLooseIsolationMVArun2v1DBoldDMwLT_3[ch]         = tau.byVLooseIsolationMVArun2v1DBoldDMwLT();  // MVArun2v1DBold
    b_byLooseIsolationMVArun2v1DBoldDMwLT_3[ch]          = tau.byLooseIsolationMVArun2v1DBoldDMwLT();
    b_byMediumIsolationMVArun2v1DBoldDMwLT_3[ch]         = tau.byMediumIsolationMVArun2v1DBoldDMwLT();
    b_byTightIsolationMVArun2v1DBoldDMwLT_3[ch]          = tau.byTightIsolationMVArun2v1DBoldDMwLT();
    b_byVTightIsolationMVArun2v1DBoldDMwLT_3[ch]         = tau.byVTightIsolationMVArun2v1DBoldDMwLT();
    b_byVVTightIsolationMVArun2v1DBoldDMwLT_3[ch]        = tau.byVVTightIsolationMVArun2v1DBoldDMwLT();
    b_byVLooseIsolationMVArun2v2DBoldDMwLT_3[ch]         = tau.byVLooseIsolationMVArun2v2DBoldDMwLT();  // MVArun2v2DBold
    b_byLooseIsolationMVArun2v2DBoldDMwLT_3[ch]          = tau.byLooseIsolationMVArun2v2DBoldDMwLT();
    b_byMediumIsolationMVArun2v2DBoldDMwLT_3[ch]         = tau.byMediumIsolationMVArun2v2DBoldDMwLT();
    b_byTightIsolationMVArun2v2DBoldDMwLT_3[ch]          = tau.byTightIsolationMVArun2v2DBoldDMwLT();
    b_byVTightIsolationMVArun2v2DBoldDMwLT_3[ch]         = tau.byVTightIsolationMVArun2v2DBoldDMwLT();
    b_byVVTightIsolationMVArun2v2DBoldDMwLT_3[ch]        = tau.byVVTightIsolationMVArun2v2DBoldDMwLT();
    b_byVLooseIsolationMVArun2v1DBnewDMwLT_3[ch]         = tau.byVLooseIsolationMVArun2v1DBnewDMwLT();  // MVArun2v1DBnew
    b_byLooseIsolationMVArun2v1DBnewDMwLT_3[ch]          = tau.byLooseIsolationMVArun2v1DBnewDMwLT();
    b_byMediumIsolationMVArun2v1DBnewDMwLT_3[ch]         = tau.byMediumIsolationMVArun2v1DBnewDMwLT();
    b_byTightIsolationMVArun2v1DBnewDMwLT_3[ch]          = tau.byTightIsolationMVArun2v1DBnewDMwLT();
    b_byVTightIsolationMVArun2v1DBnewDMwLT_3[ch]         = tau.byVTightIsolationMVArun2v1DBnewDMwLT();
    b_byVVTightIsolationMVArun2v1DBnewDMwLT_3[ch]        = tau.byVVTightIsolationMVArun2v1DBnewDMwLT();
    b_byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch] = tau.byCombinedIsolationDeltaBetaCorrRaw3Hits()<4.5; // DeltaBetaCorr
    b_byVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch]  = tau.byCombinedIsolationDeltaBetaCorrRaw3Hits()<3.5;
    b_byLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch]   = tau.byLooseCombinedIsolationDeltaBetaCorr3Hits();
    b_byMediumCombinedIsolationDeltaBetaCorr3Hits_3[ch]  = tau.byMediumCombinedIsolationDeltaBetaCorr3Hits();
    b_byTightCombinedIsolationDeltaBetaCorr3Hits_3[ch]   = tau.byTightCombinedIsolationDeltaBetaCorr3Hits();
  }else{
    b_m_3[ch]                                            = -9;
    b_pt_3[ch]                                           = -9;
    b_eta_3[ch]                                          = -9;
    b_decayMode_3[ch]                                    = -9;
    b_againstLepton_3[ch]                                = -9;
    b_gen_match_3[ch]                                    = -9;
    b_byIsolationMVArun2v1DBoldDMwLTraw_3[ch]            = -9;
    b_byIsolationMVArun2v1DBnewDMwLTraw_3[ch]            = -9;
    b_byVLooseIsolationMVArun2v1DBoldDMwLT_3[ch]         = -9;
    b_byLooseIsolationMVArun2v1DBoldDMwLT_3[ch]          = -9;
    b_byMediumIsolationMVArun2v1DBoldDMwLT_3[ch]         = -9;
    b_byTightIsolationMVArun2v1DBoldDMwLT_3[ch]          = -9;
    b_byVTightIsolationMVArun2v1DBoldDMwLT_3[ch]         = -9;
    b_byVVTightIsolationMVArun2v1DBoldDMwLT_3[ch]        = -9;
    b_byVLooseIsolationMVArun2v2DBoldDMwLT_3[ch]         = -9;
    b_byLooseIsolationMVArun2v2DBoldDMwLT_3[ch]          = -9;
    b_byMediumIsolationMVArun2v2DBoldDMwLT_3[ch]         = -9;
    b_byTightIsolationMVArun2v2DBoldDMwLT_3[ch]          = -9;
    b_byVTightIsolationMVArun2v2DBoldDMwLT_3[ch]         = -9;
    b_byVVTightIsolationMVArun2v2DBoldDMwLT_3[ch]        = -9;
    b_byVLooseIsolationMVArun2v1DBnewDMwLT_3[ch]         = -9;
    b_byLooseIsolationMVArun2v1DBnewDMwLT_3[ch]          = -9;
    b_byMediumIsolationMVArun2v1DBnewDMwLT_3[ch]         = -9;
    b_byTightIsolationMVArun2v1DBnewDMwLT_3[ch]          = -9;
    b_byVTightIsolationMVArun2v1DBnewDMwLT_3[ch]         = -9;
    b_byVVTightIsolationMVArun2v1DBnewDMwLT_3[ch]        = -9;
    b_byCombinedIsolationDeltaBetaCorrRaw3Hits_3[ch]     = -9;
    b_byVVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch] = -9;
    b_byVLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch]  = -9;
    b_byLooseCombinedIsolationDeltaBetaCorr3Hits_3[ch]   = -9;
    b_byMediumCombinedIsolationDeltaBetaCorr3Hits_3[ch]  = -9;
    b_byTightCombinedIsolationDeltaBetaCorr3Hits_3[ch]   = -9;
  }
  
  // measure b tagging efficiency
  if(!m_isData and tau.pt()>20 and b_iso_1[ch]<0.15 && b_iso_2[ch]<0.15){
    std::vector<UZH::Jet> Jets_noTau;
    for( auto const& jet: Jets ){
      if(jet.DeltaR(tau)<0.5) continue;
      Jets_noTau.push_back(jet);
    }
    m_BTaggingScaleTool.fillEfficiencies(Jets_noTau,"noTau"); // to measure b tag efficiencies for our selections
    m_BTaggingScaleTool.fillEfficienciesDeepCSV(Jets_noTau,"noTau");
  }
  
  
  
  //////////////////
  // MARK: Shifts //
  //////////////////
  //std::cout << ">>> Shifts " << std::endl;
  
  // RECOIL CORRECTIONS
  //TLorentzVector met_tlv;
  //met_tlv.SetPxPyPzE(met.et()*TMath::Cos(met.phi()), met.et()*TMath::Sin(met.phi()), 0, met.et());
  //TLorentzVector met_tlv_corrected;
  ////TLorentzVector mvamet_tlv_corrected;
  //if(m_doRecoilCorr){
  //  met_tlv_corrected = m_RecoilCorrector.CorrectPFMETByMeanResolution( met_tlv.Px(),       met_tlv.Py(),
  //                                                                      boson_tlv.Px(),     boson_tlv.Py(),
  //                                                                      boson_tlv_vis.Px(), boson_tlv_vis.Py(),
  //                                                                      m_jetAK4.N ); //m_eventInfo.lheNj
  //}else{
  //  met_tlv_corrected = met_tlv;
  //}
  //
  //// SHIFTS
  //// apply shifts to tau_tlv_shifted, lep_tlv_shifted, met_tlv_corrected
  ////std::cout << ">>> Shifts " << std::endl;
  //if(!m_isData){
  //  if(m_doJTF and maxIndex>0 and genmatch_3!=5){ // jet to tau fake (JTF)
  //    b_pt_3[ch]    = tau.pt()*(1+m_JTFshift);
  //  }
  //}
  //// save corrections to UZH::MET object  
  //met.et(met_tlv_corrected.E());
  //met.phi(met_tlv_corrected.Phi());
  
  
  
  ////////////////
  // MARK: Jets //
  ////////////////
  
  float fmet_jes    = met.et();
  float fmetphi_jes = met.phi();
  FillJetBranches( ch, Jets, met, muon1, muon1, tau );
  
  
  
  ///////////////
  // MARK: MET //
  ///////////////
  
  //met_tlv.SetPxPyPzE(met.et()*TMath::Cos(met.phi()), met.et()*TMath::Sin(met.phi()), 0, met.et());
  float fmet         = met.et();
  float fmetphi      = met.phi();
  
  b_met[ch]         = fmet;
  b_metphi[ch]      = fmetphi;
  b_pfmt_1[ch]      = TMath::Sqrt(2*muon1.pt()*fmet*( 1-TMath::Cos(deltaPhi(muon1.phi(), fmetphi ))));
  b_pfmt_2[ch]      = TMath::Sqrt(2*muon2.pt()*fmet*( 1-TMath::Cos(deltaPhi(muon2.phi(), fmetphi ))));
  
  // discriminating variables
  TLorentzVector ll_tlv = muon1.tlv()+muon2.tlv();
  b_m_vis[ch]       = ll_tlv.M();
  b_dR_ll[ch]       = muon1.DeltaR(muon2);
  b_pt_ll[ch]       = ll_tlv.Pt();
  b_dphi_ll[ch]     = fabs(muon1_tlv.DeltaPhi(muon2_tlv));
  b_deta_ll[ch]     = fabs(muon1_tlv.Eta()-muon2_tlv.Eta());
  if(tau.pt()>20){
    b_m_mutau_1[ch] = muon1.M(tau);
    b_m_mutau_2[ch] = muon2.M(tau);
  }else{
    b_m_mutau_1[ch] = -1;
    b_m_mutau_2[ch] = -1;
  }
  
  // discriminating variables
  TVector3 leg1(muon1.px(), muon1.py(), 0.);
  TVector3 leg2(muon2.px(), muon2.py(), 0.);
  TVector3 metleg(met.px(), met.py(), 0.);
  TVector3 zetaAxis = (leg1.Unit() + leg2.Unit()).Unit();
  b_pzetamiss[ch]   = metleg*zetaAxis;
  b_pzetavis[ch]    = leg1*zetaAxis + leg2*zetaAxis;
  b_dzeta[ch]       = b_pzetamiss[ch] - 0.85*b_pzetavis[ch];
  
  
  
  ///////////////////
  // MARK: Weights //
  ///////////////////
  
  b_idisoweight_1[ch]       = 1.;
  b_trigweight_1[ch]        = 1.;
  b_idisoweight_2[ch]       = 1.;
  //b_trigweight_2[ch]        = 1.;
  b_zptweight[ch]           = 1.;
  b_ttptweight[ch]          = 1.;
  b_weightbtag[ch]          = 1.;
  
  if(!m_isData){
    b_trigweight_1[ch]            = m_ScaleFactorTool.get_ScaleFactor_Mu27Trig( b_pt_1[ch],b_eta_1[ch] );
    b_idisoweight_1[ch]           = m_ScaleFactorTool.get_ScaleFactor_MuIdIso(  b_pt_1[ch],b_eta_1[ch] );
    b_idisoweight_2[ch]           = m_ScaleFactorTool.get_ScaleFactor_MuIdIso(  b_pt_2[ch],b_eta_2[ch] );
    if(m_doZpt)  b_zptweight[ch]  = m_RecoilCorrector.ZptWeight( boson_tlv.M(), boson_tlv.Pt() );
    if(m_doTTpt) b_ttptweight[ch] = genMatchSF(channel, -36); // 6*-6 = -36
    b_weightbtag[ch]              = b_weightbtag_; // do not apply b tag weight when using promote-demote method !!!
    b_weight[ch] *= b_idisoweight_1[ch] * b_idisoweight_2[ch] * b_zptweight[ch] * b_ttptweight[ch]; // * b_weightbtag[ch]
  }
  
}







void DiMuonAnalysis::FillJetBranches( const char* ch, std::vector<UZH::Jet>& Jets, UZH::MissingEt& met, const UZH::Muon& muon1, const UZH::Muon& muon2, const UZH::Tau& tau ){
  //std::cout << "FillJetBranches " << ch << std::endl;
  
  // jet multiplicities
  Int_t njets  = 0;    Int_t njets20  = 0;
  Int_t nfjets = 0;    Int_t nfjets20 = 0;
  Int_t ncjets = 0;    Int_t ncjets20 = 0;
  Int_t nbtag  = 0;    Int_t nbtag20  = 0;
  Int_t njets_noTau = 0;
  Int_t nbtag_noTau = 0;  Int_t nbtag20_noTau = 0;
  
  // to compare to uncorrected "nominal" jets
  TLorentzVector jet1,  jet2,  // default jets (JER on top of JES)
                 bjet1, bjet2; // two leading b tagged jets
  double bcsv1 = 0;
  double bcsv2 = 0;
  double bdeepcsv1 = 0;
  double bdeepcsv2 = 0;
  
  Float_t ht     = muon1.e() + muon2.e(); // total scalar energy HT
  b_weightbtag_  = 1.;
  
  for( int ijet=0; ijet<(int)Jets.size(); ++ijet ){ // already |eta|<4.7 jets
      
      // "nominal" jet
      Float_t abseta     = fabs(Jets.at(ijet).eta());
      Float_t pt         = Jets.at(ijet).pt();
      TLorentzVector jet = Jets.at(ijet).tlv();
      bool isBTagged     = getBTagStatus_promote_demote(Jets.at(ijet));
      Jets.at(ijet).setTagged(isBTagged);
      bool noTau         = (tau.pt()<20 or Jets.at(ijet).DeltaR(tau)>0.5) and abseta<2.4;
      
      // smeared jet
      if(m_isData){ // no SMEARING
        if(pt<m_AK4jetPtCut) continue;
        if(pt > jet1.Pt()){
          if(jet1.Pt()<20){ // jet1 is unset
            jet1 = jet;
          }else{ // jet1 is already set - reorder
            jet2 = jet1; // reorder
            jet1 = jet;
          }
        }else if(pt > jet2.Pt()){
            jet2 = jet;
        }
      }else{
        TLorentzVector jet_jer;
        // do SMEARING only
        
        // b tag weight before smearing
        if(pt>m_AK4jetPtCut)
          b_weightbtag_ *= m_BTaggingScaleTool.getScaleFactor(Jets.at(ijet));
        
        jet_jer = m_JetCorrectionTool.GetCorrectedJetJER(Jets.at(ijet),m_genJetAK4);
        pt = jet_jer.Pt();
        
        // reorder pt
        if(pt > jet1.Pt()){
          if(jet1.Pt()<20){ // jet1 is unset
            jet1 = jet_jer;
          }else{ // jet1 is already set - reorder
            jet2 = jet1;    // reorder
            jet1 = jet_jer;
          }
        }
        else if(pt > jet2.Pt()){
            jet2 = jet_jer;
        }
        
        Jets.at(ijet).pt(pt);          // correct UZH::Jet object's pt
        Jets.at(ijet).e(jet_jer.E());  // correct UZH::Jet object's e
        if(pt<m_AK4jetPtCut) continue; // only count >20 GeV jets
        
        met -= jet_jer - jet;          // propagate smearing to MET
        jet = jet_jer;
      }
      ht += Jets.at(ijet).e();
      
      // count jets
      if(abseta < 2.4){             // CENTRAL 20 GeV
        ncjets20++;                 //  jets
        if(pt > 30){                // CENTRAL 30 GeV
          if(isBTagged) nbtag++;    //  btag
          ncjets++;                 //  jets
        }
        if(isBTagged){              // CENTRAL 20 GeV b jet
          nbtag20++;                //  btag
          if(pt>bjet1.Pt()){ // bjet TLorentzVectors
            if(bjet1.Pt()<20){
              bjet1 = jet; // set bjet1 for first time
              bcsv1 = Jets.at(ijet).csv();
              bdeepcsv1 = Jets.at(ijet).deepCSV();
            }else{ // bjet1 is already set - reorder
              bjet2 = bjet1; bjet1 = jet;
              bcsv2 = bcsv1; bcsv1 = Jets.at(ijet).csv();
              bdeepcsv2 = bdeepcsv1; bdeepcsv1 = Jets.at(ijet).deepCSV();
            }
          }else if(pt>bjet2.Pt()){
              bjet2 = jet;
              bcsv2 = Jets.at(ijet).csv();
              bdeepcsv2 = Jets.at(ijet).deepCSV();
          }
        }
      }
      else if(abseta > 2.4){        // FORWARD 20 GeV
        nfjets20++;                 //  jets
        if(pt > 30){                // FORWARD 30 GeV
          nfjets++;                 //  jets
        }
      }
  }
  
  // jet multiplicities
  njets         = ncjets + nfjets;    njets20         = ncjets20 + nfjets20;
  b_njets[ch]   = njets;              b_njets20[ch]   = njets20;
  b_nfjets[ch]  = nfjets;             b_nfjets20[ch]  = nfjets20;
  b_ncjets[ch]  = ncjets;             b_ncjets20[ch]  = ncjets20;
  b_nbtag[ch]   = nbtag;              b_nbtag20[ch]   = nbtag20;
  b_ht[ch]      = ht;
  
  // jet kinematics
  if(njets20 > 1){
    b_jpt_1[ch] = jet1.Pt();    b_jeta_1[ch] = jet1.Eta();    b_jphi_1[ch] = jet1.Phi();
    b_jpt_2[ch] = jet2.Pt();    b_jeta_2[ch] = jet2.Eta();    b_jphi_2[ch] = jet2.Phi();
  }else if(njets20 == 1){
    b_jpt_1[ch] = jet1.Pt();    b_jeta_1[ch] = jet1.Eta();    b_jphi_1[ch] = jet1.Phi();
    b_jpt_2[ch] = -1;           b_jeta_2[ch] = -9;            b_jphi_2[ch] = -9;
  }else{
    b_jpt_1[ch] = -1;           b_jeta_1[ch] = -9;            b_jphi_1[ch] = -9;
    b_jpt_2[ch] = -1;           b_jeta_2[ch] = -9;            b_jphi_2[ch] = -9;
  }
  
  // b jets
  if(bjet1.Pt() > m_AK4jetPtCut){
    b_bpt_1[ch]      = bjet1.Pt();
    b_beta_1[ch]     = bjet1.Eta();
    b_bphi_1[ch]     = bjet1.Phi();
    b_bcsv_1[ch]     = bcsv1;
    b_bdeepcsv_1[ch] = bdeepcsv1;
  }else{
    b_bpt_1[ch]      = -1;
    b_beta_1[ch]     = -9;
    b_bphi_1[ch]     = -9;
    b_bcsv_1[ch]     = -1;
  }
  if(bjet2.Pt() > m_AK4jetPtCut){
    b_bpt_2[ch]      = bjet2.Pt();
    b_beta_2[ch]     = bjet2.Eta();
    b_bphi_2[ch]     = bjet2.Phi();
    b_bcsv_2[ch]     = bcsv2;
    b_bdeepcsv_2[ch] = bdeepcsv2;
  }else{
    b_bpt_2[ch]      = -1;
    b_beta_2[ch]     = -9;
    b_bphi_2[ch]     = -9;
    b_bcsv_2[ch]     = -1;
  }
   
}





void DiMuonAnalysis::countJets(const TLorentzVector& jet, Int_t& ncjets, Int_t& nfjets, Int_t& nbtags, const bool isBTagged){
  //std::cout << "countJets" << std::endl;
  if(jet.Pt()<30) return;
  Float_t abseta = fabs(jet.Eta());
  if(abseta<2.4){         // CENTRAL 30 GeV
    if(isBTagged) nbtags++;
    ncjets++;
  }
  else if(abseta>2.4){    // FORWARD 30 GeV
    nfjets++;
  }
  return;
}





void DiMuonAnalysis::setGenBosonTLVs(){
  //std::cout << "setGenBosonTLVs" << std::endl;
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Computation_of_generator_Z_W_Hig
  int nLep = 0;
  boson_tlv = TLorentzVector();
  for( int p=0; p<(int)m_genParticle.pdgId->size(); ++p ){
    UZH::GenParticle particle( &m_genParticle, p );
    float PID = abs(particle.pdgId());
    if(((PID==13 or PID==11) and particle.status()==1 and particle.fromHardProcessFinalState()) or
        (PID==15 and particle.status()==2 and abs(particle.mother()[0])<30)){
      nLep++;
      boson_tlv += particle.tlv();
      //if(nLep>2){
      //   std::cout<<" nLep="<<nLep<<" "<<std::setw(10)<<PID
      //            <<", M="<<std::setw(7)<<particle.mother()[0]<<", pt="<<std::setw(8)<<particle.pt()
      //            <<", status "<<std::setw(2)<<particle.status()<<", HPFS="<<particle.fromHardProcessFinalState()<<std::endl;   
      //}
      //if(nLep==2) break;
    }
  }
}






int DiMuonAnalysis::genMatch(Float_t lep_eta, Float_t lep_phi) {
  //std::cout << "genMatch" << std::endl;
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
  for( int p=0; p<(int)m_genParticle.pdgId->size(); ++p ){
    UZH::GenParticle particle( &m_genParticle, p );
    
    Float_t pt      = particle.pt();
    Float_t eta     = particle.eta();
    Float_t phi     = particle.phi();
    Int_t pdgId     = abs(particle.pdgId());
    Int_t isPrompt  = particle.isPrompt();
    Int_t isDirectPromptTauDecayProduct = particle.isDirectPromptTauDecayProduct();
    
    if(particle.status()!=1) continue;
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
    //m_genParticle.taudecay
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





Float_t DiMuonAnalysis::deltaPhi(Float_t p1, Float_t p2){
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





Float_t DiMuonAnalysis::deltaR(Float_t deta, Float_t dphi){
  //std::cout << "deltaR" << std::endl;
  return TMath::Sqrt(TMath::Power(deta,2) + TMath::Power(dphi,2));
}





void DiMuonAnalysis::printRow(const std::vector<std::string> svec, const std::vector<int> ivec, const std::vector<double> dvec, const std::vector<float> fvec, const int w){ 
  for(auto const& el: svec) std::cout << std::setw(w) << el;
  for(auto const& el: ivec) std::cout << std::setw(w) << el;
  for(auto const& el: fvec) std::cout << std::setw(w) << el;
  for(auto const& el: dvec) std::cout << std::setw(w) << el;
  std::cout << std::endl;
}





bool DiMuonAnalysis::LooseJetID(const UZH::Jet& jet) {
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Recommendations_for_13_TeV_data
  // https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2016
  Float_t eta  = fabs(jet.eta());
  Float_t NHF  = jet.nhf();  //neutralHadronEnergyFraction();
  Float_t NEMF = jet.nemf(); //neutralEmEnergyFraction();
  Float_t NM   = jet.nm();   //neutralMultiplicity();
  Float_t CM   = jet.cm();   //chargedMultiplicity();
  
  if(eta <= 2.4){
    Float_t CHF  = jet.chf();  //chargedHadronEnergyFraction();
    Float_t CEMF = jet.cemf(); //chargedEmEnergyFraction();
    return NHF < 0.99 and NEMF < 0.99 and NM+CM > 1 and
           CHF > 0    and CEMF < 0.99 and    CM > 0;
  }
  else if(eta <= 2.7){
    return NHF < 0.99 and NEMF < 0.99 and NM+CM > 1;
  }
  else if(eta <= 3.0){
    //return NEMF < 0.90 && NM > 2;
    return NEMF > 0.01 and NHF < 0.98 and NM > 2;
  }
  else if(eta  < 4.7){
    return NEMF < 0.90 and NM > 10;
  }
  return false;
}





float DiMuonAnalysis::genMatchSF(const std::string& channel, const int genmatch_2, const float tau_eta){
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
  if      (genmatch_2 == 1) {
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
  else if (genmatch_2 == 2) {
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
      std::cout << ">>> DiMuonAnalysis::genMatchSF: genmatch_2 = 66, qq = " << qq << " != -36 !!!" << std::endl;
    }
  }
  
  return 1.0;
}





void DiMuonAnalysis::shiftLeptonAndMET(const float shift, TLorentzVector& lep_shifted, TLorentzVector& met_shifted){
  //std::cout << "shiftLeptonAndMET" << std::endl;
  
  //std::cout << ">>> after:  lep_shifted pt = " << lep_shifted.Pt()  << ", m   = " << lep_shifted.M() << std::endl;
  TLorentzVector Delta_lep_tlv(lep_shifted.Px()*shift, lep_shifted.Py()*shift, 0, 0); // (dpx,dpy,0,0)
  lep_shifted *= (1.+shift);
  TLorentzVector met_diff;
  met_diff.SetPtEtaPhiM(met_shifted.Pt(),met_shifted.Eta(),met_shifted.Phi(),0.); // MET(px,dpy,0,0) - (dpx,dpy,0,0)
  met_diff -= Delta_lep_tlv;
  met_shifted.SetPtEtaPhiM(met_diff.Pt(),0,met_diff.Phi(),0.); // keep E = |p| !
}





void DiMuonAnalysis::shiftMET(TLorentzVector& shift, UZH::MissingEt& met){
  TLorentzVector met_tlv_shifted;
  met_tlv_shifted.SetPxPyPzE(met.et()*TMath::Cos(met.phi()), met.et()*TMath::Sin(met.phi()), 0, met.et());
  met_tlv_shifted -= shift;
  met_tlv_shifted.SetPtEtaPhiM(met_tlv_shifted.Pt(),0,met_tlv_shifted.Phi(),0.); // keep E = |p| !
  met.et(met_tlv_shifted.Pt());
  met.phi(met_tlv_shifted.Phi());
}





void DiMuonAnalysis::extraLeptonVetos(const std::string& channel, const UZH::Muon& muon1, const UZH::Muon& muon2){
  //std::cout << "extraLeptonVetos" << std::endl;
  
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
    if(mymuon.isMediumMuonGH() < 0.5) continue;   // for period GH and MC (see AN)
    if(mymuon.pt()!=muon1.pt() and mymuon.eta()!=muon1.eta() and mymuon.phi()!=muon1.phi() and
       mymuon.pt()!=muon2.pt() and mymuon.eta()!=muon2.eta() and mymuon.phi()!=muon2.phi()){
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
    
    // extra electron veto
    if(myelectron.passConversionVeto() and
       myelectron.isMVATightElectron() and 
       myelectron.expectedMissingInnerHits() <= 1){
       b_extraelec_veto_ = true;
    }
  }
  
}





bool DiMuonAnalysis::getBTagStatus_promote_demote( UZH::Jet& jet ) {
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

