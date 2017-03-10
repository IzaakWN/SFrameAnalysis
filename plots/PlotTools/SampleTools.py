from ROOT import TFile, TH1F, TH2F, gDirectory, kAzure
import PlotTools
from PlotTools  import Plot, makeHistName, combineCuts, combineWeights
from PrintTools import color, warning, error, printVerbose, printSameLine, LoadingBar
from math import sqrt, pow

# set in plot.py
lumi = 12.9
SAMPLE_DIR = ""
mylabel = ""
isocuts     = "iso_1 < 0.15 && iso_2 == 1"
vetos       = "dilepton_veto == 0 && extraelec_veto == 0 && extramuon_veto == 0 && " +\
                       "againstElectronVLooseMVA6_2 == 1 && againstMuonTight3_2 == 1"
baseline    = "%s && %s && q_1*q_2<0" % (isocuts, vetos)
category1   = "ncbtag > 0 && ncjets == 1 && nfjets  > 0"
category2   = "ncbtag > 0 && ncjets == 2 && nfjets == 0 && dphi_ll_bj > 2 && met < 60"
blindlimits = { }
blindcuts   = { }





    ###############
    # makeSamples #
    ###############

def makeSamples(**kwargs):
    """Calculate and set the normalization scales. Then save and list the samples with their respective cross section."""
    verbosity = kwargs.get('verbosity',2)
    
    print ">>> samples with integrated luminosity L = %s / fb at sqrt(s) = 13 TeV" % lumi
    print ">>> "
    print ">>> %12s  %12s  %26s  %18s  %12s" % ("events", "sum weights", "sample".ljust(22), "cross section (pb)", "norm. scale" )
    weight       = "weight" #(gen_match_2==5 ? 1.056 : 1.) #puweight*genweight*trigweight_1*idweight_1*isoweight_1
    weight_      = kwargs.get('weight',weight)
    treeName     = kwargs.get('treeName',"tree_mutau")
    samplesB     = kwargs.get('samplesB',[ ])
    samplesS     = kwargs.get('samplesS',[ ])
    samplesD     = kwargs.get('samplesD',{ })
    signal_scale = kwargs.get('signal_scale',1)
    
    # BACKGROUND
    for i, sampledata in enumerate(samplesB):
        if len(sampledata) is 4: sampledata += (weight_,)
        (subdir, sampleName, name, sigma, weight) = sampledata
        filename        = SAMPLE_DIR + subdir + "TauTauAnalysis.%s%s.root" % (sampleName,mylabel)
        file            = TFile( filename )
        N_tot           = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(8)
        N_tot_unweighted = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
        scale           = lumi * sigma * 1000 / N_tot
        #if "DYJetsToLL_M-10to50_nlo" in sample: weightB = "%s*%s" % (weightB,"(NUP==1 ? 0 : 1)*(NUP==2 ? 0 : 1)")
        sample = Sample( filename, name, sigma=sigma, N=N_tot, scale=scale, background=True, cuts="channel>0", weight=weight, treeName=treeName )
        samplesB[i]     = sample
        print ">>> %12i  %12i  %26s  %18.2f  %12.2f" % (N_tot,N_tot_unweighted,name.ljust(24),sigma,scale)    
        
        
    # SIGNAL
    for i, sampledata in enumerate(samplesS):
        if len(sampledata) is 4: sampledata += (weight_,)
        (subdir, sampleName, name, S_exp, weight) = sampledata
        filename        = SAMPLE_DIR + subdir + "TauTauAnalysis.%s%s.root" % (sampleName,mylabel)
        file            = TFile( filename )
        N_tot           = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(8)
        N_tot_unweighted = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
        sample = Sample( filename, name, sigma=0, N=N_tot, signal=True, cuts="channel>0", weight=weight, treeName=treeName )
        scale           = 1 #sample.normalizeSignal(S_exp) * signal_scale #N_exp / N_tot
        samplesS[i]     = sample
        print ">>> %12i  %12i  %26s  %18.2f  %12.2f" % (N_tot,N_tot_unweighted,name.ljust(24),0,scale)
        
        
    # DATA
    for channel, s in samplesD.items():
        (subdir, sampleName, name) = s
        filename        = SAMPLE_DIR + subdir + "TauTauAnalysis.%s%s.root" % (sampleName,mylabel)
        file            = TFile( filename )
        N_tot           = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(8)
        N_tot_unweighted = file.Get("histogram_mutau/cutflow_mutau").GetBinContent(1)
        sample = Sample( filename, name, data=True, cuts ="channel>0", treeName=treeName, blind=blindcuts )
        samplesD[channel] = [sample]
        print ">>> %12i  %12i  %26s  %21s" % ( N_tot, N_tot_unweighted, name.ljust(24), "L = %5.2f/fb" % lumi )
    
    
    # BACKGROUND MERGE
    mergeST  = False; mergeVV    = False
    stitchWJ = False; stitchDY50 = False; stitchDY10to50 = False
    for sample in samplesB:
        if   sample.isPartOf("ST"): mergeST  = True and kwargs.get('mergeST', True)
        elif sample.isPartOf("WW"): mergeVV  = True and kwargs.get('mergeVV', True)
        elif sample.isPartOf("DY","M-50"):  stitchDY50     = True and kwargs.get('stitchDY50',True)
        elif sample.isPartOf("DY","10-50"): stitchDY10to50 = True and kwargs.get('stitchDY10to50',True)
        elif sample.isPartOf("WJ"): stitchWJ = True and kwargs.get('stitchWJ',True)
    if mergeST:         mergeSamples(samplesB,"ST",verbosity=verbosity)
    if mergeVV:         mergeSamples(samplesB,["WW","WZ","ZZ"],name="diboson",verbosity=verbosity)
    if stitchWJ:        stitchSamples(samplesB,"WJ",name_incl="WJets",verbosity=verbosity)
    if stitchDY10to50:  stitchSamples(samplesB,"DY",label="M-10to50",verbosity=verbosity) # ,name="Drell-Yan 10-50"
    labels_DY50 = kwargs.get('labels_DY50')
    if labels_DY50:
        for label_DY in labels_DY50:
                        stitchSamples(samplesB,"DY",labels=["M-50",label_DY],verbosity=verbosity)
    elif stitchDY50:    stitchSamples(samplesB,"DY",label="M-50",verbosity=verbosity)
    print ">>> "
    




    #################
    # normalization #
    #################
    

def renormalizeWJ(samples,**kwargs):
    """Helpfunction to renormalize W + Jets."""
    #print ">>>\n>>> renormalizing WJ"
    var         = kwargs.get('var',"pfmt_1")
    QCD         = kwargs.get('QCD',True)
    channel     = kwargs.get('channel',"mutau")
    label       = kwargs.get('label',"baseline")
    cuts        = kwargs.get('cuts',baseline)
    reset       = kwargs.get('reset',True)
    shift_QCD   = kwargs.get('shift_QCD',0) # e.g. 0.30
    prepend     = kwargs.get('prepend',"")
    verbosity   = kwargs.get('verbosity',0)
    ratio_WJ_QCD_SS = True
    #samples = kwargs.get('samples',[ ])
    name        = "%s/%s%s/%s_%s_noWJrenormalizatton.png" % (PLOTS_DIR,channel,mylabel,var,label)
    title       = "%s: %s" % (channel.replace("tau","#tau").replace("mu","#mu"),label)
    plot = Plot( samples, var, 200, 80, 200, cuts=cuts, QCD=QCD, ratio_WJ_QCD_SS=ratio_WJ_QCD_SS, reset=True, shift_QCD=shift_QCD, verbosity=verbosity )
    #plot.plot(stack=True, title=title, staterror=True, ratio=True)
    plot.renormalizeWJ(prepend=prepend, verbosity=verbosity)
    plot.close()
    

def renormalizeTT(samples,**kwargs):
    """Helpfunction to renormalize TT."""
    #print ">>>\n>>> renormalizing WJ"
    var         = kwargs.get('var',"pfmt_1")
    QCD         = kwargs.get('QCD',True)
    channel     = kwargs.get('channel',"mutau")
    label       = kwargs.get('label',"baseline")
    cuts        = kwargs.get('cuts',baseline)
    reset       = kwargs.get('reset',True)
    shift_QCD   = kwargs.get('shift_QCD',0) # e.g. 0.30
    prepend     = kwargs.get('prepend',"")
    verbosity   = kwargs.get('verbosity',0)
    ratio_TT_QCD_SS = True
    #samples = kwargs.get('samples',[ ])
    if "category 1" in category:   cuts = combine(cuts,category1TT)
    elif "category 2" in category: cuts = combine(cuts,category1TT)
    else: print warning("Could not normalize TT: no category 1 or 2 selections")
    name        = "%s/%s%s/%s_%s_noTTrenormalizatton.png" % (PLOTS_DIR,channel,mylabel,var,label)
    title       = "%s: %s" % (channel.replace("tau","#tau").replace("mu","#mu"),label)
    plot = Plot( samples, var, 200, 0, 200, cuts=cuts, QCD=QCD, ratio_TT_QCD_SS=ratio_TT_QCD_SS, reset=True, shift_QCD=shift_QCD, verbosity=verbosity )
    #plot.plot(stack=True, title=title, staterror=True, ratio=True)
    plot.renormalizeTT(prepend=prepend, verbosity=verbosity)
    plot.close()
        




    #############
    # getSample #
    #############

def getSample(samples,*labels,**kwargs):
    """Method to get all samples corresponding to some name and optional label."""
    matches = [ ]
    filename = kwargs.get('filename',"")
    unique = kwargs.get('unique',False)
    for sample in samples:
        if sample.isPartOf(*labels) and filename in sample.filename:
            matches.append(sample)
    if not matches:
        print warning("Could not find a sample with search terms %s..." % (', '.join(labels+(filename,))))
    elif unique:
        if len(matches)>1: print warning("Found more than one match to %s. Using first match only: %s" % (", ".join(labels),", ".join([s.label for s in matches])))
        return matches[0]
        
    return matches
    




def removeLowMassDY(samples, **kwargs):
    """Remove low mass DY."""
    for sample in samples:
        if ("Drell-Yan" in sample.label or "DY" in sample.label ) and "10-50" in sample.label:
            samples.remove(sample)
            if kAzure+5 in PlotTools.fillcolors: PlotTools.fillcolors.remove(kAzure+5)
            print warning("Removed Drell Yan low mass and kAzure+5.")
    




    ###########
    # Merging #
    ###########

def mergeSamples(sample_list,names,**kwargs):
    """Merge samples"""
    verbosity = kwargs.get('verbosity',2)
    
    if not isinstance(names,list): names = [names]
    name0       = kwargs.get('name',names[0]) #+ " merged"
    signal      = kwargs.get('signal',False)
    background  = kwargs.get('background',True) and not signal
    labels      = kwargs.get('labels',[]) # extra search term
    labels.append(kwargs.get('label',""))
    samples     = Samples(name0, background=background, signal=signal)
    printVerbose(">>>",verbosity,level=2)
    printVerbose(">>> merging %s" % (name0),verbosity,level=1)
    
    # get samples containing names and label
    merge_list = [ ]
    for name in names:
        merge_list += [ s for s in sample_list if s.isPartOf(name,*labels) ]
    
    # check if sample list of contains to-be-stitched-sample
    if len(merge_list) < 2:
        print warning("Could not stitch %s: less than two %s samples" % (name0,name0))
        return sample_list
    fill = max([ len(s.label) for s in merge_list ])
    
    # add samples with name0 and label
    for sample in merge_list:
        printVerbose(">>>   merging %s to %s: %s" % (sample.label.ljust(fill),name0,sample.filenameshort),verbosity,level=2)
        samples.add(sample)
    
    # remove merged samples from sample_list
    if samples.samples:
        sample_list.append(samples)
        for sample in samples.samples: sample_list.remove(sample)





    #############
    # Stitching #
    #############

def stitchSamples(sample_list,name0,**kwargs):
    """Stitching samples: merge samples
       and reweight inclusive sample and rescale jet-binned samples"""
    verbosity = kwargs.get('verbosity',2)
    printVerbose(">>>",verbosity,level=2)
    printVerbose(">>> stiching %s: rescale, reweight and merge samples" % (name0),verbosity,level=1)
    # see /shome/ytakahas/work/TauTau/SFrameAnalysis/TauTauResonances/plot/config.py
    # DY cross sections  5765.4 [  4954.0, 1012.5,  332.8, 101.8,  54.8 ]
    # WJ cross sections 61526.7 [ 50380.0, 9644.5, 3144.5, 954.8, 485.6 ]
    
    sigmasLO =  { "DY": { "M-50": 4954.0, "M-10to50": 18610.0 }, "WJ": { "": 50380.0 } }
    sigmasNLO = { "DY": { "M-50": 5765.4, "M-10to50": 18610.0 }, "WJ": { "": 61526.7 } }
    
    #name0       = "DY" #"WJ"
    label_incl  = kwargs.get('label_incl',"Jets")
    name_incl   = kwargs.get('name_incl',name0+label_incl)
    labels      = kwargs.get('labels',[ ]) # extra search term
    labels.append(kwargs.get('label',""))
    sigmaLO     = sigmasLO[name0][labels[0]]
    kfactor     = sigmasNLO[name0][labels[0]] / sigmaLO
    N_incl      = 0
    weights     = [ ]
    stitch_list = [ s for s in sample_list if s.isPartOf(name0,*labels) ]
    printVerbose(">>>   %s k-factor = %.2f" % (name0, kfactor),verbosity,level=2)
    
    # check if sample list of contains to-be-stitched-sample
    if len(stitch_list) < 2:
        print warning("Could not stitch %s: less than two %s samples" % (name0,name0))
        for s in stitch_list: print ">>>   %s" % s.label
        return sample_list
    fill        = max([ len(s.label) for s in stitch_list ])
    name        = kwargs.get('name',stitch_list[0].label)
    
    # set renormalization scales with effective luminosity
    for sample in stitch_list:
        
        N_tot   = sample.N
        sigma   = sample.sigma
        N       = N_tot
        
        if name_incl in sample.filename:
            N_incl = N_tot
        elif not N_incl:
            print warning("Could not stitch %s: N_incl == 0!" % name0)
            return sample_list
        else:
            N = N_tot + N_incl*sigma/sigmaLO # effective luminosity
        
        scale = lumi * kfactor * sigma * 1000 / N
        weights.append("(NUP==%i ? %s : 1)" % (len(weights),scale))
        printVerbose(">>>   stitching %s with scale %5.2f and cross section %7.2f pb" % (sample.label.ljust(fill), scale, sigma),verbosity,level=2)
        #print ">>> weight.append(%s)" % weights[-1]
        
        if name_incl in sample.filename: sample.scale = 1.0   # apply renormalization scale with weights
        else:                            sample.scale = scale # apply renormalization scale
    
    # set weight of inclusive sample
    for sample in stitch_list:
        if sample.isPartOf(name_incl,*labels):
            sample.scale = 1.0
            sample.addWeight("*".join(weights))
    
    # merge
    mergeSamples(sample_list,name0,labels=labels,name=name,verbosity=verbosity)





    ###########
    # Samples #
    ###########

class Samples(object):
    """Class to combine a set of Sample-objects to make one histogram with the Plot class."""

    def __init__(self, label, **kwargs):
        self.samples    = [ ]
        self.label      = label
        self.cuts       = kwargs.get('cuts', "")
        self.weight     = kwargs.get('weight', "")
        self.scale      = kwargs.get('scale', 1.0)
        self.scaleBU    = self.scale # BU scale to overwrite previous renormalizations (WJ)
        self.sigma      = kwargs.get('sigma', 0.0)
        self.isData     = kwargs.get('data', False)
        self.isBackground = kwargs.get('background', False)
        self.isSignal   = kwargs.get('signal', False)
        self.blind      = kwargs.get('blind', { })
        filename = label
        treename = "tree"
        if self.samples:
            filename = self.samples[0].filename
            treename = self.samples[0].treeName
        self.filename   = kwargs.get('filename', filename)
        self._treeName  = kwargs.get('treeName', treename)
        self.filenameshort = "/".join(self.filename.split('/')[-2:])


    @property
    def treeName(self): return self._treeName

    @treeName.setter
    def treeName(self, value):
        for sample in self.samples: sample.treeName = value
        self._treeName = value

    
    def add(self, sample, **kwargs):
        #scale  = kwargs.get('scale', 1.0) * self.scale
        #sample.scale *= scale
        self.samples.append(sample)
    
    
    def hist(self, var, nBins, a, b, **kwargs):
        name    = kwargs.get('name',  makeHistName(self.label+"_merged", var))
        title   = kwargs.get('title', self.label)
        kwargs['scale'] = self.scale * kwargs.get('scale', 1.0) # pass scale down
        
        verbosity = kwargs.get('verbosity', 0)
        printVerbose(">>>\n>>> Samples - %s, %s: %s" % (color(name,color="grey"), var, self.filenameshort),verbosity)
        printVerbose(">>>    scale: %.4f" % (kwargs['scale']),verbosity)
        
        hist = TH1F(name, title, nBins, a, b)
        for sample in self.samples:
            if 'name' in kwargs: # prevent memory leaks
                kwargs['name']  = makeHistName(sample.label,name.replace(self.label+'_',''))    
            hist_new = sample.hist(var, nBins, a, b, **kwargs)
            hist.Add( hist_new )
            printVerbose(">>>    sample %s added with %.1f events" % (sample.label,hist_new.Integral()),verbosity,level=2)
        
        return hist
    
    
    def hist2D(self, var1, nBins1, a1, b1, var2, nBins2, a2, b2, **kwargs):
        name   = kwargs.get('name',  makeHistName(self.label+"_merged", "%s_vs_%s" % (var1,var2)))
        title   = kwargs.get('title', self.label)
        kwargs['scale'] = self.scale * kwargs.get('scale', 1.0) # pass scale down
        
        verbosity = kwargs.get('verbosity', 0)
        printVerbose(">>>\n>>> Samples - %s, %s vs. %s: %s" % (color(name,color="grey"), var1, var2, self.filenameshort),verbosity)
        printVerbose(">>>    scale: %.4f"        % (kwargs['scale']),verbosity)
        
        hist2D = TH2F(name, title, nBins2, a2, b2, nBins1, a1, b1)
        for sample in self.samples:
            if 'name' in kwargs: # prevent memory leaks
                kwargs['name']  = makeHistName(sample.label,name.replace(self.label+'_',''))    
            hist2D.Add( sample.hist2D(var1, nBins1, a1, b1, var2, nBins2, a2, b2, **kwargs) )
        
        return hist2D


    def resetScalesAndWeights(self,**kwargs):
        
        for sample in self.samples:
            sample.resetScalesAndWeights(**kwargs)

    
    def isPartOf(self, *labels):
        """Check if labels are in label or filename."""
        if not labels: return False
        yes = True
        for label in labels:
            yes = yes and (label in self.label or label in self.filenameshort)
        return yes





    ##########
    # Sample #
    ##########

class Sample(object):
    """Class to make histogram with the Plot class."""

    def __init__(self, filename, label, **kwargs):
        self.filename   = filename
        self.filenameshort = "/".join(self.filename.split('/')[-2:])
        self.file       = TFile(filename)
        self.label      = label
        self.cuts       = kwargs.get('cuts', "")
        self.weight     = kwargs.get('weight', "")
        self.scale      = kwargs.get('scale', 1.0)
        self.scaleBU    = self.scale # BU scale to overwrite previous renormalizations (WJ)
        self.sigma      = kwargs.get('sigma', 0.0)
        self.N          = kwargs.get('N', 0)
        self.isData     = kwargs.get('data', False)
        self.isBackground = kwargs.get('background', False)
        self.isSignal   = kwargs.get('signal', False)
        self.treeName   = kwargs.get('treeName', "tree")
        self.blind      = kwargs.get('blind', { })
        # TODO: only blind for m_vis variable!
        # TODO: rewrite class with tree method, applycut method, ...

    @property
    def tree(self): return self.file.Get(self.treeName)

    #@treeName.setter
    #def tree(self, tree): self._tree = tree
        

    
    def hist(self, var, nBins, a, b, **kwargs):
        """Make a histogram with a tree."""
        
        scale   = kwargs.get('scale', 1.0) * self.scale
        tree    = self.file.Get(self.treeName)
        name    = kwargs.get('name',  makeHistName(self.label, var))
        title   = kwargs.get('title', self.label)
        shift   = kwargs.get('shift', 0)
        smear   = kwargs.get('smear', 0)
        verbosity = kwargs.get('verbosity', 0)
        
        if self.isSignal and self.scale is not self.scaleBU and self.scaleBU:
            title += " (#times%d)" % (self.scale/self.scaleBU)
        
        blindcuts = ""
        if var in self.blind: blindcuts = self.blind[var]
        weight = combineWeights(self.weight, kwargs.get('weight', ""))
        cuts   = combineCuts(self.cuts, kwargs.get('cuts', ""), blindcuts, weight=weight)
        
        hist = TH1F(name, title, nBins, a, b)
        out = tree.Draw("%s >> %s" % (var,name), cuts, "gOff")
        
        if shift or smear:
            mean0 = hist.GetMean()
            #smear = min(1,smear)
            #smear = sqrt(smear*smear-1) #*sigma
            #tree.SetAlias("rng","sin(2*pi*rndm)*sqrt(-2*log(rndm))")
            var2 = "%s*%s + %s + %s*%s" % (var,smear,shift,(1-smear),mean0)
            tree.Draw("%s >> %s" % (var2,name), cuts, "gOff")
        if out < 0: print error("Drawing histogram for %s sample failed!" % (title))
        
        if scale is not 1.0: hist.Scale(scale)
        if scale is     0.0: print warning("Scale of %s is 0!" % self.label)
        #print hist.GetEntries()
        #gDirectory.Delete(label)
        
        printVerbose(">>>\n>>> Sample - %s, %s: %s" % (color(name,color="grey"), var, self.filenameshort),verbosity)
        printVerbose(">>>    scale:  %.4f (%.4f)" % (scale,self.scale),verbosity)
        printVerbose(">>>    weight: %s" % (("\n>>>%s*("%(' '*18)).join(weight.rsplit('*(',max(0,weight.count("*(")-1)))),verbosity)
        printVerbose(">>>    %s" % (cuts.replace("*(","\n>>>%s*("%(' '*18))),verbosity)
        return hist
        
        
        
    def hist2D(self, var1, nBins1, a1, b1, var2, nBins2, a2, b2, **kwargs):
        """Make a 2D histogram with a tree."""
        
        scale   = kwargs.get('scale', 1.0) * self.scale
        tree    = self.file.Get(self.treeName)
        name    = kwargs.get('name',  makeHistName(self.label, "%s_vs_%s" % (var1,var2)))
        title   = kwargs.get('title', self.label)
        verbosity = kwargs.get('verbosity', 0)
        
        blindcuts = ""
        if var1 in self.blind: blindcuts += self.blind[var1]
        if var2 in self.blind: blindcuts += self.blind[var2]
        weight = combineWeights(self.weight, kwargs.get('weight', ""))
        cuts   = combineCuts(self.cuts, kwargs.get('cuts', ""), blindcuts, weight=weight)
        printVerbose(">>>>\n>>> Sample - %s, %s vs. %s: %s" % (color(name,color="grey"), var1, var2, self.filenameshort),verbosity)
        printVerbose(">>>    scale:  %.4f"    % (scale),verbosity)
        printVerbose(">>>    weight: %s"      % (weight),verbosity)
        printVerbose(">>>    %s" % (cuts),verbosity)
        
        hist2D = TH2F(name, title, nBins2, a2, b2, nBins1, a1, b1)
        out = tree.Draw("%s:%s >> %s" % (var1,var2,name), cuts, "gOff")
        if out < 0: print error("Drawing histogram for %s sample failed!" % (title))
        
        #if scale is not 1.0: hist.Scale(scale)
        #if scale is     0.0: print warning("Scale of %s is 0!" % self.label)
        return hist2D
    
    
    
    def scale(self, hist, scale, **kwargs):
        """DEPRECATED - Make a scale."""
        
        if len(args):
            scale = args[0]
            if I: hist.Scale(scale)
            else: print ">>> could not scale: I = 0"
        else:
            lumi = kwargs.get('lumi', 0)
            sigma = kwargs.get('sigma', 0)
            efficiency = kwargs.get('efficiency', 1)
            acceptance = kwargs.get('acceptance', 1)
            e = kwargs.get('e', 1)
            A = kwargs.get('A', 1)
            N = kwargs.get('N', 1)
            if lumi and sigma:
                scale = lumi * sigma * efficiency * e * acceptance * A / N
                if I: hist.Scale(scale)
                else: print ">>> could not scale: I = 0"
            
    
    
    def setAllScales(self, scale):
        """Set all scales to given number."""
        #print ">>> setAllScales: scale = %.4f" % scale
        self.scale   = scale
        self.scaleBU = scale
        
    
    def normalizeSignal(self,S_exp,**kwargs):
        """Calculates normalization for a given expected signal yield."""
        
        verbosity   = kwargs.get('verbosity',0)
        cuts        = [ ("%s && %s" % (baseline, category1)),
                        ("%s && %s" % (baseline, category2)), ]
        cuts        = kwargs.get('cuts',cuts)
        weight      = kwargs.get('weight',"")
        (aa,bb)     = kwargs.get('signalregion',(0,40))
        
        N  = 0; MC = 0
        scale = 1
        for i,cut in enumerate(cuts):
            cut     = combineCuts("m_sv>0", cut)
            name    = "m_sv_for_signal_renormalization_%d" % i
            hist    = self.hist("m_sv",100,aa,bb,name=name,cuts=cut,weight=weight)
            N       += hist.GetSumOfWeights()
            MC      += hist.GetEntries()
            gDirectory.Delete(name)
        
        if N:
            scale = S_exp / N * self.scale
            printVerbose(">>> normalizeSignal: S_exp=%.4f, N=%.4f, MC=%.1f, old scale=%.4f, scale=%.4f" % (S_exp, N, MC, self.scale, scale), verbosity)
            printVerbose(">>> normalizeSignal: signalregion=(%.1f,%.1f)" % (aa,bb),verbosity)
        else: print warning("Could not find normalization for signal: no MC events in given signal region after cuts (%s)!" % cuts)
        self.setAllScales(scale)
        
        return scale
        
    
    def calculateLumiAcceptance(self,cuts,**kwargs):
        """Calculates scale for a given expected signal yield, to divide
           out the luminosity and acceptance. This method only returns the scale,
           it does not rescale the signal."""
        verbosity   = kwargs.get('verbosity',0)
        weight      = kwargs.get('weight',"")
        (a,b)       = kwargs.get('range',(0,500))
        scale       = 1
        N_tot       = self.N
        name        = "m_sv_for_LumiAcceptance"
        hist        = self.hist("m_sv",100,a,b,name=name,cuts=cuts,weight=weight)
        (N,MC)      = (hist.GetSumOfWeights(),hist.GetEntries())
        gDirectory.Delete(name)
        if N_tot and N and lumi:
            scale   = N_tot/(N*lumi)
            printVerbose(">>> normalizeSignal: N_tot=%.4f, N=%.4f, MC=%.1f, lumi=%s, current scale=%.4f, scale=%.4f" % (N_tot, N, MC, lumi, self.scale, scale), verbosity)
            printVerbose(">>> normalizeSignal: range=(%.1f,%.1f)" % (a,b),verbosity)
        else: print warning("Could not find normalization for signal: N_tot=%s, N=%s, lumi=%s!" % (N_tot,N,lumi))
        return scale


    def norm(self, hist):
        """Normalize histogram."""
        
        I = hist.Integral()
        if I:
            hist.Scale(1/I)


    def resetScalesAndWeights(self,**kwargs):
        """Reset all scales and weight to unity. Option to normalize."""
        norm    = kwargs.get('norm',True)
        weight  = kwargs.get('weight',"")
        self.scale  = 1
        self.weight = weight
        if norm and self.N:
            self.scale = 1/self.N

    
    def addWeight(self, weight):
        """Combine weight to."""
        self.weight = combineWeights(self.weight, weight)
        #print ">>> addWeight: combine weights %s" % self.weight


    def applyCuts(self, treename, cuts):
        """Make tree with cuts applied."""
        # TODO: implement method that saves new tree with cuts

    
    def isPartOf(self, *labels):
        """Check if labels are in label or filename."""
        
        if not labels: return False
        yes = True
        for label in labels:
            yes = yes and (label in self.label or label in self.filenameshort)
        
        return yes
    
    
    
    
