"""
Streamlit frontend for Weather App
Visualizes temperature trends and sky conditions.
"""

import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast Dashboard 🌤️")

place = st.text_input("Place:", help="Enter a City or Country name.")
days = st.slider(
    "Forecast Days:",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days."
)
topic = st.selectbox("Select data to view", ("Temperature", "Sky Conditions"))

if place.strip():
    if days == 1:
        st.subheader(f"{topic} for the next 24 hours in {place.title()}")
    else:
        st.subheader(f"{topic} for the next {days} days in {place.title()}")


if place:
    try:
        observing_dicts = get_data(place, days)

        if topic == "Temperature":
            temp_data = [i["main"]["temp"] for i in observing_dicts]
            dates = [i['dt_txt'] for i in observing_dicts]
            figure = px.line(
                x=dates,
                y=temp_data,
                labels={"x": "Date (GMT)", "y": "Temperature (C)"}
            )
            st.plotly_chart(figure)

        elif topic == "Sky Conditions":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/clouds.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }
            sky_condition = [i["weather"][0]["main"] for i in observing_dicts]
            sky_image = [images[n] for n in sky_condition]
            dates = [i['dt_txt'] for i in observing_dicts]
            st.image(sky_image, width=115, caption=dates)

    except ValueError as e:
        st.error(e)