#ifndef JetCorrectionTool_h
#define JetCorrectionTool_h

#include "TROOT.h"
#include "TFile.h"
#include "TH1.h"
#include "TH2.h"
#include "TF1.h"
#include "TGraph.h"
#include "TAxis.h"
#include "TGraphAsymmErrors.h"
#include "TRandom3.h"
#include "TLorentzVector.h"
#include <iostream>
#include <map>
#include <vector>
#include <cmath>
#include <string>

// SFrame include(s):
#include "core/include/SError.h"
#include "plug-ins/include/SToolBase.h"

#include "../interface/EnergyScaleCorrection_class.h"
#include "../NtupleVariables/include/JetNtupleObject.h"
#include "../NtupleVariables/include/Jet.h"
#include "../NtupleVariables/include/GenJetak4.h"
#include "../NtupleVariables/include/GenJetak4NtupleObject.h"



namespace UZH {
  class Jet;
  //class GenJetak4
}



class JetCorrectionTool  : public SToolBase   {

    private:
        std::string m_name;
        
        TGraph* MassGenBarrel;
        TGraph* MassGenEndcap;
        TGraph* MassRecoBarrel;
        TGraph* MassRecoEndcap;
        TF1* MassResBarrel;
        TF1* MassResEndcap;


    public:

        JetCorrectionTool( SCycleBase* parent, const char* name = "JetCorrectionTool" );
        ~JetCorrectionTool(); 
        
        void BeginInputData( const SInputData& id ) throw( SError ); //const Ntuple::GenJetak4NtupleObject& m_genJetAK4
        
        double GetCorrectedEnergy(double, bool, int, bool, double, double, double);
        double GetCorrectedMass(double, double, double, bool, int=0, int=0);
        TLorentzVector GetCorrectedJet(TLorentzVector, float, float, float, int=0, int=0, bool is_ak8=false);
        std::vector<TLorentzVector> GetCorrectedJet(const UZH::Jet& jet, int sigmaRes=0, bool is_ak8=false);
        TLorentzVector GetCorrectedJetJER(TLorentzVector jet,TLorentzVector genJet, float jer, float jerUp, float jerDown, 
                                          int sigmaRes=0, bool isGenJetMatched=false, double random=0);
        TLorentzVector GetCorrectedJetJER(const UZH::Jet& jet, const Ntuple::GenJetak4NtupleObject& m_genJetAK4);
        std::vector<TLorentzVector> GetCorrectedJetJERShifted(const UZH::Jet& jet, const Ntuple::GenJetak4NtupleObject& m_genjetAK4);
        
        EnergyScaleCorrection_class* eScaler;
        TRandom3* trandom;
        
        std::string m_CorrectionFileName;
        std::string m_JetResFileName;
        std::string m_JetResFileNameAK4;
        std::string m_MassGenFileName, m_MassGenBarrelHistName, m_MassGenEndcapHistName, m_MassRecoFileName, m_MassRecoBarrelHistName, m_MassRecoEndcapHistName, m_MassResFileName, m_MassResBarrelHistName, m_MassResEndcapHistName;
        
        std::vector<float*> JetRes;
        std::vector<float*> JetResAK4;
        
};


#endif //  Correction_h


