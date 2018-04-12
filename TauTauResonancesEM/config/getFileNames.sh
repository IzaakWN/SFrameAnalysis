#! /bin/bash

function peval { echo ">>> $@"; eval "$@"; }

DIR="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
N=20
SAMPLE="DYJ*"

while getopts s:n: option; do case "${option}" in
  n) N=${OPTARG};;
  s) SAMPLE="${OPTARG}*";;
esac done

peval "cd $DIR"
peval "ls -1 $SAMPLE" || exit 1
FILES=`ls $SAMPLE | xargs`
peval "cat $FILES | grep FileName | sort -R | head -n $N | sort -V"
peval "cd -"

