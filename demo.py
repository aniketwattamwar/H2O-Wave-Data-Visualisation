from h2o_wave import Q, main, app, ui,site,data
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import random
import h2o


def load_data():
    data = pd.read_csv('application_data.csv')
    return data

df = load_data()

page = site['/demo_eda']


card = page.add('header',ui.header_card(
    box='1 1 5 2', #column row width height
    title='HackerShrine demo Data visualisation',
    subtitle='by Aniket Wattamwar',
    icon='ExploreData',
))

#bar plot
df_bar = df.loc[:200,['NAME_INCOME_TYPE','AMT_INCOME_TOTAL','CODE_GENDER']]
v  = page.add('bar_plot',ui.plot_card(
    box = '1 4 4 4',
    title='Bar Plot',
    data=data(fields=df_bar.columns.tolist(),rows = df_bar.values.tolist()),
    plot = ui.plot(marks=[ui.mark(type='interval',x='=NAME_INCOME_TYPE',y='=AMT_INCOME_TOTAL',
    color='=CODE_GENDER')
    ])
))

#point plots

page.save()










