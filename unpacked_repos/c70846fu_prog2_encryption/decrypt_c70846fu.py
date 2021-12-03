import sys
import os

input_decrypt = sys.argv[1]
output_decrypt = sys.argv[2]
text_decrypt = []
input_folder_amount = 0

for filename in sorted(os.listdir(input_decrypt)):
    input_folder_amount += 1
    with open(os.path.join(input_decrypt, filename), 'r') as f:
        encrypted_to_string = f.read().rstrip()
        text_decrypt.append(encrypted_to_string)

morse_dictionary = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

SplitText = text_decrypt.split(":")

def CaesarDecrypt(inp):
    encrypted = inp
    decrypted = ""
    for x in encrypted:
        if x == " ":
            decrypted += " "
        else:
            decrypted += chr(ord(x)-3)
    return(decrypted.lower())

def HexDecrypt(inp):
    encrypted = inp    
    decrypted = ""
    for i in range(0,len(encrypted),3):
        decrypted += (chr(int(encrypted[i:i+2],16)))
    return(decrypted.lower())

def MorseDecrypt(inp):
    encrypted = inp.split("/")
    decrypted = ""
    for i in encrypted:
        tempArray = i.split(" ")
        for j in tempArray:
            if j in morse_dictionary.values():
                decrypted += (list(morse_dictionary.keys())[list(morse_dictionary.values()).index(j)])
        decrypted += " "
    return(decrypted.lower())

if SplitText[0] == "Caesar":
    print(CaesarDecrypt(SplitText[1]))
elif SplitText[0] == "Hex":
    print(HexDecrypt(SplitText[1]))
else:
    print(MorseDecrypt(SplitText[1]))


if splitText[0] == "Caesar":
    decrypted_file_name = "decrypted" + "_c70846fu"
    output = open(output_decrypt+"/"+decrypted_file_name+".txt", "w+")
    output_decrypt.write(print(CaesarDecrypt(splitText[1])))
elif splitText[0] == "Hex":
    decrypted_file_name = "decrypted" + "_c70846fu"
    output = open(output_decrypt+"/"+decrypted_file_name+".txt", "w+")
    output_decrypt.write(print(HexDecrypt(splitText[1])))
else:
    decrypted_file_name = "decrypted" + "_c70846fu"
    output = open(output_decrypt+"/"+decrypted_file_name+".txt", "w+")
    output_decrypt.write(print(MorseDecrypt(splitText[1])))

#got this to work with an input e.g. input="" , splittext = input.split(":") , however i couldnt get it to work properly for input file then output file .