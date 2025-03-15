import random,math
def mi(a,m):
    for i in range(1,m):
        if(a*i)%m==1:return i
    return None
def pa(P,Q,a,p):
    if P is None:return Q
    if Q is None:return P
    if P[0]==Q[0]and(P[1]!=Q[1]or P[1]==0):return None
    if P!=Q:s=((Q[1]-P[1])*mi(Q[0]-P[0],p))%p
    else:s=((3*P[0]**2+a)*mi(2*P[1],p))%p
    x3=(s**2-P[0]-Q[0])%p
    y3=(s*(P[0]-x3)-P[1])%p
    return(x3,y3)
def sm(k,P,a,p):
    r,a2=None,P
    while k>0:
        if k&1:r=pa(r,a2,a,p)
        a2=pa(a2,a2,a,p)
        k>>=1
    return r
def oc(pt,a,b,p):
    if pt is None:return True
    x,y=pt
    return(y**2%p)==(x**3+a*x+b)%p
def enc(Pm,k,G,PB,a,p):
    C1=sm(k,G,a,p)
    kPB=sm(k,PB,a,p)
    C2=pa(Pm,kPB,a,p)
    return(C1,C2)
def dec(C,nB,a,p):
    C1,C2=C
    nBC1=sm(nB,C1,a,p)
    inv_nBC1=(nBC1[0],(-nBC1[1])%p)
    return pa(C2,inv_nBC1,a,p)
def main():
    c=int(input("1-4: "))
    if c==1:
        a,b,p=2,2,13
        pts=[(x,y)for x in range(p)for y in 
             range(p)if(y**2%p)==(x**3+a*x+b)%p]
        print(f"Points: {pts}")
    elif c==2:
        a,b,p=1,6,11;G=(2,7)
        nB=int(input("B's pvt key: ")or"7")
        PB=sm(nB,G,a,p)
        mx=int(input("msg x: ")or"10")
        my=int(input("msg y: ")or"9")
        Pm=(mx,my)
        k=int(input("random k: ")or"3")
        C=enc(Pm,k,G,PB,a,p)
        print(f"C={C}")
        dPm=dec(C,nB,a,p)
        print(f"M={dPm}")
    elif c==3:
        px=int(input("Px: ")or"2")
        py=int(input("Py: ")or"8")
        a=int(input("a: ")or"1")
        b=int(input("b: ")or"6")
        p=int(input("p: ")or"11")
        P=(px,py)
        P2,P3,P4=sm(2,P,a,p),sm(3,P,a,p),sm(4,P,a,p)
        print(f"2P={P2},3P={P3},4P={P4}")
    elif c==4:
        a,b,p=9,17,23
        px=int(input("Px: ")or"16")
        py=int(input("Py: ")or"5")
        qx=int(input("Qx: ")or"4")
        qy=int(input("Qy: ")or"5")
        P,Q=(px,py),(qx,qy);n,R=1,P
        while R!=Q and n<p:
            R=pa(R,P,a,p);n+=1
            if R is None:break
        if R==Q:print(f"n={n}")
if __name__=="__main__":
    main()