# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:06:28 2023

@author: jim
"""

from .data.NMFS_thresholds import PTS_impulsive, Behavioral, PTS_non_impulsive
from .data import pileDrivingDefaults

from .src.constructionSources import combineSources
import pandas as pd
import numpy as np
from dataclasses import dataclass

def calcRange(SL,thresh,F:float=15.0,mRange:float=1.0):
    """Calculates the range to a given threshold, given a source level (which can be defined at any measured range, mRange, which defaults at 1 meter)
    and a transmission loss coefficient, F"""
        
    return mRange*10.**((SL-thresh)/F)

@dataclass(frozen=True)
class results:
    rangesDF:pd.DataFrame
    inputDF:pd.DataFrame

def calcRanges_MS(impact,dth,vibratory,weightingFrequencies=None,Peak=False,Behavioral=False):
    """Calculate PTS and behavioral ranges for an arbitray number of impact, 
    dth and vibratory sources using transmission loss specified by F. The inputs
    'impact', 'dth', and 'vibratory' are expected to be dictionaries containing 
    keys corresponding to parameters ('SEL', 'NPILES, and 'NSTRIKES' for impact; 
    'SEL', 'NPILES', 'TIME', and 'RATE' for DTH; and 'RMS', 'NPILES' and 'TIME' 
    for vibratory.  Values associated with each key are expected as arrays 
    representing all sources of that type. Non-default weighting frequencies 
    should be specified as a dictionary with keys 'impact', 'dth' and 'vibratory'
    with values corresponding to the single weighting frequency desired for each
    source type.  If all sources are non-impulsive, non-impulsive thresholds are 
    used.  If any sources are impulsive, the impulsive PTS thresholds are used.
    The function returns one pandas dataframe echoing inputs and one pandas data-
    frame containing calculated isopleths for each hearing group. Currently, non-
    uniform measurement ranges are not treated, a ValueError will be raised in 
    the case all measurment ranges are not equal. """
    
    
    combinedSource = combineSources(impact, vibratory, dth,Peak=Peak,Behavioral=Behavioral)
    F=combinedSource.TL
    # check if impulsive sources exist
    if combinedSource.isImpulsive:
        thresholdType = 'impulsive'
        # select thresholds
        PTS_thresholds_SEL = PTS_impulsive.LE

        # calculate PTS isopleths
        PTSranges_SEL = np.round(calcRange(combinedSource.LE,PTS_thresholds_SEL,F=F,mRange=combinedSource.measurementRange),decimals=2)
   
        data = [PTS_thresholds_SEL,PTSranges_SEL]
      
        # if Peak:
        #     PTS_thresholds_PEAK = PTS_impulsive.Lpeak
        #     PTSranges_PEAK = np.round(calcRange(combinedSource.Lpeak,PTS_thresholds_PEAK,F=F,mRange=combinedSource.measurementRange),decimals=2)
        #     data.append(PTS_thresholds_PEAK,PTSranges_PEAK)
        #     indexTitles.append('Level A (Peak) Threshold')
        #     indexTitles.append('PTS (Peak) Isopleth (m)')
        # if Behavioral:    
        #     BehavioralThreshold = np.ones_like(PTSranges_SEL)*Behavioral.Lrms_continuous
        #     BehavioralRange = np.round(calcRange(combinedSource.Lrms,BehavioralThreshold,F=F,mRange=combinedSource.measurementRange),decimals=2)
        #     data.append(BehavioralThreshold,BehavioralRange)
        #     indexTitles.append('Level B Threshold')
        #     indexTitles.append('Behavioral Range (m)')
       

        
    else:
        thresholdType = 'non-impulsive'
        PTSthresholds = PTS_non_impulsive.LE
        PTSranges = np.round(calcRange(combinedSource.LE,PTSthresholds,F=F,mRange=combinedSource.measurementRange),decimals=2)
        
        data = np.array([PTSthresholds,PTSranges])

        # if Behavioral:
        #     BehavioralThreshold = np.ones_like(PTSranges)*Behavioral.Lrms_continuous
        #     BehavioralRange = calcRange(combinedSource.Lrms,BehavioralThreshold,F=F,mRange=combinedSource.measurementRange)
        #     data.append(BehavioralThreshold, BehavioralRange)
        #     indexTitles.append('Level B Threshold')
        #     indexTitles.append('Behavioral Range (m)')
    
    PTSranges_impulsiveOnly = np.round(calcRange(combinedSource.LE_impulsiveOnly,PTS_impulsive.LE,F=combinedSource.TL_impulsive,mRange=combinedSource.measurementRange) ,decimals=2)
    PTSranges_nonImpulsiveOnly = np.round(calcRange(combinedSource.LE_nonImpulsiveOnly,PTS_non_impulsive.LE,F=combinedSource.TL_nonImpulsive,mRange=combinedSource.measurementRange),decimals=2) 
    indexTitles = ['Level A (SEL, combined) Threshold',
                   'PTS Isopleth (m, combined)',
                   'Level A (SEL, impulsive) Threshold',
                   'PTS Isopleth (m, impulsive only)',
                   'Level A (SEL, non-impulsive) Threshold',
                   'PTS Isopleth (m, non-impulsive only)',                       
                   ]
    data.append(PTS_impulsive.LE)
    data.append(PTSranges_impulsiveOnly)
    data.append(PTS_non_impulsive.LE)
    data.append(PTSranges_nonImpulsiveOnly)
    rangesDF = pd.DataFrame(np.array(data),columns=combinedSource.hg,index=indexTitles)
    rangesDF.index.name='Hearing Group'
    return results(rangesDF,combinedSource.sourcesDF)













# OLD method before constructionSource classes were used
 # # weighting functions and frequencies 
 # # if no weightingFrequencies dictionary is provided, use devaults in pileDrivingDefaults.py
 # if not weightingFrequencies:
 # # weighting functions
 #     WF_I = genWFsimple(pileDrivingDefaults.impact_Wfreq)
 #     WF_D = genWFsimple(pileDrivingDefaults.DTH_Wfreq)
 #     WF_V = genWFsimple(pileDrivingDefaults.vibratory_WFreq)  
 # else:       
 #     WF_I = genWFsimple(weightingFrequencies['impact'])
 #     WF_D = genWFsimple(weightingFrequencies['DTH'])
 #     WF_V = genWFsimple(weightingFrequencies['vibratory'])     
     
 # # get strings of hearing groups    
 # hearingGroups = WF_I.hg
 
 # ## impact

 # SELcArr_I = []
 # for SELss, Npiles, Nstrikes in zip(impact['SEL'],impact['NPILES'],impact['NSTRIKES']):
 #     # apply appropriate weighting 
 #     SELval = calcImpact_SELc(SELss,Npiles,Nstrikes)+WF_I.w
 #     SELcArr_I.append(SELval)

 # ## DTH

 # SELcArr_D = []
 # for SELss, Npiles, Tpile_m,strikeRate_s in zip(dth['SEL'],dth['NPILES'],dth['TIME'],dth['RATE']):
 #     SELval = calcDTH_SELc(SELss,Npiles,Tpile_m,strikeRate_s)+WF_D.w
 #     SELcArr_D.append(SELval)            

 # ## VIB

 # SELcArr_V = []
 # for Lrms, Npiles, Tpile_m in zip(vibratory['RMS'],vibratory['NPILES'],vibratory['TIME']):
 #     SELval = calcVib_SELc(Lrms,Npiles,Tpile_m)+WF_V.w
 #     SELcArr_V.append(calcVib_SELc(Lrms,Npiles,Tpile_m))     
 
 # # check if impulsive sources exist
 # if (len(SELcArr_I)==0) and (len(SELcArr_D)==0):
 #     PTS_thresholds = PTS_non_impulsive
 #     thresholdType = 'non-impulsive'
 # else:
 #     PTS_thresholds = PTS_impulsive
 #     thresholdType = 'impulsive'
     
 
 # # just need to finish up range calculation and build dataframes
 # SELall = np.concatenate((SELcArr_I,SELcArr_D,SELcArr_V))
 # RMSall = np.concatenate(impact['RMS'],dth['RMS'],vibratory['RMS'])
 # PEAKall = np.concatenate(impact['PEAK'],dth['PEAK'])
 
 # allRanges = np.concatenate(impact['RANGE'],dth['RANGE'],vibratory['RANGE'])
 # uniqueRanges = np.unique(allRanges)
 # if len(uniqueRanges)>1:
 #     raise ValueError('Measurement range of each source must be equal!')
 # else:
 #     mRange = uniqueRanges[0]
 # LE = addSources(SELall)
 # Lrms = addSources(RMSall)
 # Lpeak = np.max(PEAKall)














