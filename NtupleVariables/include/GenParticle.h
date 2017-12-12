
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_GenParticle_H__
#define __UZHTOP_GenParticle_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "GenParticleNtupleObject.h"


namespace Ntuple {
  class GenParticleNtupleObject;
}

namespace UZH {
  
  /**
   *  @short Class that maps GenParticleNtupleObjects to GenParticle Particle class
   *
   *        This class can be used to map the offline GenParticle information from
   *        GenParticleNtupleObjects to UZH::GenParticle class. All particles inherit 
   *        from UZH::Particle.
   *
   *  @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class GenParticle : public Basic , public Particle  {
    
    public:
    
    // default constructor
    GenParticle();
    
    // default destructor
    ~GenParticle();
    
    // constructor with index
    GenParticle( const Ntuple::GenParticleNtupleObject* ana, const Int_t idx );
    
    TLorentzVector* getTLV() const;
    TLorentzVector tlv() const;
    
    floatingnumber DeltaR(const GenParticle& p) const;
    
    // variable definitions
    int* m_pdgId;
    int* m_status;
    std::vector<int>* m_mother;
    int* m_nMoth;
    int* m_nDau;
    std::vector<int>* m_dau;
    int* m_isPrompt;
    int* m_isDirectPromptTauDecayProduct;
    int* m_fromHardProcessFinalState;
    int* m_isDirectHardProcessTauDecayProductFinalState;
    floatingnumber* m_tauvispt;
    floatingnumber* m_tauviseta;
    floatingnumber* m_tauvisphi;
    floatingnumber* m_tauvismass;
    int* m_taudecay;
    
    
    floatingnumber m_e_; // reference value for m_e pointer
    
    // there must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
    int pdgId() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kpdgId)) std::cout<<"pdgId not connected!"<<std::endl;*/ return *(m_pdgId); } 
    int status() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kstatus)) std::cout<<"status not connected!"<<std::endl;*/ return *(m_status); } 
    std::vector<int> mother() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kmother)) std::cout<<"mother not connected!"<<std::endl;*/ return *(m_mother); } 
    int nMoth() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::knMoth)) std::cout<<"nMoth not connected!"<<std::endl;*/ return *(m_nMoth); } 
    int nDau() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::knDau)) std::cout<<"nDau not connected!"<<std::endl;*/ return *(m_nDau); } 
    std::vector<int> dau() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kdau)) std::cout<<"dau not connected!"<<std::endl;*/ return *(m_dau); } 
    int isPrompt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kisPrompt)) std::cout<<"isPrompt not connected!"<<std::endl;*/ return *(m_isPrompt); } 
    int isDirectPromptTauDecayProduct() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kisDirectPromptTauDecayProduct)) std::cout<<"isDirectPromptTauDecayProduct not connected!"<<std::endl;*/ return *(m_isDirectPromptTauDecayProduct); } 
    int fromHardProcessFinalState() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kfromHardProcessFinalState)) std::cout<<"fromHardProcessFinalState not connected!"<<std::endl;*/ return *(m_fromHardProcessFinalState); } 
    int isDirectHardProcessTauDecayProductFinalState() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::kisDirectHardProcessTauDecayProductFinalState)) std::cout<<"isDirectHardProcessTauDecayProductFinalState not connected!"<<std::endl;*/ return *(m_isDirectHardProcessTauDecayProductFinalState); } 
    floatingnumber tauvispt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::ktauvispt)) std::cout<<"tauvispt not connected!"<<std::endl;*/ return *(m_tauvispt); } 
    floatingnumber tauviseta() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::ktauviseta)) std::cout<<"tauviseta not connected!"<<std::endl;*/ return *(m_tauviseta); } 
    floatingnumber tauvisphi() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::ktauvisphi)) std::cout<<"tauvisphi not connected!"<<std::endl;*/ return *(m_tauvisphi); } 
    floatingnumber tauvismass() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::ktauvismass)) std::cout<<"tauvismass not connected!"<<std::endl;*/ return *(m_tauvismass); } 
    int taudecay() const { /*if(!m_ana->getConnectSucceeded(Ntuple::GenParticleNtupleObject::ktaudecay)) std::cout<<"taudecay not connected!"<<std::endl;*/ return *(m_taudecay); } 
        
    void pdgId( const int& val){ *(m_pdgId)=val; } 
    void status( const int& val){ *(m_status)=val; } 
    void mother( const std::vector<int>& val){ *(m_mother)=val; } 
    void nMoth( const int& val){ *(m_nMoth)=val; } 
    void nDau( const int& val){ *(m_nDau)=val; } 
    void dau( const std::vector<int>& val){ *(m_dau)=val; } 
    void isPrompt( const int& val){ *(m_isPrompt)=val; } 
    void isDirectPromptTauDecayProduct( const int& val){ *(m_isDirectPromptTauDecayProduct)=val; } 
    void fromHardProcessFinalState( const int& val){ *(m_fromHardProcessFinalState)=val; } 
    void isDirectHardProcessTauDecayProductFinalState( const int& val){ *(m_isDirectHardProcessTauDecayProductFinalState)=val; } 
    void tauvispt( const floatingnumber& val){ *(m_tauvispt)=val; } 
    void tauviseta( const floatingnumber& val){ *(m_tauviseta)=val; } 
    void tauvisphi( const floatingnumber& val){ *(m_tauvisphi)=val; } 
    void tauvismass( const floatingnumber& val){ *(m_tauvismass)=val; } 
    void taudecay( const int& val){ *(m_taudecay)=val; } 
    
    
    private:
    
    const Ntuple::GenParticleNtupleObject* m_ana;
    
  }; // class GenParticle
  
  typedef std::vector< GenParticle > GenParticleVec;
  typedef std::vector< GenParticle >::iterator GenParticleVecIt;
  typedef std::vector< GenParticle >::const_iterator GenParticleVecConstIt;
  
} // end of namespace UZH

// output stream operator overloaded for GenParticle objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::GenParticle& rhs );

#endif //__UZH_GenParticle_H__
