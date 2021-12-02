# newest version
import argparse, os, re


parser = argparse.ArgumentParser(
    description= "program 2"
)

parser.add_argument("input_file_path", type=str, help = "enter your input folder path directory")
parser.add_argument("output_file_path", type=str, help = "enter your output folder path directory")
args = parser.parse_args()

input_file_path = args.input_file_path
output_file_path = args.output_file_path


input_files_path_list = []

# /////////////////////////////////////////////////////////////////////////////////////////////////////////



for filename in os.listdir(input_file_path):
    if filename.endswith(".txt"):
        construct = input_file_path + "/" + filename
        input_files_path_list.append(construct)
        

# /////////////////////////////////////////////////////////////////////////////////////////////////////////


for files in input_files_path_list:

    deconstruct = re.split("[/.]",files)
    fileNameOnly = deconstruct[1]
    outputFileDirectory = output_file_path + "/" + fileNameOnly + "_p61761ay.txt"


    method = ""
    encryptedMessage = ""

    f = open(files,"r")
    x = str(f.read())

    x = re.split("[:]",x)
    method = x[0]
    encryptedMessage = x[1].lower()
    # print(method)

    y = re.split("[ ]",encryptedMessage)
    encryptedMessage = y
    # print(encryptedMessage)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////
    if (method == "Caesar Cipher(+3)"):
        # print("Requires a Caesar Cipher of +3 \n")
        decryptedMessage = ""


        for i in encryptedMessage:

            for char in i:

                if (char == "."):
                    # this will thus also check ellipses (line by line)
                    decryptedMessage += "."
                    

                elif (char == "?"):
                    decryptedMessage += "?"
                    

                elif (char == "!"):
                    decryptedMessage += "!"

                elif (char == ","):
                    decryptedMessage += ","

                elif (char== ":"):
                    decryptedMessage += ":"

                elif (char== ";"):
                    decryptedMessage += ";"

                elif (char== "-"):
                    decryptedMessage += "-"

                elif (char== "–"):
                    decryptedMessage += "–"

                elif (char== "—"):
                    decryptedMessage += "—"

                elif (char== "("):
                    decryptedMessage += "("


                elif (char== ")"):
                    decryptedMessage += ")"

                elif (char== "{"):
                    decryptedMessage += "{"

                elif (char== "}"):
                    decryptedMessage += "}"

                elif (char== "["):
                    decryptedMessage += "["

                elif (char== "]"):
                    decryptedMessage += "]"

                elif (char== "'"):
                    decryptedMessage += "'"


                elif (char== '"'):
                    decryptedMessage += '"'

                elif (char == "\n"):
                    decryptedMessage +=""

            
            

            




                else: 
                #     ciphertext = char
                #     plaintext = ""
                #     alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
                #     alphabet = alphabet.lower()
                #     ciphertextPosition = 0

                #     while (ciphertextPosition < len(ciphertext)):
                #         ciphertextChar = ciphertext[ciphertextPosition]
                #         alphabetPosition = 3

                #         while (ciphertextChar != alphabet[alphabetPosition]):
                #             alphabetPosition += 1
                #             continue

                #         alphabetPosition = alphabetPosition - 3
                #         plaintext = plaintext + alphabet[alphabetPosition]
                #         ciphertextPosition += 1
                #         continue
                #     plaintext += " "

                # print(plaintext)
                    plaintext = ""
                    alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
                    alphabet = alphabet.lower()
                    ciphertextPosition = 0

                    while (ciphertextPosition < len(char)):
                        ciphertextChar = char[ciphertextPosition]
                        alphabetPosition = 3

                        # print(i)
                        # print(ciphertextChar)
                        # print(alphabet)
                        # print(alphabet[alphabetPosition] + "\n")
                 

                        while (ciphertextChar != alphabet[alphabetPosition]):
                            alphabetPosition += 1
                            # print("cipher text " + ciphertextChar)
                            # print("alphabet position " + alphabet[alphabetPosition])
                            continue
                        

                        # if (ciphertextChar != alphabet[alphabetPosition]):
                        alphabetPosition = alphabetPosition - 3
                        plaintext = plaintext + alphabet[alphabetPosition]
                        ciphertextPosition += 1
                        continue

                    decryptedMessage += plaintext + ""

            decryptedMessage += " "            
        # print(decryptedMessage)

        outputFile = open(outputFileDirectory, "w")
        outputFile.write(decryptedMessage)
        f.close()



# /////////////////////////////////////////////////////////////////////////////////////////////////////////
    elif (method == "Morse Code"):
        # print("Requires Morse Code \n")
        decryptedMessage = ""
        dict_morse_code = { 'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..','/':'-..-.','-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        dictKeys = list(dict_morse_code.keys())
        dictValues = list(dict_morse_code.values())
        counter = 0


        for i in encryptedMessage:

            
            if (i == "/"):
                decryptedMessage += " "
            
            # elif (char == "."):
            #         # this will thus also check ellipses (line by line)
            #     decryptedMessage += "."
                    

            elif (i == "?"):
                decryptedMessage += "?"
                    

            elif (i == "!"):
                decryptedMessage += "!"

            elif (i == ","):
                decryptedMessage += ","

            elif (i== ":"):
                decryptedMessage += ":"

            elif (i== ";"):
                decryptedMessage += ";"

            # elif (char== "-"):
            #     decryptedMessage += "-"

            # elif (char== "–"):
            #     decryptedMessage += "–"

            # elif (char== "—"):
            #     decryptedMessage += "—"

            elif (i== "("):
                decryptedMessage += "("

            elif (i== ")"):
                decryptedMessage += ")"

            elif (i== "{"):
                decryptedMessage += "{"

            elif (i== "}"):
                decryptedMessage += "}"

            elif (i== "["):
                decryptedMessage += "["

            elif (i== "]"):
                decryptedMessage += "]"

            elif (i== "'"):
                decryptedMessage += "'"

            elif (i== '"'):
                decryptedMessage += '"'

            # elif (char == "\n"):
            #     decryptedMessage +=""

            else:

                # shouldRestart = True
                # while shouldRestart:
                #     shouldRestart = False
                for val in dictValues:
                    if (i != val):
                            
                            # print("counter value is: " + str(counter))
                            # print("value in dictionary is: " + val)
                            # print("encrypted character: " + i + "\n")
                        counter += 1

                    elif (i == val):
                            # print(i)
                            # print(counter)
                            # print(dictKeys[counter])
                            # print("counter value is: " + str(counter))
                            # print("value in dictionary is: " + val)
                            # print("encrypted character: " + i + "\n")
                            
                        decryptedMessage += dictKeys[counter]
                        counter = 0
                            # print("found a character: " + decryptedMessage)
                        break
                        
        # print(decryptedMessage)
        outputFile = open(outputFileDirectory, "w")
        outputFile.write(decryptedMessage)
        f.close()
                


            


            


        


# /////////////////////////////////////////////////////////////////////////////////////////////////////////

    elif (method == "Hex"):
        # print("Requires Hex \n")
        decryptedMessage = ""

        for i in encryptedMessage:

            
            
            
            if (i == "."):
                    # this will thus also check ellipses (line by line)
                decryptedMessage += "."
                    

            elif (i == "?"):
                decryptedMessage += "?"
                    

            elif (i == "!"):
                decryptedMessage += "!"

            elif (i == ","):
                decryptedMessage += ","

            elif (i== ":"):
                decryptedMessage += ":"

            elif (i== ";"):
                decryptedMessage += ";"

            elif (i== "-"):
                decryptedMessage += "-"

            elif (i== "–"):
                decryptedMessage += "–"

            elif (i== "—"):
                decryptedMessage += "—"

            elif (i== "("):
                decryptedMessage += "("

            elif (i== ")"):
                decryptedMessage += ")"

            elif (i== "{"):
                decryptedMessage += "{"

            elif (i== "}"):
                decryptedMessage += "}"

            elif (i== "["):
                decryptedMessage += "["

            elif (i== "]"):
                decryptedMessage += "]"

            elif (i== "'"):
                decryptedMessage += "'"

            elif (i== '"'):
                decryptedMessage += '"'
            
            # elif (char == "\n"):
            #     decryptedMessage +=""
            

            else:
                x = int(i,16)
                x = chr(x)
                decryptedMessage += x

        # print(decryptedMessage)
        outputFile = open(outputFileDirectory, "w")
        outputFile.write(decryptedMessage)
        f.close()