import argparse
import os
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
morse = {'.-' : 'a','-...' : 'b','-.-.' : 'c','-..' : 'd','.' : 'e','..-.' : 'f','--.' : 'g','....' : 'h','..' : 'i','.---' : 'j','-.-' : 'k','.-..' : 'l','--' : 'm','-.' : 'n','---' : 'o','.--.' : 'p','--.-' : 'q','.-.' : 'r','...' : 's','-' : 't','..-' : 'u','...-' : 'v','.--' : 'w','-..-' : 'x','-.--' : 'y','--..' : 'z','.----' : '1','..---' : '2','...--' : '3','....-' : '4','.....' : '5','-....' : '6','--...' : '7','---..' : '8','----.' : '9','-----' : '0','--..--' : ', ','.-.-.-' : '.','..--..' : '?','-..-.' : '/','-....-' : '-','-.--.' : '(','-.--.-' : ')'}
parser = argparse.ArgumentParser()
parser.add_argument('inputf', type=str)
parser.add_argument('outputf', type=str)
args = parser.parse_args()
inputfiles = os.listdir(args.inputf)
for file in inputfiles:
    fileloc = fr'{args.inputf}/{file}'
    outloc = fr'{args.outputf}/{file[: -4]}_e22628ak.txt'
    fin = open(fileloc, 'r')
    fout = open(outloc, 'w')
    line = fin.readline()
    inp = line.strip()
    cmndend = inp.find(':')
    cmnd = inp[:cmndend]
    txt = inp[cmndend+1:]
    newtxt = ''

    if cmnd.startswith('Hex') == True:
        txt = txt.split(' ')
        for hex in txt:
            hexletter = int(hex, base=16)
            hexletter = chr(hexletter)
            newtxt = newtxt + hexletter
    elif cmnd.startswith('Caesar') == True:
        for letter in txt:
            if letter != ' ':
                letterindex = letters.index(letter) - 3
                newletter = letters[letterindex]
            else:
                newletter = ' '
            newtxt = newtxt + newletter
    else:
        temptxt = []
        txt = txt.split('/')
        for word in txt:
            word = word.strip()
            newword = word.split(' ')
            temptxt.append(newword)
        for word in temptxt:
            for letter in word:
                morsechar = morse.get(letter)
                newtxt = newtxt + morsechar
            newtxt = newtxt + ' '
            
    output = newtxt.lower()
    fout.write(output)
    fin.close()
    fout.close()