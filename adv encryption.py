# Import libraries
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import os
import base64


def encrypt_file(input_file, password):
    # Ensure the password is exactly 32 bytes (for AES-256 key size)
    key = password.encode().ljust(32)[:32]
    
    # Generate a random 16-byte initialization vector (IV)
    iv = os.urandom(16)
    
    # Create a cipher object using AES in CFB mode with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read the plaintext data from the input file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Encrypt the plaintext
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Write the IV followed by the ciphertext to the output file
    with open(f"{input_file}.enc", 'wb') as f:
        f.write(iv + ciphertext)
    print(f"Encrypted file saved as {input_file}.enc")


def decrypt_file(input_file, password):
    # Ensure the password is exactly 32 bytes (for AES-256 key size)
    key = password.encode().ljust(32)[:32]

    # Read the IV (first 16 bytes) and ciphertext from the input file
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    # Create a cipher object using AES in CFB mode with the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Write the decrypted data to a new file
    output_file = input_file.replace('.enc', '.dec')
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    print(f"Decrypted file saved as {output_file}")


# Example usage
file_to_encrypt = 'noodles.txt'  # File to encrypt
user_password = 'strongpassword'  # Password for encryption and decryption
encrypt_file(file_to_encrypt, user_password)  # Encrypt the file
decrypt_file(f"{file_to_encrypt}.enc", user_password)  # Decrypt the file
