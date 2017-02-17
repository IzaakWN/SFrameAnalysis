#! /bin/bash

echo
BASEDIR="/shome/$USER/analysis/SFrameAnalysis/BatchSubmission"
cd $BASEDIR
TESFILES="Signal_Izaak.py \
          Signal_HTT_Izaak.py \
          Background_DY_Izaak.py \
          Background_DY_NLO_Izaak.py \
          Background_TT_Izaak.py"
LTFFILES="Background_DY_Izaak.py \
          Background_DY_NLO_Izaak.py" # Background_DY_10to50_Izaak.py
EESFILES=`ls *_Izaak.py | grep -v TES | grep -v LTF | grep -v EES | grep -v SUSY | grep -v EWK | grep -v Data`
FILEND="_Izaak.py"






#################
# TES, EES, LTF #
#################

DO_VAR=(      "doTES"      "doEES"      "doLTF"  )
SHIFT=(        "0.03"       "0.01"       "0.03"  )
SHIFT_VAR=(  "TESshift"  "EESshift"   "LTFshift" )
FILES=(     "$TESFILES" "$EESFILES"  "$LTFFILES" )
UP=(         "TES1p03"    "EES1p01"    "LTF1p03" )
DOWN=(       "TES0p97"    "EES0p99"    "LTF0p97" )

for ((i=0;i<${#DO_VAR[@]};++i)); do
    
    DO_LINE="\[\"${DO_VAR[i]}\",\"false\"\]"
    DO_LINE_TRUE=`echo $DO_LINE | sed "s/false/true/"`
    
    SHIFT_LINE="\[\"${SHIFT_VAR[i]}\",\"0.00\"\]"
    SHIFT_LINE_UP=`echo $SHIFT_LINE | sed "s/0.00/${SHIFT[i]}/"`
    SHIFT_LINE_DOWN=`echo $SHIFT_LINE | sed "s/0.00/-${SHIFT[i]}/"`
    
    LABEL_LINE="postFix=\""
    LABEL_LINE_UP="${LABEL_LINE}_${UP[i]}"
    LABEL_LINE_DOWN="${LABEL_LINE}_${DOWN[i]}"
    
    echo ">>> "
    echo ">>> replacing \"${SHIFT_LINE}\" with: "
    echo ">>>    \"${SHIFT_LINE_UP}\"           "
    echo ">>>    \"${SHIFT_LINE_DOWN}\"         "
    echo ">>> "
    echo ">>> replacing \"${DO_LINE}\" with:    "
    echo ">>>    \"${DO_LINE_TRUE}\"            "
    echo ">>> "
    echo ">>> replacing \"${LABEL_LINE}\" with: "
    echo ">>>    \"${LABEL_LINE_UP}\"           "
    echo ">>>    \"${LABEL_LINE_DOWN}\"         "
    
    for f in ${FILES[i]}; do
        echo ">>> "
        echo ">>> making shifts for $f"
        if grep -q "${DO_LINE}" $f; then
            FUP=`  echo $f | sed "s/${FILEND}/_${UP[i]}${FILEND}/"`
            FDOWN=`echo $f | sed "s/${FILEND}/_${DOWN[i]}${FILEND}/"`
            echo ">>>   creating file: $FUP"
            echo ">>>   creating file: $FDOWN"
            cp $f $FUP
            cp $f $FDOWN
            sed -i "s/${DO_LINE}/${DO_LINE_TRUE}/" $FUP
            sed -i "s/${DO_LINE}/${DO_LINE_TRUE}/" $FDOWN
            if grep -q "${SHIFT_LINE}" $f; then
                sed -i "s/${SHIFT_LINE}/${SHIFT_LINE_UP}/"   $FUP
                sed -i "s/${SHIFT_LINE}/${SHIFT_LINE_DOWN}/" $FDOWN
            else echo ">>> WARNING! Could not find \"${SHIFT_LINE}\" line"
            fi
            if grep -q "${LABEL_LINE}" $f; then
                sed -i "s/${LABEL_LINE}/${LABEL_LINE_UP}/"   $FUP
                sed -i "s/${LABEL_LINE}/${LABEL_LINE_DOWN}/" $FDOWN          
            else echo ">>> WARNING! Could not find \"${LABEL_LINE}\" line"
            fi
        else echo ">>> WARNING! Could not find \"${DO_LINE}\" line"
        fi
    done
done
















# 
# 
# #######
# # TES #
# #######
# 
# TES_UP="TES1p03"
# TES_DOWN="TES0p97"
# DOTES_LINE="\[\"doTES\",\"false\"\]"
# DOTES_NEWLINE="\[\"doTES\",\"true\"\]"
# TESSHIFT="0.03"
# TESSHIFT_LINE="\[\"TESshift\",\"0.00\"\],"
# TESSHIFT_UP_NEWLINE=`echo $TESSHIFT_LINE | sed "s/0.00/$TESSHIFT/"`
# TESSHIFT_DOWN_NEWLINE=`echo $TESSHIFT_LINE | sed "s/0.00/-$TESSHIFT/"`
# LABEL_LINE="postFix=\""
# LABEL_TES_UP_NEWLINE="postFix=\"_${TES_UP}"
# LABEL_TES_DOWN_NEWLINE="postFix=\"_${TES_DOWN}"
# 
# echo " "
# echo ">>> replacing \"${TESSHIFT_LINE}\" with: "
# echo ">>>    \"${TESSHIFT_UP_NEWLINE}\"      "
# echo ">>>    \"${TESSHIFT_DOWN_NEWLINE}\"    "
# echo ">>> "
# echo ">>> replacing \"${DOTES_LINE}\" with: "
# echo ">>>    \"${DOTES_NEWLINE}\"           "
# echo ">>> "
# echo ">>> replacing \"${LABEL_LINE}\" with: "
# echo ">>>    \"${LABEL_TES_UP_NEWLINE}\"        "
# echo ">>>    \"${LABEL_TES_DOWN_NEWLINE}\"      "
# 
# for f in $TESFILES; do
#     echo ">>> "
#     echo ">>> making TES shifts for $f"
#     if grep -q "${DOTES_LINE}" $f; then
#         FUP=`  echo $f | sed "s/${FILEND}/_${TES_UP}${FILEND}/"`
#         FDOWN=`echo $f | sed "s/${FILEND}/_${TES_DOWN}${FILEND}/"`
#         echo ">>> creating file: $FUP"
#         echo ">>> creating file: $FDOWN"
#         cp $f $FUP
#         cp $f $FDOWN
#         sed -i "s/${DOTES_LINE}/${DOTES_NEWLINE}/" $FUP
#         sed -i "s/${DOTES_LINE}/${DOTES_NEWLINE}/" $FDOWN
#         if grep -q "${TESSHIFT_LINE}" $f; then
#             sed -i "s/${TESSHIFT_LINE}/${TESSHIFT_UP_NEWLINE}/"   $FUP
#             sed -i "s/${TESSHIFT_LINE}/${TESSHIFT_DOWN_NEWLINE}/" $FDOWN
#         else echo ">>> WARNING! Could not find \"${TESSHIFT_LINE}\" line"
#         fi
#         if grep -q "${LABEL_LINE}" $f; then
#             sed -i "s/${LABEL_LINE}/${LABEL_TES_UP_NEWLINE}/"   $FUP
#             sed -i "s/${LABEL_LINE}/${LABEL_TES_DOWN_NEWLINE}/" $FDOWN          
#         else echo ">>> WARNING! Could not find \"${LABEL_LINE}\" line"
#         fi
#     else echo ">>> WARNING! Could not find \"${DOTES_LINE}\" line"
#     fi
# done

echo " "


