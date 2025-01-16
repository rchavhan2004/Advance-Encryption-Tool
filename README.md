# Advance Encryption Tool

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : ROHIT CHAVHAN

**INTERN ID** : CT08JJO

**DOMAIN** : Cyber-Security & Ethical Hacking

**BATCH DURATION** : JANUARY 5th,2025 to FEBRUARY 5th,2025

**MENTOR NAME** : 

## DESCRIPTION

The **Advance Encryption Tool** is a robust and advanced tool that demonstrates secure file encryption and decryption using the powerful **AES-256** encryption algorithm provided by Python’s `cryptography` library.

-  Encrypt sensitive files with the industry-standard AES-256 encryption.
-  Decrypt encrypted files securely using the same password.
-  Learn how to manage IVs (Initialization Vectors) and handle AES encryption effectively.

---

## Features

-  **Key Derivation and Management**
  - Password-based AES-256 key derivation with padding.
-  **File Encryption**
  - AES-256 encryption with secure random IVs.
-  **File Decryption**
  - Restore encrypted files to their original form using the same password.
-  **Cross-platform Compatibility**
  - Works seamlessly across Windows, macOS, and Linux systems.

---

## How It Works

### Key Management

1. **Password-based Key Generation**:
   - The user provides a password, which is padded or truncated to 32 bytes (AES-256 requires a 256-bit key).
2. **IV (Initialization Vector)**:
   - A 16-byte random IV is generated for each encryption operation to ensure security and randomness.

### File Encryption

1. **Input File**:
   - The file to encrypt is read in binary mode.
2. **AES-256 Encryption**:
   - The file content is encrypted using the AES cipher in **CFB mode** (Cipher Feedback Mode).
3. **Output File**:
   - The IV and encrypted data are saved to a `.enc` file for secure storage.

### File Decryption

1. **Input Encrypted File**:
   - The `.enc` file is read in binary mode.
2. **IV and Data Separation**:
   - The first 16 bytes are extracted as the IV, and the remaining bytes are the ciphertext.
3. **AES-256 Decryption**:
   - The ciphertext is decrypted using the same password and IV, restoring the original file.
4. **Output File**:
   - The decrypted data is saved to a `.dec` file.

---
