import pandas as pd
data=pd.read_csv('data/textiles_data.csv')
print("Dataset Loaded:")
print(data)
def calculate_total_emissions(material, weight):
  emissions_pr_kg=data[data['Material']==material]['CO2_Emissions_kg_per_kg'].values[0]
  return emission_per_kg*weight
print(f"\nCalculating CO2 emissions for {weight_of_material}kg of each material:")
