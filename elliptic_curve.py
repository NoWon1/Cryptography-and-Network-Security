def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1: return i
    return None

def point_addition(P, Q, a, p):
    if P is None: return Q
    if Q is None: return P
    if P[0] == Q[0] and (P[1] != Q[1] or P[1] == 0): return None
    
    if P != Q:
        s = ((Q[1] - P[1]) * mod_inverse(Q[0] - P[0], p)) % p
    else:
        s = ((3 * P[0]**2 + a) * mod_inverse(2 * P[1], p)) % p
    
    x3 = (s**2 - P[0] - Q[0]) % p
    y3 = (s * (P[0] - x3) - P[1]) % p
    return (x3, y3)

def scalar_multiplication(k, P, a, p):
    result, addend = None, P
    while k > 0:
        if k & 1: result = point_addition(result, addend, a, p)
        addend = point_addition(addend, addend, a, p)
        k >>= 1
    return result

def is_on_curve(point, a, b, p):
    if point is None: return True
    x, y = point
    return (y**2 % p) == (x**3 + a*x + b) % p

def encrypt_ecc(Pm, k, G, PB, a, p):
    C1 = scalar_multiplication(k, G, a, p)
    kPB = scalar_multiplication(k, PB, a, p)
    C2 = point_addition(Pm, kPB, a, p)
    return (C1, C2)

def decrypt_ecc(C, nB, a, p):
    C1, C2 = C
    nBC1 = scalar_multiplication(nB, C1, a, p)
    inv_nBC1 = (nBC1[0], (-nBC1[1]) % p)
    return point_addition(C2, inv_nBC1, a, p)

def main():
    print("Elliptic Curve Cryptography Implementation")
    print("Choose operation:")
    print("1. Construct elliptic curve for Z/13 using E13(2,2)")
    print("2. Perform ECC encryption/decryption using E11(1,6)")
    print("3. Find 2P, 3P, 4P and test if points are on curve")
    print("4. Find n where Q = nP for curve y^2 = x^3 + 9x + 17 mod 23")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        a, b, p = 2, 2, 13
        points = [(x, y) for x in range(p) for y in range(p) if (y**2 % p) == (x**3 + a*x + b) % p]
        print(f"Points on E13(2,2): {points}")
        print(f"Number of points: {len(points)}")
    
    elif choice == 2:
        a, b, p = 1, 6, 11
        G = (2, 7)
        
        nB = int(input("Enter B's private key (default is 7): ") or "7")
        PB = scalar_multiplication(nB, G, a, p)
        print(f"B's public key PB = {PB}")
        
        mx = int(input("Enter message point x-coordinate (default is 10): ") or "10")
        my = int(input("Enter message point y-coordinate (default is 9): ") or "9")
        Pm = (mx, my)
        
        k = int(input("Enter random k for encryption (default is 3): ") or "3")
        C = encrypt_ecc(Pm, k, G, PB, a, p)
        print(f"Cipher text C = {C}")
        
        decrypted_Pm = decrypt_ecc(C, nB, a, p)
        print(f"Decrypted message = {decrypted_Pm}")
    
    elif choice == 3:
        px = int(input("Enter point P x-coordinate (default is 2): ") or "2")
        py = int(input("Enter point P y-coordinate (default is 8): ") or "8")
        a = int(input("Enter curve parameter a (default is 1): ") or "1")
        b = int(input("Enter curve parameter b (default is 6): ") or "6")
        p = int(input("Enter field size p (default is 11): ") or "11")
        
        P = (px, py)
        P2 = scalar_multiplication(2, P, a, p)
        P3 = scalar_multiplication(3, P, a, p)
        P4 = scalar_multiplication(4, P, a, p)
        
        print(f"2P = {P2}")
        print(f"3P = {P3}")
        print(f"4P = {P4}")
        
        print(f"P is on curve: {is_on_curve(P, a, b, p)}")
        print(f"2P is on curve: {is_on_curve(P2, a, b, p)}")
        print(f"3P is on curve: {is_on_curve(P3, a, b, p)}")
        print(f"4P is on curve: {is_on_curve(P4, a, b, p)}")
    
    elif choice == 4:
        a, b, p = 9, 17, 23
        
        px = int(input("Enter point P x-coordinate (default is 16): ") or "16")
        py = int(input("Enter point P y-coordinate (default is 5): ") or "5")
        qx = int(input("Enter point Q x-coordinate (default is 4): ") or "4")
        qy = int(input("Enter point Q y-coordinate (default is 5): ") or "5")
        
        P, Q = (px, py), (qx, qy)
        
        n, R = 1, P
        while R != Q and n < p:
            R = point_addition(R, P, a, p)
            n += 1
            if R is None:
                print("No solution found (reached point at infinity)")
                break
        
        if R == Q:
            print(f"The value of n is: {n}")
        else:
            print("No solution found within the range")
    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()