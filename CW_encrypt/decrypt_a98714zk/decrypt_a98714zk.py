import sys
import os

directory = str(sys.argv[1])
for filename in os.listdir(directory): # Records all the files/directories in the specified path
    if filename.endswith(".txt"):
        inputTXTfile = os.path.join(directory, filename)
        f = open(inputTXTfile,"r")
        contents = f.read()
        f.close()

        colon_position = contents.find(":")
        algorithm = contents[0:colon_position]

        if (algorithm == "Hex"):
            encryption_method = "hexadecimal"
        elif (algorithm == "Caesar Cipher(+3)"):
            encryption_method = "caesar +3"
        else:
            encryption_method = "morseCode"

        ciphertext = contents[colon_position+1:len(contents)] + " "

        if (encryption_method == "morseCode"):
            morse = {
                '.-': 'a',   '-...': 'b',   '-.-.': 'c',    '-..': 'd',      '.': 'e',   '..-.': 'f', '--.': 'g',   '....': 'h',     '..': 'i',   '.---': 'j',    '-.-': 'k',   '.-..': 'l',
                '--': 'm',     '-.': 'n',    '---': 'o',   '.--.': 'p',   '--.-': 'q',    '.-.': 'r', '...': 's',      '-': 't',    '..-': 'u',   '...-': 'v',    '.--': 'w',   '-..-': 'x',
              '-.--': 'y',   '--..': 'z',  '-----': '0',  '.----': '1',  '..---': '2',  '...--': '3', '....-': '4',  '.....': '5',  '-....': '6',  '--...': '7',  '---..': '8',  '----.': '9',
                 '/': ' ', '.-.-.-': '.', '..--..': '?', '--..--': ',', '-.-.--': '!', '-.--.-': ')', '-.--.': '(', '---...': ':', '-....-': '-'
            }

            morse_letter, morse_letters, count= '', [], 0
            while (count < len(ciphertext)):
                if (ciphertext[count] != ' '):
                    morse_letter += ciphertext[count]
                    count += 1
                else:
                    morse_letters.append(morse_letter)
                    morse_letter = ''
                    count += 1

            morseCode_decipher = ''
            for i in morse_letters:
                morseCode_decipher += morse.get(i)

            save_path = str(sys.argv[2])
            filename_removeTXT = filename[0:-4]
            output_filename = str(filename_removeTXT+"_a98714zk.txt")

            completeName = os.path.join(save_path, output_filename)

            outputFile = open(completeName, "w+")
            outputFile.write(morseCode_decipher.lower())
            outputFile.close

        elif (encryption_method == "hexadecimal"):
            hex_letter, hex_letters, count= '', [], 0
            while (count < len(ciphertext)):
                if (ciphertext[count] != ' '):
                    hex_letter += ciphertext[count]
                    count += 1
                else:
                    hex_letters.append(hex_letter)
                    hex_letter = ''
                    count += 1

            hex_decipher = ''
            for i in hex_letters:
                hex_decipher += bytearray.fromhex(i).decode()

            save_path = str(sys.argv[2])
            filename_removeTXT = filename[0:-4]
            output_filename = str(filename_removeTXT+"_a98714zk.txt")

            completeName = os.path.join(save_path, output_filename)

            outputFile = open(completeName, "w+")
            outputFile.write(hex_decipher.lower())
            outputFile.close

        elif (encryption_method == "caesar +3"):
            symbols = "0123456789?![]{}(),.-:;\'\" "
            caesar_decipher, decrypttextPosition = '', 0

            while (decrypttextPosition < len(ciphertext)):
                if (ciphertext[decrypttextPosition] == "a" or ciphertext[decrypttextPosition] == "A"):
                    if (ciphertext[decrypttextPosition] == "a"):
                        caesar_decipher += "x"
                        decrypttextPosition += 1
                    else:
                        caesar_decipher += "X"
                        decrypttextPosition += 1
                elif (ciphertext[decrypttextPosition] == "b" or ciphertext[decrypttextPosition] == "B"):
                    if (ciphertext[decrypttextPosition] == "b"):
                        caesar_decipher += "y"
                        decrypttextPosition += 1
                    else:
                        caesar_decipher += "Y"
                        decrypttextPosition += 1
                elif (ciphertext[decrypttextPosition] == "c" or ciphertext[decrypttextPosition] == "C"):
                    if (ciphertext[decrypttextPosition] == "c"):
                        caesar_decipher += "z"
                        decrypttextPosition += 1
                    else:
                        caesar_decipher += "Z"
                        decrypttextPosition += 1
                elif (ciphertext[decrypttextPosition] not in symbols):
                    plaintextChar = ciphertext[decrypttextPosition]
                    ASCIIvalue = ord(plaintextChar)
                    ASCIIvalue -= 3
                    caesar_decipher += chr(ASCIIvalue)
                    decrypttextPosition += 1
                else:
                    caesar_decipher += ciphertext[decrypttextPosition]
                    decrypttextPosition += 1

                save_path = str(sys.argv[2])
                filename_removeTXT = filename[0:-4]
                output_filename = str(filename_removeTXT+"_a98714zk.txt")

                completeName = os.path.join(save_path, output_filename)

                outputFile = open(completeName, "w+")
                outputFile.write(caesar_decipher.lower())
                outputFile.close
