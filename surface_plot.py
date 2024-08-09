import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

file_path = 'combined_city_data_format1.xlsx'  # Update with your file path
df = pd.read_excel(file_path)

selected_countries = {
    'North America': ['0', '1', '2', '', '3'],
}


# Flatten the list of selected countries
flat_list = [country for sublist in selected_countries.values() for country in sublist]

# Filter the DataFrame to include only the selected countries
columns_to_keep = ['Year'] + flat_list
df = df[columns_to_keep]

# Convert the DataFrame from wide format to long format
df_long = pd.melt(df, id_vars=['Year'], value_vars=flat_list,
                  var_name='Country', value_name='Pollution Level')

print(df_long)

fig = px.scatter(df_long
                  )

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=4, range=[0,3],
                     title = "Country"),
                     yaxis = dict(nticks=4, range=[1950, 2022],
                                  title = "Year"),
                     zaxis = dict(nticks=4, range=[0,100],
                                  title = "Pollution Levels"),),
    width=700,
    margin=dict(r=20, l=80, b=10, t=10))




# Display the animation
fig.show()




fig.show()