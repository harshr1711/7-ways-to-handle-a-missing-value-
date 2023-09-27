#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install folium


# In[48]:


import numpy as np
import pandas as pd
import folium as fo
data = pd.read_csv('datavisualization.csv')
print(data.head())
from folium import Map, FeatureGroup, Marker, LayerControl


# In[46]:


lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])

volcano = fo.FeatureGroup(name = "Volcano")

for a,b,c in zip(lat,lon,name):
    volcano.add_child(fo.Marker(location=[a,b], icon = fo.Icon(color = 'blue')))
    
fo.Map().add_child(volcano)


# In[50]:


data.head(75)


# In[62]:


import folium
city_location1 = [-1.467 , -78.442]

m = folium.Map(location=city_location1,
               zoom_start=15,
               tiles='openstreetmap')

folium.Marker(city_location1,
              popup='<i>Teste</i>', 
              tooltip='Click me!').add_to(m)


city_location2 = [63.630,-19.620]

n = folium.Map(location=city_location2,
               zoom_start=15,
               titles ='openstreetmap')

folium.Marker(city_location2,
              popup = '<i>Teste</i>',
              tooltip = 'Click me!').add_to(n)
m ,n


# In[ ]:




