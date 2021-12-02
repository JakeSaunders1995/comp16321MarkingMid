import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

openf = os.listdir(args.input)
printf = os.listdir(args.output)

sCounter=0
while sCounter<len(openf):
    file=args.input+"/"+openf[sCounter]
    text=open(file, "r")

    word=""
    morse={ 'A':'.-', 'B':'-...',
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
            '(':'-.--.', ')':'-.--.-', ' ':'/'}
    codeType =0

    #words ready to be decrypted
    while True:
        x=text.read(1)
        if not x:
            break
        word+=x

    if word[0]=="H":
        codeType=1
    elif word[0]=="C":
        codeType=2
    elif word[0]=="M":
        codeType=3

    text.close()

    found=True
    decipheredText = str()
    cipheredText=""
    wordPosition = 0
    cipheredTextPosition = 0
    i=0

    while i<len(word) and found==True:
        if word[i] == ":":
            found = False
            wordPosition=i+1
        i+=1

    while wordPosition<len(word):
        cipheredText = cipheredText + word[wordPosition]
        wordPosition+=1

    if codeType==3:      #Morse
        decipheredText = ''
        morseSingle = ''
        for letter in cipheredText:
            if (letter != ' '):
                space = 0
                morseSingle += letter
            else:
                space += 1
                if space == 2 :
                    decipheredText += ' '
                else:
                    decipheredText += list(morse.keys())[list(morse.values()).index(morseSingle)]
                    morseSingle = ''

    elif codeType == 2:      #Caesar
        while cipheredTextPosition<len(cipheredText) :
            cipheredTextChar= cipheredText[cipheredTextPosition]
            if cipheredTextChar == " ":
                decipheredText += " "
            else:
                ASCIIValue= ord(cipheredTextChar)
                ASCIIValue-=3
                decipheredText+=chr(ASCIIValue)
            cipheredTextPosition+=1
    elif codeType == 1:      #Hex
        while cipheredTextPosition<(len(cipheredText)-2):
            i+=1
            hex1=cipheredText[cipheredTextPosition]
            hex2=cipheredText[cipheredTextPosition+1]
            if hex1 == ' ' or hex2 == ' ':
                cipheredTextPosition+=1
                i=0
            else:
                x1= int(hex1, base=16)
                x2= int(hex2, base=16)
                char= chr((x1*16) + x2)
                decipheredText = decipheredText + char.lower()
                cipheredTextPosition += 1
                i+=1

    filename = openf[sCounter]
    filenameNew = filename[0:len(filename) - 4] + "_j52026pk.txt"

    printfile=open(filenameNew, "w")
    printfile.write(decipheredText.lower())
    printfile.close()
    sCounter+=1
