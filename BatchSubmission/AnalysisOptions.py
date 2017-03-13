
loadLibs=[
    #"libGenVector",
    "libNtupleVariables",
    "libGoodRunsLists",
    "libPileupReweightingTool",
    "libBTaggingTools",
    "libTauTauResonances",
    "libSVFitTool",
    "libScaleFactorTool",
    "libRecoilCorrector",
            ]

loadPacks=[
    "SFrameCore.par",
    "NtupleVariables.par",
    "GoodRunsLists.par",
    "PileupReweightingTool.par",
    "BTaggingTools.par",
    "TauTauResonances.par",
    "SVFitTool.par",
    "ScaleFactorTool.par",
    "RecoilCorrector.par",
	        ]

compilePacks=[
    "../NtupleVariables",
    "../GoodRunsLists",
    "../PileupReweightingTool",
    "../BTaggingTools",
    "../SVFitTool",
    "../TauTauResonances",
    "../LepEff2016",
    "../RecoilCorrections",
            ]

AddUserItems = [
    ["RecoTreeName","tree"], 
    ["doSVFit","true"],
            ]
  
inputTrees=["ntuplizer/tree"]
outputTrees=["tree_mutau","tree_etau"]

#End