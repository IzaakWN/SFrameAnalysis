path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="DY"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_emu2017/"+jobName
nEventsMax=-1
nProcesses=1
queue="short.q"
nFiles=3
hCPU="00:30:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   [ "DYJetsToLL_M-50_TuneCP5",
    [   "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000_0.xml",
        "DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],
    
   [ "DY1JetsToLL_M-50_TuneCP5",
    [   "DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml",
        "DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext_0000_0.xml",
        "DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext_0000_1.xml", ]],
    
   [ "DY2JetsToLL_M-50_TuneCP5",
    [   "DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml",
        "DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext_0000.xml", ]],
    
   [ "DY3JetsToLL_M-50_TuneCP5",
    [   "DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
]


userItems = [
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["doZpt","false"], # only to LO DY!
    ["EESshift","0.00"],
]

jobOptionsFile2=open("AnalysisOptionsEM.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
