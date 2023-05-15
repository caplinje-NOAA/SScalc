# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:06:33 2023

@author: jim
"""

from dash import Dash, dcc, html,State, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from . import ids, inputs


saveAlert = dbc.Alert(
    "configuration saved.",
    id="alert-auto",
    is_open=True,
    duration=4000,
)


class sourceConfig:
    n:int=1
    types:[str] = ['impact']
    
currentSourceConfig=sourceConfig()

def buildDropdown(i):
    return html.Div([html.P(f'Source {i+1} type:'),
    dbc.Select(
    id={"type": ids.SOURCE_TYPES, "index": i}, 
    options=[
        {"label": "DTH", "value": "DTH"},
        {"label": "Impact", "value": "Impact"},
        {"label": "Vibratory", "value": "Vibratory"},
    ],
)])

def render(app: Dash) -> html.Div:
   
    @app.callback(
        Output(ids.SOURCE_TYPE_DROPDOWN_CONTAINER, "children"),
        Input(ids.N_SOURCES_INPUT, "value"),
       
    )
    def build_dropdowns(n):
        
        dropdowns=[]
        if n is not None:
            print('building dropdowns')
            for i in range(n):
                
                dropdowns.append(buildDropdown(i))
        return dropdowns
    
    @app.callback(
       # Output(ids.CONFIGURE_SOURCES_CANVAS, "is_open"),
        Output(ids.CONFIG_DISPLAY,"children"),
        Output(ids.CANVAS_ALERT,"children"),
        Output(ids.INPUTS_DIV,"children"),
        Input(ids.SAVE_CONIG_BUTTON, "n_clicks"),
        [State({"type": ids.SOURCE_TYPES, "index": ALL}, "value"),
         State(ids.N_SOURCES_INPUT,"value"),
         State(ids.CONFIGURE_SOURCES_CANVAS, "is_open")
          ]
       
    )
    def save_configurations(n1,sourceTypes,nSources,is_open):
        print(n1,sourceTypes,nSources,is_open)
        if n1 is None:
            return html.Div('no config'), html.Div(), html.Div()
        else:
            outstr = f'Current Configuration: {nSources} sources ('
            for s in sourceTypes:
                outstr = outstr+f'{s}, '
            outstr=outstr[:-2]+')'
            
            return html.Div(outstr), html.Div(saveAlert), inputs.buildInputDiv(sourceTypes)
        
     
        

    return html.Div(
        [
            html.P("Enter the total number of sources"),
            dbc.Input(type="number", min=0, max=10, step=1,id=ids.N_SOURCES_INPUT),
            dbc.Col(children=[dbc.Select(
            id="select",
            options=[
                {"label": "DTH", "value": "1"},
                {"label": "Impact", "value": "2"},
                {"label": "Vibratory", "value": "3", "disabled": True},
            ],
        )],id=ids.SOURCE_TYPE_DROPDOWN_CONTAINER),
        dbc.Button("Save Configuration", id=ids.SAVE_CONIG_BUTTON, n_clicks=0,class_name='button'),
        html.Div(id=ids.CANVAS_ALERT)
        ],
        id='sourceConfigDiv',
        
    )
