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

  /**
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
    JetSubstructure = 2,
    JetSoftdropSubjets = 4,
    JetSoftdropSubjetsTruth = 8,
    JetAnalysis = 16,
    JetTruth = 32,
    JetBasic = 64,
    JetAll = 127,

  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class JetNtupleObject : public SInputVariables< SCycleBaseNTuple > {

    public:
    /// Constructor specifying the parent of the object
    JetNtupleObject( SCycleBaseNTuple* parent );

    /// remember if connect succeeded
    void setConnectSucceeded(const unsigned int index, const bool success);
    bool getConnectSucceeded(const unsigned int index) const {return m_connectsucceeded.at(index);}  

    /// Connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "Jet_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );

    void ConnectVariables( const TString& treeName,
                           const TString& prefix = "Jet_",
                           const TString& ntupleType = "NtupleMakerNtuple" ) throw( SError );

    int getDetailLevel() const {return detailLevel;}   


    // particle vector size
    Int_t                   N;
   
    enum ConnectionIndex { 
     kIDLoose=3, 
     kIDTight=4, 
     kjec=5, 
     kjecUp=6, 
     kjecDown=7, 
     kmuf=8, 
     kphf=9, 
     kemf=10, 
     knhf=11, 
     kchf=12, 
     karea=13, 
     kcm=14, 
     knm=15, 
     kche=16, 
     kne=17, 
     khf_hf=18, 
     khf_emf=19, 
     khof=20, 
     kchm=21, 
     kneHadMult=22, 
     kphoMult=23, 
     knemf=24, 
     kcemf=25, 
     kcsv=1, 
     kcharge=2, 
     kjer_sf=56, 
     kjer_sf_up=57, 
     kjer_sf_down=58, 
     kjer_sigma_pt=59, 
     ksubjet_softdrop_N=43, 
     ksubjet_softdrop_pt=44, 
     ksubjet_softdrop_eta=45, 
     ksubjet_softdrop_phi=46, 
     ksubjet_softdrop_e=47, 
     ksubjet_softdrop_m=48, 
     ksubjet_softdrop_csv=49, 
     ksubjet_softdrop_charge=50, 
     ksubjet_softdrop_partonFlavour=51, 
     ksubjet_softdrop_hadronFlavour=52, 
     ksubjet_softdrop_genParton_pdgID=53, 
     ksubjet_softdrop_nbHadrons=54, 
     ksubjet_softdrop_ncHadrons=55, 
     ktau1=26, 
     ktau2=27, 
     ktau3=28, 
     kpruned_mass=29, 
     kpruned_massCorr=30, 
     ksoftdrop_mass=31, 
     ksoftdrop_massCorr=32, 
     kpruned_jec=33, 
     kpruned_jecUp=34, 
     kpruned_jecDown=35, 
     ksoftdrop_jec=36, 
     kHbbtag=37, 
     kpartonFlavour=38, 
     khadronFlavour=39, 
     kgenParton_pdgID=40, 
     knbHadrons=41, 
     kncHadrons=42, 
 
      kEnd 
    }; 


    // vectors of properties defined in Particle.h
    std::vector< floatingnumber >  *e;
    std::vector< floatingnumber >  *pt;
    std::vector< floatingnumber >  *eta;
    std::vector< floatingnumber >  *phi;
    std::vector< floatingnumber >  *m;
    

    
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
    std::vector< int >  *subjet_softdrop_N;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_pt;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_eta;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_phi;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_e;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_m;
    std::vector< std::vector<floatingnumber> >  *subjet_softdrop_csv;
    std::vector< std::vector<int> >  *subjet_softdrop_charge;
    std::vector< std::vector<int> >  *subjet_softdrop_partonFlavour;
    std::vector< std::vector<int> >  *subjet_softdrop_hadronFlavour;
    std::vector< std::vector<int> >  *subjet_softdrop_genParton_pdgID;
    std::vector< std::vector<int> >  *subjet_softdrop_nbHadrons;
    std::vector< std::vector<int> >  *subjet_softdrop_ncHadrons;
    std::vector< floatingnumber >  *tau1;
    std::vector< floatingnumber >  *tau2;
    std::vector< floatingnumber >  *tau3;
    std::vector< floatingnumber >  *pruned_mass;
    std::vector< floatingnumber >  *pruned_massCorr;
    std::vector< floatingnumber >  *softdrop_mass;
    std::vector< floatingnumber >  *softdrop_massCorr;
    std::vector< floatingnumber >  *pruned_jec;
    std::vector< floatingnumber >  *pruned_jecUp;
    std::vector< floatingnumber >  *pruned_jecDown;
    std::vector< floatingnumber >  *softdrop_jec;
    std::vector< floatingnumber >  *Hbbtag;
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
