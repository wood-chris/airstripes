import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
file_path = 'combined_city_data_format1.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

# Define the list of 4 countries from each continent
selected_countries = {
    'North America': ['Washington, D.C., USA', 'Ottawa, Canada', 'Mexico City, Mexico', 'Havana, Cuba']
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
    'North America': 'blue'
}

# Create a mapping of countries to their respective colors
country_to_continent = {country: continent for continent, countries in selected_countries.items() for country in countries}
df_long['Continent'] = df_long['Country'].map(country_to_continent)
df_long['Color'] = df_long['Continent'].map(colors)


pollution = df_long.groupby("Year")["Pollution Level"].apply(list)[2000]
names = df_long.groupby("Year")["Country"].apply(list)[2000]
plt.pie(pollution, labels=names)
plt.show()
#print("boo")
