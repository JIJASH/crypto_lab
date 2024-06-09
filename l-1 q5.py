def rail_fence_encrypt(text, rails):
    encrypted_text = ""
    for i in range(rails):
        j = i
        while j < len(text):
            encrypted_text += text[j]
            if i != 0 and i != rails - 1:
                next_index = j + 2 * (rails - i) - 2
                if next_index < len(text):
                    encrypted_text += text[next_index]
            j += 2 * (rails - 1)
    return encrypted_text

def rail_fence_decrypt(text, rails):
    decrypted_text = [''] * len(text)
    index = 0
    for i in range(rails):
        j = i
        while j < len(text):
            decrypted_text[j] = text[index]
            index += 1
            if i != 0 and i != rails - 1:
                next_index = j + 2 * (rails - i) - 2
                if next_index < len(text):
                    decrypted_text[next_index] = text[index]
                    index += 1
            j += 2 * (rails - 1)
    return "".join(decrypted_text)

name = "JIJASHSHRESTHA"
rails = 3

encrypted_name = rail_fence_encrypt(name, rails)
decrypted_name = rail_fence_decrypt(encrypted_name, rails)

print("Name:", name)
print("Encrypted Name:", encrypted_name)
print("Decrypted Name:", decrypted_name)