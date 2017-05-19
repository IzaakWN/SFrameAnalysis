path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond_T2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WJ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=12
hCPU="04:00:00"
hVMEM="5000M"
postFix="_Moriond"
dataSets = [
            
       [ "WJetsToLNu_TuneCUETP8M1",
        [   #"WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_0000.xml",
            "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
            "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml",
            "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_0000_0.xml",
            "WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_0000_1.xml", ]],

        [ "W1JetsToLNu_TuneCUETP8M1",
         [  "W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
            "W1JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],

        [ "W2JetsToLNu_TuneCUETP8M1",
         [  "W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
            "W2JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml", ]],

        [ "W3JetsToLNu_TuneCUETP8M1",
         [  "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0001_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0001_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0001_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0002_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0002_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0002_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0003_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0003_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0003_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0004_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0004_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0004_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0005_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0005_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0005_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0006_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0006_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0006_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0007_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0007_1.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0007_2.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0008_0.xml",
            "W3JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0008_1.xml", ]],

        [ "W4JetsToLNu_TuneCUETP8M1",
         [  "W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_0000.xml",
            "W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_additional_0000.xml",
            "W4JetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_ext_0000.xml", ]], # only in postMoriond
            
            ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","false"],
                ["doRecoilCorr","true"],
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
