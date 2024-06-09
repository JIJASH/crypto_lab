def prepare_text(text):
    text = text.upper().replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + 'X'
        elif text[i] == text[i + 1]:
            prepared_text += text[i] + 'X'
        else:
            prepared_text += text[i] + text[i + 1]
            i += 1
        i += 1
    return prepared_text.replace("J", "I")

def create_playfair_matrix(key):
    matrix = [['' for _ in range(5)] for _ in range(5)]
    key = key.upper().replace("J", "I")
    key_set = set()
    i, j = 0, 0
    for char in key:
        if char not in key_set:
            matrix[i][j] = char
            key_set.add(char)
            j += 1
            if j == 5:
                i += 1
                j = 0
    for x in range(65, 91):
        if chr(x) not in key_set and chr(x) != 'J':
            matrix[i][j] = chr(x)
            key_set.add(chr(x))
            j += 1
            if j == 5:
                i += 1
                j = 0
    return matrix

def find_char_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plain_text, key):
    matrix = create_playfair_matrix(key)
    prepared_text = prepare_text(plain_text)
    encrypted_text = ""
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)
        if row1 == row2:
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row1][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text

def playfair_decrypt(encrypted_text, key):
    matrix = create_playfair_matrix(key)
    decrypted_text = ""
    for i in range(0, len(encrypted_text), 2):
        char1, char2 = encrypted_text[i], encrypted_text[i + 1]
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)
        if row1 == row2:
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row1][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return decrypted_text

plain_text = "jijashshrestha"
key = "monarchy"
encrypted_text = playfair_encrypt(plain_text, key)
decrypted_text = playfair_decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Key:", key)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)