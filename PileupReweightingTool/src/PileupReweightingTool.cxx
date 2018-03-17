#include "../include/PileupReweightingTool.h"
#include <iostream>

PileupReweightingTool::PileupReweightingTool( SCycleBase* parent, const char* name ) : SToolBase( parent ), m_name( name ) { //, m_puWeight()
  SetLogName( name ); 
}



// initialize before event loop
void PileupReweightingTool::BeginInputData( const SInputData& ) throw( SError ) {
  
  DeclareProperty( m_name + "_MCRootFileName",       m_MCRootFileName       = "$SFRAME_DIR/../PileupReweightingTool/histograms/MC_PileUp_Winter17_PU25ns_V2_fromMC.root" );
  DeclareProperty( m_name + "_m_MCRootHistName",     m_MCRootHistName       = "pileup" );
  DeclareProperty( m_name + "_DataRootFileName",     m_DataRootFileName     = "$SFRAME_DIR/../PileupReweightingTool/histograms/Data_PileUp_2017_69p2.root" );
  DeclareProperty( m_name + "_DataRootFileName80p0", m_DataRootFileName80p0 = "$SFRAME_DIR/../PileupReweightingTool/histograms/Data_PileUp_2017_80p0.root" );
  DeclareProperty( m_name + "_m_DataRootHistName",   m_DataRootHistName     = "pileup" );
  //DeclareProperty( m_name + "_DataRootFileNameUp", m_DataRootFileNameUp = "$SFRAME_DIR/../PileupReweightingTool/histograms/Moriond17_72383.root" );
  //DeclareProperty( m_name + "_m_DataRootHistNameUp", m_DataRootHistNameUp = "pileup" );
  //DeclareProperty( m_name + "_DataRootFileNameDown", m_DataRootFileNameDown = "$SFRAME_DIR/../PileupReweightingTool/histograms/Moriond17_66156.root" );
  //DeclareProperty( m_name + "_m_DataRootHistNameDown", m_DataRootHistNameDown = "pileup" );
  
  m_logger << INFO << "MCRootFileName:        " << m_MCRootFileName       << SLogger::endmsg;
  m_logger << INFO << "MCRootHistName:        " << m_MCRootHistName       << SLogger::endmsg;
  m_logger << INFO << "DataRootFileName:      " << m_DataRootFileName     << SLogger::endmsg;
  m_logger << INFO << "DataRootHistName:      " << m_DataRootHistName     << SLogger::endmsg;
  m_logger << INFO << "DataRootFileName80p0:  " << m_DataRootFileName80p0 << SLogger::endmsg;
  m_logger << INFO << "DataRootHistName80p0:  " << m_DataRootHistName     << SLogger::endmsg;
  //m_logger << INFO << "DataRootFileNameUp:    " << m_DataRootFileNameUp << SLogger::endmsg;
  //m_logger << INFO << "m_DataRootHistNameUp:    " << m_DataRootHistNameUp << SLogger::endmsg;
  //m_logger << INFO << "DataRootFileNameDown:  " << m_DataRootFileNameDown << SLogger::endmsg;
  //m_logger << INFO << "m_DataRootHistNameDown:  " << m_DataRootHistNameDown << SLogger::endmsg;
  
  TFile* MCRootFile = new TFile(m_MCRootFileName.c_str(), "READ");
  if(MCRootFile) {
      m_MCRootHist = (TH1F*)MCRootFile->Get(m_MCRootHistName.c_str());
      if(m_MCRootHist) m_MCRootHist->SetDirectory(0);
      else m_logger << WARNING << "‎Hist " << m_MCRootHistName << " does not exist. Please check." << SLogger::endmsg;
      MCRootFile->Close();
  }
  else m_logger << WARNING << "‎File " << m_MCRootFileName << " does not exist. Please check." << SLogger::endmsg;
  
  TFile* DataRootFile = new TFile(m_DataRootFileName.c_str(), "READ");
  if(DataRootFile) {
      m_DataRootHist = (TH1F*)DataRootFile->Get(m_DataRootHistName.c_str());
      if(m_DataRootHist) m_DataRootHist->SetDirectory(0);
      else m_logger << WARNING << "‎Hist " << m_DataRootHistName << " does not exist. Please check." << SLogger::endmsg;
      DataRootFile->Close();
  }
  else m_logger << WARNING << "‎File " << m_DataRootFileName << " does not exist. Please check." << SLogger::endmsg;
  
  TFile* DataRootFile80p0 = new TFile(m_DataRootFileName.c_str(), "READ");
  if(DataRootFile80p0) {
      m_DataRootHist80p0 = (TH1F*)DataRootFile80p0->Get(m_DataRootHistName.c_str());
      if(m_DataRootHist) m_DataRootHist80p0->SetDirectory(0);
      else m_logger << WARNING << "‎Hist " << m_DataRootHistName << " does not exist. Please check." << SLogger::endmsg;
      DataRootFile80p0->Close();
  }
  else m_logger << WARNING << "‎File " << m_DataRootFileName << " does not exist. Please check." << SLogger::endmsg;
  
  // DataRootFileUp = new TFile(m_DataRootFileNameUp.c_str(), "READ");
  // if(DataRootFileUp) {
  //     m_DataRootHistUp = (TH1F*)DataRootFileUp->Get(m_DataRootHistNameUp.c_str());
  //     if(m_DataRootHistUp) m_DataRootHistUp->SetDirectory(0);
  //     else m_logger << WARNING << "‎Hist " << m_DataRootHistNameUp << " does not exist. Please check." << SLogger::endmsg;
  //     DataRootFileUp->Close();
  // }
  // else m_logger << WARNING << "‎File " << m_DataRootFileNameUp << " does not exist. Please check." << SLogger::endmsg;
  // 
  // DataRootFileDown = new TFile(m_DataRootFileNameDown.c_str(), "READ");
  // if(DataRootFileDown) {
  //     m_DataRootHistDown = (TH1F*)DataRootFileDown->Get(m_DataRootHistNameDown.c_str());
  //     if(m_DataRootHistDown) m_DataRootHistDown->SetDirectory(0);
  //     else m_logger << WARNING << "‎Hist " << m_DataRootHistNameDown << " does not exist. Please check." << SLogger::endmsg;
  //     DataRootFileDown->Close();
  // }
  // else m_logger << WARNING << "‎File " << m_DataRootFileNameDown << " does not exist. Please check." << SLogger::endmsg;
  
  // Normalize to unity
  m_MCRootHist->Scale(1./m_MCRootHist->Integral());
  m_DataRootHist->Scale(1./m_DataRootHist->Integral());
  m_DataRootHist80p0->Scale(1./m_DataRootHist80p0->Integral());
  //m_DataRootHistUp->Scale(1./m_DataRootHistUp->Integral());
  //m_DataRootHistDown->Scale(1./m_DataRootHistDown->Integral());
  
  if(m_MCRootHist->GetNbinsX() != m_DataRootHist->GetNbinsX()) m_logger << WARNING << "Pileup histograms binning is different" << SLogger::endmsg;
  if(m_MCRootHist->GetNbinsX() != m_DataRootHist80p0->GetNbinsX()) m_logger << WARNING << "Pileup histograms binning is different" << SLogger::endmsg;
  m_logger << INFO << "Pileup weights initialised" << SLogger::endmsg;
  
  return;
}



void PileupReweightingTool::drawPUWeight(){
  
  int nBinsD  = m_DataRootHist->GetXaxis()->GetNbins();
  int xminD   = m_DataRootHist->GetXaxis()->GetXmin();
  int xmaxD   = m_DataRootHist->GetXaxis()->GetXmax();
  int nBinsMC = m_MCRootHist->GetXaxis()->GetNbins();
  int xminMC  = m_MCRootHist->GetXaxis()->GetXmin();
  int xmaxMC  = m_MCRootHist->GetXaxis()->GetXmax();
  
  std::cout << ">>> PileupReweightingTool::drawPUWeight check" << std::endl;
  std::cout << ">>> m_DataRootHist has "<<nBinsD<<" bins between ["<<xminD<<","<<xmaxD<<"]." << std::endl;
  std::cout << ">>> m_MCRootHist   has "<<nBinsMC<<" bins between ["<<xminMC<<","<<xmaxMC<<"]." << std::endl;
  
  TH1F* puweightHist = new TH1F("puweight","puweight",100,0,100);
  
  for(int npu=0; npu<101; npu++){
    float puweight = getPileUpWeight(npu);
    int binD   = m_DataRootHist->FindBin(npu);
    int binMC  = m_MCRootHist->FindBin(npu);
    float data = m_DataRootHist->GetBinContent(binD);
    float mc   = m_MCRootHist->GetBinContent(binMC);
    std::cout << ">>> npu ="<<std::setw(4)<<npu<<" gets puweight = data / mc = "
              <<std::setw(10)<<data<<" / "<<std::setw(10)<<mc<<" = "<<std::setw(10)<<data/mc
              << "  (binD,binMC) = ("<<std::setw(3)<<binD<<","<<std::setw(3)<<binMC<<")" << std::endl;
    puweightHist->SetBinContent(npu,puweight);
  }
  
  TCanvas canvas("canvas","canvas",0,0,800,600);
  //m_DataRootHist->SetLineColor(1);
  //m_DataRootHist->SetLineWidth(2);
  //m_MCRootHist->SetLineColor(2);
  //m_MCRootHist->SetLineWidth(2);
  puweightHist->SetLineColor(4);
  puweightHist->SetLineWidth(4);
  //m_DataRootHist->Draw("")
  //m_MCRootHist->Draw("SAME")
  puweightHist->Draw(""); //"SAME AXIS")
  canvas.SaveAs("puweight.png");
  
}



double PileupReweightingTool::getPileUpWeight(const int npu, const int sigma){
  //double weight = m_puWeight.getPUWeight( mu );
  float data(1.), mc(0.);
  //if(sigma==+1) data = m_DataRootHistUp->GetBinContent(m_DataRootHistUp->FindBin(npu));
  //else if(sigma==-1) data = m_DataRootHistDown->GetBinContent(m_DataRootHistDown->FindBin(npu));
  data = m_DataRootHist->GetBinContent(m_DataRootHist->FindBin(npu));
  mc   = m_MCRootHist->GetBinContent(m_MCRootHist->FindBin(npu));
  
  if(mc > 0.){
    //std::cout << ">>> npu="<<npu<<" has data / mc = "<<data<<" / "<<mc<<" = "<<data/mc << "  (binD,binMC) = ("<<m_DataRootHist->FindBin(npu)<<","<<m_MCRootHist->FindBin(npu)<<")" << std::endl;
    return data / mc;
  }
  m_logger << WARNING << "Non-defined Pileup Weight: " << mc << SLogger::endmsg;
  return 1;
}



double PileupReweightingTool::getPileUpWeight80p0(const int npu, const int sigma){
  float data(1.), mc(0.);
  data = m_DataRootHist80p0->GetBinContent(m_DataRootHist80p0->FindBin(npu));
  mc   = m_MCRootHist->GetBinContent(m_MCRootHist->FindBin(npu));
  
  if(mc > 0.)
    return data / mc;
  
  m_logger << WARNING << "Non-defined Pileup Weight: npu = " << npu << ", data = " << data << ", mc = " << mc << SLogger::endmsg;
  return 1;
}


