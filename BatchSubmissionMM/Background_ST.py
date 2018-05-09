path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="ST"
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
    
   [ "ST_t-channel_top_4f_inclusiveDecays",
    [   "ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_0000.xml", ]],
    
   [ "ST_t-channel_antitop_4f_inclusiveDecays",
    [   "ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_0000.xml", ]],
    
   [ "ST_tW_top_5f_inclusiveDecays",
    [   "ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_0000.xml", ]],
    
   [ "ST_tW_antitop_5f_inclusiveDecays",
    [   "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8_0000.xml", ]],
    
   [ "ST_s-channel_4f_leptonDecays",
    [   "ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
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
