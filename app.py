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


if __name__ == '__main__':
    app.run_server(debug=True)