import pandas as pd
import plotly.express as px
import streamlit as st
import time
import plotly.figure_factory as ff

# Dataset
try:
  car_data = pd.read_csv('./data/vehicles_us.csv') # read data
except FileNotFoundError:
    st.error(" Data could not be loaded, file not found", icon='🟡')
    time.sleep(.2)
st.code(car_data.info())

st.title("Vehicles Ads") 
st.markdown("////////////////////////////////////")
st.header("EDA ( Exploratory Data Analysis )")
st.subheader("Objetive: ")
st.markdown("Study the collected data and determine factors that influence the price of a vehicle.") 
# dataset preview
st.subheader("Dataset: ")

tab1, tab2 = st.tabs(["🔢 Data", "🔠 Describe data"])
tab1.subheader("Preview cars data")
tab1.write(car_data.head())

tab2.subheader("statistics")
tab2.write(car_data.describe())


