# -*- coding: utf-8 -*-
# @Author  : Yifang
# @Time    : 2020/12/26 10:03
# @Function:
import pandas as pd
import numpy as np
from urllib.request import urlopen
import json
import glob
import os

#Importing Data plotting libraries
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as py
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.ticker as ticker
import matplotlib.animation as animation

#Other Miscallaneous Libraries
import warnings
warnings.filterwarnings('ignore')
from IPython.display import HTML
import matplotlib.colors as mc
import colorsys
from random import randint
import re


#Reading the cumulative cases dataset
covid_cases = pd.read_csv('Novel Corona Virus 2019 Dataset/covid_19_data.csv')

#Viewing the dataset
covid_cases.head()

#Creating the interactive map
py.init_notebook_mode(connected=True)

#GroupingBy the dataset for the map
formated_gdf = covid_cases.groupby(['ObservationDate', 'Country/Region'])['Confirmed', 'Deaths', 'Recovered'].max()
formated_gdf = formated_gdf.reset_index()
formated_gdf['Date'] = pd.to_datetime(formated_gdf['ObservationDate'])
formated_gdf['Date'] = formated_gdf['Date'].dt.strftime('%m/%d/%Y')

formated_gdf['log_ConfirmedCases'] = np.log(formated_gdf.Confirmed + 1)
formated_gdf['log_Fatalities'] = np.log(formated_gdf.Deaths + 1)

#Plotting the figure


fig = px.choropleth(formated_gdf, locations="Country/Region", locationmode='country names',
                     color="log_ConfirmedCases", hover_name="Country/Region",projection="mercator",
                     animation_frame="Date",width=1000, height=800,
                     color_continuous_scale=px.colors.sequential.Viridis,
                     title='The Spread of COVID-19 Cases Across World')

#Showing the figure
fig.update(layout_coloraxis_showscale=True)
py.offline.iplot(fig)
