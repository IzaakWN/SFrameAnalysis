// Dear emacs, this is -*- c++ -*-
// $Id: JetNtupleObject.h 37457 2010-07-05 12:04:33Z mann $

// THIS FILE HAS BEEN GENERATED AUTOMATICALLY. DO NOT EDIT DIRECTLY, CHANGES WILL BE LOST UPON NEXT CODE GENERATION.
// Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn 


#ifndef SFRAME_NtupleVARIABLES_JetNtupleObject_H
#define SFRAME_NtupleVARIABLES_JetNtupleObject_H

// Local include(s):
#include "NtupleObjectNames.h"

// STL include(s):
#include <vector>
#include <string>

// ROOT include(s):
#include <TString.h>

// SFrame include(s):
#include "core/include/SError.h"
#include "core/include/SCycleBaseNTuple.h"
#include "plug-ins/include/SInputVariables.h"

namespace Ntuple {
  
  /*
   *  @short Class that can read the variables produced by JetNtupleObject
   *
   *         This class can be used to read the offline muon information from
   *         an ntuple produced by the SingleTopDPDMaker code.
   *
   * @author Code produced by Id: CodeIt.py 494 2010-07-30 13:41:32Z svn   
   *
   */
  
  enum JetDetails {
    JetJER = 1,
    JetTruth = 2,
    JetAnalysis = 4,
    JetBasic = 8,
    JetAll = 15,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class JetNtupleObject : public SInputVariables< SCycleBaseNTuple > {
    
    public:
    
    // constructor specifying the parent of the object
    JetNtupleObject( SCycleBaseNTuple* parent );
    
    // remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  
    
    // connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "Jet_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "Jet_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );
    
    int getDetailLevel() const { return detailLevel; }
    
    // particle vector size
    Int_t N;
    
    enum ConnectionIndex { 
      kIDLoose = 3,
      kIDTight = 4,
      kjec = 5,
      kjecUp = 6,
      kjecDown = 7,
      kmuf = 8,
      kphf = 9,
      kemf = 10,
      knhf = 11,
      kchf = 12,
      karea = 13,
      kcm = 14,
      knm = 15,
      kche = 16,
      kne = 17,
      khf_hf = 18,
      khf_emf = 19,
      khof = 20,
      kchm = 21,
      kneHadMult = 22,
      kphoMult = 23,
      knemf = 24,
      kcemf = 25,
      kcsv = 1,
      kcharge = 2,
      kjer_sf = 31,
      kjer_sf_up = 32,
      kjer_sf_down = 33,
      kjer_sigma_pt = 34,
      kpartonFlavour = 26,
      khadronFlavour = 27,
      kgenParton_pdgID = 28,
      knbHadrons = 29,
      kncHadrons = 30,
      kEnd
    }; 
    
    
    // vectors of properties defined in Particle.h
    std::vector< floatingnumber >  *pt;
    std::vector< floatingnumber >  *eta;
    std::vector< floatingnumber >  *phi;
    std::vector< floatingnumber >  *m;
    std::vector< floatingnumber >  *e;
     
    // vectors of object specific variables
    std::vector< bool >  *IDLoose;
    std::vector< bool >  *IDTight;
    std::vector< floatingnumber >  *jec;
    std::vector< floatingnumber >  *jecUp;
    std::vector< floatingnumber >  *jecDown;
    std::vector< floatingnumber >  *muf;
    std::vector< floatingnumber >  *phf;
    std::vector< floatingnumber >  *emf;
    std::vector< floatingnumber >  *nhf;
    std::vector< floatingnumber >  *chf;
    std::vector< floatingnumber >  *area;
    std::vector< int >  *cm;
    std::vector< int >  *nm;
    std::vector< floatingnumber >  *che;
    std::vector< floatingnumber >  *ne;
    std::vector< floatingnumber >  *hf_hf;
    std::vector< floatingnumber >  *hf_emf;
    std::vector< floatingnumber >  *hof;
    std::vector< int >  *chm;
    std::vector< int >  *neHadMult;
    std::vector< int >  *phoMult;
    std::vector< floatingnumber >  *nemf;
    std::vector< floatingnumber >  *cemf;
    std::vector< floatingnumber >  *csv;
    std::vector< int >  *charge;
    std::vector< floatingnumber >  *jer_sf;
    std::vector< floatingnumber >  *jer_sf_up;
    std::vector< floatingnumber >  *jer_sf_down;
    std::vector< floatingnumber >  *jer_sigma_pt;
    std::vector< int >  *partonFlavour;
    std::vector< int >  *hadronFlavour;
    std::vector< int >  *genParton_pdgID;
    std::vector< int >  *nbHadrons;
    std::vector< int >  *ncHadrons;
    
    std::vector<int> m_connectsucceeded;
    
    // save actual detail level and group
    Int_t detailLevel;
    std::string detailGroup;
    
  }; // class JetNtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_JetNtupleObject_H
