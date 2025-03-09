import streamlit as st
import re
import random
import string


# custom css
st.markdown(
    """
    <style>
        .stApp{
            background-color:  #9ef7e4 !important;
            color: #4b7171; 
        }
        .stApp h1, h2, h3 {
            color: #116767 !important;
        }
        div.stButton > button{
            background-color: #116767 ;
            color: #9ef7e4 !important;
            border: none;
        }
        .stApp label{
            color:#7d8888;
        }
        div.stButton > button:hover{
            border: none;
            color : #116767 !important;
            background-color: #88d7c6;
        }
    """,
    unsafe_allow_html= True
)

# random strong password generator
def generate_password(length=12):
    # ✅ Check if password length is valid:
    if length < 8:
        return "⚠️ Password should be at least 8 characters long!"
    
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*")
    
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining_length = length - 4

    random_chars = ''.join(random.choice(all_characters) for _ in range(remaining_length))
    
    # ✅ Combine all characters and shuffle them
    password = list(uppercase + lowercase + digit + special + random_chars)
    random.shuffle(password)

    return ''.join(password)

# strength checker and also check the password should be new one
def password_strength(password):
    last_10_passwords:list = []
    strength = 0
    errors = []

    # save the last ten passwords and check the current password is not in the list;
    if len(last_10_passwords) == 10:
        last_10_passwords.pop(0)

    # make sure the new password is not in the list
    if password in last_10_passwords:
        return("The password you have already tried. Please try a new one.")
        
    # add new password in the list
    last_10_passwords.append(password)

    # Check password length
    if len(password) < 8:
        errors.append('Password should be at least 8 characters long.')
    else:
        strength += 1

    # Check for digits
    if not re.search(r"\d", password):
        errors.append('Password should contain at least one digit.')
    else:
        strength += 1

    # Check for uppercase letters
    if not re.search(r"[A-Z]", password):
        errors.append('Password should contain at least one uppercase letter.')
    else:
        strength += 1

    # Check for lowercase letters
    if not re.search(r"[a-z]", password):
        errors.append('Password should contain at least one lowercase letter.')
    else:
        strength += 1

    # Check for special characters
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append('Password should contain at least one special character.')
    else:
        strength += 1

    return strength, errors

def main():
    # main title and content
    st.title("Password Generator and Strength Meter Tool")
    st.subheader("Secure Your Online Presence:")
    st.write("Use our **Password Generator and Strength Meter Tool** to protect your online accounts and sensitive information.")

    # tips for strong password
    st.write()
    st.header("Password Perfection")
    st.write("Learn the Secrets to Creating Unhackable Passwords")
    secrets = [
        "Password should be at least 8 characters long.",
        "Password should contain at least one uppercase letter.",
        "Password should contain at least one lowercase letter.",
        "Password should contain at least one digit.",
        "Password should contain at least one special character.(!, @, #, $, %, ^, &, *)",
        "Avoid common passwords.",
    ]
    for secret in secrets:
        st.write(f"* {secret}")

    # password generator
    st.write()
    st.header("Password Generator")
    st.write("Generate strong and unique password with a single click.\nSave your time, save your energy.")
    st.write("Select a length and click the **Generate Password** button!")
    
    # Let user select password length
    length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
    
    if st.button("Generate password"):
        new_password = generate_password(length)
        st.success(f"Your generated password: {new_password}")
        
        # ✅ Copy to Clipboard Button
        st.write("Copy to clipboard")
        st.code(new_password, language="")

    # strength meter
    st.write()
    st.header("Password Strength Meter")
    st.write("Check the strength of your password and get feedback on how to improve it.")
    password = st.text_input("Enter your password", type="password")

    if st.button("Check Strength"):
        if password:
            strength, errors = password_strength(password)
    
            if strength == 5:
                st.write(F"Passwords's Strength: {strength}/5")
                st.success("Password is strong!")
            elif strength >= 3:
                st.write(F"Passwords's Strength: {strength}/5")
                st.warning("Password strength is medium.")
            else:
                st.write(F"Passwords's Strength: {strength}/5")
                st.error("Password is weak.")
    
            if errors:
                st.subheader("For Strong Password:")
                for error in errors:
                    st.write(f"* {error}")

if __name__ == "__main__":
    main()
