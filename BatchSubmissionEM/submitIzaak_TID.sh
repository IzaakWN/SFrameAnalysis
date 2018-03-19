#! /bin/bash

if [[ $1 == 1 ]]; then
  echo ">>> JTF"
  python -u submitSFrame.py -j Background_ST_JTF1p150.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p150.log
  python -u submitSFrame.py -j Background_ST_JTF0p850.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF0p850.log
  python -u submitSFrame.py -j Background_TT_JTF1p150.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF1p150.log
  python -u submitSFrame.py -j Background_TT_JTF0p850.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p850.log
elif [[ $1 == 2 || $1 == 3 ]]; then
  echo ">>> EES"
  python -u submitSFrame.py -j Background_ST_EES1p030.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF1p030.log
  python -u submitSFrame.py -j Background_ST_EES0p970.py --nosandbox --useEnv | tee nohup/nohup_ST_JTF0p970.log
  python -u submitSFrame.py -j Background_TT_EES1p030.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF1p030.log
  python -u submitSFrame.py -j Background_TT_EES0p970.py --nosandbox --useEnv | tee nohup/nohup_TT_JTF0p970.log
else
    echo ">>> Wrong input! Use 1-3."
fi