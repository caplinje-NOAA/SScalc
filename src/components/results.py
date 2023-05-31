# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:48:31 2023

@author: jim
"""


from dash import Dash, dcc, html,State, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import traceback



from . import ids, sourceConfigInput
from ..calculator import multiSourceRange

def resTables(res:multiSourceRange.results):
    return dbc.Row([
        dbc.Col( dbc.Table.from_dataframe(res.inputDF,striped=True,bordered=True,hover=True,index=True)),
        dbc.Col( dbc.Table.from_dataframe(res.rangesDF,striped=True,bordered=True,hover=True,index=True))
        ]
        )
    



def processInputs(impact,DTH,vibratory):
    # test for empty array
    res = multiSourceRange.calcRanges_MS(impact,DTH,vibratory)
    
    return resTables(res)
    
    

def render(app: Dash) -> html.Div:
   
    @app.callback(
        output = [Output(ids.RESULTS_DIV, "children",allow_duplicate=True)],
        inputs = dict(
            
            n=Input(ids.CALCULATE_BUTTON, "n_clicks"),
  
            impact = dict(
                SEL =       State({'sourceType':ids.IMPACT, 'parameter':ids.SEL, "index": ALL}, "value"),
#                PEAK =      State({'sourceType':ids.IMPACT, 'parameter':ids.PEAK, "index": ALL}, "value"),
#                RMS =       State({'sourceType':ids.IMPACT, 'parameter':ids.RMS, "index": ALL}, "value"),
                RANGE =     State({'sourceType':ids.IMPACT, 'parameter':ids.RANGE, "index": ALL}, "value"),
                NPILES =    State({'sourceType':ids.IMPACT, 'parameter':ids.NPILES, "index": ALL}, "value"),
                NSTRIKES =  State({'sourceType':ids.IMPACT, 'parameter':ids.NSTRIKES, "index": ALL}, "value"),
                WF =        State({'sourceType':ids.IMPACT, 'parameter':ids.WF, "index": ALL}, "value"),
                F =         State({'sourceType':ids.IMPACT, 'parameter':ids.F, "index": ALL}, "value"),
            ),
            DTH = dict(
                SEL =       State({'sourceType':ids.DTH, 'parameter':ids.SEL, "index": ALL}, "value"),
#                PEAK =      State({'sourceType':ids.DTH, 'parameter':ids.PEAK, "index": ALL}, "value"),
#                RMS =       State({'sourceType':ids.DTH, 'parameter':ids.RMS, "index": ALL}, "value"),
                RANGE =     State({'sourceType':ids.DTH, 'parameter':ids.RANGE, "index": ALL}, "value"),
                NPILES =    State({'sourceType':ids.DTH, 'parameter':ids.NPILES, "index": ALL}, "value"),
                RATE =      State({'sourceType':ids.DTH, 'parameter':ids.RATE, "index": ALL}, "value"),
                TIME =      State({'sourceType':ids.DTH, 'parameter':ids.TIME, "index": ALL}, "value"),
                WF =        State({'sourceType':ids.DTH, 'parameter':ids.WF, "index": ALL}, "value"),
                F =         State({'sourceType':ids.DTH, 'parameter':ids.F, "index": ALL}, "value"),
            ),

            vibratory= dict(
                RMS =       State({'sourceType':ids.VIBRATORY, 'parameter':ids.RMS, "index": ALL}, "value"),
                RANGE =     State({'sourceType':ids.VIBRATORY, 'parameter':ids.RANGE, "index": ALL}, "value"),
                NPILES =    State({'sourceType':ids.VIBRATORY, 'parameter':ids.NPILES, "index": ALL}, "value"),
                TIME =      State({'sourceType':ids.VIBRATORY, 'parameter':ids.TIME, "index": ALL}, "value"),
                WF =        State({'sourceType':ids.VIBRATORY, 'parameter':ids.WF, "index": ALL}, "value"),
                F =         State({'sourceType':ids.VIBRATORY, 'parameter':ids.F, "index": ALL}, "value"),
                ),
            #WF = State(ids.WF_INPUT, "value"),
            #F  = State(ids.F_INPUT, "value")
                
                
            )   
    )
    def calc_results(n,impact,DTH,vibratory):
        if n is None:
            return [html.Div()]
        else:
            print('button clicked')
            try:
                inDiv = processInputs(impact, DTH, vibratory)
                
            except:
                inDiv = html.Div('error processing inputs')
                print(traceback.format_exc())
            finally:
                return [html.Div(inDiv)]
                
            #return [html.Div(inDiv)]

    return html.Div(
        [
            dbc.Button("Calculate", id=ids.CALCULATE_BUTTON, n_clicks=0,class_name='button'),
            html.Div(id=ids.RESULTS_DIV)
        ]
    )
