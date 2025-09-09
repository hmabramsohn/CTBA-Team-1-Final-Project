import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

### Initialize the app
app = Dash(__name__, use_pages=True, title= "Insurance App")
server = app.server  # Expose the server variable for deployments

app.layout = html.Div([ 
    dbc.NavbarSimple(
        fluid = True,
        id = "NavBar",
        children= [ 
            dbc.NavLink("Home", href="/", active= "exact"),
            dbc.NavLink("Insurance Map", href="/Insurance2", active= "exact"),
            dbc.NavLink("Insurance Graph", href="/Insurance3", active= "exact")
        ]), 
    #brand = "Insurance App"),
    dash.page_container
])

if __name__ == "__main__":
    app.run(debug=True)
