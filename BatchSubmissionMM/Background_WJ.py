path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WJ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_mumu2017/"+jobName
nEventsMax=-1
runningJobsLimit=6000
nProcesses=1
queue="short.q"
nFiles=3
hCPU="00:30:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   # # 94X, new JEC
   #[ "WJetsToLNu",
   # [   "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
   #  
   #[ "W1JetsToLNu",
   # [   "W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
   #
   # [ "W2JetsToLNu",
   #  [  "W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
   #  
   # [ "W3JetsToLNu",
   #  [  "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
   #  
   # [ "W4JetsToLNu",
   #  [  "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
    # 94X, new JEC, training v2
   [ "WJetsToLNu",
    [   "WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
   [ "W1JetsToLNu",
    [   "W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000_0.xml",
        "W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],
    
   [ "W2JetsToLNu",
    [   "W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
   [ "W3JetsToLNu",
    [  "W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
   [ "W4JetsToLNu",
    [  "W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["MC_V1","true"],
]

jobOptionsFile2=open("AnalysisOptionsMM.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
