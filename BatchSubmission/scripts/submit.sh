#! /bin/bash
python -u submitSFrame.py -j Background_TT_Izaak.py --nosandbox --useEnv | tee nohup/nohup_TT.log
python -u submitSFrame.py -j Background_ST_Izaak.py --nosandbox --useEnv | tee nohup/nohup_ST.log
python -u submitSFrame.py -j Background_DY_Izaak.py --nosandbox --useEnv | tee nohup/nohup_DY.log
python -u submitSFrame.py -j Background_WW_Izaak.py --nosandbox --useEnv | tee nohup/nohup_WW.log
python -u submitSFrame.py -j Background_WJ_Izaak.py --nosandbox --useEnv | tee nohup/nohup_WJ.log
python -u submitSFrame.py -j Background_WZ_Izaak.py --nosandbox --useEnv | tee nohup/nohup_WZ.log
python -u submitSFrame.py -j Background_ZZ_Izaak.py --nosandbox --useEnv | tee nohup/nohup_ZZ.log
python -u submitSFrame.py -j Data_Mu_Izaak.py       --nosandbox --useEnv | tee nohup/nohup_Mu.log 
python -u submitSFrame.py -j Signal_Izaak.py        --nosandbox --useEnv | tee nohup/nohup_signal.log
