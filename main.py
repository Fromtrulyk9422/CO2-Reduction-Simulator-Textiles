import pandas as pd

# Load the dataset
data = pd.read_csv('data/textile_data.csv')

# Show the dataset to verify it's loaded correctly
print("Dataset Loaded:")
print(data)

# Function to calculate total CO2 emissions for each material
def calculate_total_emissions(material, weight):
    CO2_Emissions_kg_per_kg = data[data['Material'] == material]['CO2_Emissions_kg_per_kg'].values[0]
    return CO2_Emissions_kg_per_kg * weight

# Function to calculate CO2 reduction if material is replaced
def calculate_CO2_reduction(material_from, material_to, weight):
    emissions_from = calculate_total_emissions(material_from, weight)
    emissions_to = calculate_total_emissions(material_to, weight)
    return emissions_from - emissions_to

# Example: Compare CO2 emissions for different materials
weight_of_material = 100  # kg of material used

print(f"\nCalculating CO2 emissions for {weight_of_material}kg of each material:")
cotton_emissions = calculate_total_emissions("Cotton", weight_of_material)
polyester_emissions = calculate_total_emissions("Polyester", weight_of_material)

print(f"CO2 emissions for Cotton: {cotton_emissions} kg")
print(f"CO2 emissions for Polyester: {polyester_emissions} kg")

# Example: Calculate CO2 reduction if replacing Cotton with Polyester
CO2_reduction = calculate_CO2_reduction("Cotton", "Polyester", weight_of_material)
print(f"\nCO2 reduction if replacing Cotton with Polyester: {CO2_reduction} kg for {weight_of_material}kg of material")
