path2xml="$SFRAME_DIR/../BatchSubmission/xmls_2017"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="EWK"
outDir="/scratch/$USER/SFrameAnalysis_ltau2017/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=4
hCPU="03:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [ ]
                            
if "Moriond" in postFix: dataSets = [
        
       [ "EWKWMinus2Jets_WToLNu_M-50",
        [   "EWKWMinus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8_0000.xml", ]],
        
       [ "EWKWPlus2Jets_WToLNu_M-50",
        [   "EWKWPlus2Jets_WToLNu_M-50_13TeV-madgraph-pythia8_0000.xml", ]],
        
       [ "EWKZ2Jets_ZToLL_M-50",
        [   "EWKZ2Jets_ZToLL_M-50_13TeV-madgraph-pythia8_0000.xml", ]],
            ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","false"],
                #["doSVFit","true"],
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
