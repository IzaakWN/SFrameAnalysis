#include "include/BTaggingScaleTool.h"

#include <cstdlib>
#include <limits>

#include <TFile.h>



//
// constructor
//
BTaggingScaleTool::BTaggingScaleTool( SCycleBase* parent, 
                                      const char* name ) : 
  SToolBase( parent ), m_name( name ) {

  SetLogName( name );

  std::string sframe_dir(std::getenv("SFRAME_DIR"));

  // m_calib = 0;
  // m_reader = 0;
  // m_reader_up = 0;
  // m_reader_down = 0;
  
  // if needed, probably best to append WP names a la Loose74X
  // see also use in BeginInputData
  wpCuts.clear();
  wpCuts["Loose"]  = 0.5426;
  wpCuts["Medium"] = 0.8484;
  wpCuts["Tight"]  = 0.9535;
  // wpCuts_veto.clear();
  // wpCuts_veto["Loose"] = 0.460;
  // wpCuts_veto["Medium"] = 0.800;
  // wpCuts_veto["Tight"] = 0.935;

  // wpCuts["Loose"] = 0.60;
  // wpCuts["Medium"] = 0.890;
  // wpCuts["Tight"] = 0.95;
 
  currentWorkingPointCut = -1;
  currentWorkingPointCut_veto = -1;
  m_effMaps.clear();
  m_effMaps_veto.clear();
  DeclareProperty( m_name + "_Tagger",    m_tagger = "CSVv2" );
  DeclareProperty( m_name + "_Tagger_veto",    m_tagger_veto = "CSVv2" );
 
  DeclareProperty( m_name + "_WorkingPoint", m_workingPoint = "Loose" );
  DeclareProperty( m_name + "_WorkingPoint_veto", m_workingPoint_veto = "Medium" );

  DeclareProperty( m_name + "_CsvFile", m_csvFile = sframe_dir + "/../BTaggingTools/csv/subjet_CSVv2_Moriond17_B_H.csv" ); // subjet_CSVv2_ichep.csv
  DeclareProperty( m_name + "_CsvFile_veto", m_csvFile_veto = sframe_dir + "/../BTaggingTools/csv/CSVv2_Moriond17_B_H.csv" );

  DeclareProperty( m_name + "_MeasurementType_udsg", m_measurementType_udsg = "incl" );//"incl" 
  DeclareProperty( m_name + "_MeasurementType_bc", m_measurementType_bc = "lt" );//"lt"

  DeclareProperty( m_name + "_MeasurementType_veto_udsg", m_measurementType_veto_udsg = "incl" ); //incl//comb
  DeclareProperty( m_name + "_MeasurementType_veto_bc", m_measurementType_veto_bc = "mujets" );


  DeclareProperty( m_name + "_EffHistDirectory", m_effHistDirectory = "bTagEff" );
  DeclareProperty( m_name + "_EffFile", m_effFile = sframe_dir + "/../BTaggingTools/efficiencies/bTagEffs_36p8_vMediumAk4_LooseAk8_lepVeto.root" ); // bTagEffs_15p9_v3.root
  DeclareProperty( m_name + "_EffFile_veto", m_effFile_veto = sframe_dir + "/../BTaggingTools/efficiencies/bTagEffs_36p8_vMediumAk4_LooseAk8_lepVeto.root" ); // Camilla // bTagEffs_15p9_v3.root
  //DeclareProperty( m_name + "_EffFile_veto", m_effFile_veto = sframe_dir + "/../BTaggingTools/efficiencies/bTagEffs_ichep2016.root" );

}



//
// destructor
//
BTaggingScaleTool::~BTaggingScaleTool() {
  // delete m_calib;
  // delete m_reader;
  // delete m_reader_up;
  // delete m_reader_down;
}



void BTaggingScaleTool::BeginInputData( const SInputData& ) throw( SError ) {

  m_logger << INFO << "Initializing BTagCalibrationStandalone" << SLogger::endmsg;
  m_logger << INFO << "CSV file:                  " << m_csvFile << SLogger::endmsg;
  m_logger << INFO << "CSV file for veto:         " << m_csvFile_veto << SLogger::endmsg;

  m_logger << INFO << "Tagger:                    " << m_tagger << SLogger::endmsg;
  m_logger << INFO << "Tagger for veto:           " << m_tagger_veto << SLogger::endmsg;
  m_logger << INFO << "WorkingPoint:              " << m_workingPoint << SLogger::endmsg;
  m_logger << INFO << "WorkingPoint for veto ak4: " << m_workingPoint_veto << SLogger::endmsg;

  m_logger << INFO << "MeasurementType veto udsg: " << m_measurementType_veto_udsg << SLogger::endmsg;
  m_logger << INFO << "MeasurementType veto  bc:  " << m_measurementType_veto_bc << SLogger::endmsg;

  m_logger << INFO << "MeasurementType udsg:      " << m_measurementType_udsg << SLogger::endmsg;
  m_logger << INFO << "MeasurementType bc:        " << m_measurementType_bc << SLogger::endmsg;
  
  m_logger << INFO << "EffHistDirectory:          " << m_effHistDirectory << SLogger::endmsg;
  m_logger << INFO << "Efficiency file:           " << m_effFile << SLogger::endmsg;
   
  BTagEntry::OperatingPoint wp = BTagEntry::OP_LOOSE;
  if (m_workingPoint.find("Loose") != std::string::npos) {
    wp = BTagEntry::OP_LOOSE;
    currentWorkingPointCut = wpCuts["Loose"];
  }
  else if (m_workingPoint.find("Medium") != std::string::npos) {
    wp = BTagEntry::OP_MEDIUM;
    currentWorkingPointCut = wpCuts["Medium"];
  }
  else if (m_workingPoint.find("Tight") != std::string::npos) {
    wp = BTagEntry::OP_TIGHT;
    currentWorkingPointCut = wpCuts["Tight"];
  }
  else if (m_workingPoint.find("Reshaping") != std::string::npos) {
    wp = BTagEntry::OP_RESHAPING;
    currentWorkingPointCut = wpCuts["Loose"]; //placeholder
    m_logger << WARNING << "Reshaping not yet implemented!" << SLogger::endmsg;
  }
  else {
    throw SError( ("Unknown working point: " + m_workingPoint).c_str(), SError::SkipCycle );
  }
  
  BTagEntry::OperatingPoint wp_veto = BTagEntry::OP_LOOSE;
  if (m_workingPoint_veto.find("Loose") != std::string::npos) {
    wp_veto = BTagEntry::OP_LOOSE;
    currentWorkingPointCut_veto = wpCuts["Loose"];
  }
  else if (m_workingPoint_veto.find("Medium") != std::string::npos) {
   
    std::cout << " working point medium"<<std::endl;
    wp_veto = BTagEntry::OP_MEDIUM;
    currentWorkingPointCut_veto = wpCuts["Medium"];

  }
  else if (m_workingPoint_veto.find("Tight") != std::string::npos) {
    wp_veto = BTagEntry::OP_TIGHT;
    currentWorkingPointCut_veto = wpCuts["Tight"];
  }
  else if (m_workingPoint_veto.find("Reshaping") != std::string::npos ) {
    wp_veto = BTagEntry::OP_RESHAPING;
    currentWorkingPointCut_veto = wpCuts["Loose"]; //placeholder
    m_logger << WARNING << "Reshaping not yet implemented!" << SLogger::endmsg;
  }
  else {
    throw SError( ("Unknown working point: " + m_workingPoint_veto).c_str(), SError::SkipCycle );
  }

  BTagCalibration m_calib(m_tagger, m_csvFile);

  m_reader.reset(new BTagCalibrationReader(wp, "central"));
  m_reader_up.reset(new BTagCalibrationReader(wp, "up"));
  m_reader_down.reset(new BTagCalibrationReader(wp, "down"));
  
  m_reader->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);
  m_reader->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);
  m_reader->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  m_reader_up->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);
  m_reader_up->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);
  m_reader_up->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  m_reader_down->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);
  m_reader_down->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);
  m_reader_down->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);



  BTagCalibration m_calib_veto(m_tagger_veto, m_csvFile_veto );

  m_reader_veto.reset(new BTagCalibrationReader(wp_veto, "central"));
  m_reader_veto_up.reset(new BTagCalibrationReader(wp_veto, "up"));
  m_reader_veto_down.reset(new BTagCalibrationReader(wp_veto, "down"));
  
  m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_veto_bc);
  m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_veto_bc);
  m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_veto_udsg);
  m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_veto_bc);
  m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_veto_bc);
  m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_veto_udsg);
  m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_veto_bc);
  m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_veto_bc);
  m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_veto_udsg);
  // m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_bc);
  // m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_bc);
  // m_reader_veto->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  // m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_bc);
  // m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_bc);
  // m_reader_veto_up->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  // m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_B, m_measurementType_bc);
  // m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_C, m_measurementType_bc);
  // m_reader_veto_down->load(m_calib_veto, BTagEntry::FLAV_UDSG, m_measurementType_udsg);


  
  // jet categories for efficiencies
  m_jetCategories = {"jet", "subjet_softdrop"};//"jet",
  m_jetCategories_veto = {"jet_ak4"};
  m_flavours = {"b", "c", "udsg"};
  
  // read in efficiencies
  readEfficiencies();

  return;

}



double BTaggingScaleTool::getScaleFactor( const double& pt, const double& eta, const int& flavour, bool isTagged, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  // Flavor
  BTagEntry::JetFlavor flavorEnum = BTagEntry::FLAV_UDSG;
  if  ( fabs(flavour)==5) flavorEnum = BTagEntry::FLAV_B;
  if  ( fabs(flavour)==15) flavorEnum = BTagEntry::FLAV_C;
  if  ( fabs(flavour)==4) flavorEnum = BTagEntry::FLAV_C;

  double MaxEta = 2.4;
  double abs_eta = fabs(eta);
  if (abs_eta > MaxEta) {
    // outside tracker range
    return 1.;
  }
  
  // range checking, double uncertainty if beyond
  std::pair<float, float> sf_bounds = m_reader->min_max_pt(flavorEnum, abs_eta);
  
  m_logger << DEBUG << "     flavor " << flavorEnum << " - " << sf_bounds.first << " " << sf_bounds.second <<" jet pt "<< pt<<  SLogger::endmsg;

  float pt_for_eval = pt;
  bool is_out_of_bounds = false;
  if (pt < sf_bounds.first) {
    pt_for_eval = sf_bounds.first + 1e-5;
    is_out_of_bounds = true;
  } else if (pt >= sf_bounds.second) {
    pt_for_eval = sf_bounds.second - 0.1;
    is_out_of_bounds = true;
  }
  m_logger << DEBUG << "*******  out of band ? " << is_out_of_bounds << "so pt_for_eval_used " <<  pt_for_eval << SLogger::endmsg;
  double sigmaScale_bc = sigma_bc;
  double sigmaScale_udsg = sigma_udsg;
  // double uncertainty in case jet outside normal kinematics
  if (is_out_of_bounds) {
    m_logger << DEBUG << sf_bounds.first << " - " << sf_bounds.second << SLogger::endmsg;
    m_logger << DEBUG << "out of bounds, using: " << pt_for_eval << " and " << abs_eta << SLogger::endmsg;
    sigmaScale_bc *= 2;
    sigmaScale_udsg *= 2;
  }
  
  m_logger << DEBUG << "getting scale factor " << SLogger::endmsg;
  double scalefactor = m_reader->eval(flavorEnum, eta, pt_for_eval);
  m_logger << DEBUG << "scale factor: " << scalefactor << SLogger::endmsg;
  if ((flavour == 5) || (flavour == 4)) {
    if ((sigma_bc > std::numeric_limits<double>::epsilon()) || (sigma_bc < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_bc > 0) {
        double scalefactor_up =  m_reader_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_bc*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_bc)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  else {
    if ((sigma_udsg > std::numeric_limits<double>::epsilon()) || (sigma_udsg < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_udsg > 0) {
        double scalefactor_up =  m_reader_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_udsg*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_udsg)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  if (scalefactor == 0) {
    throw SError( "Scale factor returned is zero!", SError::SkipCycle );
  }
  
  m_logger << DEBUG << "getting final weight for flav " << flavorEnum << SLogger::endmsg;
  
  double jetweight = 1.;
  // set effMC close to one for now, need to use real value map later
  double effMC = getEfficiency(pt, eta, flavour, jetCategory);
  
  if (isTagged) {
    m_logger << DEBUG << "     Jet is tagged " << SLogger::endmsg;
    jetweight *= scalefactor;
  }
  else {
    m_logger << DEBUG << "     Jet is not tagged " << SLogger::endmsg;
    jetweight *= (1 - (scalefactor * effMC)) / (1 - effMC);
  }
  
  m_logger << DEBUG << " jetweight " << jetweight << SLogger::endmsg;

  return jetweight;
}



double BTaggingScaleTool::getScaleFactor_veto( const double& pt, const double& eta, const int& flavour, bool isTagged, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {
  m_logger << DEBUG << "     flavor " <<  flavour<<  SLogger::endmsg;
  // Flavor
  BTagEntry::JetFlavor flavorEnum = BTagEntry::FLAV_UDSG;
  
  if  ( fabs(flavour)==5) flavorEnum = BTagEntry::FLAV_B;
  if  ( fabs(flavour)==15) flavorEnum = BTagEntry::FLAV_C;
  if  ( fabs(flavour)==4) flavorEnum = BTagEntry::FLAV_C;

  double MaxEta = 2.4;
  double abs_eta = fabs(eta);
  if (abs_eta > MaxEta) {
    // outside tracker range
    return 1.;
  }
  
  // range checking, double uncertainty if beyond
  std::pair<float, float> sf_bounds = m_reader_veto->min_max_pt(flavorEnum, abs_eta);
  
  m_logger << DEBUG << "     flavorEnum  " << flavorEnum << " ;pt bound min " << sf_bounds.first << " ;pt bound max " << sf_bounds.second <<" jet pt "<< pt<<  SLogger::endmsg;

  float pt_for_eval = pt;
  bool is_out_of_bounds = false;
  if (pt < sf_bounds.first) {
    pt_for_eval = sf_bounds.first + 1e-5;
    is_out_of_bounds = true;
  } else if (pt >= sf_bounds.second) {
    pt_for_eval = sf_bounds.second - 0.1;
    is_out_of_bounds = true;
  }
  m_logger << DEBUG << "*******  out of band ? " << is_out_of_bounds << "so pt_for_eval used " <<  pt_for_eval << SLogger::endmsg;
  double sigmaScale_bc = sigma_bc;
  double sigmaScale_udsg = sigma_udsg;
  // double uncertainty in case jet outside normal kinematics
  if (is_out_of_bounds) {
    m_logger << DEBUG << sf_bounds.first << " - " << sf_bounds.second << SLogger::endmsg;
    m_logger << DEBUG << "out of bounds, using: " << pt_for_eval << " and " << abs_eta << SLogger::endmsg;
    sigmaScale_bc *= 2;
    sigmaScale_udsg *= 2;
  }
  
 
  double scalefactor = m_reader_veto->eval(flavorEnum, eta, pt_for_eval);
  m_logger << DEBUG << "scale factor: " << scalefactor << SLogger::endmsg;
  if ((flavour == 5) || (flavour == 4)) {
    if ((sigma_bc > std::numeric_limits<double>::epsilon()) || (sigma_bc < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_bc > 0) {
        double scalefactor_up =  m_reader_veto_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_bc*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_veto_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_bc)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  else {
    if ((sigma_udsg > std::numeric_limits<double>::epsilon()) || (sigma_udsg < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_udsg > 0) {
        double scalefactor_up =  m_reader_veto_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_udsg*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_veto_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_udsg)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  if (scalefactor == 0) {
    throw SError( "Scale factor returned is zero!", SError::SkipCycle );
  }
  
  m_logger << DEBUG << "getting final weight for flavorEnum  " << flavorEnum << SLogger::endmsg;
  
  double jetweight = 1.;
  // set effMC close to one for now, need to use real value map later
  double effMC = getEfficiency(pt, eta, flavour, "jet_ak4");/// maybe change "jet_ak4_
  m_logger << DEBUG << "    Efficiency " << effMC <<SLogger::endmsg;
  if (isTagged) {
    m_logger << DEBUG << "     Jet is tagged " << SLogger::endmsg;
    jetweight *= scalefactor;
  }
  else {
    m_logger << DEBUG << "     Jet is not tagged " << SLogger::endmsg;
    jetweight *= (1 - (scalefactor * effMC)) / (1 - effMC);
  }
  
  m_logger << DEBUG << " jetweight " << jetweight << SLogger::endmsg;

  return jetweight;
}



double BTaggingScaleTool::getScaleFactor_noWeight( const double& pt, const double& eta, const int& flavour, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {
  m_logger << DEBUG << "     flavor " <<  flavour<<  SLogger::endmsg;
  // Flavor
  BTagEntry::JetFlavor flavorEnum = BTagEntry::FLAV_UDSG;
  
  if  ( fabs(flavour)==5  ) flavorEnum = BTagEntry::FLAV_B;
  if  ( fabs(flavour)==15 ) flavorEnum = BTagEntry::FLAV_C;
  if  ( fabs(flavour)==4  ) flavorEnum = BTagEntry::FLAV_C;

  double MaxEta = 2.4;
  double abs_eta = fabs(eta);
  if (abs_eta > MaxEta) {
    // outside tracker range
    return 1.;
  }
  
  // range checking, double uncertainty if beyond
  std::pair<float, float> sf_bounds = m_reader_veto->min_max_pt(flavorEnum, abs_eta);
  
  m_logger << DEBUG << "     flavorEnum  " << flavorEnum << " ;pt bound min " << sf_bounds.first << " ;pt bound max " << sf_bounds.second <<" jet pt "<< pt<<  SLogger::endmsg;

  float pt_for_eval = pt;
  bool is_out_of_bounds = false;
  if (pt < sf_bounds.first) {
    pt_for_eval = sf_bounds.first + 1e-5;
    is_out_of_bounds = true;
  } else if (pt >= sf_bounds.second) {
    pt_for_eval = sf_bounds.second - 0.1;
    is_out_of_bounds = true;
  }
  m_logger << DEBUG << "*******  out of band ? " << is_out_of_bounds << "so pt_for_eval used " <<  pt_for_eval << SLogger::endmsg;
  double sigmaScale_bc = sigma_bc;
  double sigmaScale_udsg = sigma_udsg;
  // double uncertainty in case jet outside normal kinematics
  if (is_out_of_bounds) {
    m_logger << DEBUG << sf_bounds.first << " - " << sf_bounds.second << SLogger::endmsg;
    m_logger << DEBUG << "out of bounds, using: " << pt_for_eval << " and " << abs_eta << SLogger::endmsg;
    sigmaScale_bc *= 2;
    sigmaScale_udsg *= 2;
  }
  
  // get scalefactor
  double scalefactor = m_reader_veto->eval(flavorEnum, eta, pt_for_eval);
  m_logger << DEBUG << "scale factor: " << scalefactor << SLogger::endmsg;
  if ((flavour == 5) || (flavour == 4)) {
    if ((sigma_bc > std::numeric_limits<double>::epsilon()) || (sigma_bc < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_bc > 0) {
        double scalefactor_up =  m_reader_veto_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_bc*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_veto_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_bc)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  else {
    if ((sigma_udsg > std::numeric_limits<double>::epsilon()) || (sigma_udsg < -std::numeric_limits<double>::epsilon())) {
      // m_logger << DEBUG << "limit: " << std::numeric_limits<double>::epsilon() << " value: " << sigma << SLogger::endmsg;
      if (sigma_udsg > 0) {
        double scalefactor_up =  m_reader_veto_up->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = sigmaScale_udsg*(scalefactor_up - scalefactor) + scalefactor;
      }
      else {
        double scalefactor_down =  m_reader_veto_down->eval(flavorEnum, eta, pt_for_eval);
        scalefactor = fabs(sigmaScale_udsg)*(scalefactor_down - scalefactor) + scalefactor;
      }
    }
  }
  if (scalefactor == 0) {
    throw SError( "Scale factor returned is zero!", SError::SkipCycle );
  }
  
  m_logger << DEBUG << " scalingfactor " << scalefactor << SLogger::endmsg;
  return scalefactor;
  
}



double BTaggingScaleTool::getScaleFactor( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  double jetweight = getScaleFactor(jet.pt(), jet.eta(), jet.hadronFlavour(), isTagged(jet), sigma_bc, sigma_udsg, jetCategory);

  return jetweight;
  
}



double BTaggingScaleTool::getScaleFactor_veto( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  // use fabs ?
  double jetweight = getScaleFactor_veto(jet.pt(), jet.eta(), jet.hadronFlavour(), isTagged_veto(jet), sigma_bc, sigma_udsg, jetCategory);

  return jetweight;
  
}



double BTaggingScaleTool::getScaleFactor_noWeight( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  // use fabs ?
  double jetweight = getScaleFactor_noWeight(jet.pt(), jet.eta(), jet.hadronFlavour(), sigma_bc, sigma_udsg, jetCategory);

  return jetweight;
  
}



double BTaggingScaleTool::getSoftdropSubjetScaleFactor( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  double jetweight = 1;
  
  for (int i = 0; i < jet.subjet_softdrop_N(); ++i) {
    m_logger << DEBUG << "Looking at softdrop subjet " << i
	     << ", pT=" << jet.subjet_softdrop_pt()[i] << ", eta=" << jet.subjet_softdrop_eta()[i]
	     << SLogger::endmsg;
    jetweight *= getScaleFactor(jet.subjet_softdrop_pt()[i], jet.subjet_softdrop_eta()[i], jet.subjet_softdrop_hadronFlavour()[i], isTagged(jet.subjet_softdrop_csv()[i]), sigma_bc, sigma_udsg, jetCategory);
  }

  return jetweight;
  
}



//
// return scale for Jet collection
//
double BTaggingScaleTool::getScaleFactor( const UZH::JetVec& vJets, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory) {

  double scale = 1.;
  
  m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor" << SLogger::endmsg;

  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;

    scale *= getScaleFactor(*itJet, sigma_bc, sigma_udsg, jetCategory);
  }  

  m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor done" << SLogger::endmsg;
  return scale;

}



double BTaggingScaleTool::getScaleFactor_veto( const UZH::JetVec& vJets, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory) {

  double scale = 1.;
  
  m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor_veto" << SLogger::endmsg;

  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;

    scale *= getScaleFactor_veto(*itJet, sigma_bc, sigma_udsg, jetCategory);
  }  

  m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor_veto done and total weight is " << scale<<  SLogger::endmsg;
  return scale;

}



// double BTaggingScaleTool::getScaleFactor_promote_demote( const UZH::JetVec& vJets, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory) {
//   // https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#B_tag_scale_factors
// 
//   double scale = 1.;
//   
//   m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor_promote_demote" << SLogger::endmsg;
// 
// //   TRandom3
// //   rand->SetSeed((int)((jet_eta+5)*100000))
// 
//   for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
//     m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
// 	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
// 	     << SLogger::endmsg;
// 
//     scale *= getScaleFactor_veto(*itJet, sigma_bc, sigma_udsg, jetCategory);
//   }  
// 
//   m_logger << DEBUG << "BTaggingScaleTool::getScaleFactor_promote_demote done" <<  SLogger::endmsg;
//   return scale;
// 
// }



//
// return scale for Jet collection
//
double BTaggingScaleTool::getSoftdropSubjetScaleFactor( const UZH::JetVec& vJets, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {

  double scale = 1.;
  
  m_logger << DEBUG << "BTaggingScaleTool::getSoftdropSubjetScaleFactor" << SLogger::endmsg;

  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;

    scale *= getSoftdropSubjetScaleFactor(*itJet, sigma_bc, sigma_udsg, jetCategory);
  }  

  m_logger << DEBUG << "BTaggingScaleTool::getSoftdropSubjetScaleFactor done" << SLogger::endmsg;
  return scale;

}



/// function to book histograms for efficiencies
void BTaggingScaleTool::bookHistograms() {
  
  const int nPtBins = 11;
  const int nEtaBins = 4;
  float ptBins[nPtBins+1] = {10, 20, 30, 50, 70, 100, 140, 200, 300, 670, 1000, 1500};
  float etaBins[nEtaBins+1] = {-2.5, -1.5, 0, 1.5, 2.5};
  
  for (std::vector<TString>::const_iterator jetCat = m_jetCategories.begin(); jetCat != m_jetCategories.end(); ++jetCat) {
    for (std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav) {
      Book( TH2F( *jetCat + "_" + *flav + "_" + m_workingPoint, *jetCat + "_" + *flav + "_" + m_workingPoint, nPtBins, ptBins, nEtaBins, etaBins ), m_effHistDirectory.c_str() );
      Book( TH2F( *jetCat + "_" + *flav + "_all", *jetCat + "_" + *flav + "_all", nPtBins, ptBins, nEtaBins, etaBins ), m_effHistDirectory.c_str() );
    }
  }

  for (std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav) {
    Book( TH2F("jet_ak4_" + *flav + "_" + m_workingPoint_veto, "jet_ak4_" + *flav + "_" + m_workingPoint_veto, nPtBins, ptBins, nEtaBins, etaBins ), m_effHistDirectory.c_str() );
    Book( TH2F( "jet_ak4_" + *flav + "_all", "jet_ak4_" + *flav + "_all", nPtBins, ptBins, nEtaBins, etaBins ), m_effHistDirectory.c_str() );
  }

  
}



/// function to fill jet b-tagging efficiencies
void BTaggingScaleTool::fillEfficiencies( const UZH::JetVec& vJets ) {
  
  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;
    TString flavourString = flavourToString(itJet->hadronFlavour());
    if (isTagged(*itJet)) {
      Hist( "jet_" + flavourString + "_" + m_workingPoint, m_effHistDirectory.c_str() )->Fill( itJet->pt(), itJet->eta() );
    }
    Hist( "jet_" + flavourString + "_all", m_effHistDirectory.c_str() )->Fill( itJet->pt(), itJet->eta() );
  }
  
}



/// function to fill jet b-tagging efficiencies for Ak4 used in veto
void BTaggingScaleTool::fillEfficiencies_veto( const UZH::JetVec& vJets ) {
  
  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;
    TString flavourString = flavourToString(itJet->hadronFlavour());
    if (isTagged_veto(*itJet)) {
      Hist( "jet_ak4_" + flavourString + "_" + m_workingPoint_veto, m_effHistDirectory.c_str() )->Fill( itJet->pt(), itJet->eta() );
    }
    Hist( "jet_ak4_" + flavourString + "_all", m_effHistDirectory.c_str() )->Fill( itJet->pt(), itJet->eta() );
  }
  
}



/// function to fill subjet b-tagging efficiencies
void BTaggingScaleTool::fillSoftdropSubjetEfficiencies( const UZH::JetVec& vJets ) {
  
  for (std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet) {
    m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
	     << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
	     << SLogger::endmsg;
    for (int i = 0; i < itJet->subjet_softdrop_N(); ++i) {
      m_logger << DEBUG << "Looking at softdrop subjet " << i
  	     << ", pT=" << itJet->subjet_softdrop_pt()[i] << ", eta=" << itJet->subjet_softdrop_eta()[i]
  	     << SLogger::endmsg;
      TString flavourString = flavourToString(itJet->subjet_softdrop_hadronFlavour()[i]);
      if (isTagged(itJet->subjet_softdrop_csv()[i])) {
        Hist( "subjet_softdrop_" + flavourString + "_" + m_workingPoint, m_effHistDirectory.c_str() )->Fill( itJet->subjet_softdrop_pt()[i], itJet->subjet_softdrop_eta()[i] );
      }
      Hist( "subjet_softdrop_" + flavourString + "_all", m_effHistDirectory.c_str() )->Fill( itJet->subjet_softdrop_pt()[i], itJet->subjet_softdrop_eta()[i] );
    }
  }
  
}



/// function to read efficiencies
void BTaggingScaleTool::readEfficiencies() {
  
  m_logger << INFO << "Reading in b-tagging efficiencies from file " << m_effFile << SLogger::endmsg;
  auto inFile = TFile::Open(m_effFile.c_str());
  
  for (std::vector<TString>::iterator jetCat = m_jetCategories.begin(); jetCat != m_jetCategories.end(); ++jetCat) {
    for (std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav) {
      auto hPass = (TH2F*) inFile->Get( m_effHistDirectory + "/" + *jetCat + "_" + *flav + "_" + m_workingPoint);
      auto hAll = (TH2F*) inFile->Get( m_effHistDirectory + "/" + *jetCat + "_" + *flav + "_all");
      TH2F hEff = *((TH2F*) hPass->Clone( m_effHistDirectory + "_" + *jetCat + "_" + *flav + "_" + m_workingPoint ));
      hEff.Divide(hAll);
      // delete hPass;
      // delete hAll;
      m_effMaps[(*jetCat + "_" + *flav + "_" + m_workingPoint).Data()] = hEff;
      m_logger << DEBUG << "effi TH2D binsx: " << hEff.GetNbinsX() << " binsy: " << hEff.GetNbinsY() << SLogger::endmsg;
    }
  }
  inFile->Close();
  // delete inFile;
  
  m_logger << INFO << "For Veto:Reading in b-tagging efficiencies from file " << m_effFile_veto << SLogger::endmsg;
  auto inFile_veto = TFile::Open(m_effFile_veto.c_str());
  
  for (std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav) {
    auto hPass_veto = (TH2F*) inFile_veto->Get( m_effHistDirectory + "/" + "jet_ak4_" + *flav + "_" + m_workingPoint_veto);
    auto hAll_veto = (TH2F*) inFile_veto->Get( m_effHistDirectory + "/" + "jet_ak4_" + *flav + "_all");
    TH2F hEff_veto = *((TH2F*) hPass_veto->Clone( m_effHistDirectory + "_jet_ak4_" + *flav + "_" + m_workingPoint_veto ));
    hEff_veto.Divide(hAll_veto);
    // delete hPass;
    // delete hAll;
    m_effMaps_veto[( "jet_ak4_" + *flav + "_" + m_workingPoint_veto).Data()] = hEff_veto;
    m_logger << DEBUG << "effi Veto TH2D binsx: " << hEff_veto.GetNbinsX() << " binsy: " << hEff_veto.GetNbinsY() << SLogger::endmsg;
  }
  
  inFile_veto->Close();


}



double BTaggingScaleTool::getEfficiency( const double& pt, const double& eta, const int& flavour, const TString& jetCategory ) {
  double eff = 1.;
 
  if (jetCategory!="jet_ak4"){
 
    TH2F thisHist = m_effMaps[(jetCategory + "_" + flavourToString(flavour) + "_" + m_workingPoint).Data()];
    m_logger << DEBUG << /*thisHist << " " << */ thisHist.GetName() << SLogger::endmsg;
    int binx = thisHist.GetXaxis()->FindBin(pt);
    if( pt >   thisHist.GetXaxis()->GetBinLowEdge(thisHist.GetNbinsX()+1)) binx = thisHist.GetNbinsX(); // added by Izaak
    int biny = thisHist.GetYaxis()->FindBin(eta);
    m_logger << DEBUG << "binx = " << binx << " biny = " << biny << SLogger::endmsg;
    m_logger << DEBUG << "maxx = " << thisHist.GetNbinsX() << " maxy = " << thisHist.GetNbinsY() << SLogger::endmsg;
    // implement check for overflow
    eff = thisHist.GetBinContent(binx, biny);
    m_logger << DEBUG << "For "<< jetCategory << " with pt = " << pt << ", eta = " << eta << ", flavour = " << flavour << " returning efficiency =" << eff << SLogger::endmsg;
 
  }else{
    
    TH2F thisHist_veto = m_effMaps_veto[("jet_ak4_" + flavourToString(flavour) + "_" + m_workingPoint_veto).Data()];
    m_logger << DEBUG << /*thisHist << " " << */ thisHist_veto.GetName() << SLogger::endmsg;
    int binx = thisHist_veto.GetXaxis()->FindBin(pt);
    if( pt >   thisHist_veto.GetXaxis()->GetBinLowEdge(thisHist_veto.GetNbinsX()+1)) binx = thisHist_veto.GetNbinsX(); // added by Izaak
    int biny = thisHist_veto.GetYaxis()->FindBin(eta);
    m_logger << DEBUG << "binx = " << binx << " biny = " << biny << SLogger::endmsg;
    m_logger << DEBUG << "maxx = " << thisHist_veto.GetNbinsX() << " maxy = " << thisHist_veto.GetNbinsY() << SLogger::endmsg;
    // implement check for overflow
    eff = thisHist_veto.GetBinContent(binx, biny);
    m_logger << DEBUG << "For "<< jetCategory << " with pt = " << pt << ", eta = " << eta << ", flavour = " << flavour << " returning efficiency =" << eff << SLogger::endmsg;
 
  }
  return eff;
  
}



double BTaggingScaleTool::getEfficiency( const UZH::Jet& jet, const TString& jetCategory ) {
  // https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2016#B_tag_scale_factors
  
  // TODO test eta with / without fabs
  
  //std::cout << "getBTagSF_promote_demote" << std::endl;
  
  return getEfficiency(jet.pt(),jet.eta(),jet.hadronFlavour(),jetCategory);
}



TString BTaggingScaleTool::flavourToString( const int& flavour ) {
  
  TString flavourString = "udsg";
  
  if (flavour == 5) {
    flavourString = "b";
  }
  else if (flavour == 4) {
    flavourString = "c";
  }
  // else if (flavour == 15) {
  //   flavourString = "c"; // Use C scale factors for tau for now.
  // }
  
  return flavourString;
  
}



bool BTaggingScaleTool::isTagged( const UZH::Jet& jet ) {
  
  if (jet.csv() > currentWorkingPointCut) {
    return true;  
  }
  return false;
  
}



bool BTaggingScaleTool::isTagged( const double& csv ) {
  
  if (csv > currentWorkingPointCut) {
    return true;  
  }
  return false;
  
}



bool BTaggingScaleTool::isTagged_veto(  const UZH::Jet& jet  ) {
  
  if (jet.csv() > currentWorkingPointCut_veto) {
    //std::cout << " jet.csv() " <<jet.csv() << " > currentWorkingPointCut_veto " << currentWorkingPointCut_veto << std::endl;
    return true;  
  }
  return false;
  
}



bool BTaggingScaleTool::isTagged_veto( const double& csv ) {
  
  if (csv > currentWorkingPointCut_veto) {
    //std::cout << " csv " <<csv << " > currentWorkingPointCut_veto " << currentWorkingPointCut_veto << std::endl;
    return true;  
  }
  return false;
  
}
