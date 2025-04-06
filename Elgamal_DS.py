def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def elgamal_ds():
    print("ElGamal Digital Signature Scheme")
    
    try:
        # Key Generation
        p = int(input("Enter a prime number p: "))
        alpha = int(input("Enter a generator α (1 < α < p): "))
        x = int(input("Enter a private key x (1 ≤ x ≤ p-2): "))
        
        if not is_prime(p):
            raise ValueError("p must be a prime number")
        if alpha <= 1 or alpha >= p:
            raise ValueError("alpha must be between 1 and p-1")
        if x <= 0 or x >= p-1:
            raise ValueError("x must be between 1 and p-2")
        
        beta = pow(alpha, x, p)
        print(f"Public Key (p, α, β): ({p}, {alpha}, {beta})")
        
        # Signature Generation
        m = int(input("\nEnter the message hash h(M): "))
        k = int(input(f"Enter a random number k (1 ≤ k ≤ {p-2}, gcd(k, {p-1}) = 1): "))
        
        if k <= 0 or k >= p-1:
            raise ValueError("k must be between 1 and p-2")
        if gcd(k, p-1) != 1:
            raise ValueError("k must be relatively prime to p-1")
        
        print("\nSignature Generation:")
        r = pow(alpha, k, p)
        print(f"r = α^k mod p = {alpha}^{k} mod {p} = {r}")
        
        k_inv = mod_inverse(k, p-1)
        print(f"k^(-1) mod (p-1) = {k}^(-1) mod {p-1} = {k_inv}")
        
        s = (k_inv * (m - x * r)) % (p-1)
        print(f"s = k^(-1)(m - xr) mod (p-1) = {k_inv}*({m} - {x}*{r}) mod {p-1} = {s}")
        print(f"Signature: (r, s) = ({r}, {s})")
        
        # Signature Verification
        print("\nSignature Verification:")
        if r <= 0 or r >= p:
            print(f"Verification failed: r = {r} is not in range [1, {p-1}]")
            return
        
        beta_r = pow(beta, r, p)
        r_s = pow(r, s, p)
        v1 = (beta_r * r_s) % p
        print(f"v1 = (β^r)*(r^s) mod p = ({beta}^{r})*({r}^{s}) mod {p} = {v1}")
        
        v2 = pow(alpha, m, p)
        print(f"v2 = α^m mod p = {alpha}^{m} mod {p} = {v2}")
        
        result = "valid" if v1 == v2 else "invalid"
        print(f"Verification result: Signature is {result}!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    elgamal_ds()