def prepare_input(plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("J", "I")
    return plaintext

def generate_table(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    for char in keyword:
        if char not in table and char in alphabet:
            table.append(char)
    for char in alphabet:
        if char not in table:
            table.append(char)
    table = [table[i:i + 5] for i in range(0, 25, 5)]
    return table

def playfair_encrypt(plaintext, table):
    ciphertext = ""
    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else "X"
        row1, col1 = [(index, row.index(char1)) for index, row in enumerate(table) if char1 in row][0]
        row2, col2 = [(index, row.index(char2)) for index, row in enumerate(table) if char2 in row][0]
        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
        else:
            ciphertext += table[row1][col2] + table[row2][col1]
        i += 2
    return ciphertext

def playfair_decrypt(ciphertext, table):
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = [(index, row.index(char1)) for index, row in enumerate(table) if char1 in row][0]
        row2, col2 = [(index, row.index(char2)) for index, row in enumerate(table) if char2 in row][0]
        if row1 == row2:
            plaintext += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            plaintext += table[row1][col2] + table[row2][col1]
        i += 2
    return plaintext

# Set the full name and keyword
full_name = "atmosphere"
keyword = "monarchy"

# Prepare the input
full_name = prepare_input(full_name)

# Generate the table
table = generate_table(keyword)

print(f'Plain - text: {full_name}')

# Encrypt the full name
encrypted_name = playfair_encrypt(full_name, table)
print("Encrypted name:", encrypted_name)

# Decrypt the encrypted name
decrypted_name = playfair_decrypt(encrypted_name, table)
print("Decrypted name:", decrypted_name)