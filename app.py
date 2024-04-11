import os
from dash import html, Input, Output, dash_table, callback, dcc, State, Dash


def layout():
    layout = html.Div([
        html.Br(),
        html.H1("TEST IP WEBSITE", style={"textAlign": "center"}),
        html.Br(),
        html.H3("TEST Successful!", style={"textAlign": "center", 'color': 'green'})
    ])
    return layout


app = Dash()
app.layout = layout()

server = app.server


if __name__ == '__main__':
    # LOCAL RUN
    if os.getenv('AWS_EXECUTION_ENV') is None:
        app.run_server(debug=True)
    else:
        app.run_server(host='0.0.0.0', port=8050)