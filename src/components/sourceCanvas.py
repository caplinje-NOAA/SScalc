
from dash import Dash, dcc, html,State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


from . import ids, sourceConfigInput


card = dbc.Card(
    [

        dbc.CardBody(
            [
                html.H4("Current Configuration", className="card-title"),
                html.Div('None.',id=ids.CONFIG_DISPLAY),    
                dbc.Button("Configure Sources", id=ids.CONFIGURE_SOURCES_BUTTON, n_clicks=0,class_name='button'),
            ]
        ),
    ],
    style={"width": "18rem"},
)


def render(app: Dash) -> html.Div:
   
    @app.callback(
        Output(ids.CONFIGURE_SOURCES_CANVAS, "is_open"),
        Input(ids.CONFIGURE_SOURCES_BUTTON, "n_clicks"),
        [State(ids.CONFIGURE_SOURCES_CANVAS, "is_open")],
    )
    def toggle_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open

    return html.Div(
        [
            card,
            html.Hr(),
            dbc.Offcanvas(html.Div([
                    html.P("Configure the number and type of sources here."),                
            
                    sourceConfigInput.render(app)
                ]),    
                id=ids.CONFIGURE_SOURCES_CANVAS,
                title="Source Configuration",
                is_open=False,
            ),
        ]
    )
