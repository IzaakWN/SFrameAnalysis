#! /usr/bin/env python
# -*- coding: utf-8 -*-
#***************************************************************************
#* @Project: add XML files for SFrame
#* @author Izaak Neutelings <iwn_@uzh.ch> - UZH
#***************************************************************************

import os, sys
import time
import glob
import re
import math
import optparse

# parse the command line
parser=optparse.OptionParser(usage="%prog SAMPLELISTFILE") #epilog
parser.add_option("-v", "--verbose", action="store_true",
                dest="verbose", default=False,
                help="Verbose output [default = %default]")
parser.add_option("-o", "--outDir", action="store",
                dest="outDir", default=".",
                help="Output directory for merged xml file [default = %default]")
(options, args) = parser.parse_args()

print
verbose        = options.verbose
outDir         = options.outDir  



def main():
    
    nFiles = 0
    shifts = [ ]
    
    shifts.append(( "JTF", "JTFshift",  0.10, 2, [ "Background_TT.py", "Background_ST.py" ], False ))
    shifts.append(( "EES", "EESshift",  0.03, 2, [ "Background_TT.py", "Background_ST.py" ], False ))
    
    if outDir: ensureDirectory(outDir)
    
    for shiftname, shiftvar, shiftvalue, precision, shiftfiles, noTight in shifts:
      if float(shiftvalue)==0.0: continue
      
      labelFormat     = "%%s%%.%df"%(precision)
      valueFormat     = "%%.%df"%(precision)
      labelShiftDn    = (labelFormat%(shiftname,1.-shiftvalue)).replace('.','p')
      labelShiftUp    = (labelFormat%(shiftname,1.+shiftvalue)).replace('.','p')
      shiftvalue      = valueFormat%shiftvalue
      
      for fileInName in shiftfiles:
        
        # CHECK
        if not os.path.exists(fileInName):
          error("\"%s\" does not exists!\n"%(fileInName))
          exit(1)
        
        # INPUT files
        with open(fileInName,'r') as fileIn:
          #print ">>>\n>>> %s: %s"%(shiftname,fileInName)
          
          postFixpattern  = r'.*postFix.*=.*"([^"]*)"'
          valuepattern    = (r'\[.*%s.*,.*"(\d\.\d+)".*\]'%(shiftvar)) #re.escape
          tightpattern    = (r'\[.*%s.*,.*"(\w+)".*\]'%("noTight")) #re.escape
          fileShiftDnName = fileInName.replace('.py',"_%s.py"%(labelShiftDn))
          fileShiftUpName = fileInName.replace('.py',"_%s.py"%(labelShiftUp))
          if outDir:
            fileShiftDnName = "%s/%s"%(outDir,fileShiftDnName)
            fileShiftUpName = "%s/%s"%(outDir,fileShiftUpName)
          
          for sign, fileOutName, shiftlabel in [('-',fileShiftDnName,labelShiftDn),('',fileShiftUpName,labelShiftUp)]:
            print ">>>\n>>> %s"%(green(fileOutName))
            
            # READ input xml file
            foundPostFixLine = False
            foundValueLine   = False
            foundNoTightLine = False
            with open(fileOutName,'w') as fileOut:
              fileIn.seek(0)
              for line in fileIn:
                #if "[" in line: print line.replace('\n','')
                postFixmatches = re.findall(postFixpattern,line)
                valuematches   = re.findall(valuepattern,line)
                tightmatches   = re.findall(tightpattern,line)
                
                if postFixmatches:
                    postFixmatch = postFixmatches[0]
                    if len(postFixmatches)>1:
                        error('Two matches for "%s" in file "%s":'%("postFix",fileInName))
                        error('  "%s"!'%(line))
                        exit(1)
                    if foundPostFixLine:
                        error('Reoccuring "%s" in file "%s"'%("postFix",fileInName))
                        error('  "%s"!'%(line))
                        exit(1)
                    foundPostFixLine = True
                    oldpattern = '(.*postFix.*=.*)"%s"(.*)'%(postFixmatch)
                    newpattern = '%s"_%s%s"%s'%(r"\1",shiftlabel,postFixmatch,r"\2")
                    oldline    = line.replace('\n','')
                    line       = re.sub(oldpattern,newpattern,line)
                    newline    = line.replace('\n','')
                    print ">>>   %22s  ->  %s"%(oldline.lstrip(' '),newline.lstrip(' '))
                
                if valuematches:
                    matchedvalue = valuematches[0]
                    if len(valuematches)>1:
                        error('Two matches for "%s" in file "%s":'%(shiftvar,fileOutName))
                        error('  "%s"!'%(line))
                        exit(1)
                    if foundValueLine:
                        error('Reoccuring "%s" in file "%s":'%(shiftvar,fileOutName))
                        error('  "%s"!'%(line))
                        exit(1)
                    if float(matchedvalue)!=0.00:
                        warning('"%s"\'s value "%s"!=0.00 in file "%s":'%(shiftvar,shiftvalue,fileOutName))
                        warning('   "%s"!'%(line))
                    foundValueLine = True
                    oldpattern = '(\[.*"%s".*,.*)"%s"(.*\])'%(shiftvar,matchedvalue)
                    newpattern = '%s"%s"%s'%(r"\1",sign+shiftvalue,r"\2")
                    oldline    = line.replace('\n','')
                    line       = re.sub(oldpattern,newpattern,line)
                    newline    = line.replace('\n','')
                    print ">>>   %22s  ->  %s"%(oldline.lstrip(' '),newline.lstrip(' '))
                    
                if noTight and tightmatches:
                    matchedvalue = tightmatches[0]
                    if len(tightmatches)>1:
                        error('Two matches for "%s" in file "%s":'%("noTight",fileOutName))
                        error('  "%s"!'%(line))
                        exit(1)
                    if foundNoTightLine:
                        error('Reoccuring "%s" in file "%s":'%("noTight",fileOutName))
                        error('  "%s"!'%(line))
                        exit(1)
                    foundNoTightLine = True
                    oldpattern = '(\[.*"%s".*,.*)"%s"(.*\])'%("noTight",matchedvalue)
                    newpattern = '%s"%s"%s'%(r"\1","true",r"\2")
                    oldline    = line.replace('\n','')
                    line       = re.sub(oldpattern,newpattern,line)
                    newline    = line.replace('\n','')
                    print ">>>   %22s  ->  %s"%(oldline.lstrip(' '),newline.lstrip(' '))
                    
                
                fileOut.write(line)
              
              if not foundPostFixLine:
                warning('Did not find match for "%s" in file "%s"!'%("postFix",fileInName),pre="  ")
              if not foundValueLine:
                warning('Did not find match for "%s" in file "%s"!'%(shiftvar,fileOutName),pre="  ")
              if noTight and not foundNoTightLine:
                warning('Did not find match for "%s" in file "%s"!'%("noTight",fileOutName),pre="  ")
              nFiles += 1
    print ">>>\n>>> created %d file%s"%(nFiles,'' if nFiles==1 else 's')



def green(string,**kwargs):   return "\x1b[0;32;40m%s\033[0m"%string
def error(string,**kwargs):   print ">>> %s\033[1m\033[91mERROR! %s\033[0m"%(kwargs.get('pre',""),string)
def warning(string,**kwargs): print ">>> %s\033[1m\033[93mWarning!\033[0m\033[93m %s\033[0m"%(kwargs.get('pre',""),string)

def frange(start, stop, step):
    """Yield values in a range between start and stop, with  linearly spaced steps"""
    x = start
    while x <= stop:
      yield x
      x += step

def ensureDirectory(DIR):
    """Make directory if it does not exist."""
    if not os.path.exists(DIR):
        os.makedirs(DIR)
        print ">>> made directory " + DIR
    


if __name__ == "__main__":
  main()
  print ">>> \n"


