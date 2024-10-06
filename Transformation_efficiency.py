import streamlit as st

def calculate_transformation_efficiency(colonies, recovery_volume_ul, dna_ug, volume_plated_ul):
    """Calculate transformation efficiency."""
    if dna_ug <= 0 or volume_plated_ul <= 0:
        raise ValueError("DNA amount and volume plated must be greater than zero.")
    
    # Formula: (Number of colonies * final recovery volume in µL) / (DNA (µg) * Volume plated in µL)
    transformation_efficiency = (colonies * recovery_volume_ul) / (dna_ug * volume_plated_ul)
    return transformation_efficiency

def main():
    st.title("Transformation Efficiency Calculator")
    
    # Input fields for user data
    colonies = st.number_input('Total colonies on the plate:', min_value=0, value=0)
    recovery_volume_ul = st.number_input('Final volume after recovery (in µL):', min_value=0, value=1000)  # default to 1000 µL
    dna_ug = st.number_input('Amount of DNA added (in µg):', min_value=0.0, value=0.1)
    volume_plated_ul = st.number_input('Volume plated (in µL):', min_value=0.0, value=100)  # default to 100 µL
    
    # Calculate transformation efficiency when button is clicked
    if st.button('Calculate'):
        try:
            te = calculate_transformation_efficiency(colonies, recovery_volume_ul, dna_ug, volume_plated_ul)
            st.success(f"Transformation efficiency: {te:.2e} colonies/µg DNA")
        except ValueError as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
