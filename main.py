# Convert any text to Morse Code
import sys

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encryption():
    """
    This function will encrypt the inputted text
    :return:
    """
    encrypted_slice_word = [MORSE_CODE_DICT[letter] if letter != " " else "/" for letter in word ]
    return  f"Encrypted Word: {" ".join(encrypted_slice_word)}"

def decryption():
    """
    This function is will decrypt the morse code
    :return: decrypted_word
    """
    decrypted_word = ""
    decrypted_slice_word = word.split(" ")
    for char in decrypted_slice_word:
        if char == "/":
            decrypted_word = decrypted_word + " "
        for key, value in MORSE_CODE_DICT.items():
            if value == char:
                decrypted_word = decrypted_word + key
                break
    return f"Decrypted Word: {decrypted_word}"


print(MORSE_CODE_DICT.values())
action = input("What action do you want to take? Options are 1: Encrypt 2: Decrypt.").title()
print(action)

if action != "Encrypt" and action != "Decrypt":
    print("You have inputted the wrong options. Try again")
    sys.exit(1)

word = input(f"Please enter the word/sentence you want to {action}: ").upper()

print(f"This is sentence or word that needs to {action}ed: {word}")

if action == "Encrypt":
    print(encryption())
else:
    print(decryption())
