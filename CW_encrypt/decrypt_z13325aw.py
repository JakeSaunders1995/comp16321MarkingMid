#Final: Decrypting Hex, Casaer + 3, and International Morse Code

import argparse, os, re

#Getting Args from the Terminal
parser = argparse.ArgumentParser()
parser.add_argument("input", type = str)
parser.add_argument("output", type = str)
args = parser.parse_args()

# Iterating through all Files in Input Folder
for file in os.listdir(args.input):
    
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{args.input}/{file}"
        
        #Getting Contents of File
        with open(file_path, "r") as f:
            cipherKey_and_ciphertext = f.read()

        #Getting Cipher Key
        cipherKey = cipherKey_and_ciphertext
        cipherKey = cipherKey.replace(" ","") #Removing Spaces
        cipherKey = cipherKey.lower()
        cipherKey = re.findall("hex|caesarcipher|morsecode", cipherKey)
        print(cipherKey)

        #Erasing Key from Contents of File
        ciphertext = re.sub(r"^.*?:", "", cipherKey_and_ciphertext)

        #Initializing decrypted Variable as it will be needed Later
        decrypted = ""

        #Decrypting Contents of File

        if (cipherKey[0] == "hex"):
            decrypted = bytes.fromhex(ciphertext).decode("ASCII")
            
        elif (cipherKey[0] == "caesarcipher"):
            ciphertext = ciphertext.lower()
            alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
            ciphertextPosition = 0

            while (ciphertextPosition < len(ciphertext)):
    
                ciphertextChar = ciphertext[ciphertextPosition]
                alphabetPosition = 3

                if not re.search(ciphertextChar, alphabet):
                    decrypted += ciphertextChar
                    ciphertextPosition += 1

                else:
                    while ciphertextChar != alphabet[alphabetPosition]:
                        alphabetPosition = alphabetPosition + 1
                                            
                    alphabetPosition = alphabetPosition - 3
                    decrypted += alphabet[alphabetPosition]
                    ciphertextPosition += 1
                   

        elif (cipherKey[0] == "morsecode"):
            morsecodeDictionary = {
                "A": ".-",
                "B": "-...",
                "C": "-.-.",
                "D": "-..",
                "E": ".",
                "F": "..-.",
                "G": "--.",
                "H": "....",
                "I": ".." ,
                "J": ".---",
                "K": "-.-",
                "L": ".-..",
                "M": "--",
                "N": "-.",
                "O": "---",
                "P": ".--.",
                "Q": "--.-",
                "R": ".-.",
                "S": "...",
                "T": "-",
                "U": "..-",
                "V": "...-",
                "W": ".--",
                "X": "-..-",
                "Y": "-.--",
                "Z": "--..",
                "0": "-----",
                "1": ".----",
                "2": "..---",
                "3": "...--",
                "4": "....-",
                "5": ".....",
                "6": "-....",
                "7": "--...",
                "8": "---..",
                "9": "----.",
                "@": ".--.-.",
                " ": "/",
            }

            morseChar = ""

            for morseLetter in ciphertext: 
                if (morseLetter != " "): # checks for space
                    morseChar += morseLetter #storing morse letters until they make a character
                
                else:
                    # accessing the keys using their values (reversing the encryption)
                    decrypted += list(morsecodeDictionary.keys())[list(morsecodeDictionary.values()).index(morseChar)]
                    morseChar = ""    
            if ciphertext.endswith(" ") or ciphertext.endswith("\n"):
                pass             
            else:
                decrypted += list(morsecodeDictionary.keys())[list(morsecodeDictionary.values()).index(morseChar)]

        decrypted = decrypted.lower() #decrypted message must be lowercase

        #Outputting File with Decrypted Text
        onlyName = os.path.splitext(file)[0] #Removes Extension from File Name
        newName = onlyName + "_z13325aw" + ".txt" 
        file_path = f"{args.output}/{newName}"
        with open(file_path, "w") as o:
            o.write(decrypted)



        






