path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="TT"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_emu2017/"+jobName
nEventsMax=-1
runningJobsLimit=6000
nProcesses=1
queue="short.q"
nFiles=2
hCPU="00:40:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
   [ "TTTo2L2Nu",
    [   "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_0.xml",
        "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_1.xml",
        "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_2.xml",
        "TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_0001.xml", ]],
    
   [ "TTToHadronic",
    [   "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_0.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_1.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_2.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_0.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_1.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_2.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0002_0.xml",
        "TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_0002_1.xml", ]],
    
   [ "TTToSemiLeptonic",
    [   "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_0.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_1.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0000_2.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_0.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_1.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0001_2.xml",
        "TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_0002.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["doTTpt","true"],
    ["EESshift","0.00"],
    ["JTFshift","0.00"],
]

jobOptionsFile2=open("AnalysisOptionsEM.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
