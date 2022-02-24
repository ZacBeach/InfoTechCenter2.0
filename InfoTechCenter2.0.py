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
        print("\nVRS has changed your alarm 40 minutes earlier based on the NWS forcast of",weatherAlert,":(")
        print("VRS will only allow your car to go 30MPH")
    elif weatherAlert == "Snowy":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 50MPH")
    elif weatherAlert == "Raining":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 70MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert, ":(")
        print("VRS will only allow your car to go 60MPH")
    else:
        print("\nWeather is", weatherAlert, "lets go:)")
        print("VRS has not restricted your speed")

vehicleResponceSystem()