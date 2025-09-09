# CTBA-Team-1-Final-Project

Project Overview: 
    This project is a multipage dash website that looks at data about property insurance between 2018-2022. We are specifically looking at loss ratios, premiums per policy, and policy decile grouping. We do this through the use of a map showing loss ratios between states and a bar graph which looks at mean premium per policy by state. There are a variety of factors that go into evaluating insurance. Although this is a challenge for insurance professionals, the benefit of this type of data is that is breaks down any potential problems by state. Breaking this down by state saves the insurance companies time and money, it is efficient. This content is geared toward a potential insurance executive. This data would help an insurance professional strategize, analyze and develop better suited plans for deploying insurance. This is valuable becuase it might help insurance companies in evaluating which states are most profitable and how to target them. 

How to run it: Local & Deploy Notes: VS Code
All code should run through the InsuranceApp.py and create a link to our website in the terminal.

How to run it: Local & Deploy Notes: Render 
All pages should be connected to an external URL. No additional running is needed. 


Data Sources & Data Dictionary: (explain what your variables and why you chose them)
The data source is labeled: "Supporting Underlying Metrics and Disclaimer for Analyses of US Homeowners Insurance Markets 2018-20". It is the only data source that we used in this multipage dash website. The variables we used are: Paid Loss ratio, premium per policy, policy decile grouping, zip code and year. Below are definitions of the variables: 
    
Paid Loss Ratio: The amount insurers have paid on claims to or on behalf of policyholders relative to premiums received and helps assess insurers’ underwriting profitability.Sustained high paid loss ratios may lead insurers to request rate increases, change policy terms and conditions, decide not to renew policies, or exit a market entirely.  Thus, years with high paid loss ratios may precede changes in availability and cost. (directly from data source)

Premium Per Policy: The average cost of a policy.  Premiums may be related to a number of factors, such as climate-related risk, inflation, costs of reconstruction, and reinsurance, as discussed in Section III.B.(directly dfrom data source)

Policy decile grouping: ranking insurance. Breaks up the policy into 10 groups (in our data) therfore each decile will have 10% of the data. 1st decile contains the policy hodler with the lowest risk profile and 10th decile contains the policy holder with the highest risk profile. 


List all of the packages used: 
dash, html, dcc, Input, Output, callback no_update, register_page, pandas, dash_bootstrap, dash_components, dash_daq, plotly.express

AI Disclosure:
main app:
pulled directly from in class notes. 
No AI used 
    
main page: used ChatGPT for two lines of code
code line: "dcc.Location(id="url",refresh=False)". Asked AI how to use dcc to link as a location for the URL in the main app. 
    
page w/ Insurance2: 
used only for debugging and checking errors, not to generate code
    
page w/ Insurance3:
used for debugging and checking errors 
used in the callbacks for updated the graph for selected year and selected decile 
used for calculating the mean for premium per policy
used to filter year and decile
used to find fig.update_yaxes




