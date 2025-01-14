# 🔐 Advance Encryption Tool

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/2917/2917995.png" alt="Encryption Icon" width="120">
</p>

<p align="center">
  <strong>🔒 A Secure Approach to File Encryption and Decryption with AES-256</strong>
</p>

---

## ⚡ Overview

The **Advance Encryption Tool** is a robust and advanced tool that demonstrates secure file encryption and decryption using the powerful **AES-256** encryption algorithm provided by Python’s `cryptography` library.

- ✅ Encrypt sensitive files with the industry-standard AES-256 encryption.
- ✅ Decrypt encrypted files securely using the same password.
- ✅ Learn how to manage IVs (Initialization Vectors) and handle AES encryption effectively.

---

## 🛠 Features

- 🔑 **Key Derivation and Management**
  - Password-based AES-256 key derivation with padding.
- 🗎 **File Encryption**
  - AES-256 encryption with secure random IVs.
- 🛡 **File Decryption**
  - Restore encrypted files to their original form using the same password.
- 🌐 **Cross-platform Compatibility**
  - Works seamlessly across Windows, macOS, and Linux systems.

---

## 🔠 How It Works

### 🔒 Key Management

1. **Password-based Key Generation**:
   - The user provides a password, which is padded or truncated to 32 bytes (AES-256 requires a 256-bit key).
2. **IV (Initialization Vector)**:
   - A 16-byte random IV is generated for each encryption operation to ensure security and randomness.

### 🗎 File Encryption

1. **Input File**:
   - The file to encrypt is read in binary mode.
2. **AES-256 Encryption**:
   - The file content is encrypted using the AES cipher in **CFB mode** (Cipher Feedback Mode).
3. **Output File**:
   - The IV and encrypted data are saved to a `.enc` file for secure storage.

### 🔒 File Decryption

1. **Input Encrypted File**:
   - The `.enc` file is read in binary mode.
2. **IV and Data Separation**:
   - The first 16 bytes are extracted as the IV, and the remaining bytes are the ciphertext.
3. **AES-256 Decryption**:
   - The ciphertext is decrypted using the same password and IV, restoring the original file.
4. **Output File**:
   - The decrypted data is saved to a `.dec` file.

---

## 📓 Learning Objectives

- 💡 Understand the principles of AES encryption, including modes like CFB.
- 🛡 Learn how to securely generate and handle Initialization Vectors (IV).
- 🔑 Explore password-based key management and 256-bit encryption.
- 🔐 Gain hands-on experience with Python’s `cryptography` library.

---

<p align="center">
  <strong>🔒 Secure Your Data with AES-256. Empower Your Knowledge. 🔐</strong>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/b7df8382-484a-4184-bb45-00165bef1013" alt="Secure Icon" width="80">
</p>

