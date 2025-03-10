import random
import math

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

def gcd(a, b):
    while b: a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1: return i
    return None

def elgamal():
    choice = int(input("Choose operation:\n1. ElGamal with custom values\n2. ElGamal with q=83, α=5, XA=2, k=4, M=4\nEnter choice (1-2): "))
    
    if choice == 1:
        q = int(input("Enter prime number q: "))
        alpha = int(input("Enter primitive root α: "))
        xa = int(input("Enter private key XA: "))
        k = int(input("Enter random integer k (1 < k < q-1): "))
        m = int(input("Enter message M: "))
    elif choice == 2:
        q, alpha, xa, k, m = 83, 5, 2, 4, 4
        print(f"Using q={q}, α={alpha}, XA={xa}, k={k}, M={m}")
    else:
        print("Invalid choice")
        return
    
    if not is_prime(q):
        print(f"{q} is not a prime number")
        return
    
    if k <= 1 or k >= q-1:
        print(f"k must be between 1 and q-1")
        return
    
    if gcd(k, q-1) != 1:
        print(f"k={k} must be coprime with q-1={q-1}")
        return
    
    ya = pow(alpha, xa, q)
    c1 = pow(alpha, k, q)
    c2 = (m * pow(ya, k, q)) % q
    s = pow(c1, xa, q)
    s_inv = mod_inverse(s, q)
    m_decrypted = (c2 * s_inv) % q
    
    print(f"\nElGamal Parameters:\nPrime q = {q}\nPrimitive root α = {alpha}\nPrivate key XA = {xa}")
    print(f"Public key YA = α^XA mod q = {alpha}^{xa} mod {q} = {ya}\nRandom k = {k}")
    
    print(f"\nEncryption:\nOriginal message M = {m}\nc1 = α^k mod q = {alpha}^{k} mod {q} = {c1}")
    print(f"c2 = M * YA^k mod q = {m} * {ya}^{k} mod {q} = {c2}\nCiphertext = (c1, c2) = ({c1}, {c2})")
    
    print(f"\nDecryption:\ns = c1^XA mod q = {c1}^{xa} mod {q} = {s}\ns^(-1) mod q = {s_inv}")
    print(f"M = c2 * s^(-1) mod q = {c2} * {s_inv} mod {q} = {m_decrypted}")
    
    print("\nDecryption successful: Original message recovered correctly!" if m == m_decrypted else "\nDecryption failed: Original message not recovered.")

if __name__ == "__main__":
    elgamal()