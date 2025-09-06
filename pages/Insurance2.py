# This page will construct a U.S.-based map displaying property insurance loss ratio as a function of zip code.
# Loss ratios will be displayed on a color scale. Loss rations of over >=100%, indicating a financial loss, will be uniform on a separate, striking color.
# The map will be adjustable by year.
# The map may be adjustable between displaying zip codes vs states. 

# Libraries
import pandas as pd
from dash import Input, Output, callback, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import plotly.express as px

# Raw dataset
insurance = pd.read_excel("data/Insurance.xlsx", dtype={"ZIP Code":str}, sheet_name=2)

# Useable datasets
# years for date selection
years = insurance['Year'].unique()
setUse = (insurance.loc[:,["ZIP Code", "Year", "Loss Ratio"]])
print(setUse["ZIP Code"].iloc[1])

# ZIP Code to states dictionaries from https://www.irs.gov/pub/irs-utl/zip_code_and_state_abbreviations.pdf

states_dict = {}
# Finish adding states. Fix return functions
x = 0
while x < 1:
	for i in list(range(350,353)) + list(range(354,370)):
		states_dict[str(i)] = "Alabama"
	for i in range(995,1000):
		states_dict[i] = "Alaska"
	for i in list(range(850,854)) + list(range(855,858)) + list(range(859, 861)) + list(range(863,866)):
		states_dict[i] = "Arizona"
	for i in range(716,730):
		states_dict[i] = "Arkansas"
	for i in list(range(900,909)) + list(range(910,929)) + list(range(930,962)):
		states_dict[i] = "California"
	for i in range(800,817):
		states_dict[i] = "Colorado"
	for i in range(197,200):
		states_dict[i] = "Delaware"
	for i in [200] + list(range(202,206)) + [569]:
		states_dict[i] = "Washington, DC"
	for i in list(range(320,340)) + [341, 342, 344, 346, 347, 349]:
		states_dict[i] = "Florida"
	for i in list(range(300,320)) + [398, 399]:
		states_dict[i] = "Georgia"
	for i in [967, 968]:
		states_dict[i] = "Hawaii"
	for i in range(832,839):
		states_dict[i] = "Idaho"
	for i in list(range(600,621)) + list(range(622,630)):
		states_dict[i] = "Illinois"
	for i in range(460,480):
		states_dict[i] = "Indiana"
	for i in list(range(500,517)) + list(range(520,529)):
		states_dict[i] = "Iowa"
	for i in [660,662,662] + list(range(664,680)):
		states_dict[i] = "Kansas"
	for i in range(400,428):
		states_dict[i] = "Kentucky"
	for i in [700,701] + list(range(703,709)) + list(range(710,715)):
		states_dict[i] = "Louisiana"
	for i in list(range(206,213)) + list(range(214,220)):
		states_dict[i] = "Maryland"
	for i in range(480,499):
		states_dict[i] = "Michigan"
	for i in [550,551] + list(range(553,568)):
		states_dict[i] = "Minnesota"
	for i in range(386,398):
		states_dict[i] = "Mississippi"
	for i in [630,631] + list(range(633,642)) + list(range(644,659)):
		states_dict[i] = "Missouri"
	for i in range(590,600):
		states_dict[i] = "Montana"
	for i in [680,681] + list(range(683,694)):
		states_dict[i] = "Nebraska"
	for i in [889,890,891] + [893,894,895] + [897,898]:
		states_dict[i] = "Nevada"
	for i in [870,871] + [873,874,875] + list(range(877,885)):
		states_dict[i] = "New Mexico"
	for i in range(100,150):
		states_dict[i] = "New York"
	for i in range(270,290):
		states_dict[i] = "North Carolina"
	for i in range(580,589):
		states_dict[i] = "North Dakota"
	for i in range(430,460):
		states_dict[i] = "Ohio"
	for i in [730,731] + list(range(734,742)) + list(range(743,750)):
		states_dict[i] = "Oklahoma"
	for i in range(970,980):
		states_dict[i] = "Oregon"
	for i in range(150,197):
		states_dict[i] = "Pennsylvania"
	for i in range(290,300):
		states_dict[i] = "South Carolina"
	for i in range(570,578):
		states_dict[i] = "South Dakota"
	for i in range(370,386):
		states_dict[i] = "Tennessee"
	for i in [733] + list(range(750,771)) + list(range(772,800)):
		states_dict[i] = "Texas"
	for i in range(840,848):
		states_dict[i] = "Utah"
	for i in [201] + list(range(220,247)):
		states_dict[i] = "Virginia"
	for i in list(range(980,987)) + list(range(988,995)):
		states_dict[i] = "Washington"
	for i in [530,531,532] + [534,535] + list(range(537,550)):
		states_dict[i] = "Wisconsin"
	for i in list(range(820,832)) + [834]:
		states_dict[i] = "Wyoming"
	states_dict = {str(key): value for key, value in states_dict.items()}
	x += 1

# CT, ME, NH, NJ, MA, RI, VT need special help because they start with 0
states_dict.update({
	"060":"Connecticut", "061:":"Connecticut", "062":"Connecticut", "063":"Connecticut", "064":"Connecticut","065":"Connecticut","066":"Connecticut","067":"Connecticut","068":"Connecticut","069":"Connecticut", #CT
	"039":"Maine","040":"Maine","041":"Maine","042":"Maine","043":"Maine","044":"Maine","045":"Maine","046":"Maine","047":"Maine","048":"Maine","049":"Maine", #ME
	"010":"Massachusetts","011":"Massachusetts","012":"Massachusetts","013":"Massachusetts","014":"Massachusetts","015":"Massachusetts","016":"Massachusetts","017":"Massachusetts","018":"Massachusetts","019":"Massachusetts","020":"Massachusetts","021":"Massachusetts","022":"Massachusetts","023":"Massachusetts","024":"Massachusetts","025":"Massachusetts","026":"Massachusetts","027":"Massachusetts","055":"Massachusetts", #MA
	"030":"New Hampshire", "031":"New Hampshire", "032":"New Hampshire","033":"New Hampshire","034":"New Hampshire","035":"New Hampshire","036":"New Hampshire","037":"New Hampshire","038":"New Hampshire", #NH
	"070":"New Jersey","071":"New Jersey","072":"New Jersey","073":"New Jersey","074":"New Jersey","075":"New Jersey","076":"New Jersey","077":"New Jersey","078":"New Jersey","079":"New Jersey","080":"New Jersey","081":"New Jersey","082":"New Jersey","083":"New Jersey","084":"New Jersey","085":"New Jersey","086":"New Jersey","087":"New Jersey","088":"New Jersey","089":"New Jersey", #NJ
	"005":"New York", #NY
	"028":"Rhode Island", "029":"Rhode Island", #RI
	"050":"Vermont","051":"Vermont","052":"Vermont","053":"Vermont","054":"Vermont","056":"Vermont","057":"Vermont","058":"Vermont","059":"Vermont" #VT
})

print(states_dict)

# Cutter helper to cut zip codes to 3 digits for reference
def cutter(zipCode):
	zipCode = str(zipCode[0:3]
	#zipCode = zipCode[0:3]
	return zipCode

print(cutter(setUse.iloc[2,0]))
states_dict[cutter(setUse.iloc[2,0])]

# Applying to setUse
setUse["state"] = setUse["ZIP Code"].apply(lambda row: states_dict[cutter(row["ZIP Code"])])

# Page Layout
layout =  html.Div([
    html.H1("Placeholder Title"),
    html.P("Placeholder Text"),
    html.Div(
        # Define input values
        dcc.Slider(id="mapYearSlider", className="slider",
                   min=years.min(),
                   max=years.max(),
                   step=1,
                   marks={str(year): year for year in years}),
        # Default False
        daq.ToggleSwitch(id="mapToggle", className="toggle", vertical=True),
        dcc.Graph(id="mapDisplay")
    )
])

# Callbacks: Year slider, state/zip code toggle
@callback(
    Output("mapDisplay", "figure"),
    [Input("mapYearSlider", "value"),
     Input("mapToggle", "value")]
)
def 

# Function: 
# If mapYearSlider == Year, display that year
# if mapToggle == False, display zip code map;
# else display states map