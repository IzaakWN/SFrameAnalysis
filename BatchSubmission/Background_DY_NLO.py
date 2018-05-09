path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="DY"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=3
hCPU="03:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   [ "DYJetsToLL_M-10to50_nlo",
    [   "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_HLT1_0000_0.xml",
        "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_HLT1_0000_1.xml",
        "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_HLT1_0000_2.xml", ]],
    
   [ "DY1JetsToLL_M-10to50_nlo",
    [   "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_reHLT_0000.xml", ]],
    
   [ "DY2JetsToLL_M-10to50_nlo",
    [   "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_reHLT_0000.xml", ]],
    
]

userItems = [ 
    ["IsData","false"],
    ["IsSignal","false"],
    ["doRecoilCorr","true"],
    ["doTES","false"],
    ["TESshift","0.00"],
    ["doEES","false"],
    ["EESshift","0.00"],
    ["doLTF","false"],
    ["LTFshift","0.00"],
    ["doZpt","false"], # only to LO DY!
]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
