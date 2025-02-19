import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

data = pd.read_csv("data/textile_data.csv")

def calculate_total_emissions(material, weight):
    CO2_Emissions_kg = data[data['Material'] == material]["CO2_Emissions_kg"].values[0]
    return CO2_Emissions_kg * weight

def suggest_CO2_emissions_reduction(material):
        if replacement_material == "Cotton":
            return "Try switching to polyester or linen, which have lower carbon footprints."
        elif replacement_material == "Polyester":
            return "Polyester is the best option! For an even lower carbon footprint you could consider using recycled polyester."
        elif replacement_material == "Wool":
            return "You could switch for polyester or linen to lower your carbon footprint. Alternatively you could choose responsible sources of wool. Maybe one of your neighbours has sheeps 😁" 
        elif replacement_material == "Nylon":
            return "Try switching to polyester or linen, which have lower carbon footprints."
        elif replacement_material == "Linen":
            return "Linen is great! For even better sustainable choices you could consider switching to polyester."

st.title("CO₂ Reduction Simulator for Textiles")
st.write("Choose a material and compare its CO₂ emissions with alternatives.")

materials = data["Material"].unique()
current_material = st.selectbox("Select your current material:", materials)
replacement_material = st.selectbox("Select a replacement material:", materials)

weight = st.number_input("Enter the weight of material (kg):", min_value=10, step=10)

if st.button("Calculate CO₂ Reduction"):
    current_material_CO2_emissions = calculate_total_emissions(current_material, weight)
    replacement_material_CO2_emissions = calculate_total_emissions(replacement_material, weight)
    reduction = current_material_CO2_emissions - replacement_material_CO2_emissions

    st.write(f"If you replace **{current_material}** with **{replacement_material}**,")

    if reduction > 0:
        st.write(f"you will reduce your CO₂ emissions by **{reduction:.2f} kg/CO₂**.")
        st.success("Great choice! You're reducing your CO2 emissions!")
    elif reduction < 0:
        st.write(f"you will increase your CO₂ emissions by **{abs(reduction):.2f} kg/CO₂**.")
        st.warning("This choice actually increases your CO2 emissions! Consider another option.")
    else:
        st.write(f"you will not reduce nor increase your CO₂ emissions by **{reduction:.2f} kg/CO₂**.")
        st.info("No change in CO2 emissions. Try another material!")

    suggestion = suggest_CO2_emissions_reduction(replacement_material)
    st.write(f"**Suggestion:** {suggestion}")
        
    fig, ax = plt.subplots()

    ax.bar(current_material, current_material_CO2_emissions, label=f'{current_material}: {current_material_CO2_emissions:.2f} kg/CO₂', color='green')
    ax.bar(replacement_material, replacement_material_CO2_emissions, label=f'{replacement_material}: {replacement_material_CO2_emissions:.2f} kg/CO₂', color='orange')

    ax.set_ylabel('CO₂ emissions (kg)')
    ax.set_title(f'CO₂ emissions for {current_material} and {replacement_material}')
    ax.legend()

    st.pyplot(fig)

    comparison_data = []

    for material in materials:
        if material !=current_material:
            material_CO2_emissions = calculate_total_emissions(material, weight)
            CO2_difference = current_material_CO2_emissions - material_CO2_emissions
            comparison_data.append({
                "Material": material,
                "CO₂ Emissions (kg)": f"{material_CO2_emissions:.2f}",
                "Difference in CO₂ with {current_material} (kg)": f"{CO2_difference:.2f}",
                "CO₂ Savings": f"{CO2_difference:.2f}" if CO2_difference > 0 else "",
                "CO₂ Increase": f"{abs(CO2_difference):.2f}" if CO2_difference < 0 else ""})

    comparison_df = pd.DataFrame(comparison_data)
    comparison_df[difference_column] = current_material_CO2_emissions - comparison_df["CO₂ Emissions (kg)"].astype(float)
    comparison_df = comparison_df.sort_values(by=difference_column, ascending=False)
    comparison_df = comparison_df.reset_index(drop=True)

    st.write("### {current_material} CO₂ emissions comparison with other materials (Ranked from best to worst)")
    st.dataframe(comparison_df, use_container_width=True)
