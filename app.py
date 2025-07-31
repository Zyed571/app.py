import streamlit as st
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Lab Billing System", layout="centered")

# Initialize session state variables if not already done
if "selected_tests" not in st.session_state:
    st.session_state.selected_tests = []
if "test_counter" not in st.session_state:
    st.session_state.test_counter = 0
if "current_page" not in st.session_state:
    st.session_state.current_page = 1  # Default to page 1 (test selection)

# -------------------- Page 1: Test Selection --------------------
if st.session_state.current_page == 1:
    st.title("We Care Diagnostic Laboratory Billing System")
    st.markdown("---")

    # ------------------------ Patient Details ------------------------
    st.subheader("Enter Patient Details")
    name = st.text_input("Patient's Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    sex = st.radio("Sex", ["Male", "Female", "Other"])
    date = st.date_input("Date", value=datetime.now().date())

    # ------------------------ Dynamic Doctor Input ------------------------
    num_doctors = st.selectbox("How many doctors referred the patient?", range(1, 11), index=0)
    referred_by_list = [st.text_input(f"Referred By Doctor {i+1}", key=f"doc_{i}") for i in range(num_doctors)]
    referred_by = ", ".join([doc for doc in referred_by_list if doc.strip() != ""])

    st.markdown("---")

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

    # ------------------------ Test Selection Form ------------------------
    st.subheader("Select Diagnostic Tests")

    rerun_needed = False

    with st.form(key=f"add_test_form_{st.session_state.test_counter}"):
        test_list = ["-- Select --"] + list(test_data.keys())
        test = st.selectbox("Select a Test", test_list, key=f"test_{st.session_state.test_counter}")
        price = None
        if test != "-- Select --":
            price = st.selectbox(f"Price for {test}", test_data[test], key=f"price_{st.session_state.test_counter}")
        submitted = st.form_submit_button("Add Test")

        if submitted:
            if test == "-- Select --" or price is None:
                st.warning("Please select a test and price before adding.")
            else:
                if (test, price) not in st.session_state.selected_tests:
                    st.session_state.selected_tests.append((test, price))
                    st.session_state.test_counter += 1
                    rerun_needed = True
                else:
                    st.warning("This test is already added.")

    # Trigger rerun if new test is added
    if rerun_needed:
        st.experimental_rerun()

    # ------------------------ Display Selected Tests with Amount ------------------------
    if st.session_state.selected_tests:
        st.markdown("### Selected Tests with Amount:")
        total_amount = 0
        for i, (test_name, test_price) in enumerate(st.session_state.selected_tests, 1):
            st.write(f"{i}. {test_name} - ₹{test_price}")
            total_amount += test_price

    # ------------------------ Next Button ------------------------
    if st.button("Next"):
        st.session_state.current_page = 2  # Navigate to page 2 (report generation)
        st.experimental_rerun()


# -------------------- Page 2: Report Generation --------------------
elif st.session_state.current_page == 2:
    # Hospital Information
    st.title("We Care Diagnostic Laboratory")
    st.markdown("---")
    st.subheader("Patient Report")

    # Show patient details
    st.write(f"**Patient Name**: {name}")
    st.write(f"**Age / Sex**: {age} / {sex}")
    st.write(f"**Date**: {date.strftime('%d-%m-%Y')}")
    st.write(f"**Referred By**: {referred_by}")

    # Show selected tests and their prices
    st.markdown("### Selected Tests with Amount")
    total_amount = 0
    for i, (test_name, test_price) in enumerate(st.session_state.selected_tests, 1):
        st.write(f"{i}. {test_name} - ₹{test_price}")
        total_amount += test_price

    # Show total amount
    st.markdown(f"### Total Amount: ₹{total_amount}")

    # ------------------------ Back Button (Empty Box with Black Boundary) ------------------------
    st.markdown("---")
    back_button = st.text_area("", "", height=1, key="back_button_report", placeholder="Click here to go back to test selection")

    # Go back to Page 1 (Test Selection) when user clicks on "Go Back"
    if back_button:
        st.session_state.current_page = 1
        st.experimental_rerun()
