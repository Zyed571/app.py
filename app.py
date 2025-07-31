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
    
    # Multiselect to select multiple doctors
    selected_doctors = st.multiselect("Select Referred Doctors", doctor_options, key="referred_doctors")

    # Save selected doctors to session state immediately (use the set method for setting mutable types)
    if selected_doctors != st.session_state.referred_doctors:
        st.session_state.referred_doctors = selected_doctors

    # ------------------------ Test Selection ------------------------
    st.subheader("Select Diagnostic Tests")
    
    test_list = list(test_data.keys())
    selected_test = st.selectbox("Choose a Test", ["-- Select --"] + test_list, key="selected_test")
    
    if selected_test != "-- Select --":
        price_options = test_data[selected_test]
        selected_price = st.selectbox(f"Select Price for {selected_test}", price_options, key="selected_price")
        
        if st.button("Add Test"):
            if selected_test and selected_price:
                st.session_state.selected_tests.append((selected_test, selected_price))
                st.success(f"Added {selected_test} - ₹{selected_price}")
            else:
                st.error("Please select both a test and a price option.")
        
    # ------------------------ Display Selected Tests ------------------------
    if st.session_state.selected_tests:
        st.markdown("### Selected Tests:")
        total_amount = 0
        for i, (test, price) in enumerate(st.session_state.selected_tests, 1):
            st.write(f"{i}. {test} - ₹{price}")
            total_amount += price

    # ------------------------ Navigation ------------------------
    if st.button("Next"):
        st.session_state.current_page = 2  # Move to the next page

# -------------------- Page 2: Patient Report --------------------
if st.session_state.current_page == 2:
    st.title("Dr. Pujar Hospital Diagnostic Laboratory Report")
    st.markdown("---")
    
    # Display patient details and selected tests
    st.write(f"**Patient Name**: {st.session_state.name}")
    st.write(f"**Age / Sex**: {st.session_state.age} / {st.session_state.sex}")
    st.write(f"**Date**: {st.session_state.date.strftime('%d-%m-%Y')}")
    
    # Display referred doctors
    if st.session_state.referred_doctors:
        st.write("**Referred By**: " + ", ".join(st.session_state.referred_doctors))

    st.markdown("### Selected Tests and Amounts:")
    total_amount = 0
    for i, (test, price) in enumerate(st.session_state.selected_tests, 1):
        st.write(f"{i}. {test} - ₹{price}")
        total_amount += price

    st.markdown(f"### Total Amount: ₹{total_amount}")
