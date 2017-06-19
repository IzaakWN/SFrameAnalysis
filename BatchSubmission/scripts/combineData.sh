#! /bin/bash

BASEDIR="/scratch/ineuteli/SFrameAnalysis/AnalysisOutput/"
VETO="_24"
LABEL="_Moriond" #"_ICHEP"
FINAL_LABEL="${LABEL}"

DATA_SET="MuEle"
[[ $1 == *m* ]] && DATA_SET="Mu"
[[ $1 == *e* ]] && DATA_SET="Ele"

echo
echo ">>> working in ${BASEDIR}"
cd ${BASEDIR}

echo
[[ $DATA_SET == *Mu* ]] && echo ">>> hadd SingleMuon" &&
ls -lt SingleMuon/*_?_*${LABEL}.root && echo &&
hadd -f SingleMuon/TauTauAnalysis.SingleMuon_Run2016${FINAL_LABEL}.root SingleMuon/TauTauAnalysis.SingleMuon_?_Run2016${LABEL}.root ||
echo ">>> Warning! Could not find SingleMuon root files!"
echo
[[ $DATA_SET == *Ele* ]] && echo ">>> hadd SingleElectron" &&
ls -lt SingleElectron/*_?_*${LABEL}.root && echo &&
hadd -f SingleElectron/TauTauAnalysis.SingleElectron_Run2016${FINAL_LABEL}.root SingleElectron/TauTauAnalysis.SingleElectron_?_Run2016${LABEL}.root ||
echo ">>> Warning! Could not find SingleElectron root files!"
echo

