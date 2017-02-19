#!/usr/bin/env python
# -*- coding: utf-8 -*-
#***************************************************************************
#* @Project: creating XML files for SFrame
#* @author Clemens Lange    <clange@physik.uzh.ch>        - UZH
#*
#***************************************************************************
#
# Get text file with full paths of ntuples (18/02/2017):
#  
#  Tier 3 PNFS:
#    PNFS="/pnfs/psi.ch/cms/trivcat/store/t3groups/uniz-higgs/Summer16/Ntuple_80_20170206/"
#    ls -d $PNFS/DYJ*/*/*/* > dirs_DYJ.txt
#    ls -d $PNFS/*/*/*/* > dirs.txt
#    ./createXMLfile.py dirs.txt -o xmls_Moriond
#  
#  Tier 2 PNFS:
#    PNFS="gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/ytakahas/Ntuple_Moriond17/"
#    uberftp -ls $PNFS/DY1J*/*/* | awk '{print $7}' > dirs_T2_DY1J.txt
#    uberftp -ls $PNFS/*/*/* | awk '{print $7}' > dirs_T2.txt
#    ./createXMLfile.py dirs_T2.txt -o xmls_Moriond_T2 -s PSI-T2
#
#  Print out xml file names formatted for copy-pasting into job options files:
#    cd xmls_Moriond/
#    ls *.xml | xargs -I@ echo \"@\",
#


import os
import sys
import re
import optparse
import thread
import subprocess
import math


# parse the command line
parser=optparse.OptionParser(usage="%prog sampleListFile")
parser.add_option("-s", "--site", action="store",
                dest="site", default="PSI",
                help="grid site [default = %default]")
parser.add_option("-v", "--verbose", action="store_true",
                dest="verbose", default=False,
                help="verbose output [default = %default]")
parser.add_option("-x", "--xrootd", action="store_true",
                dest="useXrootd", default=False,
                help="use Xrootd [default = %default]")
parser.add_option("-t", "--tree", action="store",
                dest="treeName", default="ntuplizer/tree",
                help="Tree to be scanned by SFrame for number of input events [default = %default]")
parser.add_option("-m", "--maxFiles", action="store",
                dest="maxFiles", default="350",
                help="Maximum number of files [default = %default]")
parser.add_option("-o", "--outDir", action="store",
                dest="outDir", default="xmls_Summer2016",
                help="Output directory for xml files [default = %default]")
(options, args) = parser.parse_args()
if len(args) != 1: parser.error("Please provide at file list name")

sampleListName = args[0]
site=options.site
verbose=options.verbose
useXrootd=options.useXrootd
treeName=options.treeName
maxFiles_original=int(options.maxFiles)
outDir=options.outDir
if verbose: print "Site:",site



dCacheInstances={}
#Xrootd and dcap prefixes
dCacheInstances["PSI"]=["root://t3dcachedb.psi.ch:1094/", "dcap://t3se01.psi.ch:22125/"]
dCacheInstances["PSI-T2"]=["root://storage01.lcg.cscs.ch/",  "root://storage01.lcg.cscs.ch/"] # PSI Tier 2



def main():
  
  if not os.path.exists(outDir):
    print "Creating output directory", outDir
    os.makedirs(outDir)
  
  with open(sampleListName) as sampleList:
    for sample in sampleList:
      if sample.startswith("#") or sample.isspace():
        continue
      print "- "*10
      sample = sample.strip("\n")
      sampleName = (sample.strip("/")).rsplit("/",1)[1]
      sampleName_file=(sample.strip("/")).rsplit("/",3)[1]
      sampleName_file+="_"+sampleName
      print "Sample: %s in location: %s producing file with list %s" %(sampleName,sample,sampleName_file )
      fileList=[]
      if not isDir(sample):
        print sample,"is not a directory."
      else:
        prefix = ""
        if (sample.startswith("/pnfs")):
          if (site not in dCacheInstances):
            print "Gridsite doesn't have dCache instances defined."
            sys.exit(1)
          if (useXrootd):
            prefix = dCacheInstances[site][0]
          else:
            prefix = dCacheInstances[site][1]
        if verbose:
          print "Using prefix:",prefix
        for subdir, files in getFiles(sample):
          for file in files:
            if (file.find(".root") >= 0):
              path = prefix + os.path.join(sample, subdir, file)
              if (verbose): print path
              if "failed" in path.lower() or "corrupt" in path.lower(): continue
              fileList.append(path)
        
        print "Processing %d files"%len(fileList)
        nFiles=int(math.ceil(len(fileList)/float(maxFiles_original)))
        if (nFiles > 1):
          maxFiles = int(math.ceil(len(fileList)/float(nFiles)))
          print "splitting file into %d subfiles of max. %d input files each" %(nFiles, maxFiles)
        else :
          maxFiles = int(maxFiles_original)
        if (len(fileList) == 0):
          print "No files found."
        for i in range(nFiles):
          if (nFiles > 1):
            outName = "%s_%d" %(sampleName_file, i)
          else:
            outName = sampleName_file
          csvList = ""
          for fileIndex in range(i*maxFiles,min((i+1)*maxFiles,len(fileList))):
            csvList = csvList+fileList[fileIndex]+","
          csvList = csvList.strip(",")
          lock=thread.allocate_lock()
          lock.acquire()
          commandMC="sframe_input.py -r -d -o %s/%s.xml %s -t %s" %(outDir, outName, csvList, treeName)
          if verbose:
            print commandMC
          processMC=subprocess.Popen(commandMC, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
          lock.release()
          output=processMC.stdout.read()
          if verbose:
            print output
          else:
            for line in output.split("\n"):
              if "events processed" in line:
                print line.strip("\n")
          outerr=processMC.stderr.read()
          print outerr
        


def getFiles(samplepath):
  '''Generator to loop over files in some directory.'''
  if "T2" in site:
    lock=thread.allocate_lock()
    lock.acquire()
    commandLS="uberftp -ls -r gsiftp://storage01.lcg.cscs.ch/%s | awk '{print $8}'"%(samplepath)
    if verbose: print commandLS
    processLS=subprocess.Popen(commandLS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    lock.release()
    subdirs_dict={}
    for line in processLS.stdout:
      if line.find(".root") <= 0: continue
      subdirs_dict.setdefault(os.path.dirname(line),[]).append(os.path.basename(line.strip()))
    for subdir,files in subdirs_dict.items():
      if verbose: print "subdir=%s, files=%s" % (subdir,files)
      yield (subdir,files)
  else:
    for subdir,dirs,files in os.walk(samplepath):
      if verbose: print "subdir=%s, files=%s" % (subdir,files)
      yield (subdir,files)
  


def isDir(samplepath):
  '''Help function check the existence of a directory.'''
  if "T2" in site:
    lock=thread.allocate_lock()
    lock.acquire()
    commandLS="uberftp -ls gsiftp://storage01.lcg.cscs.ch/%s"%(samplepath)
    if verbose: print commandLS
    processLS=subprocess.Popen(commandLS, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    lock.release()
    output=processLS.stderr.read()
    if verbose: print "isDir: stdout: %s"%processLS.stdout.read()
    if verbose: print "isDir: stderr: %s"%output
    return "No match for" not in output
  else:
    return os.path.isdir(samplepath)
  


if __name__ == "__main__":
  main()
