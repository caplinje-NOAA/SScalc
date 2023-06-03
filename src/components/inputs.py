# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:18:26 2023

@author: jim
"""

from dash import Dash, html
import dash_bootstrap_components as dbc


from . import ids
from .custom import inputGroups as ig
from ..calculator.data import pileDrivingDefaults

def titleDiv(title,i):
    return html.Div(
                dbc.Row(
                    [
                     dbc.Col(html.H4(title)),

                     ]
                    )
                )




def tabContent(index:int,Type:str):
    title = f'User Inputs for Source {index}: {Type}'
    wfDict= ids.WF_INPUT
    FDict = ids.F_INPUT_BYSOURCE
    
    if Type=='Impact':
        mainInputs = ig.inputGroupList(title,ids.impactInputDict,index=index)
        wfDict['sourceType']=ids.IMPACT
        wfDict['value'] = pileDrivingDefaults.impact_Wfreq
        FDict['sourceType']=ids.IMPACT
        
    if Type=='DTH':
        mainInputs = ig.inputGroupList(title,ids.DTH_InputDict,index=index)
        wfDict['sourceType']=ids.DTH
        wfDict['value'] = pileDrivingDefaults.DTH_WFreq
        FDict['sourceType']=ids.DTH
        
    if Type=='Vibratory':
        mainInputs = ig.inputGroupList(title,ids.vibratoryInputDict,index=index)
        wfDict['sourceType']=ids.VIBRATORY
        wfDict['value'] = pileDrivingDefaults.vibratory_WFreq
        FDict['sourceType']=ids.VIBRATORY
  
    defaultDict=[wfDict,FDict]
    defaultInputs = ig.inputGroupList('Recommended Defaults', defaultDict,index=index)
    return html.Div(
                dbc.Row(
                    [
                     dbc.Col(mainInputs),
                     
                     dbc.Col(defaultInputs)
                     ]
                    )
                )
    

def buildInputDiv(types)->html.Div:
    tabs = []
    for i,t in enumerate(types):
   
        contents = tabContent(i,t)
        tabs.append(dbc.Tab(contents,label=f'Source {i+1}: {t}'))
    return html.Div(dbc.Tabs(tabs))



def render(app: Dash) -> html.Div:
   


    return html.Div(id=ids.INPUTS_DIV)
      