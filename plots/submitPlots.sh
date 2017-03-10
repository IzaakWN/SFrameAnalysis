#!/bin/bash
# https://cp3.irmp.ucl.ac.be/projects/delphes/wiki/WorkBook/Tutorials/Mc4Bsm
# https://cp3.irmp.ucl.ac.be/projects/delphes/wiki/WorkBook/QuickTour

printf "###########################################\n"
printf "##   Run Delphes for samples %-12s##\n" "$1"
printf "###########################################\n"

CATEGORY="$1"
JOBLOGFILES="myout.txt myerr.txt"
OUTDIRS=""#"mutau eletau" # if directories are made locally
DBG=2
TOPWORKDIR="/scratch/$USER"
JOBDIR="plots/$CATEGORY"
CMSSW_DIR="/shome/ineuteli/analysis/CMSSW_8_0_20"
BASEDIR="/shome/ineuteli/analysis/SFrameAnalysis/plots"

STARTDIR=$BASEDIR
WORKDIR=$TOPWORKDIR/$JOBDIR
RESULTDIR=$BASEDIR/"submitPlots"
OUTDIR=$BASEDIR



##### MONITORING/DEBUG INFORMATION ########################################

mkdir -p /shome/ineuteli/analysis/SFrameAnalysis/plots/submitPlots
#$ -e /shome/ineuteli/analysis/SFrameAnalysis/plots/submitPlots
#$ -o /shome/ineuteli/analysis/SFrameAnalysis/plots/submitPlots

DATE_START=`date +%s`
echo "Job started at " `date`
cat <<EOF

###########################################
##       QUEUEING SYSTEM SETTINGS:       ##
###########################################
  HOME=$HOME
  USER=$USER
  JOB_ID=$JOB_ID
  JOB_NAME=$JOB_NAME
  HOSTNAME=$HOSTNAME
  TASK_ID=$TASK_ID
  QUEUE=$QUEUE
EOF

if test 0"$DBG" -gt 0; then
    echo " "
    echo "###########################################"
    echo "##         Environment Variables         ##"
    echo "###########################################"
    env
fi



##### SET ENVIRONMENT #####################################################

if test -e "$WORKDIR"; then
   echo "ERROR: WORKDIR ($WORKDIR) already exists! Aborting..." >&2
   echo `ls $TOPWORKDIR` >&2
   #exit 1
fi
mkdir -p $WORKDIR
if test ! -d "$WORKDIR"; then
   echo "ERROR: Failed to create workdir ($WORKDIR)! Aborting..." >&2
   exit 1
fi

cd $WORKDIR
cat <<EOF

###########################################
##             JOB SETTINGS:             ##
###########################################
  STARTDIR=$STARTDIR
  WORKDIR=$WORKDIR
  RESULTDIR=$RESULTDIR
  SERESULTDIR=$SERESULTDIR
EOF



echo " "
echo "###########################################"
echo "##         MY FUNCTIONALITY CODE         ##"
echo "###########################################"


source $VO_CMS_SW_DIR/cmsset_default.sh >&2
cd $CMSSW_DIR/src
SCRAM_ARCH=slc6_amd64_gcc530
eval `scramv1 runtime -sh`
if test $? -ne 0; then
   echo "ERROR: Failed to source scram environment" >&2
   exit 1
fi

cd $WORKDIR

echo ">>>\
python $BASEDIR/plot.py -s $CATEGORY >> myout.txt 2>> myerr.txt"
python $BASEDIR/plot.py -s $CATEGORY >> myout.txt 2>> myerr.txt
echo ">>> ls"
ls



##### RETRIEVAL OF OUTPUT FILES AND CLEANING UP ###########################

cd $WORKDIR
if test 0"$DBG" -gt 0; then
    echo " " 
    echo "###########################################################"
    echo "##   MY OUTPUT WILL BE MOVED TO \$RESULTDIR and \$OUTDIR   ##"
    echo "###########################################################"
    echo "  \$RESULTDIR=$RESULTDIR"
    echo "  \$OUTDIR=$OUTDIR"
    echo "Working directory contents:"
    echo "pwd: " `pwd`
    ls -Rl
fi

cd $WORKDIR
if test x"$JOBLOGFILES" != x; then
    mkdir -p $RESULTDIR
    if test ! -e "$RESULTDIR"; then
        echo "ERROR: Failed to create $RESULTDIR ...Aborting..." >&2
        exit 1
    fi
    for n in $JOBLOGFILES; do
        echo ">>> copying $n"
        if test ! -e $WORKDIR/$n; then
            echo "WARNING: Cannot find output file $WORKDIR/$n. Ignoring it" >&2
        else
            cp -a $WORKDIR/$n $RESULTDIR/"category_"${CATEGORY}_$n
            if test $? -ne 0; then
                echo "ERROR: Failed to copy $WORKDIR/$n to $RESULTDIR/${SAMPLEN}_$n" >&2
            fi
    fi
    done
fi


cd $WORKDIR
if test x"$OUTDIRS" != x; then
    if test 0"$DBG" -ge 2; then
        srmdebug="-v"
    fi
    for outdir in $OUTDIRS; do
        if test ! -e $WORKDIR/$outdir; then
            echo "WARNING: Cannot find output file $WORKDIR/$outdir. Ignoring it" >&2
        else
            if test ! -e $OUTDIR/$outdir; then
                mkdir -p $OUTDIR/$outdir # mkdir
                echo ">>> created $OUTDIR/$outdir"
            fi
            if [[ `find $WORKDIR/$outdir -maxdepth 1 -type f | wc -l` > 0 ]]; then
                echo ">>> copying files of $outdir to $OUTDIR/$outdir"
                #cp $WORKDIR/$outdir/* $OUTDIR/$outdir/ # copy, files only!
                find $WORKDIR/$outdir -maxdepth 1 -type f | xargs cp -t $OUTDIR/$outdir # copy, files only!
                if test $? -ne 0; then
                    echo "ERROR: Failed to copy $WORKDIR/$outdir/* to $OUTDIR/$outdir" >&2
                fi
            fi
            
            # find plots/MVA/ -maxdepth 1 -type d | sed "s,plots/MVA/,,"
            # ls -d $WORKDIR/*/ | sed "s,$WORKDIR,,"
            for dir in $outdir/*/; do
                [ -d "$dir" ] || continue # if not a directory, skip
                if test ! -e $OUTDIR/$dir; then
                    mkdir $OUTDIR/$dir # mkdir
                    echo ">>> created $OUTDIR/$dir"
                fi
                echo ">>> copying contents of $dir to $OUTDIR/$dir"
                cp -a $WORKDIR/$dir/* $OUTDIR/$dir # copy whole folder recursively
                if test $? -ne 0; then
                    echo "ERROR: Failed to copy $WORKDIR/$dir/* to $OUTDIR/$dir" >&2
                fi
            done
        fi
    done
fi

echo "Cleaning up $WORKDIR"
rm -rf $WORKDIR




###########################################################################

DATE_END=`date +%s`
RUNTIME=$((DATE_END-DATE_START))
echo " "
echo "#####################################################"
echo "    Job finished at " `date`
echo "    Wallclock running time: $(( $RUNTIME / 3600 )):$(( $RUNTIME % 3600 /60 )):$(( $RUNTIME % 60 )) "
echo "#####################################################"
echo " "

exit 0
