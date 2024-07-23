import pandas as pd
import plotly.express as px

# Define the path to the Excel file
file_path = 'combined_city_data_format1.xlsx'  # Update with your file path

# Read the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
except Exception as e:
    print(f"Error reading the Excel file: {e}")

# Inspect the data to ensure it was read correctly
print(df.head())

# Select the country to display
country_to_display = 'Washington, D.C., USA'

# Filter the DataFrame to include only the selected country and years from 1990 to 2022
columns_to_keep = ['Year', country_to_display]
df_filtered = df[columns_to_keep]
df_filtered = df_filtered[(df_filtered['Year'] >= 1990) & (df_filtered['Year'] <= 2022)]

# Rename the columns for clarity
df_filtered.columns = ['Year', 'Pollution Level']

# Convert Year to string for proper animation frame handling
df_filtered['Year'] = df_filtered['Year'].astype(str)

# Debug: Print the first few rows of the filtered DataFrame
print(df_filtered.head())

# Create the horizontal bar chart with color intensity based on Pollution Level
fig = px.bar(df_filtered,
             x='Pollution Level',
             y='Year',
             color='Pollution Level',
             orientation='h',
             title=f'Air Pollution Levels in {country_to_display} Over Time',
             color_continuous_scale='Viridis',
             labels={'Pollution Level': 'Air Pollution Level'},
             range_x=[0, df_filtered['Pollution Level'].max() + 10])

# Customize the layout to fill the entire window
fig.update_layout(
    xaxis_title='Air Pollution Level',
    yaxis_title='Year',
    legend_title='Pollution Level',
    template='plotly_white',
    yaxis={'categoryorder':'total ascending'},
    width=1000,
    height=600
)

# Customize the bar size and remove the margin
fig.update_traces(marker_line_width=0, marker_line_color='rgb(8,48,107)')
fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

# Show the plot
fig.show()

# Save the plot as an HTML file
fig.write_html('/mnt/data/air_pollution_single_country_bar_chart.html')
