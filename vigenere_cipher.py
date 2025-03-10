import string

def vigenere_cipher(text, key, decrypt=False):
    text, key = text.upper(), key.upper()
    shift = -1 if decrypt else 1
    res, j = '', 0
    for c in text:
        if c in string.ascii_uppercase:
            res += chr((ord(c) + shift * (ord(key[j % len(key)]) - 65) - 65) % 26 + 65)
            j += 1
    return res

key = input("Enter key: ")
message = input("Enter message: ")
encrypted = vigenere_cipher(message, key)
print(f"Encrypted: {encrypted}\nDecrypted: {vigenere_cipher(encrypted, key, True)}")