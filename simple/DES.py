def h2b(h):
    return bin(int(h,16))[2:].zfill(64)
def pc1(k):
    p=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    return ''.join(k[i-1]for i in p)
def pc2(k):
    p=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    return ''.join(k[i-1]for i in p)
def ls(b,s):
    return b[s:]+b[:s]
def gen_keys(k,s=1,n=3):
    k56=pc1(h2b(k))
    c,d=k56[:28],k56[28:]
    sh=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in range(s-1):
        c=ls(c,sh[i])
        d=ls(d,sh[i])
    return [pc2(ls(c,sh[i])+ls(d,sh[i]))for i in range(s-1,s-1+n)]
def main():
    print("Choose:")
    print("1.K1, K2, K3 from initial key")
    print("2.keys for rounds 9, 10, 11 from 8 key")
    o=input("1 or 2: ")
    if o=="1":
        k=input("Enter the 16c hex key: ")
        if len(k)!=16 or not all(c in'0123456789ABCDEFabcdef'for c in k):
            print("Error")
            return
        rk=gen_keys(k,1,3)
        s=1
    elif o=="2":
        k=input("Enter the 16c hex key: ")
        if len(k)!=16 or not all(c in'0123456789ABCDEFabcdef'for c in k):
            print("Error")
            return
        rk=gen_keys(k,9,3)
        s=9
    else:
        print("Invalid")
        return
    print("\nRound Keys:")
    for i,k in enumerate(rk,s):
        print(f"K{i} (hex): {hex(int(k,2))[2:].upper().zfill(12)}")
if __name__=="__main__":
    main()