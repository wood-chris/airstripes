import plotly.figure_factory as ff
import pandas as pd

scope = "North America"

# Define the list of 4 countries in North America
selected_countries = {
    'North America': ['Washington, D.C., USA', 'Ottawa, Canada', 'Mexico City, Mexico', 'Havana, Cuba'],
}



# Read the Excel file into a DataFrame
file_path = 'combined_city_data_format1.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

#df new
df_new = df[df['STNAME'].isin(scope)]

#list values
values = df_new['TOT_POLL'].tolist()
fips = df_new['FIPS'].tolist()

colorscale = ["#2daa4b", "#80b1d3", "#fdb462", "#b3de69", "fccde5", "ff0000", "cce6f4", "#80bld3", 
              "#fdb462", "#b3de69", "#fccde5", "#9ba991", "#604d74",]

fig = ff.create_choropleth(
      fips=fips, values=values, scope=scope, colorscale=colorscale,  
      round_legend_values=True, simplify_county=0, simplify_state=0,
      county_outline={'color': 'rgb(15,15,55)', width : 0.5},

    Legend_title='Areas within North America Highest Polution',
    title='North America')

iplot(fig, filename='My Map Creation')

