path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Moriond"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="ZZ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=5
hCPU="03:30:00"
hVMEM="5000M"
postFix="_Moriond" #"_ICHEP" #"_Moriond"
dataSets = [
       [ "ZZ_TuneCUETP8M1",
        [   "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_0.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_1.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_2.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_3.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_4.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_5.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_6.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_7.xml",
            "ZZ_TuneCUETP8M1_13TeV-pythia8_HLT1_0000_8.xml", ]],    
            ]
                
if "Moriond" in postFix: dataSets = [
        
       [ "ZZTo2L2Q_13TeV_nlo",
        [   "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0001_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0001_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0001_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0002_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0002_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0002_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0003_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0003_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0003_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0004_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0004_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0004_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0005_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0005_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0005_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0006_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0006_1.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0006_2.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0007_0.xml",
            "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0007_1.xml", ]],
            
       [ "ZZTo2Q2Nu_13TeV_nlo",
        [   "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
            "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml", ]],
            
       [ "ZZTo4Q_13TeV_nlo",
        [   "ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
            "ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml", ]],
            
       [ "ZZTo4L_13TeV_nlo",
        [   "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0000_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0000_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0000_2.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0001_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0001_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0001_2.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0002_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0002_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0002_2.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0003_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0003_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0003_2.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0004_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0004_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0004_2.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0005_0.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0005_1.xml",
            "ZZTo4L_13TeV-amcatnloFXFX-pythia8_V3_ext_0005_2.xml", ]],
            
#        [ "ZZTo4L_13TeV_powheg_pythia8",
#         [   "ZZTo4L_13TeV_powheg_pythia8_V2_0000_0.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0000_1.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0000_2.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0001_0.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0001_1.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0001_2.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0002_0.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0002_1.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0002_2.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0003_0.xml",
#             "ZZTo4L_13TeV_powheg_pythia8_V2_0003_1.xml", ]],
            
       [ "VVTo2L2Nu_13TeV_nlo",
        [   "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V1_0000.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0000_0.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0000_1.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0000_2.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0001_0.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0001_1.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0001_2.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0002_0.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0002_1.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0002_2.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0003_0.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0003_1.xml",
            "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_ext_0003_2.xml", ]],
        
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
