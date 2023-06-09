# -*- coding: utf-8 -*-
"""
Created on Mon May 22 12:44:59 2023

@author: james.caplinger
"""

import numpy as np
import pandas as pd

pd.options.display.float_format = '{:.2f}'.format
from dataclasses import dataclass, field
from enum import Enum, auto
from .MMweighting import genWFsimple, WA



# Is this really the best way to do this? 

def roundf(vals,decimals=2):
    out = []
    for val in vals:
        if val:
            out.append(np.round(val,decimals=decimals))
        else:
            out.append(val)
    return out
            
def calcSELcont(Lrms: float,T_m: float)->float:
    """Calculates the cumulative sound exposure level given a Sound Pressure Level in dB rel 1 uPa and a duration in minutes"""
    T = T_m*60
    return 10*np.log10(T)+Lrms

def calcSELImpulsive(SELss:float, N:int)->float:
    """Calculates the cumulative sound exposure level given a single-strike SEL and number of strikes"""
    return SELss+10*np.log10(N)

def addSources(Larr: [float])->float:
    """Adds sound levels from list of floats (levels in dB) in linear pressure values and converts back to dB"""
    lin = 0
    for L in Larr:
        lin = lin+10**(L/10)
    return 10*np.log10(lin)




class constructionTypes(Enum):
    vibratory = auto()
    impact = auto()
    DTH = auto()
    
@dataclass
class constructionSource:
    """Generic class for construction source which has methods to accumulate SEL and apply weighting functions"""
    SELss:float = None
    Lpeak:float = None
    Lrms:float = None
    TL:float=None
    measuredRange_m:float = None
    numberOfPiles:int  = None
    strikesPerPile:int = None
    strikeRate_Hz:float= None
    timePerPile_min:float= None
    index: int= None
    measuredRange_m: float= None
    isImpulsive:bool= None
    sourceType: constructionTypes= None
    weightingFrequency_Hz:float= None
    LE_cumulative: float = field(init=False)
    LEw: np.ndarray = field(init=False)
    weightingFunction: genWFsimple=genWFsimple
    
    def accumulateSEL(self)->None:
        """Calculate the cumulative SEL for the entire activity"""
      
    
    def applyWeighting(self)->None:
        """Calculate the cumulative SEL for the entire activity"""
        self.LEw =self.weightingFunction(self.weightingFrequency_Hz).w+self.LE_cumulative
       
    # runs after instantiation to calculated necessary vaules    
    def __post_init__(self):
        self.accumulateSEL()
        self.applyWeighting()
    
    

@dataclass 
class impactSource(constructionSource):
    """Impact specific construction source"""

    isImpulsive:bool = True
    sourceType:constructionTypes =  constructionTypes.impact
    
    def accumulateSEL(self):
        N = self.numberOfPiles*self.strikesPerPile
        self.LE_cumulative = calcSELImpulsive(self.SELss, N)
        
@dataclass  
class DTHSource(constructionSource):
    
    isImpulsive:bool = True
    sourceType: constructionTypes = constructionTypes.DTH
    
    def accumulateSEL(self):
        T_s = self.timePerPile_min*self.numberOfPiles*60
        N = T_s*self.strikeRate_Hz
        self.LE_cumulative = calcSELImpulsive(self.SELss, N)
        
@dataclass 
class vibratorySource(constructionSource):
    
    isImpulsive:bool = False
    sourceType: constructionTypes = constructionTypes.vibratory
  
    def accumulateSEL(self):
        T_m = self.timePerPile_min*self.numberOfPiles
        self.LE_cumulative = calcSELcont(self.Lrms,T_m)
        

@dataclass(frozen=True)
class combinedSource:
    LE:np.ndarray
    LE_impulsiveOnly:np.ndarray
    LE_nonImpulsiveOnly:np.ndarray
    Lpeak:float
    Lrms:float
    TL:float
    TL_impulsive:float
    TL_nonImpulsive:float
    measurementRange:float
    isImpulsive:bool 
    sourcesDF:pd.DataFrame
    hg:[str]
    
def addSourcesAlongHG(LE_all:np.ndarray,hgs:[str])->np.ndarray:
    """Adds weighted source levels for each hearing group for an arbitrary number of source.
    LE_all is expected to be a 2D np.ndarray with shape (i, len(hgs)) where i is the number of sources and
    len(hgs) is the number of hearing groups (typically 5). Source levels are added geometrically (in linear values)"""
    LE_sum = np.zeros(len(hgs),)
    # add SEL levels in each hearing group
    for i,LEhg in enumerate(LE_all.T):
        LE_sum[i] =addSources(LEhg)
        
    return LE_sum

    
def combineSources(impact:[dict], vibratory:[dict], DTH:[dict], Peak=False, Behavioral=False)->combinedSource:
    """A function which combines impact, vibratory, and DTH sources using input dictionaries
    having the appropriate keys (e.g. 'index', 'SEL', 'PEAK', 'RMS', 'RANGE', 'NPILES', 'NSTRIKES', 'TIME', 'RATE')
    and appropriate values.  Returns a combinedSource data class containing super-source levels, measurement range, 
    impulsive nature, and a dataframe containing all inputs and intermediary calculations"""
    
    print('combining sources')
    sources = []
    
    # unpack impact sources and build instances
    for i in range(len(impact['SEL'])):
        print('enter impact loop')
        sources.append(impactSource(
                                    index=i+1,
                                    SELss=impact['SEL'][i],
  #                                  Lpeak=impact['PEAK'][i],
  #                                  Lrms=impact['RMS'][i],
                                    TL=impact['F'][i],
                                    measuredRange_m=impact['RANGE'][i],
                                    numberOfPiles=impact['NPILES'][i],
                                    strikesPerPile=impact['NSTRIKES'][i],
                                    weightingFrequency_Hz=impact['WF'][i]*1e3
                                    
                                    )
                       )
    # unpack DTH sources and build instances
    for i in range(len(DTH['SEL'])):
        print('enter dthloop')
        sources.append(DTHSource(   
                                    index=i+1,
                                    SELss=DTH['SEL'][i],
     #                               Lpeak=DTH['PEAK'][i],
      #                              Lrms=DTH['RMS'][i],
                                    TL=DTH['F'][i],
                                    measuredRange_m=DTH['RANGE'][i],
                                    numberOfPiles=DTH['NPILES'][i],
                                    timePerPile_min=DTH['TIME'][i],
                                    strikeRate_Hz=DTH['RATE'][i],
                                    weightingFrequency_Hz=DTH['WF'][i]*1e3
                                    
                                    )
                       )  
    # unpack vibratory sources and build instances
    for i in range(len(vibratory['RMS'])):
        print('enter vibratory loop')
        sources.append(vibratorySource(
                                    index=i+1,
                                    Lrms=vibratory['RMS'][i],
                                    TL=vibratory['F'][i],
                                    measuredRange_m=vibratory['RANGE'][i],
                                    numberOfPiles=vibratory['NPILES'][i],
                                    timePerPile_min=vibratory['TIME'][i],
                                    weightingFrequency_Hz=vibratory['WF'][i]*1e3
                                    
                                    )
                       )  
        
        # Add sources and properties of super-source appropriately 
        
    print('exiting source loops')
    print(f'sources={sources}')
    # matrix of weighted levels
    LEw_all = np.array([source.LEw for source in sources])
    # get levels for all impulsive sources
    TL_all = np.array([source.TL for source in sources])
    TL = np.min(TL_all)    

    # overall impulsive nature, if any is impulsive assume impulsive
    isImpulsive = any([source.isImpulsive for source in sources])
    


 
    LEw_allNonImpulsive = []
    LEw_allImpulsive = []
    TL_allImpulsive = []  
    TL_allNonImpulsive = []

    nonImpulsiveExists=False
    impulsiveExists=False
    # get implusive only and non-impulsive only values
    for source in sources:
        if source.isImpulsive:
            LEw_allImpulsive.append(source.LEw)
            TL_allImpulsive.append(source.TL)
            impulsiveExists=True
            
        else:
            LEw_allNonImpulsive.append(source.LEw)
            TL_allNonImpulsive.append(source.TL)
            nonImpulsiveExists=True
            
    if nonImpulsiveExists:
        TL_nonImpulsive = np.min(np.array(TL_allNonImpulsive))
    else:
        TL_nonImpulsive = None
    if impulsiveExists:
        TL_impulsive = np.min(np.array(TL_allImpulsive))
    else:
        TL_impulsive = None
    
    # overall impulsive nature, if any is impulsive assume impulsive
    isImpulsive = any([source.isImpulsive for source in sources])

    if Peak:   
    # get peak levels, excluding vibratory
        Lpeak_allvib = np.array([source.Lpeak if source.isImpulsive else None for source in sources])
        Lpeak_all = Lpeak_allvib[Lpeak_allvib!=None]
        Lpeak = np.max(Lpeak_all)
    else:
        Lpeak=None
        
    if Behavioral:  
        # get all RMS levels
        Lrms_all = np.array([source.Lrms for source in sources])
        Lrms = addSources(Lrms_all)
    else:
        Lrms = None
    # get ranges
    ranges_all = np.array([source.measuredRange_m for source in sources])
    uniqueRanges = np.unique(ranges_all)
    if len(uniqueRanges)>1:
        raise ValueError('non uniform measurement ranges not yet implemented!')
    else:
        measurementRange = np.unique(ranges_all)[0]

    # add SEL levels in each hearing group
    LEw = addSourcesAlongHG(LEw_all, WA.hg)
    LEw_impulsive = addSourcesAlongHG(np.array(LEw_allImpulsive), WA.hg)
    LEw_non_impulsive = addSourcesAlongHG(np.array(LEw_allNonImpulsive), WA.hg)
    
        

    
    ## build dataframe
    indexArray =[f'{source.index}: {source.sourceType.name}' for source in sources]
    columnsArray = [f'SELc-{hg}' for hg in WA.hg]
    df = pd.DataFrame(data = np.round(LEw_all,decimals=2), columns=columnsArray ,index=indexArray)
    df.loc[len(df.index)]=np.round(LEw,decimals=2)
    df.rename(index={len(df.index)-1:'combined'},inplace=True)
    if Peak:
        df['Peak']=roundf(np.append(Lpeak_allvib,Lpeak))
    if Behavioral:
        df['RMS'] = np.round(np.append(Lrms_all,Lrms),decimals=2)
    df.index.set_names('Sources',inplace=True)

    return combinedSource(LE=LEw,
                          LE_impulsiveOnly = LEw_impulsive,
                          LE_nonImpulsiveOnly= LEw_non_impulsive,
                          Lpeak=Lpeak,
                          Lrms=Lrms,
                          measurementRange=measurementRange,
                          isImpulsive=isImpulsive,
                          sourcesDF=df,
                          hg=WA.hg,
                          TL=TL,
                          TL_impulsive=TL_impulsive,
                          TL_nonImpulsive=TL_nonImpulsive)
                         
        
            
        
        
    
    
    
    
    
    
        