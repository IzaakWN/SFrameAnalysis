path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="HTT"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=3
hCPU="03:00:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP" #_Moriond"
dataSets = [
        [ "GluGluHToTauTau_M125",
         [  "GluGluHToTauTau_M125_13TeV_powheg_pythia8_reHLT_v7_0000_0.xml",
            "GluGluHToTauTau_M125_13TeV_powheg_pythia8_reHLT_v7_0000_1.xml",
            "GluGluHToTauTau_M125_13TeV_powheg_pythia8_reHLT_v7_0000_2.xml", ]],
            ]
                
if "Moriond" in postFix: dataSets = [
        [ "GluGluHToTauTau_M125",
         [  "GluGluHToTauTau_M125_13TeV_powheg_pythia8_v1_0000_0.xml",
            "GluGluHToTauTau_M125_13TeV_powheg_pythia8_v1_0000_1.xml",
            "GluGluHToTauTau_M125_13TeV_powheg_pythia8_v1_0000_2.xml", ]],
            ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","true"],
                ["doRecoilCorr","true"],
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
