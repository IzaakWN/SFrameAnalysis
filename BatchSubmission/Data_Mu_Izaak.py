path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="SingleMuon"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=4
hCPU="04:00:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP"
dataSets = [
               ["SingleMuon_1_Run2016",
                [   "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0000_0.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0000_1.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0000_2.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0001_0.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0001_1.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0001_2.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0002_0.xml",
                    "SingleMuon_Run2016B-23Sep2016-v3JECv3_BCD_v4_0002_1.xml", ]],
                
               ["SingleMuon_2_Run2016",
                [   "SingleMuon_Run2016C-23Sep2016-v1JECv3_BCD_v4_0000_0.xml",
                    "SingleMuon_Run2016C-23Sep2016-v1JECv3_BCD_v4_0000_1.xml",
                    "SingleMuon_Run2016C-23Sep2016-v1JECv3_BCD_v4_0000_2.xml",
                    "SingleMuon_Run2016D-23Sep2016-v1JECv3_BCD_v4_0000_0.xml",
                    "SingleMuon_Run2016D-23Sep2016-v1JECv3_BCD_v4_0000_1.xml",
                    "SingleMuon_Run2016D-23Sep2016-v1JECv3_BCD_v4_0000_2.xml",
                    "SingleMuon_Run2016D-23Sep2016-v1JECv3_BCD_v4_0001_0.xml",
                    "SingleMuon_Run2016D-23Sep2016-v1JECv3_BCD_v4_0001_1.xml", ]],
                
               ["SingleMuon_3_Run2016",
                [   "SingleMuon_Run2016E-23Sep2016-v1_JECv3_EF_v3_0000_0.xml",
                    "SingleMuon_Run2016E-23Sep2016-v1_JECv3_EF_v3_0000_1.xml",
                    "SingleMuon_Run2016E-23Sep2016-v1_JECv3_EF_v3_0000_2.xml",
                    "SingleMuon_Run2016E-23Sep2016-v1_JECv3_EF_v3_0001.xml",
                    "SingleMuon_Run2016F-23Sep2016-v1_JECv3_EF_v3_0000_0.xml",
                    "SingleMuon_Run2016F-23Sep2016-v1_JECv3_EF_v3_0000_1.xml",
                    "SingleMuon_Run2016F-23Sep2016-v1_JECv3_EF_v3_0000_2.xml", 
                    "SingleMuon_Run2016F-23Sep2016-v1_JECv3_G_v3_0000.xml",    ]],
                
               ["SingleMuon_4_Run2016",
                [   "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0000_0.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0000_1.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0000_2.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0001_0.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0001_1.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0001_2.xml",
                    "SingleMuon_Run2016G-23Sep2016-v1_JECv3_G_v3_0002.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0000_0.xml", ]],
                
               ["SingleMuon_5_Run2016",
                [   "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0000_1.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0000_2.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0001_0.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0001_1.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0001_2.xml",
                    "SingleMuon_Run2016H-PromptReco-v2_JECv3_H_v3_0002.xml",
                    "SingleMuon_Run2016H-PromptReco-v3_JECv3_H_v3_0000.xml",   ]],
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
