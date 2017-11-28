path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WJ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=17
hCPU="04:45:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   [ "WJetsToLNu_TuneCUETP8M1",
    [   #"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_0000.xml",
        "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000.xml", ]],

    [ "W1JetsToLNu_TuneCUETP8M1",
     [  "W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
        "W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],

    [ "W2JetsToLNu_TuneCUETP8M1",
     [  "W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
        "W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],

    [ "W3JetsToLNu_TuneCUETP8M1",
     [  "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000.xml", ]],

    [ "W4JetsToLNu_TuneCUETP8M1",
     [  "W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","true"],
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
