#ifndef ScaleFactorTool_h
#define ScaleFactorTool_h

#include "../interface/ScaleFactor.h"
#include "../interface/ScaleFactorTau.h"
#include "TROOT.h"
#include "TFile.h"
#include <iostream>
#include <map>
#include <cmath>
#include <string>

// SFrame include(s):
#include "core/include/SError.h"
#include "plug-ins/include/SToolBase.h"




class ScaleFactorTool : public SToolBase {
  
  
  
  public:
    
    ScaleFactorTool( SCycleBase* parent, const char* name = "ScaleFactorTool" );
    ~ScaleFactorTool();
    void BeginInputData( const SInputData& id ) throw( SError );
    
    // MUON
    double get_Efficiency_MuTauTrig_MC(   double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="mt" );
    double get_Efficiency_MuTauTrig_Data( double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="mt" );
    double get_ScaleFactor_MuTauTrig(     double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="mt" );
    double get_ScaleFactor_Mu22Trig(      double pt1, double eta1 );
    double get_ScaleFactor_MuIdIso(       double pt,  double eta  );
    std::string m_File_Mu22Trig;
    std::string m_File_Mu24Trig;
    std::string m_File_MuTauTrig_MuLeg;
    std::string m_File_MuTauTrig_TauLeg;
    std::string m_File_MuIdIso;
    
    // ELECTRON
    double get_Efficiency_EleTauTrig_MC(   double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="et" );
    double get_Efficiency_EleTauTrig_Data( double pt1, double eta1, double pt2, double eta2, int dm, bool isRealTau,   std::string triggerFlags="et" );
    double get_ScaleFactor_EleTauTrig(     double pt1, double eta1, double pt2, double eta2, int dm, int genmatch_2=5, std::string triggerFlags="et" );
    double get_ScaleFactor_EleTrig(        double pt1, double eta1 );
    double get_ScaleFactor_EleIdIso(       double pt,  double eta  );
    std::string m_File_EleTrig;
    std::string m_File_EleTauTrig_EleLeg;
    std::string m_File_EleTauTrig_TauLeg;
    std::string m_File_EleIdIso;
    
    // EMU
    double get_Efficiency_EleMuTrig_MC(      double pt1, double eta1, double pt2, double eta2, std::string triggerFlags="em" );
    double get_Efficiency_EleMuTrig_Data(    double pt1, double eta1, double pt2, double eta2, std::string triggerFlags="em" );
    double get_ScaleFactor_EleMuTrig(        double pt1, double eta1, double pt2, double eta2, std::string triggerFlags="em" );
    double get_Efficiency_EleMuTrig_OR_MC(   double pt1, double eta1, double pt2, double eta2 );
    double get_Efficiency_EleMuTrig_OR_Data( double pt1, double eta1, double pt2, double eta2 );
    double get_ScaleFactor_EleMuTrig_OR(     double pt1, double eta1, double pt2, double eta2 );
    std::string m_File_EleMuTrig_Ele12Leg;
    std::string m_File_EleMuTrig_Ele23Leg;
    std::string m_File_EleMuTrig_Mu8Leg;
    std::string m_File_EleMuTrig_Mu23Leg;
    
    bool verbose = true;
    
    
    
  private:
    
    std::string m_name;
    ScaleFactor* m_ScaleFactor_Mu22Trig;
    ScaleFactor* m_ScaleFactor_Mu24Trig;
    ScaleFactor* m_ScaleFactor_MuTauTrig_MuLeg;
    ScaleFactorTau* m_ScaleFactor_MuTauTrig_TauLeg;
    ScaleFactor* m_ScaleFactor_MuIdIso;
    ScaleFactor* m_ScaleFactor_EleTrig;
    ScaleFactor* m_ScaleFactor_EleTauTrig_EleLeg;
    ScaleFactorTau* m_ScaleFactor_EleTauTrig_TauLeg;
    ScaleFactor* m_ScaleFactor_EleMuTrig_Ele12Leg;
    ScaleFactor* m_ScaleFactor_EleMuTrig_Ele23Leg;
    ScaleFactor* m_ScaleFactor_EleMuTrig_Mu8Leg;
    ScaleFactor* m_ScaleFactor_EleMuTrig_Mu23Leg;
    ScaleFactor* m_ScaleFactor_EleIdIso;
    
    
    
};


#endif // ScaleFactorTool_h
