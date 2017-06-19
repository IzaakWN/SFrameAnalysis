#! /bin/bash

# DEFAULT VALUES
echo
BASEDIR="." #"/shome/ineuteli/analysis/SFrameAnalysis_Moriond/BatchSubmission"
XMLDIR="xmls_Moriond_T2" #Summer2016_noJEC"
SAMPLES=("DY2JetsToLL_M-10")  #DY2JetsToLL_M-10  #DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT
N=0

# USER OPTIONS
#http://stackoverflow.com/a/39754944/5499028
SAMPLES_USER=( )
while getopts b:d:x:s: option; do
    case "${option}" in
        b) BASEDIR=${OPTARG};;
        d) XMLDIR=${OPTARG};;
        x) XMLDIR=${OPTARG};;
        s) SAMPLES_USER+=(${OPTARG});;
    esac
done
[[ $SAMPLES_USER ]] && SAMPLES=( ) && SAMPLES=${SAMPLES_USER[@]}

# CHECK DIR
DIR="${BASEDIR}/${XMLDIR}"
if [ -d $DIR ]; then
    echo ">>> in $DIR:"
    echo ">>> " 
else
    echo ">>> ERROR! Directory does not exist: $DIR"
    echo
    exit 1
fi

# LOOP over files
for sample in ${SAMPLES[@]}; do
    
    for f in `ls ${DIR}/${sample}*.xml | awk -F '/' '{print $NF}'`; do
    EVENTS=`grep "${DIR}/$f" -e 'Total number of events processed: ' | grep -Po '[0-9]*'`
    if [[ ! $EVENTS ]]; then
      echo ">>> Warning! No number of events saved in $f!"
    else
      echo ">>> $EVENTS events in $f"
      N=$(($N+$EVENTS))
    fi
    done
    
    echo ">>> "
    echo ">>> with a grand total of $N events"
    echo ">>>"
    echo ">>>"
done

#echo ">>> "
echo ">>> done"
echo
exit 0
