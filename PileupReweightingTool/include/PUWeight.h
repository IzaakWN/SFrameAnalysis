#ifndef PUWeight_H
#define PUWeight_H

#include <string>
#include <vector>

#include "TH1.h"
#include "TString.h"

// Compute pile-up weights to match data distribution
class PUWeight {
public:
  enum Scenario { Winter17_25ns, Winter15_25ns, Moriond17_25ns };

  static Scenario toScenario(const std::string& str);
  static std::string toString(const Scenario sc);

  // Constructor. Initializes default behaviour to return PU weight of 1
  PUWeight();

  // Initialise weights for a given MC pile-up scenario. Can only be
  // called once.
  void initPUWeights(const std::string& dataRootFileName, const std::string& dataRootHistName, const std::string& mcScenario);

  // Get weight factor dependent on number of added PU interactions
  // nPU is the 'true' number of interactions as explained in
  // https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJSONFileforData#2012_Pileup_JSON_Files
  double getPUWeight(const int nPU) const;


private:
  bool isInit_;
  int nPUMax_;
  std::vector<double> puWeigths_;

  // Generate weights for given data PU distribution
  std::vector<double> generateWeights(const Scenario sc, const TH1* data_npu_estimated) const;
};

#endif //PUWeight_H
