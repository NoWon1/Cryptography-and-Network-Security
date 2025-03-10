def diffie_hellman_key_exchange(p, g, private_key):
    return pow(g, private_key, p)

def calculate_shared_key(p, received_public_key, private_key):
    return pow(received_public_key, private_key, p)

def demonstrate_mitm_attack(p, g, xa, xb, xda, xdb):
    ya = diffie_hellman_key_exchange(p, g, xa)
    yb = diffie_hellman_key_exchange(p, g, xb)
    yda = diffie_hellman_key_exchange(p, g, xda)
    ydb = diffie_hellman_key_exchange(p, g, xdb)
    k_ab = calculate_shared_key(p, yb, xa)
    k_ad = calculate_shared_key(p, yda, xa)
    k_bd = calculate_shared_key(p, ydb, xb)
    
    return {
        "public_keys": {"Alice": ya, "Bob": yb, "Darth_for_Alice": yda, "Darth_for_Bob": ydb},
        "shared_keys": {"Alice_Bob": k_ab, "Alice_Darth": k_ad, "Bob_Darth": k_bd}
    }

def main():
    print("Diffie-Hellman Key Exchange Implementation")
    print("\nSelect a problem to solve:")
    print("1. Basic Diffie-Hellman Key Exchange")
    print("2. Problem with α=5, q=11, XA=2, XB=3")
    print("3. Man-in-the-middle attack simulation (p=17, g=7)")
    print("4. Diffie-Hellman with p=227, g=14")
    
    choice = int(input("\nEnter your choice (1-4): "))
    
    if choice == 1:
        p = int(input("Enter a prime number (p): "))
        g = int(input("Enter a primitive root (g): "))
        private_key = int(input("Enter your private key: "))
        
        public_key = diffie_hellman_key_exchange(p, g, private_key)
        print(f"Your public key is: {public_key}")
        
        received_public_key = int(input("Enter the received public key: "))
        shared_key = calculate_shared_key(p, received_public_key, private_key)
        print(f"The shared secret key is: {shared_key}")
        
    elif choice == 2:
        alpha, q, xa, xb = 5, 11, 2, 3
        ya = diffie_hellman_key_exchange(q, alpha, xa)
        yb = diffie_hellman_key_exchange(q, alpha, xb)
        k = calculate_shared_key(q, yb, xa)
        k_check = calculate_shared_key(q, ya, xb)
        
        print(f"YA = {ya}")
        print(f"YB = {yb}")
        print(f"K = {k}")
        print(f"Verification: K calculated by Bob = {k_check}")
        
    elif choice == 3:
        p, g, xa, xb, xda, xdb = 17, 7, 5, 4, 4, 8
        results = demonstrate_mitm_attack(p, g, xa, xb, xda, xdb)
        
        print("\nPublic Keys:")
        for name, key in results["public_keys"].items():
            print(f"{name}: {key}")
            
        print("\nShared Keys:")
        for name, key in results["shared_keys"].items():
            print(f"{name}: {key}")
            
        print("\nMITM Attack Analysis:")
        print("1. Darth intercepts Alice's public key and sends his own public key to Bob")
        print("2. Darth intercepts Bob's public key and sends his own public key to Alice")
        print("3. Alice establishes key with Darth (thinking it's Bob)")
        print("4. Bob establishes key with Darth (thinking it's Alice)")
        print("5. Darth can now decrypt, read, and re-encrypt all messages")
        
    elif choice == 4:
        p, g, xa, xb = 227, 14, 227, 170
        ya = diffie_hellman_key_exchange(p, g, xa)
        yb = diffie_hellman_key_exchange(p, g, xb)
        k = calculate_shared_key(p, yb, xa)
        
        print(f"a) Alice's public key Ya = {ya}")
        print(f"b) Bob's public key Yb = {yb}")
        print(f"c) Shared secret key K = {k}")
        print("\nd) Man-in-the-middle attack:")
        print("   1. Attacker intercepts Alice's and Bob's public keys")
        print("   2. Attacker generates own private keys XDA and XDB")
        print("   3. Attacker calculates public keys YDA and YDB")
        print("   4. Attacker sends YDA to Bob and YDB to Alice")
        print("   5. Alice calculates shared key with attacker (thinking it's Bob)")
        print("   6. Bob calculates shared key with attacker (thinking it's Alice)")
        print("   7. Attacker can now decrypt, read, and re-encrypt all messages")
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()