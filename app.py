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

st.title("Vehicles Ads") 
st.markdown("---")
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


# hist - x=odometer y=price
st.markdown("Let's plot the relacion between the odometer and the price, and see how influence in the price") 
st.code('''#histogram - x=odometer y=price
fig = px.histogram(car_data, x='odometer', y='price')''')

# checkbox to show histogram
hist_check = st.checkbox('Show histogram')

if hist_check:
  try:
    st.write(
      'mileage and price')
    fig = px.histogram(car_data, x='price')
    # show interactive ploty chart
    st.plotly_chart(fig, use_container_width=True)
  except Exception as e:
    st.error(e)

# scatter plot - x=model_year y=price
st.markdown("Let's build a scatter plot that show the relation between price and model") 
st.code('''#scatterplt - x=model_year y=price
fig = px.scatter(car_data, x='model_year', y='price')''')

# checkbox to show scatter plot
scatter_check = st.checkbox('Show scatter plot')
if scatter_check:
  try:
    st.write(
      'Price and model year')
    fig = px.scatter(car_data, x='model_year', y='price')
    # show interactive ploty chart
    st.plotly_chart(fig, use_container_width=True)
  except Exception as e:
    st.error(e)


#link to github repository
st.markdown("---")
st.page_link("https://github.com/uhserZ/vehicles_EDA", label="see Github repository", icon="😊")
