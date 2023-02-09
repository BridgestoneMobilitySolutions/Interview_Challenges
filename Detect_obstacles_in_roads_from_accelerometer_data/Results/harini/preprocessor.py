#main libraries
import os
import pickle
import numpy as np
import pandas as pd
import sys

from plotly.subplots import make_subplots
import plotly.graph_objects as go

#from config import *


def check_df(dataframe):
    print('dataframe shape:',dataframe.shape)
    print('#######################')
    print('data types:')
    print(dataframe.dtypes)
    print('#######################')
    print('sum of null values:')
    print(dataframe.isnull().sum())
    print('#######################')
    print('number of duplicates rows:', dataframe.duplicated().sum())

    
def line_plot_xyz(df,X_axis,titile):
    fig = make_subplots(rows=3, cols=1)

    fig.append_trace(go.Scatter(
    x=df[X_axis],
    y=df['acc_x']
    ), row=1, col=1)

    fig.append_trace(go.Scatter(
    x=df[X_axis],
    y=df['acc_y'],
    ), row=2, col=1)

    fig.append_trace(go.Scatter(
    x=df[X_axis],
    y=df['acc_z']
    ), row=3, col=1)


    fig.update_layout(height=800, width=2000, title_text=titile)
    
    return fig.show()    
    
  



    
def unique_values(df,column):
    print('unique values in ',column)
    print(df[column].unique())
    

 
    
def is_primary_key(df,column):
    print('Total value count:',df[column].count())
    print('Total unique value count:', df[column].nunique())





        