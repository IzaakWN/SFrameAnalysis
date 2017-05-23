
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#include "../include/Jet.h"

using namespace std;
using namespace UZH;

Jet::Jet() {
  
}


Jet::Jet( const Ntuple::JetNtupleObject* ana, const Int_t idx ) 
: Basic( idx )
 , Particle() 


  , m_isTagged( false )

{
  m_ana=ana;
  // copy variables defined in Particle.h
    m_e = &((*ana->e)[idx]); 
    m_pt = &((*ana->pt)[idx]); 
    m_eta = &((*ana->eta)[idx]); 
    m_phi = &((*ana->phi)[idx]); 
    m_m = &((*ana->m)[idx]); 

  m_lvl    = ana->detailLevel;


  m_scalefactor = 0;

  // copy rest of variables
  /*${ {AllNoBools:    printf("acc#name#\n"); if (ana->m_connectsucceeded[#index#]) 
         {printf("?\n"); m_#name# = &((*ana->#name#)[idx]);}
    else {printf("fak\n"); m_#name# = new #type#(); *m_#name# = #default#; } }}
  */
if(  ((ana->detailLevel & Ntuple::JetAnalysis) == Ntuple::JetAnalysis)  ) {
     if (ana->m_connectsucceeded[3]) m_IDLoose = ((*ana->IDLoose)[idx]); else m_IDLoose = 0; 
    if (ana->m_connectsucceeded[4]) m_IDTight = ((*ana->IDTight)[idx]); else m_IDTight = 0; 
    if (ana->m_connectsucceeded[5]) m_jec = &((*ana->jec)[idx]); else m_jec = 0; 
    if (ana->m_connectsucceeded[6]) m_jecUp = &((*ana->jecUp)[idx]); else m_jecUp = 0; 
    if (ana->m_connectsucceeded[7]) m_jecDown = &((*ana->jecDown)[idx]); else m_jecDown = 0; 
    if (ana->m_connectsucceeded[8]) m_muf = &((*ana->muf)[idx]); else m_muf = 0; 
    if (ana->m_connectsucceeded[9]) m_phf = &((*ana->phf)[idx]); else m_phf = 0; 
    if (ana->m_connectsucceeded[10]) m_emf = &((*ana->emf)[idx]); else m_emf = 0; 
    if (ana->m_connectsucceeded[11]) m_nhf = &((*ana->nhf)[idx]); else m_nhf = 0; 
    if (ana->m_connectsucceeded[12]) m_chf = &((*ana->chf)[idx]); else m_chf = 0; 
    if (ana->m_connectsucceeded[13]) m_area = &((*ana->area)[idx]); else m_area = 0; 
    if (ana->m_connectsucceeded[14]) m_cm = &((*ana->cm)[idx]); else m_cm = 0; 
    if (ana->m_connectsucceeded[15]) m_nm = &((*ana->nm)[idx]); else m_nm = 0; 
    if (ana->m_connectsucceeded[16]) m_che = &((*ana->che)[idx]); else m_che = 0; 
    if (ana->m_connectsucceeded[17]) m_ne = &((*ana->ne)[idx]); else m_ne = 0; 
    if (ana->m_connectsucceeded[18]) m_hf_hf = &((*ana->hf_hf)[idx]); else m_hf_hf = 0; 
    if (ana->m_connectsucceeded[19]) m_hf_emf = &((*ana->hf_emf)[idx]); else m_hf_emf = 0; 
    if (ana->m_connectsucceeded[20]) m_hof = &((*ana->hof)[idx]); else m_hof = 0; 
    if (ana->m_connectsucceeded[21]) m_chm = &((*ana->chm)[idx]); else m_chm = 0; 
    if (ana->m_connectsucceeded[22]) m_neHadMult = &((*ana->neHadMult)[idx]); else m_neHadMult = 0; 
    if (ana->m_connectsucceeded[23]) m_phoMult = &((*ana->phoMult)[idx]); else m_phoMult = 0; 
    if (ana->m_connectsucceeded[24]) m_nemf = &((*ana->nemf)[idx]); else m_nemf = 0; 
    if (ana->m_connectsucceeded[25]) m_cemf = &((*ana->cemf)[idx]); else m_cemf = 0; 
} // end of detail level Analysis

if(  ((ana->detailLevel & Ntuple::JetBasic) == Ntuple::JetBasic)  ) {
     if (ana->m_connectsucceeded[1]) m_csv = &((*ana->csv)[idx]); else m_csv = 0; 
    if (ana->m_connectsucceeded[2]) m_charge = &((*ana->charge)[idx]); else m_charge = 0; 
} // end of detail level Basic

if(  ((ana->detailLevel & Ntuple::JetJER) == Ntuple::JetJER)  ) {
     if (ana->m_connectsucceeded[56]) m_jer_sf = &((*ana->jer_sf)[idx]); else m_jer_sf = 0; 
    if (ana->m_connectsucceeded[57]) m_jer_sf_up = &((*ana->jer_sf_up)[idx]); else m_jer_sf_up = 0; 
    if (ana->m_connectsucceeded[58]) m_jer_sf_down = &((*ana->jer_sf_down)[idx]); else m_jer_sf_down = 0; 
    if (ana->m_connectsucceeded[59]) m_jer_sigma_pt = &((*ana->jer_sigma_pt)[idx]); else m_jer_sigma_pt = 0; 
} // end of detail level JER

if(  ((ana->detailLevel & Ntuple::JetSoftdropSubjets) == Ntuple::JetSoftdropSubjets)  ) {
     if (ana->m_connectsucceeded[43]) m_subjet_softdrop_N = &((*ana->subjet_softdrop_N)[idx]); else m_subjet_softdrop_N = 0; 
    if (ana->m_connectsucceeded[44]) m_subjet_softdrop_pt = &((*ana->subjet_softdrop_pt)[idx]); else m_subjet_softdrop_pt = 0; 
    if (ana->m_connectsucceeded[45]) m_subjet_softdrop_eta = &((*ana->subjet_softdrop_eta)[idx]); else m_subjet_softdrop_eta = 0; 
    if (ana->m_connectsucceeded[46]) m_subjet_softdrop_phi = &((*ana->subjet_softdrop_phi)[idx]); else m_subjet_softdrop_phi = 0; 
    if (ana->m_connectsucceeded[47]) m_subjet_softdrop_e = &((*ana->subjet_softdrop_e)[idx]); else m_subjet_softdrop_e = 0; 
    if (ana->m_connectsucceeded[48]) m_subjet_softdrop_m = &((*ana->subjet_softdrop_m)[idx]); else m_subjet_softdrop_m = 0; 
    if (ana->m_connectsucceeded[49]) m_subjet_softdrop_csv = &((*ana->subjet_softdrop_csv)[idx]); else m_subjet_softdrop_csv = 0; 
    if (ana->m_connectsucceeded[50]) m_subjet_softdrop_charge = &((*ana->subjet_softdrop_charge)[idx]); else m_subjet_softdrop_charge = 0; 
} // end of detail level SoftdropSubjets

if(  ((ana->detailLevel & Ntuple::JetSoftdropSubjetsTruth) == Ntuple::JetSoftdropSubjetsTruth)  ) {
     if (ana->m_connectsucceeded[51]) m_subjet_softdrop_partonFlavour = &((*ana->subjet_softdrop_partonFlavour)[idx]); else m_subjet_softdrop_partonFlavour = 0; 
    if (ana->m_connectsucceeded[52]) m_subjet_softdrop_hadronFlavour = &((*ana->subjet_softdrop_hadronFlavour)[idx]); else m_subjet_softdrop_hadronFlavour = 0; 
    if (ana->m_connectsucceeded[53]) m_subjet_softdrop_genParton_pdgID = &((*ana->subjet_softdrop_genParton_pdgID)[idx]); else m_subjet_softdrop_genParton_pdgID = 0; 
    if (ana->m_connectsucceeded[54]) m_subjet_softdrop_nbHadrons = &((*ana->subjet_softdrop_nbHadrons)[idx]); else m_subjet_softdrop_nbHadrons = 0; 
    if (ana->m_connectsucceeded[55]) m_subjet_softdrop_ncHadrons = &((*ana->subjet_softdrop_ncHadrons)[idx]); else m_subjet_softdrop_ncHadrons = 0; 
} // end of detail level SoftdropSubjetsTruth

if(  ((ana->detailLevel & Ntuple::JetSubstructure) == Ntuple::JetSubstructure)  ) {
     if (ana->m_connectsucceeded[26]) m_tau1 = &((*ana->tau1)[idx]); else m_tau1 = 0; 
    if (ana->m_connectsucceeded[27]) m_tau2 = &((*ana->tau2)[idx]); else m_tau2 = 0; 
    if (ana->m_connectsucceeded[28]) m_tau3 = &((*ana->tau3)[idx]); else m_tau3 = 0; 
    if (ana->m_connectsucceeded[29]) m_pruned_mass = &((*ana->pruned_mass)[idx]); else m_pruned_mass = 0; 
    if (ana->m_connectsucceeded[30]) m_pruned_massCorr = &((*ana->pruned_massCorr)[idx]); else m_pruned_massCorr = 0; 
    if (ana->m_connectsucceeded[31]) m_softdrop_mass = &((*ana->softdrop_mass)[idx]); else m_softdrop_mass = 0; 
    if (ana->m_connectsucceeded[32]) m_softdrop_massCorr = &((*ana->softdrop_massCorr)[idx]); else m_softdrop_massCorr = 0; 
    if (ana->m_connectsucceeded[33]) m_pruned_jec = &((*ana->pruned_jec)[idx]); else m_pruned_jec = 0; 
    if (ana->m_connectsucceeded[34]) m_pruned_jecUp = &((*ana->pruned_jecUp)[idx]); else m_pruned_jecUp = 0; 
    if (ana->m_connectsucceeded[35]) m_pruned_jecDown = &((*ana->pruned_jecDown)[idx]); else m_pruned_jecDown = 0; 
    if (ana->m_connectsucceeded[36]) m_softdrop_jec = &((*ana->softdrop_jec)[idx]); else m_softdrop_jec = 0; 
    if (ana->m_connectsucceeded[37]) m_Hbbtag = &((*ana->Hbbtag)[idx]); else m_Hbbtag = 0; 
} // end of detail level Substructure

if(  ((ana->detailLevel & Ntuple::JetTruth) == Ntuple::JetTruth)  ) {
     if (ana->m_connectsucceeded[38]) m_partonFlavour = &((*ana->partonFlavour)[idx]); else m_partonFlavour = 0; 
    if (ana->m_connectsucceeded[39]) m_hadronFlavour = &((*ana->hadronFlavour)[idx]); else m_hadronFlavour = 0; 
    if (ana->m_connectsucceeded[40]) m_genParton_pdgID = &((*ana->genParton_pdgID)[idx]); else m_genParton_pdgID = 0; 
    if (ana->m_connectsucceeded[41]) m_nbHadrons = &((*ana->nbHadrons)[idx]); else m_nbHadrons = 0; 
    if (ana->m_connectsucceeded[42]) m_ncHadrons = &((*ana->ncHadrons)[idx]); else m_ncHadrons = 0; 
}







}


Jet::~Jet() {

}

ostream& operator<<( ostream& out,
                     const Jet& rhs ) {
  
   out << "Jet -" << ( Basic) rhs; 
   out << "Jet -" << ( Particle ) rhs; 

  out << " isTagged:" << rhs.isTagged();


  out << " JES: " << rhs.getJetSF();

  ;
if(  ((rhs.getLvl() & Ntuple::JetAnalysis) == Ntuple::JetAnalysis)  ) {
   out << " IDLoose " << rhs.IDLoose();
  out << " IDTight " << rhs.IDTight();
  out << " jec " << rhs.jec();
  out << " jecUp " << rhs.jecUp();
  out << " jecDown " << rhs.jecDown();
  out << " muf " << rhs.muf();
  out << " phf " << rhs.phf();
  out << " emf " << rhs.emf();
  out << " nhf " << rhs.nhf();
  out << " chf " << rhs.chf();
  out << " area " << rhs.area();
  out << " cm " << rhs.cm();
  out << " nm " << rhs.nm();
  out << " che " << rhs.che();
  out << " ne " << rhs.ne();
  out << " hf_hf " << rhs.hf_hf();
  out << " hf_emf " << rhs.hf_emf();
  out << " hof " << rhs.hof();
  out << " chm " << rhs.chm();
  out << " neHadMult " << rhs.neHadMult();
  out << " phoMult " << rhs.phoMult();
  out << " nemf " << rhs.nemf();
  out << " cemf " << rhs.cemf();
;
} // end of detail level Analysis

if(  ((rhs.getLvl() & Ntuple::JetBasic) == Ntuple::JetBasic)  ) {
   out << " csv " << rhs.csv();
  out << " charge " << rhs.charge();
;
} // end of detail level Basic

if(  ((rhs.getLvl() & Ntuple::JetJER) == Ntuple::JetJER)  ) {
   out << " jer_sf " << rhs.jer_sf();
  out << " jer_sf_up " << rhs.jer_sf_up();
  out << " jer_sf_down " << rhs.jer_sf_down();
  out << " jer_sigma_pt " << rhs.jer_sigma_pt();
;
} // end of detail level JER

if(  ((rhs.getLvl() & Ntuple::JetSoftdropSubjets) == Ntuple::JetSoftdropSubjets)  ) {
   out << " subjet_softdrop_N " << rhs.subjet_softdrop_N();
  try{  out << " subjet_softdrop_pt " << rhs.subjet_softdrop_pt().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_eta " << rhs.subjet_softdrop_eta().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_phi " << rhs.subjet_softdrop_phi().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_e " << rhs.subjet_softdrop_e().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_m " << rhs.subjet_softdrop_m().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_csv " << rhs.subjet_softdrop_csv().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_charge " << rhs.subjet_softdrop_charge().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
;
} // end of detail level SoftdropSubjets

if(  ((rhs.getLvl() & Ntuple::JetSoftdropSubjetsTruth) == Ntuple::JetSoftdropSubjetsTruth)  ) {
   try{  out << " subjet_softdrop_partonFlavour " << rhs.subjet_softdrop_partonFlavour().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_hadronFlavour " << rhs.subjet_softdrop_hadronFlavour().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_genParton_pdgID " << rhs.subjet_softdrop_genParton_pdgID().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_nbHadrons " << rhs.subjet_softdrop_nbHadrons().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " subjet_softdrop_ncHadrons " << rhs.subjet_softdrop_ncHadrons().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
;
} // end of detail level SoftdropSubjetsTruth

if(  ((rhs.getLvl() & Ntuple::JetSubstructure) == Ntuple::JetSubstructure)  ) {
   out << " tau1 " << rhs.tau1();
  out << " tau2 " << rhs.tau2();
  out << " tau3 " << rhs.tau3();
  out << " pruned_mass " << rhs.pruned_mass();
  out << " pruned_massCorr " << rhs.pruned_massCorr();
  out << " softdrop_mass " << rhs.softdrop_mass();
  out << " softdrop_massCorr " << rhs.softdrop_massCorr();
  out << " pruned_jec " << rhs.pruned_jec();
  out << " pruned_jecUp " << rhs.pruned_jecUp();
  out << " pruned_jecDown " << rhs.pruned_jecDown();
  out << " softdrop_jec " << rhs.softdrop_jec();
  out << " Hbbtag " << rhs.Hbbtag();
;
} // end of detail level Substructure

if(  ((rhs.getLvl() & Ntuple::JetTruth) == Ntuple::JetTruth)  ) {
   out << " partonFlavour " << rhs.partonFlavour();
  out << " hadronFlavour " << rhs.hadronFlavour();
  out << " genParton_pdgID " << rhs.genParton_pdgID();
  out << " nbHadrons " << rhs.nbHadrons();
  out << " ncHadrons " << rhs.ncHadrons();
;
}


  return out;
}






TLorentzVector* Jet::getTLV() const {

  TLorentzVector* tlv = new TLorentzVector();
  tlv->SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;

}


TLorentzVector Jet::tlv() const {

  TLorentzVector tlv;
  tlv.SetPtEtaPhiE(*(m_pt), *(m_eta), *(m_phi), *(m_e));
  return tlv;

}






void Jet::scaleJES( const floatingnumber ssigma ) {
  m_scalefactor = ssigma;
  if( fabs( ssigma ) < 1e-6 ) return;
 
  *(m_e)  *= ( 1.0 + ssigma );
  *(m_pt) *= ( 1.0 + ssigma );
 
//  if ( m_lvl >= 1 ) {
//    *(m_px) *= ( 1.0 + ssigma );
//    *(m_py) *= ( 1.0 + ssigma );
//    *(m_pz) *= ( 1.0 + ssigma );
//  }
}



