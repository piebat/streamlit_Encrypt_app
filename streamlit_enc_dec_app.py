import streamlit as st
from cryptography.fernet import Fernet
import os

# Helper functions
def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_data, key):
    fernet = Fernet(key)
    return fernet.encrypt(file_data)

def decrypt_file(file_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(file_data)

# Streamlit app
def main():
    st.title("File Encryption and Decryption")

    # Generate or load key
    key = None
    key_action = st.sidebar.selectbox("Key Actions", ["Generate New Key", "Upload Key"])
    
    if key_action == "Generate New Key":
        key = generate_key()
        st.sidebar.download_button("Download Key", key, file_name="secret.key")
        st.sidebar.write("Key generated and ready to use.")
    else:
        uploaded_key = st.sidebar.file_uploader("Upload Encryption Key", type=["key"])
        if uploaded_key:
            key = uploaded_key.read()

    # If no key is available, stop the app here
    if not key:
        st.warning("Please generate or upload an encryption key to proceed.")
        return

    # Select encryption or decryption
    action = st.selectbox("Action", ["Encrypt File", "Decrypt File"])

    # Upload file
    uploaded_file = st.file_uploader("Upload File", type=None)

    if uploaded_file:
        file_data = uploaded_file.read()

        # Encrypt or Decrypt based on action
        if action == "Encrypt File":
            encrypted_data = encrypt_file(file_data, key)
            st.download_button("Download Encrypted File", encrypted_data, 
                               file_name=uploaded_file.name + ".encrypted")
            st.success("File encrypted successfully!")

        elif action == "Decrypt File":
            try:
                decrypted_data = decrypt_file(file_data, key)
                st.download_button("Download Decrypted File", decrypted_data, 
                                   file_name=uploaded_file.name.replace(".encrypted", ""))
                st.success("File decrypted successfully!")
            except Exception as e:
                st.error("Error decrypting the file. Please check if you are using the correct key.")

if __name__ == "__main__":
    main()