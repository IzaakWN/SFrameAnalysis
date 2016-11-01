path2xml="$SFRAME_DIR/../BatchSubmission/xmls_Izaak"
path2tmp="$SFRAME_DIR/../AnalysisTemp"
jobName="WW"
outDir="$SFRAME_DIR/../AnalysisOutput/" + jobName
cycleName="TauTauAnalysis"
nEventsMax=-1
#nEventsMax=200
nProcesses=1
nFiles=1
hCPU="03:30:00"
hVMEM="5000M"
postFix = ""
label = "_triggerless"
dataSets = [
                
               [ "WWTo1L1Nu2Q"+label,
                [   "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_0.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_1.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_10.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_11.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_12.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_13.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_14.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_15.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_16.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_17.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_18.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_19.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_2.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_20.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_21.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_22.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_23.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_24.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_25.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_26.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_27.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_28.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_29.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_3.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_30.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_31.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_32.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_33.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_34.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_35.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_36.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_37.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_38.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_39.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_4.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_40.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_41.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_42.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_43.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_5.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_6.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_7.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_8.xml",
                    "WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_9.xml", ]],
                    
               [ "WWTo4Q_4f"+label,
                [   "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_0.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_1.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_10.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_100.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_101.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_102.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_103.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_104.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_105.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_106.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_107.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_108.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_109.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_11.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_110.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_111.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_112.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_113.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_114.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_115.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_116.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_117.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_118.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_119.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_12.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_120.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_121.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_122.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_123.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_124.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_125.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_126.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_127.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_128.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_129.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_13.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_130.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_131.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_132.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_133.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_134.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_135.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_136.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_137.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_138.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_139.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_14.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_140.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_141.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_142.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_143.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_144.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_145.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_146.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_147.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_148.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_149.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_15.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_150.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_151.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_152.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_153.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_154.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_155.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_156.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_157.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_158.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_159.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_16.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_160.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_161.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_162.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_163.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_164.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_165.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_166.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_167.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_168.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_169.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_17.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_170.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_171.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_172.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_173.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_174.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_175.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_176.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_177.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_178.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_179.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_18.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_180.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_181.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_182.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_183.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_184.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_185.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_186.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_187.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_188.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_189.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_19.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_190.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_191.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_192.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_193.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_194.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_195.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_196.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_197.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_198.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_199.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_2.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_20.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_200.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_201.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_202.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_203.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_204.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_205.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_206.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_207.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_208.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_209.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_21.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_210.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_211.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_212.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_213.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_214.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_215.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_216.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_217.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_218.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_219.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_22.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_220.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_221.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_222.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_223.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_224.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_225.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_226.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_227.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_228.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_229.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_23.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_230.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_231.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_232.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_233.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_234.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_235.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_236.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_237.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_238.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_239.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_24.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_240.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_241.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_242.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_243.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_244.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_245.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_246.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_247.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_25.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_26.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_27.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_28.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_29.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_3.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_30.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_31.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_32.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_33.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_34.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_35.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_36.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_37.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_38.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_39.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_4.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_40.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_41.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_42.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_43.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_44.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_45.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_46.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_47.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_48.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_49.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_5.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_50.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_51.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_52.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_53.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_54.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_55.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_56.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_57.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_58.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_59.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_6.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_60.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_61.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_62.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_63.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_64.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_65.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_66.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_67.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_68.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_69.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_7.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_70.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_71.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_72.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_73.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_74.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_75.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_76.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_77.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_78.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_79.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_8.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_80.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_81.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_82.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_83.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_84.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_85.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_86.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_87.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_88.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_89.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_9.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_90.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_91.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_92.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_93.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_94.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_95.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_96.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_97.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_98.xml",
                    "WWTo4Q_4f_13TeV_amcatnloFXFX_madspin_pythia8_HLT1_0000_99.xml", ]],
                    
           ]

userItems = [ 
                ["IsData","false"],
                ["IsSignal","false"],
                ["doSVFit","false"],
             ]

jobOptionsFile2=open("AnalysisOptions.py", 'r')
command2=""
for i in [o for o in jobOptionsFile2.readlines()]:
    if ("#E" + "nd") in i : break
    command2+=i
jobOptionsFile2.close()
exec command2
userItems += AddUserItems

inputTrees=["ntuplizer/tree"]
outputTrees=["tree"]