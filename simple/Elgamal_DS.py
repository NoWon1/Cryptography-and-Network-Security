def gcd(a,b):
    while b:a,b=b,a%b
    return a
def mi(a,m):
    g,x,y=egcd(a,m)
    if g!=1:raise Exception('No inverse')
    return x%m
def egcd(a,b):
    if a==0:return(b,0,1)
    g,x,y=egcd(b%a,a)
    return(g,y-(b//a)*x,x)
def isprime(n):
    if n<=1:return 0
    if n<=3:return 1
    if n%2==0 or n%3==0:return 0
    i=5
    while i*i<=n:
        if n%i==0 or n%(i+2)==0:return 0
        i+=6
    return 1
def elgamal():
    print("Scheme")
    try:
        p=int(input("p: "))
        a=int(input("α: "))
        x=int(input("x: "))
        if not isprime(p):raise ValueError("p must be prime")
        if a<=1 or a>=p:raise ValueError("α must be 1<α<p")
        if x<=0 or x>=p-1:raise ValueError("x must be 1≤x≤p-2")   
        b=pow(a,x,p)
        print(f"Public Key: ({p}, {a}, {b})")        
        m=int(input("\nMessage hash: "))
        k=int(input(f"k (1≤k≤{p-2}, gcd(k,{p-1})=1): "))       
        if k<=0 or k>=p-1:raise ValueError("k must be 1≤k≤p-2")
        if gcd(k,p-1)!=1:raise ValueError("k must be coprime to p-1")       
        print("\nSignature Generation:")
        r=pow(a,k,p)
        print(f"r = {a}^{k} mod {p} = {r}")       
        ki=mi(k,p-1)
        print(f"k^(-1) mod {p-1} = {ki}")       
        s=(ki*(m-x*r))%(p-1)
        print(f"s = {ki}*({m}-{x}*{r}) mod {p-1} = {s}")
        print(f"Signature: ({r}, {s})")        
        print("\nVerification:")
        if r<=0 or r>=p:
            print(f"Failed: r={r} not in [1,{p-1}]")
            return        
        v1=(pow(b,r,p)*pow(r,s,p))%p
        print(f"v1 = ({b}^{r})*({r}^{s}) mod {p} = {v1}")        
        v2=pow(a,m,p)
        print(f"v2 = {a}^{m} mod {p} = {v2}")       
        print(f"Result: {'valid' if v1==v2 else 'invalid'}")
    except Exception as e:print(f"Error: {e}")
if __name__=="__main__":elgamal()