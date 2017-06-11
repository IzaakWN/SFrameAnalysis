#! /bin/bash

FILES=(
    Signal.xml
#     DYJets_M-10to50.xml
#     DYJets_M-50.xml
#     TT_TuneCUETP8M1.xml
#     WJetsToLNu.xml
#     SingleMuon.xml
#     SingleMuon_G.xml
#     SingleMuon_H_v3.xml
#     SingleMuon_H_v2.xml
)

printf "\n\n\n\n\n\n\n\n"
if make distclean && make; then
    for f in ${FILES[@]}; do
        printf "\n\n\n>>> %s%s%s\n\n" "$(tput bold)$(tput setaf 2)" $f "$(tput sgr0)"
        sframe_main config/$f
    done
fi
