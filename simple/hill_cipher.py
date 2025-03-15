import numpy as np
def hill(p, k):
    p = ''.join(c for c in p.upper() if c.isalpha())
    k = k.upper()
    km = np.zeros((2, 2), dtype=int)
    for i in range(2):
        for j in range(2):
            km[i][j] = ord(k[(i*2+j) % len(k)]) - ord('A')    
    if len(p) % 2 != 0:
        p += 'X'    
    c = ""
    for i in range(0, len(p), 2):
        pt = [ord(p[i]) - ord('A'), ord(p[i+1]) - ord('A')]
        ct = np.dot(km, pt) % 26
        c += ''.join(chr(int(x) + ord('A')) for x in ct)   
    return c
p = input("text: ")
k = input("key: ")
c = hill(p, k)
print(f"Ciphertext: {c}")