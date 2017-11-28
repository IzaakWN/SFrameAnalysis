path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SUSY"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=4
hCPU="04:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
    # SUSYGluGluToBBa1ToTauTau
   [ "SUSYGluGluToBBa1ToTauTau_M-25",
    [   "SUSYGluGluToBBa1ToTauTau_M-25_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-30",
    [   "SUSYGluGluToBBa1ToTauTau_M-30_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-35",
    [   "SUSYGluGluToBBa1ToTauTau_M-35_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-40",
    [   "SUSYGluGluToBBa1ToTauTau_M-40_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-45",
    [   "SUSYGluGluToBBa1ToTauTau_M-45_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-50",
    [   "SUSYGluGluToBBa1ToTauTau_M-50_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-55",
    [   "SUSYGluGluToBBa1ToTauTau_M-55_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-60",
    [   "SUSYGluGluToBBa1ToTauTau_M-60_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-65",
    [   "SUSYGluGluToBBa1ToTauTau_M-65_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToBBa1ToTauTau_M-70",
    [   "SUSYGluGluToBBa1ToTauTau_M-70_FilterMuOrEle15_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
    
    
    # SUSYGluGluToHToAA_AToBB_AToTauTau
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-15",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-15_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-20",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-20_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-25",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-25_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-30",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-30_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-35",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-35_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-40",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-40_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-45_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-50",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-50_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-55",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-55_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
     
   [ "SUSYGluGluToHToAA_AToBB_AToTauTau_M-60",
    [   "SUSYGluGluToHToAA_AToBB_AToTauTau_M-60_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
    
    
    # SUSYVBFToHToAA_AToBB_AToTauTau
   ["SUSYVBFToHToAA_AToBB_AToTauTau_M-20",
    [   "SUSYVBFToHToAA_AToBB_AToTauTau_M-20_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
    
   ["SUSYVBFToHToAA_AToBB_AToTauTau_M-40",
    [   "SUSYVBFToHToAA_AToBB_AToTauTau_M-40_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
    
   ["SUSYVBFToHToAA_AToBB_AToTauTau_M-60",
    [   "SUSYVBFToHToAA_AToBB_AToTauTau_M-60_TuneCUETP8M1_13TeV_madgraph_pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","true"],
    ["doRecoilCorr","false"],
    ["EESshift","0.00"],
]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
