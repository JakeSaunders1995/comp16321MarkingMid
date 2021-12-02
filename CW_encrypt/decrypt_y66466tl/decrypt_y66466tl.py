import sys
import os

args = sys.argv

def Hex(cipher_text):
    return bytearray.fromhex(cipher_text).decode()

def Caesar(cipher_text):
    plain_text = ""
    for char in cipher_text:
        if (char != ' '):
            ascii_val = ord(char)
            if (ascii_val-3 < 97):
                plain_text += chr(ascii_val+23)
            else:
                plain_text += chr(ascii_val-3)
        else:
            plain_text += char
    return plain_text

def Morse(cipher_text):
    plain_text = ""
    morse = cipher_text.split(" ")
    morse_alphabet =    [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",
                        ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",
                        ".--","-..-","-.--","--..","-----",".----","..---","...--","....-",
                        ".....","-....","--...","---..","----."]

    for char in morse:
        if (char == "/"):
            plain_text += " "
        else:
            for i in range(len(morse_alphabet)):
                if(char == morse_alphabet[i]):
                    if (i<=25):
                        plain_text += chr(i+97)
                    else:
                        plain_text += str(i-26)
                    break

    return plain_text

def decrypt(cipher_type, cipher_text):

    plain_text = ""
    if(cipher_type == "Hex"):
        plain_text = Hex(cipher_text)
    elif(cipher_type == "Caesar Cipher(+3)"):
        plain_text = Caesar(cipher_text)
    elif(cipher_type == "Morse Code"):
        plain_text = Morse(cipher_text)
    else:
        print("ERROR : Invalid encyption method")

    return plain_text

input_dir = args[1]
output_dir = args[2]

for file_name in os.listdir(input_dir):
    input_file = open(os.path.join(input_dir, file_name), "r")
    output_file = open(os.path.join(output_dir,(file_name + "_y66466tl")), "w")
    raw = input_file.read().split(':')
    cipher_type = raw[0]
    cipher_text = raw[1]
    result = decrypt(cipher_type, cipher_text)
    output_file.write(result)
