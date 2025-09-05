#Importing Libraries
from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

register_page(__name__, path='/Insurance3', name='Premium per Policy (Mean)')

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "InsuranceData.csv"

df = pd.read_csv(DATA_PATH)

#Create the layout
layout = html.Div(
    id = "premium-page", className = "page premium-page",
    children=[
        html.H1("Mean Premium per Policy", className="page-title"),
        html.Div(
            id="controls", className="controls",
            children=[
                html.Label("Filter by State(s)", className="label"),
                dcc.Dropdown(
                    id="state-dropdown",
                    options=[{"label": s, "value": s} for s in sorted(df["state"].unique())],
                    value=None,
                    placeholder="Select state(s)",
                    multi=True,
                    clearable=True,
                    className="dropdown"
                ),
                
                html.Div(className="my-3"),

                html.Small(
                    "Data source: .",
                    className="text-muted",
                    ),
                html.Label("Year", className="label"),
                dcc.RangeSlider(
                    id="year-range",
                    min=int(df["year"].min()),
                    max=int(df["year"].max()),
                    value=int(df["year"].min()),
                    marks={str(y): str(y) for y in sorted(df["year"].unique())},
                    step=None,
                    tooltip={"placement": "bottom", "always_visible": True},
                    className="range-slider"
                ),
                html.Br(),
                dcc.Graph(id="premium-graph"),
            ],
        ),
    ],
)

##Callbacks
@callback(
    Output("premium-graph", "figure"),
    Input("state-dropdown", "value"),
    Input("year-range", "value"),
)
#might need to edit below
def update_graph(selected_states, selected_year):
    d = df[
        (df["state"].isin(selected_states)) &
        (df["year"] == selected_year)
    ]
    grouped = (
        d.groupby(["year", "state"], as_index=False)
        .agg(mean_premium=("premium_per_policy", "mean"), n = ("premium_per_policy", "size"))
        .sort_values(["state"])
    )
##can change chart type here (not sure if bar is best for this) - add hover data here?
    fig = px.bar(grouped, x="year",
                  y="mean_premium",
                  color="state",
                  markers=True,
                  color_discrete_sequence=px.colors.qualitative.Safe,
                  title=f"Mean Premium per Policy - {selected_year}",
                  labels={"mean_premium": "Mean Premium ($)", "Year": "Year", "State": "State"}
                  )
    fig.update_layout(
                      font_color="white",
                      yaxis_title="USD",
                      yaxis_tickprefix="$",
                      xaxis_title="None",
                      margin=dict(l=10, r=10, t=50, b=10))
    return fig
