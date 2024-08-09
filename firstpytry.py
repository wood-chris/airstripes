import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px

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


def bar_data(position3d, size=(1,1,1)):
    # position3d - 3-list or array of shape (3,) that represents the point of coords (x, y, 0), where a bar is placed
    # size = a 3-tuple whose elements are used to scale a unit cube to get a paralelipipedic bar
    # returns - an array of shape(8,3) representing the 8 vertices of  a bar at position3d
    
    bar = np.array([[0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [1, 0, 1],
                    [1, 1, 1],
                    [0, 1, 1]], dtype=float) # the vertices of the unit cube
   
    bar *= np.asarray(size)# scale the cube to get the vertices of a parallelipipedic bar
    bar += np.asarray(position3d) #translate each  bar on the directio OP, with P=position3d
    return bar