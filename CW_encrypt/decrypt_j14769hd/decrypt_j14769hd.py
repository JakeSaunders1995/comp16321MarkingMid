import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file path here")
parser.add_argument("output", help="Output file path here")
args = parser.parse_args()
morseDict = { '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g','....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k','--' : 'm', '.-..' : 'l',
              '-.' : 'n', '---' : 'o',  '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u','.--.' : 'p', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y',
              '--..' : 'z','..--..' : '?', '.-.-.-' : '.',  '--..--' : ',',".----.":"'",".-..-.":'"',".-...":"&","-.-.--":"!","-.--.":"(","-.--.-":")","---...":":","-.-.-.":";","..--.-":"_",".--.-.":"@",
              "-....-":"-", '/' : ' '}
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        f = open(os.path.join(args.input, file),"r")
        data = f.read()
        f.close()
        temp=""
        data = data.split(":")
        if data[0] == "Hex":
            temp = bytes.fromhex(data[1].replace(" ","")).decode("ASCII")
            temp = temp.lower()
        elif data[0] == "Caesar Cipher(+3)":
            temp = ""
            for i in data[1]:
                tem = ord(i)-3
                if tem < 97:
                    tem += 26
                if i == " ":
                    temp += " "
                else:
                    temp += chr(tem)
            #temp = "".join([ i if i == " " else chr(ord(i)-3) for i in data[1]])
            temp = temp.lower()
        elif data[0] == "Morse Code":
            temp = ""
            for i in data[1].split(" "):
                temp += morseDict[i]
            temp = temp.lower()
            
        name = file.split(".")[0]
        name = name + "_j14769hd.txt"
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        f = open(os.path.join(args.output,name),"w+")
        f.write(temp)
        f.close()
