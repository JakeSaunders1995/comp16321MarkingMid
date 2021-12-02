import sys
from os import listdir
from os.path import isfile, join
import re


inputFolder = sys.argv[1]



Files = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]


morse = {
    '.-':'a', '-...':'b',
    '-.-.':'c', '-..':'d', '.':'e',
    '..-.':'f', '--.':'g', '....':'h',
    '..':'i', '.---':'j', '-.-':'k',
    '.-..':'l', '--':'m', '-.':'n',
    '---':'o', '.--.':'p', '--.-':'q',
    '.-.':'r', '...':'s', '-':'t',
    '..-':'u', '...-':'v', '.--':'w',
    '-..-':'x', '-.--':'y', '--..':'z',
    '.----':'1', '..---':'2', '...--':'3',
    '....-':'4', '.....':'5', '-....':'6',
    '--...':'7', '---..':'8', '----.':'9',
    '-----':'0', '--..--':',', '.-.-.-':'.',
    '..--..':'?', '-..-.':'/', '-....-':'-',
    '-.--.':'(', '-.--.-':')', '/' : ' '
}





def caesarTranslator(word):
       Translate = ""
       alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
       word = word.upper()
       for x in word:
              if x in alphabet:
                    position = alphabet.find(x)
                    newPos = (position - 3) % 26
                    newChar = alphabet[newPos]
                    Translate += newChar
              else:
                    Translate += x
       return Translate    


def hexTranslator(word):
       Translate = " "
       x = 4
       while x < (len(word))-1:
              subString = word[x]+word[x+1]
              integer = str(subString, 16)
              Translate += chr(integer)
              x += 2
       return Translate

def  morseTrans(word, positionInString = 0):
               
               if positionInString < len(word):
                   morseLetter = ""
                   for key,char in enumerate(word[positionInString:]):
                       if char == " ":
                           positionInString = key + positionInString + 1
                           letter = morse[morseLetter]
                           return letter + morseTrans(word, positionInString)
                       
                       else:
                           morseLetter += char
               else:
                   return ""
               


def outputs(inputText):
       decryptAnswer = " "

       if inputText[0] == "H":
              decryptAnswer = hexTranslator(inputText)
       elif inputText[0] == "M":
              decryptAnswer =  morseTrans(inputText)
       elif inputText[0] == "C":
              decryptAnswer = caesarTranslator(inputText)
       
       return decryptAnswer

for file in Files:
       inputFile = open(f"{inputFolder}/{file}")
       
       text = inputFile.readline()
       answer = printAnswer(text)

       outputFolder = sys.argv[2]
       outputFile = open(f"{outputFolder}/{file[:-4]}_h15879ac.txt","w")
       outputFile.write(answer)


       inputFile.close()
       outputFile.close() 
