# Author: Izaak Neutelings (2017)
# Config file for plot.py

#### SETTINGS ############################################################################

# LABELS & LUMI
globalTag   = "_Moriond" # extra label for opening file, saving plots to dir
plotlabel   = "_test" #_JEC_check" #_eta-weighted #_noForwardTTCR #_2xb30GeV" # extra label for image file
luminosity  = 35.9

# VERBOSITY
verbosity               = 2
verbositySampleTools    = 2
verbosityPlotTools      = 2
verbosityVariableTools  = 0
verbositySelectionTools = 0

# PLOTS OPTIONS
doStack             = True #and False
useCutTree          = True #and False
normalizeWJ         = True #and False
doQCD               = True #and False

# SAMPLE OPTIONS
splitDY             = True and False
stitchWJ            = True #and False
stitchDY50          = True #and False
stitchDY10to50      = True #and False
mergeDY             = True #and False
mergeST             = True #and False
mergeVV             = True #and False

# SAMPLES
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsToTauTauWorking2016#MC_and_data_samples
SFRAME              = "SFrameAnalysis_ltau2017" #Moriond"
SAMPLE_DIR          = os.path.expandvars("/scratch/ineuteli/SFrameAnalysis/AnalysisOutput")
PLOTS_DIR           = os.path.expandvars("/shome/ineuteli/analysis/%s/plots"%SFRAME)
DATACARDS_DIR       = "%s/%s"%(PLOTS_DIR,"datacards")

#### END SETTINGS ########################################################################


channels = [
    "mutau",
    #"etau",
    #"emu",
]


# CATEGORIES / SELECTIONS
_weight      = "weight*trigweight_or_1"
isocuts      = "iso_cuts==1"
vetos        = "lepton_vetos==0"
ptcut        = "(pt_1>26||(channel==1 && pt_1>23))"
triggers     = "abs(eta_1)<2.1 && trigger_cuts==1" # && ((%s && (triggers==1||triggers==3))||(triggers>1))" #% ptcut #pt_1>20 &&
baseline     = "channel>0 && %s && %s && q_1*q_2<0 && %s" % (isocuts,vetos,triggers) # +" && bpt_1>30" #+" && jpt_1>30" && jpt_2>30
selections   = [
    #Selection("no cuts",                ""                              ),
    Selection("baseline",               "%s" % (baseline)               ),
]


# VARIABLES
variables = [
    #Variable("m_vis",                                  35,   0.0, 140  ),
    Variable("pfmt_1",                                  40,   0.0, 200  ),
    Variable("pt_1",   "muon pt",                       40,   0.0, 200  ),
    Variable("byIsolationMVA3oldDMwLTraw_2",            50,   0.8, 1.0, filename="byIsolationMVA3oldDMwLTraw_2_zoom0p8" ),
]

samplesB = [
    ("TT", "TT_TuneCUETP8M1",                         "ttbar",                 831.76, {'extraweight':_weight+"*ttptweight_runI/ttptweight"} ),
    ("DY", "DYJetsToLL_M-10to50_TuneCUETP8M1",        "Drell-Yan 10-50",     18610.0   ),
    ("DY", "DY1JetsToLL_M-10to50_TuneCUETP8M1",       "Drell-Yan 1J 10-50",    421.5   ),
    ("DY", "DY2JetsToLL_M-10to50_TuneCUETP8M1",       "Drell-Yan 2J 10-50",    184.3   ),
    ("DY", "DY3JetsToLL_M-10to50_TuneCUETP8M1",       "Drell-Yan 3J 10-50",     95.0   ), # LO 4954.0; NLO 5765.4
    ("DY", "DYJetsToLL_M-50_TuneCUETP8M1",            "Drell-Yan 50",         4954.0   ), # 
    ("DY", "DY1JetsToLL_M-50_TuneCUETP8M1",           "Drell-Yan 1J 50",      1012.5   ),
    ("DY", "DY2JetsToLL_M-50_TuneCUETP8M1",           "Drell-Yan 2J 50",       332.8   ),
    ("DY", "DY3JetsToLL_M-50_TuneCUETP8M1",           "Drell-Yan 3J 50",       101.8   ),
    ("DY", "DY4JetsToLL_M-50_TuneCUETP8M1",           "Drell-Yan 4J 50",        54.8   ),
    ("WJ", "WJetsToLNu_TuneCUETP8M1",                 "W + jets",            50380.0   ), # LO 50380.0; NLO 61526.7
    ("WJ", "W1JetsToLNu_TuneCUETP8M1",                "W + 1J",               9644.5   ),
    ("WJ", "W2JetsToLNu_TuneCUETP8M1",                "W + 2J",               3144.5   ),
    ("WJ", "W3JetsToLNu_TuneCUETP8M1",                "W + 3J",                954.8   ),
    ("WJ", "W4JetsToLNu_TuneCUETP8M1",                "W + 4J",                485.6   ),
    ("WW", "WWTo1L1Nu2Q_13TeV_nlo",                   "WWTo1L1Nu2Q",            49.997 ),
    ("WZ", "WZTo3LNu_TuneCUETP8M1_13TeV_nlo",         "WZTo3LNu",                3.05  ),
    ("WZ", "WZTo1L1Nu2Q_13TeV_nlo",                   "WZTo1L1Nu2Q",            10.71  ),
    ("WZ", "WZTo2L2Q_13TeV_nlo",                      "WZTo2L2Q",                5.595 ),
    ("WZ", "WZJToLLLNu_nlo",                          "WZJToLLLNu",              4.708 ),
    ("VV", "VVTo2L2Nu_13TeV_nlo",                     "VVTo2L2Nu",              11.95  ),
    ("ZZ", "ZZTo2L2Q_13TeV_nlo",                      "ZZTo2L2Q",                3.22  ),
    ("ZZ", "ZZTo4L_13TeV_nlo",                        "ZZTo4L",                  1.212 ),
    ("ST", "ST_tW_top_5f_inclusiveDecays",            "ST tW",                  35.60  ), #  38.09
    ("ST", "ST_tW_antitop_5f_inclusiveDecays",        "ST atW",                 35.60  ), #  38.09
    ("ST", "ST_t-channel_top_4f_inclusiveDecays",     "ST t",                  136.02  ), #  80.95
    ("ST", "ST_t-channel_antitop_4f_inclusiveDecays", "ST at",                  80.95  ), # 136.02
]

samplesS = [
    #( "LowMass", "LowMass_28GeV_DiTauResonance",      "signal",               1000.0   ),
]

samplesD = {
    "mutau" :  ( "SingleMuon",     "SingleMuon_Run2016",     "single muon"     ),
    "etau"  :  ( "SingleElectron", "SingleElectron_Run2016", "single electron" ),
}

makeSFrameSamples(samplesB,samplesS,samplesD,weight=_weight)
samples = SampleSet(samplesB,samplesS,samplesD)
samples.printTable()
if stitchWJ:       samples.stitch("W*Jets",        name_incl="WJ",  name="WJ"                                         )
if stitchDY50:     samples.stitch("DY*J*M-50",     name_incl="DYJ", name="DY_M-50",     title="Drell-Yan M=50GeV"     )
if stitchDY10to50: samples.stitch("DY*J*M-10to50", name_incl="DYJ", name="DY_M-10to50", title="Drell-Yan 10<M<50GeV"  )
if mergeVV:        samples.merge( "VV","VV","WZ","WW","ZZ",         name="diboson",     title="diboson"               )
if mergeST:        samples.merge( "ST",                             name="ST",          title="single top"            )
if mergeDY:        samples.merge( "DY",                             name="DY",          title="Drell Yan"             )
samples.splitSample("DY",{'Z -> tautau': "gen_match_2==5", 'Drell-Yan other': "gen_match_2!=5",})
samples.splitSample("TT",{'ttbar with real tau_h': "gen_match_2==5", 'ttbar other': "gen_match_2!=5" }) #'ttbar j -> tau_h': "gen_match_2<5"
#samples.printTable()

