# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "_2017_V2_full_noRC" # extra label for opening file, saving plots to dir
plottag     = "_full_noRC" #_ZptWeights  # extra label for image file
era         = "2017"
luminosity  = 28.29 if "B-E" in era else 13.57 if "F" in era else 41.4 #86

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
loadMacros          = True #and False
makePDF             = True and False
onlyDY              = True and False
drawData            = True #and False

# DATACARD OPTIONS
doDatacard          = True and False
doNominal           = True #and False
doShifts            = True and False
doTESscan           = True and False # not for emu
doTES               = True and False # not for emu
doEES               = True and False
doJTF               = True and False
doJER               = True and False
doJEC               = True and False
doUncEn             = True and False

# SAMPLE OPTIONS
splitDY             = True and False
splitTT             = True and False
splitST             = True and False
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeTT             = True #and False
mergeST             = True #and False
mergeVV             = True #and False
normalizeWJ         = True and False # not for emu
doQCD               = True and False
OSSS_ratio          = 1.06

# SAMPLES
SFRAME              = "SFrameAnalysis_ltau2017"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_mumu2017")
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")

#### END SETTINGS ########################################################################


channels = [
    'mumu',
]

# CATEGORIES / SELECTIONS
_weight            = "genweight*puweight*trigweight_1*idisoweight_1*idisoweight_2" #*getZpt_2017(m_genboson,pt_genboson) #*zptweight" *getZpt_IWN(m_genboson,pt_genboson)
isocuts_mumu       = "iso_1<0.15 && iso_2<0.15"
vetos              = "lepton_vetos==0"
vetos_mumu         = "extraelec_veto==0 && extramuon_veto==0"
isocuts            = isocuts_mumu
vetos              = vetos_mumu
baseline           = "%s && %s && q_1*q_2<0"%(isocuts_mumu,vetos_mumu)
ZMMregion          = "70<m_vis && m_vis<110"
tau_T              = "byTightIsolationMVArun2v1DBoldDMwLT_3==1"
tau_VLnT           = "byTightIsolationMVArun2v1DBoldDMwLT_3!=1 && byVLooseIsolationMVArun2v1DBoldDMwLT_3==1"
if "B-E" in era:
  baseline        += " && (!isData || run<=304826)"
  #_weight          = _weight.replace('puweight',"puweightBtoF")
  plottag         += "_EraBtoE"
if "F" in era:
  baseline        += " && (!isData || run>=304911)"
  #_weight = _weight.replace('puweight',"puweightF")
  plottag         += "_EraF"

selections  = [
#     sel("no cuts",                                ""                                              ),
#     sel("baseline, no tau ID",                    "%s"       %(baseline_noIso2)                   ),
#     sel("baseline, no tau ID, m_T<50GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1<50")       ),
#     sel("baseline, no tau ID, m_T>80GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1>80")       ),
#     sel("ZTT enriched, no tau ID",                "%s && %s" %(baseline, ZMMregion)               ),
#     sel("ZMM region",                             "%s && %s" %(baseline,ZMMregion), title="Z -> mumu region" ),
    sel("dimuon",                                 "%s && %s" %(baseline,"m_vis>20"), title="Z -> mumu region" ),
#     sel("ZMM region, tau tight",                  "%s && %s && %s" %(baseline,ZMMregion,tau_T)    ),
#     sel("ZMM region, tau VL && !T",               "%s && %s && %s" %(baseline,ZMMregion,tau_VLnT) ),
#     sel("baseline, tight, m_T<50GeV",             "%s && %s" %(baseline,"pfmt_1<50")              ),
#     sel("baseline, tight, m_T>80GeV",             "%s && %s" %(baseline,"pfmt_1>80")              ),
]


# VARIABLES
variables = [
#     var("m_vis",                                30,     60,  120, title="dimuon mass m_mumu", filename="m_mumu"      ),
#     var("m_vis",                                44,     80,  102, title="dimuon mass m_mumu", filename="m_mumu_zoom", position="x=0.65" ),
#     var("pt_ll",                                50,      0,  200, title="dimuon pt" ),
#     var("m_2",                                  50,     0,    2, title="m_e" ),
#     var("m_2",                                  75,     0,    3, title="m_e", logy=True, filename="$NAME_log" ),
#     var("pfmt_1",                               40,     0,  200, title="m_t(mu,MET)", ctitle={'etau':"m_t(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     var("met",                                  40,     0,  200 ),
#     var("npu",                                  40,     0,   80 ),
#     var("npv",                                  40,     0,   80 ),
    var("njets",                                 8,     0,    8 ),
    var("ncjets",                                8,     0,    8 ),
    var("nfjets",                                8,     0,    8 ),
#     var("nbtag",                                 7,     0,    7 ),
#     var("pt_1",                                 50,     0,  200, title="leading muon pt"     ),
#     var("eta_1",                                26,  -2.6,  2.6, title="leading muon eta"    ),
#     var("pt_2",                                 35,     0,  140, title="subleading muon pt"  ),
#     var("eta_2",                                26,  -2.6,  2.6, title="subleading muon eta" ),
#     var("pt_3",                                 30,     0,  150, title="tau pt",  ),
#     var("eta_3",                                26,  -2.6,  2.6, title="tau eta", ),
#     #var("iso_1",                               100,     0,  0.5 ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_3",  50,   0.8,  1.0, filename="$NAME_zoom0p8", veto=['decayMode_3==11'], position='centerleft', cbinning={'iso_2.*nbtag':(20,0.8,1.0)} ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_3",  50,  -1.0,  1.0, logy=True, veto=['by.*IsolationMVA.*_3.*decayMode_3==11'], position='centerleft' ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_3",  50,   0.8,  1.0, filename="$NAME_zoom0p8", position='centerleft' ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_3",  50,  -1.0,  1.0, logy=True, position='centerleft' ),
#     var("dzeta",                                50,  -150,  100 ), # filename="Dzeta"
#     var("pzetavis",                             50,     0,  200 ),
#     var("(pt_ll-pt_genboson)/pt_genboson",     200,   -1.0, 1.0,  title="boson pt resolution",   filename="pt_boson_res",     units=""          ),
#     var("(pt_ll-pt_genboson)/pt_genboson",     400,   -1.5,   6,  title="boson pt resolution",   filename="pt_boson_res_log", units="", logy=True, ymin=100 ),
#     var("(m_vis-m_genboson)/m_genboson",       200,   -0.5, 0.5,  title="boson mass resolution", filename="m_boson_res",      units=""          ),
#     var("(m_vis-m_genboson)/m_genboson",       400,   -1.5,   6,  title="boson mass resolution", filename="m_boson_res_log",  units="", logy=True, ymin=100 ),
]

samplesB = [
    
#     ("WJ", "WJetsToLNu",                               "W + jets",             50380.0   ), # LO 50380.0; NLO 61526.7
#     ("WJ", "W1JetsToLNu",                              "W + 1J",                9644.5   ),
#     ("WJ", "W2JetsToLNu",                              "W + 2J",                3144.5   ),
#     ("WJ", "W3JetsToLNu",                              "W + 3J",                 954.8   ),
#     ("WJ", "W4JetsToLNu",                              "W + 4J",                 485.6   ),
#     ("ST", "ST_t-channel_top_4f_inclusiveDecays",      "ST t-channel t",         136.02  ),
#     ("ST", "ST_t-channel_antitop_4f_inclusiveDecays",  "ST t-channel at",         80.95  ),
#     ("ST", "ST_tW_top_5f_inclusiveDecays",             "ST tW",                   35.60  ),
#     ("ST", "ST_tW_antitop_5f_inclusiveDecays",         "ST atW",                  35.60  ),
#     ("WW", "WW_TuneCP5",                               "WW",                      63.21  ),
#     ("WZ", "WZ_TuneCP5",                               "WZ",                      22.82  ),
#     ("ZZ", "ZZ_TuneCP5",                               "ZZ",                      10.32  ),
#     ("TT", "TTTo2L2Nu",                                "ttbar 2l2#nu",            87.31  ),
#     ("TT", "TTToHadronic",                             "ttbar hadronic",         380.1   ),
#     ("TT", "TTToSemiLeptonic",                         "ttbar semileptonic",     364.4   ),
#     ("DY", "DYJetsToLL_M-10to50_TuneCP5",              "Drell-Yan 10-50",      21658.0,  ),#{'extraweight':"getZpt_IWN(m_genboson,pt_genboson)"} ), # LO 18610.0; NLO 21658.0
#     ("DY", "DYJetsToLL_M-50_TuneCP5",                  "Drell-Yan 50",          4954.0,  ),#{'extraweight':"getZpt_IWN(m_genboson,pt_genboson)"} ), # LO  4954.0; NLO  5765.4
#     ("DY", "DY1JetsToLL_M-50_TuneCP5",                 "Drell-Yan 1J 50",       1012.5,  ),#{'extraweight':"getZpt_IWN(m_genboson,pt_genboson)"} ),
#     ("DY", "DY2JetsToLL_M-50_TuneCP5",                 "Drell-Yan 2J 50",        332.8,  ),#{'extraweight':"getZpt_IWN(m_genboson,pt_genboson)"} ),
#     ("DY", "DY3JetsToLL_M-50_TuneCP5",                 "Drell-Yan 3J 50",        101.8,  ),#{'extraweight':"getZpt_IWN(m_genboson,pt_genboson)"} ),
    
    ("WJ", "WJetsToLNu",                               "W + jets",             52940.0   ), # LO 50380.0; NLO 61526.7
    ("WJ", "W1JetsToLNu",                              "W + 1J",                8104.0   ),
    ("WJ", "W2JetsToLNu",                              "W + 2J",                2793.0   ),
    ("WJ", "W3JetsToLNu",                              "W + 3J",                 992.5   ),
    ("WJ", "W4JetsToLNu",                              "W + 4J",                 544.3   ),
    ("ST", "ST_t-channel_top_4f_inclusiveDecays",      "ST t-channel t",         136.02  ),
    ("ST", "ST_t-channel_antitop_4f_inclusiveDecays",  "ST t-channel at",         80.95  ),
    ("ST", "ST_tW_top_5f_inclusiveDecays",             "ST tW",                   35.85  ),
    ("ST", "ST_tW_antitop_5f_inclusiveDecays",         "ST atW",                  35.85  ),
    ("WW", "WW_TuneCP5",                               "WW",                      75.88  ),
    ("WZ", "WZ_TuneCP5",                               "WZ",                      27.6   ),
    ("ZZ", "ZZ_TuneCP5",                               "ZZ",                      12.14  ),
    ("TT", "TTTo2L2Nu",                                "ttbar 2l2#nu",            87.31  ),
    ("TT", "TTToHadronic",                             "ttbar hadronic",         380.1   ),
    ("TT", "TTToSemiLeptonic",                         "ttbar semileptonic",     364.4   ),
    ("DY", "DYJetsToLL_M-10to50_TuneCP5",              "Drell-Yan 10-50",      18610.0,  ), #{'extraweight':"getZpt_2017(m_genboson,pt_genboson)"} ), # LO 18610.0; NLO 21658.0
    ("DY", "DYJetsToLL_M-50_TuneCP5",                  "Drell-Yan 50",          5343.0,  ), #{'extraweight':"getZpt_2017(m_genboson,pt_genboson)"} ), # LO  4954.0; NLO  5765.4
    ("DY", "DY1JetsToLL_M-50_TuneCP5",                 "Drell-Yan 1J 50",        877.8,  ), #{'extraweight':"getZpt_2017(m_genboson,pt_genboson)"} ),
    ("DY", "DY2JetsToLL_M-50_TuneCP5",                 "Drell-Yan 2J 50",        304.4,  ), #{'extraweight':"getZpt_2017(m_genboson,pt_genboson)"} ),
    ("DY", "DY3JetsToLL_M-50_TuneCP5",                 "Drell-Yan 3J 50",        111.5,  ), #{'extraweight':"getZpt_2017(m_genboson,pt_genboson)"} ),
]
if onlyDY: samplesB = [s for s in samplesB if 'DY'==s[0]]

samplesS = [ ]

samplesD = {
    'mumu' : ( "SingleMuon", "SingleMuon_Run2017", "observed", {'extratag':""} ),
}

# SAMPLESET
makeSFrameSamples(samplesD,samplesB,samplesS,weight=_weight,binN_weighted=10,cycle="DiMuonAnalysis")
samples = SampleSet(samplesD,samplesB,samplesS,channel="mumu")
if onlyDY: stitchWJ, mergeVV, mergeST, mergeTT = False, False, False, False
if stitchWJ:       samples.stitch("W*Jets",        name_incl="WJ",  name="WJ"                                         )
if stitchDY50:     samples.stitch("DY*J*M-50",     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan"             )
#if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeDY:        samples.merge( 'DY',                             name="DY",          title="Drell-Yan"             )
if mergeVV:        samples.merge( "VV","VV","WZ","WW","ZZ",         name="VV",          title="diboson"               )
if mergeST:        samples.merge( "ST",                             name="ST",          title="single top"            )
if mergeTT:        samples.merge( "TT",                             name="TT",          title="ttbar"                 )
samples.printTable()
#samples.printSampleObjects()


