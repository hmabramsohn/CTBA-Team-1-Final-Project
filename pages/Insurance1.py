# Ethiana Hacsh 
# Import libraries
import dash 
from dash import html, dcc, Input, Output, callback, no_update, register_page

# Register Homepage
register_page(__name__, path="/") 

# Establishing page layout and navigational button functionality
layout=html.Div([
    html.H2("US Homeowners Insurance Markets Home"),
    html.P("Looking at the data from 2018 - 2022"),
    html.Button("View Insurance2.py", id="btn-1", n_clicks=0), #pulled from page2.py notes
    html.Button("View Insurance3.py", id="btn-2", n_clicks=0),
    dcc.Location(id="url",refresh=False) # AI help used on 9/8/2025 # gives an ID to target within the callbacks and can change the url. Like a router anchor
]) 

# Adding a button using Callback function
@callback(
    Output("url", "pathname"),
    [Input("btn-1", "n_clicks"),
    Input("btn-2", "n_clicks")] # got from NasaWCallbacks 
)
def navigate(btn1, btn2):
    if btn1 == 1:
        return "/Insurance2"
    elif btn2 == 1:
        return "/Insurance3"
    btn1 = 0
    btn2 = 0