def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(64)

def apply_pc1(key_64bit):
    pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
           10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
           63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
           14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
    return ''.join(key_64bit[i-1] for i in pc1)

def apply_pc2(combined_key):
    pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
           23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
           41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
           44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    return ''.join(combined_key[i-1] for i in pc2)

def left_shift(bits, shift_count):
    return bits[shift_count:] + bits[:shift_count]

def generate_des_keys(key_hex, start_round=1, num_rounds=3):
    key_56bit = apply_pc1(hex_to_bin(key_hex))
    c, d = key_56bit[:28], key_56bit[28:]
    shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    for i in range(start_round - 1):
        c = left_shift(c, shift_schedule[i])
        d = left_shift(d, shift_schedule[i])
    
    return [apply_pc2(left_shift(c, shift_schedule[i]) + left_shift(d, shift_schedule[i])) 
            for i in range(start_round - 1, start_round - 1 + num_rounds)]

def main():
    print("Choose an option:")
    print("1. Generate keys K1, K2, K3 from initial key")
    print("2. Generate keys for rounds 9, 10, 11 from round 8 key")
    
    option = input("Enter option (1 or 2): ")
    
    if option == "1":
        key_hex = input("Enter the 16-character hexadecimal key (e.g., 231457799BBCDFF1): ")
        if len(key_hex) != 16 or not all(c in '0123456789ABCDEFabcdef' for c in key_hex):
            print("Error: Key must be exactly 16 hexadecimal characters")
            return
        
        round_keys = generate_des_keys(key_hex, 1, 3)
        start_round = 1
        
    elif option == "2":
        key_hex = input("Enter the 16-character hexadecimal key for round 8 (e.g., A21036331ECB5873): ")
        if len(key_hex) != 16 or not all(c in '0123456789ABCDEFabcdef' for c in key_hex):
            print("Error: Key must be exactly 16 hexadecimal characters")
            return
        
        round_keys = generate_des_keys(key_hex, 9, 3)
        start_round = 9
        
    else:
        print("Invalid option")
        return
    
    print("\nRound Keys:")
    for i, key in enumerate(round_keys, start_round):
        print(f"K{i}: {key}")
        print(f"K{i} (hex): {hex(int(key, 2))[2:].upper().zfill(12)}")

if __name__ == "__main__":
    main()