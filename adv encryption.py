from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
import os
import base64


def encrypt_file(input_file, password):
    key = password.encode().ljust(32)[:32]
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(input_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(f"{input_file}.enc", 'wb') as f:
        f.write(iv + ciphertext)
    print(f"Encrypted file saved as {input_file}.enc")


def decrypt_file(input_file, password):
    key = password.encode().ljust(32)[:32]
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    output_file = input_file.replace('.enc', '.dec')
    with open(output_file, 'wb') as f:
        f.write(plaintext)
    print(f"Decrypted file saved as {output_file}")


# Example usage
file_to_encrypt = 'noodles.txt'
user_password = 'strongpassword'
encrypt_file(file_to_encrypt, user_password)
decrypt_file(f"{file_to_encrypt}.enc", user_password)
