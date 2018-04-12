# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "_Moriond" # extra label for opening file, saving plots to dir
plotlabel   = "_test" # extra label for image file
luminosity  = 35.9

# VERBOSITY
verbosity               = 1
verbositySampleTools    = 1
verbosityPlotTools      = 0
verbosityVariableTools  = 0
verbositySelectionTools = 0

# PLOTS OPTIONS
doStack             = True #and False
compareStack        = True and False
measureOSSS         = True and False
measureSF           = True and False
doSigma             = True and False
doJECErrors         = True and False # "JER" or "JES"
checkYield          = True and False
doPlot2D            = True and False
doComparison        = True and False
drawShifts          = True and False
useCutTree          = True #and False
doSignalUpScaling   = True #and False
drawData            = True #and False
drawSignal          = True #and False

# DATACARD OPTIONS
doDatacard          = True and False
recreateDC          = True #and False
doNominal           = True #and False
doTES               = True and False
doEES               = True and False # not for mutau
doJTF               = True and False
doLTF               = True and False
doJER               = True and False
doJEC               = True and False
doZpt               = True and False
doTTpt              = True and False
doQCD_WJ            = True and False
doShapes            = True and False

# SAMPLE OPTIONS
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeTT             = True and False
mergeST             = True #and False
mergeVV             = True #and False
splitDY             = True #and False
splitTT             = True and False
splitST             = True and False
normalizeWJ         = True #and False
normalizeTT         = True #and False
doQCD               = True #and False
OSSS_ratio          = 1.06

# SAMPLES
SFRAME              = "SFrameAnalysis_ltau2017"
PNFS                = "root://t3dcachedb.psi.ch:1094//pnfs/psi.ch/cms/trivcat/store/user/ineuteli/analysis/SFrameAnalysis/AnalysisOutput/"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput")
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")

#### END SETTINGS ########################################################################


# CHANNELS
channels = [
    "mutau",
    #"etau",
]

# LABELS
if isinstance(doJECErrors,str): plotlabel+="_err_%s"%doJECErrors
elif doJECErrors==True:         plotlabel+="_err"
if not drawSignal:  plotlabel+="_noSignal"
if not doQCD:       plotlabel+="_noQCD"
if not normalizeWJ: plotlabel+="_noWJrenormalization"
if not normalizeTT: plotlabel+="_noTTrenormalization"
if not normalizeWJ and "emu" not in channels: plotlabel+="_noWJrenorm"

# BLIND
blind_dict = { "m_vis":      ( 15, 70), "m_sv" :     ( 20,  80),  "dR_ll" : (  0,1.2),
               #"pt_tt":     ( 80,200),  "pt_tt_sv":  ( 80, 200), 
               #"R_pt_m_vis": (2.5, 10), "R_pt_m_sv": (2.0,  10),
}

# CATEGORIES / SELECTIONS
_weight         = "weight*trigweight_or_1"
if "/puweight" in _weight: plotlabel+="_nopuweight"
isocuts         = "iso_cuts==1" #iso_1<0.15 && iso_2_medium==1
vetos           = "lepton_vetos==0"
vetos0          = "dilepton_veto==0 && extraelec_veto==0 && extramuon_veto==0"
vetos_mutau     = "%s && againstElectronVLooseMVA6_2==1 && againstMuonTight3_2==1"%(vetos0)
vetos_etau      = "%s && againstElectronTightMVA6_2==1 && againstMuonLoose3_2==1"%(vetos0)
vetos_emu       = "extraelec_veto==0 && extramuon_veto==0"
ptcut           = "(pt_1>26||(channel==1 && pt_1>23))"
triggers        = "abs(eta_1)<2.1 && trigger_cuts==1" # && ((%s && (triggers==1||triggers==3))||(triggers>1))" #% ptcut #pt_1>20 &&
baseline        = "channel>0 && %s && %s && q_1*q_2<0 && %s" % (isocuts,vetos,triggers) # +" && bpt_1>30" #+" && jpt_1>30" && jpt_2>30
baseline_rel    = "channel>0 && %s && %s && q_1*q_2<0 && %s" % ("iso_1>0.15 && iso_1<0.5 && iso_2_medium==1",vetos,triggers)
baseline_emu    = "channel>0 && %s && iso_1<0.20 && iso_2<0.15 && q_1*q_2<0" % (vetos_emu)
emu_check       = "channel>0 && njets==2 && jpt_1>30 && jpt_2>30 && pt_1>25 && pt_2>25 && abs(eta_1)<2.1 && abs(eta_2)<2.1 && iso_1<0.10 && q_1*q_2<0 && 70<m_vis&&m_vis<110" # && abs(eta_2)<2.1 # iso_1<0.15 && iso_2<0.15  && ncbtag==0
if "emu" in channels: baseline = baseline_emu # emu
category_bbA2   = "ncbtag >0 && ncbtag==ncjets && nfjets==0"
category_bbA    = "ncbtag==1 && ncjets==1 && nfjets==0" # no optimizations
category1       = "ncbtag>0 && ncjets==1 && nfjets >0"
category2       = "ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2 && met<60"
category2J      = "ncbtag>0 && ncjets==2 && nfjets==0"
category1TT     = "ncbtag>0 && ncjets==1 && nfjets >0 && met>60 && pfmt_1>60 && jpt_1>30 && jpt_2>30"
category2TT     = "ncbtag>0 && ncjets==2 && nfjets==0 && dphi_ll_bj>2 && met>60 && pfmt_1>60 && jpt_1>30 && jpt_2>30"
(metcut,mt1cut) = ("met<60","pfmt_1<60")
if "emu" in channels: (metcut,mt1cut) = ("met<40","pfmt_1<40")
newcuts         = "%s && %s" % (metcut,mt1cut)
newcuts_bbA     = "pzeta_disc>-40 && pfmt_1<40"

selections  = [
#     sel("no cuts",               ""                                                              ),
#     sel("QCD CR",                "%s && %s && %s && %s && %s" % (isocuts, vetos, "q_1*q_2<0", "njets>0", triggers)),
#     sel("baseline, same sign",   "%s" % (baseline.replace("q_1*q_2<0","q_1*q_2>0"))              ),# 
    sel("baseline",                "%s" % (baseline)                                             ),
#     sel("two >25 GeV jets",      "%s && %s" % (baseline, "jpt_1 > 25 && jpt_2 > 25")             ),
#     sel("two >30 GeV jets",        "%s && %s" % (baseline, "njets>1")                            ), # jpt_1 > 30 && jpt_2 > 30
#     sel(">= 1 b tag, >20 GeV",   "%s && %s" % (baseline, category_bbA2.replace('btag','btag20').replace('jets','jets20')) ),
#     sel("1 b tag, >20 GeV",      "%s && %s" % (baseline, category_bbA.replace('btag','btag20').replace('fjets','fjets20'))  ),
#     sel("1 b tag, >20 GeV, j30",   "%s && %s" % (baseline, category_bbA.replace('btag','btag20'))                             ),
#     sel("1 b tag, >20 GeV",        "%s && %s" % (baseline, category_bbA.replace('btag','btag20').replace('jets','jets20'))    ),
#     sel("1 b tag, >20 GeV, fj30",  "%s && %s" % (baseline, category_bbA.replace('btag','btag20').replace('cjets','cjets20'))  ),
#     sel(">= 1 b tag",            "%s && %s" % (baseline, category_bbA2)                          ),
#     sel("1 b tag",               "%s && %s" % (baseline, category_bbA)                           ),
#     sel("category bbA",          "%s && %s && %s" % (baseline, category_bbA, newcuts_bbA)        ),
#     sel(">30 GeV forward jet",   "%s && %s" % (baseline, "njets>1 && fjpt_1>30")                 ),
#     sel(">50 GeV forward jet",   "%s && %s" % (baseline, "njets>1 && fjpt_1>50")                 ),
#     sel("baseline 1j",           "%s && njets==1" % (baseline)                                   ),
#     sel("baseline <45",          "%s && jpt_1<45" % (baseline)                                   ),
#     sel("baseline >45",          "%s && jpt_1>45" % (baseline)                                   ),
#     sel("baseline, iso SB",      "%s" % (baseline_rel)                                           ),
#     sel("1c1c, SS, no iso",      "%s && %s" % (baseline.replace("iso_cuts==1 && ",""),category2.replace("ncbtag > 0 && ",""))),
#     sel("1c1c, SS, iso SR",      "%s && %s" % (baseline.replace("q_1*q_2<0","q_1*q_2>0"),category2.replace("ncbtag > 0 && ",""))),
#     sel("1c1c, SS, iso SB",      "%s && %s" % (baseline_rel.replace("q_1*q_2<0","q_1*q_2>0"),category2.replace("ncbtag > 0 && ",""))),
#     sel("baseline WJ CR",        "%s && %s" % (baseline,"pfmt_1>70")                             ),
#     sel("baseline 1c0f",         "%s && %s && %s" % (baseline,"ncjets==1 && nfjets==0","jpt_1>30")),
#     sel("baseline 0c1f",         "%s && %s && %s" % (baseline,"ncjets==0 && nfjets==1","jpt_1>30")),
#     sel("=2j",                   "%s"       % (emu_check)                                        ),
#     sel("=2j",                   "%s"       % (emu_check)                                        ),
#     sel(">=2j",                  "%s"       % (emu_check.replace("njets==2","njets>1"))          ),
#     sel(">1j",                   "%s"       % (emu_check.replace("njets==2","njets>1"))          ),
#     sel(">=1j",                  "%s"       % (emu_check.replace("njets==2","njets>0").replace(" && jpt_2>30",""))),
#     sel(">0j20",                 "%s"       % (emu_check.replace("njets==2","njets20>0").replace(" && jpt_2>30",""))),
#     sel("1j1f, |eta|<3",         "%s && %s" % (emu_check,"(abs(jeta_1)>3 || abs(jeta_2)>3)")),
    sel("category 1",            "%s && %s" % (baseline, category1)                              ),
    sel("category 2",            "%s && %s" % (baseline, category2)                              ),
#     sel("category 2J",            "%s && %s" % (baseline, category2J)                              ),
#     sel("category 2J DY CR",      "%s && %s" % (baseline, category2J.replace("btag > 0","btag==0")) ),
#     sel("category 1 TT CR0",     "%s && %s" % (baseline, category1TT0)                           ),
#     sel("category 1 TT CR1",     "%s && %s" % (baseline, category1TT1)                           ),
#     sel("category 2 jet cuts only", "%s && %s" % (baseline, category2J)                          ),
#     sel("category 1 TT CR",      "%s && %s" % (baseline, category1TT)                            ),
#     sel("category 2 TT CR",      "%s && %s" % (baseline, category2TT)                            ),
#     sel("category 1 met",        "%s && %s && %s" % (baseline, category1, metcut)                ),
#     sel("category 2 met, no dphi", "%s && %s && %s" % (baseline, category2J, metcut)             ),
#     ###sel("category 1 mt1",      "%s && %s && %s" % (baseline, category1, mt1cut)                ),
#     ###sel("category 2 mt1",      "%s && %s && %s" % (baseline, category2, mt1cut)                ),
#     sel("category 1 SR",         "%s && %s && %s" % (baseline, category1, signalwindow)          ),
#     sel("category 2 SR",         "%s && %s && %s" % (baseline, category2, signalwindow)          ), # && met < 60
#     sel("category 1 SR met",     "%s && %s && %s && %s" % (baseline, category1, metcut, signalwindow)),
#     ###sel("category 1 SR mt1",   "%s && %s && %s && %s" % (baseline, category1, mt1cut, signalwindow)),
#     ###sel("category 2 SR mt1",   "%s && %s && %s && %s" % (baseline, category2, mt1cut, signalwindow)),
#     sel("category 1.2",          "%s && %s && %s" % (baseline, category1, "pfmt_1<60")               ),
#     sel("category 2.2",          "%s && %s && %s" % (baseline, category2, "pfmt_1<60")               ),
#     sel("category 2.2",          "%s && %s && %s" % (baseline, category2J, "pfmt_1<60")              ), # no dphi
]


# VARIABLES
variables = [
#     ##var("m_vis",                         35,   0,  70 ),
#     ##var("m_sv",                          35,   0,  70 ),
    var("m_sv",                            40,   0, 160 ),
    var("m_vis",                           35,   0, 140 ),
#     var("m_2",                             30,   0,   3 ),
#     var("met",                             40,   0, 200 ),
    var("pfmt_1",                          40,   0, 200 ),
#     var("fjpt_1",                          49,    5, 250 ),
#     var("fjpt_2",                          49,    5, 250 ),
#     var("fjeta_1",                         50, -5.0, 5.0 ),
#     var("fjeta_2",                         50, -5.0, 5.0 ),
#     var("dphi_ll_bj",                      30,   0, 4.5 ),
#     var("ncbtag20",                         5,   0,   5 ),
#     var("ncbtag",                           5,   0,   5 ),
#     var("njets",                            6,   0,   6 ),
#     var("nfjets",                           5,   0,   5 ),
#     var("ncjets",                           5,   0,   5 ),
#     var("pzeta_disc",                      45, -145,  80 ),
#     var("ht",                              50,   0, 500 ),
#     var("pt_tt",                           50,   0, 160 ),
#     var("pt_tt_sv",                        30,   0, 160 ),
#     var("dR_ll",                           30,   0,   6 ),
#     ##var("R_pt_m_vis",                    50,   0,   7 ),
#     var("R_pt_m_sv",                       50,   0,   5 ),
#     var("jpt_1*(abs(jeta_1)<2.4 && jpt_1>30) + jpt_2*((abs(jeta_1)>=2.4||jpt_1<=30) && abs(jeta_2)<2.4 && jpt_2>30)",   49, 5,250),
#     var("jpt_1*(abs(jeta_1)>2.4)",         49,   5, 250 ), #54,4,220),
#     var("jpt_1*(abs(jeta_1)<2.4)",         49,   5, 250 ),
#     var("jpt_1*(abs(jeta_1)>3.0 && jpt_1>30) + jpt_2*((abs(jeta_1)<=3.0||jpt_1<=30) && abs(jeta_2)>3.0 && jpt_2>30)",  49, 5,250),
#     var("jpt_1*(abs(jeta_1)>3.0)",         49,   5, 250 ),
#     var("jpt_2*(abs(jeta_2)>3.0)",         49,   5, 250 ),
#     var("gen_match_2",                      9,  -1,   8 ),
#     var("ttptweight",                     100, 0.8, 1.2 ),
#     ##var("nbtag",                          5,   0,   5 ),
#     ##var("ncbtag*(isData)+ncbtag_jer*(!isData)",  5,   0,   5 ),
#     ##var("njets*(isData)+njets_jer*(!isData)",    5,   0,   5 ),
#     var( "pol_2",                           25,-1.1, 1.1 ),
#     ##var("mt_1",                          40,   0, 200 ),
#     ##var("NUP",                            6,   0,   6 ),
#     var("npu",                             21,   0,  42 ),
#     var("npv",                             21,   0,  42 ),
#     var("puppimet",                        30,   0, 120 ),
#     var("mvamet",                          30,   0, 120 ),
#     var("iso_1",                           10,   0, 0.5 ),
#     var("decayMode_2",                     11,   0,  11 ),
#     var("byIsolationMVA3oldDMwLTraw_2",    30, 0.0, 1.0 ),
]
# for p in [1, 2]:
#     variables.append(var( "pt_%i"    % p,      30,    0, 150   ))
    #variables.append(("eta_%i"   % p,      31, -3.1,   3.1 ))
# for p in [("j",1),("j",2),("b",1), ("b",2)]:
#     variables.append(var("%spt_%i"  % p,      49,    5,   250  ))#40,0,200
#     variables.append(var("%seta_%i" % p,      50, -5.0,   5.0  ))
# for n in [ "iso_2", "againstElectronVLooseMVA6_2", "againstMuonTight3_2" ]:
#     variables.append(var( n,             2, 0,   2 ))

samplesB = [                                                              # cross section [pb]
    ("TT", "TT_TuneCUETP8M1",                      "ttbar",                    831.76, {'extraweight':"ttptweight_runI/ttptweight"} ), #,
    ("ST", "ST_tW_top_5f_inclusiveDecays",         "ST tW",                     35.60  ), #  38.09
    ("ST", "ST_tW_antitop_5f_inclusiveDecays",     "ST atW",                    35.60  ), #  38.09
    ("ST", "ST_t-channel_top_4f_inclusiveDecays",     "ST t",                  136.02  ), #  80.95 # 80.95
    ("ST", "ST_t-channel_antitop_4f_inclusiveDecays", "ST at",                  80.95  ), # 136.02 # 136.02
    ("WW", "WWTo1L1Nu2Q_13TeV_nlo",                "WWTo1L1Nu2Q",               49.997 ),
    ("WZ", "WZTo3LNu_TuneCUETP8M1_13TeV_nlo",      "WZTo3LNu",                   3.05  ),
    ("WZ", "WZTo1L1Nu2Q_13TeV_nlo",                "WZTo1L1Nu2Q",               10.71  ),
    ("WZ", "WZTo2L2Q_13TeV_nlo",                   "WZTo2L2Q",                   5.595 ),
    ("WZ", "WZJToLLLNu_nlo",                       "WZJToLLLNu",                 4.708 ),
    ("VV", "VVTo2L2Nu_13TeV_nlo",                  "VVTo2L2Nu",                 11.95  ),
    ("ZZ", "ZZTo2L2Q_13TeV_nlo",                   "ZZTo2L2Q",                   3.22  ),
    ("ZZ", "ZZTo4L_13TeV_nlo",                     "ZZTo4L",                     1.212 ),
    ("WJ", "WJetsToLNu_TuneCUETP8M1",              "W + jets",               50380.0   ), # LO 50380.0; NLO 61526.7
    ("WJ", "W1JetsToLNu_TuneCUETP8M1",             "W + 1J",                  9644.5   ),
    ("WJ", "W2JetsToLNu_TuneCUETP8M1",             "W + 2J",                  3144.5   ),
    ("WJ", "W3JetsToLNu_TuneCUETP8M1",             "W + 3J",                   954.8   ),
    ("WJ", "W4JetsToLNu_TuneCUETP8M1",             "W + 4J",                   485.6   ),
    ###("DY", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell Yan 10-50",        18610.0   ),
    ("DY", "DYJetsToLL_M-10to50_TuneCUETP8M1",     "Drell-Yan 10-50",        18610.0   ), # 18610
    ("DY", "DY1JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 1J 10-50",       421.5   ), # 421.5
    ("DY", "DY2JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 2J 10-50",       184.3   ), # 184.3
    ("DY", "DY3JetsToLL_M-10to50_TuneCUETP8M1",    "Drell-Yan 3J 10-50",        95.0   ), # ???
    ("DY", "DYJetsToLL_M-50_TuneCUETP8M1",         "Drell-Yan 50",            4954.0   ), # LO 4954.0; NLO 5765.4
    ("DY", "DY1JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 1J 50",         1012.5   ),
    ("DY", "DY2JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 2J 50",          332.8   ),
    ("DY", "DY3JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 3J 50",          101.8   ),
    ("DY", "DY4JetsToLL_M-50_TuneCUETP8M1",        "Drell-Yan 4J 50",           54.8   ),
    ###("WW", "WW_TuneCUETP8M1",                      "WW",                        63.21  ), # 63.21
    ###("WZ", "WZ_TuneCUETP8M1",                      "WZ",                        22.82  ), # 10.71?
    ###("ZZ", "ZZ_TuneCUETP8M1",                      "ZZ",                        10.32  ), #  3.22?
    ###("WW", "WWTo1L1Nu2Q",                          "WW",                        1.212  ), # 1.212
    ###("WW", "WWTo4Q_4f",                            "WW",                        45.31  ), # 45.31
    ###("ST", "ST_tW_top_5f_NoFullyHadronicDecays",      'ST',                     38.09  ), # 
    ###("ST", "ST_tW_antitop_5f_NoFullyHadronicDecays",  'ST',                      0.00  ), # 
    ###("ST", "ST_s-channel_4f_leptonDecays",            'ST',                     10.11  ), # 10.11
    ###("ST", "ST_t-channel_antitop_4f_inclusiveDecays", 'ST',                     80.95  ), # 80.95
    ###("ST", "ST_t-channel_top_4f_inclusiveDecays",     'ST',                      0.00  ), # 
]

samplesD = {
    "mutau" :  ( "SingleMuon",      "SingleMuon_Run2016",     "single muon",     {'blind':blind_dict} ),
    "etau"  :  ( "SingleElectron",  "SingleElectron_Run2016", "single electron", {'blind':blind_dict} ),
    "emu"   :  ( "SingleMuon",      "SingleMuon_Run2016",     "single muon",     {'blind':blind_dict} ),
}

samplesS   = [ ]
VLQ_bqX    = [ ]
VLQ_bqX_MB300 = [ ]
VLQ_bqX_MB450 = [ ]
SUSY_bbA   = [ ]
if 'bbA' in plotlabel or doDataCard:
  SUSY_bbA = [(25,0.021),(30,0.0311),(35,0.04172),(40,0.0568),(45,0.07724),(50,0.09666),(55,0.11672),(60,0.1386),(65,0.157),(70,0.175),]
  if not doDataCard:
    SUSY_bbA = [m for m in SUSY_bbA if m[0]%10==0]
  for mass, eff in SUSY_bbA:
    samplesS.append(( "SUSY", "SUSYGluGluToBBa1ToTauTau_M-%d"%mass, "bbA m_{A}=%d"%mass, 1*eff, { 'upscale': 500/eff } ))
if 'bbA' not in plotlabel or doDataCard:
  VLQ_bqX = [(20,0.6969),(28,1),(40,0.7082),(50,0.7318),(60,0.7685),(70,0.8032)]
  VLQ_bqX_MB300 = [(20,1.),(28,1.),(40,1.),(50,1.),(60,1.),(70,1.)]
  VLQ_bqX_MB450 = [(20,1.),(28,1.),(40,1.),(50,1.),(60,1.),(70,1.)]
  for mass, eff in VLQ_bqX:
    samplesS.append(( "LowMass", "LowMassDiTau_M-%d_MB-%d"%(mass,170), "VLQ m_{B}=%d, m_{X}=%d"%(170,mass), 1*eff, { 'upscale': 500/eff } ))
  if doDataCard:
    for mass, eff in VLQ_bqX_MB300:
      samplesS.append(( "LowMass", "LowMassDiTau_M-%d_MB-%d"%(mass,300), "VLQ m_{B}=%d, m_{X}=%d"%(300,mass), 1*eff ))
    for mass, eff in VLQ_bqX_MB450:
      samplesS.append(( "LowMass", "LowMassDiTau_M-%d_MB-%d"%(mass,450), "VLQ m_{B}=%d, m_{X}=%d"%(450,mass), 1*eff ))

# SAMPLESET
makeSFrameSamples(samplesD,samplesB,samplesS,weight=_weight,binN_weighted=8)
samples = SampleSet(samplesD,samplesB,samplesS)
#samples.printTable()
if stitchWJ:       samples.stitch('W*Jets',        name_incl="WJ",  name="WJ"                                         )
if stitchDY50:     samples.stitch('DY*J*M-50',     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan M=50GeV"     )
if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeDY:        samples.merge( 'DY',                             name="DY",          title="Drell-Yan"             )
if mergeVV:        samples.merge( 'VV','WZ','WW','ZZ',              name="VV",          title="diboson"               )
if mergeST:        samples.merge( 'ST',                             name="ST",          title="single top"            )
if mergeTT:        samples.merge( 'TT',                             name="TT",          title="ttbar"                 )
if splitDY:        samples.splitSample("DY",{'Z -> tautau':           "gen_match_2==5", 'Drell-Yan other': "gen_match_2!=5"})
if splitTT:        samples.splitSample("TT",{'ttbar with real tau_h': "gen_match_2==5", 'ttbar other':     "gen_match_2!=5" }) #'ttbar j -> tau_h': "gen_match_2<5"
#if splitST:        samples.splitSample("ST",{'single top with real tau_h': "gen_match_2==5", 'single top other': "gen_match_2!=5" }) #'ttbar j -> tau_h': "gen_match_2<5"
samples.printTable()
#samples.printSampleObjects()

# SHIFT
samplesB_TESUp, samplesB_TESDown, samplesB_EESUp, samplesB_EESDown, samplesB_JTFUp, samplesB_JTFDown = [ ], [ ], [ ], [ ], [ ], [ ]
if doTES:
  samplesB_TESUp   = samples.shiftSample(['TT','ST','DY'],"_TES1p03"," +3% TES", title_veto="other")
  samplesB_TESDown = samples.shiftSample(['TT','ST','DY'],"_TES0p97"," -3% TES", title_veto="other")
if doLTF:
  samplesB_LTFUp   = samples.shiftSample(['TT','ST','DY'],"_LTF1p10"," +3% LTF ES", filter=not doStack, title_veto="real")
  samplesB_LTFDown = samples.shiftSample(['TT','ST','DY'],"_LTF0p90"," -3% LTF ES", filter=not doStack, title_veto="real")
if doJTF:
  samplesB_JTFUp   = samples.shiftSample(['TT','ST','WJ'],"_JTF1p10"," +10% JTF ES", filter=not doStack, title_veto="real")
  samplesB_JTFDown = samples.shiftSample(['TT','ST','WJ'],"_JTF0p90"," -10% JTF ES", filter=not doStack, title_veto="real")


