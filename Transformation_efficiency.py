def main():
    st.title("Transformation Efficiency Calculator")
    
    # Input fields for user data
    colonies = st.number_input('Total colonies on the plate:', min_value=0, value=0, step=1)
    recovery_volume_ul = st.number_input('Final volume after recovery (in µL):', min_value=0.0, value=1000.0, step=1.0)  # default to 1000 µL
    dna_ug = st.number_input('Amount of DNA added (in µg):', min_value=0.0, value=0.1, step=0.1)
    volume_plated_ul = st.number_input('Volume plated (in µL):', min_value=0.0, value=100.0, step=1.0)  # default to 100 µL
    
    # Calculate transformation efficiency when button is clicked
    if st.button('Calculate'):
        try:
            te = calculate_transformation_efficiency(colonies, recovery_volume_ul, dna_ug, volume_plated_ul)
            st.success(f"Transformation efficiency: {te:.2e} colonies/µg DNA")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
