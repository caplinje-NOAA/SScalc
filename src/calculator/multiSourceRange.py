# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:06:28 2023

@author: jim
"""

from .data.NMFS_thresholds import PTS_impulsive, Behavioral
from .src.userSpreadsheetTools import calcImpact_SELc,calcDTH_SELc,calcVib_SELc, calcRange, addSources
from .src.MMweighting import genWFsimple
import pandas as pd
import numpy as np



def calcRange(impact,dth,vibratory,weightingFrequency,F):

    ## impact
   
    SELcArr_I = []
    for SELss, Npiles, Nstrikes in zip(impact[0],impact[4],impact[5]):
        SELcArr_I.append(calcImpact_SELc(SELss,Npiles,Nstrikes))
    ## DTH

    SELcArr_D = []
    for SELss, Npiles, Tpile_m,strikeRate_s in zip(dth[0],dth[4],dth[6],dth[5]):
        SELcArr_D.append(calcDTH_SELc(SELss,Npiles,Tpile_m,strikeRate_s))            

    ## VIB

    SELcArr_V = []
    for Lrms, Npiles, Tpile_m in zip(vibratory[0],vibratory[2],vibratory[3]):
        SELcArr_V.append(calcVib_SELc(Lrms,Npiles,Tpile_m))     
        
    SELall = np.concatenate((SELcArr_I,SELcArr_D,SELcArr_V))
    
    SELc = addSources(SELall)
    
    WF = genWFsimple(weightingFrequency)
    SELw = SELc+WF.w
    
#    PTSranges = calcRange(SELw,PTS_non_impulsive.LE,F=TL,mRange=mRange)

    return SELc