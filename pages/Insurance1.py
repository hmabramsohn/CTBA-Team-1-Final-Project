# Ethiana Hacsh 
# Import libraries
import dash 
from dash import html, dcc, Input, Output, callback, no_update, register_page

# Register Homepage
register_page(__name__, path="/") 

# Establishing page layout and navigational button functionality
layout=html.Div(className="wrap", children=[
    html.H2("US Homeowners Insurance Information"),
    html.P("Loss Ratio by State and Premiums by Policy Group from 2018-2022", id="mainText")
]) 