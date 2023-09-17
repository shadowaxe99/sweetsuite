```python
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

class DataEncryption:

    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode())
        encrypted_data = {
            'ciphertext': b64encode(ciphertext).decode('utf-8'),
            'cipher_tag': b64encode(tag).decode('utf-8'),
            'nonce': b64encode(cipher.nonce).decode('utf-8'),
        }
        return encrypted_data

    def decrypt(self, encrypted_data):
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=b64decode(encrypted_data['nonce']))
        plaintext = cipher.decrypt_and_verify(b64decode(encrypted_data['ciphertext']), b64decode(encrypted_data['cipher_tag']))
        return plaintext.decode()

# Usage
key = get_random_bytes(32)  # AES-256
data_encryption = DataEncryption(key)
encrypted_data = data_encryption.encrypt('Investor data')
decrypted_data = data_encryption.decrypt(encrypted_data)
```