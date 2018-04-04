# Requires "cryptography" (pip install cryptography)
from cryptography.fernet import Fernet
choice = input("Would you like to encrypt or decrypt? (encrypt) (decrypt) ").lower()
if (choice == "encrypt"):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    textToEncrypt = str.encode(input("Please input the text to encrypt: "))
    encryptedText = cipher_suite.encrypt(textToEncrypt)
    print(encryptedText.decode())
    displayKey = input("Would you like to display the encryption key so text can be decrypted later? (Yes) (No)").lower()
    if (displayKey == "yes"):
        print(key.decode())
elif (choice == "decrypt"):
    key = str.encode(input("Please enter the encryption key: "))
    cipher_suite = Fernet(key)
    encryptedText = str.encode(input("Please enter the encrypted text: "))
    decryptedText = cipher_suite.decrypt(encryptedText)
    print(decryptedText.decode())