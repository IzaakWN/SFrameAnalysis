
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_Jet_H__
#define __UZHTOP_Jet_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "JetNtupleObject.h"



namespace Ntuple {
  class JetNtupleObject;
}

namespace UZH {
  
  /**
   *  @short Class that maps JetNtupleObjects to Jet Particle class
   *
   *         This class can be used to map the offline Jet information from
   *         JetNtupleObjects to UZH::Jet class. All particles inherit 
   *         from UZH::Particle.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class Jet : public Basic 
 , public Particle 
  {
  public:

    /// default c'tor
    Jet();
    /// default d'tor
    ~Jet();
    
    /// c'tor with index
    Jet( const Ntuple::JetNtupleObject* ana, const Int_t idx );

    TLorentzVector* getTLV() const;
    TLorentzVector tlv() const;


    
    // variable definitions


    bool            m_isTagged; ///< user-level flag to indicate b-tag


    floatingnumber  m_scalefactor; ///< scale factor for JES shifts (0 for nominal JES)

    bool m_IDLoose;
    bool m_IDTight;
    floatingnumber* m_jec;
    floatingnumber* m_jecUp;
    floatingnumber* m_jecDown;
    floatingnumber* m_muf;
    floatingnumber* m_phf;
    floatingnumber* m_emf;
    floatingnumber* m_nhf;
    floatingnumber* m_chf;
    floatingnumber* m_area;
    int* m_cm;
    int* m_nm;
    floatingnumber* m_che;
    floatingnumber* m_ne;
    floatingnumber* m_hf_hf;
    floatingnumber* m_hf_emf;
    floatingnumber* m_hof;
    int* m_chm;
    int* m_neHadMult;
    int* m_phoMult;
    floatingnumber* m_nemf;
    floatingnumber* m_cemf;
    floatingnumber* m_csv;
    int* m_charge;
    floatingnumber* m_jer_sf;
    floatingnumber* m_jer_sf_up;
    floatingnumber* m_jer_sf_down;
    floatingnumber* m_jer_sigma_pt;
    int* m_partonFlavour;
    int* m_hadronFlavour;
    int* m_genParton_pdgID;
    int* m_nbHadrons;
    int* m_ncHadrons;





    void           setTagged( const bool isTagged = true ) { m_isTagged = isTagged; }
    bool           isTagged() const { return m_isTagged; }


    floatingnumber getJetSF() const { return m_scalefactor; }
    void           scaleJES( const floatingnumber scale);


    // check level given here must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
    bool IDLoose() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kIDLoose)) std::cout<<"IDLoose not connected!"<<std::endl;*/ return (m_IDLoose); } 
    bool IDTight() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kIDTight)) std::cout<<"IDTight not connected!"<<std::endl;*/ return (m_IDTight); } 
    floatingnumber jec() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjec)) std::cout<<"jec not connected!"<<std::endl;*/ return *(m_jec); } 
    floatingnumber jecUp() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjecUp)) std::cout<<"jecUp not connected!"<<std::endl;*/ return *(m_jecUp); } 
    floatingnumber jecDown() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjecDown)) std::cout<<"jecDown not connected!"<<std::endl;*/ return *(m_jecDown); } 
    floatingnumber muf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kmuf)) std::cout<<"muf not connected!"<<std::endl;*/ return *(m_muf); } 
    floatingnumber phf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kphf)) std::cout<<"phf not connected!"<<std::endl;*/ return *(m_phf); } 
    floatingnumber emf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kemf)) std::cout<<"emf not connected!"<<std::endl;*/ return *(m_emf); } 
    floatingnumber nhf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::knhf)) std::cout<<"nhf not connected!"<<std::endl;*/ return *(m_nhf); } 
    floatingnumber chf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kchf)) std::cout<<"chf not connected!"<<std::endl;*/ return *(m_chf); } 
    floatingnumber area() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::karea)) std::cout<<"area not connected!"<<std::endl;*/ return *(m_area); } 
    int cm() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kcm)) std::cout<<"cm not connected!"<<std::endl;*/ return *(m_cm); } 
    int nm() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::knm)) std::cout<<"nm not connected!"<<std::endl;*/ return *(m_nm); } 
    floatingnumber che() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kche)) std::cout<<"che not connected!"<<std::endl;*/ return *(m_che); } 
    floatingnumber ne() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kne)) std::cout<<"ne not connected!"<<std::endl;*/ return *(m_ne); } 
    floatingnumber hf_hf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::khf_hf)) std::cout<<"hf_hf not connected!"<<std::endl;*/ return *(m_hf_hf); } 
    floatingnumber hf_emf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::khf_emf)) std::cout<<"hf_emf not connected!"<<std::endl;*/ return *(m_hf_emf); } 
    floatingnumber hof() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::khof)) std::cout<<"hof not connected!"<<std::endl;*/ return *(m_hof); } 
    int chm() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kchm)) std::cout<<"chm not connected!"<<std::endl;*/ return *(m_chm); } 
    int neHadMult() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kneHadMult)) std::cout<<"neHadMult not connected!"<<std::endl;*/ return *(m_neHadMult); } 
    int phoMult() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kphoMult)) std::cout<<"phoMult not connected!"<<std::endl;*/ return *(m_phoMult); } 
    floatingnumber nemf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::knemf)) std::cout<<"nemf not connected!"<<std::endl;*/ return *(m_nemf); } 
    floatingnumber cemf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kcemf)) std::cout<<"cemf not connected!"<<std::endl;*/ return *(m_cemf); } 
    floatingnumber csv() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kcsv)) std::cout<<"csv not connected!"<<std::endl;*/ return *(m_csv); } 
    int charge() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kcharge)) std::cout<<"charge not connected!"<<std::endl;*/ return *(m_charge); } 
    floatingnumber jer_sf() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjer_sf)) std::cout<<"jer_sf not connected!"<<std::endl;*/ return *(m_jer_sf); } 
    floatingnumber jer_sf_up() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjer_sf_up)) std::cout<<"jer_sf_up not connected!"<<std::endl;*/ return *(m_jer_sf_up); } 
    floatingnumber jer_sf_down() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjer_sf_down)) std::cout<<"jer_sf_down not connected!"<<std::endl;*/ return *(m_jer_sf_down); } 
    floatingnumber jer_sigma_pt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kjer_sigma_pt)) std::cout<<"jer_sigma_pt not connected!"<<std::endl;*/ return *(m_jer_sigma_pt); } 
    int partonFlavour() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kpartonFlavour)) std::cout<<"partonFlavour not connected!"<<std::endl;*/ return *(m_partonFlavour); } 
    int hadronFlavour() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::khadronFlavour)) std::cout<<"hadronFlavour not connected!"<<std::endl;*/ return *(m_hadronFlavour); } 
    int genParton_pdgID() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kgenParton_pdgID)) std::cout<<"genParton_pdgID not connected!"<<std::endl;*/ return *(m_genParton_pdgID); } 
    int nbHadrons() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::knbHadrons)) std::cout<<"nbHadrons not connected!"<<std::endl;*/ return *(m_nbHadrons); } 
    int ncHadrons() const { /*if(!m_ana->getConnectSucceeded(Ntuple::JetNtupleObject::kncHadrons)) std::cout<<"ncHadrons not connected!"<<std::endl;*/ return *(m_ncHadrons); } 
    
    void IDLoose( const bool& val){ (m_IDLoose)=val; } 
    void IDTight( const bool& val){ (m_IDTight)=val; } 
    void jec( const floatingnumber& val){ *(m_jec)=val; } 
    void jecUp( const floatingnumber& val){ *(m_jecUp)=val; } 
    void jecDown( const floatingnumber& val){ *(m_jecDown)=val; } 
    void muf( const floatingnumber& val){ *(m_muf)=val; } 
    void phf( const floatingnumber& val){ *(m_phf)=val; } 
    void emf( const floatingnumber& val){ *(m_emf)=val; } 
    void nhf( const floatingnumber& val){ *(m_nhf)=val; } 
    void chf( const floatingnumber& val){ *(m_chf)=val; } 
    void area( const floatingnumber& val){ *(m_area)=val; } 
    void cm( const int& val){ *(m_cm)=val; } 
    void nm( const int& val){ *(m_nm)=val; } 
    void che( const floatingnumber& val){ *(m_che)=val; } 
    void ne( const floatingnumber& val){ *(m_ne)=val; } 
    void hf_hf( const floatingnumber& val){ *(m_hf_hf)=val; } 
    void hf_emf( const floatingnumber& val){ *(m_hf_emf)=val; } 
    void hof( const floatingnumber& val){ *(m_hof)=val; } 
    void chm( const int& val){ *(m_chm)=val; } 
    void neHadMult( const int& val){ *(m_neHadMult)=val; } 
    void phoMult( const int& val){ *(m_phoMult)=val; } 
    void nemf( const floatingnumber& val){ *(m_nemf)=val; } 
    void cemf( const floatingnumber& val){ *(m_cemf)=val; } 
    void csv( const floatingnumber& val){ *(m_csv)=val; } 
    void charge( const int& val){ *(m_charge)=val; } 
    void jer_sf( const floatingnumber& val){ *(m_jer_sf)=val; } 
    void jer_sf_up( const floatingnumber& val){ *(m_jer_sf_up)=val; } 
    void jer_sf_down( const floatingnumber& val){ *(m_jer_sf_down)=val; } 
    void jer_sigma_pt( const floatingnumber& val){ *(m_jer_sigma_pt)=val; } 
    void partonFlavour( const int& val){ *(m_partonFlavour)=val; } 
    void hadronFlavour( const int& val){ *(m_hadronFlavour)=val; } 
    void genParton_pdgID( const int& val){ *(m_genParton_pdgID)=val; } 
    void nbHadrons( const int& val){ *(m_nbHadrons)=val; } 
    void ncHadrons( const int& val){ *(m_ncHadrons)=val; } 
    

  private:
    const Ntuple::JetNtupleObject* m_ana;
  }; // class Jet

  typedef std::vector< Jet > JetVec;
  typedef std::vector< Jet >::iterator JetVecIt;
  typedef std::vector< Jet >::const_iterator JetVecConstIt;





} // end of namespace UZH

/// output stream operator overloaded for Jet objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::Jet& rhs );


#endif //__UZH_Jet_H__
