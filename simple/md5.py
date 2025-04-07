def m():
    def md5(m):
        if isinstance(m,str):m=m.encode('utf-8')
        a,b,c,d=0x67452301,0xEFCDAB89,0x98BADCFE,0x10325476
        s=[7,12,17,22]*4+[5,9,14,20]*4+[4,11,16,23]*4+[6,10,15,21]*4
        K=[0xD76AA478,0xE8C7B756,0x242070DB,0xC1BDCEEE,0xF57C0FAF,0x4787C62A,0xA8304613,0xFD469501,
           0x698098D8,0x8B44F7AF,0xFFFF5BB1,0x895CD7BE,0x6B901122,0xFD987193,0xA679438E,0x49B40821,
           0xF61E2562,0xC040B340,0x265E5A51,0xE9B6C7AA,0xD62F105D,0x02441453,0xD8A1E681,0xE7D3FBC8,
           0x21E1CDE6,0xC33707D6,0xF4D50D87,0x455A14ED,0xA9E3E905,0xFCEFA3F8,0x676F02D9,0x8D2A4C8A,
           0xFFFA3942,0x8771F681,0x6D9D6122,0xFDE5380C,0xA4BEEA44,0x4BDECFA9,0xF6BB4B60,0xBEBFBC70,
           0x289B7EC6,0xEAA127FA,0xD4EF3085,0x04881D05,0xD9D4D039,0xE6DB99E5,0x1FA27CF8,0xC4AC5665,
           0xF4292244,0x432AFF97,0xAB9423A7,0xFC93A039,0x655B59C3,0x8F0CCC92,0xFFEFF47D,0x85845DD1,
           0x6FA87E4F,0xFE2CE6E0,0xA3014314,0x4E0811A1,0xF7537E82,0xBD3AF235,0x2AD7D2BB,0xEB86D391]
        F=lambda x,y,z:(x&y)|(~x&z);G=lambda x,y,z:(x&z)|(y&~z);H=lambda x,y,z:x^y^z;I=lambda x,y,z:y^(x|~z)
        r=lambda x,c:((x<<c)|(x>>(32-c)))&0xFFFFFFFF
        l=len(m)*8;m=bytearray(m);m.append(0x80)
        while len(m)%64!=56:m.append(0)
        m+=l.to_bytes(8,byteorder='little')
        for i in range(0,len(m),64):
            M=[int.from_bytes(m[i+j:i+j+4],byteorder='little')for j in range(0,64,4)]
            A,B,C,D=a,b,c,d
            for j in range(64):
                if j<16:f,g=F(B,C,D),j
                elif j<32:f,g=G(B,C,D),(5*j+1)%16
                elif j<48:f,g=H(B,C,D),(3*j+5)%16
                else:f,g=I(B,C,D),(7*j)%16
                t=D;D=C;C=B;B=(B+r((A+f+K[j]+M[g])&0xFFFFFFFF,s[j]))&0xFFFFFFFF;A=t
            a,b,c,d=(a+A)&0xFFFFFFFF,(b+B)&0xFFFFFFFF,(c+C)&0xFFFFFFFF,(d+D)&0xFFFFFFFF
        digest=bytearray(16)
        for i,v in enumerate([a,b,c,d]):digest[4*i:4*i+4]=v.to_bytes(4,byteorder='little')
        return''.join(f'{b:02x}'for b in digest)
    
    p=input("PT: ")or"SCOPE"
    m=p.encode('utf-8');l=len(m)*8
    pb=448-(l%512)
    if pb<=0:pb+=512
    lb=64;tb=l+pb+lb;nb=tb//512
    pm=bytearray(m);pm.append(0x80);pm.extend([0]*((pb//8)-1));
    pm.extend(l.to_bytes(8,byteorder='little'))
    M=[]
    for i in range(nb):
        b=pm[i*64:i*64+64]
        M.append(['{:08x}'.format(int.from_bytes(b[j:j+4],byteorder='little'))
                  for j in range(0,64,4)])
    B=int(input("B: ")or"01100010",2)
    C=int(input("C: ")or"01100011",2)
    D=int(input("D: ")or"01100101",2)
    fr=(B&C)|(~B&D)
    mr=(B&C)|(B&D)|(C&D) 
    print(f"\nMD5 hash of '{p}': {md5(p)}")
    print(f"Length padding: {pb}")
    print(f"Length bits appended: {lb}")
    print(f"Number of blocks after padding: {nb}") 
    print("\nSixteen 32-bit message sub-blocks (M0 to M15) in hex:")
    for blk in M:
        for i,w in enumerate(blk):print(f"M{i}: {w}")
    print(f"\nF function result on buffers B,C,D: {format(fr,'08b')}")
    print(f"Majority function result on buffers B,C,D: {format(mr,'08b')}")
if __name__=="__main__":m()