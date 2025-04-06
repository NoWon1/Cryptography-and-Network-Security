def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
    
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % phi

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keypair(p, q, d=None):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    
    n = p * q
    phi = (p - 1) * (q - 1)
    
    if d is not None:
        if gcd(d, phi) != 1:
            raise ValueError('d must be coprime to phi(n).')
        e = mod_inverse(d, phi)
    else:
        e = 65537  # Common choice for e
        while gcd(e, phi) != 1:
            e += 2
        d = mod_inverse(e, phi)
    
    return ((e, n), (d, n))

def sign(private_key, message_hash):
    d, n = private_key
    return pow(message_hash, d, n)

def verify(public_key, message_hash, signature):
    e, n = public_key
    return pow(signature, e, n) == message_hash

def main():
    print("RSA Digital Signature Algorithm Implementation\n")
    
    mode = input("Choose mode (1 for general, 2 for specific example): ")
    
    if mode == '2':
        # Specific example
        q = int(input("Enter q (default 19): ") or "19")
        p = int(input("Enter another prime p: "))
        XA = int(input("Enter private key XA (default 5): ") or "5")
        Hm = int(input("Enter message hash H(M) (default 17): ") or "17")
        
        # These parameters not directly used in RSA-DS
        _ = input("Enter a (default 2): ") or "2"
        _ = input("Enter k (default 7): ") or "7"
        
        n = p * q
        phi = (p - 1) * (q - 1)
        d = XA
        
        try:
            e = mod_inverse(d, phi)
            public_key = (e, n)
            private_key = (d, n)
            
            print("\nUser A's Public Key (e, n):", public_key)
            
            signature = sign(private_key, Hm)
            print("Digital Signature for H(M)=", Hm, "is:", signature)
            
            is_valid = verify(public_key, Hm, signature)
            print("Signature Verification:", "Valid" if is_valid else "Invalid")
        
        except Exception as e:
            print("Error:", e)
    
    else:
        # General RSA-DS implementation
        try:
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            use_custom_d = input("Specify private key? (y/n): ").lower() == 'y'
            
            if use_custom_d:
                d = int(input("Enter d: "))
                public_key, private_key = generate_keypair(p, q, d)
            else:
                public_key, private_key = generate_keypair(p, q)
                
            message_hash = int(input("Enter H(M): "))
            
            print("\nPublic Key (e, n):", public_key)
            print("Private Key (d, n):", private_key)
            
            signature = sign(private_key, message_hash)
            print("Digital Signature:", signature)
            
            is_valid = verify(public_key, message_hash, signature)
            print("Verification Result:", "Valid" if is_valid else "Invalid")
        
        except Exception as e:  
            print("Error:", e)

if __name__ == "__main__":
    main()