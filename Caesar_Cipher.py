alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function for encryption
def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26 
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's is the text after encryption: {cipher_text}")

# function for decryption
def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26 
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Here's is the text after decryption: {plain_text}")


# Main Function
want_to_end = False 
while not want_to_end:
    operation = input("Type 'encrypt' for encription, type 'decrypt' for decryption:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Enter shift key:\n"))

    if operation == "encrypt":
        encryption(plain_text=text, shift_key=shift)
    elif operation == "decrypt":
        decryption(cipher_text=text, shift_key=shift)
    want_to_continue = input("Do you want to Continue?...\nType 'yes' to continue, type 'no' to exit.\n")
    if want_to_continue == "no":
        want_to_end = True
        print("Thank You!")
