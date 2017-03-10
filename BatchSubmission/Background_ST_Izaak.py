path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond_T2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="ST"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=3
hCPU="03:30:00"
hVMEM="5000M"
postFix="_Moriond"
dataSets = [
                       
       [ "ST_tW_top_5f_inclusiveDecays",
        [   "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext_0000.xml", ]],
       
       [ "ST_tW_antitop_5f_inclusiveDecays",
        [   "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_ext_0000.xml", ]],
                       
#        [ "ST_tW_top_5f_NoFullyHadronicDecays",
#         [   "ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1_0000.xml", ]],
#        
#        [ "ST_tW_antitop_5f_NoFullyHadronicDecays",
#         [   "ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1_0000.xml", ]],
#        
#        [ "ST_s-channel_4f_leptonDecays",
#         [   "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_0000.xml", ]],
            
       [ "ST_t-channel_antitop_4f_inclusiveDecays",
        [   "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_0000_0.xml",
            "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_0000_1.xml", ]],
            
       [ "ST_t-channel_top_4f_inclusiveDecays",
        [   "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_0000_0.xml",
            "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_0000_1.xml",
            "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1_0000_2.xml", ]],
        
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
