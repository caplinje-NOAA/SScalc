# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:16:27 2023

@author: james.caplinger

Ranges to regulatory thresholds as dataclasses
Taken from 2022 NMFS: Summary of Marine Mammal Protection Act Acoustic Thresholds
Last edited on 4/14/2023

"""

from dataclasses import dataclass
import numpy as np

# Onset of permanent Threshold Shift for Non-impulsive sources (NMFS 2018)
@dataclass
class PTS_non_impulsive:
    # hearing group identifiers
    hg: np.ndarray =    np.array(['LF','MF','HF','PW','OW'])
    # 24 hour SEL                  |    |    |    |    |  
    LE:    np.ndarray = np.array([199.,198.,173.,201.,219.])

# Onset of permanent Threshold Shift for impulsive sources (NMFS 2018)
@dataclass
class PTS_impulsive:
    # hearing group identifiers
    hg: np.ndarray =    np.array(['LF','MF','HF','PW','OW'])
    # peak                         |    |    |    |    |  
    Lpeak: np.ndarray = np.array([219.,230.,202.,218.,232.])
    # 24 hour SEL
    LE:    np.ndarray = np.array([183.,185.,155.,185.,203.])

# Underwater Level B Harassment Acoustic Thresholds (NOAA 2005)
@dataclass
class Behavioral:
    Lrms_continuous: float = 120.
    Lrms_impulsive:  float = 160.
    
#PTS onset for Underwater Explosivves (NMFS 2018)
@dataclass
class Explosives_PTS_impulsive:
    # hearing group identifiers
    hg: np.ndarray =    np.array(['LF','MF','HF','PW','OW'])
    # peak                         |    |    |    |    |  
    Lpeak: np.ndarray = np.array([219.,230.,202.,218.,232.])
    # 24 hour SEL
    LE: np.ndarray = np.array([183.,185.,155.,185.,203.])

#TTS onset for Underwater Explosivves (NMFS 2018)    
@dataclass
class Explosives_TTS_impulsive:
    # hearing group identifiers
    hg: np.ndarray =    np.array(['LF','MF','HF','PW','OW'])
    # peak                         |    |    |    |    |  
    Lpeak: np.ndarray = np.array([213.,224.,196.,212.,226.])
    # 24 hour SEL
    LE:    np.ndarray = np.array([168.,170.,140.,170.,188.])

# Behavioral Thresholds (Multiple detonations) for Underwater Explosives (NMFS 2018)    
@dataclass
class Explosives_Behavioral:
    # hearing group identifiers
    hg: np.ndarray = np.array(['LF','MF','HF','PW','OW'])
    # 24 hour SEL               |    |    |    |    |  
    LE: np.ndarray = np.array([163.,165.,135.,165.,183.])


    
  
    
