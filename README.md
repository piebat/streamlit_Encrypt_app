# A Streamlit python application to Encrypt and Decript file to disk
## Secure Folder Encryption &amp; Decryption App
The App has been created by chatGPT and tested by me.
It works and it is anmaizing how simple it was.

The prompts were: 
- python script to encrypt and decript file on disk
- Can you create a strimlit app fro it?


### Install Dependencies:
Ensure you have the necessary libraries installed:
```bash
pip install streamlit cryptography
```

### How the Streamlit App Works:
1. **Key Generation/Upload**: 
   - You can either generate a new encryption key and download it, or upload an existing key for encryption/decryption.
2. **Encrypt/Decrypt Files**: 
   - Upload a file for encryption or decryption. Based on the chosen action, the file will be processed, and you can download the result.
   - If you choose encryption, the file will be saved as `<filename>.encrypted`.
   - If you choose decryption, the `.encrypted` extension is removed from the file name.

### Running the App:
Run the app with the following command:
```bash
streamlit run streamlit_encrypt_decrypt_app.py
```

This will launch a Streamlit app in your browser where you can interact with the encryption/decryption functionality through a simple user interface.

### Features:
- **Generate New Key**: Generates a new encryption key, which you can download.
- **Upload Key**: Allows the user to upload an existing encryption key for decryption or encryption.
- **File Upload**: Upload a file to either encrypt or decrypt.
- **File Download**: After processing, the resulting encrypted or decrypted file can be downloaded.

Let me know if you need further customizations!
