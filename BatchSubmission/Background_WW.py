path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WW"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=5
hCPU="03:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   [ "WW_TuneCUETP8M1",
    [   "WW_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
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
