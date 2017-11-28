path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="LowMass"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=15
hCPU="03:00:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   ["LowMass_30GeV_DiTauResonance",
    [   "LowMass_30GeV_TauTau_13TeV_RunIISpring16MiniAOD_v2.xml", ]],
    
]

userItems = [
    ["IsData","false"],
    ["IsSignal","true"],
    ["doRecoilCorr","True"],
    ["TESshift","0.00"],
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
