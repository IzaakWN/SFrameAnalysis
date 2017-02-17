path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="TT"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=3
hCPU="04:00:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP" #"_Moriond"
dataSets = [
       ["TT_TuneCUETP8M1",
        [   "TT_TuneCUETP8M1_13TeV-powheg-pythia8_reHLT_ext_0000_0.xml",
            "TT_TuneCUETP8M1_13TeV-powheg-pythia8_reHLT_ext_0000_1.xml",
            "TT_TuneCUETP8M1_13TeV-powheg-pythia8_reHLT_ext_0001_0.xml",
            "TT_TuneCUETP8M1_13TeV-powheg-pythia8_reHLT_ext_0001_1.xml",
            "TT_TuneCUETP8M1_13TeV-powheg-pythia8_reHLT_ext_0002.xml",   ]],
            ]
                
if "Moriond" in postFix: dataSets = [
       ["TT_TuneCUETP8M1",
        [   "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_0000_0.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_0000_1.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_0000_2.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_additional_0000_0.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_additional_0000_1.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_additional_0000_2.xml",
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_V1_additional_0001.xml",   ]],
            ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","false"],
                ["doRecoilCorr","false"],
                ["doTTpt","true"],
                ["doTES","false"],
                ["TESshift","0.00"],
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
