# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:18:26 2023

@author: jim
"""

from dash import Dash, html
import dash_bootstrap_components as dbc


from . import ids
from .custom import inputGroups as ig

def titleDiv(title,i):
    return html.Div(
                dbc.Row(
                    [
                     dbc.Col(html.H4(title)),
                     dbc.Col(html.Div(dbc.Button(id={"type": ids.HIDDEN_SOURCE_BUTTON, "index": i},disabled=True),style={'display':'none'})),
                     dbc.Col(html.Div(id={"type": ids.SELRES, "index": i}))
                     ]
                    )
                )

        

def buildInputDiv(types)->html.Div:
    cols = []
    for i,t in enumerate(types):
        title = titleDiv(f'Source {i}: {t}',i)
        if t=='Impact':
            col = ig.inputGroupList(title,ids.impactInputDict,index=i,className='app-div')
        if t=='DTH':
            col = ig.inputGroupList(title,ids.DTH_InputDict,index=i,className='app-div')
        if t=='Vibratory':
            col = ig.inputGroupList(title,ids.vibratoryInputDict,index=i,className='app-div')
        cols.append(dbc.Col(col))
    return html.Div(dbc.Row(cols))



def render(app: Dash) -> html.Div:
   


    return html.Div(id=ids.INPUTS_DIV)
      