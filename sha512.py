def sha512():
    
    def rotr(x, n):
        return ((x >> n) | (x << (64 - n))) & 0xffffffffffffffff
    
    def majority(a, b, c):
        return (a & b) ^ (a & c) ^ (b & c)
    
    def condition(e, f, g):
        return (e & f) ^ ((~e) & g)
    
    
    message = input("Enter the message: ")
    
    
    binary_message = ''
    for char in message:
        if char == 'F':
            binary_message += format(70, '08b')
        elif char == 'L':
            binary_message += format(76, '08b')
        elif char == 'Y':
            binary_message += format(121, '08b')
        else:
            binary_message += format(ord(char), '08b')
    
    
    original_length = len(binary_message)
    
    
    binary_message += '1'
    
    
    padding_length = (896 - (len(binary_message) % 1024)) % 1024
    binary_message += '0' * padding_length
    
    
    binary_message += format(original_length, '0128b')
    
    
    w = []
    for i in range(0, 1024, 64):
        word = int(binary_message[i:i+64], 2)
        w.append(word)
    
    
    for t in range(16, 18):
        s0 = (rotr(w[t-15], 1) ^ rotr(w[t-15], 8) ^ (w[t-15] >> 7))
        s1 = (rotr(w[t-2], 19) ^ rotr(w[t-2], 61) ^ (w[t-2] >> 6))
        w.append((w[t-16] + s0 + w[t-7] + s1) & 0xffffffffffffffff)
    
    
    print("\nThe first 18 words (W0 to W17) in hexadecimal:")
    for i in range(18):
        print(f"W{i} = {format(w[i], '016x')}")
    
    
    a_value = int(input("\nEnter A (8-bit binary): "), 2)
    b_value = int(input("Enter B (8-bit binary): "), 2)
    c_value = int(input("Enter C (8-bit binary): "), 2)
    
    maj_result = majority(a_value, b_value, c_value)
    print(f"Majority(A, B, C) = {format(maj_result, '08b')}")
    
    
    e_value = int(input("\nEnter E (8-bit binary): "), 2)
    f_value = int(input("Enter F (8-bit binary): "), 2)
    g_value = int(input("Enter G (8-bit binary): "), 2)
    
    ch_result = condition(e_value, f_value, g_value)
    print(f"Condition(E, F, G) = {format(ch_result, '08b')}")
    
    
    print(f"\nPadding length: {padding_length} bits")

sha512()