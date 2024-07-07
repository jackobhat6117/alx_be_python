
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_INTERCEPT = 32  
CELSIUS_TO_FAHRENHEIT_INTERCEPT = 32  

def convert_to_celsius(fahrenheit):
   
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_INTERCEPT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_TO_FAHRENHEIT_INTERCEPT

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp)
            print(f"{temp}°F is {converted}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
