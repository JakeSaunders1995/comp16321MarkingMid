

import sys 
import os 

InFold = sys.argv[1] + "/test_file3.txt"
OutFold = sys.argv[2] + "/decryption.txt"



readFile = open(InFold, "r")
inputCode = readFile.read()






code = str(inputCode)


firstLetter = code[0]



for firstLetter in code:
    if firstLetter == "H":


        def hexToASCII (hexx):
            return chr(int(hexx, 16))

        # hexadecimal = "53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e"
        hexadecimal = code
        
        hexadecimal = hexadecimal.replace(" ", "")
        # hexadecimal = hexadecimal.replace("['Hex:", "")
        # hexadecimal = hexadecimal.replace("']", "")
        hexadecimal = hexadecimal.replace("Hex:", "")
        
        text = ""

        if len(hexadecimal) % 2 == 0:
            for i in range(0, len(hexadecimal), 2):
                string = hexadecimal[i] + hexadecimal[i+1]
                text += hexToASCII (string)

        # print(text)     




    elif firstLetter == "C":

        import string

        plainText = code
        plainText = plainText.replace("Caesar Cipher(+3):", "")
        plainText = plainText.replace("", "")
        # plainText = plainText.replace("")

        shift = -3

        alphabet1 = string.ascii_lowercase 
        alphabet2 = alphabet1[shift:] + alphabet1[:shift]
        table = str.maketrans(alphabet1, alphabet2)

        resultCode = plainText.translate(table)
        
        # print(resultCode)


    if firstLetter == "M":
    # elif firstLetter == "M":


    	

     
        MORSE_CODE_DICT = { 'a':'.-', 'b':'-...',
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
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-'}

        def decrypt(morseCode):


            morseCode += ' '
         
            decryption = ''
            cipher = ''
            for letter in morseCode:
 
                if (letter != ' '):
                    i = 0
                    cipher += letter

                else:
                    i += 1
         
                    if i == 2 :
                        decryption += ' '

                    else:
                        decryption += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                        .values()).index(cipher)]
                        cipher = ''
 
            return decryption

        # morseCode = ".... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. - "

        morseCode = code
        morseCode = morseCode.replace("Morse Code:", "")
        morseCode= morseCode.replace("/", "")

        output = decrypt(morseCode)
        # print (output)

writeFile = open(OutFold, "w")
writeFile.write(output)
writeFile.close()



        
