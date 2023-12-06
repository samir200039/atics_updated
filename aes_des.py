from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes


def pad(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    padded_data = data + bytes([padding_length] * padding_length)
    return padded_data


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_data = pad(plaintext, 8)  # 8 bytes block size for DES
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext


def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)
    return plaintext


def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(plaintext, 16)  # 16 bytes block size for AES
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext


def aes_decrypt(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data)
    return plaintext


# Example usage:
des_key = b"abcdefgh"  # 8 bytes key for DES
aes_key = get_random_bytes(16)  # 16 bytes key for AES

plaintext = b"Hello, DES and AES!"

des_encrypted = des_encrypt(des_key, plaintext)
des_decrypted = des_decrypt(des_key, des_encrypted)

aes_encrypted = aes_encrypt(aes_key, plaintext)
aes_decrypted = aes_decrypt(aes_key, aes_encrypted)

print("Original text:", plaintext)
print("DES Encrypted:", des_encrypted)
print("DES Decrypted:", des_decrypted)
print("AES Encrypted:", aes_encrypted)
print("AES Decrypted:", aes_decrypted)
