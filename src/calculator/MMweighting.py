# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:18:37 2023

@author: james.caplinger
"""
import numpy as np
from dataclasses import dataclass

from .data import MMweightingFunctionCoefficients as WCF


# get data from MMweightingFunctionCoefficients.py
a  = WCF.a
f1 = WCF.f1
f2 = WCF.f2
C  = WCF.C
K  = WCF.K
b  = WCF.b
hearingGroups = WCF.hearingGroups



# generate center frequencies for third octive bands from start to stop i
def thirdOctavef(start,stop):
    f = []
    for i in range(start,stop+1):
        f.append(10**(i/10.)*1e3)
    
    return np.array(f)

## default frequency array
fdefault = thirdOctavef(-20,30)

@dataclass
class WF:
    w: np.ndarray
    f: np.ndarray
    hearingGroup: str
    funits: str = 'Hz'
    wunits: str = 'dB'
 
@dataclass
class WA:
    w: np.ndarray = np.empty((5,))
    hg: np.ndarray =    np.array(['LF','MF','HF','PW','OW'])
# Calculates the MM weighting filters for all hearing groups
def weightingMM(f,groupIndex):
  n = groupIndex
  Wf =  np.zeros((len(f),))
  fkHz = f/1e3

  Wf = C[n] + 10*np.log10((fkHz/f1[n])**(2*a[n])/((1+(fkHz/f1[n])**2)**a[n]*(1+(fkHz/f2[n])**2)**b))
  out = WF(w=Wf,f=f,hearingGroup=hearingGroups[n])
  return out


## default frequency array
fdefault = thirdOctavef(-20,30)
## generate all WFs
def genWFs(f=fdefault):

    WF_LF = weightingMM(f,hearingGroups.index('LF'))
    WF_MF = weightingMM(f,hearingGroups.index('MF'))
    WF_HF = weightingMM(f,hearingGroups.index('HF'))
    WF_PW = weightingMM(f,hearingGroups.index('PW'))
    WF_OW = weightingMM(f,hearingGroups.index('OW'))
    
    WF_all = [WF_LF,WF_MF,WF_HF,WF_PW,WF_OW]
    return WF_all

def genWFsimple(f=2e3):
    '''Generates simple single frequency weightings for each hearing group'''
    WF = genWFs(np.array([f]))
    out = WA()
    for i,wf in enumerate(WF):
        if wf.f[0] ==f:
            if wf.hearingGroup==out.hg[i]:
                out.w[i]=wf.w[0]
    return out
        

    

