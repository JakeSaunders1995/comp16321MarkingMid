import string
import sys,os
input_path = sys.argv[1]
output_path = sys.argv[2]


for file in os.listdir(input_path):
    with open(os.path.join(input_path,file), "r") as f:
        cipherTextFile = f.read()
    algorithm, cipherText = tuple(cipherTextFile.split(":"))
    plaintext = ""

    if algorithm.lower() == "hex":
        decimal_values = []
        for char in cipherText.split(" "):
            decimal_values.append(int(char, base=16))
        for dec in decimal_values:
            plaintext += chr(dec)



    elif algorithm.lower() == "caesar cipher(+3)":
        list_alphabet = list(string.ascii_letters)
        for char in cipherText:
            if char in list_alphabet:
                cipher_index = list_alphabet.index(char)
                plaintext_char = list_alphabet[(cipher_index-3)%26]
                plaintext += plaintext_char
            else:
                plaintext += char


    elif algorithm.lower() == "morse code":
        letterToMorse = { 'A':'.-', 'B':'-...',
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
                        '(':'-.--.', ')':'-.--.-','!':"-.-.--"}
        MorsetoLetter = {morse: letter for letter, morse in letterToMorse.items()}
        for morseword in cipherText.split("/"):
            word = ""
            for morseletter in morseword.split(" "):
                if morseletter != " " and morseletter!="":
                    word += MorsetoLetter[morseletter]
            plaintext += word + " "
            plaintext = plaintext.lower()
    file_name = output_path+"\{}".format(file.split(".")[0]+"_r07539ym.txt")
    with open(file_name, "w+") as plaintext_file:
        plaintext_file.write(plaintext.strip())
        os.rename(file_name,file.split(".")[0]+"_r07539ym.txt")
