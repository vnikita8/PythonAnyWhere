import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from pages import home

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
    Output('output_div', 'children'),
    Input("main_button", "n_clicks"),
    State('smoking', 'value'),
    State('IL1b', 'value'),
    State('TNF', 'value'),
)

def update_output(clicks, *kwargs):
    if clicks is not None:
        print(kwargs)
        return f"курение: {kwargs[0]}"
    else:
        return "Error"


#Обновление







@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)