import dash 
from dash import html, dcc, Input, Output, callback, no_update
import dash_labs

# Ethiana Hacsh 

dash_labs.plugins.register_page(__name__, path="/Insurance1") # establishing that this is the home page 

layout=html.Div([
    html.H2("US Homeowners Insurance Markets Home"),
    html.P("Looking at the data from 2018 - 2022"),
    html.Button("View Insurance2.py", id="btn-1", n_clicks=0), #pulled from page2.py notes
    html.Button("View Insurance3.py", id="btn-2", n_clicks=0),
    dcc.Location(id="url") # AI help used on 9/8/2025 # gives an ID to target within the callbacks and can change the url. Like a router anchor
]) 


# Adding a button
@callback(
    Output("url", "href"),
    [Input("btn-1", "n_clicks"),
    Input("btn-2", "n_clicks")] # got from NasaWCallbacks 
)
def navigate(btn1, btn2):
    if btn1:
        return "/Insurance2"
    if btn2:
        return "/Insurance3"
    else:
        return no_update #AI used on 9/8/2025 # keeping the page stable if no action is needed. Nothing clicked and URL is not changed. Tells Dash to keep the current value
        

# compare with hers on github

# add any AI assistnace comment block in code

