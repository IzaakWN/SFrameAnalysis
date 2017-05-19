#! /usr/bin/env python

import time
start = time.time()
import os, sys #, ROOT
from ROOT import TFile, TTree, TObject
#import numpy # to set branch addres
from math import log, pow, floor

# https://root.cern.ch/root/html/tutorials/tree/copytree.C.html
# https://root.cern.ch/root/html/tutorials/tree/copytree3.C.html
# to get branch channel with string "channel": getattr(oldtree,"channel")

# /scratch/ineuteli/SFrameAnalysis/AnalysisOutput/
# /shome/ineuteli/analysis/SFrameAnalysis/AnalysisOutput/

mylabel     = "_Moriond"
DIR         = "."
doLFT       = True #and False
doEES       = True and False
doTES       = True #and False
doNominal   = True and False


# CUTS
isocuts   = "iso_cuts==1"
vetos     = "lepton_vetos==0"
ptcut     = "(pt_1>26||(channel==1 && pt_1>23))"
triggers  = "abs(eta_1)<2.1 && (( %s && (triggers==1||triggers==3))||(triggers>1))" % ptcut



    #################
    # makeThreshold #
    #################

def makeThreshold(n,**kwargs):
    """Help function to find a good stepsize for read out when looping over a large number N.
       In a for loop with index i, you could do a print out like:
         if i % threshold == 0: print "some progress message" """
    max_digits = kwargs.get('max',6)
    #                      floor(log(N/10.0,10))        stepsize = (number of digits in N) - 2
    #              max(0.0,floor(log(N/10.0,10)))       make sure it is at least 0
    #        min(6,max(0.0,floor(log(N/10.0,10))))      set maximum step size to 10^6 (otherwise one has to wait too long for an update)
    # pow(10,min(6,max(0.0,floor(log(N/10.0,10)))))     make treshold a power of 10
    return pow(10,min(max_digits,max(0.0,floor(log(n/10.0,10)))))



    ###########
    # cutTree #
    ###########

def cutTree(oldfilename, treenames, **kwargs):
    """Extract tree from file and save in new one."""
    start_here = time.time()
    
    # TREENAME
    treename = ""
    if isinstance(treenames,str): treenames = [treenames]
    if len(treenames) == 1:       treename  = "_%s"%treenames[0]
    print ">>>\n>>> extracting tree(s) from file"
    N           = kwargs.get('N',-1)
    
    # CUTS
    cuts        = kwargs.get('cuts',"channel>0")
    if isinstance(cuts,str):      cuts = [cuts]*len(treenames)
    if len(treenames)!=len(cuts): print ">>> Warning! len(treenames)!=len(cuts)"
    
    # FILE OPTIONS
    newfilename = kwargs.get('newfilename',False)
    update      = kwargs.get('update',False)
    if not newfilename:
        if update: newfilename = oldfilename
        else:      newfilename = oldfilename.replace(".root","%s_string.root"%(treename))
    copycontents = kwargs.get('copycontents',False) and oldfilename!=newfilename
    option      = 'read' if copycontents else ('update' if update else 'recreate')
    option      = kwargs.get('option',option)
    label       = kwargs.get('label',"_cut" if (oldfilename==newfilename) else "")
    
    # FILE
    oldfile     = TFile(oldfilename)
    if copycontents: succes = oldfile.Cp(newfilename,True)
    newfile     = TFile(newfilename,'update')
    
    # PRINT
    print ">>>   file in:    \"%s\"" % (oldfilename)
    print ">>>   file out:   \"%s\"" % (newfilename)
    print ">>>   tree label: \"%s\"" % (label)
    print ">>>   settings:   update=%s, option=\"%s\", copycontents=%s" % (update,option,copycontents)
    
    for treename, cut in zip(treenames,cuts):
        oldtree     = oldfile.Get(treename)
        newtreename = treename+label
        print ">>>   copying tree \"%s\" into \"%s\" with cuts" % (treename,newtreename)
        print ">>>     \"%s\"" % (cut)
        newtree     = None
        maxmessage  = ""
        if N>0:
            newtree    = oldtree.CopyTree(cut,"",N)
            maxmessage = " (max %i)"%N
        else:
            newtree = oldtree.CopyTree(cut)
        #newtree.SetName(newtreename)
        newtree.Write(newtreename,TObject.kOverwrite)
        print ">>>   extraction done: %i%s of %i entries copied" % (newtree.GetEntries(),maxmessage,oldtree.GetEntries())
    
    print ">>>   writing and closing new file: %s" % (newfilename)  
    #newfile.Write(TObject.kOverwrite)
    newfile.Close()
    oldfile.Close()

    print ">>>   took %.2f seconds." % (time.time()-start_here)
    




    ##################
    # Help functions #
    ##################

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR

def color(string,**kwargs):
    """Color"""
    # http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
    text_color_dict = { "black"     : "0;30;",  "red"       : "1;31;",
                        "green"     : "0;32;",  "yellow"    : "1;33;", "orange"    : "1;33;",
                        "blue"      : "1;34;",  "purple"    : "0;35;",
                        "magenta"   : "1;36;",  "grey"      : "0;37;",  }
    background_color_dict = {   "black"     : "40", "red"       : "41",
                                "green"     : "42", "yellow"    : "43", "orange"    : "43",
                                "blue"      : "44", "purple"    : "45",
                                "magenta"   : "46", "grey"      : "47", }                  
    color_code = text_color_dict[kwargs.get('color',"red")] + background_color_dict[kwargs.get('background',"black")]
    return kwargs.get('prepend',"") + "\x1b[%sm%s\033[0m" % ( color_code, string )

def warning(string,**kwargs):
    return color("Warning! "+string, color="yellow", prepend=">>> "+kwargs.get('prepend',""))
    
def error(string,**kwargs):
    return color("ERROR! "+string, color="red", prepend=">>> "+kwargs.get('prepend',""))





    ########
    # main #
    ########

def main():
    """Main method: list files and which trees to extract."""
    
    # FILES
    files = [
        ( "LowMass",         "LowMass_30GeV_DiTauResonance" ),
        ( "SingleMuon",      "SingleMuon_Run2016"           ),
        ( "SingleElectron",  "SingleElectron_Run2016"       ),
        ( "TT", "TT_TuneCUETP8M1"                           ),
        ( "DY", "DYJetsToLL_M-10to50_TuneCUETP8M1"          ),
        ( "DY", "DY1JetsToLL_M-10to50_TuneCUETP8M1"         ),
        ( "DY", "DY2JetsToLL_M-10to50_TuneCUETP8M1"         ),
        ( "DY", "DY3JetsToLL_M-10to50_TuneCUETP8M1"         ), 
        ( "DY", "DYJetsToLL_M-50_TuneCUETP8M1"              ), 
        ( "DY", "DY1JetsToLL_M-50_TuneCUETP8M1"             ),
        ( "DY", "DY2JetsToLL_M-50_TuneCUETP8M1"             ),
        ( "DY", "DY3JetsToLL_M-50_TuneCUETP8M1"             ),
        ( "DY", "DY4JetsToLL_M-50_TuneCUETP8M1"             ),
        ( "WJ", "WJetsToLNu_TuneCUETP8M1"                   ), 
        ( "WJ", "W1JetsToLNu_TuneCUETP8M1"                  ),
        ( "WJ", "W2JetsToLNu_TuneCUETP8M1"                  ),
        ( "WJ", "W3JetsToLNu_TuneCUETP8M1"                  ),
        ( "WJ", "W4JetsToLNu_TuneCUETP8M1"                  ),
        ( "WW", "WWTo1L1Nu2Q_13TeV_nlo"                     ),
        ( "WZ", "WZTo3LNu_TuneCUETP8M1_13TeV_nlo"           ),
        ( "WZ", "WZTo1L1Nu2Q_13TeV_nlo"                     ),
        ( "WZ", "WZTo2L2Q_13TeV_nlo"                        ),
        ( "WZ", "WZJToLLLNu_nlo"                            ),
        ( "ZZ", "VVTo2L2Nu_13TeV_nlo"                       ),
        ( "ZZ", "ZZTo2L2Q_13TeV_nlo"                        ),
        ( "ZZ", "ZZTo4L_13TeV_nlo"                          ),
        ( "ST", "ST_tW_top_5f_inclusiveDecays"              ),
        ( "ST", "ST_tW_antitop_5f_inclusiveDecays"          ),
        ( "ST", "ST_t-channel_top_4f_inclusiveDecays"       ),
        ( "ST", "ST_t-channel_antitop_4f_inclusiveDecays"   ),
             ]
    
    
    # SHIFTS
    newfiles = []
    if doEES:
      for subdir,filename in files:
        newfiles.append((subdir,filename+"_EES0p99"))
        newfiles.append((subdir,filename+"_EES1p01"))
    if doTES:
      for subdir,filename in files:
        if subdir in ["DY","TT","LowMass"]:
          newfiles.append((subdir,filename+"_TES0p97"))
          newfiles.append((subdir,filename+"_TES1p03"))
    if doLFT:
      for subdir,filename in files:
        if subdir in ["DY"]:
          newfiles.append((subdir,filename+"_LTF0p97"))
          newfiles.append((subdir,filename+"_LTF1p03"))
    if doNominal: files += newfiles
    else:         files  = newfiles
    
    
    # CHANNEL & TREENAMES
    channels  = [   "mutau",
                    "etau"
                ]
    treenames = ["tree_%s"%c for c in channels]
    
    
    Nmax      = -1 #000000
    cuts      = "channel>0 && abs(eta_1)<2.1 && %s && %s" % (isocuts,vetos)
    OUTDIR    = "%s/trimmed"%DIR; ensureDirectory(OUTDIR)
    for subdir, samples in files:
        oldfilename = "%s/%s/TauTauAnalysis.%s%s.root" % (DIR,subdir,samples,mylabel)
        newdir      = "%s/%s"%(OUTDIR,subdir); ensureDirectory(newdir)
        newfilename = "%s/TauTauAnalysis.%s%s.root" % (newdir,samples,mylabel)
        if os.path.isfile(oldfilename):
            print oldfilename
            #cutTree(oldfilename,treenames,cuts=cuts,newfilename=newfilename,copycontents=True)
            #cutTree(oldfilename,treenames,cuts=cuts,update=True)
        else: print warning("%s Does not exist!"%oldfilename)




if __name__ == '__main__':
    print
    main()
    end = time.time()
    print ">>>\n>>> done in %.2f seconds\n" % (end-start)



# TODO: use TTreeFormula to cut tree
# TODO: check efficiency
# https://root.cern.ch/root/roottalk/roottalk04/2010.html
# https://root.cern.ch/phpBB3/viewtopic.php?t=16775
# 
# newtree     = oldtree.CloneTree(0) # TTree(treename, treename)    
# print ">>> make TTreeFormula and GetNData"
# cut_form = TTreeFormula( 'channel', cut, oldtree )
# cut_form.GetNdata()
# 
# print ">>> selecting and copying entries"
# N = kwargs.get('N',oldtree.GetEntries())
# threshold = makeThreshold(N)
# for i in range(N):
#     if i % threshold == 0: print ">>>\t%5.2f%%: copied %i entries of %i" % (100.0*i/N,i,N)
#     oldtree.GetEntry(i)
#     if cut_form.EvalInstance(i) is not 0:
#         newtree.Fill()

# def makeTree(filename, treename, **kwargs):
#     """Extract tree from file and save in new one."""
#     print ">>>\n>>> extracting tree %s from %s" % (treename,filename)
#     start_here = time.time()
#     
#     channel = 0
#     if "mutau" in treename:  channel = 1
#     elif "etau" in treename: channel = 2
#     
#     oldfile     = TFile(filename)
#     oldtree     = oldfile.Get(treename)
#     newfilename = kwargs.get('newfilename',filename.replace( ".root", "_%s.root" % treename ))
#     newfile     = TFile(newfilename, 'recreate')
#     
#     print ">>> cloning tree"
#     newtree     = oldtree.CloneTree(0) # TTree(treename, treename)
#     
#     print ">>> selecting and copying entries"
#     N           = kwargs.get('N',oldtree.GetEntries())
#     threshold   = makeThreshold(N)
#     for i in range(N):
#         if i % threshold == 0: print ">>>\t%5.2f%%: copied %i entries of %i" % (100.0*i/N,i,N)
#         oldtree.GetEntry(i)
#         if oldtree.channel == channel:
#             newtree.Fill()
# 
#     newN = oldtree.GetEntries()
#     print ">>> extraction of %s done: %i of %i entries copied" % (treename,N,newN)
#     print ">>> writing and closing new file: %s" % (newfilename)
#     newfile.Write()
#     newfile.Close()
#     oldfile.Close()
#     
#     print ">>> took %.2f seconds." % (time.time()-start_here)
#     print ">>> "
