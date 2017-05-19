#include "include/BTaggingScaleTool.h"
#include <cstdlib>
#include <limits>
#include <TFile.h>



BTaggingScaleTool::BTaggingScaleTool( SCycleBase* parent, const char* name ) : 
  SToolBase( parent ), m_name( name ) {

  SetLogName( name );

  std::string sframe_dir(std::getenv("SFRAME_DIR"));

  CSV_WP.clear();
  CSV_WP["Loose"]  = 0.5426;
  CSV_WP["Medium"] = 0.8484;
  CSV_WP["Tight"]  = 0.9535;
 
  currentWorkingPointCut = -1;
  m_effMaps.clear();

  DeclareProperty( m_name + "_Tagger",    m_tagger = "CSVv2" );
  DeclareProperty( m_name + "_WorkingPoint", m_workingPoint = "Medium" );  
  DeclareProperty( m_name + "_CsvFile", m_csvFile = sframe_dir + "/../BTaggingTools/csv/CSVv2_Moriond17_B_H.csv" ); // subjet_CSVv2_ichep.csv
  
  DeclareProperty( m_name + "_MeasurementType_udsg", m_measurementType_udsg = "incl" ); 
  DeclareProperty( m_name + "_MeasurementType_bc", m_measurementType_bc = "mujets" ); // for AK4 jets; for AK8 jets, use "lt"
  
  DeclareProperty( m_name + "_EffHistDirectory", m_effHistDirectory = "bTagEff" );
  DeclareProperty( m_name + "_EffFile", m_effFile = sframe_dir + "/../BTaggingTools/efficiencies/bTagEffs_HTT_baseline.root" );

}



BTaggingScaleTool::~BTaggingScaleTool(){ }



void BTaggingScaleTool::BeginInputData( const SInputData& ) throw( SError ) {
  
  // jet categories for efficiencies
  m_jetCategories = {"jet_ak4"}; //"jet", "subjet_softdrop"};
  m_flavours = {"udsg", "b", "c"};
  
  BTagEntry::OperatingPoint wp = BTagEntry::OP_LOOSE;
  if (m_workingPoint.find("Loose") != std::string::npos) {
    wp = BTagEntry::OP_LOOSE;
    currentWorkingPointCut = CSV_WP["Loose"];
  }
  else if (m_workingPoint.find("Medium") != std::string::npos) {
    //std::cout << " working point medium"<<std::endl;
    wp = BTagEntry::OP_MEDIUM;
    currentWorkingPointCut = CSV_WP["Medium"];
  }
  else if (m_workingPoint.find("Tight") != std::string::npos) {
    wp = BTagEntry::OP_TIGHT;
    currentWorkingPointCut = CSV_WP["Tight"];
  }
  else {
    throw SError( ("Unknown working point: " + m_workingPoint).c_str(), SError::SkipCycle );
  }
  
  m_logger << INFO << "Tagger:                " << m_tagger << SLogger::endmsg;
  m_logger << INFO << "WorkingPoint:          " << m_workingPoint << SLogger::endmsg;
  m_logger << INFO << "WorkingPoint Cut:      " << currentWorkingPointCut << SLogger::endmsg;
  m_logger << INFO << "MeasurementType udsg:  " << m_measurementType_udsg << SLogger::endmsg;
  m_logger << INFO << "MeasurementType bc:    " << m_measurementType_bc << SLogger::endmsg;
  m_logger << INFO << "EffHistDirectory:      " << m_effHistDirectory << SLogger::endmsg;
  m_logger << INFO << "Efficiency file:       " << m_effFile << SLogger::endmsg;
  m_logger << INFO << "CSV file:              " << m_csvFile << SLogger::endmsg;
  m_logger << INFO << "Initializing BTagCalibrationStandalone  " << SLogger::endmsg;

  BTagCalibration m_calib(m_tagger, m_csvFile);  
  
  m_reader.reset(      new BTagCalibrationReader(wp, "central" ));
  m_reader_up.reset(   new BTagCalibrationReader(wp, "up"      ));
  m_reader_down.reset( new BTagCalibrationReader(wp, "down"    ));
  
  m_logger << INFO << "Reader loading";
  m_reader->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);
  m_reader->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);         m_logger << INFO << ".";
  m_reader->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  m_reader_up->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);
  m_reader_up->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);      m_logger << INFO << ".";
  m_reader_up->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  m_reader_down->load(m_calib, BTagEntry::FLAV_B, m_measurementType_bc);    m_logger << INFO << ".";
  m_reader_down->load(m_calib, BTagEntry::FLAV_C, m_measurementType_bc);
  m_reader_down->load(m_calib, BTagEntry::FLAV_UDSG, m_measurementType_udsg);
  m_logger << INFO << " done" << SLogger::endmsg;
  
  // read in efficiencies
  readEfficiencies();
  
  return;

}



double BTaggingScaleTool::getScaleFactor( const double& pt, const double& eta, const int& flavour, bool isTagged, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ){
  //std::cout << ">>> BTaggingScaleTool::getScaleFactor" << std::endl;
  //m_logger << DEBUG << "     flavor " << flavorEnum << " - " << sf_bounds.first << " " << sf_bounds.second <<" jet pt "<< pt<<  SLogger::endmsg;

  // Flavor
  BTagEntry::JetFlavor flavorEnum = BTagEntry::FLAV_UDSG;
  if  ( fabs(flavour)== 5) flavorEnum = BTagEntry::FLAV_B;
  if  ( fabs(flavour)==15) flavorEnum = BTagEntry::FLAV_C;
  if  ( fabs(flavour)== 4) flavorEnum = BTagEntry::FLAV_C;

  double MaxEta = 2.4;
  double abs_eta = fabs(eta);
  if (abs_eta > MaxEta) {
    // outside tracker range
    return 1.;
  }
  
  // range checking, double uncertainty if beyond
  std::pair<float, float> sf_bounds = m_reader->min_max_pt(flavorEnum, abs_eta);
  
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



double BTaggingScaleTool::getScaleFactor_noWeight( const double& pt, const double& eta, const int& flavour, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ){
  //std::cout << ">>> BTaggingScaleTool::getScaleFactor_noWeight" << std::endl;
  m_logger << DEBUG << "     flavor " <<  flavour<<  SLogger::endmsg;
  
  BTagEntry::JetFlavor flavorEnum = BTagEntry::FLAV_UDSG;
  if  ( fabs(flavour)==5  ) flavorEnum = BTagEntry::FLAV_B;
  if  ( fabs(flavour)==15 ) flavorEnum = BTagEntry::FLAV_C;
  if  ( fabs(flavour)==4  ) flavorEnum = BTagEntry::FLAV_C;

  double MaxEta = 2.4;
  double abs_eta = fabs(eta);
  if (abs_eta > MaxEta) { // outside tracker range
    return 1.;
  }
  
  // range checking, double uncertainty if beyond
  std::pair<float, float> sf_bounds = m_reader->min_max_pt(flavorEnum, abs_eta);
  
  m_logger << DEBUG << "     flavorEnum  " << flavorEnum << "; pt bound min " << sf_bounds.first << "; pt bound max " << sf_bounds.second <<" jet pt "<< pt<<  SLogger::endmsg;

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
  
  m_logger << DEBUG << " scalingfactor " << scalefactor << SLogger::endmsg;
  return scalefactor;
  
}



double BTaggingScaleTool::getScaleFactor( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {
  // use fabs ?
  double jetweight = getScaleFactor(jet.pt(), jet.eta(), jet.hadronFlavour(), isTagged(jet), sigma_bc, sigma_udsg, jetCategory);
  return jetweight;
}



double BTaggingScaleTool::getScaleFactor_noWeight( const UZH::Jet& jet, const double& sigma_bc, const double& sigma_udsg, const TString& jetCategory ) {
  // use fabs ?
  double jetweight = getScaleFactor_noWeight(jet.pt(), jet.eta(), jet.hadronFlavour(), sigma_bc, sigma_udsg, jetCategory);
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



/// function to book histograms for efficiencies
void BTaggingScaleTool::bookHistograms() {
  
  const int nPtBins = 11;
  const int nEtaBins = 4;
  float ptBins[nPtBins+1] = {10, 20, 30, 50, 70, 100, 140, 200, 300, 670, 1000, 1500};
  float etaBins[nEtaBins+1] = {-2.5, -1.5, 0, 1.5, 2.5};
  std::string directories[3] = {m_effHistDirectory, m_effHistDirectory+"_mutau", m_effHistDirectory+"_etau"};
  
  for(const std::string &directory: directories){
    for(std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav){
      Book( TH2F("jet_ak4_"+*flav+"_"+m_workingPoint, "jet_ak4_"+*flav+"_"+m_workingPoint, nPtBins, ptBins, nEtaBins, etaBins), directory.c_str() );
      Book( TH2F("jet_ak4_"+*flav+"_all",             "jet_ak4_"+*flav+"_all",             nPtBins, ptBins, nEtaBins, etaBins), directory.c_str() );
    }
  }
}



void BTaggingScaleTool::fillEfficiencies( const UZH::JetVec& vJets, std::string channel ) {
  
  std::string directory = m_effHistDirectory;
  if(channel!="") directory=directory+"_"+channel;
  
  for(std::vector< UZH::Jet>::const_iterator itJet = vJets.begin(); itJet < vJets.end(); ++itJet){
    // m_logger << DEBUG << "Looking at jet " << itJet - vJets.begin()
    //      << ", pT=" << (*itJet).pt() << ", eta=" << (*itJet).eta()
    //      << SLogger::endmsg;
    TString flavourString = flavourToString(itJet->hadronFlavour());
    if(isTagged(*itJet)){
      Hist("jet_ak4_"+flavourString+"_"+m_workingPoint, directory.c_str())->Fill(itJet->pt(), itJet->eta());
    }
    Hist(  "jet_ak4_"+flavourString+"_all",             directory.c_str())->Fill(itJet->pt(), itJet->eta());
  }
  
}



void BTaggingScaleTool::readEfficiencies() {
  
  m_logger << INFO << "Reading in b-tagging efficiencies from file " << m_effFile << SLogger::endmsg;
  auto inFile = TFile::Open(m_effFile.c_str());
  
  for (std::vector<TString>::const_iterator flav = m_flavours.begin(); flav != m_flavours.end(); ++flav) {
    auto hPass =   (TH2F*) inFile->Get(  m_effHistDirectory + "/" + "jet_ak4_" + *flav + "_" + m_workingPoint);
    auto hAll  =   (TH2F*) inFile->Get(  m_effHistDirectory + "/" + "jet_ak4_" + *flav + "_all");
    TH2F hEff  = *((TH2F*) hPass->Clone( m_effHistDirectory + "_jet_ak4_" + *flav + "_" + m_workingPoint ));
    hEff.Divide(hAll);
    m_effMaps[( "jet_ak4_" + *flav + "_" + m_workingPoint).Data()] = hEff;
    m_logger << DEBUG << "effi TH2D binsx: " << hEff.GetNbinsX() << " binsy: " << hEff.GetNbinsY() << SLogger::endmsg;
  }
  
  inFile->Close();


}



double BTaggingScaleTool::getEfficiency( const double& pt, const double& eta, const int& flavour, const TString& jetCategory ) {
  double eff = 1.;
  
  TH2F thisHist = m_effMaps[("jet_ak4_" + flavourToString(flavour) + "_" + m_workingPoint).Data()];
  m_logger << DEBUG << /*thisHist << " " << */ thisHist.GetName() << SLogger::endmsg;
  int binx = thisHist.GetXaxis()->FindBin(pt);
  if( pt >   thisHist.GetXaxis()->GetBinLowEdge(thisHist.GetNbinsX()+1)) binx = thisHist.GetNbinsX(); // added by Izaak
  int biny = thisHist.GetYaxis()->FindBin(eta);
  m_logger << DEBUG << "binx = " << binx << " biny = " << biny << SLogger::endmsg;
  m_logger << DEBUG << "maxx = " << thisHist.GetNbinsX() << " maxy = " << thisHist.GetNbinsY() << SLogger::endmsg;
  // implement check for overflow
  eff = thisHist.GetBinContent(binx, biny);
  m_logger << DEBUG << "For "<< jetCategory << " with pt = " << pt << ", eta = " << eta << ", flavour = " << flavour << " returning efficiency =" << eff << SLogger::endmsg;
 
  return eff;
  
}



double BTaggingScaleTool::getEfficiency( const UZH::Jet& jet, const TString& jetCategory ) {
  // https://twiki.cern.ch/twiki/bin/view/CMS/HiggsToTauTauWorking2016#B_tag_scale_factors
  
  // TODO test eta with / without fabs
  return getEfficiency(jet.pt(),jet.eta(),jet.hadronFlavour(),jetCategory);
}



TString BTaggingScaleTool::flavourToString( const int& flavour ) {
  
  TString flavourString = "udsg";
  
  if (flavour == 5) flavourString = "b";
  else if (flavour == 4) flavourString = "c";
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
