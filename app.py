import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Lab Billing System", layout="centered")

st.title("🧾 We Care Diagnostic Laboratory Billing System")
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

# ------------------------ Session State Init ------------------------
if "selected_tests" not in st.session_state:
    st.session_state.selected_tests = []

# ------------------------ Test Selection ------------------------
st.subheader("🧪 Select Diagnostic Tests")

test_list = list(test_data.keys())
test = st.selectbox("Choose a Test", ["-- Select --"] + test_list, index=0, key="test_select")

if test != "-- Select --":
    price_options = test_data[test]
    selected_price = st.selectbox(f"Select Price for {test}", price_options, key="price_select")

    if st.button("✅ Add Test"):
        if (test, selected_price) not in st.session_state.selected_tests:
            st.session_state.selected_tests.append((test, selected_price))
            st.success(f"Added {test} - ₹{selected_price}")
        else:
            st.warning(f"{test} (₹{selected_price}) is already added.")
        st.experimental_rerun()  # reset dropdowns by rerunning

# ------------------------ Show Selected Tests ------------------------
if st.session_state.selected_tests:
    st.markdown("### 📝 Selected Tests:")
    total_amount = 0
    for i, (t, p) in enumerate(st.session_state.selected_tests, 1):
        st.write(f"{i}. {t} - ₹{p}")
        total_amount += p

    # ------------------------ Final Bill ------------------------
    st.markdown("---")
    st.subheader("🧾 Final Bill")
    st.write(f"**Patient Name:** {name}")
    st.write(f"**Age / Sex:** {age} / {sex}")
    st.write(f"**Date:** {date.strftime('%d-%m-%Y')}")
    st.write(f"**Referred By:** {referred_by}")
    st.markdown(f"### 💰 Total Amount: ₹{total_amount}")

    # Print button (browser-based)
    st.markdown("""
        <br>
        <button onclick="window.print()" style="padding:10px 20px;font-size:16px;">🖨️ Print Bill</button>
        <br><br>
    """, unsafe_allow_html=True)

    # Clear Tests Button
    if st.button("🔄 Clear All Tests"):
        st.session_state.selected_tests.clear()
        st.success("Test list cleared.")
