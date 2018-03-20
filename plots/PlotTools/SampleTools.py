#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Izaak Neutelings (2017)

import re
from ctypes import c_double
from math import sqrt, pow
from ROOT import TFile, TTree, TH1D, TH2D, gDirectory, TColor, \
                 kAzure, kBlack, kBlue, kCyan, kGray, kGreen, kMagenta, kOrange, kPink, kRed, kSpring, kTeal, kWhite, kViolet, kYellow
from copy import copy, deepcopy

# for channel in ["mutau","etau","emu","mumu"]:
#     TTscales[channel] = {"category 1":0, "category 2":0} # so TT renormalization is done once for each category

# QCDcol = TColor.GetColor(250,202,255);   ttcol_v2 = TColor.GetColor(135,206,250)
# DYcol  = TColor.GetColor(248,206,104);   ZLcol    = TColor.GetColor(100,182,232)
# WJcol  = TColor.GetColor(222,90,106);    VVcol    = TColor.GetColor(222,140,106)
# TTcol  = TColor.GetColor(155,152,204);   TTJcol   = TColor.GetColor(100,222,106)


colors_sample_dict = {
    "TT":               kRed-2,
    'TTT':              kRed-2,         'ZTT':              kGreen-2,
    'TTL':              kRed+1,         'ZL':               kAzure+5,
    'TTJ':              kPink-2,        'ZJ':               kSpring-7,
    'ttbar':            kRed-2,         'Drell*Yan':        kGreen-2,
    'ttbar*real*tau':   kRed-2,         'Z*tau':            kGreen-2,
    'ttbar*l':          kRed+1,         'Z*ll':             kAzure+1,
    'ttbar*j':          kPink-2,        'Z*j*tau':          kGreen-7,
    'ttbar*other':      kOrange+9,      'Drell*Yan other':  kAzure+5, #kSpring+3,
    'ST':               kMagenta-3,     'D*Y*10*50':        kAzure+5,
    'single top':       kMagenta-3,     'D*Y*50':           kGreen-2,
    'QCD':              kRed-7,         'WW':               kYellow+771,
    'W*jets':           kOrange-5,      'WZ':               kYellow+771,
    'W*J':              kOrange-5,      'ZZ':               kYellow+771,
    'W':                kOrange-5,      'VV':               kYellow+771,
    'data':             kBlack,         'diboson':          kYellow+771,
    'single muon':      kBlack,         'signal':           kAzure+4,
    'single electron':  kBlack,
}

nPlotsMade = 0


def makeSFrameSamples(samplesD,samplesB,samplesS,**kwargs):
    """
    Make Sample objects from a list of SFrame samples given
      subdir, name, title and cross section for simulations,
      subdir, name and title for data.
    The data should be a dictionary with channel as keys.
    """
    outdir = kwargs.get('dir',      SAMPLE_DIR  )
    weight = kwargs.get('weight',   ""          )
    
    # DATA
    for channel, sample in samplesD.items():
        subdir, name, title = sample[:3]
        sdict = dict(kwargs,**sample[3]) if len(sample)>3 else kwargs.copy()
        sdict['weight'] = ""
        samplesD[channel] = SFrameSampleD(subdir,name,title,**sdict)
    
    # BACKGROUND
    for i, sample in enumerate(samplesB):
        subdir, name, title, sigma = sample[:4]
        sdict = dict(kwargs,**sample[4]) if len(sample)>4 else kwargs.copy()
        samplesB[i] = SFrameSampleB(subdir,name,title,sigma,**sdict)
    
    # SIGNAL
    for i, sample in enumerate(samplesS):
        subdir, name, title, sigma = sample[:4]
        sdict = dict(kwargs,**sample[4]) if len(sample)>4 else kwargs.copy()
        samplesS[i] = SFrameSampleS(subdir,name,title,sigma,**sdict)
    
def SFrameSampleB(subdir,name,title,sigma,**kwargs):
    """Help function to create a background Sample object with SFrame information."""
    kwargs['SFrame']     = True
    kwargs['background'] = True
    return Sample(name,title,sigma,SFrameOutputPath(SAMPLE_DIR,subdir,name),**kwargs)
    
def SFrameSampleS(subdir,name,title,sigma,**kwargs):
    """Help function to create a signal Sample object with SFrame information."""
    kwargs['SFrame'] = True
    kwargs['signal'] = True
    return Sample(name,title,sigma,SFrameOutputPath(SAMPLE_DIR,subdir,name),**kwargs)
    
def SFrameSampleD(subdir,name,title,**kwargs):
    """Help function to create a data Sample object with SFrame information."""
    kwargs['SFrame'] = True
    kwargs['data']   = True
    kwargs['weight'] = ""
    return Sample(name,title,SFrameOutputPath(SAMPLE_DIR,subdir,name),**kwargs)
    
def SFrameOutputPath(outdir,subdir,samplename,*args,**kwargs):
    """Return a path to a root file from SFrame."""
    verbosity   = getVerbosity(kwargs,verbosityPlotTools,verbositySampleTools)
    tag         = globalTag
    if args and isinstance(args,str): tag = args[0]
    file        = "%s/%s/TauTauAnalysis.%s%s.root" % (outdir,subdir,samplename,tag)
    LOG.verbose("file = \"%s\""%(file),     verbosity,level=3)
    return file
    
def shiftSample(samples0,searchterms,file_app,title_app,**kwargs):
    """Shift sample filename and title. Find the sample via a simple search term."""
    weight      = kwargs.get('weight',      ""          )
    filter      = kwargs.get('filter',      False       )
    #samples     = getSample(samples0,searchterm)
    if not (isinstance(searchterms,list) or isinstance(searchterms,tuple)): searchterms = [ searchterms ]
    
    samples     = [ ]
    for searchterm in searchterms:
      for sampleinfo in samples0:
        subdir, filename, title, sigma = sampleinfo[:4]
        sdict = sampleinfo[4] if len(sampleinfo)>4 else { }
        if searchterm in subdir or searchterm in filename or searchterm in title:
          samples.append((subdir, filename+file_app, title+title_app, sigma, sdict))
        elif not filter:
          samples.append(sampleinfo)
    print samples
    
    return samples


    ############
    # Cutflows #
    ############

def getEfficienciesFromHistogram(hist,cuts):
    """Get efficiencies for some histogram, as defined by a list of selections."""
    
    efficiencies = [ ]
    N_tot0 = hist.GetBinContent(1)
    N_tot  = N_tot0
    N      = N_tot0
    for i, cutname in enumerate(cuts,1):
        if i>1:      N = hist.GetBinContent(i)
        if N_tot0<1: N_tot0 = N
        if N and N_tot:
            efficiencies.append(( cutname, N, N/N_tot*100, N/N_tot0*100 ))
        else:
            efficiencies.append(( cutname, N, 0, 0 ))
            LOG.warning("getEfficienciesFromHistogram - GetBinContent(%i) = %s, GetBinContent(%i) = %s "%(i,N,i-1,N_tot))
        N_tot = N
    
    #for cutname, efficiency in efficiencies:
    #    print ">>> %s: %5.2f%%" % (cut,efficiency*100)
    
    return efficiencies
    
def getEfficienciesFromTree(tree,cuts,**kwargs):
    """Get efficiencies for some tree, as defined by a list of selections [(name,cut)]."""
    
    efficiencies = [ ]
    if not cuts: return [ ]
    N_tot0 = kwargs.get('N',float(tree.GetEntries(cuts[0][1])))
    N_tot  = N_tot0
    N      = N_tot0
    for i, (cutname,cut) in enumerate(cuts):
        N = float(tree.GetEntries(cut))
        if N_tot0<1:  N_tot0 = N
        if N and N_tot:
            efficiencies.append(( cutname, N, N/N_tot*100, N/N_tot0*100 ))
        else: 
            efficiencies.append(( cutname, N, 0, 0 ))
            LOG.warning("getEfficienciesFromTree - GetEntries(cut) = %.1f, GetEntries(cut-1) = %.1f, cut=%s"%(N,N_tot,cut))
        N_tot = N
    
    return efficiencies
    
def printComparingCutflow(efficiencies1,efficiencies2):
    print ">>> %13s:   %21s %8s   %15s   %16s   " % ("name","events".center(21,' '),"ratio".center(5,' '),"rel. eff.".center(15,' '),"abs. eff.".center(17,' '))
    for (name1,N1,releff1,abseff1), (name2,N2,releff2,abseff2) in zip(efficiencies1,efficiencies2):
       ratio = "-"
       if N1: ratio = N2/N1
       print (">>> %13s:   %9d - %9d %8.2f   %6.2f - %6.2f   %7.3f - %7.3f  " % (name1,N1,N2,ratio,releff1,releff2,abseff1,abseff2))
    


def getColor(name):
    """Get color for some sample name."""
    if isinstance(name,Sample): name = sample.name
    for searchterm in sorted(colors_sample_dict,key=lambda x: len(x),reverse=True):
      if re.findall(searchterm.replace('*',".*"),name):
        LOG.verbose('getColor - "%s" gets color %s from searchterm "%s"!'%(name,colors_sample_dict[searchterm],searchterm),verbositySampleTools,level=3) 
        return colors_sample_dict[searchterm]
    LOG.warning('getColor: Could not find color for "%s"!'%name)
    return 0
    


    ##########
    # Sample #
    ##########

class Sample(object):
    """
    TODO:
    Sample class to
      - hold all relevant sample information: file, name, cross section, number of events,
        type, extra weight, extra scale, color, ...
      - calculate and set normalization (norm) based on integrated luminosity, cross section
        and number of events
      - make histogram with the Plot class
      - split histograms into subsamples (based on some (generator-level) selections
    """
    
    def __init__(self, name, title, *args, **kwargs):
        
        # UNWRAP optional arguments
        sigma    = -1.0
        filename = ""
        for arg in args:
            if sigma < 0 and not kwargs.get('sigma',False) and\
               (isinstance(arg,float) or isinstance(arg,int)): sigma = arg
            if not filename and not kwargs.get('filename',False) and\
               isinstance(arg,str): filename = arg
        
        # INITIALIZE attributes
        self.name           = name
        self.title          = title
        self.tags           = [ ]
        self.filename       = kwargs.get('filename',        filename            )
        self.filenameshort  = "/".join(self.filename.split('/')[-2:])
        self.file           = TFile(self.filename) if self.filename else None
        self._tree          = kwargs.get('tree',            None                )
        self._treename      = kwargs.get('treeName',        "tree_mutau"        )
        self.sigma          = kwargs.get('sigma',           sigma               )
        self.N              = kwargs.get('N',               -1                  ) # sum weights
        self.N_unweighted   = kwargs.get('N_unweighted',    -1                  ) # "raw" number of MC events
        self.N_exp          = kwargs.get('N_exp',           -1                  ) # events you expect to have to check fail rate
        self.binN_weighted  = kwargs.get('binN_weighted',   8                   ) # index of bin with total sum of weight
        self.norm           = kwargs.get('norm',            1.0                 ) # normalization L*sigma/N
        self.scale          = kwargs.get('scale',           1.0                 ) # renormalization scales
        self.upscale        = kwargs.get('upscale',         1.0                 ) # drawing up/down scaling
        self._scaleBU       = self.scale # back up scale to overwrite previous renormalizations
        self.weight         = kwargs.get('weight',          ""                  ) # weights
        self.extraweight    = kwargs.get('extraweight',     ""                  ) # extra weights
        self.cuts           = kwargs.get('cuts',            ""                  ) # extra cuts
        self.isData         = kwargs.get('data',            False               )
        self.isBackground   = kwargs.get('background',      False               )
        self.isSignal       = kwargs.get('signal',          False               )
        self.blind          = kwargs.get('blind',           { }                 )
        self.split_dict     = kwargs.get('split',           { }                 )
        self.splitsamples   = [ ]
        self.color          = kwargs.get('color',           getColor(self.title))
        self.linecolor      = kwargs.get('linecolor',       kBlack              )
        self.lumi           = kwargs.get('lumi',            luminosity          )
        self.isSFrame       = kwargs.get('SFrame',          True                )
        
        # CHECK FILE
        if not isinstance(self,MergedSample) and (not self.file or not isinstance(self.file,TFile)): # self.filename
            LOG.fatal('SampleSet::SampleSet: Could not open or find file for "%s" sample: "%s"'%(self.name,self.filename))
        
        # SFRAME
        if self.sigma>=0 and self.isSFrame and not self.isData and not isinstance(self,MergedSample):
            self.normalizeToLumiCrossSectionSFrame(self.lumi)
        
        # CHECK NUMBER OF EVENTS
        if 0 < self.N < self.N_exp*0.97:
            LOG.warning('SampleSet::SampleSet: Sample "%s" has significantly less events (%d) than expected (%d).'%(self.N,self.N_exp))
        
        # SPLIT
        if self.split_dict:
            self.split(self.split_dict,**kwargs)
        
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
      """Returns string representation of Variable object."""
      #return '<%s.%s("%s","%s") at %s>'%(self.__class__.__module__,self.__class__.__name__,self.name,self.title,hex(id(self)))
      return '<%s("%s","%s") at %s>'%(self.__class__.__name__,self.name,self.title,hex(id(self)))
      
    def __add__(self, sample):
        """Add samples into MergedSamples."""
        if isinstance(sample,Sample):
          mergedsample = MergedSample(self,sample)
          return self
        return None
    
    def __mul__(self, scale):
        """Multiply selection with some weight (that can be string or Selection object)."""
        if isinstance(scale,float) or isinstance(scale,int):
          self.setScale(scale)
          return self
        return None
    
    def row(self,**kwargs):
        """Returns string that can be used as a row in a samples summary table"""
        pre    = kwargs.get('pre', "")
        return ">>>  %s%-20s  %-40s  %12.2f  %10i  %11i  %10.3f  %s" %\
          (pre,self.title,self.name,self.sigma,self.N_unweighted,self.N,self.norm,self.extraweight)
    
    def printRow(self):
        print self.row()
        
    def printSampleObjects(self,**kwargs):
        """Print all sample objects recursively"""
        pre = kwargs.get('pre',"")
        print ">>> %s%r"%(kwargs.get('pre',""),self)
        if isinstance(self,MergedSample):
          for sample in self.samples:
            sample.printSampleObjects(pre=pre+"  ")
        for sample in self.splitsamples:
          sample.printSampleObjects(pre=pre+"  ")
    
    #@property
    #def filename(self):
    #  return self._filename
    #
    #@filename.setter
    #def filename(self, value):
    #  self._filename = value
    #  if self.file:
    #    self.file.Close()
    #    self.file = TFile(self._filename)
    #  if isinstance(self,MergedSample):
    #    for sample in self.samples:
    #      sample.filename = value
    #  for sample in self.splitsamples:
    #      sample.filename = value
    
    @property
    def treename(self):
      return self._treename
    
    @treename.setter
    def treename(self, value):
      self._treename = value
      if isinstance(self,MergedSample):
        for sample in self.samples:
          sample.treename = value
      for sample in self.splitsamples:
          sample.treename = value
    
    @property
    def tree(self):
      if self._tree:
        if self._tree.GetName()==self._treename:
          return self._tree
        else:
          return self.file.Get(self._treename)
      else: return self.file.Get(self._treename)
    
    @tree.setter
    def tree(self, value):
      self._tree = value
    
    @property
    def labels(self):
      return [ self.name, self.title, self.filenameshort ]
    
    @labels.setter
    def labels(self, value):
      LOG.warning("Sample - No setter for \"labels\" attribute!")
    
    @property
    def scaleBU(self):
      return self._scaleBU
    
    @scaleBU.setter
    def scaleBU(self, value):
      LOG.warning("Sample - Not allowed to set scaleBU (%.4g)!"%self._scaleBU)
      
    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for key, val in self.__dict__.items():
            setattr(result, key, deepcopy(val, memo))
        return result
    
    def clone(self,*args,**kwargs):
        """Shallow copy."""
        samename                = kwargs.get('samename', False )
        deep                    = kwargs.get('deep',     False )
        name                    = args[0] if len(args)>0 else self.name  + ("" if samename else  "_clone" )
        title                   = args[1] if len(args)>1 else self.title + ("" if samename else " (clone)")
        filename                = args[2] if len(args)>2 else self.filename
        newsample               = type(self)(name,title,filename,**kwargs)
        splitsamples            = [s.clone(samename=samename,deep=deep) for s in self.splitsamples] if deep else self.splitsamples[:]
        newsample               = type(self)(name,title,filename,**kwargs)
        newdict                 = self.__dict__.copy()
        newdict['name']         = name
        newdict['title']        = title
        newdict['splitsamples'] = splitsamples
        if deep and self.file:
          file = TFile(self.file.GetName())
          newdict['file'] = file
        newsample.__dict__.update(newdict)
        return newsample
        
    def setColor(self,*args):
        """Set color"""
        self.color = args[0] if args else getColor(self.title)
        
    #def setFileName(self,filename):
    #    """Set filename."""
    #    self.filename = filename
        
    def appendFileName(self,file_app):
        """Append filename (before globalTag)."""
        oldfilename   = self.filename
        newfilename   = oldfilename if file_app in oldfilename else oldfilename.replace(globalTag,file_app+globalTag)
        self.filename = newfilename
        if self.file:
          reopenTree = True if self.tree else False
          self.file.Close()
          self.file = TFile(self.filename)
          if reopenTree: self.tree = self.file.Get(self.treename)
        LOG.verbose('replacing "%s" with "%s"'%(oldfilename,self.filename),verbositySampleTools,level=3)
        if isinstance(self,MergedSample):
          for sample in self.samples:
            sample.appendFileName(file_app)
        for sample in self.splitsamples:
            sample.appendFileName(file_app)
        
    def setTreeName(self,treename):
        """Set treename."""
        self.treename = treename
        
    def setScale(self,scale):
        """Set treename, for split samples as well."""
        self.scale = scale
        for sample in self.splitsamples:
            sample.scale = scale
        
    def resetScale(self,scale=1,**kwargs):
        """Reset scale to BU scale."""
        self.scale = self.scaleBU*scale
        for sample in self.splitsamples:
            sample.resetScale(**kwargs)
        if isinstance(self,MergedSample):
          for sample in self.samples:
            sample.resetScale(**kwargs)
        
    def reloadFile(self,**kwargs):
        """Close and reopen file. Use it to free up some memory."""
        if self.file:
            self.file.Close()
        if self.filename:
            self.file = TFile(self.filename)
        for sample in self.splitsamples:
            sample.reloadFile(**kwargs)   
        if isinstance(self,MergedSample):
          for sample in self.samples:
            sample.reloadFile(**kwargs)
        
    def addWeight(self, weight):
        """Combine weight."""
        #print ">>> addWeight: combine weights %s" % self.weight
        self.weight = combineWeights(self.weight, weight)
        
    def normalizeToLumiCrossSection(self,lumi,**kwargs):
        """Calculate and set the normalization for simulation as L*sigma/N"""
        norm     = 1
        sigma    = kwargs.get('sigma',  self.sigma  )
        N_events = kwargs.get('N',      self.N      )
        if self.sigma<0:
            LOG.warning("Sample::normalizeToLumiCrossSection: Cannot normalize sigma = %s < 0"%(sigma))
            return -1
        if self.isData:
            LOG.warning('Sample::normalizeToLumiCrossSection: Ignoring data sample "%s"'%(self.name))
            return norm
        if N_events:
            norm = lumi*sigma*1000/N_events
        else:
            LOG.warning('Sample::normalizeToLumiCrossSection: Cannot normalize "%s" sample: N_events = %s!'%(self.name,N_events))
        if norm <= 0:
            LOG.warning('Sample::normalizeToLumiCrossSection: Calculated normalization for "%s" sample is %.5g <= 0 (L=%.5g,sigma=%.5g,N=%.5g)!'%(self.name,norm,lumi,sigma,N_events))
        
        self.norm = norm
        return norm
        
    
    def normalizeToLumiCrossSectionSFrame(self,lumi,**kwargs):
        """Calculate and set the normalization for a SFrame sample."""
        
        channel             = kwargs.get('cutflow',             "mutau"             )
        binN                = kwargs.get('binN',                1                   )
        binN_weighted       = kwargs.get('binN_weighted',       self.binN_weighted  )
        cutflowHist         = self.file.Get("histogram_%s/cutflow_%s"%(channel,channel))
        if not cutflowHist:
            cutflowHist     = self.file.Get("histogram_emu/cutflow_emu")
        if not cutflowHist:
            cutflowHist     = self.file.Get("histogram_ditau/cutflow_ditau")
        self.N              = cutflowHist.GetBinContent(binN_weighted)
        self.N_unweighted   = cutflowHist.GetBinContent(binN)
        
        return self.normalizeToLumiCrossSection(lumi,**kwargs)
        
    
    def split(self,*args,**kwargs):
        """Split sample for some dictionairy of cuts."""
        
        verbosity      = getVerbosity(kwargs,verbositySampleTools)
        split_dict     = args[0] if len(args) else self.split_dict
        splitsamples   = [ ]
        
        for i, (title, cut) in enumerate(split_dict.items()):
            sample       = self.clone("%s_split%d"%(self.name,i),title)
            sample.cuts  = combineCuts(self.cuts,cut)
            sample.color = getColor(sample.title)
            splitsamples.append(sample)
        
        self.split_dict   = split_dict
        self.splitsamples = splitsamples # save list of split samples
        #return splitsamples
        
    
    def hist(self, *args, **kwargs):
        """Make a histogram with a tree."""
        
        verbosity     = getVerbosity(kwargs,verbositySampleTools)
        var, N, a, b, cuts = unwrapVariableSelection(*args)
        scale         = kwargs.get('scale',           1.0                         ) * self.scale * self.upscale * self.norm
        treename      = kwargs.get('treename',        self.treename               )
        name          = kwargs.get('name',            makeHistName(self.name,var) )
        name         += kwargs.get('append',          ""                          )
        title         = kwargs.get('title',           self.title                  )
        shift         = kwargs.get('shift',           0                           )
        smear         = kwargs.get('smear',           0                           )
        blind         = kwargs.get('blind',           self.blind                  )
        color0        = kwargs.get('color',           self.color                  )
        linecolor     = kwargs.get('linecolor',       self.linecolor              )
        
        if self.upscale != 1:
            title += " (#times%d)" % (self.upscale)
        
        # CUTS & WEIGHTS
        blindcuts = ""
        if var in blind and "SS" not in name: blindcuts = blind[var] # TODO: blind by removing bins from hist or rounding? FindBin(a), SetBinContent
        weight    = combineWeights(self.weight, self.extraweight, kwargs.get('weight', ""))
        cuts      = combineCuts(cuts, kwargs.get('cuts', ""), self.cuts, blindcuts, weight=weight)
        
        # TREE
        tree = None
        if treename!=self.treename: tree = self.file.Get(treename)
        elif not self.tree:         tree = self.file.Get(treename)
        else:                       tree = self.tree
        if not tree or not isinstance(tree,TTree):
          if not self.file:
            LOG.error('Sample::hist Could not find tree "%s" for "%s"! File is closed: %s'%(treename,self.name,self.filename))
          else:
            LOG.error('Sample::hist Could not find tree "%s" for "%s"! Check %s'%(treename,self.name,self.filename))
          exit(1)
        
        # HIST
        hist = TH1D(name, title, N, a, b)
        if self.isData: hist.SetBinErrorOption(TH1D.kPoisson)
        else:           hist.Sumw2()
        
        # DRAW
        out = tree.Draw("%s >> %s" % (var,name), cuts, "gOff")
        if out < 0: LOG.error("Drawing histogram for %s sample failed!" % (title))
        
        # SCALE
        if scale != 1.0: hist.Scale(scale)
        if scale == 0.0: LOG.warning("Scale of %s is 0!" % self.name)
        if verbosity>2: printBinError(hist)
        
        # STYLE
        hist.SetLineColor(linecolor)
        hist.SetFillColor(color0)
        hist.SetMarkerColor(color0)
        
        # PRINT
        if verbosity>1:
            # TODO: make simple table ?
            print ">>>\n>>> Sample - %s, %s: %s (%s)" % (color(name,color="grey"),var,self.filenameshort,self.treename)
            print ">>>    norm=%.4f, scale=%.4f, total %.4f" % (self.norm,self.scale,scale)
            print ">>>    weight:  %s" % (("\n>>>%s*("%(' '*18)).join(weight.rsplit('*(',max(0,weight.count("*(")-1))))
            print ">>>    entries: %d (%.2f integral)" % (hist.GetEntries(),hist.Integral())
            print ">>>    %s" % (cuts.replace("*(","\n>>>%s*("%(' '*18)))
        return hist
        
    
    def isPartOf(self, *searchterms, **kwargs):
        """Check if all labels are in the sample's name, title or tags."""
        searchterms = [l for l in searchterms if l!='']
        if not searchterms: return False
        found       = True
        regex       = kwargs.get('regex',       False   )
        exlcusive   = kwargs.get('exclusive',   True    )
        for searchterm in searchterms:
            if not regex:
                searchterm = re.sub(r"(?<!\\)\+",r"\+",searchterm) # replace + with \+
                searchterm = re.sub(r"([^\.])\*",r"\1.*",searchterm) # replace * with .*
            if exlcusive:
                for samplelabel in [self.name,self.title]+self.tags:
                    #print "Sample::isPartOf - %s in %s ? (excl.)"%(searchterm,samplelabel)
                    matches    = re.findall(searchterm,samplelabel)
                    if matches: break
                else: return False # none of the labels contain the searchterm
            else: # inclusive
                for samplelabel in [self.name,self.title]+self.tags:
                    #print "Sample::isPartOf - %s in %s ? (incl.)"%(searchterm,samplelabel)
                    matches    = re.findall(searchterm,samplelabel)
                    if matches: return True # one of the searchterm has been found
        return exlcusive
    


class SampleData(object):
    def __init__(self, name, title, *args, **kwargs):
        kwargs['isData'] = True
        Sample.__init__(self,name,title,*args,**kwargs)
    




    ################
    # MergedSample #
    ################

class MergedSample(Sample):
    """Class to combine a list of Sample objects to make one histogram with the Plot class."""

    def __init__(self, *args, **kwargs):
        name, title, samples = unwrapMergedSamplesArgs(*args,**kwargs)
        self.samples = list(samples)
        Sample.__init__(self,name,title)
        if self.samples: self.initFromSample(samples[0])
        
    def initFromSample(self, sample, **kwargs):
        """Set some relevant attributes (inherited from the Sample class) with a given sample."""
        self.filename     = sample.filename
        self._treename    = sample.treename
        self.isSignal     = sample.isSignal
        self.isBackground = sample.isBackground
        self.isData       = sample.isData
        self._color       = sample.color
        self.linecolor    = sample.linecolor
        self.split_dict   = sample.split_dict
    
    def __iter__(self):
      """Start iteration over samples."""
      for sample in self.samples:
        yield sample
    
    def __add__(self,sample):
      """Start iteration over samples."""
      self.add(sample)
    
    def add(self, sample, **kwargs):
        """Add Sample object to list of samples."""
        if not self.samples: self.initFromSample(sample)
        self.samples.append(sample)
    
    def row(self,**kwargs):
        """Returns string that can be used as a row in a samples summary table."""
        pre    = kwargs.get('pre', "")
        string = ">>>  %s%-20s  %-40s  %12.2f  %10i  %11i  %10.3f  %s" %\
          (pre,self.title,self.name,self.sigma,self.N_unweighted,self.N,self.norm,self.extraweight)
        for sample in self.samples:
          string += "\n" + sample.row(pre=pre+"  ")
        return string
    
    def clone(self,*args,**kwargs):
        """Shallow copy."""
        samename           = kwargs.get('samename', False )
        deep               = kwargs.get('deep',     False )
        #samples            = kwargs.get('samples',  False )
        strings            = [ a for a in args if isinstance(a,str) ]
        name               = args[0] if len(args)>0 else self.name + ("" if samename else  "_clone" )
        title              = args[1] if len(args)>1 else self.title+ ("" if samename else " (clone)")
        samples            = [s.clone(samename=samename,deep=deep) for s in self.samples] if deep else self.samples[:]
        splitsamples       = [ ]
        for oldsplitsample in self.splitsamples:
          if deep:
            newsplitsample = oldsplitsample.clone(samename=samename,deep=deep)
            if isinstance(newsplitsample,MergedSample):
              # splitsamples.samples should have same objects as self.samples !!!
              for subsample in oldsplitsample.samples:
                if subsample in self.samples:
                  newsplitsample.samples[oldsplitsample.samples.index(subsample)] = samples[self.samples.index(subsample)]
            splitsamples.append(newsplitsample)
          else:
            splitsamples.append(sample)
        newdict            = self.__dict__.copy()
        newdict['name']    = name
        newdict['title']   = title
        newdict['samples'] = samples
        newdict['splitsamples'] = splitsamples
        newsample          = type(self)(name,title,*samples,**kwargs)
        newsample.__dict__.update(newdict)
        return newsample
    
    def hist(self, *args, **kwargs):
        """Draw histgram for multiple samples. (Override Sample method.)"""
        
        verbosity        = getVerbosity(kwargs,verbositySampleTools)
        var, N, a, b, cuts = unwrapVariableSelection(*args)
        name             = kwargs.get('name',               makeHistName(self.name+"_merged", var))
        name            += kwargs.get('append',             ""                      )
        title            = kwargs.get('title',              self.title              )
        blind            = kwargs.get('blind',              self.blind              )
        cuts             = combineCuts(cuts,                self.cuts               )
        kwargs['weight'] = combineWeights(kwargs.get('weight', ""), self.weight     )# pass scale down
        kwargs['scale']  = kwargs.get('scale', 1.0) * self.scale * self.norm # pass scale down
        
        if verbosity>1:
          print ">>>\n>>> Samples - %s, %s: %s" % (color(name,color="grey"), var, self.filenameshort)
          print ">>>    norm=%.4f, scale=%.4f, total %.4f" % (self.norm,kwargs['scale'],self.scale)
        
        hist = TH1D(name, title, N, a, b)
        hist.Sumw2()
        for sample in self.samples:
            if 'name' in kwargs: # prevent memory leaks
                kwargs['name']  = makeHistName(sample.name,name.replace(self.name+'_',''))    
            hist_new = sample.hist(var, N, a, b, cuts, **kwargs)
            hist.Add( hist_new )
            LOG.verbose("    sample %s added with %.1f events (%d entries)" % (sample.name,hist_new.Integral(),hist_new.GetEntries()),verbosity,level=2)
        
        # COLOR
        hist.SetLineColor(self.linecolor)
        hist.SetFillColor(self.color)
        hist.SetMarkerColor(self.color)
        
        if verbosity>2: printBinError(hist)
        return hist
        
                
def unwrapMergedSamplesArgs(*args,**kwargs):
    """Help function to unwrap arguments for MergedSamples."""
    
    strings = [ ]
    samples = [ ]
    args    = list(args)
    for arg in args[:]:
      if isinstance(arg,str):
        strings.append(arg)
        args.remove(arg)
      elif isinstance(arg,Sample):
        samples.append(arg)
        args.remove(arg)
      elif isinstance(arg,list) or isinstance(arg,tuple):
        if arg and isinstance(arg[0],Sample):
          samples.append(arg[0])
          args.remove(arg[0])
    
    if len(strings)==1:
      name, title = strings[0], strings[0]
    elif len(strings)>1:
      name, title = strings[:3]
    elif len(samples)==0:
      name, title = "noname", "no title"
    else:
      name, title = '-'.join([s.name for n in samples]), ', '.join([s.title for n in samples])
    return name, title, samples




    #############
    # SampleSet #
    #############

class SampleSet(object):
    """
    TODO:
    Sample set class to hold set of samples and give easy functionality to:
       - find sample by name/pattern (wildcard or regex?)
       - find samples by type: signal, background, simlation, data samples, ...
       - merge, stitch and split sample by name/pattern,
       - draw all histograms for a given variable and set of selections,
       - allow switching on/off the splitting of samples (e.g. into final state) when draw,
       - allow fixed order,
       - renormalize in control regions: WJ, TT, ... (instead of in Plot)
       - measure OS/SS ratio, ... (instead of in Plot)
    """
    
    def __init__(self, samplesD, samplesB, samplesS, **kwargs):
        
        self.samplesB           = list(samplesB)
        self.samplesS           = list(samplesS)
        self._samplesD          = samplesD # may be a dictionary with channel as keys
        self.channel            = kwargs.get('channel',     "mutau"     )
        self.verbosity          = kwargs.get('verbosity',   0           )
        self.loadingbar         = kwargs.get('loadingbar',  True        ) and self.verbosity<2
        self.ignore             = kwargs.get('ignore',      [ ]         )
        self.shiftQCD           = kwargs.get('shiftQCD',    0           )
        #self.weight             = kwargs.get('weight',      ""          )
        
        self.color_dict         = { }
        self.linecolor_dict     = { }
        
    def __str__(self):
      """Returns string representation of Sample object."""
      return str([s.name for s in self.samplesB+self.samplesS]+[s.name for s in self.samplesD])
    
    def printTable(self):
      """Print table of all samples."""
      print ">>>\n>>> samples with integrated luminosity L = %s / fb at sqrt(s) = 13 TeV" % (luminosity)
      print ">>>  %-20s  %-40s  %12s  %10s  %11s  %10s  %s" %\
            ("sample title","name","sigma [pb]","events","sum weights","norm.","extra weight")
      for sample in self.samples:
        sample.printRow()
    
    @property
    def samples(self):
      """Getter for "samples" attribute of SampleSet."""
      return self.samplesB+self.samplesS+self.samplesD
    @samples.setter
    def samples(self, value):
      """Setter for "samples" attribute."""
      # samplesB, samplesS, samplesD = [ ], [ ], [ ]
      # for sample in value:
      #   if   sample.isData:       samplesD.append(sample)
      #   elif sample.isBackground: samplesB.append(sample)
      #   elif sample.isSignal:     samplesS.append(sample)
      #   else: LOG.warning("Sample.samples - Sample \"%s\" has no background or signal flag!"%sample.title)
      # self.samplesB, self.samplesS, self.samplesD = samplesB, samplesS, samplesD
      LOG.warning("Sample.samplesD - No setter for \"samples\" attribute available!")
    
    @property
    def samplesD(self):
      """Getter for "samplesD". If dataset depends on channel, return the data sample
      corresponding to the current channel."""
      if not self._samplesD:
        return [ ]
      if isinstance(self._samplesD,dict):
        if self.channel in self._samplesD:
          return [self._samplesD[self.channel]]
        else:
          LOG.warning("Sample::samplesD - Channel \"%s\" not in _samplesD: %s"%(self.channel,self._samplesD))
      return self._samplesD
    
    @samplesD.setter
    def samplesD(self, value):
      """Setter for "samplesD". If dataset depends on channel, set the given data sample
      to the current channel."""
      if isinstance(value,dict):
        self._samplesD = value
      elif   isinstance(self._samplesD,dict): #and len(value)==1:
        self._samplesD[self.channel] = value #[0]
      elif isinstance(self._samplesD,list) and isinstance(value,list):
        self._samplesD = value
      LOG.warning("Sample.samplesD - Check setter for \"samplesD\" attribute!")
    
    @property
    def samplesMC(self):
      return self.samplesB + self.samplesS
    @samplesMC.setter
    def samplesMC(self, value):
      samplesB, samplesS = [ ], [ ]
      for sample in value:
        if sample.isBackground: samplesB.append(sample)
        elif sample.isSignal:   samplesS.append(sample)
        else: LOG.warning("Sample::samplesMC - Sample \"%s\" has no background or signal flag!"%sample.title)
      self.samplesB, self.samplesS = samplesB, samplesS
    
    def __iter__(self):
      """Start iteration over samples."""
      for sample in self.samples:
        yield sample
    
    def setTreeName(self,treename):
        """Set tree name for each sample to draw histograms with."""
        for sample in self.samples:
          sample.setTreeName(treename)
          
    def setChannel(self,channel):
        """Set channel."""
        self.channel = channel
    
    def setColors(self):
        """TODO: Check and compare all sample's colors and set to another one if needed."""
        
        verbosity   = getVerbosity(kwargs,verbositySampleTools)
        usedColors  = [ ]
        
        # CHECK SPLIT
        for sample in self.samples:
            if sample.color is kBlack:
                LOG.warning("SamplesSet::setColors - %s"%sample.name)
            if sample.color in usedColor:
                # TODO: check other color
                sample.setColor()
                LOG.warning("SamplesSet::setColors - Color used twice!")
            else:
                usedColors.append(sample.color)
    
    def reloadFile(self,**kwargs):
        """Help function to reload all files in samples list."""
        for sample in self.samples:
            sample.reloadFile()    
        
    def cleanMemory(self):
        """Open/reopen files to reset file memories."""
        global nPlotsMade
        if nPlotsMade%10==0 and nPlotsMade>0:
          self.reloadFile()
        nPlotsMade +=1
    
    def changeContext(self,*args):
        """Help function to change context of variable object."""
        for arg in args:
          if isinstance(arg,Variable):
            arg.changeContext(self.channel)
            selections = [a for a in args if isinstance(a,Selection) or isSelectionString(a)]
            if len(selections)>0:
              arg.changeContext(selections[0].selection)
            return arg
        return None
    
    def plotStack(self, *args, **kwargs):
        """Plot stack."""
        self.cleanMemory()
        kwargs['stack'] = True
        var = self.changeContext(*args)
        plotargs = [ var ] if var else [ ]
        plotargs += self.createHistograms(*args,**kwargs)
        return Plot(*plotargs,**kwargs)
        
    
    def getStack(self, *args, **kwargs):
        """Get stack."""
        name                 = kwargs.get('name',"stack")
        kwargs['data']       = False
        kwargs['signal']     = False
        kwargs['background'] = True
        var = self.changeContext(*args)
        histLists            = self.createHistograms(*args,**kwargs)
        stack                = THStack(name,name)
        for hist in histLists[1]:
            stack.Add(hist)
        return stack

    
    def createHistograms(self,*args,**kwargs):
        """Create histograms for all samples and return lists of histograms and a dictionairy
        of sample objects with histograms as keys."""
        
        var, N, a, b, cuts = unwrapVariableSelection(*args)
        verbosity       = getVerbosity(kwargs,verbositySampleTools)
        weight          = kwargs.get('weight',          ""                  )
        weight_data     = kwargs.get('weight_data',     ""                  )
        split           = kwargs.get('split',           True                )
        reset           = kwargs.get('reset',           False               )
        append          = kwargs.get('append',          ""                  )
        ratio_WJ_QCD    = kwargs.get('ratio_WJ_QCD_SS', False               )
        task            = kwargs.get('task',            "making histograms" )
        
        histsS          = [ ]
        histsB          = [ ]
        histsD          = [ ]
        #samples_dict    = { }
        
        samples = self.samples
        if split:
            samples = [ ]
            for sample in self.samples:
              if sample.splitsamples:
                samples += sample.splitsamples
              else:
                samples.append(sample)
        
        bar = None
        if self.loadingbar and verbosity<2:
            bar = LoadingBar(len(samples),width=16,pre=">>> %s: %s: "%(var,task),counter=True,remove=True)
        for sample in samples:
            if bar:   bar.message(sample.title)
            if reset: sample.resetScale()
            if sample.name in self.ignore:
              if bar: bar.count("%s skipped"%sample.title)
              continue
            
            # ADD background
            if sample.isBackground and kwargs.get('background',True):
              hist = sample.hist(var,N,a,b,cuts,append=append,weight=weight,verbosity=verbosity)
              histsB.append(hist)
              #samples_dict[hist] = sample
            
            # ADD signal
            elif sample.isSignal and kwargs.get('signal',True):
              hist = sample.hist(var,N,a,b,cuts,append=append,weight=weight,verbosity=verbosity)
              histsS.append(hist)
              #samples_dict[hist] = sample
            
            # ADD data
            elif sample.isData and kwargs.get('data',True):
              hist = sample.hist(var,N,a,b,cuts,append=append,weight=weight_data,verbosity=verbosity)
              histsD.append(hist)
              #samples_dict[hist] = sample
            
            if bar: bar.count("%s done"%sample.name)
        
        # ADD QCD
        if kwargs.get('QCD',False):
            hist = self.QCD(var,N,a,b,cuts,ratio_WJ_QCD_SS=ratio_WJ_QCD,append=append,weight=weight,verbosity=verbosity)
            if hist:
              histsB.append(hist)
              #samples_dict[hist] = "QCD"
        
        return [ histsD, histsB, histsS ] #, samples_dict
        
    
    def QCD(self,*args,**kwargs):
        """Substract MC from data with same sign (SS) selection of a lepton - tau pair
           and return a histogram of the difference."""
        
        verbosity            = getVerbosity(kwargs,verbositySampleTools)
        var, N, a, b, cuts0  = unwrapVariableSelection(*args)
        if verbosity > 1:
            print header("estimating QCD for variable %s" % (var))
            #LOG.verbose("\n>>> estimating QCD for variable %s" % (self.var),verbosity,level=2)
        
        samples         = self.samples
        name            = kwargs.get('name',            makeHistName("QCD",var) )
        append          = kwargs.get('append',          ""                      )+"_SS"
        ratio_WJ_QCD    = kwargs.get('ratio_WJ_QCD_SS', False                   )
        doRatio_WJ_QCD  = isinstance(ratio_WJ_QCD,      c_double                )
        
        weight          = kwargs.get('weight',          ""                      )
        weight_data     = kwargs.get('weight',          ""                      )
        
        relax           = 'emu' in self.channel or ("jets" in cuts0 and "btag" in cuts0 and "btag" not in var)
        relax           = kwargs.get('relax',relax) #and False
        if "n" in var.lower() and ("jets" in var or "btag" in var):
          if relax:
            LOG.warning("SampleSet::QCD - Don't relax cuts in QCD CR for \"%s\""%(var))
            relax = False
        
        shift           = kwargs.get('shift',0.0) + self.shiftQCD # for systematics
        scaleup         = 2.0 if "emu" in self.channel else OSSS_ratio
        scaleup         = 1.0 if "q_1*q_2>0" in cuts0.replace(' ','') else scaleup
        scaleup         = kwargs.get('scaleup',scaleup)
        LOG.verbose("   QCD: scaleup = %s, shift = %s, self.shiftQCD = %s" % (scaleup,shift,self.shiftQCD),verbosity,level=2)
        
        # CUTS: invert charge
        cuts            = invertCharge(cuts0)
        
        # CUTS: relax cuts for QCD_SS_SB
        # https://indico.cern.ch/event/566854/contributions/2367198/attachments/1368758/2074844/QCDStudy_20161109_HTTMeeting.pdf
        QCD_OS_SR = 0
        #if relax:
        #    
        #    # GET yield QCD_OS_SR = SF * QCD_SS_SR
        #    if 'emu' in self.channel: # use weight instead of scaleup
        #        scaleup     = 1.0
        #        weight      = combineWeights("getQCDWeight(pt_2, pt_1, dR_ll)",weight)
        #        weight_data = "getQCDWeight(pt_2, pt_1, dR_ll)" # SF ~ 2.4 average
        #    kwargs_SR       = kwargs.copy()
        #    kwargs_SR.update({ 'scaleup':scaleup, 'weight':weight, 'weight_data':weight_data, 'relax':False })
        #    histQCD_OS_SR   = self.QCD(**kwargs_SR)
        #    QCD_OS_SR       = histQCD_OS_SR.Integral(1,N+1) # yield
        #    scaleup         = 1.0
        #    gDirectory.Delete(histQCD_OS_SR.GetName())
        #    if QCD_OS_SR < 1: LOG.warning("QCD: QCD_SR = %.1f < 1"%QCD_OS_SR)
        #    
        #    # RELAX cuts for QCD_OS_SB = SF * QCD_SS_SB
        #    append      = "_isorel" + append
        #    iso_relaxed = "iso_1>0.15 && iso_1<0.5 && iso_2==1" #iso_2_medium
        #    if 'emu' in self.channel: iso_relaxed = "iso_1>0.20 && iso_1<0.5 && iso_2<0.5"
        #    else: cuts = relaxJetSelection(cuts)
        #    cuts = invertIsolation(cuts,to=iso_relaxed)
        #    
        #    # # CHECK for 30 GeV jets
        #    # if "bpt_" in var and "btag" in cuts0 and "btag" not in cuts:
        #    #   btags_g  = re.findall(r"&*\ *nc?btag\ *>\ *(\d+)\ *",cuts0)
        #    #   btags_ge = re.findall(r"&*\ *nc?btag\ *>=\ *(\d+)\ *",cuts0)
        #    #   btags_e  = re.findall(r"&*\ *nc?btag\ *==\ *(\d+)\ *",cuts0)
        #    #   nbtags = 0
        #    #   if   btags_g:  nbtags = int(btags_g[0])+1
        #    #   elif btags_ge: nbtags = int(btags_ge[0])
        #    #   elif btags_e:  nbtags = int(btags_e[0])
        #    #   if nbtags>0:
        #    #     if "bpt_1" in var and nbtags>0:
        #    #       cuts+=" && bpt_1>30"
        #    #       LOG.warning("QCD: %s - added 30 GeV cut on b jets in \"%s\""%(var,cuts))
        #    #     if "bpt_2" in var and nbtags>1:
        #    #       cuts+=" && bpt_2>30"
        #    #       LOG.warning("QCD: %s - added 30 GeV cut on b jets in \"%s\""%(var,cuts))
        
        LOG.verbose("   QCD - cuts = %s %s" % (cuts,"(relaxed)" if relax else ""),verbosity,level=2)
        
        # HISTOGRAMS
        histD  = None
        histWJ = None
        histsD_SS, histsB_SS, histsS_SS = self.createHistograms(var,N,a,b,cuts,signal=False,QCD=False,task="calculating QCD",append=append,split=False)
        
        # GET WJ
        if doRatio_WJ_QCD:
          for hist in histsB_SS:
            if ("WJ" in hist.GetName() or re.findall(r"w.*jets",hist.GetName(),re.IGNORECASE)):
              if histWJ:
                LOG.warning("SampleSet::QCD - more than one W+jets sample in SS region, going with first instance!", pre="  ")
                break
              else: histWJ = hist
          if not histWJ:
            LOG.warning("SampleSet::QCD - Did not find W+jets sample!", pre="  ")
        
        # CHECK data
        if not histsD_SS:
            LOG.warning("No data to make DATA driven QCD!")
            return None
        histD_SS = histsD_SS[0]
        
        # STACK
        stack_SS = THStack("stack_SS","stack_SS")
        for hist in histsB_SS: stack_SS.Add(hist)
        histQCD = substractStackFromHist(stack_SS,histD_SS,name=name+append,title="QCD multijet")
        if not histQCD: LOG.warning("Could not make QCD! QCD histogram is none!", pre="  ")
        
        # YIELD only
        if relax:
            QCD_SS = histQCD.Integral(1,N+1)
            if QCD_SS:
                scaleup = QCD_OS_SR/QCD_SS # normalizing to OS_SR
                LOG.verbose("   QCD - scaleup = QCD_OS_SR/QCD_SS_SB = %.1f/%.1f = %.3f" % (QCD_OS_SR,QCD_SS,scaleup),verbosity,level=2)
            else:
                LOG.warning("SampleSet::QCD - QCD_SS_SB.Integral() == 0!")
        scale   = scaleup*(1.0+shift) # scale up QCD 6% in OS region by default
        histQCD.Scale(scale)
        histQCD.SetFillColor(getColor('QCD'))
        MC_SS   = stack_SS.GetStack().Last().Integral()
        data_SS = histD_SS.Integral()
        QCD_SS  = histQCD.Integral()
        
        # WJ/QCD ratio in SS
        if doRatio_WJ_QCD and histWJ:
            WJ_SS  = histWJ.Integral()
            if QCD_SS: ratio_WJ_QCD.value = WJ_SS/QCD_SS
            else: LOG.warning("SampleSet::QCD - QCD integral is 0!", pre="  ")
            LOG.verbose("   QCD - data_SS = %.1f, MC_SS = %.1f, QCD_SS = %.1f, scale=%.3f, WJ_SS = %.1f, ratio_WJ_QCD_SS = %.3f"%(data_SS,MC_SS,QCD_SS,scale,WJ_SS,ratio_WJ_QCD.value),verbosity,level=2)
        else:
            LOG.verbose("   QCD - data_SS = %.1f, MC_SS = %.1f, QCD_SS = %.1f, scale=%.3f"%(data_SS,MC_SS,QCD_SS,scale),verbosity,level=2)
        
        close(histsS_SS+histsB_SS+histsD_SS)
        return histQCD
        
    
    def renormalizeWJ(self,*args,**kwargs):
        """Renormalize WJ by requireing that MC and data has the same number of events in
           the mt_1 > 80 GeV sideband.
           This method assume that the variable of this Plot object is a transverse mass and is plotted
           from 80 GeV to at least 100 GeV."""
        
        verbosity           = getVerbosity(kwargs,verbositySampleTools)
        samples             = self.samples
        var, nBins, xmin, xmax, cuts  = unwrapVariableSelection(*args)
        
        LOG.verbose("%srenormalizing WJ with mt > 80 GeV sideband for variable %s"%(kwargs.get('pre',"  "),var),True)
        
        # CHECK mt
        if not re.search(r"m_?t",var,re.IGNORECASE):
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: variable %s is not a transverse mass variable!"%(var), pre="  ")
            return
        
        # CHECK a, b (assume histogram range goes from 80 to >100 GeV)
        LOG.verbose("  nBins=%s, (a,b)=(%s,%s)"%(nBins,xmin,xmax), verbosity, level=2)
        LOG.verbose('  cuts = "%s"'%(cuts), verbosity, level=1)
        if xmin is not 80:
            LOG.warning("SampleSet::renormalizeWJ - Renormalizing WJ with %s > %s GeV, instead of mt > 80 GeV!" % (var,xmin), pre="  ")
        if xmax < 150:
            LOG.warning("SampleSet::renormalizeWJ - Renormalizing WJ with %s < %s GeV < 150 GeV!" % (var,xmax), pre="  ")
            return
        
        R       = c_double() # ratio_WJ_QCD_SS
        WJ      = None
        histD   = None
        histWJ  = None
        histsWJ = [ ]
        stack   = THStack("stack_QCD","stack_QCD")
        histsD, histsB, histsS = self.createHistograms(var,nBins,xmin,xmax,cuts,reset=True,signal=False,QCD=True,ratio_WJ_QCD_SS=R,split=False)
        
        # CHECK MC and DATA
        if not histsB:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: no MC!", pre="  ")
            return
        if not histsD:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: no data!", pre="  ")
            return
        histD  = histsD[0]
        
        # STACK
        QCD     = False
        e_QCD   = Double()
        I_QCD   = 0
        R       = R.value
        histsWJ = [ ]
        LOG.verbose(" ",verbosity,level=2)
        for hist in histsB:
            if hist.Integral(1,nBins)<=0:
                LOG.warning("SampleSet::renormalizeWJ - Ignored %s with an integral of %s <= 0 !" % (hist.GetName(),hist.Integral()), pre="  ")
            if "WJ" in hist.GetName() or re.findall(r"w.jets",hist.GetName(),re.IGNORECASE):
                histsWJ.append(hist)
            if "qcd" in hist.GetName().lower():
                QCD   = True
                I_QCD = hist.IntegralAndError(1,nBins,e_QCD)
            LOG.verbose("   adding to stack %s (%.1f events)" % (hist.GetName(),hist.Integral()),verbosity,level=2)
            stack.Add(hist)
        
        # CHECK WJ hist
        if len(histsWJ) > 1:
            namesWJ = ', '.join([h.GetName() for h in histsWJ])
            LOG.warning("SampleSet::renormalizeWJ - More than one WJ sample (%s), renormalizing with first instance (%s)!"%(namesWJ,histsWJ[0].GetName()), pre="  ")
        elif len(histsWJ) < 1:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: no WJ sample!", pre="  ")
            return 0.
        histWJ  = histsWJ[0]
        
        # GET WJ sample
        WJ      = self.get("WJ",unique=True)
        if not WJ:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: no WJ sample!", pre="  ")
            return 0.
        
        # INTEGRATE
        e_MC    = Double()
        e_D     = Double()
        e_WJ    = Double()
        I_MC    = stack.GetStack().Last().IntegralAndError(1,nBins,e_MC)
        I_D     = histD.IntegralAndError(1,nBins,e_D)
        I_WJ    = histWJ.IntegralAndError(1,nBins,e_WJ)
        purity0 = 100.0*I_WJ/I_MC
        close(histsD+histsB+histsS)
        if I_MC < 10:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: integral of MC is %s < 10!" % I_MC, pre="  ")
            return 0.
        print ">>>   data: %.1f, MC: %.1f, WJ: %.1f, QCD: %.1f, R: %.3f, WJ prior purity: %.2f%%)" % (I_D,I_MC,I_WJ,I_QCD,R,purity0)
        if I_D < 10:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: integral of data is %s < 10!" % I_D, pre="  ")
            return 0.
        if I_WJ < 10:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: integral of WJ is %s < 10!" % I_WJ, pre="  ")
            return 0.
        
        # SET WJ SCALE
        e_MC_noWJ = sqrt(e_MC**2 - e_WJ**2)
        I_MC_noWJ = I_MC - I_WJ
        scale = ( I_D - I_MC + I_WJ - R*I_QCD ) / (I_WJ - R*I_QCD)
        err_scale = scale * sqrt( (e_D**2+e_MC_noWJ**2+e_QCD**2)/abs(I_D-I_MC_noWJ-R*I_QCD)**2 + (e_WJ**2+e_QCD**2)/(I_WJ-R*I_QCD)**2 )
        
        if scale < 0:
            LOG.warning("SampleSet::renormalizeWJ - Could not renormalize WJ: scale = %.2f < 0!" % scale, pre="  ")
            return scale
        WJ.resetScale(scale)
        print ">>>   WJ renormalization scale = %.3f (new total scale = %.3f)" % (scale, WJ.scale)
        return scale
        
    
    def renormalizeTT(self,**kwargs):
        """Renormalize TT by requireing that MC and data has the same number of events in some control region.
           ..."""
        
    def measureOSSSratio(self,**kwargs):
        """Measure OS/SS ratio by substract non-QCD MC from data with opposite sign (OS) and same sign (SS)
           requirements of a lepton pair."""
        
    def significanceScan(self,*args,**kwargs):
        """Scan cut on a range of some variable, integrating the signal and background histograms,
           calculating the S/(1+sqrt(B)) and finally drawing a histogram with these values."""
    
    def measureSFFromVar(self,var,nBins,a,b,**kwargs):
        """Method to create a SF for a given var, s.t. the data and MC agree."""
        
    def get(self,*searchterms,**kwargs):
        return getSample(self.samples,*searchterms,**kwargs)
    
    def getSignal(self,*searchterms,**kwargs):
        return getSignal(self.samplesS,*searchterms,**kwargs)
        
    def getBackground(self,*searchterms,**kwargs):
        return getBackground(self.samplesB,*searchterms,**kwargs)
        
    def getMC(self,*searchterms,**kwargs):
        return getMC(self.samplesMC,*searchterms,**kwargs)
        
    def getData(self,*searchterms,**kwargs):
        return getData(self.samplesD,*searchterms,**kwargs)
        
    def merge(self,*searchterms,**kwargs):
        self.samplesMC = merge(self.samplesMC,*searchterms,**kwargs)
        
    def stitch(self,*searchterms,**kwargs):
        self.samplesMC = stitch(self.samplesMC,*searchterms,**kwargs)
        
    def replaceMergedSamples(self,mergedsample):
        """Help function to replace merged samples with their MergedSample object in the same position."""
        index0 = len(self.samples)
        for sample in mergedsample:
            index = self.samples.index(sample)
            if index<index0: index0 = index
            self.samples.remove(sample)
        self.samples.insert(index0,mergedsample)
    
    def splitSample(self,*args,**kwargs):
        """Split sample for some dictionairy of cuts."""
        searchterms      = [ arg for arg in args if isinstance(arg,str)  ]
        split_dict       = [ arg for arg in args if isinstance(arg,dict) ][0]
        kwargs['unique'] = True
        sample           = self.get(*searchterms,**kwargs)
        if sample:
          sample.split(split_dict,**kwargs)
        else:
          LOG.warning('SampleSet::splitSample - Could not find sample with searchterms "%s"'%('", "').join(searchterms))
          
    def shiftSample(self,searchterms,file_app,title_app,**kwargs):
        """Shift samples in samples set by creating new samples with new filename/titlename/weight."""
        filter          = kwargs.get('filter',      False       )
        if not (isinstance(searchterms,list) or isinstance(searchterms,tuple)): searchterms = [ searchterms ]
        samplesD        = { }
        samplesB        = [ ]
        samplesS        = [ ]
        for sample in self.samplesB:
          if sample.isPartOf(*searchterms,exclusive=False):
            newsample = sample.clone(samename=True,deep=True)
            newsample.appendFileName(file_app)
            newsample.title = newsample.title+title_app
            samplesB.append(newsample)
          elif not filter:
            newsample = sample.clone(samename=True,deep=True)
            samplesB.append(newsample)
        for sample in self.samplesS:
          if sample.isPartOf(*searchterms,exclusive=False):
            newsample = sample.clone(samename=True,deep=True)
            newsample.appendFileName(file_app)
            newsample.title = newsample.title+title_app
            samplesS.append(newsample)
          elif not filter:
            newsample = sample.clone(samename=True,deep=True)
            samplesS.append(newsample)
        if not filter:
            samplesD = self.samplesD
        
        return SampleSet(samplesD,samplesB,samplesS,**kwargs)
        


    #############
    # getSample #
    #############

def getSample(samples,*searchterms,**kwargs):
    """Help function to get all samples corresponding to some name and optional label."""
    verbosity   = getVerbosity(kwargs,verbositySampleTools)
    filename    = kwargs.get(    'filename',        ""          )
    unique      = kwargs.get(    'unique',          False       )
    matches     = [ ]
    for sample in samples:
        if sample.isPartOf(*searchterms) and filename in sample.filename:
            matches.append(sample)
    if not matches:
        LOG.warning("getSample - Could not find a sample with search terms %s..." % (', '.join(labels+(filename,))))
    elif unique:
        if len(matches)>1: LOG.warning("getSample - Found more than one match to %s. Using first match only: %s" % (", ".join(searchterms),", ".join([s.name for s in matches])))
        return matches[0]
    return matches

def getData(samples,**kwargs):
    return getSampleWithAttribute(samples,'isData',**kwargs)

def getBackground(samples,**kwargs):
    """Help function to get background from a list of samples."""
    return getSampleWithAttribute(samples,'isBackground',**kwargs)

def getSignal(samples,**kwargs):
    """Help function to get signal from a list of samples."""
    return getSampleWithAttribute(samples,'isSignal',**kwargs)

def getSampleWithAttribute(samples,attribute,**kwargs):
    """Help function to get sample with some attribute from a list of samples."""
    matches = [ ]
    unique  = kwargs.get('unique',False)
    for sample in samples:
        if hasattr(sample,attribute): matches.append(sample)
    if not matches:
        LOG.warning("Could not find a signal sample...")
    elif unique:
        if len(matches)>1: LOG.warning("Found more than one signal sample. Using first match only: %s" % (", ".join([s.name for s in matches])))
        return matches[0]
    return matches

def getHist(hists,*searchterms,**kwargs):
    """Help function to get all histograms corresponding to some name and optional searchterm."""
    matches     = [ ]
    unique      = kwargs.get('unique',      False   )
    for hist in hists:
        yes = True
        for searchterm in searchterms:
            yes = yes and (searchterm in hist.GetName()) #or hist.GetTitle()
        if yes: matches.append(hist)
    if not matches:
        LOG.warning("Could not find a sample with search terms %s..." % (', '.join(searchterms)))
    elif unique:
        if len(matches)>1: LOG.warning("Found more than one match to %s. Using first match only: %s" % (", ".join(searchterms),", ".join([h.name for h in matches])))
        return matches[0]
    return matches
    




    ###########
    # Merging #
    ###########

def merge(sampleList,*searchterms,**kwargs):
    """Merge samples from a sample list, that match a set of search terms."""
    
    verbosity = getVerbosity(kwargs,verbositySampleTools,1)
    name0     = kwargs.get('name',  searchterms[0]  )
    title0    = kwargs.get('title', name0           )
    LOG.verbose("",verbosity,level=2)
    LOG.verbose(" merging %s"%(name0),verbosity,level=1)
    
    # GET samples containing names and searchterm
    mergeList = [ s for s in sampleList if s.isPartOf(*searchterms,exclusive=False) ]
    if len(mergeList) < 2:
        LOG.warning('Could not merge "%s": less than two "%s" samples'%(name0,name0))
    fill = max([ len(s.name) for s in mergeList ])+2 # number of spaces
    
    # ADD samples with name0 and searchterm
    mergedsample = MergedSample(name0,title0)
    for sample in mergeList:
        samplename = ("\"%s\""%(sample.name)).ljust(fill)
        LOG.verbose("   merging %s to %s: %s"%(samplename,name0,sample.filenameshort),verbosity,level=2)
        mergedsample.add(sample)
    
    # REMOVE replace merged samples from sampleList, preserving the order
    if mergedsample.samples and sampleList:
      if isinstance(sampleList,SampleSet):
        sampleList.replaceMergedSamples(mergedsample)
      else:
        index0 = len(sampleList)
        for sample in mergedsample.samples:
            index = sampleList.index(sample)
            if index<index0: index0 = index
            sampleList.remove(sample)
        sampleList.insert(index,mergedsample)
    return sampleList
    



    #############
    # Stitching #
    #############

def stitch(sampleList,*searchterms,**kwargs):
    """Stitching samples: merge samples and reweight inclusive sample and rescale jet-binned
    samples."""
    
    verbosity         = getVerbosity(kwargs,verbositySampleTools,1)
    name0             = kwargs.get('name',      searchterms[0]  )
    title0            = kwargs.get('title',     name0           )
    name_incl         = kwargs.get('name_incl', name0           )
    LOG.verbose("",verbosity,level=2)
    LOG.verbose(" stiching %s: rescale, reweight and merge samples" % (name0),verbosity,level=1)
    
    N_incl            = 0
    weights           = [ ]
    sigmaLO, sigmaNLO = crossSections(name0,*searchterms)
    kfactor           = sigmaNLO / sigmaLO
    LOG.verbose("   %s k-factor = %.2f" % (name0, kfactor),verbosity,level=2)
    
    # CHECK if sample list of contains to-be-stitched-sample
    stitchList = sampleList.samples if isinstance(sampleList,SampleSet) else sampleList
    stitchList = [ s for s in stitchList if s.isPartOf(*searchterms) ]
    if len(stitchList) < 2:
        LOG.warning("Could not stitch %s: less than two %s samples (%d)" % (name0,name0,len(stitchList)))
        for s in stitchList: print ">>>   %s" % s.name
        if len(stitchList)==0: return sampleList
    fill       = max([ len(s.name) for s in stitchList ])+2
    name       = kwargs.get('name',stitchList[0].name)
    
    # SET renormalization scales with effective luminosity
    # assume first sample in the list s the inclusive sample
    for sample in stitchList:
        
        N_tot = sample.N
        N_eff = N_tot
        sigma = sample.sigma # inclusive or jet-binned cross section
        
        if sample.isPartOf(name_incl):
            N_incl = N_tot
        elif not N_incl:
            LOG.warning("Could not stitch %s: N_incl == 0!" % name0)
        else:
            N_eff = N_tot + N_incl*sigma/sigmaLO # effective luminosity
        
        norm = luminosity * kfactor * sigma * 1000 / N_eff
        weights.append("(NUP==%i ? %s : 1)" % (len(weights),norm))
        LOG.verbose("   stitching %s with normalization %7.3f and cross section %8.2f pb" % (sample.name.ljust(fill), norm, sigma),verbosity,level=2)
        #print ">>> weight.append(%s)" % weights[-1]
        
        sample.norm = norm # apply lumi-cross section normalization
        if len(stitchList)==1: return sampleList
    
    # SET weight of inclusive sample
    for sample in stitchList:
      if sample.isPartOf(name_incl):
        sample.norm = 1.0 # apply lumi-cross section normalization via weights
        sample.addWeight('*'.join(weights))
        title0 = sample.title
    
    # MERGE
    merge(sampleList,name0,*searchterms,title=title0,verbosity=verbosity)
    return sampleList


def crossSections(*searchterms,**kwargs):
    """Returns inclusive LO and NLO cross section for stitching og DY and WJ."""
    # see /shome/ytakahas/work/TauTau/SFrameAnalysis/TauTauResonances/plot/config.py
    # DY cross sections  5765.4 [  4954.0, 1012.5,  332.8, 101.8,  54.8 ]
    # WJ cross sections 61526.7 [ 50380.0, 9644.5, 3144.5, 954.8, 485.6 ]
    
    isDY          = False
    isDY_M10to50  = ""
    isDY_M50      = ""
    isWJ          = False
    
    sigmas        = { 'DY': { 'M-50':     ( 4954.0, 5765.4),
                              'M-10to50': (18610.0,21658.0) },
                      'WJ':               (50380.0,61526.7) }
    
    for searchterm in searchterms:
        searchterm = searchterm.replace('*','')
        if "DY" in searchterm:
            isDY = True
        if "10to50" in searchterm:
            isDY_M10to50 = "M-10to50"
        if "50" in searchterm and not "10" in searchterm:
            isDY_M50 = "M-50"
        if "WJ" in searchterm:
            isWJ = True
    
    if isDY and isWJ:
        LOG.error("crossSections - Detected both isDY and isWJ!")
        exit(1)
    elif isWJ:
        return sigmas['WJ']
    elif isDY:
        if isDY_M10to50 and isDY_M50:
            LOG.error("crossSections - Matched to both \"M-10to50\" and \"M-50\"!")
            exit(1)
        if not (isDY_M10to50 or isDY_M50):
            LOG.error("crossSections - Did not match to either \"M-10to50\" or \"M-50\" for DY!")
            exit(1)
        return sigmas['DY'][isDY_M10to50+isDY_M50]
    else:
        LOG.error("crossSections - Did not find a DY or WJ match!")
        exit(1)


import PlotTools
from PlotTools      import *
from SettingTools   import *
from SelectionTools import *
from VariableTools  import *
from PrintTools     import *
