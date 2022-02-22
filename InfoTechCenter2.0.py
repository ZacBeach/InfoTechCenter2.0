# Code Name - Hornet

# Import Libraries Here
from time import sleep #You can use Python’s sleep() function to add a time delay to your code.
import colorama
from colorama import Fore, Back, Style
colorama.init(strip=False, autoreset=True)

import random

# Wellcome Branch

print(Fore.GREEN + "Welcome to Hornets InfoTechCenter")
sleep(1)
print("\nHornet's Operating System Booting up\n")
sleep(1)

#Gas Branch

# Gas Level Function
def gasLevelGage():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGage()

# Create If-ELIF-ELSE statements using Comparative operator == Equal to in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell","BP","Citgo","Circle K","Mobil","Speedway","Marathon","love's","Meijer","Costco","Sunoco"]
    miles = round(random.uniform(1,25), 1)
    if gasLevelIndicator == "Empty":
        print("      ***WARNING***\n Your gas tank is empty\nCalling Emergency Contact")
    elif gasLevelIndicator == "Low":
        print("      ***WARNING***\n  Your gas tank is low\nThe closest gas station is\n" + random.choice(gasStations) + " which is " + str(miles) + " miles away")
    elif gasLevelIndicator == "Quarter Tank":
        print("You have a Quarter Tank of gas\n  Get to a gas station soon")
    elif gasLevelIndicator == "Half Tank":
        print("You have a Half Tank of gas\nYou have 125 miles to empty")
    elif gasLevelIndicator == "Tree Quarter Tank":
        print("You have a Three Quarter Tank of gas\nYou have 205 miles to empty")
    else:
        print("You have a Full Tank of gas\nYou have 310 miles to empty")

# Call Function here
gasLevelAlert()