#ifndef ScaleFactorTool_h
#define ScaleFactorTool_h

#include <cstdlib>
#include <limits>
#include <iostream>
#include <map>
#include <cmath>
#include <string>
#include "../interface/ScaleFactor.h"
#include "../interface/ScaleFactorJSON.h"
#include "../interface/ScaleFactorTau.h"
#include "TROOT.h"
#include "TFile.h"

// SFrame include(s):
#include "core/include/SError.h"
#include "plug-ins/include/SToolBase.h"




class ScaleFactorTool : public SToolBase {
  
  
  
  public:
    
    ScaleFactorTool( SCycleBase* parent, const char* name = "ScaleFactorTool" );
    ~ScaleFactorTool();
    void BeginInputData( const SInputData& id ) throw( SError );
    
    // MUON
    float get_ScaleFactor_Mu27Trig( double pt, double eta );
    float get_ScaleFactor_MuIdIso(  double pt, double eta );
    float get_ScaleFactor_MuId(     double pt, double eta );
    float get_ScaleFactor_MuIso(    double pt, double eta );
    std::string m_File_Mu27Trig;
    std::string m_Hist_Mu27Trig;
    //float get_Efficiency_MuTauTrig_MC(   double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="mt" );
    //float get_Efficiency_MuTauTrig_Data( double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="mt" );
    //float get_ScaleFactor_MuTauTrig(     double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="mt" );
    //float get_ScaleFactor_MuTauTrig_OR(  double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="mt" );
    //float get_ScaleFactor_Mu22Trig(      double pt1, double eta1 );
    //float get_ScaleFactor_MuIdIso(       double pt1, double eta1 );
    //std::string m_File_Mu22Trig;
    //std::string m_File_Mu24Trig;
    //std::string m_File_MuTauTrig_MuLeg;
    //std::string m_File_MuTauTrig_TauLeg;
    //std::string m_File_MuIdIso;
    std::string m_File_MuId;
    std::string m_File_MuIso;
    std::string m_WP_MuId;
    std::string m_WP_MuIso;
    
    // ELECTRON
    //float get_Efficiency_EleTauTrig_MC(   double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="et" );
    //float get_Efficiency_EleTauTrig_Data( double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="et" );
    //float get_ScaleFactor_EleTauTrig(     double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="et" );
    //float get_ScaleFactor_EleTauTrig_OR(  double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="et" );
    //float get_ScaleFactor_EleTrig(        double pt, double eta );
    float get_ScaleFactor_EleId(          double pt, double eta );
    float get_ScaleFactor_EleIdIso(       double pt, double eta );
    //std::string m_File_EleTrig;
    //std::string m_File_EleTauTrig_EleLeg;
    //std::string m_File_EleTauTrig_TauLeg;
    //std::string m_File_EleIdIso;
    std::string m_File_EleId;
    std::string m_File_EleReco;
    std::string m_Hist_EleId;
        
    bool verbose = true;
    
    
    
  private:
    
    std::string m_name;
    ScaleFactor* m_ScaleFactor_Mu27Trig;
    //ScaleFactor* m_ScaleFactor_Mu22Trig;
    //ScaleFactor* m_ScaleFactor_Mu24Trig;
    //ScaleFactor* m_ScaleFactor_MuTauTrig_MuLeg;
    //ScaleFactorTau* m_ScaleFactor_MuTauTrig_TauLeg;
    //ScaleFactorJSON* m_ScaleFactor_MuIdIso;
    ScaleFactorJSON* m_ScaleFactor_MuId;
    ScaleFactorJSON* m_ScaleFactor_MuIso;
    //ScaleFactor* m_ScaleFactor_EleTrig;
    //ScaleFactor* m_ScaleFactor_EleTauTrig_EleLeg;
    //ScaleFactorTau* m_ScaleFactor_EleTauTrig_TauLeg;
    //ScaleFactor* m_ScaleFactor_EleIdIso;
    ScaleFactor* m_ScaleFactor_EleId;
    ScaleFactor* m_ScaleFactor_EleReco;
     
    
};


#endif // ScaleFactorTool_h
