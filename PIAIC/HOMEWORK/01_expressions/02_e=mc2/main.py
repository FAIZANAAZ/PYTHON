# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
def main():
    C = 299792458  # Speed of light in m/s
    
    while True:
        user_input = input("\nEnter kilos of mass (or type 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("\n🚀 Program exited. Have a great day!\n")
            break
        
        try:
            mass_in_kg = float(user_input)  # Allow decimal values
            E = mass_in_kg * C**2  # E = m * c^2
            
            print(f"""\n🧪 e = m * C^2...
📌 m = {mass_in_kg} kg
⚡ C = {C} m/s
🔥 {E:.2e} joules of energy!\n""")  # Uses scientific notation
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

if __name__ == '__main__':
    main()
