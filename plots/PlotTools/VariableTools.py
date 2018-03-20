#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

import os, re
from array import array
from math import sqrt, pow, log
from SettingTools import *
from PrintTools   import *
#from SelectionTools import Selection

               
varlist = {
    'fjpt_1':          "leading forward jet pt (|eta|>2.4)",
    'fjpt_2':          "subleading forward jet pt (|eta|>2.4)",
    'fjeta_1':         "leading forward jet eta (|eta|>2.4)",
    'fjeta_2':         "subleading forward jet eta (|eta|>2.4)",
    'pt_3':            "tau pt",
    'eta_3':           "tau eta",
    'jpt_1':           "leading jet pt",                 'jpt_2':       "subleading jet pt",
    'bpt_1':           "leading b jet pt",               'bpt_2':       "subleading b jet pt",
    'abs(jeta_1)':     "leading jet abs(eta)",           'abs(jeta_2)': "subleading jet abs(eta)",
    'abs(beta_1)':     "leading b jet abs(eta)",         'abs(beta_2)': "subleading b jet abs(eta)",
    'jeta_1':          "leading jet eta",                'jeta_2':      "subleading jet eta",
    'beta_1':          "leading b jet eta",              'beta_2':      "subleading b jet eta",
    'njets':           "multiplicity of jets",
    'ncjets':          "multiplicity of central jets",   'nfjets':     "multiplicity of forward jets",
    'nbtag':           "multiplicity of b tagged jets",  'ncbtag':     "multiplicity of b tagged jets",
    'beta_1':          "leading b jet eta",              'beta_2':     "subleading b jet eta",
    'pt_tt':           "pt_ltau",                        'R_pt_m_vis': "R = pt_ltau / m_vis",
    'pt_tt_sv':        "SVFit pt_ltau,sv",               'R_pt_m_sv':  "SVFit R_{sv} = pt_ltau / m_sv",
    'm_sv':            "SVFit mass m_sv",                'dzeta':      "D_{zeta}",
    'dR_ll':           "#DeltaR_{ltau}",                 'pzeta_disc': "D_{zeta}",
    'pfmt_1':          "m_t(l,MET)",                     'pzetavis':   "p_{zeta}^{vis}",
    'dphi_ll_bj':      "#Deltaphi_ll',bj",               'pzetamiss':  "p_{zeta}^{miss}",
    'puweight':        "pileup weight",                  'met':        "MET",
    'chargedPionPt_2': "charged pion pt",                'metphi':     "MET phi",
    'neutralPionPt_2': "neutral pion pt",                
}



def makeLatex(title):
    """Convert patterns in a string to LaTeX format."""
    
    GeV = False
    cm  = False
    
    #if "jpt" in title:
    #    if   "jpt_1" in title and title.count(">3.0") is 2:
    #        title = "leading forward jet p_{T} (|#eta|>3.0)"
    #    elif "jpt_1" in title and title.count(">2.4") is 2:
    #        title = "leading forward jet p_{T} (|#eta|>2.4)"
    #    elif "jpt_1" in title and title.count("<3.0") is 2:
    #        title = "leading central jet p_{T} (|#eta|<3.0)"
    #    elif "jpt_1" in title and title.count("<2.4") is 2:
    #        title = "leading central jet p_{T} (|#eta|<2.4)"
    #    elif "jpt_1" in title and title.count("<2.4") is 1:
    #        title = "central jpt_1 (|#eta|<2.4)"
    #    elif "jpt_1" in title and title.count(">2.4") is 1:
    #        title = "forward jpt_1 (|#eta|>2.4)"
    #    elif "jpt_1" in title and title.count(">3.0") is 1:
    #        title = "forward jpt_1 (|#eta|>3.0)"
    #    elif "jpt_2" in title and title.count(">3.0") is 1:
    #        title = "forward jpt_2 (|#eta|>3.0)"
    #    elif "jpt_2" in title and title.count(">2.4") is 1:
    #        title = "forward jpt_2 (|#eta|>2.4)"
    #    elif ">" in title or "<" in title or "=" in title:
    #        LOG.warning("makeLatex: Boolean expression detected! How to replace \"%s\"?"%(title))
    #if "_jer" in title:
    #    title = title.replace("_jer","")
    
    for var in varlist:
        if var in title:
            title = title.replace(var,varlist[var])
            break
    
    strings = [ ]
    for string in title.split(' / '):
        
        if "p_" in string.lower():
            string = re.sub(r"(?<!i)(p)_([^{}()<>=\ ]+)",r"\1_{\2}",string,flags=re.IGNORECASE).replace('{t}','{T}')
            GeV = True
        
        if "pt" in string.lower() and "ptweighted" not in string.lower() and "byPhotonPt" not in string.lower():
            string = re.sub(r"(?<!k)(p)t_([^{}()<>=\ ]+)",r"\1_{T}^{\2}",string,flags=re.IGNORECASE)
            string = re.sub(r"\b(p)t\b",r"\1_{T}",string,flags=re.IGNORECASE)
            GeV = True
        
        if "m_" in string.lower():
            string = re.sub(r"(?<!u)(m)_([^{}\(\)<>=\ ]+)",r"\1_{\2}",string,flags=re.IGNORECASE).replace('{t}','{T}')
            GeV = True
        
        if "mt_" in string.lower():
            string = re.sub(r"(m)t_([^{}()<>=\ ]+)",r"\1_{T}^{\2}",string,flags=re.IGNORECASE)
            GeV = True
        
        if " d_" in string.lower():
            string = re.sub(r"(\ d)_([^{}()<>=\ ]+)",r"\1_{\2}",string,flags=re.IGNORECASE)
            cm = True
        
        if "tau" in string.lower():
            string = string.replace("tau","#tau").replace("Tau","#tau")
            string = re.sub(r"tau_([^{}<>=\ ]+)",r"tau_{\1}",string,flags=re.IGNORECASE)
        
        if "phi" in string.lower() and "dphi" not in string.lower():
            string = string.replace("phi","#phi")
            string = re.sub(r"phi_([^{}<>=\ ]+)",r"phi_{\1}",string,flags=re.IGNORECASE)
        
        if "zeta" in string.lower() and "#zeta" not in string.lower():
            if "Dzeta" in string:
                string = string.replace("Dzeta","D_{zeta}")
                GeV = True
            if "zeta_" in string.lower():
                string = string.replace("zeta_","#zeta_{").replace("Zeta_","#Zeta_{") + "}"
            else:
                string = string.replace("zeta","#zeta").replace("Zeta","#Zeta")
            GeV = True
        
        if "eta" in string.lower() and "#eta" not in string.lower() and "#zeta" not in string.lower() and "deta" not in string.lower():
            string = string.replace("eta","#eta")
            string = re.sub(r"eta_([^{}<>=\ ]+)",r"eta_{\1}",string,flags=re.IGNORECASE)
        
        if "abs(" in string and ")" in string:
            string = string.replace("abs(","|").replace(")","") + "|" # TODO: split at next space
        
        if  "mu" in string.lower():
            string = re.sub(r"mu(?![lo])",r"#mu",string,flags=re.IGNORECASE)
            #string = string.replace("mu","#mu").replace("Mu","#mu")
            #string = string.replace("si#mulation","simulation")
        
        if "ttbar" in string.lower():
            string = string.replace("ttbar","t#bar{t}").replace("TTbar","t#bar{t}")
        
        if "npv" in string.lower():
            string = string.replace("npv","number of vertices")
        
        if '->' in string:
            string = string.replace('->','#rightarrow')
        
        if "=" in string:
            string = string.replace(">=","#geq").replace("<=","#leq")
        
        strings.append(string.replace('##','#'))
    
    newtitle = ' / '.join(strings)
    
    if GeV or "mass" in newtitle or ("MET" in newtitle.lower() and "phi" not in newtitle ):
      if "GeV" not in newtitle:
        newtitle += " [GeV]"
    if cm:
      newtitle += " [cm]"
      if GeV:
        LOG.warning("makeLatex: Flagged units are both GeV and cm!")
    
    return newtitle
    


def makeTitle(title,**kwargs):
    """Make header with LaTeX."""
    title = makeLatex(title,**kwargs)
    if " [GeV]" in title:
      title = title.replace('[GeV]',"")
    return title
    


def makeHistName(*labels,**kwargs):
    """Use label and var to make an unique and valid histogram name."""
    hist_name = '_'.join(labels)
    hist_name = hist_name.replace("+","-").replace(" - ","-").replace(".","p").replace(" ","_").replace(
                                  "(","-").replace(")","-").replace("[","-").replace("]","-").replace(
                                  "<","lt").replace(">","gt").replace("=","e").replace("*","x")
    return hist_name
    


def makeFileName(name,**kwargs):
    """Make filename without inconvenient character."""
    name = name.replace(" and ",'-').replace(',','-').replace('(','').replace(')','').replace(':','-').replace(
                             '|','').replace('&','').replace('-m_T','-mt').replace(
                         '>=',"geq").replace('<=',"leq").replace('>',"gt").replace('<',"lt").replace("=","eq").replace(
                          ' ','')
    #if not (".png" in name or ".pdf" in name or ".jpg" in name): name += kwargs.get('ext',".png")
    return name
    


def shift(arg, shift,**kwargs):
    """Shorthand for shiftJetSelections and shiftJetVariables. Warning! Only use this for
       single variables, if they do not contain comparison or boolean tokens!"""
    for token in ['>','<','=','&&','||']:
      if token in arg:
        if '*' in arg and "q_1*q_2" not in arg:
            LOG.warning("shift: \'*\' token found in argument \"%s\","%(arg)+\
                  "is this a variable or selection? Assuming selections.")
        return shiftJetSelections(arg, shift, **kwargs)
    return shiftJetVariable( arg, shift, **kwargs)
    
def shiftJetSelections(cuts,shift,**kwargs):
    """Convert variables in cuts to variables
       that have been propagated a given JEC/JER shift."""
    
    verbosity   = max(kwargs.get('verbosity',0),verbosityVariableTools)
    cutsShift   = cuts[:]
    if len(shift)>0 and shift[0] != '_': shift = '_'+shift
    if "jets20" in cuts: LOG.warning("shiftJetSelections: \"jets20\" in cuts")
    for jvar in [ "jpt_1","jpt_2","jeta_1","jeta_2", "jets", "ncbtag",
                  "pfmt_1","met","dphi_ll_bj" ]:
        cutsShift = cutsShift.replace(jvar,jvar+shift)
    cutsShift = cutsShift.replace("met_nom","met") #.replace("jets_nom","jets")
    if verbosity>0: print ">>>   shiftJetSelections with \"%s\" shift\n>>>   \"%s\"\n>>>     -> \"%s\""%(shift,cuts,cutsShift)
    return cutsShift
    
def shiftJetVariable(var,shift,**kwargs):
    """Convert variable to a variable
       that had been propagated a given JEC/JER shift."""
    
    verbosity   = max(kwargs.get('verbosity',0),verbosityVariableTools)
    varShift    = var[:]
    if len(shift)>0 and shift[0] != '_': shift = '_'+shift
    if "jets20" in var: LOG.warning('shiftJetVariable: "jets20" in var')
    for jvar in [ "jpt_1", "jpt_2", "jeta_1", "jeta_2", "jets", "ncbtag",
                  "pfmt_1", "met", "dphi_ll_bj" ]:
        varShift = varShift.replace(jvar,jvar+shift)
    varShift = varShift.replace("met_nom","met")
    if verbosity>0: print '>>>   shiftJetSelections with "%s" shift\n>>>   "%s"\n>>>     -> "%s"'%(shift,var,varShift)
    return varShift
    


class Variable(object):
    """
    Variable class to:
       - hold all relevant information of a variable that will be plotted;
           var name, filename friendly name, LaTeX friendly title, binning, ...
       - allow for variable binning into TH1
       - allow for contextual binning, i.e. depending on channel/selection/...
       - easy string conversions: filename, LaTeX, ...
       - analysis-specific operations: applying variations, ...
    """
    
    def __init__(self, name, *args, **kwargs):
        strings         = [a for a in args if isinstance(a,str) ]
        self.name            = name
        self.title           = strings[0] if strings else makeLatex(self.name)
        self.title           = kwargs.get('title',          self.title                  ) # for plot axes
        self.filename        = kwargs.get('filename',       makeFileName(self.name)     ) # for file
        self.filename        = self.filename.replace('$NAME',self.name)
        self.nBins           = None
        self.min             = None
        self.max             = None
        self.xbins           = None
        self.setBinning(*args)
        self.units           = kwargs.get('units',          ""                          ) # for plot axes
        self.logx            = kwargs.get('logx',           False                       )
        self.logy            = kwargs.get('logy',           False                       )
        self.position        = kwargs.get('position',       ""                          ) # legend position
        #self.plot            = kwargs.get('plots',          True                        )
        self.veto            = kwargs.get('veto',           [ ]                         )
        self.contexttitle    = getContextFromDict(kwargs, None, key='ctitle'                ) # context-dependent title
        self.contextbinning  = getContextFromDict(kwargs, None, key='cbinning', regex=True  ) # context-dependent binning
        self.contextposition = getContextFromDict(kwargs, None, key='cposition', regex=True ) # context-dependent position
        if self.veto:
          if not (isinstance(self.veto,list) or instance(self.veto,tuple)): self.veto = [ self.veto ]
    
    @property
    def var(self): return self.name
    @var.setter
    def var(self,value): self.name = value
    
    @property
    def N(self): return self.nBins
    @N.setter
    def N(self,value): self.nBins = value
    
    @property
    def a(self): return self.min
    @a.setter
    def a(self,value): self.a = value
    
    @property
    def b(self): return self.max
    @b.setter
    def b(self,value): self.b = value
    
    @property
    def xmin(self): return self.min
    @xmin.setter
    def xmin(self,value): self.xmin = value
    
    @property
    def xmax(self): return self.max
    @xmax.setter
    def xmax(self,value): self.xmax = value
    
    def __str__(self):
      """Returns string representation of Variable object."""
      return self.name
    
    def __repr__(self):
      """Returns string representation of Variable object."""
      #return '<%s.%s("%s","%s",%s,%s,%s)>'%(self.__class__.__module__,self.__class__.__name__,self.name,self.title,self.nBins,self.xmin,self.xmax)
      return '<%s("%s","%s",%s,%s,%s)>'%(self.__class__.__name__,self.name,self.title,self.nBins,self.xmin,self.xmax)
      #hex(id(self))
    
    def __iter__(self):
      """Start iteration over variable information."""
      for i in [self.name,self.nBins,self.min,self.max]:
        yield i
    
    def setBinning(self,*args):
        """Set binning: (N,min,max), or xbins if it is set"""
        numbers         = [a for a in args if isinstance(a,int) or isinstance(a,float) ]
        xbins           = [a for a in args if isinstance(a,list) or isinstance(a,tuple) ]
        if len(numbers)==3:
          self.nBins    = numbers[0]
          self.min      = numbers[1]
          self.max      = numbers[2]
          self.xbins    = None
        elif len(xbins)>1:
          xbins         = xbins[0]
          self.nBins    = len(xbins)-1
          self.min      = xbins[0]
          self.max      = xbins[-1]
          self.xbins    = array('d',list(xbins))
        else:
          print error('Variable: bad arguments "%s" for binning!'%(args))
          exit(1)

          
    def getBinning(self):
        """Get binning: (N,xmin,xmax), or xbins if it is set"""
        if self.hasVariableBinning():
          return self.xbins
        else:
          return (self.nBins,self.min,self.max)
        
    def hasVariableBinning(self):
        """True is xbins is set."""
        return xbins != None
    
    def isPartOf(self, *searchterms, **kwargs):
        """Check if all labels are in the variable's name, title."""
        searchterms = [l for l in searchterms if l!='']
        if not searchterms: return False
        found       = True
        regex       = kwargs.get('regex',       False   )
        exlcusive   = kwargs.get('exclusive',   True    )
        for searchterm in searchterms:
            if not regex:
                searchterm = re.sub(r"([^\.])\*",r"\1.*",searchterm) # replace * with .*
            if exlcusive:
                for varlabel in [self.name,self.title]:
                    matches    = re.findall(searchterm,varlabel)
                    if matches: break
                else: return False # none of the labels contain the searchterm
            else: # inclusive
                for varlabel in [self.name,self.title]:
                    matches    = re.findall(searchterm,varlabel)
                    if matches: return True # one of the searchterm has been found
        return exlcusive
    
    def changeContext(self,*args):
        """Change the contextual title for a set of arguments, if it is available"""
        if self.contexttitle:
          title = self.contexttitle.getContext(*args)
          if title!=None: self.title = title
        if self.contextbinning:
          binning = self.contextbinning.getContext(*args)
          if binning!=None: self.setBinning(*binning)
        if self.contextposition:
          position = self.contextposition.getContext(*args)
          if position!=None: self.position = position
        #if self.contextplot:
        #  plot = self.contextplot.getContext(*args)
        #  if binning!=None: self.plot = plot
    
    def plotForSelection(self,selection):
        if not isinstance(selection,str):
          selection = selection.selection
        for searchterm in self.veto:
          if re.search(searchterm,selection):
              LOG.verbose('Variable::plotForSelection: Regex match of selection "%s" to "%s"'%(selection,searchterm),True)
              return False
        return True
    
    def unwrap(self):
        return (self.name,self.nBins,self.min,self.max)
    
    def latex(self):
        return makeLatex(self.name)
    
    #def load(self,context):
    #    """Load contextual binning, if available."""
    #    for pattern, variable in self.context:
    #        if re.match("(?:" + pattern + r")\Z", context):
    #            return variable
    
    def shiftJetVariable(self,shift,**kwargs):
        return shiftJetVariable(self.name,shift,**kwargs)

def var(*args,**kwargs):
    """Shorthand for Variable class."""
    return Variable(*args,**kwargs)
    
def wrapVariable(*args,**kwargs):
    """Help function to wrap variable arguments into a Variable object."""
    if   len(args) == 4 or len(args) == 5:
      return Variable(args) # (varname,N,a,b)
    elif len(args) == 1 and isinstance(args[0],Variable):
      return args[0]
    LOG.warning('wrapVariable: Could not unwrap arguments "%s" to a Variable object. Returning None.'%args)
    return None
    
def unwrapVariableBinning(*args,**kwargs):
    """Help function to unwrap variable arguments to return variable name, number of bins,
    minumum and maximum x axis value."""
    if   len(args) == 4:
      return (varname,N,a,b)
    elif len(args) == 1 and isintance(args[0],Variable):
      return args[0].unwrap()
    LOG.warning('unwrapVariableBinning: Could not unwrap arguments "%s" to a Variable object. Returning None.'%args)
    return None



class Context(object):
    """
    Context class to save different objects that depend on a certain context 
    TODO: point to specific attribute ?
    TODO: allow to set context for pattern (e.g. selection string)
    """
    
    def __init__(self, context_dict, *args, **kwargs):
        if not isinstance(context_dict,dict):
          LOG.warning("Context::Context: No dictionary given!")
        self.context = context_dict
        self.default = args[0] if len(args)>0 else context_dict.get('default',None)
        self.regex   = kwargs.get('regex',False)
        
    def __iter__(self):
        """Start iteration over selection information."""
        for i in self.context:
          yield i
        
    def getContext(self,*args,**kwargs):
        """Get the contextual object for a set of ordered arguments. If it is not available, return Default."""
        
        regex = kwargs.get('regex', self.regex)
        
        # CHECK
        if len(args)==0:
          LOG.warning("Context::getContext: No arguments given!")
          return self.default
        if not self.context:
          LOG.warning("Context::getContext: No context dictionary!")
          return None
        
        # MATCH
        ckey = args[0]
        if regex:
          for key in sorted(self.context,key=lambda x: len(x),reverse=True):
            #LOG.verbose('Context::getContext: Matching "%s" to "%s"'%(key,ckey),True)
            if re.search(key,ckey):
              #LOG.verbose('Context::getContext: Regex match of key "%s" to "%s"'%(key,ckey),True)
              ckey = key
              break
          else:
              return self.default
        elif ckey not in self.context:
          return self.default
        result = self.context[ckey]
        
        # RESULT
        if isinstance(result,Context):
          return result.getContext(*args[1:],**kwargs) # recursive
        else:
          return result
        

def getContextFromDict(contextdict,*default,**kwargs):
    """Check for context in contextdict. If a dictionary is given, make a Context object. Else return None."""
    ckey    = kwargs.get('key',         'context'   )
    regex   = kwargs.get('regex',       False       )
    context = contextdict.get(ckey,     None        ) # context-dependent
    if isinstance(context,Context):
        return context
    if isinstance(context,dict):
        if len(default)==0: default = context.get('default', None)
        else: default = default[0]
        context = Context(context,default,regex=regex)
        return context
    elif not context:
        return None
    LOG.error('getContext - No valid arguments "%s"'%(args))
    return None


