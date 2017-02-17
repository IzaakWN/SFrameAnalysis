path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Izaak"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="signal"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=3
hCPU="03:00:00"
hVMEM="5000M"
postFix="_ICHEP" #"_ICHEP" #"_Moriond"
dataSets = [
    ["LowMass_30GeV_DiTauResonance",
     [  "LowMass_30GeV_DiTauResonance_RunIISpring16MiniAODv2_asymptotic_miniAODv2.xml"
        #"LowMass_30GeV_DiTauResonance_RunIISpring16MiniAODv2_asymptotic_miniAODv2_short.xml",
        ]],                
            ]
                
if "Moriond" in postFix: dataSets = [
    ["LowMass_30GeV_DiTauResonance",
     [  "LowMass_30GeV_DiTauResonance_RunIISpring16MiniAODv2_asymptotic_miniAODv2_short.xml", ]],
            ]

userItems = [
                ["IsData","false"],
                ["IsSignal","true"],
                ["doRecoilCorr","false"], # set to true?
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
