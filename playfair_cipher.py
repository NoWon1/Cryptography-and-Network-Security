def create_playfair_square(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    square = ''.join(dict.fromkeys(key + alphabet))
    return [square[i:i+5] for i in range(0, 25, 5)]

def find_position(square, char):
    for i, row in enumerate(square):
        if char in row:
            return i, row.index(char)

def playfair_cipher(message, key, decrypt=False):
    square = create_playfair_square(key)
    message = ''.join(c for c in message.upper().replace('J', 'I') if c.isalpha())
    
    if not decrypt:
        i = 0
        while i < len(message) - 1:
            if message[i] == message[i+1]:
                message = message[:i+1] + 'X' + message[i+1:]
            i += 1
        if len(message) % 2 != 0:
            message += 'X'
    
    result = ""
    for i in range(0, len(message), 2):
        if i+1 < len(message):
            a, b = message[i], message[i+1]
            row1, col1 = find_position(square, a)
            row2, col2 = find_position(square, b)
            
            if row1 == row2:
                result += square[row1][(col1 + (1 if not decrypt else -1)) % 5]
                result += square[row2][(col2 + (1 if not decrypt else -1)) % 5]
            elif col1 == col2:
                result += square[(row1 + (1 if not decrypt else -1)) % 5][col1]
                result += square[(row2 + (1 if not decrypt else -1)) % 5][col2]
            else:
                result += square[row1][col2]
                result += square[row2][col1]
    
    return result

plaintext = input("Enter plaintext: ")
key = input("Enter key: ")
ciphertext = playfair_cipher(plaintext, key)
decrypted = playfair_cipher(ciphertext, key, decrypt=True)

print(f"Ciphertext: {ciphertext}")
print(f"Decrypted text: {decrypted}")