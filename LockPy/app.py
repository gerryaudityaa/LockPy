import sys
import logging
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QStatusBar
)
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from .encryption import generate_key, encrypt_file, decrypt_file
from .utils import setup_logging

class EncryptionThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, key, file_path, mode):
        super().__init__()
        self.key = key
        self.file_path = file_path
        self.mode = mode  # 'encrypt' or 'decrypt'

    def run(self):
        try:
            if self.mode == 'encrypt':
                encrypt_file(self.key, self.file_path)
                self.finished.emit(f"File encrypted successfully: {self.file_path}")
            else:
                decrypt_file(self.key, self.file_path)
                self.finished.emit(f"File decrypted successfully: {self.file_path}")
        except Exception as e:
            self.finished.emit(f"Error: {str(e)}")

class EncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LockPy - File Encryption Tool")
        self.setGeometry(100, 100, 500, 300)
        self.setWindowIcon(QIcon("icon.png"))  # Add an icon

        # Initialize key
        self.key = None

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # File selection
        self.file_path = QLineEdit(self)
        self.file_path.setReadOnly(True)
        browse_button = QPushButton("Browse", self)
        browse_button.clicked.connect(self.browse_file)
        layout.addWidget(QLabel("File to Encrypt/Decrypt:"))
        layout.addWidget(self.file_path)
        layout.addWidget(browse_button)

        # Key management
        self.key_label = QLabel("Key: Not Loaded", self)
        generate_key_button = QPushButton("Generate Key", self)
        generate_key_button.clicked.connect(self.generate_key)
        save_key_button = QPushButton("Save Key", self)
        save_key_button.clicked.connect(self.save_key)
        load_key_button = QPushButton("Load Key", self)
        load_key_button.clicked.connect(self.load_key)
        layout.addWidget(self.key_label)
        layout.addWidget(generate_key_button)
        layout.addWidget(save_key_button)
        layout.addWidget(load_key_button)

        # Actions
        encrypt_button = QPushButton("Encrypt", self)
        encrypt_button.clicked.connect(self.encrypt_file)
        decrypt_button = QPushButton("Decrypt", self)
        decrypt_button.clicked.connect(self.decrypt_file)
        layout.addWidget(encrypt_button)
        layout.addWidget(decrypt_button)

        # Status bar
        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            self.file_path.setText(file_path)

    def generate_key(self):
        self.key = generate_key()
        self.key_label.setText("Key: Generated")
        logging.info("Encryption key generated.")
        QMessageBox.information(self, "Key Generated", "A new encryption key has been generated.")

    def save_key(self):
        if self.key:
            key_file_path, _ = QFileDialog.getSaveFileName(self, "Save Key", "", "Key Files (*.key)")
            if key_file_path:
                with open(key_file_path, 'wb') as key_file:
                    key_file.write(self.key)
                logging.info(f"Encryption key saved to {key_file_path}.")
                QMessageBox.information(self, "Key Saved", "The encryption key has been saved.")
        else:
            logging.warning("Attempted to save key, but no key was generated.")
            QMessageBox.warning(self, "No Key", "No encryption key has been generated.")

    def load_key(self):
        key_file_path, _ = QFileDialog.getOpenFileName(self, "Load Key", "", "Key Files (*.key)")
        if key_file_path:
            with open(key_file_path, 'rb') as key_file:
                self.key = key_file.read()
            self.key_label.setText("Key: Loaded")
            logging.info(f"Encryption key loaded from {key_file_path}.")
            QMessageBox.information(self, "Key Loaded", "The encryption key has been loaded.")

    def encrypt_file(self):
        if not self.key:
            logging.warning("No encryption key loaded.")
            QMessageBox.warning(self, "No Key", "No encryption key has been loaded or generated.")
            return

        file_path = self.file_path.text()
        if not file_path:
            logging.warning("No file selected for encryption.")
            QMessageBox.warning(self, "No File", "No file has been selected.")
            return

        self.thread = EncryptionThread(self.key, file_path, 'encrypt')
        self.thread.finished.connect(self.status_bar.showMessage)
        self.thread.start()

    def decrypt_file(self):
        if not self.key:
            logging.warning("No encryption key loaded.")
            QMessageBox.warning(self, "No Key", "No encryption key has been loaded or generated.")
            return

        file_path = self.file_path.text()
        if not file_path:
            logging.warning("No file selected for decryption.")
            QMessageBox.warning(self, "No File", "No file has been selected.")
            return

        self.thread = EncryptionThread(self.key, file_path, 'decrypt')
        self.thread.finished.connect(self.status_bar.showMessage)
        self.thread.start()

def main():
    setup_logging()
    app = QApplication(sys.argv)
    window = EncryptionApp()
    window.show()
    sys.exit(app.exec_())