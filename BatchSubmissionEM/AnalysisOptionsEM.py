
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
    "../GoodRunsLists",
    "../PileupReweightingTool",
    "../TauTauResonancesEM",
    "../BTaggingTools",
    "../LepEff2017",
    "../RecoilCorrections",
    "../JetCorrectionTool",
    "../SVFitTool",
]

AddUserItems = [
    ["RecoTreeName","tree"],
    ["doJEC","false"],
    ["doSVFit","false"],
]
  
inputTrees=["ntuplizer/tree"]
outputTrees=["tree_emu"]

#End
