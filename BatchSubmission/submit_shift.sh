#! /bin/bash

function peval { echo -e ">>> $(tput setab 0)$(tput setaf 7)$@$(tput sgr0)"; eval "$@"; }

if [[ $1 == 1 ]]; then
  echo ">>> shift down"
  peval "python -u submitSFrame.py -j shift/Background_DY_TES0p99.py --nosandbox --useEnv | tee nohup/nohup_DY_TES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_TT_TES0p99.py --nosandbox --useEnv | tee nohup/nohup_TT_TES0p99.log"
  #peval "python -u submitSFrame.py -j shift/Background_ST_TES0p99.py --nosandbox --useEnv | tee nohup/nohup_ST_TES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_DY_LTF0p97.py --nosandbox --useEnv | tee nohup/nohup_DY_LTF0p97.log"
  peval "python -u submitSFrame.py -j shift/Signal_LowMass_TES0p99.py --nosandbox --useEnv | tee nohup/nohup_LowMass_TES0p99.log"
  peval "python -u submitSFrame.py -j shift/Signal_SUSY_TES0p99.py   --nosandbox --useEnv | tee nohup/nohup_SUSY_TES0p99.log"
elif [[ $1 == 2 ]]; then
  echo ">>> shift up"
  peval "python -u submitSFrame.py -j shift/Background_DY_TES1p01.py --nosandbox --useEnv | tee nohup/nohup_DY_TES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_TT_TES1p01.py --nosandbox --useEnv | tee nohup/nohup_TT_TES1p01.log"
  #peval "python -u submitSFrame.py -j shift/Background_ST_TES1p01.py --nosandbox --useEnv | tee nohup/nohup_ST_TES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_DY_LTF1p03.py --nosandbox --useEnv | tee nohup/nohup_DY_LTF1p03.log"
  peval "python -u submitSFrame.py -j shift/Signal_LowMass_TES1p01.py --nosandbox --useEnv | tee nohup/nohup_LowMass_TES1p01.log"
  peval "python -u submitSFrame.py -j shift/Signal_SUSY_TES1p01.py   --nosandbox --useEnv | tee nohup/nohup_SUSY_TES1p01.log"
elif [[ $1 == 3 ]]; then
  echo ">>> shift down"
  peval "python -u submitSFrame.py -j shift/Background_DY_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_DY_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_TT_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_TT_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_WJ_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_WJ_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_ST_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_ST_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_VV_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_VV_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_WW_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_WW_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_WZ_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_WZ_EES0p99.log"
  peval "python -u submitSFrame.py -j shift/Background_ZZ_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_ZZ_EES0p99.log"
  #peval "python -u submitSFrame.py -j shift/Signal_LowMass_EES0p99.py --nosandbox --useEnv | tee nohup/nohup_LowMass_EES0p99.log"
  #peval "python -u submitSFrame.py -j shift/Signal_SUSY_EES0p99.py   --nosandbox --useEnv | tee nohup/nohup_SUSY_EES0p99.log"
elif [[ $1 == 4 ]]; then
  echo ">>> shift up"
  peval "python -u submitSFrame.py -j shift/Background_DY_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_DY_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_TT_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_TT_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_WJ_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_WJ_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_ST_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_ST_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_VV_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_VV_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_WW_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_WW_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_WZ_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_WZ_EES1p01.log"
  peval "python -u submitSFrame.py -j shift/Background_ZZ_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_ZZ_EES1p01.log"
  #peval "python -u submitSFrame.py -j shift/Signal_LowMass_EES1p01.py --nosandbox --useEnv | tee nohup/nohup_LowMass_EES1p01.log"
  #peval "python -u submitSFrame.py -j shift/Signal_SUSY_EES1p01.py   --nosandbox --useEnv | tee nohup/nohup_SUSY_EES1p01.log"
else
  echo ">>> Wrong input! Use 1-2."
fi
