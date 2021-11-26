import sys
import os
OutputFolder = sys.argv[-1]
InputFolder = sys.argv[-2]

textFiles = os.listdir(InputFolder)

def hexadecimal(string):
    decryptedString = bytes.fromhex(string).decode('utf-8')
    return decryptedString.lower()

def morseCode(string):
    MorseDict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd',
                 '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                 '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
                 '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                 '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                 '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                 '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2',
                 '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                 '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
                #removed all punctionation from this as it says it doesnt need it

    string = string.split()
    decryptedString = ''
    
    for each in string:
        if each == '/':
            decryptedString += ' '
        else:
            decryptedString += MorseDict.get(each)
    
    return decryptedString.lower()

def caesar(string):
    string = string.strip()
    decryptedString = ""
    plaintextPosition = 0
    while (plaintextPosition < len(string)):
        plaintextChar = string[plaintextPosition]
        ASCIIValue = ord(plaintextChar)
        if ASCIIValue == 32:
            decryptedString += ' '
        else:
            ASCIIValue = ASCIIValue - 3
            if ASCIIValue < 97:
                ASCIIValue += 26
            decryptedString += chr(ASCIIValue)
        
        plaintextPosition += 1
    
    return decryptedString.lower()


for each in textFiles:
    outFilePath = OutputFolder + '/' + each[0:-4] + '_h08963ob.txt'
    path = InputFolder + '/' + each
    inpf = open(path, "r")
    encryptedString = inpf.read()
    inpf.close()
    
    #figure out which encryption method is used:
    for i in range(len(encryptedString)):  #find where the colon is
        if encryptedString[i] == ':':
            posColon = i
    
    #take everthing before the colon as the encryption type
    encryptMethod = encryptedString[0:posColon]
   
    if encryptMethod == 'Hex':
        decryptedString = hexadecimal(encryptedString[posColon+1:])
        
    elif encryptMethod == 'Morse Code':
        decryptedString = morseCode(encryptedString[posColon+1:])
        
    else:
        decryptedString = caesar(encryptedString[posColon+1:])
    
    outf = open(outFilePath, 'w+')
    outf.write(decryptedString)
    outf.close()
    