
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#include "../include/GenJetak4.h"

using namespace std;
using namespace UZH;

GenJetak4::GenJetak4() { }
GenJetak4::~GenJetak4() { }

GenJetak4::GenJetak4( const Ntuple::GenJetak4NtupleObject* ana, const Int_t idx ) : Basic( idx ) {
  
  m_ana = ana;
  
  // copy variables defined in Particle.h
  m_lvl = ana->detailLevel;
  
  // copy rest of variables
  /*${ {AllNoBools:
  printf("acc#name#\n");if (ana->m_connectsucceeded[#index#]) {printf("?\n"); m_#name# = &((*ana->#name#)[idx]);}
  else {printf("fak\n"); m_#name# = new #type#(); *m_#name# = #default#; } }}
  */
  
  if(  ((ana->detailLevel & Ntuple::GenJetak4Truth) == Ntuple::GenJetak4Truth)  ) {
    if (ana->m_connectsucceeded[1]) m_genJetAK4_pt = &((*ana->genJetAK4_pt)[idx]); else m_genJetAK4_pt = 0; 
    if (ana->m_connectsucceeded[2]) m_genJetAK4_phi = &((*ana->genJetAK4_phi)[idx]); else m_genJetAK4_phi = 0; 
    if (ana->m_connectsucceeded[3]) m_genJetAK4_eta = &((*ana->genJetAK4_eta)[idx]); else m_genJetAK4_eta = 0; 
    if (ana->m_connectsucceeded[4]) m_genJetAK4_e = &((*ana->genJetAK4_e)[idx]); else m_genJetAK4_e = 0; 
  } // end of detail level Truth
  
}


ostream& operator<<( ostream& out, const GenJetak4& rhs ) {

  out << "GenJetak4 -" << ( Basic) rhs; 
  
  if( ((rhs.getLvl() & Ntuple::GenJetak4Truth) == Ntuple::GenJetak4Truth) ) {
    out << " genJetAK4_pt " << rhs.genJetAK4_pt(); 
    out << " genJetAK4_phi " << rhs.genJetAK4_phi(); 
    out << " genJetAK4_eta " << rhs.genJetAK4_eta(); 
    out << " genJetAK4_e " << rhs.genJetAK4_e(); 
  } // end of detail level Truth
  
  return out;
}

