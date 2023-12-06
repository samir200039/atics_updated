def decrypt_shift_cipher(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text

def break_shift_cipher(ciphertext):
    for shift in range(26):
        decrypted_text = decrypt_shift_cipher(ciphertext, shift)
        print(f"shift {shift}:{decrypted_text}")

ciphertext = input("enter the shift cipher ciphertext: ")
break_shift_cipher(ciphertext)
