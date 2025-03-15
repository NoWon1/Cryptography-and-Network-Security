import math
def g(a,b):
    while b:a,b=b,a%b
    return a
def m(e,p):
    for d in range(1,p):
        if(d*e)%p==1:return d
    return None
def ip(n):
    if n<=1:return False
    if n<=3:return True
    if n%2==0 or n%3==0:return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:return False
        i+=6
    return True
def rsa():
    c=int(input("Choose:\n1.custom\n2.p=7, q=11, e=17, M=8"
    "\n3.p=3, q=11, e=7, M=5\n4. Decrypt C=20 with e=13, n=77\n1-4: "))
    if c==1:
        p=int(input("prime p: "))
        q=int(input("prime q: "))
        e=int(input("public exponent e: "))
        M=int(input("msg M: "))
    elif c==2:
        p,q,e,M=7,11,17,8
    elif c==3:
        p,q,e,M=3,11,7,5
    elif c==4:
        C,e,n=20,13,77
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                p,q=i,n//i
                if ip(p)and ip(q):break
        h=(p-1)*(q-1)
        d=m(e,h)
        M=pow(C,d,n)
        print(f"Decrypted: {M}")
        return
    else:
        return
    if not(ip(p)and ip(q)):
        return
    n=p*q
    h=(p-1)*(q-1)
    if g(e,h)!=1:
        return
    d=m(e,h)
    C=pow(M,e,n)
    M_d=pow(C,d,n)
    print(f"Encrypted: {C}")
if __name__=="__main__":
    rsa()