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
    
    if weights: weights = "*".join(weights)
    else:       weights = ""
    
    #print weights
    return weights
    


def combineCuts(*cuts,**kwargs):
    """Combine cuts and apply weight if needed."""
    
    verbosity   = getVerbosity(kwargs,verbositySelectionTools)
    cuts        = [ unwrapSelection(cut) for cut in cuts if cut and (isinstance(cut,str) or isinstance(cut,Selection)) ]
    weight      = kwargs.get('weight', False)
    
    # TODO: take "or" into account with parentheses
    for cut in cuts:
        if "||" in cuts: LOG.warning("combineCuts - Be careful with those \"or\" statements!")
        # [cut.strip() for i in cut.split('||')]
    
    if weight:
      string = re.sub("\(.*\)","",weight)
      if re.search(r"[=<>\+\-\&\|]",string):
        weight = "(%s)"%weight
    
    if cuts:
      cuts = " && ".join(cuts)
      if weight:
        string = re.sub("\(.*\)","",cuts)
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
    


def invertCharge(cuts,**kwargs):
    """Find, invert and replace charge selections."""
    
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
    
    LOG.verbose("   \"%s\"\n>>>   -> \"%s\" (%s)\n>>>" % (cuts0,cuts,"OS" if OS else "SS"),verbosity,level=2)
    return cuts
    


def invertIsolation(cuts,**kwargs):
    """Find, invert and replace isolation selections."""
    
    verbosity   = max(kwargs.get('verbosity',0),verbositySelectionTools)
    channel     = kwargs.get('channel','emu')
    iso_relaxed = kwargs.get('to','iso_1<0.5 && iso_2<0.5 && iso_1>0.20') # outdated (iso_1>0.20||iso_2>0.15) pzeta_disc>-35 && nbtag<1
    cuts0       = cuts 
    
    # MATCH PATTERNS https://regex101.com
    match_iso_1 = re.findall(r"iso_1\ *[<>]\ *\d+\.\d+\ *[^\|]&*\ *",cuts)
    match_iso_2 = re.findall(r"iso_2\ *\!?=?[<=>]\ *\d+\.\d+\ *[^\|]&*\ *",cuts)
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
        if len(match_iso_1) or len(match_iso_2): LOG.warning("invertIsolation: %d iso_1 and %d iso_2 matches! cuts=%s"%(len(match_iso_1),len(match_iso_2),cuts))
    cuts    = cuts.rstrip(' ').rstrip('&').rstrip(' ')
    
    LOG.verbose("  \"%s\"\n>>>   -> \"%s\"\n>>>" % (cuts0,cuts),verbosity,level=2)
    return cuts
    


def relaxJetSelection(cuts,**kwargs):
    """Find, relax and replace jet selections:
         1) remove b tag requirements
         2) relax central jet requirements."""
    
    verbosity       = max(kwargs.get('verbosity',0),verbositySelectionTools)
    channel         = kwargs.get('channel','mutau')
    btags_relaxed   = kwargs.get('btags',"")
    cjets_relaxed   = kwargs.get('ncjets',"ncjets>1" if "ncjets==2" in cuts.replace(' ','') else "ncjets>0")
    cuts0           = cuts
    
    # MATCH PATTERNS
    btags  = re.findall(r"&*\ *nc?btag(?:20)?\ *[<=>]=?\ *\d+\ *",cuts)
    cjets  = re.findall(r"&*\ *ncjets(?:20)?\ *[<=>]=?\ *\d+\ *",cuts)
    cjets += re.findall(r"&*\ *nc?btag(?:20)?\ *[<=>]=?\ *ncjets(?:20)?\ *",cuts)
    LOG.verbose(">>> relaxJetSelection:\n>>>   btags = %s\n>>>   cjets = \"%s\"" % (btags,cjets),verbosity,level=2)
    
    # REPLACE
    if len(btags) and len(cjets):
        if len(btags)>1: LOG.warning("relaxJetSelection: More than one btags match! cuts=%s"%cuts)
        if len(cjets)>1: LOG.warning("relaxJetSelection: More than one cjets match! cuts=%s"%cuts)
        cuts = cuts.replace(btags[0],'')
        cuts = cuts.replace(cjets[0],'')
        if btags_relaxed: cuts = "%s && %s && %s" % (cuts,btags_relaxed,cjets_relaxed)
        else:             cuts = "%s && %s"       % (cuts,              cjets_relaxed)
    elif cuts:
        if len(btags) or len(cjets): LOG.warning("relaxJetSelection: %d btags and %d cjets matches! cuts=%s"%(len(btags),len(cjets),cuts))
    cuts = cuts.lstrip(' ').lstrip('&').lstrip(' ')
    
    LOG.verbose(">>>   \"%s\"\n>>>   -> \"%s\"\n>>>" % (cuts0,cuts),verbosity,level=2)
    return cuts


def isSelectionString(string,**kwargs):
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
          self.title     = kwargs.get('title',    makeLatex(   self.name)) # for plot axes
          self.selection = unwrapSelection(args[0])
        elif len(args)==2:
          self.title     = args[0]
          self.selection = unwrapSelection(args[0])
        if self.selection=="":
           LOG.warning('Selection::Selection - No selection string given for "%s"!'%(self.name))
        self.context     = getContextFromDict(kwargs,self.selection) # context-dependent channel selections
    
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
          selection2 = Selection(selection2,selection2) # make selection object
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
    
    def combine(self, *selection2s):
        # TODO: check if selection2 is a string, if possible
        name     = ", ".join([self.name]    +[s.name for s in selection2s])
        title    = ", ".join([self.title]   +[s.title for s in selection2s])
        filename = ", ".join([self.filename]+[s.filename for s in selection2s])
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
    if   len(args)==5 or len(args)==6:
      return args
    elif len(args)==2 and isinstance(args[0],Variable) and isinstance(args[1],Selection):
      return args[0].unwrap()+(unwrapSelection(args[1]),)
    LOG.warning('unwrapVariableSelection - Could not unwrap arguments "%s", len(args)=%d. Returning None.'%(args,len(args)))
    return None
        

