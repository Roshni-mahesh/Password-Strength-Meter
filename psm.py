import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Checker By Roshni Mahesh", page_icon="🔑", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
    .stButton button:hover {background-color: #45a049; center:center}
</style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔐 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1  # Increase score by 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback
    if feedback:
        with st.expander("🔍 **Improve your Password**"):
            for item in feedback:
                st.write(item)

# User input
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

# Button action
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
