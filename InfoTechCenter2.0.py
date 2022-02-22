import random

# Gas Level Function
def gasLevelGage():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    print(currentGasLevel)
    return currentGasLevel

# Create If-ELIF-ELSE statements using Comparative operators to display gas level messages
def gasLevelAlert():
    if gasLevelGage() == "Empty":
        print("      ***WARNING***\n You have run out of gas\nCalling Emergency Contact")

# gasLevelGage()
gasLevelAlert()