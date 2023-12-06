def decrypt_shift_cipher(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def break_shift_cipher(ciphertext):
    for shift in range(1, 26):
        decrypted_text = decrypt_shift_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    break_shift_cipher(ciphertext)
