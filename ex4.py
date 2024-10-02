#  Write a program that converts temperatures from Celsius to Fahrenheit based on user input.

######### SOLUTION #########

def converter():
    celsius_value = float(input("Enter the value (°C) "))

    fahrenheit_value = (1.8 * celsius_value) + 32

    return fahrenheit_value

output = converter()
print(f"The temperature in Fahrenheit (°F) is: {output:.2f}")