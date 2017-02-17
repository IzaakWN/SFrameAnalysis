path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="DY"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=8
hCPU="04:00:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP" #"_Moriond"
dataSets = [

       ["DYJetsToLL_M-50_TuneCUETP8M1",
        [   "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_reHLT_ext_0000.xml", ]],

       ["DY1JetsToLL_M-50_TuneCUETP8M1",
        [   "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000_0.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000_1.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000_2.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0001_0.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0001_1.xml", ]],

       ["DY2JetsToLL_M-50_TuneCUETP8M1",
        [   "DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000_0.xml",
            "DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000_1.xml", ]],

       ["DY3JetsToLL_M-50_TuneCUETP8M1",
        [   "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000.xml", ]],

       ["DY4JetsToLL_M-50_TuneCUETP8M1",
        [   "DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_HLT1_0000.xml", ]],

            ]



    ################
    #  Moriond  #
    ################
                
if "Moriond" in postFix: dataSets = [
       
       [ "DYJetsToLL_M-10to50_TuneCUETP8M1", # M-10to50
        [   "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_0.xml",
            "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_1.xml", ]],
         
       [ "DY1JetsToLL_M-10to50_TuneCUETP8M1", # M-10to50
        [   "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_1.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_2.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0009_0.xml",
            "DY1JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0009_1.xml", ]],
         
       [ "DY2JetsToLL_M-10to50_TuneCUETP8M1", # M-10to50
        [   "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0000_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0001_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0002_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0003_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0004_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0005_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0006_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0007_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0008_2.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0009_0.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0009_1.xml",
            "DY2JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V3_0009_2.xml", ]],
         
       [ "DY3JetsToLL_M-10to50_TuneCUETP8M1", # M-10to50
        [   "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_0.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_1.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_2.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_0.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_1.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_2.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_0.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_1.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_2.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0003_0.xml",
            "DY3JetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0003_1.xml", ]],
         
       [ "DYJetsToLL_M-50_TuneCUETP8M1",
        [   "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0000_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0000_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0000_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0001_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0001_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0001_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0002_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0002_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0002_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0003_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0003_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0003_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0004_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0004_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0004_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0005_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0005_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0005_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0006_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0006_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0006_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0007_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0007_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0007_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0008_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0008_1.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0008_2.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0009_0.xml",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_ext_retry_0009_1.xml", ]],
        
       [ "DY1JetsToLL_M-50_TuneCUETP8M1",
        [   "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_0.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_1.xml",
            "DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_2.xml", ]],
        
       [ "DY2JetsToLL_M-50_TuneCUETP8M1",
        [   "DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_0000.xml", ]],
        
       [ "DY3JetsToLL_M-50_TuneCUETP8M1",
        [   "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_0.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_1.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0000_2.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_0.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_1.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0001_2.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_0.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_1.xml",
            "DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V2_0002_2.xml", ]],
        
       [ "DY4JetsToLL_M-50_TuneCUETP8M1",
        [   "DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V1_0000.xml", ]],
             
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
                ["doZpt","true"], # only to LO DY!
             ]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems
