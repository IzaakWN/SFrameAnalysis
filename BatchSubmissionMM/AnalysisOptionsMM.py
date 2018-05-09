
loadLibs=[
    "libNtupleVariables",
    "libGoodRunsLists",
    "libPileupReweightingTool",
    "libBTaggingTools",
    "libTauTauResonancesMM",
    "libScaleFactorTool",
    "libRecoilCorrector",
    "libJetCorrectionTool",
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
]

compilePacks=[
    "../NtupleVariables",
    "../PileupReweightingTool",
    "../TauTauResonancesMM",
    "../BTaggingTools",
    "../LepEff2017",
    "../JetCorrectionTool",
]

AddUserItems = [
    ["RecoTreeName","tree"],
    ["doJEC","true"],
]

cycleName="DiMuonAnalysis"  
inputTrees=["ntuplizer/tree"]
outputTrees=["tree_mumu"]

#End
