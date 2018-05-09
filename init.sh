# get all necessary packages
# check out SFrame
echo "Creating a few directories"
mkdir AnalysisTemp
#mkdir AnalysisOut

cd SFrame/
source setup.sh
cd -;

echo "Compiling sub-directories"
for dir in SFrame BTaggingTools NtupleVariables PileupReweightingTool TauTauResonances GoodRunsLists LepEff2016 RecoilCorrections JetCorrectionTool SVFitTools
do
    echo
    echo $dir
    echo
    cd $dir
    make distclean
    make
    cd -
done
