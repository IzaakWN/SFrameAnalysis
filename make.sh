for dir in BTaggingTools GoodRunsLists LepEff2016 NtupleVariables PileupReweightingTool SFrame SVFitTools JetCorrectionTool TauTauResonances RecoilCorrections
do
    echo
    echo $dir
    echo
    cd $dir
    make distclean
    make
    cd -
done
