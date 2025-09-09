import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

### Initialize the app
app = Dash(__name__, use_pages=True, title= "Insurance App")
server = app.server  # Expose the server variable for deployments

app.layout = html.Div([ 
    dbc.NavbarSimple(
        className= "NavBar",
        children= [ 
            dbc.NavLink("Home", href="/", active= "exact", className="navitem"),
            dbc.NavLink("Insurance Map", href="/Insurance2", active= "exact", className="navitem"),
            dbc.NavLink("Insurance Graph", href="/Insurance3", active= "exact", className="navitem")
        ]),
    dash.page_container
], id="navigation")

if __name__ == "__main__":
    app.run(debug=True)
