path2xml="$SFRAME_DIR/../BatchSubmission/xmls_postMoriond_T2"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="ZZ"
outDir="/scratch/$USER/SFrameAnalysis/AnalysisOutput/"+jobName #"$SFRAME_DIR/../AnalysisOutput/"+jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=4
hCPU="04:30:00"
hVMEM="5000M"
postFix="_Moriond"
dataSets = [
        
#        [ "ZZTo2L2Q_13TeV_nlo",
#         [   "ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_0000.xml", ]],
            
     # [ "ZZTo2Q2Nu_13TeV_nlo",
     #  [   "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_0.xml",
     #      "ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8_V2_0000_1.xml", ]],
        
     # [ "ZZTo4Q_13TeV_nlo",
     #  [   "ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8_0000_0.xml",
     #      "ZZTo4Q_13TeV_amcatnloFXFX_madspin_pythia8_0000_1.xml", ]],
            
#        [ "ZZTo4L_13TeV_nlo",
#         [   "ZZTo4L_13TeV-amcatnloFXFX-pythia8_ext_0000.xml", ]],
            
     # [ "ZZTo4L_13TeV_powheg_pythia8",
     #  [   "ZZTo4L_13TeV_powheg_pythia8_0000.xml", ]],
            
       [ "VVTo2L2Nu_13TeV_nlo",
        [   "VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8_0000.xml", ]],
        
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
