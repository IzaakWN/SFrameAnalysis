path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="HTT"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=2
hCPU="03:30:00"
hVMEM="5000M"
postFix="_Moriond"
dataSets = [
    ["SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV",
     [  "SUSYGluGluToHToTauTau_M-160_TuneCUETP8M1_13TeV-pythia8.xml", ]],
            ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","true"],
                ["doSVFit","false"],
                ["doRecoilCorr","True"],
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
