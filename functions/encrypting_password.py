import json
from cryptography.fernet import Fernet


# opening secret key for encoding
with open('./notes/config.json', 'r') as f:
    config = json.load(f)
print(config["secret_key"])

# initialize Fernet class
f = Fernet(config["secret_key"].encode())

# encryption
message = "test"
encmessage = f.encrypt(message.encode())
print("Encrypted: " + str(encmessage.decode()))
print("Original: " + str(f.decrypt(encmessage).decode()))