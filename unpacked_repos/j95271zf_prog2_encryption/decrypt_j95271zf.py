import argparse
import re
import os

parser = argparse.ArgumentParser(description = 'Path')
parser.add_argument('inputpath', type=str, help='input file path')
parser.add_argument('outputpath', type=str, help='output file path')
args = parser.parse_args()

InputPath = args.inputpath
OutputPath = args.outputpath
dirs1 = os.listdir(args.inputpath)

for filein in dirs1:
    f = open(InputPath + "/" + filein)
    cipher = f.read()
    
    decryption = ""
    MorseCode = {'.-':'a', '-...':'b',
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
                '-.--.':'(', '-.--.-':')', '---...':':',
                '-.-.-.':';', '-...-':'=', '.----.':"'",
                '-.-.--':'!', '..--.-':'_', '.-..-.':'"',
                '...-..-':'$', '.-...':'&', '.--.-.':'@',
                '.-.-.':'+'}
    message = ""

    if cipher[0] == "H":
        for i in range(4,len(cipher),3):
            hexChar = cipher[i:i+2]
            Dec = int(hexChar,16)
            if Dec > 96 or Dec < 65:
                ASCIIvalue = chr(Dec)
            else:
                ASCIIvalue = chr(Dec + 32)
            decryption += ASCIIvalue
        ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","w")
        ff.write(decryption)
        ff.close()
        

    if cipher[0] == "C":
        for i in range(18,(len(cipher)-1)):
            if ord(cipher[i]) == 32:
                NewValue = cipher[i]
            elif ord(cipher[i]) == 97:
                NewValue = "x"
            elif ord(cipher[i]) == 98:
                NewValue = "y"
            elif ord(cipher[i]) == 99:
                NewValue = "z"
            else:
                NewValue = chr(ord(cipher[i])-3)
            decryption += NewValue
        ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","w")
        ff.write(decryption)
        ff.close()
    

    if cipher[0] == "M":
        cipher = re.split("\:|\ |\/",cipher)
        for i in range(2,len(cipher)):
            if cipher[i] == '' and cipher[i+1] == '':
                ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","a")
                ff.write(" ")
                ff.close()
            elif cipher[i] == '' and cipher[i+1] != '':
                ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","a")
                ff.write("")
                ff.close() 
            else:
                ff = open(OutputPath + "/" + filein[:-4] + "_j95271zf.txt","a")
                ff.write(MorseCode.get(cipher[i]))
                ff.close()

    f.close()

