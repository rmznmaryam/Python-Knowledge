# Maryam Ramzaan
# TerraHacks Hackathon at Toronto Metropolitan University
#  August 2024

def calculate_energy_footprint(electricity_kwh, gas_therms):
    # Average emissions factors (in kg CO2 per unit) 
    electricity_emission_factor = 0.233  # kg CO2 per kWh
    gas_emission_factor = 0.0053         # kg CO2 per therm
    
    # Calculate the emissions
    electricity_emissions = electricity_kwh * electricity_emission_factor
    gas_emissions = gas_therms * gas_emission_factor
    
    return electricity_emissions + gas_emissions

def calculate_travel_footprint(miles_driven, flight_hours):
    # Average emissions factors (in kg CO2 per unit)
    car_emission_factor = 0.411  # kg CO2 per mile
    flight_emission_factor = 0.254  # kg CO2 per passenger-mile
    
    # Calculate the emissions
    car_emissions = miles_driven * car_emission_factor
    flight_emissions = flight_hours * flight_emission_factor
    # Results
    return car_emissions + flight_emissions

def main():
    print("    Hello, and welcome to the Carbon Footprint Calculator!")
    
    # Input data from the user
    electricity_kwh = float(input("Enter your electricity consumption in kWh: "))
    gas_therms = float(input("Enter your gas consumption in therms: "))
    miles_driven = float(input("Enter the number of miles you drive per year: "))
    flight_hours = float(input("Enter the number of flight hours you take per year: "))
    
    # Calculate footprints
    print("    Your Carbon Footprint is... ")
    energy_footprint = calculate_energy_footprint(electricity_kwh, gas_therms)
    travel_footprint = calculate_travel_footprint(miles_driven, flight_hours)
    
    total_footprint = energy_footprint + travel_footprint
    
    print(f"Your total carbon footprint is {total_footprint:.2f} kg CO2 per year.")

if __name__ == "__main__":
    main()