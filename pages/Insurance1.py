import dash 
from dash import html 

dash.register_page(__name__, path="/") # establishing that this is the home page 

layout=html.Div([
    html.H2("US Homeowners Insurance Markets Home"),
    html.P("Looking at the data from 2018 - 2022")
])

# Adding a callback here 
    # Can add: button clicks, sliders, "children", etc. 

@callback(
    Output("", ""),
    Input("", "")
    
)

# adding def and if statment here too
