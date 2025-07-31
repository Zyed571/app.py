import streamlit as st
from datetime import datetime

st.set_page_config(page_title="We Care Diagnostic Laboratory Billing", layout="centered")

# -------------------- CSS for Professional Look & Print --------------------
st.markdown("""
    <style>
    body { font-family: 'Segoe UI', sans-serif; }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
        margin: auto;
    }

    .section-header {
        font-size: 18px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 10px;
        color: #2e2e2e;
    }

    .test-box {
        background-color: #f1f1f1;
        padding: 8px 12px;
        border-radius: 5px;
        margin-bottom: 6px;
    }

    @media print {
        .stButton, .stSelectbox, .stTextInput, .stNumberInput, .stRadio, .stDateInput, .stSelectbox label,
        .stTextInput label, .stNumberInput label, .stRadio label, .stDateInput label, footer, header {
            display: none !important;
        }

        .test-box {
            background: none;
            border: none;
            padding: 0;
            margin: 0;
        }

        body {
            font-size: 14px;
            color: black;
        }

        .section-header {
            margin-top: 20px;
            font-size: 16px;
            font-weight: bold;
        }

        html, body {
            margin: 0;
            padding: 0;
        }
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- Session State --------------------
if "selected_tests" not in st.session_state:
    st.session_state.selected_tests = []
if "test_counter" not in st.session_state:
    st.session_state.test_counter = 0

# -------------------- Title --------------------
st.title("We Care Diagnostic Laboratory Billing")
st.markdown("---")

# -------------------- Patient Details --------------------
st.markdown('<div class="section-header">Patient Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Patient's Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
with col2:
    sex = st.radio("Sex", ["Male", "Female", "Other"], horizontal=True)
    date = st.date_input("Date", value=datetime.now().date())

# -------------------- Doctor Referral --------------------
st.markdown('<div class="section-header">Referred By</div>', unsafe_allow_html=True)

num_doctors = st.selectbox("Number of referring doctors", range(1, 11), index=0)
referred_by_list = [
    st.text_input(f"Doctor {i+1}", key=f"doc_{i}")
    for i in range(num_doctors)
]
referred_by = ", ".join([doc for doc in referred_by_list if doc.strip() != ""])

# -------------------- Test Data --------------------
test_data = {
    "CBC": [300, 350], "Hb%": [100], "TC/DC": [100], "Platelet Count": [100],
    "ESR": [200], "BL. GROUP & RH TYPE": [100], "BT/CT": [150], "AE. COUNT": [200],
    "MP-BY KIT": [250], "M.T. TEST": [300], "MAL-PARASITE": [200], "WIDAL TEST": [100],
    "V.D.R.L": [200], "HCL": [200], "BRUCELLA": [850], "R.A. FACTOR": [1000],
    "TRIDOT": [25], "HBsAg": [200], "C.R.P.": [350], "DENGUE (IgG/IgM)": [650],
    "CHEKENGUNNYA TEST": [600], "ASLO": [1200], "Alb": [100], "SUGAR": [100],
    "MICRO.": [200], "B.SALT & PIGMENT": [200], "PREGNANCY TEST": [200],
    "SEMEN ANALYSIS": [500], "BL. SUGAR RANDOM": [100], "FASTING/PAST LUNCH": [200],
    "Sr. BILIRUBIN": [200], "S.GOT.": [200], "S.GPT.": [200], "UREA": [200],
    "URIC ACID": [200], "SERUM ELECTROLYTE": [600], "S. CHOLESTEROL": [200],
    "TRIGLYCERIDE": [200], "LIPID PROFILE": [650], "L.F.T": [650], "K.F.T": [600],
    "S. CALCIUM": [200], "THYROID PROFILE": [700], "T3, T4, TSH": [750],
    "CD4, CD8": [2200], "WESTREN’S BLOT": [3000], "HBA1C": [850],
}

# -------------------- Test Selection --------------------
st.markdown('<div class="section-header">Diagnostic Test Selection</div>', unsafe_allow_html=True)

with st.form(key=f"add_test_form_{st.session_state.test_counter}"):
    test = st.selectbox("Select a Test", ["-- Select --"] + list(test_data.keys()), key=f"test_{st.session_state.test_counter}")
    if test != "-- Select --":
        price = st.selectbox(f"Price for {test}", test_data[test], key=f"price_{st.session_state.test_counter}")
        submitted = st.form_submit_button("Add Test")
        if submitted:
            if (test, price) not in st.session_state.selected_tests:
                st.session_state.selected_tests.append((test, price))
                st.session_state.test_counter += 1
                st.rerun()
            else:
                st.warning("This test is already added.")

# -------------------- Display Selected Tests --------------------
if st.session_state.selected_tests:
    st.markdown('<div class="section-header">Selected Tests</div>', unsafe_allow_html=True)
    total = 0
    for i, (test, price) in enumerate(st.session_state.selected_tests, start=1):
        st.markdown(f"<div class='test-box'>{i}. {test} — ₹{price}</div>", unsafe_allow_html=True)
        total += price

    # -------------------- Final Bill --------------------
    st.markdown('<div class="section-header">Final Bill Summary</div>', unsafe_allow_html=True)
    st.write(f"**Patient Name:** {name}")
    st.write(f"**Age / Sex:** {age} / {sex}")
    st.write(f"**Date:** {date.strftime('%d-%m-%Y')}")
    st.write(f"**Referred By:** {referred_by}")
    st.markdown(f"### Total Amount: ₹{total}")

    # -------------------- Print Button --------------------
    st.markdown("""
        <br>
        <button onclick="window.print()" style="padding:10px 20px;font-size:16px;">
            Print Report
        </button>
        <br><br>
    """, unsafe_allow_html=True)

    # -------------------- Clear Button --------------------
    if st.button("Clear All Tests"):
        st.session_state.selected_tests.clear()
        st.session_state.test_counter = 0
        st.success("All tests cleared.")
        st.rerun()
