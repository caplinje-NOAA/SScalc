import dash_bootstrap_components as dbc
from dash import Dash, html
from src.components import (
    sourceCanvas,
    inputs,
    results,
    genInputs

)


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    # year_dropdown.render(app, data),
                    # month_dropdown.render(app, data),
                    # category_dropdown.render(app, data),
                ],
            ),
            dbc.Row([
            dbc.Col(sourceCanvas.render(app)),
            dbc.Col(genInputs.render(app))
            ]),
            inputs.render(app),
            html.Hr(),
            results.render(app),
            

        ],
    )
