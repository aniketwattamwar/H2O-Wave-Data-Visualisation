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

# print(df)

 
page = site['/eda']


card = page.add('header', ui.header_card(
    box='1 1 5 2',
    title='Credit Card Fraud Detection Data Visualisation',
    subtitle='made by HackerShrine',
    icon='ExploreData',
))



# plotting data
df_point =  df.loc[:200,['DAYS_REGISTRATION','DAYS_ID_PUBLISH','NAME_EDUCATION_TYPE']]
v = page.add('point_plot', ui.plot_card(
    box='1 3 5 2',
    title='Point Plot',
    data=data(fields=df_point.columns.tolist(),rows=df_point.values.tolist()),
    plot=ui.plot([
        ui.mark(type='point', 
        x='=DAYS_REGISTRATION', y='=DAYS_ID_PUBLISH',
        color='=NAME_EDUCATION_TYPE')
    ])
))

df_point_sized =  df.loc[:200,['AMT_INCOME_TOTAL','AMT_CREDIT','AMT_ANNUITY']]
v = page.add('point_plot_sized', ui.plot_card(
    box='1 5 5 2',
    title='Point Plot Sized',
    data=data(fields=df_point_sized.columns.tolist(),rows=df_point_sized.values.tolist()),
    plot=ui.plot([
        ui.mark(type='point', 
        x='=AMT_INCOME_TOTAL', y='=AMT_CREDIT',size='=AMT_ANNUITY')
    ])
))


df_bar=  df.loc[:200,['NAME_INCOME_TYPE','AMT_INCOME_TOTAL','CODE_GENDER']]
v = page.add('bar_plot', ui.plot_card(
    box='6 3 4 4',
    title='Bar Plot',
    data=data(fields=df_bar.columns.tolist(),rows=df_bar.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='interval', 
        x='=NAME_INCOME_TYPE', y='=AMT_INCOME_TOTAL',
        color='=CODE_GENDER', dodge='auto')
    ])
))

df_bar_stacked=  df.loc[:200,['AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_FAMILY_STATUS']]
print(df_bar_stacked)
v = page.add('df_bar_stacked', ui.plot_card(
    box='1 7 9 4',
    title='Stacked Bar Plot',
    data=data(fields=df_bar_stacked.columns.tolist(),rows=df_bar_stacked.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='interval', 
        x='=NAME_INCOME_TYPE', y='=AMT_INCOME_TOTAL',
        color='=NAME_FAMILY_STATUS', stack='auto')
    ])
))

df_line=  df.loc[:200,['SK_ID_CURR','NAME_INCOME_TYPE','AMT_INCOME_TOTAL']]
v = page.add('df_line', ui.plot_card(
    box='6 11 4 4',
    title='Line Plot',
    data=data(fields=df_line.columns.tolist(),rows=df_line.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='line', 
        x='=SK_ID_CURR', y='=AMT_INCOME_TOTAL', curve='smooth')
    ])
))

df_area=  df.loc[:200,['AMT_INCOME_TOTAL','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS']]
v = page.add('df_area', ui.plot_card(
    box='1 11 5 4',
    title='Area Plot',
    data=data(fields=df_area.columns.tolist(),rows=df_area.values.tolist()),
    plot=ui.plot(marks=[
        ui.mark(type='area',
        x='=NAME_EDUCATION_TYPE', y='=AMT_INCOME_TOTAL',
        color='=NAME_FAMILY_STATUS')
    ])
))

df_b=  df.loc[:200,['AMT_INCOME_TOTAL','NAME_HOUSING_TYPE']]
v = page.add('df_b', ui.plot_card(
    box='1 15 5 4',
    title='Bar Plot',
    data=data(fields=df_b.columns.tolist(),rows=df_b.values.tolist()),
    plot=ui.plot([
        ui.mark(type='interval', 
        x='=NAME_HOUSING_TYPE', y='=AMT_INCOME_TOTAL' ) 
    ])
))

df_line_step =  df.loc[:100,['SK_ID_CURR','NAME_INCOME_TYPE','AMT_INCOME_TOTAL']]
v = page.add('df_heatmap', ui.plot_card(
    box='6 15 4 4',
    title='Line Step Plot',
    data=data(fields=df_line_step.columns.tolist(),rows=df_line_step.values.tolist()),
    plot=ui.plot([
        ui.mark(type='path', 
        x='=SK_ID_CURR', y='=AMT_INCOME_TOTAL', curve='step' ) 
    ])
))


page.save()

 