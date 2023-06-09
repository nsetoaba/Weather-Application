import json
import requests   #pip install requests
import streamlit as st
import time
from streamlit_lottie import st_lottie

# API URL and Key
#url = "https://api.openweathermap.org/data/2.5/weather?q="
#api_key = 'af22c7596d09d252fea018a8e62c68aa'

@st.cache
def get_weather_data(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=af22c7596d09d252fea018a8e62c68aa')
    return response.json()

# Emojis are found here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My simpel weather page", page_icon=":tada:", layout = "wide")

@st.cache(allow_output_mutation=True)  # This improves the streamlit performance
def load_lottieurl(url):
    time.sleep(2)
    r = requests.get(url)
    if r.status_code != 200:
        st.write("Unavailable")
        return None
    return r.json()

#  ----- LOAD Assets ----
Lottie_various_locations_image = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_UgZWvP.json")

#  ----- Header section -----
with st.container():
    st.title("Welcome to my weather page:wave:")
    st.subheader("I am Ntau. :smile:")
    st.subheader("A Product Manager from Praha, Czechia.")
    st.write("I enjoy working with python and love learning new technologies.")
    st.write("Go through my interactive page and have an overview of a few things I have done!")

# ----- Show display of weather -----
with st.container():
    st.write("---")
    st.header("What is the weather today in your location?")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st_lottie(Lottie_various_locations_image, height=350, loop=True, speed = 1.5, quality = "medium")
        st.write(
            """        
            - Enter any location that you can think of and see what the weather is like.
            """
        )

# Streamlit app for the weather

url = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = 'af22c7596d09d252fea018a8e62c68aa'

def app():
    # Page title
    st.title("What's the weather like?")

    # Lottie animation
    Lottie_confused_image = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_qqu8eybe.json")
    st_lottie(Lottie_confused_image, speed=1, width=200, height=200, key="lottie")
    
    # City ID input
    city_id = st.text_input("Enter City ID:")

    # Submit button
    if st.button("Get Weather"):
        # Full URL
        complete_url = url + city_id + "&appid=" + api_key

        # GET request via API found in openweather
        response = requests.get(complete_url)

        # JSON data
        data = response.json()

        # Extract weather data
        if data["cod"] != "404":
            weather = data["main"]
            temperature = round(weather["temp"] - 273.15, 2)
            humidity = weather["humidity"]
            pressure = weather["pressure"]
            report = data["weather"][0]["description"].capitalize()
            st.write(f"Temperature: {temperature}°C")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Pressure: {pressure}hPa")
            st.write(f"Weather Report: {report}")
        else:
            st.error("City not found")

# Run Streamlit app
if __name__ == "__main__":
    app()