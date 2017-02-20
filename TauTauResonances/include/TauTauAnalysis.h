// Dear emacs, this is -*- c++ -*-
// $Id: CycleCreators.py 344 2012-12-13 13:10:53Z krasznaa $
#ifndef TauTauAnalysis_H
#define TauTauAnalysis_H

// SFrame include(s):
#include "core/include/SCycleBase.h"

// ROOT include(s):
//#include <TBits.h>
//#include "TMatrixD.h"
// External include(s):
#include "../NtupleVariables/include/JetNtupleObject.h"
#include "../NtupleVariables/include/Jet.h"
#include "../NtupleVariables/include/EventInfoNtupleObject.h"
#include "../NtupleVariables/include/ElectronNtupleObject.h"
#include "../NtupleVariables/include/Electron.h"
#include "../NtupleVariables/include/MuonNtupleObject.h"
#include "../NtupleVariables/include/Muon.h"
#include "../NtupleVariables/include/TauNtupleObject.h"
#include "../NtupleVariables/include/Tau.h"
#include "../NtupleVariables/include/MissingEtNtupleObject.h"
#include "../NtupleVariables/include/MissingEt.h"
#include "../NtupleVariables/include/GenParticleNtupleObject.h"
#include "../NtupleVariables/include/GenParticle.h"
#include "../GoodRunsLists/include/TGoodRunsList.h"
#include "../PileupReweightingTool/include/PileupReweightingTool.h"
#include "../BTaggingTools/include/BTaggingScaleTool.h"
#include "../LepEff2016/interface/ScaleFactorTool.h"
#include "../RecoilCorrections/interface/RecoilCorrector.h"
#include "../SVFitTools/interface/SVFitTool.h"
#include "../SVFitTools/interface/SVfitStandaloneAlgorithm.h"
//#include "../SVFit/include/NSVfitStandaloneAlgorithm.h"
//#include "../SVfitStandalone/interface/SVfitStandaloneAlgorithm.h"
//#include "../SVfitStandalone/interface/SVfitStandaloneLikelihood.h"

//class TH1D;
//class TH2D;
//class TRandom3;
//class TBits;

#include <TFile.h>
#include <TTree.h>
#include <TMath.h>
#include "TRandom3.h"



namespace UZH {
  class Jet;
  class Electron;
  class Muon;
  class Tau;
  class MissingEt;
  class GenParticle;
}



/**
 *   @short Class to run Tau Tau Analysis
 *
 *          Put a longer description over here...
 *
 *  @author Izaak Neutelings and Yuta Takahasi (from Camilla Galloni's code)
 *  @version $Revision: 344 $
 */
class TauTauAnalysis : public SCycleBase {

  public:
  
    // enumeration of all cut flags
    typedef enum {
      kBeforeCuts,            // C0
      kJSON,                  // C1
      kTrigger,               // C2
      kMetFilters,            // C3
      kLepton,                // C4
      kLepTau,                // C6
      kBeforeCutsWeighted,    // C7
      kNumCuts                // last!
    } SelectionCuts;
  
    // static array of all cut names
    const std::string kCutName[ kNumCuts ] = {
      "BeforeCuts",             // C0
      "JSON",                   // C1
      "Trigger",                // C2
      "MetFilters",             // C3
      "Lepton",                 // C4
      "LepTau",                 // C6
      "BeforeCutsWeighted",     // C7
    };
    
    
    // default constructor and destructor
    TauTauAnalysis();  // default constructor
    ~TauTauAnalysis(); // default destructor
    
    // SFrame
    virtual void BeginCycle() throw( SError );                        // called beginning of the cycle
    virtual void EndCycle()   throw( SError );                        // called at the end of the cycle
    virtual void BeginInputData( const SInputData& ) throw( SError ); // called at the beginning of a new input data
    virtual void EndInputData  ( const SInputData& ) throw( SError ); // called after finishing to process an input data
    virtual void BeginInputFile( const SInputData& ) throw( SError ); // called after opening each new input file
    virtual void ExecuteEvent(   const SInputData&, Double_t    ) throw( SError ); // called for every event
    virtual bool isGoodEvent(    int runNumber, int lumiSection );    // check good lumi section
    
    
    /// Function to book tree branches
    //virtual void FillBranches(const std::string& channel,  const std::vector<UZH::Jet>& Jet, const UZH::Tau& tau, const  TLorentzVector& lepton, const UZH::MissingEt& met );
    virtual void FillBranches( const std::string& channel, const std::vector<UZH::Jet>& Jet,
                               const UZH::Tau& tau, const int taugen, const UZH::Muon& muon, const UZH::Electron& electron,
                               const UZH::MissingEt& met, const UZH::MissingEt& puppimet );//, const UZH::MissingEt& mvamet=NULL);
    
    // check pass of triggers / MET filters
    virtual TString passTrigger( int runNumber );
    virtual bool passMETFilters();
    
    // obtain event weights for MC
    virtual void getEventWeight();
    
    // GenFilter to select Z to tautau events
    virtual void genFilterZtautau();
    
    // set tlv of generator boson for recoil corrections
    virtual void setGenBosonTLVs();
    
    // match reco objects to taus
    virtual int genMatch( Float_t lep_eta, Float_t lep_phi );
    
    // help function
    virtual Float_t deltaPhi( Float_t p1, Float_t p2 );
    virtual Float_t deltaR(   Float_t p1, Float_t p2 );
    virtual void shiftLeptonAndMET( const float shift, TLorentzVector& lep_shifted, TLorentzVector& met_shifted, bool shiftEnergy = false );
    
    // IDs
    //virtual bool isNonTrigElectronID( const UZH::Electron& electron );
    virtual bool LooseJetID( const UZH::Jet& jet );
    
    // extra scaling factors
    virtual float genMatchSF( const std::string& channel, const int genmatch_2, const float tau_eta = 0. );
    virtual bool  getBTagWeight_promote_demote( const UZH::Jet& jet );
    
    // checks
    virtual void checks();
    virtual void cutflowCheck( const std::string& channel );
    virtual void visiblePTCheck();
    
    /// fill cut flow
    //virtual void fillCutflow( const std::string histName, const std::string dirName, const Int_t id, const Double_t weight = 1.);
    virtual void fillCutflow( TString histName, TString dirName, const Int_t id, const Double_t weight = 1. );
    virtual void printCutFlow( const std::string& ch, const std::string& name, const TString hname, const TString dirname, std::vector<std::string> cutName );
    
    
    
  private:
    
    
    ///
    /// INPUT VARIABLE OBJECTS:
    ///
    
    Ntuple::JetNtupleObject         m_jetAK4;         ///< jet container
    Ntuple::EventInfoNtupleObject   m_eventInfo;      ///< event info container
    Ntuple::ElectronNtupleObject    m_electron;       ///< electron container
    Ntuple::MuonNtupleObject        m_muon;           ///< muon container
    Ntuple::TauNtupleObject         m_tau;            ///< tau container
    Ntuple::MissingEtNtupleObject   m_missingEt;      ///< missing E_T container
    Ntuple::MissingEtNtupleObject   m_puppimissingEt; ///< missing E_T container
    //Ntuple::MissingEtNtupleObject   m_mvamissingEt;   ///< missing E_T container
    Ntuple::GenParticleNtupleObject m_genParticle;    ///< gen particle container
    
    
    ///
    /// OTHER OBJECTS
    ///
    
    Root::TGoodRunsList m_grl;
    PileupReweightingTool m_PileupReweightingTool;
    BTaggingScaleTool m_BTaggingScaleTool;
    ScaleFactorTool m_ScaleFactorTool;
    RecoilCorrectorTool m_RecoilCorrector;
    SVFitTool m_SVFitTool;
    
    //TLorentzVector applySVFitSemileptonic (float cov00, float cov10, float cov11, float met, float met_phi, TLorentzVector lep1 , TLorentzVector lep2);
    //TLorentzVector applySVFitHadronic     (float cov00, float cov10, float cov11, float met, float met_phi, TLorentzVector lep1 , TLorentzVector lep2);
    //TLorentzVector applySVFit             (float cov00, float cov10, float cov11, float met, float met_phi, TLorentzVector lep1 , TLorentzVector lep2);
    //float applySVFit(float cov00, float cov10, float cov11, float met, float met_phi, TLorentzVector lep1 , TLorentzVector lep2, const std::string& channel);
    
    void extraLeptonVetos(const std::string& channel, const UZH::Muon& muon, const UZH::Electron& electron);
    
    // naming
    std::string m_recoTreeName;                     ///< name of tree with reconstructed objects in ntuple
    // std::string m_outputTreeName;                ///< name of output tree
    std::vector<std::string> m_outputTreeName_ch_;  ///< name of output trees for analysis
    std::vector<std::string> channels_;

    int m_ntupleLevel;                ///< cut at which branches for ntuple are written out
    std::string m_jetAK4Name;         ///< name of AK4 jet collection in tree with reconstructed objects
    std::string m_electronName;       ///< name of electron collection in tree with reconstructed objects
    std::string m_muonName;           ///< name of muon collection in tree with reconstructed objects
    std::string m_tauName;            ///< name of tau collection in tree with reconstructed objects
    std::string m_missingEtName;      ///< name of missing E_T collection in tree with reconstructed objects
    std::string m_genParticleName;    ///< name of gen particle collection in tree with reconstructed objects
  
    // XML flags for TauTauAnalysis
    bool      m_isData;
    bool      m_isSignal;
    bool      m_applyMETFilters;
    bool      m_doSVFit;
    bool      m_doRecoilCorr;
    bool      m_doZpt;
    bool      m_doTTpt;
    bool      m_doTES;
    double    m_TESshift;
    bool      m_doEES;
    double    m_EESshift;
    double    m_EESshiftEndCap;
    bool      m_doLTF;
    double    m_LTFshift;

    ///
    /// CUTS
    ///
     
    // jet
    double    m_jetPtCut;         ///< cut on jet pT
    double    m_jetEtaCut;        ///< cut on jet eta
    double    m_AK4jetPtCut;      ///< cut on jet pT
    double    m_AK4jetEtaCut;     ///< cut on jet eta
    double    m_CSVWorkingPoint;
    
    // b-tagging
    double    m_csvMin;
    
    // electrons
    double    m_electronPtCut;
    double    m_electronEtaCut;
    double    m_electronD0Cut;
    double    m_electronDzCut;
    double    m_electronIsoCut;
    
    // muons
    double    m_muonPtCut;
    double    m_muonEtaCut;
    double    m_muonD0Cut;
    double    m_muonDzCut;
    double    m_muonIsoCut;
    
    // leptons = muons and electrons
    double    m_leptonPtCut;
    double    m_leptonEtaCut;
    
    // taus
    double    m_tauPtCut;
    double    m_tauEtaCut;
    double    m_tauDzCut;
    
    // MET
    double    m_metCut;
    
    
    ///
    /// FILE NAME
    ///
    
    std::string m_jsonName;
    //std::string m_TrigSF_muonName;
    //std::string m_IDSF_muonName;
    //std::string m_IsoSF_muonName;
    //std::string m_IDSF_eleName;

    // other variables needed
    //std::vector<std::string> m_triggerNames_mutau;
    //std::vector<std::string> m_triggerNames_eletau;
    struct UnPreScaledRun{ int start; int end;};
    //UnPreScaledRun initializeUnPreScaledRun( int start, int end ){ UnPreScaledRun run = { start, end }; return run; }
    std::map<std::string,UnPreScaledRun> m_triggerNamesToRun_mutau;
    std::map<std::string,UnPreScaledRun> m_triggerNamesToRun_etau;
    std::map<std::string,UnPreScaledRun> m_triggerNamesToRun_emu;
    
    int mu_tau;
    int ele_tau;
    
    
    ///
    /// BRANCHES
    ///
    
    double b_weight_;
    double b_genweight_;
    double b_puweight_;
    double b_weightbtag_;
    double b_npu_;
    double b_dR_ll_gen_ = -1;
    Int_t b_isData_;
    
    bool b_dilepton_veto_;
    bool b_extraelec_veto_;
    bool b_extramuon_veto_;
    
    //double b_weightBtag;
    //double b_weightBtag_veto;
    
    bool GenEvent_Htata_filter;
    bool GenEvent_Ztata_filter;
    
    TLorentzVector boson_tlv;
    TLorentzVector boson_tlv_vis;
    
    
    // synchronisation:
    // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#Synchronisation
    
    std::map<std::string,Double_t> b_weight;
    std::map<std::string,Double_t> b_genweight;
    std::map<std::string,Double_t> b_puweight;
    std::map<std::string,Double_t> b_weightbtag;
    //std::map<std::string,Double_t> b_genmatchweight;
    std::map<std::string,Double_t> b_zptweight;
    std::map<std::string,Double_t> b_ttptweight;
    std::map<std::string,Int_t>    b_channel;  // 1 mutau; 2 eletau;
    std::map<std::string,Int_t>    b_isData;
    
    std::map<std::string,Int_t>    b_run;
    std::map<std::string,Int_t>    b_evt;
    std::map<std::string,Int_t>    b_lum;
    
    std::map<std::string,Int_t>    b_npv;
    std::map<std::string,Int_t>    b_npu; 
    std::map<std::string,Int_t>    b_NUP;
    std::map<std::string,Double_t> b_rho;
    
    std::map<std::string,Int_t>    b_njets;
    std::map<std::string,Int_t>    b_nfjets;
    std::map<std::string,Int_t>    b_ncjets;
    std::map<std::string,Int_t>    b_nbtag;
    std::map<std::string,Int_t>    b_ncbtag;
    std::map<std::string,Int_t>    b_nfbtag;
    std::map<std::string,Int_t>    b_njets20;
    std::map<std::string,Int_t>    b_nfjets20;
    std::map<std::string,Int_t>    b_ncjets20;
    std::map<std::string,Int_t>    b_nbtag20;
    std::map<std::string,Int_t>    b_ncbtag20;
    std::map<std::string,Int_t>    b_nfbtag20;
    
    std::map<std::string,Double_t> b_pt_1;
    std::map<std::string,Double_t> b_eta_1;
    std::map<std::string,Double_t> b_phi_1;
    std::map<std::string,Double_t> b_m_1;
    std::map<std::string,Int_t>    b_q_1;
    std::map<std::string,Double_t> b_d0_1;
    std::map<std::string,Double_t> b_dz_1;
    //std::map<std::string,Double_t> b_mt_1;
    std::map<std::string,Double_t> b_pfmt_1;
    std::map<std::string,Double_t> b_puppimt_1;
    std::map<std::string,Double_t> b_iso_1;
    std::map<std::string,Int_t>    b_id_e_mva_nt_loose_1;
    std::map<std::string,Int_t>    b_id_e_mva_nt_loose_1_old;
    std::map<std::string,Int_t>    b_gen_match_1;
    std::map<std::string,Double_t> b_trigweight_1;
    //std::map<std::string,Double_t> b_idweight_1;
    //std::map<std::string,Double_t> b_isoweight_1;
    std::map<std::string,Double_t> b_idisoweight_1;
    
    std::map<std::string,Double_t> b_pt_2;
    std::map<std::string,Double_t> b_eta_2;
    std::map<std::string,Double_t> b_phi_2;
    std::map<std::string,Double_t> b_m_2;
    std::map<std::string,Int_t>    b_q_2;
    std::map<std::string,Double_t> b_d0_2;
    std::map<std::string,Double_t> b_dz_2;
    std::map<std::string,Double_t> b_mt_2;
    std::map<std::string,Double_t> b_pfmt_2;
    std::map<std::string,Double_t> b_puppimt_2;
    std::map<std::string,Double_t> b_iso_2;
    std::map<std::string,Double_t> b_iso_2_medium;
    std::map<std::string,Int_t>    b_gen_match_2;
    std::map<std::string,Int_t>    b_trigweight_2;
    //std::map<std::string,Double_t> b_isoweight_2;
    //std::map<std::string,Double_t> b_idweight_2;
    std::map<std::string,Double_t> b_idisoweight_2;
    std::map<std::string,Double_t> b_pol_2;
    
    std::map<std::string,Double_t> b_againstElectronVLooseMVA6_2;
    std::map<std::string,Double_t> b_againstElectronLooseMVA6_2;
    std::map<std::string,Double_t> b_againstElectronMediumMVA6_2;
    std::map<std::string,Double_t> b_againstElectronTightMVA6_2;
    std::map<std::string,Double_t> b_againstElectronVTightMVA6_2;
    std::map<std::string,Double_t> b_againstMuonLoose3_2;
    std::map<std::string,Double_t> b_againstMuonTight3_2;
    std::map<std::string,Double_t> b_byCombinedIsolationDeltaBetaCorrRaw3Hits_2;
    std::map<std::string,Double_t> b_byIsolationMVA3newDMwLTraw_2;
    std::map<std::string,Double_t> b_byIsolationMVA3oldDMwLTraw_2;
    std::map<std::string,Double_t> b_chargedIsoPtSum_2;
    std::map<std::string,Double_t> b_neutralIsoPtSum_2;
    std::map<std::string,Double_t> b_puCorrPtSum_2;
    std::map<std::string,Double_t> b_decayModeFindingOldDMs_2;
    std::map<std::string,Double_t> b_decayMode_2;
    
    std::map<std::string,Int_t>    b_dilepton_veto;
    std::map<std::string,Int_t>    b_extraelec_veto;
    std::map<std::string,Int_t>    b_extramuon_veto;
    std::map<std::string,Int_t>    b_lepton_vetos;
    
    std::map<std::string,Double_t> b_jpt_1;
    std::map<std::string,Double_t> b_jeta_1;
    std::map<std::string,Double_t> b_jphi_1;
    std::map<std::string,Double_t> b_jpt_2;
    std::map<std::string,Double_t> b_jeta_2;
    std::map<std::string,Double_t> b_jphi_2;
    
    std::map<std::string,Double_t> b_bpt_1;
    std::map<std::string,Double_t> b_beta_1;
    std::map<std::string,Double_t> b_bphi_1;
    std::map<std::string,Double_t> b_bcsv_1;
    std::map<std::string,Double_t> b_bpt_2;
    std::map<std::string,Double_t> b_beta_2;
    std::map<std::string,Double_t> b_bphi_2;
    std::map<std::string,Double_t> b_bcsv_2;
    
    std::map<std::string,Double_t> b_met;
    std::map<std::string,Double_t> b_met_old;
    std::map<std::string,Double_t> b_metphi;
    //std::map<std::string,Double_t> b_metcorrphi;
    std::map<std::string,Double_t> b_puppimet;
    std::map<std::string,Double_t> b_puppimetphi;
    //std::map<std::string,Double_t> b_mvamet;
    //std::map<std::string,Double_t> b_mvamet_old;
    //std::map<std::string,Double_t> b_mvametphi;
    
    std::map<std::string,Double_t> b_metcov00;
    std::map<std::string,Double_t> b_metcov01;
    std::map<std::string,Double_t> b_metcov10;
    std::map<std::string,Double_t> b_metcov11;
    //std::map<std::string,Double_t> b_mvacov00;
    //std::map<std::string,Double_t> b_mvacov01;
    //std::map<std::string,Double_t> b_mvacov10;
    //std::map<std::string,Double_t> b_mvacov11;
    
    std::map<std::string,Double_t> b_m_vis;
    std::map<std::string,Double_t> b_pt_tt;
    std::map<std::string,Double_t> b_pt_tt_vis;
    std::map<std::string,Double_t> b_R_pt_m_vis;
    std::map<std::string,Double_t> b_R_pt_m_vis2;
    
    std::map<std::string,Double_t> b_m_sv; 
    //std::map<std::string,Double_t> b_m_sv_pfmet;
    std::map<std::string,Double_t> b_pt_tt_sv;
    std::map<std::string,Double_t> b_R_pt_m_sv;
    
    std::map<std::string,Double_t> b_dR_ll;
    std::map<std::string,Double_t> b_dR_ll_gen;
    std::map<std::string,Double_t> b_dphi_ll_bj;
    std::map<std::string,Double_t> b_mt_tot;
    std::map<std::string,Double_t> b_ht;
    
    std::map<std::string,Double_t> b_m_genboson;
    std::map<std::string,Double_t> b_pt_genboson;
    
    //std::map<std::string,Double_t> b_pt_sv; 
    //std::map<std::string,Double_t> b_eta_sv; 
    //std::map<std::string,Double_t> b_phi_sv;
    std::map<std::string,Double_t> b_pzetamiss;
    std::map<std::string,Double_t> b_pzetavis;
    std::map<std::string,Double_t> b_pzeta_disc;
    
    std::map<std::string,Double_t> b_vbf_mjj;
    std::map<std::string,Double_t> b_vbf_deta;
    std::map<std::string,Double_t> b_vbf_jdphi;
    std::map<std::string,Int_t>    b_vbf_ncentral;
    std::map<std::string,Int_t>    b_vbf_ncentral20;

    // Macro adding the functions for dictionary generation
    ClassDef( TauTauAnalysis, 0 );
  
}; // class TauTauAnalysis

#endif // TauTauAnalysis_H

