# Harrison Abramsohn

# This page will construct a U.S.-based map displaying property insurance loss ratio as a function of zip code.
# Loss ratios will be displayed on a color scale. Loss rations of over >=100%, indicating a financial loss, will be uniform on a separate, striking color.
# The map will be adjustable by year.
# The map may be adjustable between displaying zip codes vs states. 

# NEEDS
# Add error handling to functions
# Requirements.txt

# Libraries
import pandas as pd
from dash import Input, Output, callback, html, dcc, Dash, register_page
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.express as px
import dash_labs

# For local testing
#app = Dash(__name__)
register_page(__name__, path="/Insurance2")

# Raw dataset
insurance = pd.read_excel("data/Insurance.xlsx", dtype={"ZIP Code":str}, sheet_name=2)

# Useable datasets
# years for date selection
years = insurance['Year'].unique()
years = [str(year) for year in years]

# filtered setUse for useful variables
setUse = (insurance.loc[:,["ZIP Code", "Year", "Loss Ratio"]])

# ZIP Code to states dictionaries taken from https://www.irs.gov/pub/irs-utl/zip_code_and_state_abbreviations.pdf

# Creating a dictionary to later assign to our DataFrame.
states_dict = {}
# This loop assigns a range of three-digit numbers, representing the highest level zip code, to every U.S. state except some exceptions.
x = 0
while x < 1:
	for i in list(range(350,353)) + list(range(354,370)):
		states_dict[str(i)] = "AL"
	for i in range(995,1000):
		states_dict[i] = "AK"
	for i in list(range(850,854)) + list(range(855,858)) + list(range(859, 861)) + list(range(863,866)):
		states_dict[i] = "AZ"
	for i in range(716,730):
		states_dict[i] = "AR"
	for i in list(range(900,909)) + list(range(910,929)) + list(range(930,962)):
		states_dict[i] = "CA"
	for i in range(800,817):
		states_dict[i] = "CO"
	for i in range(197,200):
		states_dict[i] = "DE"
	for i in [200] + list(range(202,206)) + [569]:
		states_dict[i] = "DC"
	for i in list(range(320,340)) + [341, 342, 344, 346, 347, 349]:
		states_dict[i] = "FL"
	for i in list(range(300,320)) + [398, 399]:
		states_dict[i] = "GA"
	for i in [967, 968]:
		states_dict[i] = "HI"
	for i in range(832,839):
		states_dict[i] = "ID"
	for i in list(range(600,621)) + list(range(622,630)):
		states_dict[i] = "IL"
	for i in range(460,480):
		states_dict[i] = "IN"
	for i in list(range(500,517)) + list(range(520,529)):
		states_dict[i] = "IA"
	for i in [660,661,662] + list(range(664,680)):
		states_dict[i] = "KS"
	for i in range(400,428):
		states_dict[i] = "KY"
	for i in [700,701] + list(range(703,709)) + list(range(710,715)):
		states_dict[i] = "LA"
	for i in list(range(206,213)) + list(range(214,220)):
		states_dict[i] = "MD"
	for i in range(480,500):
		states_dict[i] = "MI"
	for i in [550,551] + list(range(553,568)):
		states_dict[i] = "MN"
	for i in range(386,398):
		states_dict[i] = "MS"
	for i in [630,631] + list(range(633,642)) + list(range(644,659)):
		states_dict[i] = "MO"
	for i in range(590,600):
		states_dict[i] = "MT"
	for i in [680,681] + list(range(683,694)):
		states_dict[i] = "NE"
	for i in [889,890,891] + [893,894,895] + [897,898]:
		states_dict[i] = "NV"
	for i in [870,871] + [873,874,875] + list(range(877,885)):
		states_dict[i] = "NM"
	for i in range(100,150):
		states_dict[i] = "NY"
	for i in range(270,290):
		states_dict[i] = "NC"
	for i in range(580,589):
		states_dict[i] = "ND"
	for i in range(430,460):
		states_dict[i] = "OH"
	for i in [730,731] + list(range(734,742)) + list(range(743,750)):
		states_dict[i] = "OK"
	for i in range(970,980):
		states_dict[i] = "OR"
	for i in range(150,197):
		states_dict[i] = "PA"
	for i in range(290,300):
		states_dict[i] = "SC"
	for i in range(570,578):
		states_dict[i] = "SD"
	for i in range(370,386):
		states_dict[i] = "TN"
	for i in [733] + list(range(750,771)) + list(range(772,800)):
		states_dict[i] = "TX"
	for i in range(840,848):
		states_dict[i] = "UT"
	for i in [201] + list(range(220,248)):
		states_dict[i] = "VA"
	for i in range(247, 269):
		states_dict[i] = "WV"
	for i in list(range(980,987)) + list(range(988,995)):
		states_dict[i] = "WA"
	for i in [530,531,532] + [534,535] + list(range(537,550)):
		states_dict[i] = "WI"
	for i in list(range(820,832)) + [834]:
		states_dict[i] = "WY"
	states_dict = {str(key): value for key, value in states_dict.items()}
	x += 1

# CT, ME, NH, NJ, MA, RI, and VT must be hardcoded in this scenario as their zip codes begin with 0.
states_dict.update({
	"060":"CT","061":"CT","062":"CT","063":"CT","064":"CT","065":"CT","066":"CT","067":"CT","068":"CT","069":"CT", #CT
	"039":"ME","040":"ME","041":"ME","042":"ME","043":"ME","044":"ME","045":"ME","046":"ME","047":"ME","048":"ME","049":"ME", #ME
	"010":"MA","011":"MA","012":"MA","013":"MA","014":"MA","015":"MA","016":"MA","017":"MA","018":"MA","019":"MA","020":"MA","021":"MA","022":"MA","023":"MA","024":"MA","025":"MA","026":"MA","027":"MA","055":"MA", #MA
	"030":"NH","031":"NH","032":"NH","033":"NH","034":"NH","035":"NH","036":"NH","037":"NH","038":"NH", #NH
	"070":"NJ","071":"NJ","072":"NJ","073":"NJ","074":"NJ","075":"NJ","076":"NJ","077":"NJ","078":"NJ","079":"NJ","080":"NJ","081":"NJ","082":"NJ","083":"NJ","084":"NJ","085":"NJ","086":"NJ","087":"NJ","088":"NJ","089":"NJ", #NJ
	"005":"NY", #NY
	"028":"RI","029":"RI", #RI
	"050":"VT","051":"VT","052":"VT","053":"VT","054":"VT","056":"VT","057":"VT","058":"VT","059":"VT" #VT
})


# This function cuts passed zip codes into the first 3 digits: the highest level zip code which determines state.
def cutter(zipCode):
	zipCode = str(zipCode[0:3])
	return zipCode

# This function assigns the cut zip code to a state in states_dict.
def assign(zipCode):
	try:
		zipCode = cutter(zipCode)
		state = states_dict[zipCode]
		return state
	except:
		return "Unknown"

# Applying to setUse
setUse["State"] = [assign(x) for x in setUse['ZIP Code']]
# Dropping "Unknowns"
setUse = setUse[setUse["State"] != "Unknown"]


# Page Layout
layout =  html.Div([
    html.H1("Mean Loss Ratio for Property Insurers per State From 2018-2022"),
    html.P(
        "Loss ratio is a financial indicator used by insurance companies comparing the amount earned in premiums to the amount paid out in claims. The first map shows the mean loss ratio by state for visual comparison between 2018-2022. The second map highlights states where property insurers paid out more in claims than they collected in premiums. Insurers, on average, lost money in these states."
        ),
    html.Div([
        # Define input values
        dcc.Slider(id="mapYearSlider", className="slider",
                   min=int(years[0]),
                   max=int(years[-1]),
                   step=None,
				   value=int(years[0]),
                   marks={year: year for year in years}),
        # Default False
        daq.ToggleSwitch(id="mapToggle", className="toggle", vertical=True, value=False),
        dcc.Graph(id="mapDisplay")
	])
])

# Callbacks: Year slider, scale/over 100% toggle
@callback(
    Output("mapDisplay", "figure"),
    [Input("mapYearSlider", "value"),
    Input("mapToggle", "value")]
)
def mapSet(mapYearSlider, mapToggle):
	setUseYearState = setUse[setUse['Year'] == mapYearSlider].groupby("State").mean("Loss Ratio").reset_index()
	setUseYearState["Loss Ratio"] = setUseYearState["Loss Ratio"] * 100
	if mapToggle == False:
		mapDisplay = px.choropleth(
			setUseYearState,
			locations = "State",
			locationmode = "USA-states",
			color = "Loss Ratio",
			scope = "usa",
			title = f"Map of US States Colored by Mean Loss Ratio for year {mapYearSlider}",
   			color_continuous_scale="hot_r",
			range_color=(0, 150)
			)
	else:
		setUseYearState["Financial Loss"] = setUseYearState["Loss Ratio"] > 100
		mapDisplay = px.choropleth(
			setUseYearState,
			locations = "State",
			locationmode = "USA-states",
			color = "Financial Loss",
			scope = "usa",
			title = f"Map Displaying States where Insurers Lost Money (Loss Ratio >100%) for Year {mapYearSlider}",
			color_continuous_scale="hot_r",
		)
	mapDisplay.update_layout(margin=dict(l=0, r=0, t=40, b=0))
	return mapDisplay

# For local testing
#if __name__ == "__main__":
#	app.run(debug=True)

# Function: 
# If mapYearSlider == Year, display that year
# if mapToggle == False, display relative scale map;
# else over 100% map