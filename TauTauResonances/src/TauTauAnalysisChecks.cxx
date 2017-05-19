// $Id: CycleCreators.py 344 2012-12-13 13:10:53Z krasznaa $

// Local include(s):
#include "../include/TauTauAnalysis.h"






void TauTauAnalysis::makeHistogramsForChecks(){
  //std::cout << "makeHistogramsForChecks" << std::endl;

  // histograms - cutflow
  for (auto ch: channels_){
    TString dirname = "histogram_" + ch;
    TString tch = ch;
    
    if(m_isData){
      int  nperiods=7*2-1;
      float periods[7*2] = { 272007-1, 275376+1,   275657-1, 276283+1,   276315-1, 276811+1,
                             276831-1, 277420+1,   277772-1, 278808+1,   278820-1, 280385+1,   280919-1, 284044+1  };
      Book( TH1F("runnumber", "runnumber", nperiods, periods ), dirname );
    }
    
    // Book( TH1F("lepton_pt",         "lepton_pt",        100,   0, 120 ), dirname);
    // Book( TH1F("lepton_eta",        "lepton_eta",       100,   0, 3.0 ), dirname);
    // Book( TH1F("lepton_ID",         "lepton_ID",          2,   0, 2   ), dirname);
    // Book( TH1F("lepton_N",          "lepton_N",          10,   0, 10  ), dirname);
    // Book( TH1F("lepton_pt_pt23",    "lepton_pt_pt23",   100,   0, 120 ), dirname);
    // Book( TH1F("lepton_eta_pt23",   "lepton_eta_pt23",  100,   0, 3.0 ), dirname);
    // Book( TH1F("lepton_ID_pt23",    "lepton_ID_pt23",     2,   0, 2   ), dirname);
    // Book( TH1F("lepton_N_pt23",     "lepton_N_pt23",     10,   0, 10  ), dirname);
    // Book( TH1F("lepton_pt_2p4",     "lepton_pt_2p4",    100,   0, 120 ), dirname);
    // Book( TH1F("lepton_eta_2p4",    "lepton_eta_2p4",   100,   0, 3.0 ), dirname);
    // Book( TH1F("lepton_ID_2p4",     "lepton_ID_2p4",      2,   0, 2   ), dirname);
    // Book( TH1F("lepton_N_2p4",      "lepton_N_2p4",      10,   0, 10  ), dirname);
    // Book( TH1F("lepton_pt_vtx",     "lepton_pt_vtx",    100,   0, 120 ), dirname);
    // Book( TH1F("lepton_eta_vtx",    "lepton_eta_vtx",   100,   0, 3.0 ), dirname);
    // Book( TH1F("lepton_ID_vtx",     "lepton_ID_vtx",      2,   0, 2   ), dirname);
    Book( TH1F("triggers",          "triggers",          10,   0, 10  ), dirname);
    
    // Book( TH1F("gen_match_1_pt23_eta2p4",  "gen_match_1_pt23_eta2p4", 8, 0, 8 ), dirname);
    // Book( TH1F("gen_match_1_d0_dz",  "gen_match_1_d0_dz", 8, 0, 8 ), dirname);
    // Book( TH1F("gen_match_1_baseline", "gen_match_1_baseline", 8, 0, 8 ), dirname);
    // Book( TH1F("gen_match_2",  "gen_match_2", 8, 0, 8 ), dirname);
    // Book( TH1F("gen_match_2_baseline", "gen_match_2_baseline", 8, 0, 8 ), dirname);
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
}






void TauTauAnalysis::checks(){
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
  
  if( ch == "etau" ) return;
   
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
    //    if(muon.isMediumMuonGH() < 0.5)
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


