path2xml="/shome/ineuteli/shared/xml/xmls_MC2017_V2_newJEC"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SingleMuon"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput_emu2017/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=100
nProcesses=1
queue="short.q"
nFiles=2
hCPU="00:40:00"
hVMEM="5000M"
postFix="_2017_V2"
dataSets = [
    
#    ["SingleMuon_Run2017B",
#     [   "SingleMuon_Run2017B-17Nov2017-v1_0000.xml", ]],
#     
#    ["SingleMuon_Run2017C",
#     [   "SingleMuon_Run2017C-17Nov2017-v1_0000_0.xml",
#         "SingleMuon_Run2017C-17Nov2017-v1_0000_1.xml", ]],
#     
#    ["SingleMuon_Run2017D",
#     [   "SingleMuon_Run2017D-17Nov2017-v1_0000.xml", ]],
#     
#    ["SingleMuon_Run2017E",
#     [   "SingleMuon_Run2017E-17Nov2017-v1_0000.xml", ]],
#     
#    ["SingleMuon_Run2017F",
#     [   "SingleMuon_Run2017F-17Nov2017-v1_0000_0.xml",
#         "SingleMuon_Run2017F-17Nov2017-v1_0000_1.xml", ]],
    
   ["SingleMuon_Run2017B",
    [   "SingleMuon_Run2017B_17Nov2017-v1_0.xml",
        "SingleMuon_Run2017B_17Nov2017-v1_1.xml", ]],
    
   ["SingleMuon_Run2017C",
    [   "SingleMuon_Run2017C_17Nov2017-v1_0.xml",
        "SingleMuon_Run2017C_17Nov2017-v1_1.xml",
        "SingleMuon_Run2017C_17Nov2017-v1_2.xml",
        "SingleMuon_Run2017C_17Nov2017-v1_3.xml", ]],
    
   ["SingleMuon_Run2017D",
    [   "SingleMuon_Run2017D_17Nov2017-v1_0.xml",
        "SingleMuon_Run2017D_17Nov2017-v1_1.xml", ]],
    
   ["SingleMuon_Run2017E",
    [   "SingleMuon_Run2017E_17Nov2017-v1_0.xml",
        "SingleMuon_Run2017E_17Nov2017-v1_1.xml", ]],
    
   ["SingleMuon_Run2017F",
    [   "SingleMuon_Run2017F_17Nov2017-v1_0.xml",
        "SingleMuon_Run2017F_17Nov2017-v1_1.xml",
        "SingleMuon_Run2017F_17Nov2017-v1_2.xml",
        "SingleMuon_Run2017F_17Nov2017-v1_3.xml",
        "SingleMuon_Run2017F_17Nov2017-v1_4.xml",
        "SingleMuon_Run2017F_17Nov2017-v1_5.xml", ]],
    
]

userItems = [
    ["IsData","true"],
    ["IsSignal","false"],
    ["doRecoilCorr","false"],
]

jobOptionsFile2=open("AnalysisOptionsEM.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
