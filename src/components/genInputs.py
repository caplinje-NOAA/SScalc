# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:38:22 2023

@author: jim
"""

from dash import Dash, dcc, html,State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from . import ids, sourceConfigInput
from .custom import inputGroups as ig



wf_dict = {'name':"Weighting Frequency",'id':ids.WF_INPUT,'unit':'KHz','value':2.0}
TL_dict = {'name':"TL coef.",'id':ids.F_INPUT,'unit':'dB','value':15.0}

def render(app: Dash) -> html.Div:
   

    return ig.inputGroupList('General Inputs', [TL_dict])