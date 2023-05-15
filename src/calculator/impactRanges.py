# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:24:28 2023

@author: james.caplinger
A python version of the NMFS user spreadsheet Impact Pile Driving tab
Checked results against spreadsheet with full agreement on 4/13/2023
last edited: 4/13/2023, dependencies unknown

"""

from data.NMFS_thresholds import PTS_impulsive, Behavioral
from src.userSpreadsheetTools import calcSELImpulsive, calcRange
import src.MMweighting as MMW
import pandas as pd
import numpy as np

weightingFrequency = 2.0e3 # 2.0 kHz is default WF factor for Impact
TL = 15.0         # transmission loss coefficient
### Pile Specific INPUTS ###
SELss = 183.        # Single Strike SEL (dB rel 1 uPa s)
Lpeak = 210.        # Peak Level, 0-peak (dB rel 1 uPa)
Lrms = 193.         # RMS source level (dB rel 1 uPa)
mRange = 10.        # range of Lrms in meters
Npiles = 2          # number of piles in 24 hours
strikesPerPile = 1200 # strikes per pile
###############

# geting weighting adjustments
WF = MMW.genWFsimple(weightingFrequency)
# hearing group strings
hg = PTS_impulsive.hg

# calculate SEL
N = Npiles*strikesPerPile
SEL = calcSELImpulsive(SELss,N)

# apply weighting adjustment
SELw = SEL+WF.w

# Calculate Ranges
PTSranges_SEL = calcRange(SELw,PTS_impulsive.LE,F=TL,mRange=mRange)
PTSranges_Peak = calcRange(Lpeak,PTS_impulsive.Lpeak,F=TL,mRange=mRange)
behavioralRange = calcRange(Lrms,Behavioral.Lrms_impulsive,F=TL,mRange=mRange)

# Build Dataframe and print results
df = pd.DataFrame(np.array([PTS_impulsive.LE,PTSranges_SEL,PTS_impulsive.Lpeak,PTSranges_Peak]),columns=hg,index=['SELcum Threshold', 'PTS SEL Isopleth (m)','Lpeak Threshold', 'PTS peak Isopleth (m)'])
pd.options.display.float_format = '{:,.2f}'.format
print('_______________________________________________________')
print('Source levels in dB')
print(f'SELss = {SELss:.1f}, SELcum = {SEL:.1f}, Lpeak={Lpeak:.1f}, Lrms={Lrms:.1f} ')
print('_______________________________________________________')
print(f'Level A results:')
print(df)
print('_______________________________________________________')
print('Level B results:')
print(f'Range to {Behavioral.Lrms_impulsive:.1f} dB threshold: {behavioralRange:.2f} meters.')
print('_______________________________________________________')
