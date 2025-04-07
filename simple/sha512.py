def s():
    r=lambda x,n:((x>>n)|(x<<(64-n)))&0xffffffffffffffff
    m=lambda a,b,c:(a&b)^(a&c)^(b&c)
    c=lambda e,f,g:(e&f)^((~e)&g)
    i=input("the message: ")
    b=''.join(format({'F':70,'L':76,'Y':121}.get(h,ord(h)),
                     '08b')for h in i)
    l=len(b)
    b+='1'
    p=(896-(len(b)%1024))%1024
    b+='0'*p+format(l,'0128b')
    w=[int(b[j:j+64],2)for j in range(0,1024,64)]
    for t in range(16,18):
        s0=r(w[t-15],1)^r(w[t-15],8)^(w[t-15]>>7)
        s1=r(w[t-2],19)^r(w[t-2],61)^(w[t-2]>>6)
        w+=[(w[t-16]+s0+w[t-7]+s1)&0xffffffffffffffff]
    print("\nThe first 18 words (W0 to W17) in hex:")
    for j in range(18):print(f"W{j} = {format(w[j],'016x')}")
    a=int(input("\nA: "),2)
    b=int(input("B: "),2)
    d=int(input("C: "),2)
    print(f"Majority(A, B, C) = {format(m(a,b,d),'08b')}")
    e=int(input("\nE: "),2)
    f=int(input("F: "),2)
    g=int(input("G: "),2)
    print(f"Condition(E, F, G) = {format(c(e,f,g),'08b')}")
    print(f"\nPadding length: {p} bits")
s()