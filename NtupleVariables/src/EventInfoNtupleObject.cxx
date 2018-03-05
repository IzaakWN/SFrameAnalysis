// $Id: EventInfoNtupleObject.cxx 43055 2015-01-29 16:26:25Z clange $

// Local include(s):
#include "../include/EventInfoNtupleObject.h"

namespace Ntuple {

  EventInfoNtupleObject::EventInfoNtupleObject( SCycleBaseNTuple* parent ) : SInputVariables< SCycleBaseNTuple >( parent ) {
  }


  void EventInfoNtupleObject::ConnectVariables( const TString& treeName,
                                              UInt_t detail_level,
                                              const TString& prefix,
                                              const TString& ntupleType ) throw( SError ) {

    // get instance of NtupleObjectNames
    NtupleObjectNames m_objectNames(ntupleType);
    //
    // variables to be connected:
    //
    ConnectVariable( treeName, m_objectNames.getName("runNumber"  ), runNumber  );
    ConnectVariable( treeName, m_objectNames.getName("eventNumber"), eventNumber);
    ConnectVariable( treeName, m_objectNames.getName("lumiBlock"  ), lumiBlock  );

    if( ( (detail_level & Ntuple::EventInfoBasic) == Ntuple::EventInfoBasic) ) {
      ConnectVariable( treeName, m_objectNames.getName("rho"          ), rho          );
      ConnectVariable( treeName, m_objectNames.getName("PV_filter"    ), PV_filter    );
      ConnectVariable( treeName, m_objectNames.getName("PV_N"         ), PV_N         );
    }
    if( (detail_level & Ntuple::EventInfoTrigger) == Ntuple::EventInfoTrigger ) {
      ConnectVariable( treeName, m_objectNames.getName("trigDecision"), trigDecision );
      //ConnectVariable( treeName, m_objectNames.getName("trigObject_pt"), trigObject_pt  );  
      //ConnectVariable( treeName, m_objectNames.getName("trigObject_eta"), trigObject_eta  );     
      //ConnectVariable( treeName, m_objectNames.getName("trigObject_phi"), trigObject_phi  );
      //ConnectVariable( treeName, m_objectNames.getName("trigObject_lastname"), trigObject_lastname  );
      //ConnectVariable( treeName, m_objectNames.getName("trigObject_filterLabels"), trigObject_filterLabels  );

    }
    if( (detail_level & Ntuple::EventInfoTruth) == Ntuple::EventInfoTruth ) {   
      ConnectVariable( treeName, m_objectNames.getName("genEventWeight"   ), genEventWeight   );
      ConnectVariable( treeName, m_objectNames.getName("lheV_pt"          ), lheV_pt          );
      ConnectVariable( treeName, m_objectNames.getName("lheV_mass"        ), lheV_mass        );
      ConnectVariable( treeName, m_objectNames.getName("lheHT"            ), lheHT            );
      ConnectVariable( treeName, m_objectNames.getName("lheNj"            ), lheNj            );
      ConnectVariable( treeName, m_objectNames.getName("averageIntPerXing"), averageIntPerXing);
      ConnectVariable( treeName, m_objectNames.getName("actualIntPerXing" ), actualIntPerXing );
      ConnectVariable( treeName, m_objectNames.getName("bunchCrossing"    ), bunchCrossing    );
    }
    if( (detail_level & Ntuple::EventInfoPDF) == Ntuple::EventInfoPDF  ) {
      ConnectVariable( treeName, m_objectNames.getName("pdf_id"   ), pdf_id    );
      ConnectVariable( treeName, m_objectNames.getName("pdf_x"    ), pdf_x     );
      ConnectVariable( treeName, m_objectNames.getName("pdf_xPDF" ), pdf_xPDF  );
      ConnectVariable( treeName, m_objectNames.getName("pdf_scale"), pdf_scale );
    }
    if( (detail_level & Ntuple::EventInfoMETFilters) == Ntuple::EventInfoMETFilters  ) {
      ConnectVariable( treeName, m_objectNames.getName("passFilter_HBHE"               ), passFilter_HBHE               );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_HBHEIso"            ), passFilter_HBHEIso            );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_HBHELoose"          ), passFilter_HBHELoose          );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_CSCHalo"            ), passFilter_CSCHalo            );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_HCALlaser"          ), passFilter_HCALlaser          );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_ECALDeadCell"       ), passFilter_ECALDeadCell       );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_GoodVtx"            ), passFilter_GoodVtx            );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_TrkFailure"         ), passFilter_TrkFailure         );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_EEBadSc"            ), passFilter_EEBadSc            );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_ECALlaser"          ), passFilter_ECALlaser          );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_TrkPOG"             ), passFilter_TrkPOG             );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_TrkPOG_manystrip"   ), passFilter_TrkPOG_manystrip   );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_TrkPOG_toomanystrip"), passFilter_TrkPOG_toomanystrip);
      ConnectVariable( treeName, m_objectNames.getName("passFilter_TrkPOG_logError"    ), passFilter_TrkPOG_logError    );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_METFilters"         ), passFilter_METFilters         );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_globalTightHalo2016"), passFilter_globalTightHalo2016);
      ConnectVariable( treeName, m_objectNames.getName("passFilter_muonBadTrack"       ), passFilter_muonBadTrack       );
      ConnectVariable( treeName, m_objectNames.getName("passFilter_chargedHadronTrackResolution"), passFilter_chargedHadronTrackResolution );
 
    }
    
    return;
    
  }

} // namespace Ntuple
