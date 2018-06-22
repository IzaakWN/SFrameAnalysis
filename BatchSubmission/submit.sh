#! /bin/bash

function peval { echo ">>> $@"; eval "$@"; }

if [[ $1 == 1 ]]; then
    echo ">>> DY, ST, LowMass"
    peval "python -u submitSFrame.py -j Background_DY.py --nosandbox --useEnv | tee nohup/nohup_DY.log"
    peval "python -u submitSFrame.py -j Background_ST.py --nosandbox --useEnv | tee nohup/nohup_ST.log"
    peval "python -u submitSFrame.py -j Background_WW.py --nosandbox --useEnv | tee nohup/nohup_WW.log"
    peval "python -u submitSFrame.py -j Background_WZ.py --nosandbox --useEnv | tee nohup/nohup_WZ.log"
    #peval "python -u submitSFrame.py -j Signal_LowMass.py --nosandbox --useEnv | tee nohup/nohup_LowMass.log"
elif [[ $1 == 2 || $1 == 3 ]]; then
    echo ">>> TT, WJ, SUSY"
    peval "python -u submitSFrame.py -j Background_TT.py --nosandbox --useEnv | tee nohup/nohup_TT.log"
    peval "python -u submitSFrame.py -j Background_WJ.py --nosandbox --useEnv | tee nohup/nohup_WJ.log"
    peval "python -u submitSFrame.py -j Background_ZZ.py --nosandbox --useEnv | tee nohup/nohup_ZZ.log"
    peval "python -u submitSFrame.py -j Background_VV.py --nosandbox --useEnv | tee nohup/nohup_VV.log"
    #peval "python -u submitSFrame.py -j Signal_SUSY.py --nosandbox --useEnv | tee nohup/nohup_SUSY.log"
    if [[ $1 == 3 ]]; then
        echo ">>> data single muon and electron"
        peval "python -u submitSFrame.py -j Data_Mu.py   --nosandbox --useEnv | tee nohup/nohup_Mu.log"
        peval "python -u submitSFrame.py -j Data_Ele.py  --nosandbox --useEnv | tee nohup/nohup_Ele.log"
        #/scratch/ineuteli/SFrameAnalysis/AnalysisOutput/combineData.sh
    fi
else
    echo ">>> Wrong input! Use 1-3."
fi
