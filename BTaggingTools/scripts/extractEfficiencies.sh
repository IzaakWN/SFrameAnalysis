#! /bin/bash

echo
VERBOSITY=0
VERBOSE_FLAG=""
OUTPUTFILE=""
DIRECTORY=""
while getopts d:o:v option; do
  case "${option}"
  in
    d) DIRECTORY="-d ${OPTARG}";;
    o) OUTPUTFILE="-o ${OPTARG}";;
    v) VERBOSITY=1; VERBOSE_FLAG="-v";;
  esac
done

WP="Medium"
PREFIX="jet_ak4_"
LABEL="Moriond"
ANALYSIS="TauTauAnalysis"
FILE_DIR="/scratch/ineuteli/SFrameAnalysis/AnalysisOutput"
FILES=(
  TT/${ANALYSIS}.TT_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DYJetsToLL_M-10to50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY1JetsToLL_M-10to50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY2JetsToLL_M-10to50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY3JetsToLL_M-10to50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DYJetsToLL_M-50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY1JetsToLL_M-50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY2JetsToLL_M-50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY3JetsToLL_M-50_TuneCUETP8M1_${LABEL}.root
  DY/${ANALYSIS}.DY4JetsToLL_M-50_TuneCUETP8M1_${LABEL}.root
  WJ/${ANALYSIS}.WJetsToLNu_TuneCUETP8M1_${LABEL}.root
  WJ/${ANALYSIS}.W1JetsToLNu_TuneCUETP8M1_${LABEL}.root
  WJ/${ANALYSIS}.W2JetsToLNu_TuneCUETP8M1_${LABEL}.root
  WJ/${ANALYSIS}.W3JetsToLNu_TuneCUETP8M1_${LABEL}.root
  WJ/${ANALYSIS}.W4JetsToLNu_TuneCUETP8M1_${LABEL}.root
  WW/${ANALYSIS}.WWTo1L1Nu2Q_13TeV_nlo_${LABEL}.root
  WZ/${ANALYSIS}.WZTo1L1Nu2Q_13TeV_nlo_${LABEL}.root
  WZ/${ANALYSIS}.WZTo2L2Q_13TeV_nlo_${LABEL}.root
  WZ/${ANALYSIS}.WZJToLLLNu_nlo_${LABEL}.root
  ZZ/${ANALYSIS}.VVTo2L2Nu_13TeV_nlo_${LABEL}.root
  ZZ/${ANALYSIS}.ZZTo2L2Q_13TeV_nlo_${LABEL}.root
  ZZ/${ANALYSIS}.ZZTo4L_13TeV_nlo_${LABEL}.root
  ST/${ANALYSIS}.ST_tW_top_5f_inclusiveDecays_${LABEL}.root
  ST/${ANALYSIS}.ST_tW_antitop_5f_inclusiveDecays_${LABEL}.root
  ST/${ANALYSIS}.ST_t-channel_top_4f_inclusiveDecays_${LABEL}.root
  ST/${ANALYSIS}.ST_t-channel_antitop_4f_inclusiveDecays_${LABEL}.root
)

FILES=(${FILES[@]/#/${FILE_DIR}/}) # prepend FILE_DIR to files
#echo ${FILES[@]}
echo ">>> ls -lh"
ls -lh ${FILES[@]} | \
  while read c1 c2 c3 c4 c5 c6 c7 c8 c9; do
    printf "%4s %3s %s %5s %s\n" $c7 $c6 $c8 $c5 $c9;
  done 

#for file in ${FILES[@]}; do
  #file="$FILE_DIR/$file"
  #[[ -e $file ]] && echo "found $file" || echo "did not find $file"
  #echo $f
#done

echo 
echo ">>> extractEfficiencies.py"
python extractEfficiencies.py ${FILES[@]} $VERBOSE_FLAG -w $WP -p $PREFIX $OUTPUTFILE $DIRECTORY -r
echo

