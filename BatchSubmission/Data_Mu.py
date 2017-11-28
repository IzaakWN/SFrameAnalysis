path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V1_small"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SingleMuon"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_ltau2017/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=11
hCPU="05:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   ["SingleMuon_Run2017B",
    [   "SingleMuon_Run2017B-12Sep2017-v1_0000_0.xml",
        "SingleMuon_Run2017B-12Sep2017-v1_0000_1.xml",
        "SingleMuon_Run2017B-12Sep2017-v1_0001_0.xml",
        "SingleMuon_Run2017B-12Sep2017-v1_0001_1.xml",
        "SingleMuon_Run2017B-12Sep2017-v1_0002_0.xml",
        "SingleMuon_Run2017B-12Sep2017-v1_0002_1.xml", ]],
    
   ["SingleMuon_Run2017C",
    [   "SingleMuon_Run2017C-12Sep2017-v1_0000_0.xml",
        "SingleMuon_Run2017C-12Sep2017-v1_0000_1.xml",
        "SingleMuon_Run2017C-12Sep2017-v1_0001_0.xml",
        "SingleMuon_Run2017C-12Sep2017-v1_0001_1.xml",
        "SingleMuon_Run2017C-12Sep2017-v1_0002_0.xml",
        "SingleMuon_Run2017C-12Sep2017-v1_0002_1.xml", ]],
    
   ["SingleMuon_Run2017D",
    [   "SingleMuon_Run2017D-PromptReco-v1_GTv11_0000_0.xml",
        "SingleMuon_Run2017D-PromptReco-v1_GTv11_0000_1.xml",
        "SingleMuon_Run2017D-PromptReco-v1_GTv11_0001_0.xml",
        "SingleMuon_Run2017D-PromptReco-v1_GTv11_0001_1.xml",
        "SingleMuon_Run2017D-PromptReco-v1_GTv11_0002_0.xml",
        "SingleMuon_Run2017D-PromptReco-v1_GTv11_0002_1.xml", ]],
    
   ["SingleMuon_Run2017E",
    [   "SingleMuon_Run2017E-PromptReco-v1_GTv11_0000_0.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0000_1.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0001_0.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0001_1.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0002_0.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0002_1.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0003_0.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0003_1.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0004_0.xml",
        "SingleMuon_Run2017E-PromptReco-v1_GTv11_0004_1.xml", ]],
    
   ["SingleMuon_5_Run2016",
    [   "SingleMuon_Run2017F-PromptReco-v1_GTv11_0000_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0000_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0001_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0001_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0002_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0002_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0003_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0003_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0004_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0004_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0005_0.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0005_1.xml",
        "SingleMuon_Run2017F-PromptReco-v1_GTv11_0006.xml",   ]],
    
]

userItems = [
    ["IsData","true"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
