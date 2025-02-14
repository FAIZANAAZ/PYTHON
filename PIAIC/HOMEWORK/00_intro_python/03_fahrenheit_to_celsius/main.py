
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C

# ///////////////////////////////////////

# User se Fahrenheit temperature input lena
user_answer = float(input("🌡️ Enter temperature in Fahrenheit: "))

# Fahrenheit se Celsius mein conversion
convert_Celsius = (user_answer - 32) * 5 / 9  

# Output ko clean aur readable format mein print karna
print(f"🌍 Temperature: {user_answer:.1f}°F  =  {convert_Celsius:.2f}°C ❄️🔥")


