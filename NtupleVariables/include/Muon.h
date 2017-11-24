
// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 

#ifndef __UZHTOP_Muon_H__
#define __UZHTOP_Muon_H__

#include <cmath>
#include "Particle.h"
#include <vector>
#include "MuonNtupleObject.h"


class TRandom;


namespace Ntuple {
  class MuonNtupleObject;
}

namespace UZH {
  
  /*
   *  @short Class that maps MuonNtupleObjects to Muon Particle class
   *
   *         This class can be used to map the offline Muon information from
   *         MuonNtupleObjects to UZH::Muon class. All particles inherit 
   *         from UZH::Particle.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 
   *
   */
  
  class Muon : public Basic , public Particle  {
    
    public:
    
    // default constructor
    Muon();
    
    // default destructor
    ~Muon();
    
    // constructor with index
    Muon( const Ntuple::MuonNtupleObject* ana, const Int_t idx );
    
    TLorentzVector* getTLV() const;
    TLorentzVector tlv() const;
    
    // variable definitions
    floatingnumber* m_charge;
    int* m_pdgId;
    floatingnumber* m_SemileptonicPFIso;
    floatingnumber* m_SemileptonicCorrPFIso;
    int* m_isHighPtMuon;
    int* m_isLooseMuon;
    int* m_isTightMuon;
    int* m_isMediumMuon;
    int* m_isMediumMuonGH;
    int* m_isPFMuon;
    int* m_isGlobalMuon;
    int* m_isTrackerMuon;
    int* m_isSoftMuon;
    floatingnumber* m_pfDeltaCorrRelIso;
    floatingnumber* m_photonIso;
    floatingnumber* m_neutralHadIso;
    floatingnumber* m_chargedHadIso;
    floatingnumber* m_trackIso;
    floatingnumber* m_d0;
    floatingnumber* m_dz;
    floatingnumber* m_d0_allvertices;
    floatingnumber* m_dz_allvertices;
    floatingnumber* m_bestTrack_pt;
    floatingnumber* m_bestTrack_ptErr;
    int* m_trackerHits;
    int* m_matchedStations;
    int* m_pixelHits;
    int* m_globalHits;
    floatingnumber* m_normChi2;
    
    // there must be consistent with ...NtupleObject.cxx, otherwise you'll get a segfault
    floatingnumber charge() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kcharge)) std::cout<<"charge not connected!"<<std::endl;*/ return *(m_charge); } 
    int pdgId() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kpdgId)) std::cout<<"pdgId not connected!"<<std::endl;*/ return *(m_pdgId); } 
    floatingnumber SemileptonicPFIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kSemileptonicPFIso)) std::cout<<"SemileptonicPFIso not connected!"<<std::endl;*/ return *(m_SemileptonicPFIso); } 
    floatingnumber SemileptonicCorrPFIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kSemileptonicCorrPFIso)) std::cout<<"SemileptonicCorrPFIso not connected!"<<std::endl;*/ return *(m_SemileptonicCorrPFIso); } 
    int isHighPtMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisHighPtMuon)) std::cout<<"isHighPtMuon not connected!"<<std::endl;*/ return *(m_isHighPtMuon); } 
    int isLooseMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisLooseMuon)) std::cout<<"isLooseMuon not connected!"<<std::endl;*/ return *(m_isLooseMuon); } 
    int isTightMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisTightMuon)) std::cout<<"isTightMuon not connected!"<<std::endl;*/ return *(m_isTightMuon); } 
    int isMediumMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisMediumMuon)) std::cout<<"isMediumMuon not connected!"<<std::endl;*/ return *(m_isMediumMuon); } 
    int isMediumMuonGH() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisMediumMuonGH)) std::cout<<"isMediumMuonGH not connected!"<<std::endl;*/ return *(m_isMediumMuonGH); } 
    int isPFMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisPFMuon)) std::cout<<"isPFMuon not connected!"<<std::endl;*/ return *(m_isPFMuon); } 
    int isGlobalMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisGlobalMuon)) std::cout<<"isGlobalMuon not connected!"<<std::endl;*/ return *(m_isGlobalMuon); } 
    int isTrackerMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisTrackerMuon)) std::cout<<"isTrackerMuon not connected!"<<std::endl;*/ return *(m_isTrackerMuon); } 
    int isSoftMuon() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kisSoftMuon)) std::cout<<"isSoftMuon not connected!"<<std::endl;*/ return *(m_isSoftMuon); } 
    floatingnumber pfDeltaCorrRelIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kpfDeltaCorrRelIso)) std::cout<<"pfDeltaCorrRelIso not connected!"<<std::endl;*/ return *(m_pfDeltaCorrRelIso); } 
    floatingnumber photonIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kphotonIso)) std::cout<<"photonIso not connected!"<<std::endl;*/ return *(m_photonIso); } 
    floatingnumber neutralHadIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kneutralHadIso)) std::cout<<"neutralHadIso not connected!"<<std::endl;*/ return *(m_neutralHadIso); } 
    floatingnumber chargedHadIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kchargedHadIso)) std::cout<<"chargedHadIso not connected!"<<std::endl;*/ return *(m_chargedHadIso); } 
    floatingnumber trackIso() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::ktrackIso)) std::cout<<"trackIso not connected!"<<std::endl;*/ return *(m_trackIso); } 
    floatingnumber d0() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kd0)) std::cout<<"d0 not connected!"<<std::endl;*/ return *(m_d0); } 
    floatingnumber dz() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kdz)) std::cout<<"dz not connected!"<<std::endl;*/ return *(m_dz); } 
    floatingnumber d0_allvertices() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kd0_allvertices)) std::cout<<"d0_allvertices not connected!"<<std::endl;*/ return *(m_d0_allvertices); } 
    floatingnumber dz_allvertices() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kdz_allvertices)) std::cout<<"dz_allvertices not connected!"<<std::endl;*/ return *(m_dz_allvertices); } 
    floatingnumber bestTrack_pt() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kbestTrack_pt)) std::cout<<"bestTrack_pt not connected!"<<std::endl;*/ return *(m_bestTrack_pt); } 
    floatingnumber bestTrack_ptErr() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kbestTrack_ptErr)) std::cout<<"bestTrack_ptErr not connected!"<<std::endl;*/ return *(m_bestTrack_ptErr); } 
    int trackerHits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::ktrackerHits)) std::cout<<"trackerHits not connected!"<<std::endl;*/ return *(m_trackerHits); } 
    int matchedStations() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kmatchedStations)) std::cout<<"matchedStations not connected!"<<std::endl;*/ return *(m_matchedStations); } 
    int pixelHits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kpixelHits)) std::cout<<"pixelHits not connected!"<<std::endl;*/ return *(m_pixelHits); } 
    int globalHits() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::kglobalHits)) std::cout<<"globalHits not connected!"<<std::endl;*/ return *(m_globalHits); } 
    floatingnumber normChi2() const { /*if(!m_ana->getConnectSucceeded(Ntuple::MuonNtupleObject::knormChi2)) std::cout<<"normChi2 not connected!"<<std::endl;*/ return *(m_normChi2); } 
        
    void charge( const floatingnumber& val){ *(m_charge)=val; } 
    void pdgId( const int& val){ *(m_pdgId)=val; } 
    void SemileptonicPFIso( const floatingnumber& val){ *(m_SemileptonicPFIso)=val; } 
    void SemileptonicCorrPFIso( const floatingnumber& val){ *(m_SemileptonicCorrPFIso)=val; } 
    void isHighPtMuon( const int& val){ *(m_isHighPtMuon)=val; } 
    void isLooseMuon( const int& val){ *(m_isLooseMuon)=val; } 
    void isTightMuon( const int& val){ *(m_isTightMuon)=val; } 
    void isMediumMuon( const int& val){ *(m_isMediumMuon)=val; } 
    void isMediumMuonGH( const int& val){ *(m_isMediumMuonGH)=val; } 
    void isPFMuon( const int& val){ *(m_isPFMuon)=val; } 
    void isGlobalMuon( const int& val){ *(m_isGlobalMuon)=val; } 
    void isTrackerMuon( const int& val){ *(m_isTrackerMuon)=val; } 
    void isSoftMuon( const int& val){ *(m_isSoftMuon)=val; } 
    void pfDeltaCorrRelIso( const floatingnumber& val){ *(m_pfDeltaCorrRelIso)=val; } 
    void photonIso( const floatingnumber& val){ *(m_photonIso)=val; } 
    void neutralHadIso( const floatingnumber& val){ *(m_neutralHadIso)=val; } 
    void chargedHadIso( const floatingnumber& val){ *(m_chargedHadIso)=val; } 
    void trackIso( const floatingnumber& val){ *(m_trackIso)=val; } 
    void d0( const floatingnumber& val){ *(m_d0)=val; } 
    void dz( const floatingnumber& val){ *(m_dz)=val; } 
    void d0_allvertices( const floatingnumber& val){ *(m_d0_allvertices)=val; } 
    void dz_allvertices( const floatingnumber& val){ *(m_dz_allvertices)=val; } 
    void bestTrack_pt( const floatingnumber& val){ *(m_bestTrack_pt)=val; } 
    void bestTrack_ptErr( const floatingnumber& val){ *(m_bestTrack_ptErr)=val; } 
    void trackerHits( const int& val){ *(m_trackerHits)=val; } 
    void matchedStations( const int& val){ *(m_matchedStations)=val; } 
    void pixelHits( const int& val){ *(m_pixelHits)=val; } 
    void globalHits( const int& val){ *(m_globalHits)=val; } 
    void normChi2( const floatingnumber& val){ *(m_normChi2)=val; } 
        
    
    private:
    
    const Ntuple::MuonNtupleObject* m_ana;
    
  }; // class Muon
  
  typedef std::vector< Muon > MuonVec;
  typedef std::vector< Muon >::iterator MuonVecIt;
  typedef std::vector< Muon >::const_iterator MuonVecConstIt;
  
  // sort Muons by pT
  bool operator<( const Muon& e1, const Muon& e2 );
  
  // function class to sort Muon vector contents by pT
  class sortMuonPt {
    public:
      bool operator()( const Muon& e1, const Muon& e2 );
  };
  
} // end of namespace UZH

// output stream operator overloaded for Muon objects
std::ostream& operator<<( std::ostream& out,
                          const UZH::Muon& rhs );

#endif //__UZH_Muon_H__
