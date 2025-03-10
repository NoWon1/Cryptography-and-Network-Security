def diffie_hellman(p, g, x):
    return pow(g, x, p)

def mitm_attack():
    g=int(input("Enter generator (α): "))
    q=int(input("Enter prime modulus (q): "))
    xa=int(input("Alice's private key (XA): "))
    xb=int(input("Bob's private key (XB): "))
    xc=int(input("Attacker's private key (XC): "))

    ya=diffie_hellman(q,g,xa)
    yb=diffie_hellman(q,g,xb)
    yc=diffie_hellman(q,g,xc)

    kac=diffie_hellman(q,yc,xa)
    kbc=diffie_hellman(q,yc,xb)

    print(f"\nPublic Keys:\nAlice (YA): {ya}\nBob (YB): {yb}\nJohn (YC): {yc}")
    print(f"\nShared Keys:\nAlice-John: {kac}\nBob-John: {kbc}")

    print("\nMITM Attack Process:")
    print("1.Alice sends YA; John intercepts.")
    print("2.John sends YC to Bob.")
    print("3.Bob sends YB; John intercepts.")
    print("4.John sends YC to Alice.")
    print("5.Alice computes shared key with John.")
    print("6.Bob computes shared key with John.")
    print("7.John decrypts and re-encrypts messages.")

if __name__=="__main__":
    mitm_attack()