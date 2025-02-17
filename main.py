import pandas as pd
data=pd.read_csv('data/textile_data.csv')
print("Dataset Loaded:")
print(data)
def calculate_total_emissions(material, weight):
  emissions_pr_kg=data[data['Material']==material]['CO2_Emissions_kg_per_kg'].values[0]
  return emission_per_kg*weight
weight_of_material = 100 
print(f"\nCalculating CO2 emissions for {weight_of_material}kg of each material:")
def calculate_CO2_reduction(material_from, material_to, weight):
  emissions_from = calculate_total_emissions(material_from, weight)
  emissions_to = calculate_total_emission(material_to, weight)
  return emissions_from - emission_to
print (f"CO2 emissions for Cotton:{cotton_emissions} kg")
print(f"CO2 emissions for Polyester: {polyester_emissions} kg")

# Example: Calculate CO2 reduction if replacing Cotton with Polyester
CO2_reduction = calculate_CO2_reduction("Cotton", "Polyester", weight_of_material)
print(f"\nCO2 reduction if replacing Cotton with Polyester: {CO2_reduction} kg for {weight_of_material}kg of material")
