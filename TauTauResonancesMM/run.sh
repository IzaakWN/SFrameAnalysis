#! /bin/bash

FILES=(
    DYJets_M-50.xml
#    TTTo2L2Nu.xml
#    WJets.xml
#    SingleMuon.xml
)

RUN_ONLY=0
while getopts s option; do
  [[ ${option} = s ]] && RUN_ONLY=1;
done

[[ $RUN_ONLY > 0 ]] || printf "\n\n\n\n\n\n\n"
if [[ $RUN_ONLY > 0 ]] || ( make distclean && make ); then
  for f in ${FILES[@]}; do
    CMD="sframe_main config/$f"
    printf "\n\n\n>>> %s%s%s\n\n" "$(tput bold)$(tput setaf 2)" "$CMD" "$(tput sgr0)"
    $CMD
  done
fi
