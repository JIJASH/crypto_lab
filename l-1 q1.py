def encrypt(key, word):
    result = ""
    for letter in word:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset + key) % 26 + ascii_offset)
        else:
            result += letter
    return result

def decrypt(key, word):
    result = ""
    for letter in word:
        if letter.isalpha():
            ascii_offset = 65 if letter.isupper() else 97
            result += chr((ord(letter) - ascii_offset - key) % 26 + ascii_offset)
        else:
            result += letter
    return result

def main():
    plaintext = "JIJASHSHRESTHA"
    key = 3

    print(f'Plain-Text: {plaintext}')
    encrypted = encrypt(key, plaintext)
    print(f"Encrypted: {encrypted}")

    
    decrypted = decrypt(key, encrypted)
    print(f"Decrypted: {decrypted}")

if __name__ == "__main__":
    main()