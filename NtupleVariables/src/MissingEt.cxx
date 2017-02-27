
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#include "../include/MissingEt.h"

using namespace std;
using namespace UZH;

MissingEt::MissingEt() {
  
}


MissingEt::MissingEt( const Ntuple::MissingEtNtupleObject* ana, const Int_t idx ) 
: Basic( idx )



{
  m_ana=ana;
  // copy variables defined in Particle.h

  m_lvl    = ana->detailLevel;


  // copy rest of variables
  /*${ {AllNoBools:    printf("acc#name#\n"); if (ana->m_connectsucceeded[#index#]) 
         {printf("?\n"); m_#name# = &((*ana->#name#)[idx]);}
    else {printf("fak\n"); m_#name# = new #type#(); *m_#name# = #default#; } }}
  */
if(  ((ana->detailLevel & Ntuple::MissingEtAnalysis) == Ntuple::MissingEtAnalysis)  ) {
     if (ana->m_connectsucceeded[3]) m_sumEt = &((*ana->sumEt)[idx]); else m_sumEt = 0; 
    if (ana->m_connectsucceeded[4]) m_corrPx = &((*ana->corrPx)[idx]); else m_corrPx = 0; 
    if (ana->m_connectsucceeded[5]) m_corrPy = &((*ana->corrPy)[idx]); else m_corrPy = 0; 
    if (ana->m_connectsucceeded[6]) m_significance = &((*ana->significance)[idx]); else m_significance = 0; 
} // end of detail level Analysis

if(  ((ana->detailLevel & Ntuple::MissingEtBasic) == Ntuple::MissingEtBasic)  ) {
     if (ana->m_connectsucceeded[1]) m_et = &((*ana->et)[idx]); else m_et = 0; 
    if (ana->m_connectsucceeded[2]) m_phi = &((*ana->phi)[idx]); else m_phi = 0; 
} // end of detail level Basic

if(  ((ana->detailLevel & Ntuple::MissingEtCovAnalysis) == Ntuple::MissingEtCovAnalysis)  ) {
     if (ana->m_connectsucceeded[7]) m_cov00 = &((*ana->cov00)[idx]); else m_cov00 = 0; 
    if (ana->m_connectsucceeded[8]) m_cov10 = &((*ana->cov10)[idx]); else m_cov10 = 0; 
    if (ana->m_connectsucceeded[9]) m_cov11 = &((*ana->cov11)[idx]); else m_cov11 = 0; 
} // end of detail level CovAnalysis

if(  ((ana->detailLevel & Ntuple::MissingEtMVAAnalysis) == Ntuple::MissingEtMVAAnalysis)  ) {
     if (ana->m_connectsucceeded[10]) m_recoil_pt = &((*ana->recoil_pt)[idx]); else m_recoil_pt = 0; 
    if (ana->m_connectsucceeded[11]) m_recoil_eta = &((*ana->recoil_eta)[idx]); else m_recoil_eta = 0; 
    if (ana->m_connectsucceeded[12]) m_recoil_phi = &((*ana->recoil_phi)[idx]); else m_recoil_phi = 0; 
    if (ana->m_connectsucceeded[13]) m_recoil_pdgId = &((*ana->recoil_pdgId)[idx]); else m_recoil_pdgId = 0; 
}







}


MissingEt::~MissingEt() {

}

ostream& operator<<( ostream& out,
                     const MissingEt& rhs ) {
  
   out << "MissingEt -" << ( Basic) rhs; 



  ;
if(  ((rhs.getLvl() & Ntuple::MissingEtAnalysis) == Ntuple::MissingEtAnalysis)  ) {
   out << " sumEt " << rhs.sumEt();
  out << " corrPx " << rhs.corrPx();
  out << " corrPy " << rhs.corrPy();
  out << " significance " << rhs.significance();
;
} // end of detail level Analysis

if(  ((rhs.getLvl() & Ntuple::MissingEtBasic) == Ntuple::MissingEtBasic)  ) {
   out << " et " << rhs.et();
  out << " phi " << rhs.phi();
;
} // end of detail level Basic

if(  ((rhs.getLvl() & Ntuple::MissingEtCovAnalysis) == Ntuple::MissingEtCovAnalysis)  ) {
   out << " cov00 " << rhs.cov00();
  out << " cov10 " << rhs.cov10();
  out << " cov11 " << rhs.cov11();
;
} // end of detail level CovAnalysis

if(  ((rhs.getLvl() & Ntuple::MissingEtMVAAnalysis) == Ntuple::MissingEtMVAAnalysis)  ) {
   try{  out << " recoil_pt " << rhs.recoil_pt().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " recoil_eta " << rhs.recoil_eta().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " recoil_phi " << rhs.recoil_phi().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
  try{  out << " recoil_pdgId " << rhs.recoil_pdgId().at(0);} catch(...){std::cout<<"except: no element"<<std::endl;};
;
}


  return out;
}












