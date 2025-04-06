def md5_implementation():
    def md5(message):
        if isinstance(message, str):
            message = message.encode('utf-8')
        
        
        a0 = 0x67452301
        b0 = 0xEFCDAB89
        c0 = 0x98BADCFE
        d0 = 0x10325476
        
        
        s = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]
        
        
        K = [
            0xD76AA478, 0xE8C7B756, 0x242070DB, 0xC1BDCEEE,
            0xF57C0FAF, 0x4787C62A, 0xA8304613, 0xFD469501,
            0x698098D8, 0x8B44F7AF, 0xFFFF5BB1, 0x895CD7BE,
            0x6B901122, 0xFD987193, 0xA679438E, 0x49B40821,
            0xF61E2562, 0xC040B340, 0x265E5A51, 0xE9B6C7AA,
            0xD62F105D, 0x02441453, 0xD8A1E681, 0xE7D3FBC8,
            0x21E1CDE6, 0xC33707D6, 0xF4D50D87, 0x455A14ED,
            0xA9E3E905, 0xFCEFA3F8, 0x676F02D9, 0x8D2A4C8A,
            0xFFFA3942, 0x8771F681, 0x6D9D6122, 0xFDE5380C,
            0xA4BEEA44, 0x4BDECFA9, 0xF6BB4B60, 0xBEBFBC70,
            0x289B7EC6, 0xEAA127FA, 0xD4EF3085, 0x04881D05,
            0xD9D4D039, 0xE6DB99E5, 0x1FA27CF8, 0xC4AC5665,
            0xF4292244, 0x432AFF97, 0xAB9423A7, 0xFC93A039,
            0x655B59C3, 0x8F0CCC92, 0xFFEFF47D, 0x85845DD1,
            0x6FA87E4F, 0xFE2CE6E0, 0xA3014314, 0x4E0811A1,
            0xF7537E82, 0xBD3AF235, 0x2AD7D2BB, 0xEB86D391
        ]
        
        
        def F(x, y, z): return (x & y) | (~x & z)
        def G(x, y, z): return (x & z) | (y & ~z)
        def H(x, y, z): return x ^ y ^ z
        def I(x, y, z): return y ^ (x | ~z)
        
        def left_rotate(x, c):
            return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF
        
        
        original_length_bits = len(message) * 8
        message = bytearray(message)
        message.append(0x80)
        while len(message) % 64 != 56:
            message.append(0)
        message += original_length_bits.to_bytes(8, byteorder='little')
        
        
        for i in range(0, len(message), 64):
            chunk = message[i:i+64]
            
            
            M = [int.from_bytes(chunk[j:j+4], byteorder='little') for j in range(0, 64, 4)]
            
            
            A, B, C, D = a0, b0, c0, d0
            
            
            for j in range(64):
                if j < 16:
                    f = F(B, C, D)
                    g = j
                elif j < 32:
                    f = G(B, C, D)
                    g = (5 * j + 1) % 16
                elif j < 48:
                    f = H(B, C, D)
                    g = (3 * j + 5) % 16
                else:
                    f = I(B, C, D)
                    g = (7 * j) % 16
                
                temp = D
                D = C
                C = B
                B = (B + left_rotate((A + f + K[j] + M[g]) & 0xFFFFFFFF, s[j])) & 0xFFFFFFFF
                A = temp
            
            
            a0 = (a0 + A) & 0xFFFFFFFF
            b0 = (b0 + B) & 0xFFFFFFFF
            c0 = (c0 + C) & 0xFFFFFFFF
            d0 = (d0 + D) & 0xFFFFFFFF
        
        
        digest = bytearray(16)
        for i, val in enumerate([a0, b0, c0, d0]):
            digest[4*i:4*i+4] = val.to_bytes(4, byteorder='little')
        return ''.join(f'{b:02x}' for b in digest)
    
    
    plaintext = input("Enter plaintext (default 'SCOPE'): ") or "SCOPE"
    
    
    message = plaintext.encode('utf-8')
    
    
    original_length_bits = len(message) * 8
    
    
    padding_bits = 448 - (original_length_bits % 512)
    if padding_bits <= 0:
        padding_bits += 512
    
    
    length_bits = 64
    
    
    total_bits = original_length_bits + padding_bits + length_bits
    num_blocks = total_bits // 512
    
    
    padded_message = bytearray(message)
    padded_message.append(0x80)  
    padded_message.extend([0] * ((padding_bits // 8) - 1))
    padded_message.extend(original_length_bits.to_bytes(8, byteorder='little'))
    
    
    M_blocks = []
    for block_idx in range(num_blocks):
        block_start = block_idx * 64
        block = padded_message[block_start:block_start+64]
        M = [int.from_bytes(block[i:i+4], byteorder='little') for i in range(0, 64, 4)]
        M_blocks.append(['{:08x}'.format(word) for word in M])
    
    
    b_str = input("Enter buffer B in binary (default 01100010): ") or "01100010"
    c_str = input("Enter buffer C in binary (default 01100011): ") or "01100011"
    d_str = input("Enter buffer D in binary (default 01100101): ") or "01100101"
    
    
    b = int(b_str, 2)
    c = int(c_str, 2)
    d = int(d_str, 2)
    
    
    f_result = (b & c) | (~b & d)
    majority_result = (b & c) | (b & d) | (c & d)
    
    
    print(f"\nMD5 hash of '{plaintext}': {md5(plaintext)}")
    print(f"Length of padding bits: {padding_bits}")
    print(f"Length bits to be appended: {length_bits}")
    print(f"Number of blocks after padding: {num_blocks}")
    
    print("\nSixteen 32-bit message sub-blocks (M0 to M15) in hexadecimal format:")
    for block_idx, block in enumerate(M_blocks):
        for i, word in enumerate(block):
            print(f"M{i}: {word}")
    
    print(f"\nF function result on buffers B,C,D (binary): {format(f_result, '08b')}")
    print(f"Majority function result on buffers B,C,D (binary): {format(majority_result, '08b')}")

if __name__ == "__main__":
    md5_implementation()