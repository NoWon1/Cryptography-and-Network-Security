import random,math
def p(n):
    if n<=1:return False
    if n<=3:return True
    if n%2==0 or n%3==0:return False
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:return False
        i+=6
    return True
def g(a,b):
    while b:a,b=b,a%b
    return a
def mi(a,m):
    for i in range(1,m):
        if(a*i)%m==1:return i
    return None
def e():
    c=int(input("Choose:\n1. Custom"
    "\n2.q=83, α=5, XA=2, k=4, M=4\n1-2: "))
    if c==1:
        q=int(input("q: "))
        a=int(input("α: "))
        x=int(input("XA: "))
        k=int(input("k: "))
        m=int(input("M: "))
    elif c==2:
        q,a,x,k,m=83,5,2,4,4
    else:return
    if not p(q):return
    if k<=1 or k>=q-1:return
    if g(k,q-1)!=1:return
    y=pow(a,x,q)
    c1=pow(a,k,q)
    c2=(m*pow(y,k,q))%q
    s=pow(c1,x,q)
    si=mi(s,q)
    md=(c2*si)%q
    print(f"C=({c1},{c2})")
    print(f"M={md}")
if __name__=="__main__":
    e()