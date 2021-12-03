import argparse
import os
import re


morse_code = { 'a':'.-', 'b':'-...','c':'-.-.', 'd':'-..', 'e':'.','f':'..-.', 'g':'--.', 'h':'....','i':'..', 'j':'.---', 'k':'-.-','l':'.-..', 'm':'--', 'n':'-.','o':'---', 'p':'.--.', 'q':'--.-','r':'.-.', 's':'...', 't':'-','u':'..-', 'v':'...-', 'w':'.--','x':'-..-', 'y':'-.--', 'z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-', ' ':'/'}




parser = argparse.ArgumentParser()
parser.add_argument('input_file', type=str, help = 'Enter input file path')
parser.add_argument('output_file', type=str, help = 'Enter input file path')
args = parser.parse_args()

input_file=args.input_file
output_file=args.output_file

files = os.listdir(input_file)

for z in files:
    in_put=open(os.path.join(input_file,z)).read()
    arr = in_put.split(":")
    algo=arr[0]
    data=arr[1]
    decrypt = ''

    for y in data.split():   

        if algo == "Morse Code":
       
            for x in in_put.split():
                for key in morse_code:
                    if morse_code[key] == x:
                        decrypt += key

        elif algo == "Caesar Cipher(+3)":
        
                       
            alphabet="abcdefghijklmnopqrstuvwxyzabc"  


            for i in range(len(data)):
                #data[i] = data[i].lower()
                for m in range(len(data[i])):
                    text = ""
                    if data[i][m].isalpha():
                        aposition = len(alphabet) - 1
                        while True:
                            if data[i][m] == alphabet[aposition]:
                                text = alphabet[aposition-3]
                                break
                            aposition -= 1
                    else:
                        text = data[i][m]
                    decrypt += text
                decrypt += " "                                                                                                  
           

        elif algo == "Hex":
            data_split = data.split()
            for letter in data_split:
                final = bytes.fromhex(letter)


                ascii = final.decode("ASCII")
                decrypt += ascii



    n_file=re.split("[.]",z)[0] + "_f66089ms.txt"
    result=open(os.path.join(output_file,n_file),"w")
    result.write(decrypt)

    result.close()




