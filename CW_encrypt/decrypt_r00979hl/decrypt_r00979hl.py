# a python program written by Hanmin Liu
# decryption
import os
import argparse
#initialize arguments
parser = argparse.ArgumentParser()
parser.add_argument("fin", help="state the input file here")
parser.add_argument("fout", help="state the output file here")
args = parser.parse_args()

input_folder = os.scandir(args.fin)

#initialize table and dictionary
alpha = "xyzabcdefghijklmnopqrstuvwxyz"
morse = {
#according to wikipekia
'.-': 'a',
'-...':'b',
'-.-.':'c',
'-..':'d',
'.':'e',
'..-.':'f',
'--.': 'g',
'....': 'h',
'..': 'i',
'.---':'j',
'-.-': 'k',
'.-..': 'l',
'--': 'm',
'-.': 'n',
'---': 'o',
'.--.': 'p',
'--.-': 'q',
'.-.': 'r',
'...': 's',
'-': 't',
'..-': 'u',
'...-': 'v',
'.--': 'w',
'-..-': 'x',
'-.--': 'y',
'--..': 'z',
'/': ' ',
'.----': '1',
'..---': '2',
'...--': '3',
'....-': '4',
'.....': '5',
'-....': '6',
'--...': '7',
'---..': '8',
'----.': '9',
'-----': '0',
'.-.-.-': '.',
'---...': ':',
'--..--': ',',
'-.-.-.': ';',
'..--..': '?',
'-...-': '=',
'.----.': '\'',
'-..-.': '/',
'-.-.--': '!',
'-....-': '-',
'..--.-': '_',
'.-..-.': '\"',
'-.--.': '(',
'-.--.-': ')',
'...-..-': '$',
'.-...': '&',
'.--.-.': '@',
'.-.-.': '+'
}

# find the input test file
for input_name in input_folder:
    #if("r00979hl" not in input_name.name):
    if(True):
        # initialize file input and output
        f = open(input_name)
        output_name = input_name.name.replace(".txt","_r00979hl.txt")
        g = open(str(args.fout)+"/"+output_name, "w")
        # read the file in
        strIn = f.read()

        #identify the cipher
        strIn_list = strIn.split(":")
        if("+3" in strIn_list[0]):
            # caesar
            for i in range(len(strIn_list[1])):
                if(ord(strIn_list[1][i]) >= 97 and ord(strIn_list[1][i]) <= 122):
                    for j in range(3,len(alpha)):
                        if(alpha[j] == strIn_list[1][i]):
                            g.write(alpha[j-3])
                            break
                else:
                    g.write(strIn_list[1][i])
        elif("ex" in strIn_list[0]):
            # hex
            strHex_list = strIn_list[1].split(" ")
            for hexNum in strHex_list:
                x = int(hexNum,16)
                if(x >= 65 and x <= 90):
                    x += 32
                g.write(chr(x))
        elif("orse" in strIn_list[0]):
            # morse
            strMor_list = strIn_list[1].split(" ")
            for morChr in strMor_list:
                if(morChr != '\n'):
                    g.write(morse[morChr])

        else:
            print("cipher type unidentifiable")

        # file closing
        f.close()
        g.close()
