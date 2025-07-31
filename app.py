# -------------------- Page 2: Patient Report --------------------
if st.session_state.current_page == 2:
    st.title("Dr. Pujar Hospital Diagnostic Laboratory Report")
    st.markdown("---")
    
    # Display patient details and selected tests
    st.write(f"**Patient Name**: {st.session_state.name}")
    st.write(f"**Age / Sex**: {st.session_state.age} / {st.session_state.sex}")
    st.write(f"**Date**: {st.session_state.date.strftime('%d-%m-%Y')}")
    
    # Display referred doctors - Each doctor on a new line
    if st.session_state.referred_doctors:
        st.write("**Referred By**:")
        for doctor in st.session_state.referred_doctors:
            st.write(f"- {doctor}")

    st.markdown("### Selected Tests and Amounts:")
    total_amount = 0
    for i, (test, price) in enumerate(st.session_state.selected_tests, 1):
        st.write(f"{i}. {test} - ₹{price}")
        total_amount += price

    st.markdown(f"### Total Amount: ₹{total_amount}")
    
    # Signature Option at the Bottom Right
    st.markdown("<div style='position: fixed; bottom: 10px; right: 10px;'>", unsafe_allow_html=True)
    st.subheader("Signature:")
    signature = st.text_input("Sign here (Type your name)", key="signature")
    st.markdown("</div>", unsafe_allow_html=True)

    if signature:
        st.write(f"**Signature**: {signature}")
