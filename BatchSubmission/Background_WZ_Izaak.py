path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WZ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=8
hCPU="03:30:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP" #"_Moriond"
dataSets = [             
       [ "WZ_TuneCUETP8M1",
        [   "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_0.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_1.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_2.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_3.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_4.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_5.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_6.xml",
            "WZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_7.xml", ]],    
            ]
                
if "Moriond" in postFix: dataSets = [
              
       [ "WZTo3LNu_TuneCUETP8M1_13TeV_nlo",
        [   "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0000_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0000_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0000_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0001_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0001_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0001_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0002_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0002_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0002_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0003_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0003_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0003_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0004_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0004_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0004_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0005_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0005_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0005_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0006_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0006_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0006_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0007_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0007_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0007_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0008_0.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0008_1.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0008_2.xml",
            "WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_V2_0009.xml", ]],
                          
       [ "WZTo1L1Nu2Q_13TeV_nlo",
        [   "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
            "WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml", ]],
                          
       [ "WZTo1L3Nu_13TeV_nlo",
        [   "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
            "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml",
            "WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_2.xml", ]],
        
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
