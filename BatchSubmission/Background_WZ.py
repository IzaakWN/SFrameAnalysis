path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WZ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
nEventsMax=-1
runningJobsLimit=6000
nProcesses=1
queue="short.q"
nFiles=1
hCPU="00:40:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   [ "WZ_TuneCP5",
    [   "WZ_TuneCP5_13TeV-pythia8_0000.xml", ]],
    
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
