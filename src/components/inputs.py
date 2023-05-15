# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:18:26 2023

@author: jim
"""

from dash import Dash, dcc, html,State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from . import ids

def buildImpactDiv(i)->html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H4(f'Source {i+1}: Impact'),
            html.Hr(),
            html.Div(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("SELss"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_SEL, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa2s)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Lpeak"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_PEAK, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Lrms"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_RMS, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Range of source levels"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_RANGE, "index": i}),
                        dbc.InputGroupText("meters"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Number of Piles"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_NPILES, "index": i}),
                        dbc.InputGroupText("#"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Strikes per pile"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.IMPACT_INPUT_NSTRIKES, "index": i}),
                        dbc.InputGroupText("#"),
                    ],
                    className="mb-3",
                ),

            ]
        )

            

        ],
    )

def buildVibDiv(i)->html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H4(f'Source {i+1}: Vibratory'),
            html.Hr(),
            html.Div(
            [
               
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Lrms"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.VIBRATORY_INPUT_RMS, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Range of source levels"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.VIBRATORY_INPUT_RANGE, "index": i}),
                        dbc.InputGroupText("meters"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Number of Piles"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.VIBRATORY_INPUT_NPILES, "index": i}),
                        dbc.InputGroupText("#"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Time per pile"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.VIBRATORY_INPUT_TIME, "index": i}),
                        dbc.InputGroupText("Min."),
                    ],
                    className="mb-3",
                ),

            ]
        )

            

        ],
    )

def buildDTHDiv(i)->html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H4(f'Source {i+1}:DTH'),
            html.Hr(),
            html.Div(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("SELss"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_SEL, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa2s)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Lpeak"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_PEAK, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Lrms"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_RMS, "index": i}),
                        dbc.InputGroupText("dB (rel 1 uPa)"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Range of source levels"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_RANGE, "index": i}),
                        dbc.InputGroupText("meters"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Number of Piles"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_NPILES, "index": i}),
                        dbc.InputGroupText("#"),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Time per pile"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_TIME, "index": i}),
                        dbc.InputGroupText("Min."),
                    ],
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Strike Rate"),
                        dbc.Input(placeholder="-", type="number",id={"type": ids.DTH_INPUT_RATE, "index": i}),
                        dbc.InputGroupText("Per Second"),
                    ],
                    className="mb-3",
                ),

            ]
        )

            

        ],
    )



def buildInputDiv(types)->html.Div:
    cols = []
    for i,t in enumerate(types):
        if t=='Impact':
            cols.append(dbc.Col(buildImpactDiv(i)))
        if t=='Vibratory':
            cols.append(dbc.Col(buildVibDiv(i)))
        if t=='DTH':
            cols.append(dbc.Col(buildDTHDiv(i)))
    return html.Div(dbc.Row(cols))


def render(app: Dash) -> html.Div:
   


    return html.Div(id=ids.INPUTS_DIV)
      