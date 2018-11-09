# !/usr/bin/env python

import os, sys
import subprocess
import time
from argparse import ArgumentParser
import os, sys

argv = sys.argv
description = '''This script splits up the plots script into the different selection categories and sends them to the batch system.'''
parser = ArgumentParser(description=description,epilog="Succes!")
parser.add_argument( "-r", "--remove-log", dest="removeLogFiles", default=False, action='store_true',
                     help="remove existing log files" )
args = parser.parse_args()

DIR = "/shome/ineuteli/analysis/SFrameAnalysis/plots"
LOGDIR = "%s/submitPlots" % DIR



def getCategories():
    # get list of configs
    header = "list of available categories:"
    tab = "\n>>>\t"
    out = subprocess.check_output("python %s/plot.py -l" % DIR, shell=True, stderr=open(os.devnull, 'w'))
    #print ">>> output from plot.py -l:"
    #print out
    #print ">>> end output"
    if not header in out or not tab in out: sys.exit(1)
    return out.split(header)[1].split(tab)[1:-1]



def main():
    #print
    
    # MAKE LOG DIR
    if not os.path.exists(LOGDIR):
        os.makedirs(LOGDIR)
        print ">>> made directory %s" % LOGDIR
        
    # REMOVE LOG FILES
    if args.removeLogFiles:
        try:
            out = subprocess.check_output("rm %s/*" % LOGDIR, shell=True, stderr=subprocess.STDOUT)
            print "\n>>> removed old log files"
        except subprocess.CalledProcessError as e:
            if "No such file or directory" in e.output and os.path.exists(LOGDIR):
                print "\n>>> could not remove old log files: no log files in %s" % LOGDIR
            elif not os.path.exists(LOGDIR):
                print "\n>>> could not remove old log files: log directory does not exits: %s" % LOGDIR
            else: print "\n>>> could not remove old log files"

    # GET CATEGORIES from plot.py    
    categories = getCategories()
    
    # SUBMIT JOBS for each category
    if len(categories) > 0:
        for category, i in zip(categories, range(len(categories))):
            category = category.replace(" and ","-").replace(" ","").replace(",","-")
            print "\n>>> category %i: %s" % ( i, category )
            command = "qsub -q all.q -N category_%s %s/submitPlots.sh %s" % ( i, DIR, i )
            print ">>> " + command
            sys.stdout.write(">>> ")
            sys.stdout.flush()
            os.system(command)
        #print



if __name__ == '__main__':
    main()
    print "\n>>> done\n"


