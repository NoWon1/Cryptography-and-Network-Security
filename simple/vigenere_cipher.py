import string
def v(t, k, d=False):
    t, k = t.upper(), k.upper()
    s = -1 if d else 1
    r, j = '', 0
    for c in t:
        if c in string.ascii_uppercase:
            r += chr((ord(c) + s * (ord(k[j % len(k)]) - 65) - 65) % 26 + 65)
            j += 1
    return r
k = input("key: ")
m = input("message: ")
e = v(m, k)
print(f"Encrypted: {e}")
print(f"Decrypted: {v(e, k, True)}")