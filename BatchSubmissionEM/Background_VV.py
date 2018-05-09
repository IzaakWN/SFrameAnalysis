path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_trainingV2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="VV"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_emu2017/"+jobName
nEventsMax=-1
runningJobsLimit=6000
nProcesses=1
nFiles=2
hCPU="05:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   [ "VVTo2L2Nu_13TeV_nlo",
    [   "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_0000.xml", ]],
    
]


userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
    ["doEES","false"],
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