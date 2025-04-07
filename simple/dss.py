import random as r
def mp(b,e,m):
    t=1;b%=m
    while e:
        if e&1:t=(t*b)%m
        e>>=1;b=(b*b)%m
    return t
def eg(a,b):
    if a==0:return b,0,1
    g,x,y=eg(b%a,a)
    return g,y-(b//a)*x,x
def mi(a,m):
    g,x,_=eg(a,m)
    if g!=1:raise Exception('No inverse')
    return x%m
def sgn(p,q,g,x,h):
    k=r.randint(1,q-1)
    r1=mp(g,k,p)%q
    if r1==0:return sgn(p,q,g,x,h)
    s=(mi(k,q)*(h+x*r1))%q
    if s==0:return sgn(p,q,g,x,h)
    return r1,s
def vfy(p,q,g,y,h,r1,s):
    if not(0<r1<q and 0<s<q):return 0
    w=mi(s,q)
    u1,u2=(h*w)%q,(r1*w)%q
    v=(mp(g,u1,p)*mp(y,u2,p))%p%q
    return v==r1
if __name__=="__main__":
    try:
        print("DSS")
        p=int(input("p: "))
        q=int(input("q: "))
        g=int(input("g: "))
        x=int(input("x: "))
        h=int(input("H(M): "))
        y=mp(g,x,p)
        print(f"Public key: {y}")
        r1,s=sgn(p,q,g,x,h)
        print(f"Signature: r={r1}, s={s}")
        v=vfy(p,q,g,y,h,r1,s)
        print(f"Verification: {
            'Valid' if v else 'Invalid'}")
    except Exception as e:
        print(f"Error: {e}")