import streamlit as st
import re
import random
import string

# Function to check password strength
def check_password_strength(password):
    # Check password criteria
    length = len(password) >= 8
    uppercase = re.search(r'[A-Z]', password) is not None
    lowercase = re.search(r'[a-z]', password) is not None
    digit = re.search(r'[0-9]', password) is not None
    special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate strength score
    score = sum([length, uppercase, lowercase, digit, special_char])
    
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

# Function to generate a strong password
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Function to check if the password is common
def is_common_password(password):
    try:
        with open("common_passwords.txt", "r") as f:
            common_passwords = f.read().splitlines()
        return password in common_passwords
    except FileNotFoundError:
        st.warning("⚠️ 'common_passwords.txt' file not found. Skipping common password check.")
        return False

# Streamlit App
def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔒", layout="centered")

    # Title and description
    st.title("🔒 Password Strength Checker")
    st.write("Check the strength of your password or generate a secure one.")

    # Tabs for different functionalities
    tab1, tab2 = st.tabs(["Check Password Strength", "Generate Strong Password"])

    with tab1:
        st.header("Check Password Strength")
        password = st.text_input("Enter your password:", type="password")
        if st.button("Check Strength"):
            if password:
                strength = check_password_strength(password)
                st.success(f"Password Strength: **{strength}**")
                if is_common_password(password):
                    st.error("⚠️ Warning: This password is too common!")
            else:
                st.warning("Please enter a password.")

    with tab2:
        st.header("Generate Strong Password")
        length = st.number_input("Password length:", min_value=8, max_value=50, value=12)
        if st.button("Generate Password"):
            generated_password = generate_strong_password(length)
            st.success("Generated Password:")
            st.code(generated_password)
            strength = check_password_strength(generated_password)
            st.success(f"Password Strength: **{strength}**")

# Run the app
if __name__ == "__main__":
    main()