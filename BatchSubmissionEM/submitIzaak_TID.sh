#! /bin/bash

function peval { echo ">>> $@"; eval "$@"; }

if [[ $1 == 1 ]]; then
  echo ">>> JTF"
#   peval "python -u submitSFrame.py -j Background_TT_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF1p10.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF0p90.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p10.log"
#   peval "python -u submitSFrame.py -j Background_TT_JTF1p15.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF1p15.log"
#   peval "python -u submitSFrame.py -j Background_TT_JTF0p85.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p85.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF1p15.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p15.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF0p85.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF0p85.log"
#   peval "python -u submitSFrame.py -j Background_TT_EES0p97.py --nosandbox --useEnv | tee nohup/nohup_TT_EES0p97.log"
#   peval "python -u submitSFrame.py -j Background_ST_EES1p03.py --nosandbox --useEnv | tee nohup/nohup_ST_EES1p03.log"
elif [[ $1 == 2 ]]; then
  echo ">>> EES"
#   peval "python -u submitSFrame.py -j Background_TT_JTF0p90.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p90.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF1p10.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p10.log"
#   peval "python -u submitSFrame.py -j Background_TT_JTF0p85.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p85.log"
#   peval "python -u submitSFrame.py -j Background_ST_JTF1p15.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p15.log"
#   peval "python -u submitSFrame.py -j Background_TT_EES1p03.py --nosandbox --useEnv | tee nohup/nohup_TT_EES1p03.log"
#   peval "python -u submitSFrame.py -j Background_ST_EES0p97.py --nosandbox --useEnv | tee nohup/nohup_ST_EES0p97.log"
else
    echo ">>> Wrong input! Use 1-2."
fi
