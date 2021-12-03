import argparse
import os
morsecode ={
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z",
    "/":" ",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    "-----":"0",
    ".-.-.-":".",
    "--..--":",",
    "---...":":",
    "..--..":"?",
    ".----.":"'",
    "-....-":"-",
    "-..-.":"/",
    ".--.-.":"@",
    "-...-":"=",
    "..--.-":"_",
    "-.--.":"(",
    "-.--.-":")",
    ".-..-.":'"',
    "-.-.-.":";"
    }
cae=list("abcdefghijklmnopqrstuvwxyz")
parser = argparse.ArgumentParser()
parser.add_argument('inp', type=str, help="path of input file")
parser.add_argument('outp', type=str, help="path of output file")
args = parser.parse_args()
if os.path.exists(args.inp):
    files_in=os.listdir(args.inp)
for file in files_in:
    input_file = open(args.inp+'/'+file)
    s=input_file.read()
    input_file.close()
    alg=s[0:s.index(':')]
    text=s[s.index(':')+1:]
    outs=""
    if alg=="Caesar Cipher(+3)":
        text=text.strip()
        for i in text:    
            if i == ' ':
                outs+=' '
                continue
            outs+=cae[(cae.index(i)+23)%26]
    if alg=="Morse Code":
        m=list(map(str,text.split(' ')))
        for i in m:
            outs+=morsecode[i]
    if alg=="Hex":
        h=list(map(str,text.split(' ')))
        for i in h:
            outs+=chr(int(i,16))
    output_file = open(args.outp+'/'+file[:-4]+"_j23676kd.txt", "w")
    output_file.write(outs.lower())
    output_file.close()

