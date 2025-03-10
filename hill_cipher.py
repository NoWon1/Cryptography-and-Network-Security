import numpy as np

def hill_cipher(plaintext, key):
    plaintext = ''.join(c for c in plaintext.upper() if c.isalpha())
    key = key.upper()
    
    key_matrix = np.zeros((2, 2), dtype=int)
    for i in range(2):
        for j in range(2):
            key_matrix[i][j] = ord(key[(i*2+j) % len(key)]) - ord('A')
    
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        p = [ord(plaintext[i]) - ord('A'), ord(plaintext[i+1]) - ord('A')]
        c = np.dot(key_matrix, p) % 26
        ciphertext += ''.join(chr(int(x) + ord('A')) for x in c)
    
    return ciphertext

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = hill_cipher(plaintext, key)

print(f"\nKey: {key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"DeCiphertext: {plaintext}")