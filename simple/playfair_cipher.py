def create_sq(k):
    k = ''.join(dict.fromkeys(k.upper().replace('J', 'I')))
    a = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    s = ''.join(dict.fromkeys(k + a))
    return [s[i:i+5] for i in range(0, 25, 5)]
def find_pos(s, c):
    for i, r in enumerate(s):
        if c in r:
            return i, r.index(c)
def pf(m, k, d=False):
    s = create_sq(k)
    m = ''.join(c for c in m.upper().replace('J', 'I') if c.isalpha())  
    if not d:
        i = 0
        while i < len(m) - 1:
            if m[i] == m[i+1]:
                m = m[:i+1] + 'X' + m[i+1:]
            i += 1
        if len(m) % 2 != 0:
            m += 'X'   
    r = ""
    for i in range(0, len(m), 2):
        if i+1 < len(m):
            a, b = m[i], m[i+1]
            r1, c1 = find_pos(s, a)
            r2, c2 = find_pos(s, b)
            
            if r1 == r2:
                r += s[r1][(c1 + (1 if not d else -1)) % 5]
                r += s[r2][(c2 + (1 if not d else -1)) % 5]
            elif c1 == c2:
                r += s[(r1 + (1 if not d else -1)) % 5][c1]
                r += s[(r2 + (1 if not d else -1)) % 5][c2]
            else:
                r += s[r1][c2]
                r += s[r2][c1]  
    return r
p = input("Enter plaintext: ")
k = input("Enter key: ")
c = pf(p, k)
print(f"Ciphertext: {c}")
print(f"Decrypted: {pf(c, k, d=True)}")