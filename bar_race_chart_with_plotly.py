import pandas as pd
import plotly.express as px

# Read the Excel file into a DataFrame
file_path = 'combined_city_data_format1.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

# Define the list of 4 countries from each continent
selected_countries = {
    'North America': ['Washington, D.C., USA', 'Ottawa, Canada', 'Mexico City, Mexico', 'Havana, Cuba'],
    'Europe': ['London, United Kingdom', 'Berlin, Germany', 'Paris, France', 'Rome, Italy'],
    'Asia': ['Hangzhou, China', 'Delhi, India', 'Tokyo, Japan', 'Seoul, South Korea'],
    'South America': ['Brasília, Brazil', 'Buenos Aires, Argentina', 'Santiago, Chile', 'Bogotá, Colombia'],
    'Africa': ['Pretoria, South Africa', 'Abuja, Nigeria', 'Cairo, Egypt', 'Nairobi, Kenya'],
    'Oceania': ['Sydney, Australia', 'Wellington, New Zealand', 'Suva, Fiji', 'Nukuʻalofa, Tonga']
}


# Flatten the list of selected countries
flat_list = [country for sublist in selected_countries.values() for country in sublist]

# Filter the DataFrame to include only the selected countries
columns_to_keep = ['Year'] + flat_list
df = df[columns_to_keep]

# Convert the DataFrame from wide format to long format
df_long = pd.melt(df, id_vars=['Year'], value_vars=flat_list,
                  var_name='Country', value_name='Pollution Level')

# Define colors for each continent
colors = {
    'North America': 'blue',
    'Europe': 'green',
    'Asia': 'red',
    'South America': 'purple',
    'Africa': 'orange',
    'Oceania': 'pink'
}

# Create a mapping of countries to their respective colors
country_to_continent = {country: continent for continent, countries in selected_countries.items() for country in countries}
df_long['Continent'] = df_long['Country'].map(country_to_continent)
df_long['Color'] = df_long['Continent'].map(colors)

# Create the animated bar chart race
fig = px.line(df_long,
             x='Year',
             y='Pollution Level',
             color='Continent',
             animation_frame='Country',
             animation_group='Year',
             range_x=[df_long['Year'].min(), df_long['Year'].max()],
             range_y=[0, df_long['Pollution Level'].max() + 5],
             color_discrete_map=colors,

             title='Air Pollution Levels Over Time')

fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})

# Display the animation
fig.show()

# Save the animation to an HTML file
fig.write_html('../racechart.html')
