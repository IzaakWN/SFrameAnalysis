path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SingleMuon"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_mumu2017/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
nEventsMax=-1
runningJobsLimit=6000
nProcesses=1
queue="short.q"
nFiles=6
hCPU="00:40:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   ["SingleMuon_Run2017B",
    [   "SingleMuon_Run2017B-17Nov2017-v1_0000_0.xml",
        "SingleMuon_Run2017B-17Nov2017-v1_0000_1.xml",
        "SingleMuon_Run2017B-17Nov2017-v1_0001.xml", ]],
    
   ["SingleMuon_Run2017C",
    [   "SingleMuon_Run2017C-17Nov2017-v1_0000_0.xml",
        "SingleMuon_Run2017C-17Nov2017-v1_0000_1.xml",
        "SingleMuon_Run2017C-17Nov2017-v1_0001_0.xml",
        "SingleMuon_Run2017C-17Nov2017-v1_0001_1.xml",
        "SingleMuon_Run2017C-17Nov2017-v1_0002.xml", ]],
    
   ["SingleMuon_Run2017D",
     [   "SingleMuon_Run2017D-17Nov2017-v1_0000_0.xml",
        "SingleMuon_Run2017D-17Nov2017-v1_0000_1.xml",
        "SingleMuon_Run2017D-17Nov2017-v1_0001.xml", ]],
    
   ["SingleMuon_Run2017E",
    [   "SingleMuon_Run2017E-17Nov2017-v1_0000_0.xml",
        "SingleMuon_Run2017E-17Nov2017-v1_0000_1.xml",
        "SingleMuon_Run2017E-17Nov2017-v1_0001_0.xml",
        "SingleMuon_Run2017E-17Nov2017-v1_0001_1.xml", ]],
    
   ["SingleMuon_Run2017F",
    [   "SingleMuon_Run2017F-17Nov2017-v1_0000_0.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0000_1.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0000_2.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0001_0.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0001_1.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0001_2.xml",
        "SingleMuon_Run2017F-17Nov2017-v1_0002.xml", ]],
    
]

userItems = [
    ["IsData","true"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
]

jobOptionsFile2=open("AnalysisOptionsMM.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
