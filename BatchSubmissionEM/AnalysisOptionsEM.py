
loadLibs=[
    "libNtupleVariables",
    "libGoodRunsLists",
    "libPileupReweightingTool",
    "libBTaggingTools",
    "libTauTauResonancesEM",
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
    "TauTauResonancesEM.par",
    "ScaleFactorTool.par",
    "RecoilCorrector.par",
    "JetCorrectionTool.par",
    "SVFitTool.par",
]

compilePacks=[
    "../NtupleVariables",
    "../PileupReweightingTool",
    "../TauTauResonancesEM",
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
outputTrees=["tree_emu"]

#End
