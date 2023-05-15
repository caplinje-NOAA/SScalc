# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 14:24:28 2023

@author: james.caplinger
A python version of the NMFS user spreadsheet vibratory tab
Checked results against spreadsheet with full agreement on 4/13/2023
last edited: 4/13/2023, dependencies unknown

"""

from data.NMFS_thresholds import PTS_non_impulsive, Behavioral
from src.userSpreadsheetTools import calcSELcont, calcRange
import src.MMweighting as MMW
import pandas as pd
import numpy as np
print('--Vibratory Pile Driving Calculator--')
# Generic inputs / assumed constants
weightingFrequency = 2.5e3 # 2.5 kHz is default WF factor for vibratory
TL = 15.0      # transmission loss coefficient

### PILE SPECIFIC INPUTS ###
Lrms = 170.    # RMS source level (dB rel 1 uPa)
mRange = 10.   # range of Lrms in meters
Npiles = 3     # number of piles in 24 hours
Tpile_m = 2.5*60.0 # minutes to drive one pile
###############

# geting weighting adjustments
WF = MMW.genWFsimple(weightingFrequency)
# hearing group strings
hg = PTS_non_impulsive.hg

# calculate SEL
T_m = Tpile_m*Npiles
SEL = calcSELcont(Lrms,T_m)

# apply weighting adjustment
SELw = SEL+WF.w

# Calculate Ranges
PTSranges = calcRange(SELw,PTS_non_impulsive.LE,F=TL,mRange=mRange)
behavioralRange = calcRange(Lrms,Behavioral.Lrms_continuous,F=TL,mRange=mRange)

# Build Dataframe and print results
df = pd.DataFrame(np.array([PTS_non_impulsive.LE,PTSranges]),columns=hg,index=['SELcum Threshold', 'PTS Isopleth (m)'])
pd.options.display.float_format = '{:,.2f}'.format
print('_______________________________________________________')
print('Level A results:')
print(df)
print('_______________________________________________________')
print('Level B results:')
print(f'Range to {Behavioral.Lrms_continuous:.1f} dB threshold: {behavioralRange:.2f} meters.')
print('_______________________________________________________')
















