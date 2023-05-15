# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:18:37 2023

@author: james.caplinger
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from dataclasses import dataclass
#from basicTools import genericCSVhandler as gCSV
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


#####| LF | MF  |  HF |  PW |  OW |# Hearing Groups
a  = [   1,  1.6,  1.8,    1, 2   ]
f1 = [ 0.2,  8.8,   12,  1.9, 0.94]
f2 = [  19,  110,  140,   30, 25  ] 
C  = [0.13,  1.2, 1.36, 0.75, 0.64]
K  = [ 179,  177,  152,  180, 198 ]
b  = 2.0 # for all
hearingGroups = ['LF','MF','HF','PW','OW']

# generate center frequencies for third octive bands from start to stop i
def thirdOctavef(start,stop):
    f = []
    for i in range(start,stop+1):
        f.append(10**(i/10.)*1e3)
    
    return np.array(f)
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
        
    

def broadbandLevel(Ldecidecade):
    p = 0
    for Lpi in Ldecidecade:
        p = p + 10**(Lpi/10)
    return 10*np.log10(p)

def applyWeighting(f: np.ndarray,L: np.ndarray,group:str) -> [WF]:
    WF_all = genWFs(f=f)
    wfi = hearingGroups.index(group)
    wf = WF_all[wfi]
    Lweighted = L-wf.w
    return Lweighted
            

## go ahead and plot those bad boys
def plotGroups():
    WF_all = genWFs()
    ### common settings ###
    linewidth = 0.6

    f = WF_all[0].f
    #color = 'b'
    ylim = [-40,5]
    xlim = [np.min(f),np.max(f)]
    grid = False
    manualLims = True
        
        
    fig, ax = plt.subplots()
    legendstr=[]
    for wf in WF_all:
        
        ax.semilogx(wf.f,wf.w,linewidth=linewidth)
        legendstr.append(wf.hearingGroup)

    ax.set_xlabel(wf.funits)
    ax.set_ylabel(wf.wunits)
    if manualLims:
        ax.set_ylim(ylim)
        ax.set_xlim(xlim)
    ax.set_title('MM Weighting Functions')
    ax.legend(legendstr)
    ax.grid(visible=grid)

## some validation against JASCOs appendix digitized
# def validate():
#     meanError = []
#     WF_all = genWFs()
#     for i,group in enumerate(hearingGroups):
#         wf = WF_all[i]
#         dfolder = 'data//MMwfVal//'
#         path = f'{dfolder}{group}.txt'
#         valData = gCSV.loadXYdata(path)
#         err = []
#         for j in range(valData.n):
#             iif = np.argmin(np.abs(valData.x[j]-wf.f))
#             winterp = np.interp(valData.x[j],wf.f,wf.w)
#             pntError = np.abs(valData.y[j]-winterp)
#             err.append(pntError)
#             if pntError>5:
#                 print(f'sig. error found at {valData.x[j]:.1f} Hz for {group}')
#                 print(f'Reference has {valData.y[j]:.1f} dB vs. {wf.w[iif]:.1f} dB here.')
#         #print(err)
#         meanError.append(np.mean(np.array(err)))
#     totalmean = np.mean(np.array(meanError))
    
#     #print('MMweighting.py validation result:')
#     #print(f'Mean error rel. to digitized data = {totalmean:.3f} dB')
    
#     if totalmean<0.17:
#         return True
#     else:
#         raise ValueError('Weighting functions do not agree with reference!!')
#         return False
                
# validate()           
        
        
        
    
