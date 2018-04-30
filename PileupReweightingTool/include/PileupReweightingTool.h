#ifndef PileupReweightingTool_h
#define PileupReweightingTool_h

#include "TROOT.h"
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
// SFrame include(s):
#include "core/include/SError.h"
#include "plug-ins/include/SToolBase.h"

//#include "PUWeight.h"

//namespace Root{
//  class TPileupReweighting;
//}

class PileupReweightingTool : public SToolBase {

    public:
        /// constructor
        PileupReweightingTool( SCycleBase* parent, const char* name = "PileupReweightingTool" );
        ~PileupReweightingTool() { };
        
        void BeginInputData( const SInputData& id, std::string dataFileName="$SFRAME_DIR/../PileupReweightingTool/histograms/Data_PileUp_2017_69p2.root", std::string tag="" ) throw( SError );
        void drawPUWeight();
        double getPileUpWeight(const int npu, const int sigma=0);
        //double getPileUpWeight80p0(const int npu, const int sigma=0);


    private:
        std::string m_name;         ///< name of the tool
        //PUWeight m_puWeight;      ///< instance of PUWeight class

        // tool properties
        std::string m_MCRootFileName;
        std::string m_MCRootHistName;
        std::string m_DataRootFileName;
        std::string m_DataRootHistName;
        //std::string m_DataRootFileName80p0;
        //std::string m_DataRootHistName80p0;
        std::string m_DataRootFileNameUp;
        std::string m_DataRootHistNameUp;
        std::string m_DataRootFileNameDown;
        std::string m_DataRootHistNameDown;
        //TFile* MCRootFile;
        //TFile* DataRootFile;
        //TFile* DataRootFile80p0;
        //TFile* DataRootFileUp;
        //TFile* DataRootFileDown;
        TH1F* m_MCRootHist;
        TH1F* m_DataRootHist;
        //TH1F* m_DataRootHist80p0;
        TH1F* m_DataRootHistUp;
        TH1F* m_DataRootHistDown;
        
};


#endif //  __PILEUPREWEIGHTINGTTOOL_H__
