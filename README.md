# Weather Wear App

This project is a machine learning-powered application that recommends suitable outfits based on the current weather conditions in any city.

## Features
- Fetches real-time weather data for any city using the Open-Meteo API and geocoding.
- Predicts the best outfit to wear based on temperature, humidity, wind speed, and weather conditions.
- Uses a Random Forest model trained on a synthetic dataset of weather and outfit combinations.
- Command-line interface for entering a city and receiving outfit suggestions.

## What I Did
- Generated a synthetic dataset mapping weather conditions to appropriate outfits.
- Trained a Random Forest classifier to predict outfit recommendations.
- Implemented weather data fetching with city-to-coordinates geocoding.
- Built a script to interactively suggest outfits based on user input and real-time weather.

## How to Use
1. Clone the repository and set up a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Run `main.py` to train the model (if not already trained).
4. Run `script.py` and enter your city to get a weather-based outfit suggestion.

---

Feel free to contribute or suggest improvements! 