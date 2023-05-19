# -*- coding: utf-8 -*-
"""
Created on Thu May 18 13:42:30 2023

@author: jim

Super messy and failed on \mu, mathjax is better in terms of implementation but I don't like the font contrast

"""

from dash import html




    
def parseSup(string):
    """parse a string and return list of strings and html items to support superscripts"""
    cl = string.find('^{')
    if cl>-1:
        s = string.find('{')
        e = string.find('}')
        subtext = string[s+1:e]
        return [string[0:cl],html.Sup(subtext)]+parseSup(string[e+1:])
    else:
        return [string]
    
def parseSub(string):
    """parse a string and return list of strings and html items to support subscripts"""
    cl = string.find('_{')
    if cl>-1:
        s = string.find('{')
        e = string.find('}')
        subtext = string[s+1:e]
        return [string[0:cl],html.Sub(subtext)]+parseSup(string[e+1:])
    else:
        return [string]



def parseAll(string):
    """parse a string and return list of strings and html items to support sub and superscripts"""
    out = [string]
    out2 = []
    for string in out:
        if isinstance(string,str):
            out2=out2+parseSup(string)
        else:
            out2 = out2+[string]
    out3 = []
    for string in out2:
        if isinstance(string,str):
            out3=out3+parseSub(string)
        else:
            out3 = out3+[string]
            

    return out3
        