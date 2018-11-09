# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "" # extra label for opening file, saving plots to dir
plottag     = "_test" # extra label for image file
era         = "2017" #B-E"
luminosity  = 28.29 if "B-E" in era else 13.57 if "F" in era else 41.4 #86

# VERBOSITY
verbosity               = 1
verbositySampleTools    = 1
verbosityPlotTools      = 0
verbosityVariableTools  = 0
verbositySelectionTools = 0

# PLOTS OPTIONS
doStack             = True #and False
drawShifts          = True and False
useCutTree          = True and False
loadMacros          = True #and False
makePDF             = True and False
drawData            = True #and False

# DATACARD OPTIONS
doDatacard          = True and False
doNominal           = True #and False
doShifts            = True #and False
doTESscan           = True #and False
doTES               = True and False
doMES               = True and False # not for etau
doEES               = True #and False # not for mutau
doJTF               = True and False
doLTF               = True #and False
doJER               = True #and False
doJEC               = True #and False
doUncEn             = True #and False
doZpt               = True #and False

# SAMPLE OPTIONS
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeTT             = True #and False
mergeST             = True #and False
mergeVV             = True #and False
mergeTop            = True and False
splitDY             = True #and False
splitDYByDM         = True and False
splitTT             = True and False
splitST             = True and False
normalizeWJ         = True and False
doQCD               = True #and False
doFakeRate          = True and False # does not work for nanoAOD
doFakeFactor        = True and False
favSignals          = False
OSSS_ratio          = 1.00

# SAMPLES
isNanoAOD           = True #and False
NANOAOD             = "LQ_2017"
SFRAME              = "SFrameAnalysis_ltau2017"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/analysis/%s"%NANOAOD)
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")
#sys.path.append('/shome/ineuteli/analysis/CMSSW_8_1_0/src/CombineHarvester/LQ_2017/theory_LQ.py')

#### END SETTINGS ########################################################################

if not doShifts:
  doTES, doEES, doJTF, doJER, doJEC, doUncEn = False, False, False, False, False, False
splitTT = splitTT and not mergeTop
splitST = splitST and not mergeTop

# CATEGORIES / SELECTIONS
if channels[0]=='mutau':
  _weight            = "genWeight*weight*getPUWeight(Pileup_nTrueInt)*getLeptonTauFake(1,genPartFlav_2,eta_2)*(genPartFlav_2==5 ? 0.89 : 1)"
  baseline           = "q_1*q_2<0 && pfRelIso04_all_1<0.15 && idDecayMode_2==1 && idMVAoldDM2017v2_2>=16 && idAntiMu_2>=2 && idAntiEle_2>=1 && extramuon_veto==0 && extraelec_veto==0 && dilepton_veto==0"
else:
  _weight            = "genWeight*weight*getPUWeight(Pileup_nTrueInt)*getLeptonTauFake(2,genPartFlav_2,eta_2)*(genPartFlav_2==5 ? 0.89 : 1)*getTrigEff(pt_1,eta_1)"
  baseline           = "q_1*q_2<0 && pfRelIso03_all_1<0.10 && idDecayMode_2==1 && idMVAoldDM2017v2_2>=16 && idAntiMu_2>=1 && idAntiEle_2>=8 && extramuon_veto==0 && extraelec_veto==0 && dilepton_veto==0"
if doFakeFactor:
  plottag         += "_FF"
elif doQCD and not doFakeRate:
  plottag         += "_WJ-QCD"
#WJscale            = 1.136 if 'iso_2' in baseline else 1.086 if 'run2v2DBoldDM' in baseline else 1.082 if 'run2v1DBnewDM' in baseline else -1

selections  = [
#     sel("baseline",          "%s"       %(baseline)                                ),
#     sel("m_T<50GeV",         "%s && %s" %(baseline,"pfmt_1<50")                   ),
    sel("1b",                "%s && %s" %(baseline,"pt_1>30 && pt_2>50 && m_vis>95 && nbtag>0 && jpt_1>50")),
]
blind_dict = {
  "pt_1+pt_2+jpt_1":       ( 600, 10e10),
  "pt_1+pt_2+jpt_1+jpt_2": ( 600, 10e10),
}
PlotTools.linecolors[0] = kAzure+10
PlotTools.linecolors[1] = kRed

# VARIABLES
htbins = range(0,600,50) + range(600,800,100) + [800,1000,3000]
variables = [
#     var("m_vis",                                80,     0,  400, filename="$VAR", cbinning={'nbtag':(20,0,200),'m_vis>':(27,80,350)} ),
#     var("m_vis",                                40,     0, 1000, filename="$VAR_zoom", cbinning={'nbtag':(20,0,200)} ),
    var("pt_1+pt_2+jpt_1",                               htbins, filename="ST", title="scalar sum pt", logy=True, ymin=0.05 ),
#     var("pt_1+pt_2+jpt_1",                      40,     0, 2000, filename="ST_50", title="scalar sum pt", logy=True ),
#     var("pt_1+pt_2+jpt_1+jpt_2",                40,     0, 2000, filename="ST_2_50", title="scalar sum pt" ),
#     var("pt_1+pt_2+jpt_1+jpt_2",                         htbins, filename="ST_2", title="scalar sum pt" ),
#     var("dR_ll",                                30,     0,    6 ),
#     var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     var("met",                                  40,     0,  200 ),
#     var("metphi",                               35,  -3.5,  3.5 ),
#     var("npu",                                  40,     0,   80 ),
#     var("npv",                                  40,     0,   80 ),
#     var("rho",                                  70,     0,   70 ),
#     var("njets",                                 8,     0,    8 ),
#     var("ncjets",                                8,     0,    8 ),
#     var("nbtag",                                 7,     0,    7 ),
#     var("pt_1",                                 50,     0,  200, title="muon pt",  ctitle={'etau':"electron pt"}  ),
#     var("eta_1",                                26,  -2.6,  2.6, title="muon eta", ctitle={'etau':"electron eta"} ),
#     var("pt_2",                                 30,     0,  150, title="tau pt",   ctitle={'emu': "electron pt"}  ),
#     var("eta_2",                                26,  -2.6,  2.6, title="tau eta",  ctitle={'emu': "electron eta"} ),
#     #var("iso_1",                               100,     0,  0.5 ),
#     var("decayMode_2",                          14,     0,   14, position='center' ),
#     var("dzeta",                                50,  -150,  100 ), # filename="Dzeta"
#     var("pzetavis",                             50,     0,  200 ),
]

samplesB = [
    ('TT', "TTTo2L2Nu",                 "ttbar 2l2#nu",              88.29  ),
    ('TT', "TTToHadronic",              "ttbar hadronic",           377.96  ),
    ('TT', "TTToSemiLeptonic",          "ttbar semileptonic",       365.35  ),
    ('ST', "ST_t-channel_top",          "ST t-channel t",           136.02  ),
    ('ST', "ST_t-channel_antitop",      "ST t-channel at",           80.95  ),
    ('ST', "ST_tW_top",                 "ST tW",                     35.85  ),
    ('ST', "ST_tW_antitop",             "ST atW",                    35.85  ),
    #('WW', "WW_TuneCP5",                "WW",                        75.88  ),
    #('WZ', "WZ_TuneCP5",                "WZ",                        27.6   ),
    #('ZZ', "ZZ_TuneCP5",                "ZZ",                        12.14  ),
    ('WJ', "WJetsToLNu",                "W + jets",               52940.0   ),
    ('WJ', "W1JetsToLNu",               "W + 1J",                  8104.0   ),
    ('WJ', "W2JetsToLNu",               "W + 2J",                  2793.0   ),
    ('WJ', "W3JetsToLNu",               "W + 3J",                   992.5   ),
    ('WJ', "W4JetsToLNu",               "W + 4J",                   544.3   ),
    ('DY', "DYJetsToLL_M-10to50",       "Drell-Yan 10-50",        18610.0   ),
    ('DY', "DYJetsToLL_M-50",           "Drell-Yan 50",            5343.0   ),
    ('DY', "DY1JetsToLL_M-50",          "Drell-Yan 1J 50",          877.8   ),
    ('DY', "DY2JetsToLL_M-50",          "Drell-Yan 2J 50",          304.4   ),
    ('DY', "DY3JetsToLL_M-50",          "Drell-Yan 3J 50",          111.5   ),
]

xsections = {
  'SLQ-s': {  500:  0.17276,
             1000:  0.00351,
             1500:  0.000231893,
             2000:  2.83429e-05, },
  'VLQ-s': {  500:  100*0.01635,
             1000:  100*0.0002226,
             1500:  100*1.117e-05,
             2000:  100*9.842e-07, },
  'SLQ-p': {  500:  4.79e-01,
             1000:  5.03e-03,
             1500:  1.68e-04,
             2000:  8.00e-06, },
  'VLQ-p': {  500:  1.98e+01,
             1000:  1.93e-01,
             1500:  6.44e-03,
             2000:  3.29e-04, },
}

samplesS = [ ]
masses = [ 500, 1000, 1500, 2000 ]
if doDatacard:
  for mass in masses:
    samplesS.append(( 'LQ', "LQ3ToTauB_s-channel_M%d"%(mass),       "Scalar LQ, %d GeV"%(mass),      1.0  ))
    samplesS.append(( 'LQ', "LQ3ToTauB_pair_M%d"%(mass),            "Scalar LQ pair, %d GeV"%(mass), 1.0  ))
    samplesS.append(( 'LQ', "VectorLQ3ToTauB_s-channel_M%d"%(mass), "Vector LQ, %d GeV"%(mass),      1.0  ))
    samplesS.append(( 'LQ', "VectorLQ3ToTauB_pair_M%d"%(mass),      "Vector LQ pair, %d GeV"%(mass), 1.0  ))
  samplesS = sorted(samplesS,key=lambda x: x[1])
elif favSignals:
  for mass in [ 1000 ]:
    samplesS.append(( 'LQ', "LQ3ToTauB_s-channel_M%d"%(mass),       "Scalar LQ single, %d GeV"%(mass), xsections['SLQ-s'][mass]  ))
    samplesS.append(( 'LQ', "LQ3ToTauB_pair_M%d"%(mass),            "Scalar LQ pair, %d GeV"%(mass),   xsections['SLQ-p'][mass]  ))
    samplesS.append(( 'LQ', "VectorLQ3ToTauB_s-channel_M%d"%(mass), "Vector LQ single, %d GeV"%(mass), xsections['VLQ-s'][mass]  ))
    samplesS.append(( 'LQ', "VectorLQ3ToTauB_pair_M%d"%(mass),      "Vector LQ pair, %d GeV"%(mass),   xsections['VLQ-p'][mass]  ))
else:
  for mass in [ 1000 ]:
    samplesS.append(( 'LQ', "LQ3ToTauB_s-channel_M%d"%(mass),       "Scalar LQ, %d GeV"%(mass), xsections['SLQ-s'][mass] )) # -> b#tau
    samplesS.append(( 'LQ', "VectorLQ3ToTauB_s-channel_M%d"%(mass), "Vector LQ, %d GeV"%(mass), xsections['VLQ-s'][mass] ))

samplesD = {
    'mutau': ( 'SingleMuon',      "SingleMuon_Run2017",     "observed" ),
    'etau':  ( 'SingleElectron',  "SingleElectron_Run2017", "observed" ),
}

# SAMPLESET
makeNanoAODSamples(channels[0],samplesD,samplesB,samplesS,weight=_weight,binN_weighted=16,blind=blind_dict)
samples = SampleSet(samplesD,samplesB,samplesS,channel=channels[0],nanoAOD=True)
#samples.printTable()
if stitchWJ:       samples.stitch('W*Jets',        name_incl="WJ",  name="WJ"                                         )
if stitchDY50:     samples.stitch('DY*J*M-50',     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan M=50GeV"     )
#if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeDY:        samples.merge( 'DY',                             name="DY",          title="Drell-Yan"             )
#if mergeVV:        samples.merge( 'VV','WZ','WW','ZZ',              name="VV",          title="diboson"               )
if mergeST:        samples.merge( 'ST',                             name="ST",          title="single top"            )
if mergeTT:        samples.merge( 'TT',                             name="TT",          title="ttbar"                 )
if mergeTop:       samples.merge( 'TT','ST',                        name="top",         title="ttbar and single top"  )
elif splitTT:      samples.split('TT', [('TTT',"ttbar with real tau_h","genPartFlav_2==5"), ('TTJ',"ttbar other",     "genPartFlav_2!=5")]) #'ttbar j -> tau_h': "genPartFlav_2<5"
#if splitST:     samples.split('ST', [('STT',"single top with real tau_h',"genPartFlav_2==5"), ('STJ',"single top other","genPartFlav_2!=5")])
if splitDY:
  ZTT = "Z -> tau_{#mu}tau_{h}" if channels[0]=="mutau" else "Z -> tau_{e}tau_{h}"
  if doFakeFactor: samples.split('DY', [('ZTT',ZTT,  "genPartFlav_2==5"), ('ZL', "Drell-Yan with l -> tau_{h}","genPartFlav_2!=5")])
  #if doFakeFactor: samples.split('DY', [('ZTT',ZTT,  "genPartFlav_2==5"), ('ZL',"Drell-Yan with l -> tau_{h}","genPartFlav_2!=5")])
  else:            samples.split('DY', [('ZTT',ZTT,  "genPartFlav_2==5"), ('ZJ', "Drell-Yan other", "genPartFlav_2!=5")])
samples.printTable()
#samples.printSampleObjects()


