
loadLibs=[
    #"libGenVector",
    "libNtupleVariables",
    "libGoodRunsLists",
    "libPileupReweightingTool",
    "libBTaggingTools",
    "libTauTauResonances",
    "libScaleFactorTool",
    "libRecoilCorrector",
    "libJetCorrectionTool",
    "libSVFitTool",
]

loadPacks=[
    "SFrameCore.par",
    "NtupleVariables.par",
    "GoodRunsLists.par",
    "PileupReweightingTool.par",
    "BTaggingTools.par",
    "TauTauResonances.par",
    "ScaleFactorTool.par",
    "RecoilCorrector.par",
    "JetCorrectionTool.par",
    "SVFitTool.par",
]

compilePacks=[
    "../NtupleVariables",
    "../GoodRunsLists",
    "../PileupReweightingTool",
    "../TauTauResonances",
    "../BTaggingTools",
    "../LepEff2016",
    "../RecoilCorrections",
    "../JetCorrectionTool",
    "../SVFitTool",
]

AddUserItems = [
    ["RecoTreeName","tree"],
    ["doJEC","true"],
    ["doSVFit","true"],
]
  
inputTrees=["ntuplizer/tree"]
outputTrees=["tree_mutau","tree_etau"]

#End
