import argparse
import os
import string
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
parser.add_argument("output", type=str)
args = parser.parse_args()

input = args.input
output = args.output

punctuation=string.punctuation
alphabet=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
for file in os.listdir(input):
    f = open(input+"/"+file,"r")
    encryption = f.read()

    separate = encryption.split(":") #creates a list with 2 items: items before ':' and after ':'

    algorithm=separate[0]
    ciphertext=separate[1]
    plaintext_list=[]

    if algorithm == "Hex":
        hex_values=ciphertext.split()
        for i in hex_values:
            hex_as_int=int(i,16) #converts hex into a base 10 number. in int(i,16), 16 specifies the base
            letter=chr(hex_as_int)
            plaintext_list.append(letter)
        plaintext="".join(plaintext_list)

    elif algorithm == "Caesar Cipher(+3)":
        words=ciphertext.split()

        for word in words:
            indiv="" #string of an individual word
            for letter in word:
                if letter in punctuation:
                    indiv+=letter
                else:
                    index=alphabet.index(letter)-3
                    indiv+=alphabet[index]
            plaintext_list.append(indiv)
        plaintext=" ".join(plaintext_list) # converts the list into a sentence with spaces
    elif algorithm == "Morse Code":
        morse={".-":"a",
        "-...":"b",
        "-.-.":"c",
        "-..":"d",
        ".":"e",
        "..-.":"f",
        "--.":"g",
        "....":"h",
        "..":"i",
        ".---":"j",
        "-.-":"k",
        ".-..":"l",
        "--":"m",
        "-.":"n",
        "---":"o",
        ".--.":"p",
        "--.-":"q",
        ".-.":"r",
        "...":"s",
        "-":"t",
        "..-":"u",
        "...-":"v",
        ".--":"w",
        "-..-":"x",
        "-.--":"y",
        "--..":"z",
        ".----":"1",
        "..---":"2",
        "...--":"3",
        "....-":"4",
        ".....":"5",
        "-....":"6",
        "--...":"7",
        "---..":"8",
        "----.":"9",
        "-----":"0",
        ".-.-.-":".",
        "..--..":"?",
        "-.-.--":"!",
        "--..--":",",
        "---...":":",
        "-.-.-.":";",
        "-..-.":"/",
        "-....-":"-",
        "-.--.":"(",
        "-.--.-":")",
        ".----.":"'"
        }
        words=ciphertext.split("/")
        for word in words:
            word=word.split()
            indiv=""
            for letter in word:
                letter=letter.strip()
                indiv+=morse[letter]
            plaintext_list.append(indiv)
        plaintext=" ".join(plaintext_list)
    plaintext=plaintext.lower()
    f.close()
    file = open(output+"/"+file[:-4]+"_t56563bk.txt","w")
    file.write(plaintext)
