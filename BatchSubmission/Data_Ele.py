path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SingleElectron"
outDir="/scratch/$USER/SFrameAnalysis_ltau2017/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=22
hCPU="05:30:00"
hVMEM="5000M"
postFix="_2017"
dataSets = [
    
   ["SingleElectron_1_Run2016",
    [   "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0001_0.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0001_1.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0001_2.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0002_0.xml",
        "SingleElectron_Run2016B-03Feb2017_ver2-v2SingleElectron_BCD_03Feb2017_0002_1.xml", ]],
        
   ["SingleElectron_2_Run2016",
    [   "SingleElectron_Run2016C-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016C-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016C-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016D-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016D-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016D-03Feb2017-v1SingleElectron_BCD_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016D-03Feb2017-v1SingleElectron_BCD_03Feb2017_0001_0.xml",
        "SingleElectron_Run2016D-03Feb2017-v1SingleElectron_BCD_03Feb2017_0001_1.xml", ]],
        
   ["SingleElectron_3_Run2016",
    [   "SingleElectron_Run2016E-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016E-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016E-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016E-03Feb2017-v1SingleElectron_EF_03Feb2017_0001.xml",
        "SingleElectron_Run2016F-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016F-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016F-03Feb2017-v1SingleElectron_EF_03Feb2017_0000_2.xml",    ]],
        
   ["SingleElectron_4_Run2016",
    [   "SingleElectron_Run2016F-03Feb2017-v1SingleElectron_G_03Feb2017_0000.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0001_0.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0001_1.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0001_2.xml",
        "SingleElectron_Run2016G-03Feb2017-v1SingleElectron_G_03Feb2017_0002.xml",   ]],
        
   ["SingleElectron_5_Run2016",
    [   "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0000_0.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0000_1.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0000_2.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0001_0.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0001_1.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0001_2.xml",
        "SingleElectron_Run2016H-03Feb2017_ver2-v1SingleElectron_H_03Feb2017_0002.xml",
        "SingleElectron_Run2016H-03Feb2017_ver3-v1SingleElectron_H_03Feb2017_0000.xml",   ]],
    
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
