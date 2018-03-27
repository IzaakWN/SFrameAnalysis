#! /bin/bash

function peval { echo ">>> $@"; eval "$@"; }

case $1 in
  1) echo ">>> DY TES Down uneven"
     FILES=`ls TES/Background_DY_TES0p99*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p97*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p95*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p93*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p91*.py | sort -r`
     ;;
  2) echo ">>> DY TES Up even"
     FILES=`ls TES/Background_DY_TES1p00*.py`
     FILES+=" "`ls TES/Background_DY_TES1p02*.py`
     FILES+=" "`ls TES/Background_DY_TES1p04*.py`
     FILES+=" "`ls TES/Background_DY_TES1p060.py`
     ;;
  3) echo ">>> DY TES Down even"
     FILES=`ls TES/Background_DY_TES0p98*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p96*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p94*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p92*.py | sort -r`
     FILES+=" "`ls TES/Background_DY_TES0p90*.py | sort -r`
     ;;
  4) echo ">>> DY TES Up uneven"
     FILES=`ls TES/Background_DY_TES1p01*.py`
     FILES+=" "`ls TES/Background_DY_TES1p03*.py`
     FILES+=" "`ls TES/Background_DY_TES1p05*.py`
     ;;
  *) echo ">>> Wrong input! Use 1-4."
     exit 1
     ;;
esac

echo ">>> shift files: $FILES"
for f in $FILES; do
  SHIFT=`echo $f | sed 's/.*\(TES.*\)\.py/\1/'`
  peval "python -u submitSFrame.py -j $f --nosandbox --useEnv | tee nohup/nohup_DY_${SHIFT}.log"
done;
