from get_weather import fetch_weather
from predict import predict_outfit

city = input("Enter your city: ")
weather = fetch_weather(city)

print("Current weather:", weather)
outfit = predict_outfit(weather)
print("Suggested outfit:", outfit)
