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

weight = st.number_input("Enter the weight of material (kg):", min_value=10, step=10)

if st.button("Calculate CO₂ Reduction"):
    current_CO2_emissions = calculate_total_emissions(current_material, weight)
    replacement_CO2_emissions = calculate_total_emissions(replacement_material, weight)
    reduction = current_CO2_emissions - replacement_CO2_emissions

    st.write(f"If you replace **{current_material}** with **{replacement_material}**,")

    if reduction > 0:
        st.write(f"you will reduce your CO₂ emissions by **{reduction:.2f} kg/CO₂**.")
        st.success("Great choice! You're reducing your CO2 emissions!")
    elif reduction < 0:
        st.write(f"you will increase your CO₂ emissions by **{reduction:.2f} kg/CO₂**.")
        st.warning("This choice actually increases your CO2 emissions! Consider another option.")
    else:
        st.write(f"you will not reduce nor increase your CO₂ emissions by **{reduction:.2f} kg/CO₂**.")
        st.info("No change in CO2 emissions. Try another material!")

def suggest_CO2_emissions_reduction(material):
    if material == "Cotton":
        return "Try switching to polyester or linen, which have lower carbon footprints."
    elif material == "Polyester":
        return "You could consider using recycled polyester for even better sustainable choices!"
    elif material == "Wool":
        return "You could switch for polyester or linen to lower your carbon footprint. Alternatively you could choose responsable sources of wool. Maybe one of your neighbours has sheeps 😁" 
    elif material == "Nylon":
        return "Try switching to polyester or linen, which have lower carbon footprints."
    if material == "Linen":
        return "Linen is great! For an even lower carbon footprint you could consider switching to polyester."
