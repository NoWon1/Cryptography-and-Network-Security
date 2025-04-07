def g(a,b):
    while b:a,b=b,a%b
    return a
def m(e,p):
    def x(a,b):
        if a==0:return b,0,1
        g,x,y=x(b%a,a)
        return g,y-(b//a)*x,x
    g,x,y=x(e,p)
    if g!=1:raise Exception('No inverse')
    return x%p
def p(n):
    if n<=1:return 0
    if n<=3:return 1
    if n%2==0 or n%3==0:return 0
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:return 0
        i+=6
    return 1
def k(p,q,d=None):
    if not(p(p)and p(q)):raise ValueError('Need primes')
    n,f=p*q,(p-1)*(q-1)
    if d:
        if g(d,f)!=1:raise ValueError('Not coprime')
        e=m(d,f)
    else:
        e=65537
        while g(e,f)!=1:e+=2
        d=m(e,f)
    return(e,n),(d,n)
def s(k,h):
    d,n=k
    return pow(h,d,n)
def v(k,h,s):
    e,n=k
    return pow(s,e,n)==h
def main():
    print("RSA-DS Implementation\n")
    if input("Mode (1=gen, 2=spec): ")=='2':
        q=int(input("q: ")or"19")
        p=int(input("p: "))
        d=int(input("XA: ")or"5")
        h=int(input("H(M): ")or"17")
        input("a: ")or"2"
        input("k: ")or"7"
        try:
            n,f=p*q,(p-1)*(q-1)
            e=m(d,f)
            u,r=(e,n),(d,n)
            i=s(r,h)
            print(f"\nPublic Key: {u}\nSignature: {i}\nVerification: {
                'Valid'if v(u,h,i)else'Invalid'}")
        except Exception as e:print("Error:",e)
    else:
        try:
            p,q=int(input("p: ")),int(input("q: "))
            if input("Custom d? (y/n): ")=='y':d=int(input("d: "));u,r=k(p,q,d)
            else:u,r=k(p,q)
            h=int(input("H(M): "))
            i=s(r,h)
            print(f"\nPublic Key: {u}\nPrivate Key: {r}\nSignature: {i}\nVerification: {
                'Valid'if v(u,h,i)else'Invalid'}")
        except Exception as e:print("Error:",e)
if __name__=="__main__":main()