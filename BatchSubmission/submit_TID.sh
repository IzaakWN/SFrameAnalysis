#! /bin/bash

function peval { echo -e ">>> $(tput setab 0)$(tput setaf 7)$@$(tput sgr0)"; eval "$@"; }

if [[ $1 == 1 ]]; then
  echo ">>> shift Down"
  peval "python -u submitSFrame.py -j TES/Background_TT_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p90.log"
  peval "python -u submitSFrame.py -j TES/Background_ST_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF0p90.log"
  peval "python -u submitSFrame.py -j TES/Background_WJ_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_WJ_JTF0p90.log"
  peval "python -u submitSFrame.py -j TES/Background_DY_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_DY_JTF0p90.log"
  peval "python -u submitSFrame.py -j TES/Background_TT_TES0p97.py --nosandbox --useEnv | tee nohup/nohup_TT_TES0p97.log"
  peval "python -u submitSFrame.py -j TES/Background_ST_TES0p97.py --nosandbox --useEnv | tee nohup/nohup_ST_TES0p97.log"
  peval "python -u submitSFrame.py -j TES/Background_DY_TES0p97.py --nosandbox --useEnv | tee nohup/nohup_DY_TES0p97.log"
elif [[ $1 == 2 ]]; then
  echo ">>> shift up"
  peval "python -u submitSFrame.py -j TES/Background_TT_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF1p10.log"
  peval "python -u submitSFrame.py -j TES/Background_ST_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p10.log"
  peval "python -u submitSFrame.py -j TES/Background_WJ_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_WJ_JTF1p10.log"
  peval "python -u submitSFrame.py -j TES/Background_DY_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_DY_JTF1p10.log"
  peval "python -u submitSFrame.py -j TES/Background_TT_TES1p03.py --nosandbox --useEnv | tee nohup/nohup_TT_TES1p03.log"
  peval "python -u submitSFrame.py -j TES/Background_ST_TES1p03.py --nosandbox --useEnv | tee nohup/nohup_ST_TES1p03.log"
  peval "python -u submitSFrame.py -j TES/Background_DY_TES1p03.py --nosandbox --useEnv | tee nohup/nohup_DY_TES1p03.log"
else
  echo ">>> Wrong input! Use 1-2."
fi
