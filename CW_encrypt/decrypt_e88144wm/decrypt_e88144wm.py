import os, argparse

# handels the command line arguments, turns them into varibales
parser = argparse.ArgumentParser()
parser.add_argument('inputPath', type=str)
parser.add_argument('outputPath', type=str)
args = parser.parse_args()

# sets variables to the input and output path specified by the user
inpPath = args.inputPath
outPath = args.outputPath


morseDict = {
    '.-' : 'a' , '-...' : 'b', '-.-.': 'c' , 
    '-..' : 'd' , '.' : 'e' , '..-.': 'f' , 
    '--.' : 'g' , '....' : 'h' , '..': 'i' , 
    '.---' : 'j' , '-.-' : 'k' ,
    '.-..' : 'l' , '--' : 'm' , '-.': 'n' ,
    '---' : 'o' , '.--.' : 'p' , '--.-': 'q' ,
    '.-.' : 'r' , '...' : 's' , '-': 't' ,
    '..-' : 'u' , '...-' : 'v' , '.--': 'w' ,
    '-..-' : 'x' , '-.--' : 'y' , '--..': 'z' ,
    '.----' : '1' , '..---' : '2' , '...--': '3' ,
    '....-' : '4' , '.....' : '5' , '-....': '6' ,
    '--...' : '7' , '---..' : '8' , '----.': '9' ,
    '-----' : '0' , '--..--' : ',' , '.-.-.-': '.' ,
    '..--..' : '?' , '-..-.' : '/' , '-....-': '-' ,
    '-.--.' : '(' , '-.--.-' : ')' , '': ''
}

def hex_decrypt(value):
    decrypted = bytes.fromhex(value).decode()
    decrypted = decrypted.lower()
    return(decrypted)

def caesar_decrypt(value):
    normal_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    caesar_alpha = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', ' ']
    decrypted = ''
    for i in value:
        index = caesar_alpha.index(i)
        decrypted = decrypted + normal_alpha[index]
    return decrypted
    
def morse_decrypt(value):
    decrypted = ''
    value = value.split('/') 
    for i in value:
        word = ''
        wordList = i.split(' ')
        for letter in wordList:
            word = word + morseDict[letter]
        decrypted = decrypted + word + ' '
    return decrypted[:-1]


# looping through files
for name in os.listdir(inpPath):
    file = open(inpPath + '/' + name, 'r')
    data = file.read()
    data = data.split(':')
    text = data[1].replace('\n', '')
    if data[0] == 'Hex':
        text = hex_decrypt(text)
    elif data[0] == 'Caesar Cipher(+3)':
        text = caesar_decrypt(text)
    else:
        text = morse_decrypt(text)

    name = name[:-4] + "_e88144wm.txt"
    outputFile = open(outPath + '/' + name, 'a')
    outputFile.write(text)
    outputFile.close()
