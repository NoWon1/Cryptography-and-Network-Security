def caesar_cipher(text, key, decrypt=False):
    result = ""
    shift = -key if decrypt else key
    
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

plaintext = input("Enter plaintext: ")
keys = [int(k) for k in input("Enter keys (comma-separated): ").split(',')]

for key in keys:
    encrypted = caesar_cipher(plaintext, key)
    decrypted = caesar_cipher(encrypted, key, decrypt=True)
    
    print(f"\nKey = {key}")
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print(f"Verification: {'Success' if plaintext == decrypted else 'Failed'}")
