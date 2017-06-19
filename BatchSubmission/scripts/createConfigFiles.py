#! /usr/bin/env python

from argparse import ArgumentParser
import os, sys


argv = sys.argv
description = '''This script make plots.'''
parser = ArgumentParser(prog="createConfigFiles",description=description,epilog="Succes!")
parser.add_argument( "-s", "--samples", dest="samples", nargs='+', default=[], action='store',
                     metavar="SAMPLES", help="create config files for SAMPLES" )
parser.add_argument( "-x", "--xml-dir", dest="XML_DIR", default="xmls_Moriond", action='store',
                     metavar="XML_DIR", help="find xml files in XML_DIR" )
# parser.add_argument( "-", "--etau", dest="etau", default=False, action='store_true',
#                      help="run only for the etau channel" )
args = parser.parse_args()





def main():
    """Main function."""
    
#     if not os.path.exists(outDir):
#         print "Creating output directory", outDir
#         os.makedirs(outDir)
#     os.path.isdir(samplepath)
    
    print args.samples
    
#     os.walk(samplepath)
    
    

    



if __name__ == '__main__':
    print
    main()
    print ">>>\n>>> done\n"




