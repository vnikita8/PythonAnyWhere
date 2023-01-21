import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app
from pages import home
from ai import AI_Help

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/home' or pathname == '/':
        return home.layout
@app.callback(
    Output('output_str', 'children'),
    Output('output_accuracy', 'children'),
    Input("main_button", "n_clicks"),
    State('smoking', 'value'),
    State('IL1b', 'value'),
    State('TNF', 'value'),
    State('APEX1', 'value'),
    State('XPD', 'value'),
    State('EGFR', 'value'),
    State('CHEK2', 'value'),
    State('TGFb1', 'value'),
    State('EPHX1', 'value')
)

def update_output(clicks, *kwargs):
    if clicks is not None or clicks != 0:
        smoking = "н" if kwargs[0]=="Нет" else "к"
        helper = AI_Help(smoking, kwargs[1], kwargs[2], kwargs[3], kwargs[4], kwargs[5], kwargs[6], kwargs[7], kwargs[8])
        result = helper.go_train()
        res_str = "имеется предрасположенность к раку" if result[0] == 1 else "предрасположенности к раку нет"
        return [f"Результат: {res_str}", f"Точность: {result[1]}"]
    else:
        return "Error"



if __name__ == '__main__':
    app.run_server(debug=True)