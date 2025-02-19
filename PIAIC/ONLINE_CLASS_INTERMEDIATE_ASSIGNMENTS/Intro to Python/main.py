def main():
    Gravitational_percentage = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }  

    user_planet = input("Enter a planet from the following list: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune: ")
    user_weight = float(input("Enter your weight on Earth in lbs: "))  # ✅ Corrected prompt & used float
    
    if user_planet in Gravitational_percentage:
        weight_on_planet = round(user_weight * Gravitational_percentage[user_planet] / 100, 2)  # ✅ Rounded to 2 decimals
        print(f"The weight on {user_planet} is {weight_on_planet} lbs.")

if __name__ == "__main__":
    main()
