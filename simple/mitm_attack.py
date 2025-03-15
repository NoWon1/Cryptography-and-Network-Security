def dh(p,g,x):
    return pow(g,x,p)
def m():
    g=int(input("generator (α): "))
    q=int(input("prime modulus (q): "))
    xa=int(input("Al's pvt key (XA): "))
    xb=int(input("B's pvt key (XB): "))
    xc=int(input("Attacker's pvt key (XC): "))
    ya=dh(q,g,xa)
    yb=dh(q,g,xb)
    yc=dh(q,g,xc)
    kac=dh(q,yc,xa)
    kbc=dh(q,yc,xb)
    print(f"\nPublic Keys:\nAl:{ya}\nB:{yb}\nJ:{yc}")
    print(f"\nShared Keys:\nAl-J:{kac}\nB-J:{kbc}")
if __name__=="__main__":
    m()