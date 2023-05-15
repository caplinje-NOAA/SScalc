# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:24:28 2023

@author: james.caplinger
A python version of the NMFS user spreadsheet Impact Pile Driving tab, modified for simultaneous sources (of vibratory and impact combined)
Checked results against spreadsheet with full agreement on 4/13/2023
last edited: 4/13/2023, dependencies unknown

"""

from data.NMFS_thresholds import PTS_impulsive, Behavioral
from basicTools.userSpreadsheetTools import calcSELImpulsive, calcSELcont, calcRange, addSources
import MMweighting as MMW
import pandas as pd
import numpy as np

### INPUTS ###
weightingFrequency = 2.0e3 # 2.0 kHz is default WF factor for DTH
SELss_i = 183     # Single Strike SEL (dB rel 1 uPa s)
SELss_d = 159
Lpeak = 210       # Peak Level, 0-peak (dB rel 1 uPa)
Lrms_i = 193      # RMS source level (dB rel 1 uPa)
Lrms_d = 167
mRange = 10.        # range of Lrms in meters
## impact parameters
Npiles_i = 1          # number of piles in 24 hours
strikesPerPile = 2400 # strikes per second
# DTH parameters
Npiles_d = 2
Tpile_m = 2*60    # minutes to drive one pile
strikeRate_s = 8 # strikes per second

TL = 15.0         # transmission loss coefficient
###############

# add sources levels

# geting weighting adjustments
WF = MMW.genWFsimple(weightingFrequency)
# hearing group strings
hg = PTS_impulsive.hg

# calculate SEL
Ni = Npiles_i*strikesPerPile
SELi = calcSELImpulsive(SELss_i,Ni)
# calculate SEL
T_s = Tpile_m*Npiles_d*60
Nd = T_s*strikeRate_s
SELd = calcSELImpulsive(SELss_d,Nd)


SEL = addSources(SELd,SELi)

Lrms = addSources(Lrms_i,Lrms_d)
# apply weighting adjustment
SELw = SEL+WF.w

# Calculate Ranges
PTSranges_SEL = calcRange(SELw,PTS_impulsive.LE,F=TL,mRange=mRange)
PTSranges_Peak = calcRange(Lpeak,PTS_impulsive.Lpeak,F=TL,mRange=mRange)
behavioralRange = calcRange(Lrms,Behavioral.Lrms_continuous,F=TL,mRange=mRange)

# Build Dataframe and print results
df = pd.DataFrame(np.array([PTS_impulsive.LE,PTSranges_SEL,PTS_impulsive.Lpeak,PTSranges_Peak]),columns=hg,index=['SELcum Threshold', 'PTS SEL Isopleth (m)','Lpeak Threshold', 'PTS peak Isopleth (m)'])
pd.options.display.float_format = '{:,.2f}'.format
print('_______________________________________________________')
print('Source levels in dB')
print(f'SELss = {SELss_i:.1f}, SELcum = {SEL:.1f}, Lpeak={Lpeak:.1f}, Lrms={Lrms:.1f} ')
print('_______________________________________________________')
print(f'Level A results:')
print(df)
print('_______________________________________________________')
print('Level B results:')
print(f'Range to {Behavioral.Lrms_continuous:.1f} dB threshold: {behavioralRange:.2f} meters.')
print('_______________________________________________________')
