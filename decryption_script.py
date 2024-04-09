import os
from cryptography.fernet import Fernet

def decrypt_file(key, filepath):
    # Generate cipher using the encryption key
    cipher = Fernet(key)

    # Read the encrypted file content
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()

    # Decrypt the file content
    decrypted_data = cipher.decrypt(encrypted_data)

    # Write the decrypted data back to the file
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

def decrypt_files_in_directory(key, directory, target_extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)

            # Check if the file has any of the target extensions
            _, file_extension = os.path.splitext(file)
            if file_extension in target_extensions:
                decrypt_file(key, filepath)

def load_key_from_file(key_file_path):
    with open(key_file_path, 'rb') as key_file:
        return key_file.read()

if __name__ == "__main__":
    # Specify the directory to decrypt
    directory_to_decrypt = 'testdir/'

    # Specify the target file extensions to decrypt (e.g., ['.txt', '.docx'])
    target_extensions = ['.txt', '.pdf', '.csv', '.docx', '.mp4']

    # Specify the file path from which to load the key
    key_file_path = 'encryption_key.key'

    # Load the encryption key from the file
    encryption_key = load_key_from_file(key_file_path)

    # Decrypt files with the target extensions in the directory
    decrypt_files_in_directory(encryption_key, directory_to_decrypt, target_extensions)
