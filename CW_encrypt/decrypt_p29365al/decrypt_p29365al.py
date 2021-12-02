import sys
import os
import argparse


INPUT_FOLDER = sys.argv[1]
OUTPUT_FOLDER = sys.argv[2]
DIRECTORY = os.listdir(INPUT_FOLDER)


def hexDecrypt(data):
    hexadecimal = bytes. fromhex(data)
    english = hexadecimal. decode("ASCII")
    return english


def Caesar_3(plaintext):
    #taken from one of the labs with a slight modification
    decipherText = ""
    plaintextPosition = 0
    while (plaintextPosition < len(plaintext)):
        plaintextChar = plaintext[plaintextPosition]
        ASCIIValue = ord(plaintextChar)

        if plaintextChar != ' ':
            ASCIIValue = ASCIIValue - 3
            if ASCIIValue < ord('a'):
                ASCIIValue = ord('z') - (ord('a') - ASCIIValue)

        decipherText = decipherText + chr(ASCIIValue)
        plaintextPosition = plaintextPosition + 1
    return decipherText


if __name__ == '__main__':

    for i in range(len(DIRECTORY)):

        file = open(INPUT_FOLDER + "/" + DIRECTORY[i])
        text = file.readline()
        start = 0

        if text[start] == "M":

            file_name = DIRECTORY[i]
            morse_converter = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
            morse = text[11:]
            morse += " "
            lenword = len(morse)
            words = ''
            for i in (morse):
                if i != ' ':
                    words=words+i
                    if i not in morse_converter:
                        break
                elif i == '/':
                    output_file = "test_file3_Morse.txt"
                    output_file = OUTPUT_FOLDER + "/" + output_file
                    with open (output_file, "a") as file:
                        file.write(morse_converter[words])
                else:
                    output_file = "test_file3_p29365al.txt"
                    output_file = OUTPUT_FOLDER + "/" + output_file
                    with open (output_file, "a") as file:
                        file.write(morse_converter[words])
                    words = ''
                   
        elif text[start] == "C":
            code = text[18:]
            decipherText = Caesar_3(code)
            output_file = "test_file2_p29365al.txt"
            output_file = OUTPUT_FOLDER + "/" + output_file
            with open (output_file, "a") as file:
                file.write(decipherText)
                file.close()

        elif text[start] == "H":
            english = hexDecrypt(text[4:])
            output_file = "test_file1_p29365al.txt"
            output_file = OUTPUT_FOLDER + "/" + output_file
            with open (output_file, "a") as file:
                file.write(english)
                file.close()