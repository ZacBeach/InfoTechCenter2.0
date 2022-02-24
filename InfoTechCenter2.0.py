import random

# Weather Branch

def weather():
    weatherForecast = ["Icy","Snowy","Raining","Windy","Foggy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# calling weather function to determine weather
weatherAlert = weather()

def vehicleResponceSystem():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert,":(")
        print("VRS will only allow your car to go 30MPH")

vehicleResponceSystem()