#! /bin/bash
# check with
#    grep -e "postFix=\"_Moriond\"" *_Izaak.py
#    grep -e "postFix=\"_ICHEP\"" *_Izaak.py

echo
BASEDIR="/shome/$USER/analysis/SFrameAnalysis/BatchSubmission"
cd $BASEDIR

FILES=`ls Signal_*_Izaak.py Background_*_Izaak.py Data_*_Izaak.py | grep -v "_TES" | grep -v "_EES" | grep -v "_LTF"`
LABEL="postFix=\""
LABEL1="postFix=\"_ICHEP\""
LABEL2="postFix=\"_Moriond\""
PATH1="xmls_Izaak"
PATH2="xmls_Moriond"

FILES0=( ) # no match
FILES1=( ) # match to LABEL1
FILES2=( ) # match to LABEL2

for f in $FILES; do
    if ! grep -q "$LABEL" $f; then
        echo ">>> Warning! File $f does not contain the label \"$LABEL\"!"
    fi
    if grep -q "$LABEL1" $f; then
        FILES1+=($f)
        (grep -q "$LABEL2" $f) && echo ">>> Warning! $f contains both \"$LABEL1\" and \"$LABEL2\"."
    elif grep -q "$LABEL2" $f; then
        FILES2+=($f)
    else
        FILES0+=($f)
    fi
done

echo ">>> "
if [[ $FILES1 ]]; then
    if [[ $FILES2 ]]; then
        echo ">>> Warning! The files do not all contain the same postFix:"
        echo ">>> \"$LABEL1\" was found in files"
        echo ">>>    ${FILES1[@]}" | sed 's/.py/.py\n>>>   /g'
        echo ">>> \"$LABEL2\" was found in files"
        echo ">>>    ${FILES2[@]}" | sed 's/.py/.py\n>>>   /g'
    fi    
    echo ">>> replacing \"$LABEL1\" with \"$LABEL2\""
    echo ">>> and \"$PATH1\" with \"$PATH2\" in files:"
    echo ">>>    ${FILES1[@]} " | sed 's/.py/.py\n>>>   /g'
    sed -i "s/${LABEL1}/${LABEL2}/" ${FILES1[@]}
    sed -i "s/${PATH1}/${PATH2}/"   ${FILES1[@]}
    
elif [[ $FILES2 ]]; then
    echo ">>> replacing $LABEL2 with $LABEL1"
    echo ">>> and \"$PATH2\" with \"$PATH1\" in files:"
    echo ">>>    ${FILES2[@]} " | sed 's/.py/.py\n>>>   /g'
    sed -i "s/${LABEL2}/${LABEL1}/" ${FILES2[@]}
    sed -i "s/${PATH2}/${PATH1}/"   ${FILES2[@]}
elif [[ $FILES0 ]]; then
    echo ">>> no matches with \"$LABEL1\" nor \"$LABEL2\" were found in these files:"
    echo ">>>    ${FILES0[@]} " | sed 's/.py/.py\n>>>   /g'
else
    echo ">>> Warning! Bug!"
    echo ">>> FILES  = $FILES"
    echo ">>> FILES0 = ${FILES1[@]}"
    echo ">>> FILES1 = ${FILES2[@]}"
    echo ">>> FILES2 = ${FILES3[@]}"
    echo ">>> no matches with \"$LABEL1\" nor \"$LABEL2\" were found in these files:"
    echo ">>>    ${FILES0[@]}" | sed 's/.py/.py\n>>>   /g'
fi

echo ">>> run shiftConfigFiles.sh:"
./shiftConfigFiles.sh

echo ">>> finished shiftConfigFiles.sh"
echo ">>>"
echo ">>> done"
echo " "
