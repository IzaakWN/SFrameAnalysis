path2xml="$SFRAME_DIR/../BatchSubmission/xmls_VTcheck" #"/shome/ineuteli/shared/xml/xmls_MC2017_V2_newJEC"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="DY"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
nEventsMax=-1
#nEventsMax=200
runningJobsLimit=6000
nProcesses=1
queue="short.q"
nFiles=2
hCPU="00:25:00"
hVMEM="5000M"
postFix="_2017_V2_VTcheck"
dataSets = [
    
   [ "DYJetsToLL_M-50_TuneCP5",
    [   "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000_0.xml",
        "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],
    
]


userItems = [
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["doZpt","false"], # only to LO DY!
    ["TESshift","0.00"],
    ["EESshift","0.00"],
    ["LTFshift","0.00"],
]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
