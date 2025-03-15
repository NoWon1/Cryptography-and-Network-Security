def c(t, k, d=False):
    r = ""
    s = -k if d else k
    for ch in t:
        if ch.isalpha():
            a = ord('A') if ch.isupper() else ord('a')
            r += chr((ord(ch) - a + s) % 26 + a)
        else:
            r += ch
    return r
p = input("Text: ")
ks = [int(k) for k in input("keys: ").split(',')]
for k in ks:
    e = c(p, k)
    d = c(e, k, True)
    print(f"Key = {k}")
    print(f"Encrypted: {e}")
    print(f"Decrypted: {d}")