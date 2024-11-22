import streamlit as st

# Function to calculate Delta resistances from Star resistances
def STAR_DELTA(R1, R2, R3):
    # Calculating the Delta resistances using the given formulas
    R12 = (R1 * R2 + R2 * R3 + R3 * R1) / R3
    R23 = (R1 * R2 + R2 * R3 + R3 * R1) / R1
    R31 = (R1 * R2 + R2 * R3 + R3 * R1) / R2
    return R12, R23, R31

# Streamlit app setup
st.title("02305A21L45-PS4")  # Title of the app (adjust for your Roll No. and Problem Statement No.)

# Input fields for the resistances in Star connection
R1 = st.number_input("Enter R1 (in ohms):", min_value=0.0)
R2 = st.number_input("Enter R2 (in ohms):", min_value=0.0)
R3 = st.number_input("Enter R3 (in ohms):", min_value=0.0)

# Calculate button
if st.button("Calculate Delta Resistances"):
    # Call the STAR_DELTA function to calculate R12, R23, and R31
    R12, R23, R31 = STAR_DELTA(R1, R2, R3)
    
    # Display the results
    st.write(f"R12 (Delta resistance between R1 and R2): {R12:.2f} ohms")
    st.write(f"R23 (Delta resistance between R2 and R3): {R23:.2f} ohms")
    st.write(f"R31 (Delta resistance between R3 and R1): {R31:.2f} ohms")
