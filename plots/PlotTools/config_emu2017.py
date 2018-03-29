# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "_2017_V2" # extra label for opening file, saving plots to dir
plotlabel   = "_newJEC" # extra label for image file
luminosity  = 41.86

# VERBOSITY
verbosity               = 1
verbositySampleTools    = 1
verbosityPlotTools      = 0
verbosityVariableTools  = 0
verbositySelectionTools = 0

# PLOTS OPTIONS
doStack             = True #and False
drawShifts          = True #and False
useCutTree          = True #and False

# DATACARD OPTIONS
doDatacard          = True and False
recreateDC          = True #and False
doNominal           = True #and False
doTESscan           = True and False # not for emu
doTES               = True and False
doEES               = True #and False
doJTF               = True #and False
doJER               = True #and False
doJEC               = True #and False

# SAMPLE OPTIONS
splitDY             = True #and False
splitTT             = True #and False
splitST             = True and False
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeTT             = True #and False
mergeST             = True #and False
mergeVV             = True #and False
normalizeWJ         = True and False # not for emu
doQCD               = True #and False
OSSS_ratio          = 1.06

# SAMPLES
SFRAME              = "SFrameAnalysis_ltau2017"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_emu2017")
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")

#### END SETTINGS ########################################################################


channels = [
    "emu",
]
if not normalizeWJ and "emu" not in channels: plotlabel+="_noWJrenorm"

# CATEGORIES / SELECTIONS
_weight            = "genweight*puweight*trigweight_1*idisoweight_1*idisoweight_2"
#weight_           += "*ttptweight"; plotlabel+="_ttptweight"
isocuts            = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
isocuts_emu        = "iso_1<0.20 && iso_2<0.15"
vetos              = "lepton_vetos==0"
vetos_emu          = "extraelec_veto==0 && extramuon_veto==0"
isocuts            = isocuts_emu
vetos              = vetos_emu
baseline           = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%(isocuts,vetos)
baseline_noIso2    = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%("iso_1<0.15",vetos)
baselineSS         = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2>0"%(isocuts,vetos)
baseline_antiIso   = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2<0"%("iso_1>0.15 && iso_1<0.50 && iso_2==1",vetos)
baselineSS_antiIso = "channel>0 && %s && %s && decayMode_2<11 && q_1*q_2>0"%("iso_1>0.15 && iso_1<0.50 && iso_2==1",vetos)
ZTTregion          = "45<m_vis && m_vis<85 && pt_2>30 && nbtag==0 && pzeta_disc>-30"
baseline           = baseline.replace("Mode_2","Mode_3")
baseline_noIso2    = baseline_noIso2.replace("Mode_2","Mode_3")

selections  = [
#     sel("no cuts",                                ""                                                 ),
#     sel("baseline, no tau ID",                    "%s"       %(baseline_noIso2)                      ),
#     sel("baseline, no tau ID, m_T<50GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1<50")          ),
#     sel("baseline, no tau ID, m_T>80GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1>80")           ),
#     sel("ZTT enriched, no tau ID",                "%s && %s" %(baseline, ZTTregion)                   ),
#     sel("baseline",                               "%s"       %(baseline)                              ),
#     sel("baseline, tight",                        "%s"       %(baseline)                              ),
#     sel("baseline, tight, m_T<50GeV",             "%s && %s" %(baseline,"pfmt_1<50")                  ),
#     sel("baseline, tight, m_T>80GeV",             "%s && %s" %(baseline,"pfmt_1>80")                  ),
#     sel("ZTT enriched, tight",                    "%s && %s" %(baseline, ZTTregion)                   ),
#     sel("baseline, m_T<50GeV",                    "%s && %s" %(baseline,"pfmt_1<50")                     ),
#     sel("baseline, m_T<50GeV, DM0",               "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==0")   ),
#     sel("baseline, m_T<50GeV, DM1",               "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==1")   ),
#     sel("baseline, m_T<50GeV, DM10",              "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==10")  ),
#     sel("baseline, >=1b",                         "%s && %s" %(baseline,"nbtag>0")                       ),
#     sel("baseline, >=1b, 20",                     "%s && %s" %(baseline,"nbtag20>0")                     ),
    sel("baseline, >=1b, no tau ID", "%s && %s" %(baseline,"nbtag_noTau>0 && againstLepton_3==1") ),
#     sel("baseline, >=1b, m_T<100GeV", "%s && %s" %(baseline,"nbtag_noTau>0 && againstLepton_3==1 && pfmt_1<100") ),
    sel("baseline, >=1b, tight",      "%s && %s" %(baseline,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3==1") ),
#     sel("baseline, >=1b, Tight fail", "%s && %s" %(baseline,"nbtag_noTau>0 && againstLepton_3==1 && byTightIsolationMVArun2v1DBoldDMwLT_3!=1") ),
#     sel("baseline, >=1b, VTight",     "%s && %s" %(baseline,"nbtag_noTau>0 && againstLepton_3==1 && byVTightIsolationMVArun2v1DBoldDMwLT_3==1") ),
]


# VARIABLES
variables = [
    var("m_vis",                                40,     0,  200, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     ###var("m_sv",                              40,     0,  200 ),
#     var("m_2",                                  50,     0,    2, title="m_e" ),
#     var("m_2",                                  75,     0,    3, title="m_e", logy=True, filename="$NAME_log" ),
#     ###var("ht",                                50,     0,  500 ),
#     var("dR_ll",                                30,     0,    6 ),
    var("pfmt_1",                               40,     0,  200, title="m_t(mu,MET)", ctitle={'etau':"m_t(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     var("met",                                  40,     0,  200 ),
#     var("metphi",                               36,  -3.5,  3.5 ),
    var("gen_match_2",                          9,    -1,    8, position='center', title="electron gen. match" ),
    var("gen_match_3",                          9,    -1,    8, position='center', title="tau gen. match" ),
#     ###var("puweight",                            100,     0,  200, logy=True ),
#     var("npu",                                  40,     0,   80 ),
#     var("npv",                                  40,     0,   80 ),
#     var("rho",                                  70,     0,   70 ),
#     var("njets",                                 8,     0,    8 ),
#     var("nbtag",                                 7,     0,    7 ),
#     ###var("nbtag20",                               7,     0,    7 ),
#     var("pt_1",                                 50,     0,  200, title="muon pt",  ctitle={'etau':"electron pt"}  ),
#     var("eta_1",                                26,  -2.6,  2.6, title="muon eta", ctitle={'etau':"electron eta"} ),
#     var("pt_2",                                 30,     0,  150, title="tau pt",   ctitle={'emu': "electron pt"}  ),
#     var("eta_2",                                26,  -2.6,  2.6, title="tau eta",  ctitle={'emu': "electron eta"} ),
#     var("pt_3",                                 30,     0,  150, title="tau pt",  ),
#     var("eta_3",                                26,  -2.6,  2.6, title="tau eta", ),
#     #var("iso_1",                               100,     0,  0.5 ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_3",  50,   0.8,  1.0, filename="$NAME_zoom0p8", veto=['decayMode_3==11'], position='centerleft', cbinning={'iso_2.*nbtag':(20,0.8,1.0)} ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_3",  50,  -1.0,  1.0, logy=True, veto=['by.*IsolationMVA.*_3.*decayMode_3==11'], position='centerleft' ),
#     ###var("byIsolationMVArun2v1DBoldDMwLTraw_2",  30,  -0.2,  1.0, filename="$NAME_zoom-0p2", position='centerleft' ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_3",  50,   0.8,  1.0, filename="$NAME_zoom0p8", position='centerleft' ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_3",  50,  -1.0,  1.0, logy=True, position='centerleft' ),
#     var("chargedPionPt_3",                      80,     0,  100 ),
#     var("neutralPionPt_3",                      80,     0,  100 ),
#     var("chargedIsoPtSum_3",                    80,     0,  100, logy=True, cbinning={'by.*IsolationMVA.*_3':(50,0,50)} ),
#     var("neutralIsoPtSum_3",                    80,     0,  100, logy=True, cbinning={'by.*IsolationMVA.*_3':(80,0,80)} ),
#     var("chargedIsoPtSumdR03_3",                80,     0,  100, logy=True, cbinning={'by.*IsolationMVA.*_3':(50,0,50)} ),
#     var("neutralIsoPtSumdR03_3",                80,     0,  100, logy=True, cbinning={'by.*IsolationMVA.*_3':(80,0,80)} ),
#     var("puCorrPtSum_3",                        70,     0,   70 ),
#     var("photonPtSumOutsideSignalCone_3",       60,     0,   30, logy=True ),
#     var("photonPtSumOutsideSignalConedR03_3",   60,     0,   30, logy=True ),
#     var("byPhotonPtSumOutsideSignalCone_3",      4,     0,    4 ),
#     var("nPhoton_3",                            12,     0,   12 ),
#     var("ptWeightedDetaStrip_3",                60,     0,  0.6, logy=True ),
#     var("ptWeightedDphiStrip_3",                60,     0,  0.6, logy=True ),
#     var("ptWeightedDrSignal_3",                 60,     0,  0.6, logy=True ),
#     var("ptWeightedDrIsolation_3",              60,     0,  0.6, logy=True ),
#     var("leadingTrackChi2_3",                   60,     0,    6 ),
#     var("leadingTrackPt_3",                     70,     0,   70 ),
#     var("eRatio_3",                             51, -0.01, 1.01, logy=True, cbinning={'by.*IsolationMVA.*_3':(38,-0.01,1.01)} ),
#     var("dxy_Sig_3",                            65,    -3,  3.5, cbinning={'by.*IsolationMVA.*_3':(40,-4.0,4.0)} ),
#     var("ip3d_3",                               50, -0.08, 0.08 ),
#     var("ip3d_Sig_3",                           60,    -6,    6, cbinning={'by.*IsolationMVA.*_3':(70,-6,8)} ),
#     var("hasSecondaryVertex_3",                  4,     0,    4 ),
#     var("decayDistMag_3",                       50,     0,  1.5, logy=True ),
#     var("flightLenthSig_3",                     75,     0,   15, cbinning={'by.*IsolationMVA.*_3':(50,0,20)} ),
#     #var("d0_3",                                 60, -0.04, 0.04, title="tau d_0", ctitle={'etau':"electron d_0"} ),
#     #var("dz_3",                                 60,     0, 0.04, title="tau d_z", ctitle={'etau':"electron d_z"} ),
#     var("dzeta",                                50,  -150,  100 ), # filename="Dzeta"
#     var("pzetavis",                             50,     0,  200 ),
]
# for p in [("b",1),("b",2),("j",1),("j",2)]:
#     variables.append(var( "%spt_%i"  % p,      50,    0,   250  ))
#     variables.append(var( "%seta_%i" % p,      50, -5.0,   5.0  ))

samplesB = [
    #("TT", "TT_TuneCUETP8M2T4",                        "ttbar",                   831.76   ), # {'extraweight':_weight+"*ttptweight_runI/ttptweight"}
    ("TT", "TTTo2L2Nu",                                "ttbar 2l2#nu",             87.31   ),
    ("TT", "TTToHadronic",                             "ttbar hadronic",          380.1    ),
    ("TT", "TTToSemiLeptonic",                         "ttbar semileptonic",      364.4    ),
    ("ST", "ST_t-channel_top_4f_inclusiveDecays",      "ST t-channel t",           136.02  ),
    ("ST", "ST_t-channel_antitop_4f_inclusiveDecays",  "ST t-channel at",           80.95  ),
    ("ST", "ST_tW_top_5f_inclusiveDecays",             "ST tW",                     35.60  ),
    ("ST", "ST_tW_antitop_5f_inclusiveDecays",         "ST atW",                    35.60  ),
    ("WW", "WW_TuneCP5",                               "WW",                        63.21  ),
    ("WZ", "WZ_TuneCP5",                               "WZ",                        22.82  ),
    ("ZZ", "ZZ_TuneCP5",                               "ZZ",                        10.32  ),
    ("WJ", "WJetsToLNu",                               "W + jets",               50380.0   ), # LO 50380.0; NLO 61526.7
    ("WJ", "W1JetsToLNu",                              "W + 1J",                  9644.5   ),
    ("WJ", "W2JetsToLNu",                              "W + 2J",                  3144.5   ),
    ("WJ", "W3JetsToLNu",                              "W + 3J",                   954.8   ),
    ("WJ", "W4JetsToLNu",                              "W + 4J",                   485.6   ),
    ("DY", "DYJetsToLL_M-50_TuneCP5",                  "Drell-Yan 50",            4954.0   ), # LO 4954.0; NLO 5765.4
    ("DY", "DY1JetsToLL_M-50_TuneCP5",                 "Drell-Yan 1J 50",         1012.5   ),
    ("DY", "DY2JetsToLL_M-50_TuneCP5",                 "Drell-Yan 2J 50",          332.8   ),
    ("DY", "DY3JetsToLL_M-50_TuneCP5",                 "Drell-Yan 3J 50",          101.8   ),
]

samplesS = [
    #( "LowMass", "LowMass_28GeV_DiTauResonance",      "signal",               1000.0   ),
]

samplesD = {
    "mutau" :  ( "SingleMuon",      "SingleMuon_Run2017",     "single muon"     ),
    #"etau" :  ( "SingleElectron",   "SingleElectron_Run2017", "single electron" ),
    "emu"   :  ( "SingleMuon",      "SingleMuon_Run2017",     "single muon"     ),
}

# SAMPLESET
makeSFrameSamples(samplesD,samplesB,samplesS,weight=_weight,binN_weighted=10)
samples = SampleSet(samplesD,samplesB,samplesS)
#samples.printTable()
if stitchWJ:       samples.stitch("W*Jets",        name_incl="WJ",  name="WJ"                                         )
if stitchDY50:     samples.stitch("DY*J*M-50",     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan M>50GeV"     )
#if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeVV:        samples.merge( "VV","VV","WZ","WW","ZZ",         name="VV",          title="diboson"               )
if mergeST:        samples.merge( "ST",                             name="ST",          title="single top"            )
if mergeTT:        samples.merge( "TT",                             name="TT",          title="ttbar"                 )
if splitDY:        samples.splitSample("DY",{'Z -> tautau':           "gen_match_3==5", 'Drell-Yan other': "gen_match_3!=5" })
if splitTT:        samples.splitSample("TT",{'ttbar with real tau_h': "gen_match_3==5", 'ttbar other':     "gen_match_3!=5" }) #'ttbar j -> tau_h': "gen_match_2<5"
samples.printTable()
#samples.printSampleObjects()

# SHIFT
samplesB_TESscan = { }
samplesB_TESUp, samplesB_TESDown, samplesB_EESUp, samplesB_EESDown, samplesB_JTFUp, samplesB_JTFDown = [ ], [ ], [ ], [ ], [ ], [ ]
if doEES:
  samplesB_EESUp   = samples.shiftSample(['TT','ST'],"_EES1p03","  +3% EES",    filter=not doStack)
  samplesB_EESDown = samples.shiftSample(['TT','ST'],"_EES0p97","  -3% EES",    filter=not doStack)
if doJTF:
  #samplesB_JTFUp   = samples.shiftSample(['TT','ST'],"_JTF1p15"," +15% JTF ES", filter=not doStack, title_veto="real")
  #samplesB_JTFDown = samples.shiftSample(['TT','ST'],"_JTF0p85"," -15% JTF ES", filter=not doStack, title_veto="real")
  samplesB_JTFUp   = samples.shiftSample(['TT','ST'],"_JTF1p10"," +10% JTF ES", filter=not doStack, title_veto="real")
  samplesB_JTFDown = samples.shiftSample(['TT','ST'],"_JTF0p90"," -10% JTF ES", filter=not doStack, title_veto="real")
  #samplesB_EESUp.printTable()
  #samplesB_JTFDown.printTable()
  #samplesB_JTFUp.printTable()
  #samplesB_JTFUp.printSampleObjects()


