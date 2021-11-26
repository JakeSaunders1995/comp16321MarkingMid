import argparse
import os

morse_code_dict = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z"}
parser = argparse.ArgumentParser()
parser.add_argument("input_path",help="Path to input file")
parser.add_argument("output_path",help="Path to output file")
args = parser.parse_args()

def main(input_file):

    algorithm,ciphertext = open(args.input_path+"/"+input_file,"r").read().rstrip().split(":")
    plaintext = ""
    if algorithm == "Hex":
        hexes = ciphertext.split(" ")
        plaintext = "".join(chr(int(x,16)) for x in hexes)
    elif algorithm == "Morse Code":
        words = ciphertext.split(" / ")
        for x in words:
            plaintext += "".join(morse_code_dict[y] for y in x.split(" "))+" "
    else:
        key = int(algorithm[-3:-1])*-1
        for x in range(len(ciphertext)):
            if ciphertext[x] == " ":
                plaintext+=" "
                continue
            if ord(ciphertext[x]) < 97 or ord(ciphertext[x]) > 122:
                plaintext += ciphertext[x]
                continue
            new = (ord(ciphertext[x]) + key)
            if new < 97:
                new += 26
            elif new > 122:
                new -= 26
            plaintext += chr(new)

    print(plaintext)

    try: # write to file
        open(args.output_path+"/"+input_file[:-4]+"_w25464il.txt","x").write(plaintext)
    except:
        open(args.output_path+"/"+input_file[:-4]+"_w25464il.txt","w").write(plaintext)

for filename in os.listdir(args.input_path):
    main(filename)
