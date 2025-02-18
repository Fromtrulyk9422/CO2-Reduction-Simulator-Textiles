import pandas as pd
import streamlit as st

data = pd.read_csv("data/textile_data.csv")

def calculate_total_emissions(material, weight):
    CO2_Emissions_kg_per_kg = data[data['Material'] == material]['CO2_Emissions_kg_per_kg'].values[0]
    return CO2_Emissions_kg_per_kg * weight

st.title("CO₂ Reduction Simulator for Textiles")
st.write("Choose a material and compare its CO₂ emissions with alternatives.")

materials = data["Material"].unique()
current_material = st.selectbox("Select your current material:", materials)
replacement_material = st.selectbox("Select a replacement material:", materials)

weight = st.number_input("Enter the weight of material (kg):", min_value=0, step=10)

if st.button("Calculate CO₂ Reduction"):
    current_CO2_emissions = calculate_total_emissions(current_material, weight)
    replacement_CO2_emissions = calculate_total_emissions(replacement_material, weight)
    reduction = current_CO2_emissions - replacement_CO2_emissions

    st.write(f"If you replace **{current_material}** with **{replacement_material}**,")
    st.write(f"you will reduce your CO₂ emissions by **{reduction:.2f} kg CO₂**.")

    if reduction > 0:
        st.success("Great choice! You're reducing your CO2 emissions!")
    elif reduction < 0:
        st.warning("This choice actually increases your CO2 emissions! Consider another option.")
    else:
        st.info("No change in CO2 emissions. Try another material!")
