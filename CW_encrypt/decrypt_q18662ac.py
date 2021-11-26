import argparse
import os

parse = argparse.ArgumentParser()
parse.add_argument("input_folder",help = "The folder which contains the inputs")
parse.add_argument("output_folder",help = "The folder which will contains the Output")
args  = parse.parse_args()

def decryption(f):
    data = f.read()
    for i in range (len(data)):
        if data[i] == ":":
            pos = i
      
    if data[0] == "H":
        p = f.seek(pos+1)
        data = f.read()
        bytearray = bytes.fromhex(data)
        ascii_str = bytearray.decode()  
        ascii_str = ascii_str.lower()
        return ascii_str

    elif data[0] == "C":
        p = f.seek(pos+1)
        data = f.read()
        cipher = data.lower()
        string = ""
        for i in range (len(data)):
            if cipher[i].isalpha():
                newdata = ord(cipher[i])
                if newdata < 100:
                    newdata = newdata+26
                newdata = newdata-3
                string += chr(newdata)
            else:
                string += data[i]
        return string

    else: 
        p = f.seek(pos+1)
        data = f.read()
        words = data.split()
        mc_translation = {'.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g','....' : 'h',  '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0', '-..-.':'/', '-....-':'-', '-.--.':'(', '-.--.-':')', '.--.-.':'@'}
        string=""
        for i in words:
            string += mc_translation[i]
        return string

for file in os.scandir(args.input_folder):
    file1=open(file,"r")
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_q18662ac.txt"
    file2=open(args.output_folder+"/"+string,"w")
    file2.write(decryption(file1))
    file1.close()
    file2.close()