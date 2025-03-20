# LockPy

LockPy is a secure file encryption tool built with Python and PyQt5. It allows users to encrypt and decrypt files using the Fernet symmetric encryption algorithm. The application features a simple and intuitive graphical user interface (GUI) and supports multi-threading for responsive file operations.

## Features

- **Generate Encryption Keys**: Create a new encryption key for securing files.
- **Save and Load Keys**: Save encryption keys to a file and load them for future use.
- **Encrypt Files**: Securely encrypt files using the generated key.
- **Decrypt Files**: Decrypt files using the corresponding encryption key.
- **Multi-Threading**: Encrypt and decrypt files in the background without freezing the GUI.
- **Logging**: Detailed logging for debugging and tracking operations.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. Clone the repository:
   
   ```bash
   git clone https://github.com/yourusername/LockPy.git
   cd LockPy
   
2. Install the required dependencies:
 
   ```bash
   pip install -r requirements.txt
   
3. Run the application:

   ```bash
   python run.py

### Usage
1. **Generate a Key**: Click "Generate Key" to create a new encryption key.
2. **Save the Key**: Save the key to a file using "Save Key".
3. **Load a Key**: Load a previously saved key using "Load Key".
4. **Select a File**: Use the "Browse" button to select a file for encryption or decryption.
5. **Encrypt/Decrypt**: Click "Encrypt" or "Decrypt" to process the selected file.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Submit a pull request.


## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.