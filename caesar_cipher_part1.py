

#code to encode our msg



alphabet=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
"s", "t", "u", "v", "w", "x","y" "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x","y", "z"]

directions=input("Type 'encode' to encrypt and 'decode' to decrypt \n")
text = input("Enter your message\n").lower()
shift=int(input("Type shift number\n"))


def encrypt(my_text,my_shift):
    cipher_text=" "
    for letter in my_text:
        alphabet.index(letter)
        position=alphabet.index(letter)
        new_position=position + my_shift
        new_letter=alphabet[new_position]
        cipher_text +=new_letter
    print(f"The encoded text is: {cipher_text}")
encrypt(my_text=text,my_shift=shift)