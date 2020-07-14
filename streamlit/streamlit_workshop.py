import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

st.title("Zip code data")

df = pd.read_csv('C:\\Users\\sivkumar\\Documents\\Study Materials\\GeoSpatial\\zip_with_data.csv', header="infer", sep=',')

st.text("State Names")

chart_data = pd.DataFrame(df.groupby(['state_name'])['pincode'].agg('count'))

st.bar_chart(chart_data)

state = st.sidebar.selectbox('select state:',df.state_name.unique().tolist())

county = st.sidebar.multiselect('select state:',df[df['state_name']==state].county_name.unique().tolist())

map_data_filter = (df['state_name']==state) & (df['county_name'].isin(county))

map_data = df.loc[map_data_filter]

st.map(map_data)

if st.checkbox('show data'):
    st.write(map_data)