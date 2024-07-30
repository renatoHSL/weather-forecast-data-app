import streamlit as st
import plotly.express as px
from get_data import get_data

st.title("In Search for Happiness")

x_option = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_option = st.selectbox("Select the data for the Y-axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{x_option} and {y_option}")


x_data = get_data(x_option)
y_data = get_data(y_option)


figure = px.scatter(x=x_data, y=y_data, labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)
