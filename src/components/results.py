# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:48:31 2023

@author: jim
"""


from dash import Dash, dcc, html,State, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from . import ids, sourceConfigInput
from ..calculator import multiSourceRange



def processInputs(impact,DTH,vibratory,WF,F):
    # test for empty array
    return f'total SELc = {multiSourceRange.calcRange(impact,DTH,vibratory,WF,F):.2f}'
    
    

def render(app: Dash) -> html.Div:
   
    @app.callback(
        output = [Output(ids.RESULTS_DIV, "children")],
        inputs = dict(
            
            n=Input(ids.CALCULATE_BUTTON, "n_clicks"),
  
            impact = [
                State({"type": ids.IMPACT_INPUT_SEL['id'], "index": ALL}, "value"),
                State({"type": ids.IMPACT_INPUT_PEAK['id'], "index": ALL}, "value"),
                State({"type": ids.IMPACT_INPUT_RMS['id'], "index": ALL}, "value"),
                State({"type": ids.IMPACT_INPUT_RANGE['id'], "index": ALL}, "value"),
                State({"type": ids.IMPACT_INPUT_NPILES['id'], "index": ALL}, "value"),
                State({"type": ids.IMPACT_INPUT_NSTRIKES['id'], "index": ALL}, "value")
            ],
            DTH = [
                State({"type": ids.DTH_INPUT_SEL['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_PEAK['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_RMS['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_RANGE['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_NPILES['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_RATE['id'], "index": ALL}, "value"),
                State({"type": ids.DTH_INPUT_TIME['id'], "index": ALL}, "value")
            ],

            vibratory= [
                State({"type": ids.VIBRATORY_INPUT_RMS['id'], "index": ALL}, "value"),
                State({"type": ids.VIBRATORY_INPUT_RANGE['id'], "index": ALL}, "value"),
                State({"type": ids.VIBRATORY_INPUT_NPILES['id'], "index": ALL}, "value"),
                State({"type": ids.VIBRATORY_INPUT_TIME['id'], "index": ALL}, "value")
                ],
            WF = State(ids.WF_INPUT, "value"),
            F  = State(ids.F_INPUT, "value")
                
                
            )   
    )
    def calc_results(n,impact,DTH,vibratory,WF,F):
        if n is None:
            return [html.Div()]
        else:
            
            return [html.Div(processInputs(impact, DTH, vibratory,WF,F))]

    return html.Div(
        [
            dbc.Button("Calculate", id=ids.CALCULATE_BUTTON, n_clicks=0,class_name='button'),
            html.Div(id=ids.RESULTS_DIV)
        ]
    )
