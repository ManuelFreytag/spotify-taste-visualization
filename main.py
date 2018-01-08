# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 22:01:01 2017

@author: Manuel Freytag
"""

#TODO:
#Add data panel excerpt
#add summary widget
from login import login
from dataImport import getData

from bokeh.plotting import *
from bokeh.io import curdoc
from bokeh.layouts import row, column, widgetbox
from bokeh.models import HoverTool
from bokeh.models import FuncTickFormatter
from bokeh.models.widgets import Select
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

"""
1) DATA IMPORT
"""
#IMPORT
credentials = login()
username = "manu.freytag@web.de"
data = getData(credentials,username, saved = True)

#DATA DESCRIPTION
DESC = ["addDate","aname","tname"]

AXIS_TICKERS = ["danceability","mode","speechiness","accusticness",
        "instrumentalness","tempo","loudness","energy","liveness",
        "duration_ms","key","valence"]

CIRCLE_TICKERS = ["tempo", "loudness","duration_ms","None"]

#Every circle ticker is included in the axes_ticker
columns = list(set(DESC + AXIS_TICKERS))
#data = pd.read_csv("data.csv",sep = ";", decimal = ",", encoding = "cp1252")
data = data.loc[:,columns]

"""
2) DATA PREPARATION

prepare data and create new columns for insight visualization
"""

#transform the data into date time
data["addDate"] = pd.to_datetime(data["addDate"])
data["addYM"] = pd.to_datetime(data.addDate.map(lambda x: x.strftime("%Y-%m")))

#group by month
aggr_songs = data.groupby(by = "addYM").size()
#create new column and indicate the number of 
data = data.merge(aggr_songs.to_frame("count"), left_on = "addYM", right_index = True)
        
#add dummy entries for months with 0 additions
months = pd.date_range(data["addYM"].min(),data["addYM"].max(),freq = "MS")
#check if freq is bigger than zero
for month in months:
    if(data[data["addYM"] == month].size == 0):
        tmp = pd.Series({"addYM":month,"count":0})
        data = data.append(tmp, ignore_index = True)
        
data_df = data.copy()
data_df = data_df.sort_values(by = "addYM")

"""
3) BOKEH VISUALIZATION

creating objects and joining them with data
"""

#ADD WIDGETS
#We are not allowed to select the same think for x and y values
def nix(val, lst):
    return [x for x in lst if x != val]

x_ticker = Select(title = "x-axis", value = "energy", options=nix("duration_ms", AXIS_TICKERS))
y_ticker = Select(title = "y-axis", value = "duration_ms", options = nix("energy", AXIS_TICKERS))
circle_ticker = Select(title = "circle size", value = "None", options = nix("None",CIRCLE_TICKERS))

def update(selected = None):
    source_df = data_df[["addYM","count","aname","tname",x_ticker.value,y_ticker.value]]
    
    if(circle_ticker.value == "None"):
        source_df["circle"] = 4
    else:
        #remove nan
        circle_vals = data_df[circle_ticker.value].dropna()
        #normalize all without nan
        circle_vals.loc[:] = list(MinMaxScaler().fit_transform(circle_vals.values.reshape(-1,1))*12) #max val has size 12
        #join based on index
        source_df = source_df.join(circle_vals)
    
    #rename the last two entries to x and y
    source_df.columns = ["addYM","count","aname","tname","x","y","circle"]
    source.data = source.from_df(source_df)

def x_ticker_change(attrname, old,new):
    #x and y axis values must be differing
    y_ticker.options = nix(new, AXIS_TICKERS)
    circle_ticker.options = nix(new, CIRCLE_TICKERS)
    #change the labels
    first.xaxis.axis_label = x_ticker.value
    update()
    
def y_ticker_change(attrname, old,new):
    #x and y axis values must be differing
    x_ticker.options = nix(new, AXIS_TICKERS)
    circle_ticker.options = nix(new, CIRCLE_TICKERS)
    first.yaxis.axis_label = y_ticker.value
    update()
    
def circle_ticker_change(attrname, old,new):
    #x and y axis values can be the SAME
    x_ticker.options = nix(new, AXIS_TICKERS)
    y_ticker.options = nix(new, AXIS_TICKERS)
    update()
   
x_ticker.on_change('value',x_ticker_change)
y_ticker.on_change('value',y_ticker_change)
circle_ticker.on_change('value',circle_ticker_change)

#initialize
source = ColumnDataSource()
update()

#ADD TOOLS
hover = HoverTool(tooltips = [
        ("Artist","@aname"),
        ("Track name","@tname")
        ])

TOOLS = "box_select,reset,box_zoom"

#ADD PLOTS
first = figure(tools = [hover,TOOLS])
first.circle('x','y',size = 'circle',color = "#66CD00", source = source)
first.xaxis.axis_label = x_ticker.value
first.yaxis.axis_label = y_ticker.value

second = figure(tools = [hover,TOOLS],x_axis_type="datetime")
second.circle('addYM','count', color = "darkgrey", source = source)
second.line('addYM','count', color = "#66CD00",source=source)
second.xaxis.axis_label = "Added at date"
second.yaxis.axis_label = "Count of songs added"

#setup layout
widgets = widgetbox(x_ticker,y_ticker,circle_ticker)
main_row = row(widgets, first, second)

curdoc().add_root(main_row)
curdoc().title = "test"
