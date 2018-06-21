#! /bin/bash

function peval { echo -e ">>> $(tput setab 0)$(tput setaf 7)$@$(tput sgr0)"; eval "$@"; }

if [[ $1 == 1 ]]; then
  echo ">>> ST, DY, VV"
  peval "python -u submitSFrame.py -j Background_DY.py --nosandbox --useEnv | tee nohup/nohup_DY.log"
  peval "python -u submitSFrame.py -j Background_ST.py --nosandbox --useEnv | tee nohup/nohup_ST.log"
  peval "python -u submitSFrame.py -j Background_WW.py --nosandbox --useEnv | tee nohup/nohup_WW.log"
  peval "python -u submitSFrame.py -j Background_WZ.py --nosandbox --useEnv | tee nohup/nohup_WZ.log"
  peval "python -u submitSFrame.py -j Background_ZZ.py --nosandbox --useEnv | tee nohup/nohup_ZZ.log"
elif [[ $1 == 2 || $1 == 3 ]]; then
  echo ">>> TT, WJ, data"
  peval "python -u submitSFrame.py -j Background_TT.py --nosandbox --useEnv | tee nohup/nohup_TT.log"
  if [[ $1 == 3 ]]; then
    echo ">>> data single muon and electron"
    peval "python -u submitSFrame.py -j Data_Mu.py   --nosandbox --useEnv | tee nohup/nohup_Mu.log"
  fi
  peval "python -u submitSFrame.py -j Background_WJ.py --nosandbox --useEnv | tee nohup/nohup_WJ.log" # mostly fakes
else
    echo ">>> Wrong input! Please specify 1-3."
fi
