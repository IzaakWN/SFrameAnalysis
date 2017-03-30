#!/usr/bin/env python
#python extractEfficiencies.py ../../AnalysisOutput/Nak8_v0/*root -w Loose -p jet_  -r
#python extractEfficiencies.py ../../AnalysisOutput/prova_justTauIso_LepPairPt_StandardID_EleTight_MuTight_15p9fb_69p2_PW_filters_VetoMediumWP/*root -w Tight -p jet_ak4_

#python extractEfficiencies.py ../../AnalysisOutput/Nak8_v0/*root -w Medium -p jet_ak4_ 
#python extractEfficiencies.py ../../AnalysisOutput/Nak8_v0/*root -w Loose -p subjet_softdrop_  
import os
import sys
from optparse import OptionParser
from ROOT import *

def main():
  
  parser = OptionParser(usage="usage: %prog [options] inputFiles")
  parser.add_option("-o", "--output", dest="outputFile", default="bTagEffs.root", action="store",
                    help="name of output ROOT file [default: %default]")
  parser.add_option("-d", "--directory", dest="directory", default="bTagEff", action="store",
                    help="name of directory containing histograms within ROOT file [default: %default]")
  parser.add_option("-p", "--prefix", dest="prefix", default="jet_", action="store",
                    help="prefix for histograms [default: %default]")
  parser.add_option("-w", "--workingpoint", dest="workingpoint", default="Loose", action="store",
                    help="b-tagging working point [default: %default]")
  parser.add_option("-r", "--replace", dest="replace", default=False, action="store_true",
                    help="replace/overwrite/recreate output ROOT file [default: %default]")
  parser.add_option("-v", "--verbose", dest="verbose", default=False, action="store_true",
                    help="make script verbose")

  
  (options, args) = parser.parse_args()
  
  if len(args) < 1:
    parser.error("Please provide at least one ROOT file name")

  fileList = args
  outputFile = options.outputFile
  directory = options.directory
  prefix = options.prefix
  workingpoint = options.workingpoint
  replace = options.replace
  verbose = options.verbose

  print "Using file list:", fileList
  print "output ROOT file:", outputFile
  print "Using histogram directory:", directory
  print "Using histogram prefix:", prefix
  print "Using b-tagging working point:", workingpoint
  print "Replacing output ROOT file:", replace
  print "-"*80
  
  # this is hardcoded, but should be fine
  flavourNames = ["udsg", "b", "c"]
  nominator = "_"+workingpoint
  denominator = "_all"
  
  files = []
  for file in fileList:
    files.append(TFile(file))

  # print files
  nomHists = {}
  denomHists = {}
  effHists = {}
  for flavour in flavourNames:
    flavNomHist = 0
    flavDenomHist = 0
    for i,file in enumerate(files):
      
      baseHistName = "%s/%s%s" %(directory, prefix, flavour)
      baseHistNameNoDir = "%s%s" %(prefix, flavour)
      if verbose: print "Getting histograms for ",baseHistNameNoDir,"in file",file
     
      if (i == 0):
        print "file.Get(%s%s)).Clone(%s%s%03d)"%(baseHistName, nominator,baseHistNameNoDir, nominator, i)
        nomHist = file.Get("%s%s" %(baseHistName, nominator)).Clone("%s%s%03d" %(baseHistNameNoDir, nominator, i))
        denomHist = file.Get("%s%s" %(baseHistName, denominator)).Clone("%s%s%03d" %(baseHistNameNoDir, denominator, i))
        flavNomHist = nomHist.Clone("%s%s_sum" %(baseHistNameNoDir, nominator))
        flavDenomHist = denomHist.Clone("%s%s_sum" %(baseHistNameNoDir, denominator))
      else:
     
        nomHist = file.Get("%s%s" %(baseHistName, nominator)).Clone("%s%s%03d" %(baseHistNameNoDir, nominator, i))
        denomHist = file.Get("%s%s" %(baseHistName, denominator)).Clone("%s%s%03d" %(baseHistNameNoDir, denominator, i))
        flavNomHist.Add(nomHist)
        flavDenomHist.Add(denomHist)
    nomHists[flavour] = flavNomHist
    denomHists[flavour] = flavDenomHist
    effHists[flavour] = flavNomHist.Clone("%s%s_eff" %(baseHistNameNoDir, nominator))
    effHists[flavour].Divide(flavDenomHist)
    nomHists[flavour].SetName("%s%s" %(baseHistNameNoDir, nominator))
    denomHists[flavour].SetName("%s%s" %(baseHistNameNoDir, denominator))
  
  #plot histograms
  
  
  #write out file
  openOptions = "UPDATE"
  if (replace):
    openOptions = "RECREATE"
  outFile = TFile.Open(outputFile, openOptions)
  if (replace or not outFile.GetDirectory(directory)):
    outFile.mkdir(directory)
    print ">>> made directory %s in %s" % (directory,outputFile) # if verbose:
  outFile.cd(directory)
  outDir = outFile.GetDirectory(directory)
  for flavour in flavourNames:
    if (outDir.GetListOfKeys().Contains(nomHists[flavour].GetName())):
      print "ERROR: histogram already exist in output file."
      sys.exit(1)
    nomHists[flavour].Write()
    denomHists[flavour].Write()
    effHists[flavour].Write()
  outFile.Write()
  outFile.Close()
  
  
  for file in files:
    file.Close()
  
  


if __name__ == "__main__":
  main()
