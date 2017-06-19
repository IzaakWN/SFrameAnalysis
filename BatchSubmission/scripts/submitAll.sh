# -u option to avoid output buffering
rm -r nohup/nohup_*.log
python -u submitSFrame.py -j Data_Mu_Izaak.py --nosandbox --useEnv > nohup/nohup_Mu.log & disown
python -u submitSFrame.py -j Signal_Izaak.py --nosandbox --useEnv > nohup/nohup_Signal.log & disown
python -u submitSFrame.py -j Background_TT_Izaak.py --nosandbox --useEnv > nohup/nohup_TT.log & disown
python -u submitSFrame.py -j Background_DY_Izaak.py --nosandbox --useEnv > nohup/nohup_DY.log & disown
python -u submitSFrame.py -j Background_WW_Izaak.py --nosandbox --useEnv > nohup/nohup_WW.log & disown
python -u submitSFrame.py -j Background_WJ_Izaak.py --nosandbox --useEnv > nohup/nohup_WJ.log & disown
python -u submitSFrame.py -j Background_WZ_Izaak.py --nosandbox --useEnv > nohup/nohup_WZ.log & disown
python -u submitSFrame.py -j Background_ZZ_Izaak.py --nosandbox --useEnv > nohup/nohup_ZZ.log & disown
python -u submitSFrame.py -j Background_ST_Izaak.py --nosandbox --useEnv > nohup/nohup_ST.log & disown

