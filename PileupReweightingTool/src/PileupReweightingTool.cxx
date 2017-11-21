#include "../include/PileupReweightingTool.h"
#include <iostream>
//
// constructor
//
PileupReweightingTool::PileupReweightingTool( SCycleBase* parent, const char* name ) : 
  SToolBase( parent ), m_name( name ), m_puWeight() {

  SetLogName( name );
  
  DeclareProperty( m_name + "_HistoPath",        m_histoPath = "$SFRAME_DIR/../PileupReweightingTool/histograms/" );
  DeclareProperty( m_name + "_DataRootFileName", m_dataRootFileName = "Data_Pileup_2016_271036-284044_80bins.root" );
  DeclareProperty( m_name + "_DataRootHistName", m_dataRootHistName = "pileup" );
  DeclareProperty( m_name + "_MCScenario",       m_mcScenario = "Winter17_25ns" );

}

// destructor
PileupReweightingTool::~PileupReweightingTool(){}


// initialize before event loop
void PileupReweightingTool::BeginInputData( const SInputData& ) throw( SError ) {

  m_logger << INFO << SLogger::endmsg;
  m_logger << INFO << "HistoPath:           " << m_histoPath << SLogger::endmsg;
  m_logger << INFO << "DataRootFileName:    " << m_dataRootFileName << SLogger::endmsg;
  m_logger << INFO << "DataRootHistName:    " << m_dataRootHistName << SLogger::endmsg;
  m_logger << INFO << "MCScenario:          " << m_mcScenario << SLogger::endmsg;
  
  m_puWeight.initPUWeights(m_histoPath+"/"+m_dataRootFileName, m_dataRootHistName, m_mcScenario);
  m_logger << INFO << "Pileup weights initialised" << SLogger::endmsg;
   
  return;
}

// get the weight
double PileupReweightingTool::getPileUpweight(float  mu ){
  return weight = m_puWeight.getPUWeight( mu );
  return weight;
}
