#! /bin/bash

if [[ $1 == 1 ]]; then
  echo ">>> ST, DY, VV"
  python -u submitSFrame.py -j Background_ST.py --nosandbox --useEnv | tee nohup/nohup_ST.log
  python -u submitSFrame.py -j Background_DY.py --nosandbox --useEnv | tee nohup/nohup_DY.log
  python -u submitSFrame.py -j Background_WW.py --nosandbox --useEnv | tee nohup/nohup_WW.log
  python -u submitSFrame.py -j Background_WZ.py --nosandbox --useEnv | tee nohup/nohup_WZ.log
  python -u submitSFrame.py -j Background_ZZ.py --nosandbox --useEnv | tee nohup/nohup_ZZ.log
elif [[ $1 == 2 || $1 == 3 ]]; then
  echo ">>> TT, WJ"
  python -u submitSFrame.py -j Background_TT.py --nosandbox --useEnv | tee nohup/nohup_TT.log
  if [[ $1 == 3 ]]; then
    echo ">>> data single muon and electron"
    python -u submitSFrame.py -j Data_Mu.py   --nosandbox --useEnv | tee nohup/nohup_Mu.log
  fi
  python -u submitSFrame.py -j Background_WJ.py --nosandbox --useEnv | tee nohup/nohup_WJ.log
else
    echo ">>> Wrong input! Use 1-3."
fi
