import sys
import os
import glob

# dictionaries start
morseCode = {'.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
            '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
            '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o',
            '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
            '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y',
            '--..':'z', '-----':'0', '.----':'1', '..---':'2', '...--':'3',
            '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8',
            '----.':'9', '.-.-.-':'.', '--..--':',','---...':':', '-.-.-.':';',
            '-....-':'-', '-.--.':'(', '-.--.-':')', '.----.':'\'', '.-..-.':'\"',
            '-.-.--':'!', '..--..':'?', '-..-.':'/', '.--.-.':'@', '.-.-.':'+',
            '/':' ', '.-...':'&', '..--.-':'_', '-...-':'='
            }

caesar = {'d':'a', 'e':'b', 'f':'c', 'g':'d', 'h':'e',
          'i':'f', 'j':'g', 'k':'h', 'l':'i', 'm':'j',
          'n':'k', 'o':'l', 'p':'m', 'q':'n', 'r':'o',
          's':'p', 't':'q', 'u':'r', 'v':'s', 'w':'t',
          'x':'u', 'y':'v', 'z':'w', 'a':'x', 'b':'y',
          'c':'z',}

hex = {'41':'a', '42':'b', '43':'c', '44':'d', '45':'e',
       '46':'f', '47':'g', '48':'h', '49':'i', '4a':'j',
       '4b':'k', '4c':'l', '4d':'m', '4e':'n', '4f':'o',
       '50':'p', '51':'q', '52':'r', '53':'s', '54':'t',
       '55':'u', '56':'v', '57':'w', '58':'x', '59':'y',
       '61':'a', '62':'b', '63':'c', '64':'d', '65':'e',
       '66':'f', '67':'g', '68':'h', '69':'i', '6a':'j',
       '6b':'k', '6c':'l', '6d':'m', '6e':'n', '6f':'o',
       '70':'p', '71':'q', '72':'r', '73':'s', '74':'t',
       '75':'u', '76':'v', '77':'w', '78':'x', '79':'y',
       '5a':'z', '7a':'z', '20':' ', '21':'!', '22':'\"',
       '23':'#', '24':'$', '25':'%', '26':'&', '27':'\'',
       '28':'(', '29':')', '2a':'*', '2b':'+', '2c':',',
       '2d':'-', '2e':'.', '2f':'/', '30':'0', '31':'1',
       '32':'2', '33':'3', '34':'4', '35':'5', '36':'6',
       '37':'7', '38':'8', '39':'9', '3a':':', '3b':';',
       '3c':'<', '3d':'=', '3e':'>', '3f':'?', '5b':'[',
       '5c':'\\', '5d':']', '5e':'^', '5f':'_', '60':'`',
       '7b':'{', '7c':'|', '7d':'}', '7e':'~'}
#dictionaries end

pathIn = sys.argv[1]
pathOut = sys.argv[2]
dirIn = os.path.join(pathIn, '*.txt')

for i in glob.glob(dirIn):
    fIn = open(os.path.join(os.getcwd(), i), 'r')
    filename = os.path.splitext(os.path.basename(i))[0]
    algotext = str(fIn.read())
    split = algotext.split(':')
    algorithm = split[0]
    cipherText = split[1]
    encrypted = cipherText.split(' ')
    plainText = ""

    if (algorithm[0] == 'm' or algorithm[0] == 'M'):
        for x in encrypted:
            plainText += morseCode[x]

    elif (algorithm[0] == 'c' or algorithm[0] == 'C'):
        a = 0
        b = 0
        for words in encrypted:
            word = words.split()
            for i in word:
                letters = list(i)
                for x in letters:
                    plainText += caesar[x]
                plainText += ' '

    elif (algorithm[0] == 'h' or algorithm [0] == 'H'):
        for x in encrypted:
            plainText += hex[x]

    else:
        print("Algorithm not found")

    if os.path.exists(pathOut):
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'w')
        print(plainText, file = fOut)
        fOut.close()
    else:
        os.makedirs(pathOut)
        newFile = filename + '_r22997aa.txt'
        dirOut = os.path.join(pathOut, newFile)
        fOut = open(dirOut, 'w')
        print(plainText, file = fOut)
        fOut.close()
