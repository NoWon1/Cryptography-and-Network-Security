def dh(p,g,pk):
    return pow(g,pk,p)
def cs(p,rpk,pk):
    return pow(rpk,pk,p)
def mitm(p,g,xa,xb,xda,xdb):
    ya=dh(p,g,xa)
    yb=dh(p,g,xb)
    yda=dh(p,g,xda)
    ydb=dh(p,g,xdb)
    k_ab=cs(p,yb,xa)
    k_ad=cs(p,yda,xa)
    k_bd=cs(p,ydb,xb)
    return {
        "pblc_keys":{"Al":ya,"B":yb,"Darth_Al":yda,"Darth_B":ydb},
        "shared_keys":{"Al_B":k_ab,"Al_Darth":k_ad,"B_Darth":k_bd}
    }
def main():
    print("1.DH")
    print("2.α=5, q=11, XA=2, XB=3")
    print("3.MiTM(p=17, g=7)")
    print("4.DH p=227, g=14")
    c=int(input("\n1-4: "))  
    if c==1:
        p=int(input("prime (p): "))
        g=int(input("primitive root (g): "))
        pk=int(input("your pvt key: ")) 
        pbk=dh(p,g,pk)
        print(f"Your pblc key: {pbk}")
        rpk=int(input("received pblc key: "))
        sk=cs(p,rpk,pk)
        print(f"shared secret key is: {sk}")
    elif c==2:
        a,q,xa,xb=5,11,2,3
        ya=dh(q,a,xa)
        yb=dh(q,a,xb)
        k=cs(q,yb,xa)
        k_c=cs(q,ya,xb)
        print(f"YA={ya}")
        print(f"YB={yb}")
        print(f"K={k}")
    elif c==3:
        p,g,xa,xb,xda,xdb=17,7,5,4,4,8
        r=mitm(p,g,xa,xb,xda,xdb)
        print("\npblc Keys:")
        for n,k in r["pblc_keys"].items():
            print(f"{n}:{k}")   
        print("\nShared Keys:")
        for n,k in r["shared_keys"].items():
            print(f"{n}:{k}")
    elif c==4:
        p,g,xa,xb=227,14,227,170
        ya=dh(p,g,xa)
        yb=dh(p,g,xb)
        k=cs(p,yb,xa)       
        print(f"Ya={ya}")
        print(f"Yb={yb}")
        print(f"K={k}")  
    else:
        print("Invalid")
if __name__=="__main__":
    main()