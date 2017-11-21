path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond_T2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WW"
outDir="/scratch/$USER/SFrameAnalysis_ltau2017/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=5
hCPU="03:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
   
       [ "WWTo1L1Nu2Q_13TeV_nlo",
        [   "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_0000.xml", ]],
   
#        [ "WW_TuneCUETP8M1",
#         [   "WW_TuneCUETP8M1_13TeV-pythia8_0000.xml", ]],
        
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
