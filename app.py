import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Dr. Pujar Hospital Diagnostic Laboratory Billing System", layout="centered")

# Initialize session state variables if not already done
if "selected_tests" not in st.session_state:
    st.session_state.selected_tests = []
if "test_counter" not in st.session_state:
    st.session_state.test_counter = 0
if "current_page" not in st.session_state:
    st.session_state.current_page = 1  # Default to page 1 (test selection)
if "referred_doctors" not in st.session_state:
    st.session_state.referred_doctors = []

# -------------------- Page 1: Test Selection --------------------
if st.session_state.current_page == 1:
    st.title("Dr. Pujar Hospital Diagnostic Laboratory Billing System")
    st.markdown("---")

    # ------------------------ Patient Details ------------------------
    st.subheader("Enter Patient Details")
    name = st.text_input("Patient's Name", key="patient_name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1, key="patient_age")
    sex = st.radio("Sex", ["Male", "Female", "Other"], key="patient_sex")
    date = st.date_input("Date", value=datetime.now().date(), key="patient_date")

    # Save patient details to session_state
    st.session_state.name = name
    st.session_state.age = age
    st.session_state.sex = sex
    st.session_state.date = date

    # ------------------------ Doctor Selection ------------------------
    st.subheader("Select Referred Doctors")
    
    doctor_options = [
        "Dr. Santosh Pujari (MS - Ayu, ENT, Ph.D)",
        "Dr. Vinod JB (MS - Ayu)",
        "Dr. Avinash Bhavikatti (M.B.B.S, MS, F.S.G.E. Surgical Gastroenterology)",
        "Dr. Divya Bhavikatti (MBBS, MS - OBG)",
        "Dr. Sana Kouser Jamadar (MBBS, Family Physician)",
        "Dr. Vijaykumar Nayak (MS - Ayu, Ph.D)"
    ]

    # Multi-selection of doctors
    selected_doctors = st.multiselect(
        "Choose the Doctors who referred the patient",
        options=doctor_options,
        key="doctor_select"
    )

    # Display selected doctors
    if selected_doctors:
        st.write("### Selected Doctors:")
        for doctor in selected_doctors:
            st.write(f"- {doctor}")
        
        # Save selected doctors to session state
        st.session_state.referred_doctors = selected_doctors

    # ------------------------ Test Data ------------------------
    test_data = {
        "CBC": [300, 350],
        "Hb%": [100],
        "TC/DC": [100],
        "Platelet Count": [100],
        "ESR": [200],
        "BL. GROUP & RH TYPE": [100],
        "BT/CT": [150],
        "AE. COUNT": [200],
        "MP-BY KIT": [250],
        "M.T. TEST": [300],
        "MAL-PARASITE": [200],
        "WIDAL TEST": [100],
        "V.D.R.L": [200],
        "HCL": [200],
        "BRUCELLA": [850],
        "R.A. FACTOR": [1000],
        "TRIDOT": [25],
        "HBsAg": [200],
        "C.R.P.": [350],
        "DENGUE (IgG/IgM)": [650],
        "CHEKENGUNNYA TEST": [600],
        "ASLO": [1200],
        "Alb": [100],
        "SUGAR": [100],
        "MICRO.": [200],
        "B.SALT & PIGMENT": [200],
        "PREGNANCY TEST": [200],
        "SEMEN ANALYSIS": [500],
        "BL. SUGAR RANDOM": [100],
        "FASTING/PAST LUNCH": [200],
        "Sr. BILIRUBIN": [200],
        "S.GOT.": [200],
        "S.GPT.": [200],
        "UREA": [200],
        "URIC ACID": [200],
        "SERUM ELECTROLYTE": [600],
        "S. CHOLESTEROL": [200],
        "TRIGLYCERIDE": [200],
        "LIPID PROFILE": [650],
        "L.F.T": [650],
        "K.F.T": [600],
        "S. CALCIUM": [200],
        "THYROID PROFILE": [700],
        "T3, T4, TSH": [750],
        "CD4, CD8": [2200],
        "WESTREN’S BLOT": [3000],
        "HBA1C": [850],
    }

    # ------------------------ Test Selection ------------------------
    st.subheader("Select Diagnostic Tests")

    # Multi-selection of tests
    selected_tests = st.multiselect(
        "Choose Tests to Add",
        options=list(test_data.keys()),
        key="test_select"
    )

    # Display selected tests with their prices
    if selected_tests:
        st.write("### Selected Tests with Prices:")
        total_amount = 0
        for test in selected_tests:
            selected_price = test_data[test][0]  # Taking the first price option
            total_amount += selected_price
            st.write(f"{test}: ₹{selected_price}")
        st.write(f"### Total Amount: ₹{total_amount}")

    # Add Next Button to proceed
    if st.button("Next", key="next_page"):
        st.session_state.current_page = 2  # Move to next page

# -------------------- Page 2: Patient Report --------------------
elif st.session_state.current_page == 2:
    st.title("Dr. Pujar Hospital Diagnostic Laboratory")
    st.markdown("---")

    # Display hospital details in the report
    st.write("### Hospital Information")
    st.write("**Hospital Name**: Dr. Pujar Hospital Diagnostic Laboratory")
    st.write("**Address**: Dr. Pujar Road, City XYZ")
    st.write("**Phone**: +123 456 7890")
    st.write("**Email**: info@drpujarhospital.com")
    st.write("---")

    # Display patient details
    st.write(f"**Patient Name**: {st.session_state.name}")
    st.write(f"**Age / Sex**: {st.session_state.age} / {st.session_state.sex}")
    st.write(f"**Date**: {st.session_state.date.strftime('%d-%m-%Y')}")

    # Display the referred doctor(s)
    if st.session_state.referred_doctors:
        st.write(f"**Referred By**: {', '.join(st.session_state.referred_doctors)}")
    
    st.write("### Tests & Results:")
    
    # Display the selected tests and total amount
    total_amount = 0
    for test in selected_tests:
        selected_price = test_data[test][0]  # Taking the first price option
        total_amount += selected_price
        st.write(f"{test}: ₹{selected_price}")

    # Total amount
    st.write(f"### Total Amount: ₹{total_amount}")

    # Add Next Button to proceed to final print
    if st.button("Next", key="final_report"):
        st.write("Generating the report...")  # Simulating next step
