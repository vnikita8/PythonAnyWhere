import dash_core_components as dcc
import dash_html_components as html



style_for_block = {'display':"flex", "align-items": "center", "gap": 10}
style_for_DropDown = {"width": 85}
style_for_MainButton = {"width": 100}


layout = html.Div([
    html.H1('Кафедра Генетики Кемеровского государственного университета'),
    
    #Блок с курением
    html.Div([
        html.P('Курение:'),
        dcc.Dropdown(["Да", "Нет"],"Нет", style=style_for_DropDown, id="smoking")
    ], style=style_for_block),

    #Блоки с генами 
    html.Div([
        html.P('IL1b:'),
        dcc.Dropdown(["T/T", "T/C","C/C"],"T/T", style=style_for_DropDown, id="IL1b")
    ], style=style_for_block),
    html.Div([
        html.P('TNF:'),
        dcc.Dropdown(["G/G", "G/A", "A/A"],"G/G", style=style_for_DropDown, id="TNF")
    ], style=style_for_block),
    html.Div([
        html.P('APEX1:'),
        dcc.Dropdown(["G/G", "T/T", "T/G"],"G/G", style=style_for_DropDown, id="APEX1")
    ], style=style_for_block),
    html.Div([
        html.P('XPD:'),
        dcc.Dropdown(["T/G", "G/G", "T/T"],"T/G", style=style_for_DropDown, id="XPD")
    ], style=style_for_block),
    html.Div([
        html.P('EGFR:'),
        dcc.Dropdown(["A/A", "T/T", "A/T"],"A/A", style=style_for_DropDown, id="EGFR")
    ], style=style_for_block),
    html.Div([
        html.P('CHEK2:'),
        dcc.Dropdown(["N/P", "P/P", "N/N"],"N/P", style=style_for_DropDown, id="CHEK2")
    ], style=style_for_block),
    html.Div([
        html.P('TGFb1:'),
        dcc.Dropdown(["G/G", "G/C", "C/C"],"G/G", style=style_for_DropDown, id="TGFb1")
    ], style=style_for_block),
    html.Div([
        html.P('EPHX1:'),
        dcc.Dropdown(["T/T", "T/C", "C/C"],"T/T", style=style_for_DropDown, id="EPHX1")
    ], style=style_for_block),

    html.Button("Прогноз..", n_clicks=0, id="main_button", style=style_for_MainButton),
    html.Div(id="output_str", children='Enter a value and press submit')
], style={"align-items": "center"})


