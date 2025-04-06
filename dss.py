def mod_pow(base, exponent, modulus):
    """Efficient modular exponentiation"""
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def extended_gcd(a, b):
    """Extended Euclidean Algorithm"""
    if a == 0:
        return b, 0, 1
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    """Calculate modular multiplicative inverse"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def dsa_sign(p, q, g, x, h_m):
    """Generate DSA signature"""
    import random
    k = random.randint(1, q - 1)
    r = mod_pow(g, k, p) % q
    if r == 0:
        return dsa_sign(p, q, g, x, h_m)
    s = (mod_inverse(k, q) * (h_m + x * r)) % q
    if s == 0:
        return dsa_sign(p, q, g, x, h_m)
    return r, s

def dsa_verify(p, q, g, y, h_m, r, s):
    """Verify DSA signature"""
    if r <= 0 or r >= q or s <= 0 or s >= q:
        return False
    w = mod_inverse(s, q)
    u1 = (h_m * w) % q
    u2 = (r * w) % q
    v = (mod_pow(g, u1, p) * mod_pow(y, u2, p)) % p % q
    return v == r

def main():
    try:
        print("Digital Signature Standard (DSS) Implementation")
        
        # Get user inputs
        p = int(input("Enter prime modulus p: "))
        q = int(input("Enter prime divisor q: "))
        g = int(input("Enter generator g: "))
        x = int(input("Enter private key x: "))
        h_m = int(input("Enter message hash H(M): "))
        
        # Calculate public key
        y = mod_pow(g, x, p)
        print(f"\nPublic key (y): {y}")
        
        # Generate signature
        r, s = dsa_sign(p, q, g, x, h_m)
        print(f"\nSignature: (r={r}, s={s})")
        
        # Verify signature
        valid = dsa_verify(p, q, g, y, h_m, r, s)
        print(f"\nSignature verification: {'Valid' if valid else 'Invalid'}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()