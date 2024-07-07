FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_INTERCEPT = 32  
CELSIUS_TO_FAHRENHEIT_INTERCEPT = 32

def convert_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - FAHRENHEIT_TO_CELSIUS_INTERCEPT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * float(celsius) + CELSIUS_TO_FAHRENHEIT_INTERCEPT
    print(f"{celsius}°C is {fahrenheit}°F")


def user_input_interaction():

    user_temperature_input = input("Enter the temperature to convert: ")

    if user_temperature_input.isnumeric():
        
        user_checker = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

        if (user_checker == 'C'):
            convert_to_fahrenheit(user_temperature_input)
        elif (user_checker == 'F'):
            convert_to_celsius(user_temperature_input)
        else: 
            print("Enter the correct degree. ")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    

if __name__ == "__main__":
    user_input_interaction()





