import argparse
import re
import os

parser = argparse.ArgumentParser(description='Input and Output files')
parser.add_argument('inputfile', type=str, help='Input file')
parser.add_argument('outputfile', type=str, help='Output file')
args = parser.parse_args()


inputFile = args.inputfile
outputFile = args.outputfile

def fileWrite(directory,file,out):
    if outputFile[-1] != "/":
        outputName = outputFile + "/" + x.split(".txt")[0] + "_j91917bs.txt"
        outFile = outputName
        dir = os.path.dirname(outFile)
    else:
        outputName = outputFile + x.split(".txt")[0] + "_j91917bs.txt"
        dir = os.path.dirname(outputFile)

    if not os.path.exists(dir):
        os.makedirs(dir)

    decryptedDone = open(outFile, "w")
    decryptedDone.write(out)
    decryptedDone.close()


for x in os.listdir(inputFile):

    file = os.path.join(inputFile, x)
    dpath = os.path.dirname(file)

    readFile = open(file, "r")
    line = readFile.readline()

    split = re.split('[:]', line)
    typeOfEncryption = split[0]
    data = split[1]

    if split[0] == "Hex":
      #HEX
      hexDecrypted = bytes.fromhex(split[1]).decode("ascii") #fromhex turns into byte string, decode turns into normal
      decryptedLower = hexDecrypted.lower()
      # print(decryptedLower)
      fileWrite(outputFile, x, decryptedLower)


    elif split[0] == "Caesar Cipher(+3)":
      #CAESAR CIPHER
      alphabet = "abcdefghijklmnopqrstuvwxyz"
      decryptedText = ""
      for i in range(len(data)):
          item = data[i].lower()
          if item in alphabet:
              pos = alphabet.find(item)
              newLetter = ((pos - 3) % 26)
              decryptedText += alphabet[newLetter]
          else:
              decryptedText += item
      fileWrite(outputFile, x, decryptedText)


    elif split[0] == "Morse Code":
      #Morse
      dict = {
      'A':'.-', 'B':'-...',
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
      '(':'-.--.', ')':'-.--.-', ' ': '/'
      }

      msg = split[1]
      msg += " "

      encrypted = ""
      decrypted = ""


      for y in msg:
            if (y != " "):
                j = 0
                encrypted += y
            else:
                j += 1
                if j == 2:
                    decrypted += ' '
                else:
                    decrypted += list(dict.keys())[list(dict
                    .values()).index(encrypted)]
                    encrypted = ''

      decryptedLower = decrypted.lower()
      fileWrite(outputFile, x, decryptedLower) 
