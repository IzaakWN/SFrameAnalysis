
loadLibs=[
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
    "../PileupReweightingTool",
    "../TauTauResonances",
    "../BTaggingTools",
    "../LepEff2017",
    "../JetCorrectionTool",
]

AddUserItems = [
    ["RecoTreeName","tree"],
    ["doJEC","true"],
    ["doSVFit","false"],
]

cycleName="TauTauAnalysis"  
inputTrees=["ntuplizer/tree"]
outputTrees=["tree_mutau","tree_etau"]

#End
