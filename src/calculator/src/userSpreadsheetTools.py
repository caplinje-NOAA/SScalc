# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:52:12 2023

@author: james.caplinger
A collection of very basic acoustic tools related to estimated MM impacts

"""

import numpy as np

def calcSELcont(Lrms: float,T_m: float)->float:
    """Calculates the sound exposure level given a Sound Pressure Level in dB rel 1 uPa and a duration in minutes"""
    T = T_m*60
    return 10*np.log10(T)+Lrms

def calcSELImpulsive(SELss,N):
    return SELss+10*np.log10(N)

def calcRange(SL,thresh,F:float=15.0,mRange:float=1.0):
    """Calculates the range to a given threshold, given a source level (which can be defined at any measured range, mRange, which defaults at 1 meter)
    and a transmission loss coefficient, F"""
        
    return mRange*10.**((SL-thresh)/F)

def addSources(Larr):
    """Adds sound levels from two sources in linear pressure values and converts back to dB"""
    lin = 0
    for L in Larr:
        lin = lin+10**(L/10)
    return 10*np.log10(lin)

def calcImpact_SELc(SELss,Npiles,strikesPerPile):
    # calculate SEL
    N = Npiles*strikesPerPile
    return calcSELImpulsive(SELss,N)

def calcDTH_SELc(SELss,Npiles,Tpile_m,strikeRate_s):
    # calculate SEL
    T_s = Tpile_m*Npiles*60
    N = T_s*strikeRate_s
    return calcSELImpulsive(SELss,N)

def calcVib_SELc(Lrms,Npiles,Tpile_m):
    T_m = Tpile_m*Npiles
    return calcSELcont(Lrms,T_m)