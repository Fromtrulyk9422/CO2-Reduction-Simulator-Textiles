import pandas as pd

data = pd.read_csv('data/textile_data.csv')

print("Dataset Loaded:")
print(data)

def calculate_total_emissions(material, weight):
    CO2_Emissions_kg_per_kg = data[data['Material'] == material]['CO2_Emissions_kg_per_kg'].values[0]
    return CO2_Emissions_kg_per_kg * weight

def calculate_CO2_emissions_reduction(material_from, material_to, weight):
    emissions_from = calculate_total_emissions(material_from, weight)
    emissions_to = calculate_total_emissions(material_to, weight)
    return emissions_from - emissions_to

weight_of_material = 100  # kg of material used

print(f"\nCalculating CO2 emissions for {weight_of_material}kg of each material:")
cotton_emissions = calculate_total_emissions("Cotton", weight_of_material)
polyester_emissions = calculate_total_emissions("Polyester", weight_of_material)

print(f"CO2 emissions for Cotton: {cotton_emissions} kg")
print(f"CO2 emissions for Polyester: {polyester_emissions} kg")

CO2_emissions_reduction = calculate_CO2_emissions_reduction("Cotton", "Polyester", weight_of_material)
print(f"\nCO2 emissions reduction if replacing Cotton with Polyester: {CO2_emissions_reduction} kg for {weight_of_material}kg of material")
