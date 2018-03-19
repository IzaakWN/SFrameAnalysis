#! /bin/bash

FILES=(
#  DYJets_M-50_v2.xml
#  WJets_v2.xml
#  WJets_v2_newJEC.xml
#  TTTo2L2Nu_v2.xml
  TTTo2L2Nu_v2_newJEC.xml
#  SingleMuon_v2.xml
#  SingleMuon_v2_newJEC.xml
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
