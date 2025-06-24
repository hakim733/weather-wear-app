import pandas as pd
import random
import os

def generate_synthetic_data(n=200):
    data = []

    for _ in range(n):
        temp = round(random.uniform(-10, 40), 1)  # °C
        humidity = random.randint(20, 100)        # %
        wind = round(random.uniform(0, 25), 1)    # km/h
        condition = random.choice(["Clear", "Clouds", "Rain", "Snow", "Thunderstorm", "Drizzle"])

        # Outfit logic
        if temp < 0:
            outfit = "Winter coat and boots"
        elif temp < 10:
            outfit = "Jacket and jeans"
        elif temp < 20:
            outfit = "Sweater and jeans"
        elif temp < 28:
            outfit = "T-shirt and jeans"
        else:
            outfit = "Shorts and T-shirt"

        if "Rain" in condition or "Drizzle" in condition:
            outfit += " + Umbrella"
        if "Snow" in condition:
            outfit += " + Gloves"
        if wind > 15:
            outfit += " + Windbreaker"

        data.append({
            "temp": temp,
            "humidity": humidity,
            "wind_speed": wind,
            "condition": condition,
            "outfit": outfit
        })

    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/outfit_dataset.csv", index=False)
    print("✅ Synthetic data saved to data/outfit_dataset.csv")

generate_synthetic_data(250)
