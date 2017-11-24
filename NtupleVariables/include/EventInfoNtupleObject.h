// Dear emacs, this is -*- c++ -*-
// $Id: EventInfoNtupleObject.h 43055 2015-01-29 16:26:25Z clange $
#ifndef SFRAME_NtupleVARIABLES_EventInfoNtupleObject_H
#define SFRAME_NtupleVARIABLES_EventInfoNtupleObject_H

// Local include(s):
#include "NtupleObjectNames.h"

// STL include(s):
#include <vector>

// ROOT include(s):
#include <TString.h>

// SFrame include(s):
#include "core/include/SError.h"
#include "core/include/SCycleBaseNTuple.h"
#include "plug-ins/include/SInputVariables.h"

namespace Ntuple {

  /**
  *  @short Class that can read the variables produced by EventInfoNtupleObject
  *
  *         This class can be used to read the offline muon information from
  *         an ntuple produced by the SingleTopDPDMaker code.
  *
  * @author Clemens Lange <Clemens.Lange@desy.de>
  *
  * $Revision: 43055 $
  * $Date: 2015-01-29 16:26:25 +0000 (Thu, 29 Jan 2015) $
  */
  
  enum EventInfoDetails {
    EventInfoBasic = 1,
    EventInfoTrigger = 2,
    EventInfoTruth = 4,
    EventInfoPDF = 8,
    EventInfoMETFilters = 16,
  };
  
  // forward declaration of NtupleObjectNames
  class NtupleObjectNames;
  class EventInfoNtupleObject : public SInputVariables< SCycleBaseNTuple > {

    public:
    /// Constructor specifying the parent of the object
    EventInfoNtupleObject( SCycleBaseNTuple* parent );

    /// Connect the variables to the input branches
    void ConnectVariables( const TString& treeName,
                           UInt_t detail_level = 0,
                           const TString& prefix = "",
                           const TString& ntupleType = "UZHCMSNtuple" ) throw( SError );

    enum ConnectionIndex { 
      kmcVx_z,
      kEnd
    };

    //
    // all variables 
    //
    Int_t eventNumber;
    Int_t runNumber;
    Int_t lumiBlock;

    // EventInfoBasic
    std::vector< int >* averageIntPerXing;
    std::vector< int >* actualIntPerXing;
    std::vector< int >* bunchCrossing;
    floatingnumber rho;

    // EventInfoTrigger
    std::map<std::string,bool>* trigDecision;
    //std::vector< floatingnumber >* trigObject_pt;
    //std::vector< floatingnumber >* trigObject_eta;
    //std::vector< floatingnumber >* trigObject_phi;
    //std::vector< std::string >* trigObject_lastname;
    //std::map< std::string, std::vector<std::string> >* trigObject_filterLabels;


    // EventInfoTruth
    Float_t genEventWeight;
    
    // EventInfoPDF
    std::vector< int >* pdf_id;
    std::vector< floatingnumber >* pdf_x;
    std::vector<floatingnumber>* pdf_xPDF;
    std::vector<floatingnumber>* pdf_scale;


    // EventInfoMETFilters
    bool	passFilter_HBHE;
    bool	passFilter_HBHEIso;
    bool	passFilter_HBHELoose;
    bool	passFilter_CSCHalo;
    bool	passFilter_HCALlaser;
    bool	passFilter_ECALDeadCell;
    bool	passFilter_GoodVtx;
    bool	passFilter_TrkFailure;
    bool	passFilter_EEBadSc;
    bool	passFilter_ECALlaser;
    bool	passFilter_TrkPOG;
    bool	passFilter_TrkPOG_manystrip;
    bool	passFilter_TrkPOG_toomanystrip;
    bool	passFilter_TrkPOG_logError;
    bool	passFilter_METFilters;
    bool        PV_filter;
    bool        passFilter_globalTightHalo2016;
    bool        passFilter_muonBadTrack;
    bool        passFilter_chargedHadronTrackResolution;

    float lheV_pt;
    float lheV_mass;
    float lheHT;
    int lheNj;

    Int_t PV_N;
    // save actual detail_level
    Int_t detailLevel;

  }; // class EventInfoNtupleObject

} // namespace Ntuple

#endif // SFRAME_NtupleVARIABLES_EventInfoNtupleObject_H
