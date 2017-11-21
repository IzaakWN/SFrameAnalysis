#! /bin/bash

echo
BASEDIR="." #"/shome/$USER/analysis/SFrameAnalysis/BatchSubmission"
cd $BASEDIR
TESFILES="Signal_LowMass.py \
          Background_DY.py \
          Background_TT.py"
LTFFILES="Background_DY.py"
EESFILES=`ls Background_*.py Signal_*.py | grep -v TES | grep -v LTF | grep -v EES | grep -v SUSY | grep -v EWK | grep -v VBF | grep -v Data`
FILEND=".py"
WARNING="\e[31m\e[1mWARNING!"
S="\e[0m"

#################
# TES, EES, LTF #
#################

DO_VAR=(      "doTES"       "doLTF"      "doEES"  )
SHIFT=(       "0.012"        "0.03"       "0.01"  )
SHIFT_VAR=(  "TESshift"   "LTFshift"   "EESshift" )
FILES=(     "$TESFILES"  "$LTFFILES"  "$EESFILES" )
UP=(         "TES1p03"     "LTF1p03"    "EES1p01" )
DOWN=(       "TES0p97"     "LTF0p97"    "EES0p99" )

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
            else echo -e ">>> ${WARNING} Could not find \"${SHIFT_LINE}\" line${S}"
            fi
            if grep -q "${LABEL_LINE}" $f; then
                sed -i "s/${LABEL_LINE}/${LABEL_LINE_UP}/"   $FUP
                sed -i "s/${LABEL_LINE}/${LABEL_LINE_DOWN}/" $FDOWN          
            else echo -e ">>> ${WARNING} Could not find \"${LABEL_LINE}\" line${S}"
            fi
        else echo -e ">>> ${WARNING} Could not find \"${DO_LINE}\" line${S}"
        fi
    done
done


echo " "
