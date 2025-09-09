# CTBA-Team-1-Final-Project

Project Overview: 
    This project is a multipage dash website that looks at data about property insurance between 2018-2022. We are specifically looking at loss ratios, premiums per policy, and policy decile grouping. We do this through the use of a map comparing loss ratios between states and a bar graph which looks at mean premium per policy by state. There are a variety of factors that go into evaluating insurance. Grouping summary statistics by state helps insurance professionals to strategize, analyze and develop better suited business plans. These maps can help insurance companies evauluate which states are most profitable and, if combined with a hitorical analysis, derive some factors of large-scale profitability. 

How to run it:

Run InsuranceApp.py after installing all required packages. Access the local site through the terminal.

Data Sources & Data Dictionary: 

The data source, from the U.S. Treasury Department, is labeled: "Supporting Underlying Metrics and Disclaimer for Analyses of US Homeowners Insurance Markets 2018-20". A link to the dataset can be found on this page: https://home.treasury.gov/news/press-releases/jy2791. The variables we used are: Paid Loss Ratio, Premium per Policy, Policy Decile Grouping, Zip Code and Year. Below are definitions of the variables: 
    
Paid Loss Ratio: The amount insurers have paid on claims to or on behalf of policyholders relative to premiums received and helps assess insurers’ underwriting profitability.Sustained high paid loss ratios may lead insurers to request rate increases, change policy terms and conditions, decide not to renew policies, or exit a market entirely.  Thus, years with high paid loss ratios may precede changes in availability and cost. (directly from data source)

Premium Per Policy: The average cost of a policy.  Premiums may be related to a number of factors, such as climate-related risk, inflation, costs of reconstruction, and reinsurance, as discussed in Section III.B.(directly from data source)

Policy Decile Grouping: ranking insurance. Breaks up the policy into 10 groups (in our data) therfore each decile will have 10% of the data. 1st decile contains the policy hodler with the lowest risk profile and 10th decile contains the policy holder with the highest risk profile. 

List all of the packages used: 
dash, html, dcc, Input, Output, callback, no_update, register_page, pandas, dash_bootstrap, dash_components, dash_daq, plotly.express

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
used for finding function to calculate the mean for premium per policy
used to format the function to filter year and decile
used to find fig.update_yaxes