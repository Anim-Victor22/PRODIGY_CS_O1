source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
          'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_source = len(source)

'''def encryption(plain_text, shift_key):
    cipher_text = ' '
    for char in plain_text():
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    return cipher_text





def decryption(cipher_text, shift_key):
    plain_text = ' '
    for char in cipher_text():
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            cipher_text += char
    return plain_text'''


def encryption_decryption(user_text, shift_key, mode):
    result = ' '                                                            # creates an empty string for the end result
    if mode == "d":
        shift_key = -shift_key
        for char in user_text():
            if char in source:
                position = source.index(char)                                # finds the pos of each character
                new_position = (position + shift_key) % num_source    # finds the new pos of char after en(de)cryption.
                                                                    # The % is available to handle -ve indexes

                result += source[new_position]
            else:
                result += char
    elif mode == "e":
        for char in user_text():
            if char in source:
                position = source.index(char)
                new_position = (position + shift_key) % num_source
                result += source[new_position]
            else:
                result += char
    return result


end = False
while not end:
    user_input = input("Type e for encryption or d for decryption: \n")
    text = input("Type in your text: \n").lower
    key = int(input("Type the shift key: \n"))
    if user_input == 'e':
        ciphertext = encryption_decryption(user_text=text, shift_key=key, mode=user_input)
        print(f"ciphertext is: {ciphertext}")

    elif user_input == 'd':
        plaintext = encryption_decryption(user_text=text, shift_key=key, mode=user_input)
        print(f"plaintext is: {plaintext}")
    play_again = input("Type 'yes' to continue, type 'no' to exit. \n").lower()
    if play_again == 'no':
        end = True
        print("Have a nice day! Bye..")
