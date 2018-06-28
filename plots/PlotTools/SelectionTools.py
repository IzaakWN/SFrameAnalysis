#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

from ROOT import TCut
import os, re
from copy import copy, deepcopy
from SettingTools  import *
from VariableTools import *
from PrintTools    import *



def combineWeights(*weights,**kwargs):
    """Combine cuts and apply weight if needed."""
    
    verbosity   = getVerbosity(kwargs,verbositySelectionTools)
    weights     = [ w for w in weights if w and isinstance(w,str) ]
    
    if weights:
      weights = "*".join(weights)
      weights = weights.replace('*/','/')
    else:
      weights = ""
    
    #print weights
    return weights
    


def combineCuts(*cuts,**kwargs):
    """Combine cuts and apply weight if needed."""
    
    verbosity   = getVerbosity(kwargs,verbositySelectionTools)
    cuts        = [ unwrapSelection(cut) for cut in cuts if cut and (isinstance(cut,str) or isinstance(cut,Selection)) ]
    weight      = kwargs.get('weight', False)
    
    # TODO: take "or" into account with parentheses
    for cut in cuts:
        if "||" in cuts: LOG.warning('combineCuts - Be careful with those "or" statements!')
        # [cut.strip() for i in cut.split('||')]
    
    if weight:
      string = re.sub("\(.+\)","",weight)
      if re.search(r"[=<>\+\-\&\|]",string):
        weight = "(%s)"%weight
    
    if cuts:
      cuts = " && ".join(cuts)
      if weight:
        string = re.sub("\(.+\)","",cuts)
        if re.search(r"[=<>\+\-\&\|]",string):
          cuts = "(%s)*%s"%(cuts,weight)
        else:
          cuts = "%s*%s"%(cuts,weight)
    elif weight:
      cuts = weight
    else:
      cuts = ""

    #print cuts
    return cuts
    


def stripWeights(cuts):
    """Help function to remove weights and extract main selection string.
    e.g. '(pt>1 && abs(eta)<1)*weight' -> 'pt>1 && abs(eta)<1.5'"""
    matches = re.findall(r"\(([^)]+\(.+\|\|[^(\?:,]+\)[^(\?:,]+)\)",cuts)
    if not matches:
      matches = re.findall(r"^[^()\?:,]+\(.+\|\|[^(\?:,]+\)[^()\?:,]+$",cuts)
    if not matches:
      matches = re.findall(r"(?<!\w)\(([^)\?:,]+)\)",cuts)
    #print matches
    if len(matches)==0:
      return cuts
    elif len(matches)>1:
      LOG.warning('stripWeights: %d selection string matches in "%s"! Going with the first: "%s"'%(len(matches),cuts,matches[0]))
    return matches[0]
    


def makeBlindCuts(var,a,b,N,xmin,xmax,**kwargs):
    """Helpfunction to make a selection string to blind a given variable within some window (a,b),
    making sure the cuts match the bin edges of some (N,xmin,xmax) binning."""
    blindcut = ""
    xbins    = kwargs.get('xbins', [ ] ) # TODO: variable xbins ?
    binwidth = float(xmax-xmin)/N
    if xmax<=xmin:
      LOG.ERROR('makeBlindCuts: "%s" has xmax = %s <= %s = xmin !'%(var,xmax,xmin))
    if b<=a:
      LOG.ERROR('makeBlindCuts: "%s" has window a = %s <= %s = b !'%(var,a,b))
    if xmin<a<xmax:
      bin, rem = divmod(a-xmin,binwidth)
      xlow     = bin*binwidth
      blindcut = "%s<%s"%(var,xlow)
    if xmin<b<xmax:
      bin, rem = divmod(b-xmin,binwidth)
      if rem>0:    bin      += 1
      xhigh    = bin*binwidth
      if blindcut:
        blindcut = "(%s || %s<%s)"%(blindcut,xhigh,var)
      else:
        blindcut = "%s<%s"%(xhigh,var)
    LOG.verbose('makeBlindCuts: blindcut = "%s" for a (%s,%s) window and (%s,%s,%s) binning'%(blindcut,a,b,N,xmin,xmax),verbosity,level=2) 
    return blindcut
    


def invertCharge(cuts,**kwargs):
    """Helpfunction to find, invert and replace charge selections."""
    
    verbosity   = max(kwargs.get('verbosity',0),verbositySelectionTools)
    cuts0       = cuts
    OS          = kwargs.get('OS',False)
    
    # MATCH PATTERNS https://regex101.com
    matchOS = re.findall(r"q_[12]\ *\*\ *q_[12]\ *<\ *0",cuts)
    matchSS = re.findall(r"q_[12]\ *\*\ *q_[12]\ *>\ *0",cuts)
    LOG.verbose("invertCharge:\n>>>   matchOS = %s\n>>>   matchSS = %s" % (matchOS,matchSS),verbosity,level=2)
    
    # CUTS: invert charge
    if (len(matchOS)+len(matchSS))>1:
        LOG.warning("invertCharge: more than one charge match (%d OS, %d SS) in \"%s\""%(len(matchOS),len(matchSS),cuts))
    if OS:
        for match in matchSS: cuts = cuts.replace(match,"q_1*q_2<0") # invert to OS
    else:
        for match in matchOS: cuts = cuts.replace(match,"q_1*q_2>0") # invert to SS
    if not cuts:
        if OS: cuts = "q_1*q_2<0"
        else:  cuts = "q_1*q_2>0"
    # if "q_1*q_2>0" in cuts.replace(' ',''): scale = 1.0
    # if "q_1*q_2<0" in cuts.replace(' ',''):
    #     cuts = cuts.replace("q_1 * q_2 < 0","q_1*q_2>0").replace("q_1*q_2 < 0","q_1*q_2>0").replace("q_1*q_2<0","q_1*q_2>0")        
    # elif cuts: cuts = "q_1*q_2>0 && %s" % cuts
    # else:      cuts = "q_1*q_2>0"
    
    LOG.verbose('  "%s"\n>>>   -> "%s" %s\n>>>'%(cuts0,cuts,"OS" if OS else "SS"),verbosity,level=2)
    return cuts
    


def invertIsolation(cuts,**kwargs):
    """Helpfunction to find, invert and replace isolation selections."""
    
    verbosity   = max(kwargs.get('verbosity',0),verbositySelectionTools)
    channel     = kwargs.get('channel','emu')
    iso_relaxed = kwargs.get('to','iso_1<0.5 && iso_2<0.5 && iso_1>0.20') # outdated (iso_1>0.20||iso_2>0.15) pzeta_disc>-35 && nbtag<1
    cuts0       = cuts 
    
    # MATCH PATTERNS https://regex101.com
    match_iso_1 = re.findall(r"iso_1\ *[<>]=?\ *\d+\.\d+\ *[^\|]&*\ *",cuts)
    match_iso_2 = re.findall(r"iso_2\ *!?[<=>]=?\ *\d+\.?\d*\ *[^\|]&*\ *",cuts)
    LOG.verbose("invertIsolation:\n>>>   match_iso_1 = %s\n>>>   match_iso_2 = \"%s\"" % (match_iso_1,match_iso_2),verbosity,level=2)
    
    # REPLACE
    if "iso_cuts==1" in cuts.replace(' ',''):
        cuts = re.sub(r"iso_cuts\ *==\ *1",iso_relaxed,cuts)
    elif len(match_iso_1) and len(match_iso_2):
        if len(match_iso_1)>1: LOG.warning("invertIsolation: More than one iso_1 match! cuts=%s"%cuts)
        if len(match_iso_2)>1: LOG.warning("invertIsolation: More than one iso_2 match! cuts=%s"%cuts)
        cuts = cuts.replace(match_iso_1[0],'')
        cuts = cuts.replace(match_iso_2[0],'')
        cuts = "%s && %s" % (iso_relaxed,cuts)
    elif cuts:
        if len(match_iso_1) or len(match_iso_2): LOG.warning('invertIsolation: %d iso_1 and %d iso_2 matches! cuts="%s"'%(len(match_iso_1),len(match_iso_2),cuts))
    cuts    = cuts.rstrip(' ').rstrip('&').rstrip(' ')
    
    LOG.verbose('  "%s"\n>>>   -> "%s"\n>>>'%(cuts0,cuts),verbosity,level=2)
    return cuts
    


def relaxJetSelection(cuts,**kwargs):
    """Helpfunction to find, relax and replace jet selections:
         1) remove b tag requirements
         2) relax central jet requirements."""
    
    ncjets_relaxed  = "ncjets>1" if "ncjets==2" in cuts.replace(' ','') else "ncjets>0"
    verbosity       = max(kwargs.get('verbosity',0),verbositySelectionTools)
    channel         = kwargs.get('channel', 'mutau'        )
    btags_relaxed   = kwargs.get('btags',   ""             )
    cjets_relaxed   = kwargs.get('ncjets',  ncjets_relaxed )
    cuts0           = cuts
    
    # MATCH PATTERNS
    btags  = re.findall(r"&*\ *nc?btag(?:20)?\ *[<=>]=?\ *\d+\ *",cuts)
    cjets  = re.findall(r"&*\ *ncjets(?:20)?\ *[<=>]=?\ *\d+\ *",cuts)
    cjets += re.findall(r"&*\ *nc?btag(?:20)?\ *[<=>]=?\ *ncjets(?:20)?\ *",cuts)
    LOG.verbose('relaxJetSelection:\n>>>   btags = %s\n>>>   cjets = "%s"' % (btags,cjets),verbosity,level=2)
    if len(btags)>1: LOG.warning('relaxJetSelection: More than one btags match! Only using first instance in cuts "%s"'%cuts)
    if len(cjets)>1: LOG.warning('relaxJetSelection: More than one cjets match! Only using first instance in cuts "%s"'%cuts)
    
    # REPLACE
    #if len(btags):
    #    cuts = cuts.replace(btags[0],'')
    #    if btags_relaxed: cuts = "%s && %s"%(cuts,btags_relaxed)
    #if len(cjets):
    #    cuts = cuts.replace(cjets[0],'')
    #    cuts = "%s && %s"%(cuts,cjets_relaxed)
    if len(btags) and len(cjets):
        cuts = cuts.replace(btags[0],'')
        cuts = cuts.replace(cjets[0],'')
        if btags_relaxed: cuts = "%s && %s && %s" % (cuts,btags_relaxed,cjets_relaxed)
        else:             cuts = "%s && %s"       % (cuts,              cjets_relaxed)
    #elif len(btags) or len(cjets):
    #    LOG.warning("relaxJetSelection: %d btags and %d cjets matches! cuts=%s"%(len(btags),len(cjets),cuts))
    cuts = cuts.lstrip(' ').lstrip('&').lstrip(' ')
    
    LOG.verbose('  "%s"\n>>>   -> "%s"\n>>>'%(cuts0,cuts),verbosity,level=2)
    return cuts
    


def vetoJetTauFakes(cuts,**kwargs):
    """Helpfunction to ensure the jet to tau fakes (gen_match_2==6) are excluded in selection string.
       Assume string contains gen_match_2 compared to any digits from 1 to 6.
     """
    
    verbosity   = max(kwargs.get('verbosity',0),verbositySelectionTools)
    removeTID   = kwargs.get('noTID', False )
    cuts0       = cuts
    
    if removeTID:
      cuts  = re.sub(r"(\*\ *\(\ *gen_match_2\ *==[^)]*\?[^)]*\))","",cuts) #.replace('**','*')
    match   = re.findall(r"(gen_match_2\ *(!?[<=>]=?\ *\d))(?!\ *\?)",cuts)
    if len(match)==0:
      subcuts0 = stripWeights(cuts)
      subcuts1 = combineCuts(subcuts0,"gen_match_2<6")
      cuts     = cuts.replace(subcuts0,subcuts1)
      return cuts
    elif len(match)>1:
      LOG.warning('vetoFakeRate: more than one "gen_match_2" match (%d) in "%s"'%(len(match),cuts))
    match, genmatch = match[0]
    genmatch = genmatch.replace(' ','')
    
    if '!=' in genmatch:
      if '5' in genmatch: # "gen_match_2!=5"
        cuts = cuts.replace(match,"gen_match_2<5")
      elif not '6' in genmatch: # "gen_match_2!=*"
        cuts = combineCuts(cuts,"gen_match_2!=6")
    elif "=6" in genmatch: # "gen_match_2*=6"
        LOG.warning('vetoFakeRate: selection "%s" with "%s" set to "0"!'%(cuts,genmatch)) 
        cuts = "0"
    elif '>' in genmatch: # "gen_match_2>*"
        cuts = combineCuts(cuts,"gen_match_2!=6")
    
    #LOG.verbose('  "%s"\n>>>   -> "%s"\n>>>'%(cuts0,cuts),verbosity,level=2)
    return cuts



def isSelectionString(string,**kwargs):
    """Check if string has boolean or comparison operators."""
    if not isinstance(string,str): return False
    elif '<'  in string: return True
    elif '>'  in string: return True
    elif '==' in string: return True
    elif '&&' in string: return True
    elif '||' in string: return True
    return False


class Selection(object):
    """
    Selection class to:
       - hold all relevant information of a selection that will be used to make plots:
           selection pattern, filename friendly name, LaTeX friendly title, ...
       - easy string conversions: filename, LaTeX, ...
       - analysis-specific operations: relaxing cuts, inverting cuts, applying variations, ...
    """
    
    def __init__(self, name, *args, **kwargs):
        self.name        = name
        self.filename    = kwargs.get('filename', makeFileName(self.name)) # for file
        self.selection   = ""
        if len(args)==1:
          self.title     = kwargs.get('title',    makeTitle(   self.name)) # for plot axes
          self.selection = unwrapSelection(args[0])
        elif len(args)==2:
          self.title     = args[0]
          self.selection = unwrapSelection(args[0])
        if self.selection=="":
           LOG.warning('Selection::Selection - No selection string given for "%s"!'%(self.name))
        self.context     = getContextFromDict(kwargs,self.selection) # context-dependent channel selections
        self.only            = kwargs.get('only',           [ ]                         )
        self.veto            = kwargs.get('veto',           [ ]                         )
        if self.only:
          if not isList(self.only): self.only = [ self.only ]
        if self.veto:
          if not isList(self.veto): self.veto = [ self.veto ]
    
    @property
    def cut(self): return self.selection
    @cut.setter
    def cut(self,val): self.selection = val
    
    def __str__(self):
      """Returns string representation of Selection object."""
      return self.name
    
    def __repr__(self):
      """Returns string representation of Selection object."""
      return '<%s("%s","%s") at %s>'%(self.__class__.__name__,self.name,self.selection,hex(id(self)))
    
    def __iter__(self):
      """Start iteration over selection information."""
      for i in [self.name,self.selection]:
        yield i
    
    def __add__(self, selection2):
        """Add selections by combining their selection string (can be string or Selection object)."""
        if isinstance(selection2,str):
          selection2 = Selection("",selection2) # make selection object
        return combine(selection2)
    
    def __mul__(self, weight):
        """Multiply selection with some weight (that can be string or Selection object)."""
        result = None
        if isinstance(selection2,str):
          result = Selection("%s (%s)"(self.name,weight),combineCuts(self.selection,weight=weight))
        else:
          result = Selection("%s (%s)"(self.name,weight.title),combineCuts(self.selection,weight=weight))
        return result
    
    def changeContext(self,*args):
        """Change the contextual selections for a set of arguments, if it is available"""
        if self.context:
          self.selections = self.context.getContext(*args)
    
    def plotForVariable(self,variable,**kwargs):
        """Check is variable is vetoed for this variable."""
        verbosity = getVerbosity(kwargs,verbosityVariableTools)
        if not isinstance(variable,str):
          variable = variable.name
        for searchterm in self.veto:
          if re.search(searchterm,variable):
            LOG.verbose('Variable::plotForSelection: Regex match of variable "%s" to "%s"'%(variable,searchterm),verbosity,level=2)
            return False
        for searchterm in self.only:
          if re.search(searchterm,variable):
            LOG.verbose('Variable::plotForSelection: Regex match of variable "%s" to "%s"'%(variable,searchterm),verbosity,level=2)
            return True
        return len(self.only)==0
    
    def combine(self, *selection2s):
        # TODO: check if selection2 is a string, if possible
        name     = ", ".join([self.name]    +[s.name     for s in selection2s if s.name    ])
        title    = ", ".join([self.title]   +[s.title    for s in selection2s if s.title   ])
        filename = ", ".join([self.filename]+[s.filename for s in selection2s if s.filename])
        cuts     = combineCuts(*([self.cut]+[s.cut for s in selection2s ]))
        sum      = Selection(name,cuts,title=title,filename=filename)
        return sum
    
    def invertIsolation(self,**kwargs):
        """Find, invert and replace isolation selections."""
        name      = "%s_relaxed_iso"%(self.name)
        title     = "%s (relaxed iso)"%(self.title)
        filename  = "%s_relaxed_iso"%(self.filename)
        selection = invertIsolation(self.selection,**kwargs)
        return Selection(name,selection,title=title,filename=self.filename)
    
    def relaxJetSelections(self,**kwargs):
        """Find, relax and replace jet selections."""
        name      = "%s_relaxed_jets"%(self.name)
        title     = "%s (relaxed jet selections)"%(self.title)
        filename  = "%s_relaxed_jets"%(self.filename)
        selection = relaxJetSelection(self.selection,**kwargs)
        return Selection(name,selection,title=title,filename=self.filename)
    
    def latex(self):
        return makeLatex(self.name)
    
    def shift(self,shifts,**kwargs):
        if len(shifts)>0 and shifts[0]!='_':
          shifts = '_'+shifts
        newstring              = shift(self.selection,shifts,**kwargs)
        newselection           = deepcopy(self)
        newselection.selection = newstring
        if self.selection != newstring:
          newselection.filename += shifts
        return newselection
    
    def shiftSelection(self,shifts,**kwargs):
        return shift(self.name,shifts,**kwargs)
    
    def isPartOf(self, *searchterms, **kwargs):
        """Check if all labels are in the sample's name, title or tags."""
        searchterms = [l for l in searchterms if l!='']
        if not searchterms: return False
        found       = True
        regex       = kwargs.get('regex',       False   )
        exlcusive   = kwargs.get('exclusive',   True    )
        labels      = [self.name,self.title]
        for searchterm in searchterms:
          if not regex:
              searchterm = re.sub(r"(?<!\\)\+",r"\+",searchterm) # replace + with \+
              searchterm = re.sub(r"([^\.])\*",r"\1.*",searchterm) # replace * with .*
          if exlcusive:
              for samplelabel in labels:
                  matches = re.findall(searchterm,samplelabel)
                  if matches: break
              else: return False # none of the labels contain the searchterm
          else: # inclusive
              for samplelabel in labels:
                  matches = re.findall(searchterm,samplelabel)
                  if matches: return True # one of the searchterm has been found
        return exlcusive
    
def sel(*args,**kwargs):
    """Shorthand for Selection class."""
    return Selection(*args,**kwargs)

def unwrapSelection(selection,**kwargs):
    """Make sure returned object is a string."""
    if isinstance(selection,Selection):
      return selection.selection
    return selection

def unwrapVariableSelection(*args,**kwargs):
    """Help function to unwrap arguments that contain variable and selection."""
    if len(args)==1 and isList(args[0]):
      args = args[0]
    if   len(args)==5:
      xvar, nxbins, xmin, xmax, cuts = args
      xbins = [ ]
    elif len(args)==2 and isinstance(args[0],Variable):
      xvar, nxbins, xmin, xmax = args[0].unwrap()
      xbins = args[0].xbins
      cuts = unwrapSelection(args[1]) if isinstance(args[1],Selection) else args[1]
    elif len(args)==3 and isList(args[1]):
      xvar, xbins, cuts = args
      nxbins, xmin, xmax = len(xbins)-1, xbins[0], xbins[-1]
    else:
      LOG.error('unwrapVariableSelection - Could not unwrap arguments "%s", len(args)=%d. Returning None.'%(args,len(args)))
    return xvar, nxbins, xmin, xmax, xbins, cuts
    
def unwrapVariableSelection2D(*args,**kwargs):
    """Help function to unwrap 2D arguments that contain variable and selection."""
    if len(args)==1 and isList(args[0]):
      args = args[0]
    if len(args)==9:
      xvar, nxbins, xmin, xmax, yvar, nybins, ymin, ymax, cuts = args
      xbins, ybins = [ ], [ ]
    elif len(args)==5 and isList(args[1]) and isList(args[3]):
      xvar, xbins, yvar, ybins, cuts = args
      nxbins, xmin, xmax = len(xbins)-1, xbins[0], xbins[-1]
      nybins, ymin, ymax = len(ybins)-1, ybins[0], ybins[-1]
    elif len(args)==7 and isList(args[1]):
      xvar, xbins, yvar, nybins, ymin, ymax, cuts = args
      nxbins, xmin, xmax = len(xbins)-1, xbins[0], xbins[-1]
    elif len(args)==7 and isList(args[5]):
      xvar, nxbins, xmin, xmax, yvar, ybins, cuts = args
      nybins, ymin, ymax = len(ybins)-1, ybins[0], ybins[-1]
    else:
      LOG.error('unwrapVariableSelection - Could not unwrap arguments "%s", len(args)=%d. Returning None.'%(args,len(args)))
    return xvar, nxbins, xmin, xmax, xbins, yvar, nybins, ymin, ymax, ybins, cuts






