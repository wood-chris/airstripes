import pandas as pd
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

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

year = 1950
colours = df_long.groupby("Year")["Color"].apply(list)[year]
rgba_col = []
for colour in colours:
    if colour == "blue":
        rgba_col.append([0,0,1,random.uniform(0.5,1)])
    elif colour == "green":
        rgba_col.append([0,1,0,random.uniform(0.5,1)])
    elif colour == "red":
        rgba_col.append([1,0,0,random.uniform(0.5,1)])
    elif colour == "orange":
        rgba_col.append([1,0.4,0,random.uniform(0.5,1)])
    elif colour == "purple":
        rgba_col.append([1,0.2,1,random.uniform(0.5,1)])
    elif colour == "pink":
        rgba_col.append([1,0.1,0.4,random.uniform(0.5,1)])
exp = [0.05 for x in range(len(rgba_col)) ]


fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    ax.axis('equal')
    pollution = df_long.groupby("Year")["Pollution Level"].apply(list)[frame]
    names = df_long.groupby("Year")["Country"].apply(list)[frame]
    ax.pie(pollution, labels=names, colors=rgba_col, explode=exp)
    ax.set_title(frame)

ani = FuncAnimation(fig, update, frames=range(1950,2023), repeat=False)
plt.show()