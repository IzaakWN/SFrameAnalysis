path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="signal"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
#nEventsMax=200
nEventsMax=-1
nProcesses=1
nFiles=15
hCPU="03:00:00"
hVMEM="5000M"
postFix="_Moriond"
dataSets = [
  ["LowMass_30GeV_DiTauResonance",
    [ "LowMass_30GeV_DiTauResonance_RunIISpring16MiniAODv2_PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v2.xml", ]],
            ]

userItems = [
                ["IsData","false"],
                ["IsSignal","true"],
                ["doRecoilCorr","false"],
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
