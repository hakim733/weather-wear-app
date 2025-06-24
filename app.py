import streamlit as st
from get_weather import fetch_weather
from predict import predict_outfit

# Set page config
st.set_page_config(page_title="👗 Weather Outfit Recommender", layout="centered")

# Fancy CSS styles
st.markdown("""
    <style>
    .title {
        font-size: 3em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.2em;
    }
    .subtitle {
        font-size: 1.3em;
        text-align: center;
        color: #555;
        margin-bottom: 2em;
    }
    .weather-box {
        border-radius: 12px;
        background: #f0f2f6;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">👕 What Should I Wear Today?</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Live weather + outfit prediction powered by AI</div>', unsafe_allow_html=True)

# Input
city = st.text_input("🌍 Enter your city", "Berlin")

if city:
    with st.spinner("Fetching weather..."):
        weather = fetch_weather(city)

    if weather:
        st.markdown('<div class="weather-box">', unsafe_allow_html=True)
        st.subheader("🌤️ Current Weather in " + city)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Temperature", f"{weather['temp']} °C")
            st.metric("Humidity", f"{weather['humidity']}%")
        with col2:
            st.metric("Wind Speed", f"{weather['wind_speed']} km/h")
            st.metric("Condition", weather['condition'])
        st.markdown('</div>', unsafe_allow_html=True)

        outfit = predict_outfit(weather)

        # Fancy result
        st.markdown("### 👚 Recommended Outfit")
        st.success(f"**{outfit}**", icon="🧥")

    else:
        st.error("⚠️ Couldn't fetch weather. Please check the city name.")
