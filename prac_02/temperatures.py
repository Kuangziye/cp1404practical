"""
FIRST_CONVERSION_VOLUME = 32
SECOND_CONVERSION_VOLUME = 1.8

function main():
    get choice
    get user_temperature
    if choice == "C"
        celsius = user_temperature
        fahrenheit = calculate_celsius_to_fahrenheit(user_temperature)
        display celsius, fahrenheit
    fahrenheit = user_temperature
    celsius = calculate_fahrenheit_to_celsius(user_temperature)

function calculate_celsius_to_fahrenheit(user_temperature):
    fahrenheit = FIRST_CONVERSION_VOLUME + user_temperature * SECOND_CONVERSION_VOLUME
    return fahrenheit

function calculate_fahrenheit_to_celsius(user_temperature):
    celsius = (user_temperature - FIRST_CONVERSION_VOLUME) / SECOND_CONVERSION_VOLUME
    return celsius

main()

"""

FIRST_CONVERSION_VOLUME = 32
SECOND_CONVERSION_VOLUME = 1.8


def main():
    choice = str(input("Which temperature type you want to enter(C/F):")).upper()
    user_temperature = float(input("Temperature:"))
    if choice == "C":
        celsius = user_temperature
        fahrenheit = calculate_celsius_to_fahrenheit(user_temperature)
        print(f"The celsius you enter is {celsius:.2f},it corresponds to {fahrenheit:.2f} fahrenheit")
    fahrenheit = user_temperature
    celsius = calculate_fahrenheit_to_celsius(user_temperature)
    print(f"The fahrenheit you enter is {fahrenheit:.2f},it corresponds to {celsius:.2f} celsius")


def calculate_celsius_to_fahrenheit(user_temperature):
    fahrenheit = FIRST_CONVERSION_VOLUME + user_temperature * SECOND_CONVERSION_VOLUME
    return fahrenheit


def calculate_fahrenheit_to_celsius(user_temperature):
    celsius = (user_temperature - FIRST_CONVERSION_VOLUME) / SECOND_CONVERSION_VOLUME
    return celsius


main()
