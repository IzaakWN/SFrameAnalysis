#! /bin/bash

FILES=(
#    Signal.xml
#    SUSY.xml
#    DYJets_M-10to50.xml
#    DYJets_M-50.xml
#    VBF.xml
    TT_TuneCUETP8M1.xml
#    TTJets_DiLept.xml
#    WJetsToLNu.xml
#    SingleMuon.xml
)

RUN_ONLY=0
while getopts s option; do
    [[ ${option} = s ]] && RUN_ONLY=1;
done

   [[ $RUN_ONLY > 0 ]] || printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
if [[ $RUN_ONLY > 0 ]] || ( make distclean && make ); then
    for f in ${FILES[@]}; do
        printf "\n\n\n\n\n\n\n\n\n\n\n>>> %s%s%s\n\n" "$(tput bold)$(tput setaf 2)" $f "$(tput sgr0)"
        sframe_main config/$f
    done
fi
