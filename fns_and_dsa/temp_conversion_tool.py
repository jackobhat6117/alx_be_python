FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")

def user_input_interaction():
    user_temperature_input = input("Enter the temperature to convert: ")

    if user_temperature_input.replace('.', '', 1).isdigit():  
        user_checker = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if user_checker == 'C':
            convert_to_fahrenheit(user_temperature_input)
        elif user_checker == 'F':
            convert_to_celsius(user_temperature_input)
        else: 
            print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    user_input_interaction()
