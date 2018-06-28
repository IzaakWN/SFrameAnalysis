# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "_2017_V2" # extra label for opening file, saving plots to dir
plottag     = "" # extra label for image file
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
useCutTree          = True #and False
loadMacros          = True #and False
makePDF             = True and False

# DATACARD OPTIONS
doDatacard          = True and False
doNominal           = True #and False
doShifts            = True #and False
doTESscan           = True #and False
doTES               = True #and False
doMES               = True #and False # not for etau
doEES               = True #and False # not for mutau
doJTF               = True #and False
doLTF               = True #and False
doJER               = True #and False
doJEC               = True #and False
doUncEn             = True #and False

# SAMPLE OPTIONS
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeTT             = True #and False
mergeST             = True #and False
mergeVV             = True #and False
splitDY             = True #and False
splitTT             = True #and False
splitST             = True and False
normalizeWJ         = True #and False
doQCD               = True and False
doFakeRate          = True #and False
OSSS_ratio          = 1.06

# SAMPLES
SFRAME              = "SFrameAnalysis_ltau2017"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput_ltau2017")
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")

#### END SETTINGS ########################################################################


channels = [
    "mutau",
    #"etau",
]
if not doShifts:
  doTES, doEES, doJTF, doJER, doJEC, doUncEn = False, False, False, False, False, False

# CATEGORIES / SELECTIONS
_weight            = "genweight*puweight*trigweight_1*idisoweight_1*getLeptonTauFake(channel,gen_match_2,eta_2)"
if doTESscan: _weight += "*(gen_match_2==5 ? 0.883 : 1)"
#_weight           += "*ttptweight"; plottag+="_ttptweight"
#_weight            = _weight.replace('puweight',"puweight80p0"); plottag+="_PU80p0"
triggers           = "(triggers!=2 || pt_1>28)"
isocuts            = "iso_1<0.15 && iso_2==1" #iso_cuts==1"
vetos              = "lepton_vetos==0"
baseline           = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2<0 && decayMode_2<11"%(isocuts,vetos)
baseline_noIso2    = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2<0 && decayMode_2<11"%("iso_1<0.15",vetos)
baseline_JFR       = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2<0 && decayMode_2<11"%("iso_1<0.15 && iso_2_vloose==1 && iso_2!=1",vetos)
baselineSS         = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2>0 && decayMode_2<11"%(isocuts,vetos)
baseline_antiIso   = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2<0 && decayMode_2<11"%("iso_1>0.15 && iso_1<0.50 && iso_2==1",vetos)
baselineSS_antiIso = "channel>0 && (triggers!=2 || pt_1>28) && %s && %s && q_1*q_2>0 && decayMode_2<11"%("iso_1>0.15 && iso_1<0.50 && iso_2==1",vetos)
ZTTregion          = "45<m_vis && m_vis<85 && pt_2>30 && nbtag==0 && dzeta>-30" # tau discr. check
ZTTregion2         = "pfmt_1<40 && 45<m_vis && m_vis<85 && pt_2>30 && dzeta>-25" # tau ES measurement
if "B-E" in era:
  baseline        += " && (!isData || run<=304826)"
  baseline_noIso2 += " && (!isData || run<=304826)"
  _weight          = _weight.replace('puweight',"puweightBtoF") #E
  plottag         += "_EraBtoE"
if "F" in era:
  baseline        += " && (!isData || run>=304911)"
  baseline_noIso2 += " && (!isData || run>=304911)"
  _weight = _weight.replace('puweight',"puweightF")
  plottag         += "_EraF"

selections  = [
#     sel("no cuts",                                ""                                                          ),
#     sel("baseline, no tau ID",                    "%s"       %(baseline_noIso2)                               ),
#     sel("baseline, no tau ID, m_T<50GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1<50")                   ),
#     sel("baseline, no tau ID, m_T>80GeV",         "%s && %s" %(baseline_noIso2,"pfmt_1>80")                   ),
#     sel("ZTT enriched, no tau ID",                "%s && %s" %(baseline_noIso2, ZTTregion)                    ),
#     sel("ZTT enriched, no tau ID, DM0",           "%s && %s && decayMode_2==0" %(baseline_noIso2,  ZTTregion) ),
#     sel("ZTT enriched, no tau ID, DM1",           "%s && %s && decayMode_2==1" %(baseline_noIso2,  ZTTregion) ),
#     sel("ZTT enriched, no tau ID, DM10",          "%s && %s && decayMode_2==10" %(baseline_noIso2, ZTTregion) ),
#     sel("ZTT enriched, no tau ID, DM11",          "%s && %s" %(baseline_noIso2.replace('2<11','2==11'), ZTTregion) ),
#     sel("ZTT enriched, no tau ID, 0 photons",      "%s && %s && nPhoton_2==0" %(baseline_noIso2, ZTTregion)   ),
#     sel("ZTT enriched, no tau ID, DM0, 0 photons", "%s && %s && decayMode_2==0 && nPhoton_2==0" %(baseline_noIso2,  ZTTregion) ),
#     sel("ZTT enriched, no tau ID, DM10, 0 photons","%s && %s && decayMode_2==10 && nPhoton_2==0" %(baseline_noIso2, ZTTregion) ),
    sel("baseline, pt>25",                          "%s"       %(baseline)                                      ),
#     sel("baseline, pt>25",                         "%s"       %(baseline)                                      ),
#     sel("baseline, pt>28",                         "%s && %s" %(baseline,"pt_1>28")                            ),
#     sel("tight",                                    "%s"       %(baseline)                                    ),
#     sel("pt_mu>29, tight",                        "%s && %s" %(baseline,"pt_1>29")                            ),
#     sel("pt_mu>29, tight, m_T>80GeV",             "%s && %s" %(baseline,"pt_1>29 && pfmt_1>80")               ),
#     sel("pt_mu>29, tight, m_T<50GeV",             "%s && %s" %(baseline,"pt_1>29 && pfmt_1<50")               ),
#     sel("pt_mu>29, VL && !T",                     "%s && %s" %(baseline_JFR,"pt_1>29")                        ),
#     sel("pt_mu>29, VL && !T, m_T>80GeV",          "%s && %s" %(baseline_JFR,"pt_1>29 && pfmt_1>80")           ),
#     sel("pt_mu>29, VL && !T, m_T<50GeV",          "%s && %s" %(baseline_JFR,"pt_1>29 && pfmt_1<50")           ),
#     sel("tight, m_T>80GeV",                       "%s && %s" %(baseline,"pfmt_1>80")                          ),
#     sel("tight, m_T<50GeV",                       "%s && %s" %(baseline,"pfmt_1<50")                          ),
#     sel("tight, m_T<50GeV, DM10",                 "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==10")       ),
#     sel("tight, m_T<50GeV, no photons, DM10",     "%s && %s" %(baseline,"pfmt_1<50 && nPhoton_2==0 && decayMode_2==10")),
#     sel("tight, m_T<50GeV, DM10 restr",             "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==10 && 0.90<m_2 && m_2<1.30")),
#     sel("tight, m_T<50GeV, no photons, DM10 restr", "%s && %s" %(baseline,"pfmt_1<50 && nPhoton_2==0 && decayMode_2==10 && 0.90<m_2 && m_2<1.30")),
#     sel("no tau ID, m_T<50GeV, abs(eta_2)<1.5",   "%s && %s" %(baseline_noIso2,"pfmt_1<50 && abs(eta_2)<1.5") ),
#     sel("no tau ID, m_T<50GeV, abs(eta_2)>1.5",   "%s && %s" %(baseline_noIso2,"pfmt_1<50 && abs(eta_2)>1.5") ),
#     sel("baseline, tight, m_T>80GeV",             "%s && %s" %(baseline,"pfmt_1>80")                          ),
#     sel("ZTT enriched, tight",                    "%s && %s" %(baseline, ZTTregion)                           ),
#     sel("ZTT enriched, no tau ID",                "%s && %s" %(baseline_noIso2, ZTTregion)                    ),
#     sel("ZTT enriched, no tau ID, abs(eta_2)<1.5", "%s && %s && %s" %(baseline_noIso2,ZTTregion,"abs(eta_2)<1.5") ),
#     sel("ZTT enriched, no tau ID, abs(eta_2)>1.5", "%s && %s && %s" %(baseline_noIso2,ZTTregion,"abs(eta_2)>1.5") ),
#     sel("ZTT enriched, tight, DM0",               "%s && %s && decayMode_2==0" %(baseline, ZTTregion)         ),
#     sel("ZTT enriched, tight, DM1",               "%s && %s && decayMode_2==1" %(baseline, ZTTregion)         ),
#     sel("ZTT enriched, tight, DM10",              "%s && %s && decayMode_2==10" %(baseline, ZTTregion)        ),
#     sel("ZTT enriched, tight, 0 photons",         "%s && %s && nPhoton_2==0 " %(baseline, ZTTregion)          ),
#     sel("ZTT enriched, tight, DM0, 0 photons",    "%s && %s && decayMode_2==0 && nPhoton_2==0" %(baseline, ZTTregion)  ),
#     sel("ZTT enriched, tight, DM10, 0 photons",   "%s && %s && decayMode_2==10 && nPhoton_2==0" %(baseline, ZTTregion) ),
#     sel("m_T<50GeV",                              "%s && %s" %(baseline,"pfmt_1<50")                          ),
#     sel("m_T<50GeV, DM0",                         "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==0")        ),
#     sel("m_T<50GeV, DM1",                         "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==1")        ),
#     sel("m_T<50GeV, DM10",                        "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==10")       ),
#     sel("m_T<50GeV, DM1 restr",                   "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==1 && 0.35<m_2 && m_2<1.2") ), #1.15*sqrt(0.009*pt_2)
#     sel("m_T<50GeV, DM10 restr",                  "%s && %s" %(baseline,"pfmt_1<50 && decayMode_2==10 && 0.90<m_2 && m_2<1.3") ),
#     sel("m_T<50GeV, restr",                       "%s && %s" %(baseline,"pfmt_1<50 && (decayMode_2!=1 || 0.35<m_2 && m_2<1.2) && (decayMode_2!=10 || 0.90<m_2 && m_2<1.30)") ),
#     sel("m_T<50GeV, Dzeta>-20GeV",                "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20")                    ),
#     sel("m_T<50GeV, Dzeta>-20GeV, DM0",           "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && decayMode_2==0")  ),
#     sel("m_T<50GeV, Dzeta>-20GeV, DM1",           "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && decayMode_2==1")  ),
#     sel("m_T<50GeV, Dzeta>-20GeV, DM10",          "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && decayMode_2==10") ),
#     sel("m_T<50GeV, Dzeta>-20GeV, DM1 restr",     "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && decayMode_2==1 && 0.35<m_2 && m_2<1.2") ), #1.15*sqrt(0.009*pt_2)
#     sel("m_T<50GeV, Dzeta>-20GeV, DM10 restr",    "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && decayMode_2==10 && 0.90<m_2 && m_2<1.3") ),
#     sel("m_T<50GeV, Dzeta>-20GeV, restr",         "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-20 && (decayMode_2!=1 || 0.35<m_2 && m_2<1.2) && (decayMode_2!=10 || 0.90<m_2 && m_2<1.30)") ),
#     sel("m_T<50GeV, Dzeta>-30GeV, DM1 restr",     "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-30 && decayMode_2==1 && 0.35<m_2 && m_2<1.2") ), #1.15*sqrt(0.009*pt_2)
#     sel("m_T<50GeV, Dzeta>-30GeV, DM10 restr",    "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-30 && decayMode_2==10 && 0.90<m_2 && m_2<1.3") ),
#     sel("m_T<50GeV, Dzeta>-30GeV, restr",         "%s && %s" %(baseline,"pfmt_1<50 && dzeta>-30 && (decayMode_2!=1 || 0.35<m_2 && m_2<1.2) && (decayMode_2!=10 || 0.90<m_2 && m_2<1.30)") ),
#     sel("ZTT region",                           "%s && %s"       %(baseline,ZTTregion2)                       ),
#     sel("ZTT region, DM0",                      "%s && %s && %s" %(baseline,ZTTregion2,"decayMode_2==0")      ),
#     sel("ZTT region, DM1",                      "%s && %s && %s" %(baseline,ZTTregion2,"decayMode_2==1")      ),
#     sel("ZTT region, DM10",                     "%s && %s && %s" %(baseline,ZTTregion2,"decayMode_2==10")     ),
#     sel("ZTT region, DM1 restr",                "%s && %s && %s" %(baseline,ZTTregion2,"decayMode_2==1 && 0.35<m_2 && m_2<1.2") ), #1.15*sqrt(0.009*pt_2)
#     sel("ZTT region, DM10 restr",               "%s && %s && %s" %(baseline,ZTTregion2,"decayMode_2==10 && 0.90<m_2 && m_2<1.3") ),
#     sel("ZTT region, restr",                    "%s && %s && %s" %(baseline,ZTTregion2,"(decayMode_2!=1 || 0.35<m_2 && m_2<1.2) && (decayMode_2!=10 || 0.90<m_2 && m_2<1.30)") ),
#     sel("baseline, >=1b, no tau ID",              "%s && %s" %(baseline_noIso2,"nbtag>0")                     ),
#     sel("baseline, >=1b, no tau ID",              "%s && %s" %(baseline_noIso2,"nbtag>0"), only="jesUp"       ).shift('jesUp'),
#     sel("baseline, >=1b, no tau ID",              "%s && %s" %(baseline_noIso2,"nbtag>0"), only="jesDown"     ).shift('jesDown'),
#     sel("baseline, >=1b",                         "%s && %s" %(baseline,"nbtag>0")                            ),
#     sel("baseline, >=1b, vloose",                 "%s && %s" %(baseline.replace('iso_2','iso_2_vloose'), "nbtag>0") ),
#     sel("baseline, >=1b, loose",                  "%s && %s" %(baseline.replace('iso_2','iso_2_loose'),  "nbtag>0") ),
#     sel("baseline, >=1b, medium",                 "%s && %s" %(baseline.replace('iso_2','iso_2_medium'), "nbtag>0") ),
#     sel("baseline, >=1b, tight",                  "%s && %s" %(baseline,"nbtag>0")                            ),
#     sel("baseline, >=1b, vtight",                 "%s && %s" %(baseline.replace('iso_2','iso_2_vtight'),  "nbtag>0") ),
#     sel("baseline, >=1b, vvtight",                "%s && %s" %(baseline.replace('iso_2','iso_2_vvtight'), "nbtag>0") ),
#     sel("baseline, >=1b, tight",                  "%s && %s" %(baseline,"nbtag>0"), only="jesUp"              ).shift('jesUp'),
#     sel("baseline, >=1b, tight",                  "%s && %s" %(baseline,"nbtag>0"), only="jesDown"            ).shift('jesDown'),
#     sel("baseline, >=1b, m_T<100GeV",             "%s && %s" %(baseline,"nbtag>0 && pfmt_1<100")              ),
#     sel("baseline, >=1b, no tau ID, m_T<100GeV",  "%s && %s" %(baseline_noIso2,"nbtag>0 && pfmt_1<100")       ),
]


# VARIABLES
variables = [
    var("m_vis",                                40,     0,  200, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     ###var("m_sv",                                 40,     0,  200 ),
#     var("m_2",                                  50,     0,    2, title="m_tau" ),
#     var("m_2",                                  25,     0,    2, title="m_tau", filename="$NAME_0p08" ),
#     var("m_2",                                  75,     0,    3, title="m_tau", logy=True, filename="$NAME_log", veto="decayMode_2" ),
#     var("m_2",                                  35,  0.18, 1.58, title="m_tau", filename="$NAME_0p2to1p6", only='decayMode_2==1(?!0)' ),
#     var("m_2",                                  20,  0.76, 1.56, title="m_tau", filename="$NAME_0p8to1p6", only='decayMode_2==10' ),
#     var("m_2",                                  10,  0.72, 1.56, title="m_tau", filename="$NAME_0p8to1p6_0p08", only='decayMode_2==10' ),
#     var("ht",                                   50,     0, 2500 ),
#     var("dR_ll",                                30,     0,    6 ),
    var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ),
#     var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ).shift('jerUp'),
#     var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ).shift('jerDown'),
#     var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ).shift('jesUp'),
#     var("pfmt_1",                               40,     0,  200, title="m_T(mu,MET)", ctitle={'etau':"m_T(e,MET)"}, cbinning={'iso_2.*nbtag':(20,0,200)} ).shift('jesDown'),
#     var("met",                                  40,     0,  200 ),
#     var("met",                                  40,     0,  200 ).shift('jerUp'),
#     var("met",                                  40,     0,  200 ).shift('jerDown'),
#     var("met",                                  40,     0,  200 ).shift('jesUp'),
#     var("met",                                  40,     0,  200 ).shift('jesDown'),
#     var("metphi",                               35,  -3.5,  3.5 ),
#     var("gen_match_2",                           9,    -1,    8, position='center', title="tau gen. match", ),
#     ###var("puweight",                            100,     0,  200, logy=True ),
#     var("npu",                                  40,     0,   80 ),
#     var("npv",                                  40,     0,   80 ),
#     var("rho",                                  70,     0,   70 ),
#     var("njets",                                 8,     0,    8 ),
#     var("nbtag",                                 7,     0,    7 ),
#     ###var("nbtag20",                               7,     0,    7 ),
    var("pt_1",                                 50,     0,  200, title="muon pt",  ctitle={'etau':"electron pt"}  ),
#     var("eta_1",                                26,  -2.6,  2.6, title="muon eta", ctitle={'etau':"electron eta"} ),
    var("pt_2",                                 30,     0,  150, title="tau pt",   ctitle={'emu': "electron pt"}  ),
#     var("eta_2",                                26,  -2.6,  2.6, title="tau eta",  ctitle={'emu': "electron eta"} ),
#     #var("iso_1",                               100,     0,  0.5 ),
#     var("decayMode_2",                          14,     0,   14, position='center' ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_2",  50,  -1.0,  1.0, logy=True, veto='iso_2.*decayMode_2==11', position='centerleft' ),
#     var("byIsolationMVArun2v1DBoldDMwLTraw_2",  50,   0.8,  1.0, filename="$NAME_zoom0p8", veto='decayMode_2==11', position='centerleft', cbinning={'iso_2.*nbtag':(20,0.8,1.0)} ),
#     var("byIsolationMVArun2v2DBoldDMwLTraw_2",  50,  -1.0,  1.0, logy=True, veto='iso_2.*decayMode_2==11', position='centerleft' ),
#     var("byIsolationMVArun2v2DBoldDMwLTraw_2",  50,   0.8,  1.0, filename="$NAME_zoom0p8", veto='decayMode_2==11', position='centerleft', cbinning={'iso_2.*nbtag':(20,0.8,1.0)} ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_2",  50,   0.8,  1.0, filename="$NAME_zoom0p8", position='centerleft' ),
#     var("byIsolationMVArun2v1DBnewDMwLTraw_2",  50,  -1.0,  1.0, logy=True, position='centerleft' ),
#     var("chargedPionPt_2",                      80,     0,  100 ),
#     var("neutralPionPt_2",                      80,     0,  100, veto='decayMode_2==1?0' ),
#     var("chargedIsoPtSum_2",                    80,     0,  100, logy=True, cbinning={'iso_2':(50,0,50)} ),
#     var("neutralIsoPtSum_2",                    80,     0,  100, logy=True, cbinning={'iso_2':(80,0,80)} ),
#     var("chargedIsoPtSumdR03_2",                80,     0,  100, logy=True, cbinning={'iso_2':(50,0,50)} ),
#     var("neutralIsoPtSumdR03_2",                80,     0,  100, logy=True, cbinning={'iso_2':(80,0,80)} ),
#     var("puCorrPtSum_2",                        70,     0,   70 ),
#     var("photonPtSumOutsideSignalCone_2",       60,     0,   30, logy=True ),
#     var("photonPtSumOutsideSignalConedR03_2",   60,     0,   30, logy=True ),
#     var("byPhotonPtSumOutsideSignalCone_2",      4,     0,    4 ),
#     var("nPhoton_2",                            12,     0,   12, title="number of photons", veto='nPhoton_2==0' ),
#     var("ptWeightedDetaStrip_2",                60,     0,  0.6, logy=True ),
#     var("ptWeightedDphiStrip_2",                60,     0,  0.6, logy=True ),
#     var("ptWeightedDrSignal_2",                 60,     0,  0.6, logy=True ),
#     var("ptWeightedDrIsolation_2",              60,     0,  0.6, logy=True ),
#     var("leadingTrackChi2_2",                   60,     0,    6 ),
#     var("leadingTrackPt_2",                     70,     0,   70 ),
#     var("eRatio_2",                             51, -0.01, 1.01, logy=True, cbinning={'iso_2':(38,-0.01,1.01)} ),
#     var("dxy_Sig_2",                            65,    -3,  3.5, cbinning={'iso_2':(40,-4.0,4.0)} ),
#     var("ip3d_2",                               50, -0.08, 0.08 ),
#     var("ip3d_Sig_2",                           60,    -6,    6, cbinning={'iso_2':(70,-6,8)} ),
#     var("hasSecondaryVertex_2",                  4,     0,    4 ),
#     var("decayDistMag_2",                       50,     0,  1.5, logy=True ),
#     var("flightLenthSig_2",                     75,     0,   15, cbinning={'iso_2':(50,0,20)} ),
#     var("d0_2",                                 60, -0.04, 0.04, title="tau d_0", ctitle={'etau':"electron d_0"} ),
#     var("dz_2",                                 60,     0, 0.04, title="tau d_z", ctitle={'etau':"electron d_z"} ),
#     var("dzeta",                                50,  -150,  100 ), # filename="Dzeta"
#     var("pzetavis",                             50,     0,  200 ),
]
# for p in [("b",1),("b",2),("j",1),("j",2)]:
#     variables.append(var( "%spt_%i"  % p,      50,    0,   250  ))
#     variables.append(var( "%seta_%i" % p,      50, -5.0,   5.0  ))
#veto=['nbtag==0']

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
    "mutau": ( "SingleMuon",      "SingleMuon_Run2017",     "single muon"     ),
    #"etau":  ( "SingleElectron",  "SingleElectron_Run2017", "single electron" ),
    #"emu":   ( "SingleMuon",      "SingleMuon_Run2017",     "single muon"     ),
}

# SAMPLESET
makeSFrameSamples(samplesD,samplesB,samplesS,weight=_weight,binN_weighted=10)
samples = SampleSet(samplesD,samplesB,samplesS)
#samples.printTable()
if stitchWJ:   samples.stitch('W*Jets',        name_incl="WJ",  name="WJ"                                         )
if stitchDY50: samples.stitch('DY*J*M-50',     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan M=50GeV"     )
#if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeVV:    samples.merge( 'VV','WZ','WW','ZZ',              name="VV",          title="diboson"               )
if mergeST:    samples.merge( 'ST',                             name="ST",          title="single top"            )
if mergeTT:    samples.merge( 'TT',                             name="TT",          title="ttbar"                 )
if splitDY:    samples.split( 'DY', [('ZTT',"Z -> tau_{mu}tau_{h}","gen_match_2==5"),  ('ZJ',"Drell-Yan other","gen_match_2!=5")])
#if splitDY:    samples.split( 'DY', [('ZTT_DM0',"h^{\pm}","decayMode_2==0"), ('ZTT_DM1',"h^{\pm}h^{0}","decayMode_2==1"), ('ZTT_DM10',"h^{\pm}h^{\mp}h^{\pm}","decayMode_2==10"),])
if splitTT:    samples.split( 'TT', [('TTT',"ttbar with real tau_h","gen_match_2==5"), ('TTJ',"ttbar other","gen_match_2!=5")]) #'ttbar j -> tau_h': "gen_match_2<5"
#if splitST:    samples.split('ST',[('STT',"single top with real tau_h',"gen_match_2==5"), ('STJ',"single top other","gen_match_2!=5")])
samples.printTable()
#samples.printSampleObjects()

# SHIFT
samples_TESscan, samples_TMESscanUp, samples_TMESscanDown = { }, { }, { }
samples_TESUp, samples_TESDown, samples_MESUp, samples_MESDown, samples_EESUp, samples_EESDown  = [ ], [ ], [ ], [ ], [ ], [ ]
samples_JTFUp, samples_JTFDown, samples_LTFUp, samples_LTFDown = [ ], [ ], [ ], [ ]
if (doShifts and doDatacard) or drawShifts:
  if doMES:
    samples_MESUp   = samples.shift(['*'],"_MES1p01"," +1% MES", filter=False)
    samples_MESDown = samples.shift(['*'],"_MES0p99"," -1% MES", filter=False)
  if doTES:
    samples_TESUp   = samples.shift(['TT','DY','ST'],"_TES1p03"," +3% TES", filter=False, title_veto="other")
    samples_TESDown = samples.shift(['TT','DY','ST'],"_TES0p97"," -3% TES", filter=False, title_veto="other")
    #samples_TESUp.printTable()
    #samples_TESUp.printSampleObjects()
  if doJTF:
    samples_JTFUp   = samples.shift(['TT','DY','ST','WJ'],"_JTF1p10"," +10% JTF ES", filter=False, title_veto="real")
    samples_JTFDown = samples.shift(['TT','DY','ST','WJ'],"_JTF0p90"," -10% JTF ES", filter=False, title_veto="real")
    #samples_JTFUp.printTable()
    #samples_JTFUp.printSampleObjects()
  if doLTF:
    samples_LTFUp   = samples.shift(['DY'],"_LTF1p03"," +3% LTF ES", filter=True, title_veto="real")
    samples_LTFDown = samples.shift(['DY'],"_LTF0p97"," -3% LTF ES", filter=True, title_veto="real")
  if doTESscan:
    (minshift,maxshift,steps) = ( -0.060, 0.060, 0.001 )
    tesshifts  = [ s*steps for s in xrange(int(minshift/steps),int(maxshift/steps)+1) if s ]
    for tshift in tesshifts:
      if doStack and abs(tshift)!=0.030: continue
      #if abs(tshift)<=0.020 or abs(tshift)>=0.050: continue
      #if abs(tshift)>=0.050: continue
      shifttag = " %s%% TES"%(("%+.2f"%(100.0*tshift)).rstrip('0').rstrip('.'))
      shiftkey = "%.3f"%(1+tshift)
      filetag  = "_TES"+shiftkey.replace('.','p')
      samples_TESscan[shiftkey] = samples.shift(['DY'],filetag,shifttag,filter=True,share=True,close=True,title_veto="other")
      if doMES:
        if abs(tshift)<0.050: continue # TODO: REMOVE!!!
        shifttagUp   = shifttag+" +1% MES"
        shifttagDown = shifttag+" -1% MES"
        filetagUp    = filetag+"_MES1p01"
        filetagDown  = filetag+"_MES0p99"
        samples_TMESscanUp[shiftkey]   = samples.shift(['DY'],filetagUp,  shifttagUp,  filter=True,share=True,close=True,title_veto="other")
        samples_TMESscanDown[shiftkey] = samples.shift(['DY'],filetagDown,shifttagDown,filter=True,share=True,close=True,title_veto="other")
    #samples_TESscan['0.970'].printTable()
    #samples_TESscan['0.970'].printSampleObjects()


