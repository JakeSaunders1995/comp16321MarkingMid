import os, argparse, re
from pathlib import Path

#takes folder input
parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)
parser.add_argument("destination_path", type=Path)
p = parser.parse_args()

decoded = ""
for file in os.listdir(p.file_path):
      openedFile = open((str(p.file_path) + "/" + str(file)),"r")
      line = openedFile.read()
      openedFile.close()

      colonIndex = line.find(':')
      cipherType = line[0:colonIndex]
      cipher = line[colonIndex+1:len(line)]

      if cipherType == "Hex":
          decoded =  bytearray.fromhex(cipher).decode()

      if cipherType == "Caesar Cipher(+3)":
          decoded = ""
          alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
          ciphertextPosition = 0
          ciphertextChar = "a"
          while (ciphertextPosition < (len(cipher)-1)):
              ciphertextChar = cipher[ciphertextPosition]
              alphabetPosition = 29
              if cipher[ciphertextPosition] == " ":
                  decoded = decoded + " "
              else:
                  while ciphertextChar != alphabet[alphabetPosition]:
                      alphabetPosition = alphabetPosition - 1

                  alphabetPosition = alphabetPosition - 3
                  decoded = decoded + alphabet[alphabetPosition]
              ciphertextPosition += 1

      if cipherType == "Morse Code":
          morseCode =   {'.-': 'a',     '-...': 'b',   '-.-.': 'c',
        '-..': 'd',    '.': 'e',      '..-.': 'f',
        '--.': 'g',    '....': 'h',   '..': 'i',
        '.---': 'j',   '-.-': 'k',    '.-..': 'l',
        '--': 'm',     '-.': 'n',     '---': 'o',
        '.--.': 'p',   '--.-': 'q',   '.-.': 'r',
        '...': 's',    '-': 't',      '..-': 'u',
        '...-': 'v',   '.--': 'w',    '-..-': 'x',
        '-.--': 'y',   '--..': 'z',

        '-----': '0',  '.----': '1',  '..---': '2',
        '...--': '3',  '....-': '4',  '.....': '5',
        '-....': '6',  '--...': '7',  '---..': '8',
        '----.': '9',  '.-.-.-':'.',  '--..--': ',',
        '..--..': '?',  '-.-.--':'!',  '.----.': "'",
        '.-..-.': '"',  '-.--.':'(',  '-.--.-': ')',
        '.-...': '&',  '---...':':',  '-.-.-.': ';',
        '-..-.': '/',  '..--.-':'-',  '-...-': '=',
        '-....-':'-',
        }
        #M = Morse E = English
          Mchar = ""
          letterList = []
          sentence = ""
          for x in range(0, len(cipher)):
             if cipher[x] == "/":
                 sentence = sentence + " "
             elif (cipher[x] == " ") and (Mchar != ""):
                 #translate
                 Eletter = morseCode.get(Mchar)
                 sentence = sentence + Eletter
                 Mchar = ""
             elif (cipher[x] == " "):
                 continue
             else:
                 Mchar = Mchar + cipher[x]
                 if x == len(cipher)-1:
                     Eletter = morseCode.get(Mchar)
                     sentence = sentence + Eletter
                     Mchar = ""

          decoded = sentence

      file = file.replace(".txt", "_f77541nz.txt", 1)
      openedFile = open((str(p.destination_path) + "/" + str(file)),"w")
      openedFile.write(decoded)
      openedFile.close()
