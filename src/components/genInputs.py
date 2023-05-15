# -*- coding: utf-8 -*-
"""
Created on Sat May 13 15:38:22 2023

@author: jim
"""

from dash import Dash, dcc, html,State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from . import ids, sourceConfigInput





def render(app: Dash) -> html.Div:
   

    return html.Div(
        className="app-div",
        children=[
            html.H4(f'General Inputs'),
            html.Hr(),
            html.Div(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Weighting Frequency"),
                        dbc.Input(value="2.0", type="number",id=ids.WF_INPUT),
                        dbc.InputGroupText("KHz"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("TL"),
                        dbc.Input(value="15", type="number",id=ids.F_INPUT),
                        dbc.InputGroupText("dB"),
                    ],
                    className="mb-3",
                    )
               
            ]
        )

            

        ],
    )