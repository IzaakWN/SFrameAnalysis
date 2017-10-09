
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_GenJetak4_H__
#define __UZHTOP_GenJetak4_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "GenJetak4NtupleObject.h"



namespace Ntuple {
  class GenJetak4NtupleObject;
}

namespace UZH {
  
  /**
   *  @short Class that maps GenJetak4NtupleObjects to GenJetak4 Particle class
   *
   *         This class can be used to map the offline GenJetak4 information from
   *         GenJetak4NtupleObjects to UZH::GenJetak4 class. All particles inherit 
   *         from UZH::Particle.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class GenJetak4 : public Basic 
  
  {
  public:
  
    /// default c'tor
    GenJetak4();
    /// default d'tor
    ~GenJetak4();
    
    /// c'tor with index
    GenJetak4( const Ntuple::GenJetak4NtupleObject* ana, const Int_t idx );
    
    
    
    // variable definitions
    
    
        float* m_genJetAK4_pt;
    float* m_genJetAK4_phi;
    float* m_genJetAK4_eta;
    float* m_genJetAK4_e;

    
    

    
    

    // check level given here must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
        float genJetAK4_pt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenJetak4NtupleObject::kgenJetAK4_pt)) std::cout<<"genJetAK4_pt not connected!"<<std::endl;*/ return *(m_genJetAK4_pt); } 
    float genJetAK4_phi() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenJetak4NtupleObject::kgenJetAK4_phi)) std::cout<<"genJetAK4_phi not connected!"<<std::endl;*/ return *(m_genJetAK4_phi); } 
    float genJetAK4_eta() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenJetak4NtupleObject::kgenJetAK4_eta)) std::cout<<"genJetAK4_eta not connected!"<<std::endl;*/ return *(m_genJetAK4_eta); } 
    float genJetAK4_e() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenJetak4NtupleObject::kgenJetAK4_e)) std::cout<<"genJetAK4_e not connected!"<<std::endl;*/ return *(m_genJetAK4_e); } 
    
        void genJetAK4_pt( const float& val){ *(m_genJetAK4_pt)=val; } 
    void genJetAK4_phi( const float& val){ *(m_genJetAK4_phi)=val; } 
    void genJetAK4_eta( const float& val){ *(m_genJetAK4_eta)=val; } 
    void genJetAK4_e( const float& val){ *(m_genJetAK4_e)=val; } 
    
    
  private:
    const Ntuple::GenJetak4NtupleObject* m_ana;
    
  }; // class GenJetak4

  typedef std::vector< GenJetak4 > GenJetak4Vec;
  typedef std::vector< GenJetak4 >::iterator GenJetak4VecIt;
  typedef std::vector< GenJetak4 >::const_iterator GenJetak4VecConstIt;

  

} // end of namespace UZH

/// output stream operator overloaded for GenJetak4 objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::GenJetak4& rhs );


#endif //__UZH_GenJetak4_H__
