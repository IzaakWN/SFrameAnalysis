#ifndef __BTAGGINGSCALETOOL_H__
#define __BTAGGINGSCALETOOL_H__

#include <TH2.h>
#include "../NtupleVariables/include/Jet.h"
#include "../include/BTagCalibrationStandalone.h"

// SFrame include(s):
#include "core/include/SError.h"
#include "plug-ins/include/SToolBase.h"



class BTaggingScaleTool : public SToolBase {
  
  // Follow examples in https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagCalibration
  // Note: UZH::JetVec is a std::vector<UZH::Jet> typedef
  
 public:

  BTaggingScaleTool( SCycleBase* parent, const char* name = "BTaggingScaleTool" );
  ~BTaggingScaleTool();
  
  /// function booking histograms
  void BeginInputData( const SInputData& id ) throw( SError );
  
  /// function for AK4 jets
  double getScaleFactor( const double& pt, const double& eta, const int& flavour, bool isTagged, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4" );
  double getScaleFactor( const UZH::Jet& jet, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4");
  double getScaleFactor( const UZH::JetVec& vJets, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4" );
  
  /// function for Izaak: return just the scalefactor instead of the jetweight
  double getScaleFactor_noWeight( const double& pt, const double& eta, const int& flavour, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4" );
  double getScaleFactor_noWeight( const UZH::Jet& jet, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4");
  
  /// function for promote - demote: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#B_tag_scale_factors
  //double getScaleFactor_promote_demote( const UZH::JetVec& vJets, const double& sigma_bc = 0., const double& sigma_udsg = 0., const TString& jetCategory = "jet_ak4" );
  
  /// functions for efficiencies
  void bookHistograms();
  void fillEfficiencies( const UZH::JetVec& vJets, std::string channel="" );
  void readEfficiencies();
  double getEfficiency( const double& pt, const double& eta, const int& flavour, const TString& jetCategory = "jet_ak4" );
  double getEfficiency( const UZH::Jet& jet, const TString& jetCategory = "jet_ak4" );
  
  /// function to convert flavor integer to TString
  TString flavourToString( const int& flavour );
  
  /// help functions to check if jet is b-tagged according to chosen csv working point
  bool isTagged( const UZH::Jet& jet );
  bool isTagged( const double csv );


 private:

  std::string m_name; // name of the tool
  std::string m_tagger;
  std::string m_workingPoint;
  std::string m_csvFile;
  std::string m_measurementType_udsg;
  std::string m_measurementType_bc;
  std::string m_effHistDirectory;
  std::string m_effFile;
  std::vector<TString> m_jetCategories;
  std::vector<TString> m_flavours;
  std::map<std::string, double> CSV_WP; // could have a function to set these
  double currentWorkingPointCut;
  std::map<std::string, TH2F> m_effMaps;
  std::unique_ptr<BTagCalibrationReader> m_reader;
  std::unique_ptr<BTagCalibrationReader> m_reader_up;
  std::unique_ptr<BTagCalibrationReader> m_reader_down;
  
};


#endif //  __BTAGGINGSCALETOOL_H__
