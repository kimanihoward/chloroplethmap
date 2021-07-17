import pandas as pd
import plotly.graph_objs as go
# Read Data
df = pd.read_csv("covid_19_data.csv")
# Rename columns
df = df.rename(columns={'Country/Region':'Country'})
df = df.rename(columns={'ObservationDate':'Date'})
# Manipulate Dataframe
df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed']>0]
# Create the Choropleth

fig = go.Figure(data=go.Choropleth(
    locations = df_countries['Country'],
    locationmode = 'country names',
    z = df_countries['Confirmed'],
    colorscale = 'Reds'
    
))
# Manipulating the original dataframe

# Creating the visualization

fig.update_layout(
    title_text='date,county,state,fips,cases,deaths',
    title_x=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=False,
    ))

fig.show()