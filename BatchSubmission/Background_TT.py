path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="TT"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=5
hCPU="07:00:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   [ "TT_TuneCUETP8M1",
    [   "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_0000_0.xml",
        "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_0000_1.xml",
        "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_ext_0000_0.xml",
        "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_ext_0000_1.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["doTTpt","true"],
    ["TESshift","0.00"],
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
