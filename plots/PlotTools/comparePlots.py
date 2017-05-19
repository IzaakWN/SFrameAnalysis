import os, sys
import datetime
from argparse import ArgumentParser


# ARGUMENT & OPTIONS
argv = sys.argv
usage = '''This script make plots.'''
parser = ArgumentParser(description="Make textfile with hierarchy of subdir for a given dir",usage=usage,epilog="Succes!")
parser.add_argument( "filename", nargs='?', type=str, default=None, action='store',
                     metavar="NAME", help="name of output .tex file" )
args = parser.parse_args()



# LATEX CONTENT
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
header = \
"""%s
\documentclass[8pt,a4paper]{article}
\usepackage[margin=4mm]{geometry}
\usepackage{graphicx}
\usepackage{float}
\begin{document}
"""
figure = \
"""
\begin{figure}[H]
	\centering
	\includegraphics[width=90mm]{%s}
	\hspace{5mm}
	\includegraphics[width=90mm]{%s}
	\caption{%s}
\end{figure}
"""
footer = \
"""
\end{document}
"""

header = header.replace('\b','\\b') % ("% generated on "+date)
figure = figure.replace('\b','\\b')
footer = footer.replace('\b','\\b')


# VARIABLE DICTIONARY
vars_dict = {   "pt_1":  "p^1_T",  "pt_2":  "p^2_T",
                "eta_1": "\eta_1", "eta_2": "\eta_2",
                "jpt_1":   "jet 1 p_T", "jpt_2":   "jet 2 p_T",
                "bpt_1": "b jet 1 p_T", "bpt_2": "b jet 2 p_T",
                "abs(jeta_1)":   "jet 1 |\eta|", "abs(jeta_2)":   "jet 2 |\eta|",
                "abs(beta_1)": "b jet 1 |\eta|", "abs(beta_2)": "b jet 1 |\eta|",
                "jeta_1": "jet 1 \eta",   "jeta_2":   "jet 2 \eta",
                "beta_1": "b jet 1 \eta", "beta_2": "b jet 2 \eta",
                "dR_ll":  "\Delta R_{ll}",
                "m_vis": "m_{\text{vis}}", }





    ##############
    # writeLaTeX #
    ##############

def writeLaTeXFile(filename, plots):
    """Write LaTeX file."""
    
    file = open(filename, 'w')
    file.write(header)
    for fig1, fig2, caption in plots:
        file.write(figure % (fig1,fig2,caption))
    file.write(footer)
                  
    file.close()

    print "\n>>> written %i comparisons to %s" % (len(plots), filename)





    ##############
    # includeFig #
    ##############

def includeFig(fig):
    """Return boolean as to whether it should be included or not."""
    
    illegal = [ "iso-vetos-SS" ]#"abs", "jpt", "bpt", "phi" ]
    
    for flag in illegal:
        if flag in fig: return False
    return True






    ##############
    # includeFig #
    ##############

def makeLaTeX(var):
    """Make nice variables."""

    var = var.replace(".png","").replace(".jpg","").replace(".pdf","")
    if var in vars_dict: var = "$%s$" % vars_dict[var]
    else:           var = var.replace("_","\\textunderscore ")

    return var





    ##############
    # getFigures #
    ##############

def getFigures(caption):
    """Get list of all available figures."""
    
    path1 = "mutau_69p2mb/"
    path2 = "mutau_ICHEP/"
    
    figs1 = os.listdir(path1)
    figs2 = os.listdir(path2)
    plots = [ ]
    
    for fig in figs1:
        if includeFig(fig) and ".png" in fig and fig in figs2:
            fullcaption = "%s: %s" % (makeLaTeX(fig), caption)
            plots.append((path1+fig,path2+fig,fullcaption))
    
    return plots





    ########
    # main #
    ########

def main():
    """Main function."""

    filename = args.filename
    if not filename: filename = "compare.tex"
    if not ".tex" in filename: filename += ".tex"
    caption = "62 mb vs. 69.2 mb"

    plots = getFigures(caption)
    writeLaTeXFile(filename,plots)





if __name__ == '__main__':
    print
    main()
    print ">>> Done.\n"




