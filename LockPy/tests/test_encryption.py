import os
import tempfile
from cryptography.fernet import Fernet
from LockPy.encryption import generate_key, encrypt_file, decrypt_file

def test_encryption_decryption():
    key = generate_key()
    test_data = b"Hello, World!"

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(test_data)
        temp_file_path = temp_file.name

    try:
        # Encrypt the file
        encrypt_file(key, temp_file_path)

        # Decrypt the file
        decrypt_file(key, temp_file_path)

        # Verify the decrypted data
        with open(temp_file_path, 'rb') as file:
            decrypted_data = file.read()
        assert decrypted_data == test_data, "Decrypted data does not match original data."
    finally:
        os.remove(temp_file_path)