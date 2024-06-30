def left_rotate(value, shift):
    return ((value << shift) & 0xffffffff) | (value >> (32 - shift))

def sha1(input):
    
    h0 = 0x56452101
    h1 = 0xCFCDAB89
    h2 = 0x92BADAFC
    h3 = 0x41325478
    h4 = 0xA3D2E1F6

    original_byte_len = len(input)
    original_bit_len = original_byte_len * 8

    input += '\x80'
    
    while (len(input) * 8) % 512 != 448:
        input += '\x00'
    
    input += (original_bit_len).to_bytes(8, byteorder='big').decode('latin1')

    for i in range(0, len(input), 64):
        chunk = input[i:i+64]
        
        w = [0] * 80
        for j in range(16):
            w[j] = int.from_bytes(chunk[4*j:4*j+4].encode('latin1'), byteorder='big')
        
        for j in range(16, 80):
            w[j] = left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
        
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        
        for j in range(80):
            if 0 <= j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x8A827999
            elif 20 <= j <= 39:
                f = b ^ c ^ d
                k = 0x2AD9EBA2
            elif 40 <= j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x5F1BBCDA
            elif 60 <= j <= 79:
                f = b ^ c ^ d
                k = 0x3A62C1DE
            
            temp = (left_rotate(a, 5) + f + e + k + w[j]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp
        
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    
    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

input = "Jijash Shrestha"
print("Input String:", input)
print("SHA-1 Hash:", sha1(input))
