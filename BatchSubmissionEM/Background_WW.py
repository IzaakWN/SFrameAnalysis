path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_newJEC"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WW"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_emu2017/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
queue="short.q"
nFiles=2
hCPU="00:40:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   [ "WW_TuneCP5",
    [   "WW_TuneCP5_13TeV-pythia8_0000.xml", ]],    
#    [ "WW_TuneCUETP8M1",
#     [   "WW_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
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
