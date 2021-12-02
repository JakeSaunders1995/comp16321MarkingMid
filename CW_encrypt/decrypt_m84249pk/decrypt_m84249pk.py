import sys
import os

input_folder=sys.argv[1]
output_folder=sys.argv[2]
count=0
hex=False
caes=False
Morse=False
decrypted=""
for file in os.scandir(input_folder):
    file1=open(file,"r")
    count+=1
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_m84249pk.txt"
    file2=open(output_folder+"/"+string,"w")

    cipher=str(file1.read())
    def encryption_type(cipher):
        if cipher[0:4]=="Hex:":

            return 1
        if cipher[0:4]=="Caes":
            return 2
        if cipher[0:4]=="Mors":
            return 3
    x=encryption_type(cipher)
    if x==1:
        hex=True
    if x==2:
        caes=True
    if x==3:
        Morse=True
    encrypted=""
    for i in range(len(cipher)):
        if cipher[i]==":":
            encrypted=cipher[i+1:len(cipher)]


    def hexa_decrypt(encrypted):
        return (bytes.fromhex(encrypted).decode("utf-8"))
    def caesar_decrypt(encrypted):
        string=""
        for i in range(len(encrypted)):
            if encrypted[i].isalpha():
                ascii=ord(encrypted[i])
                if ascii<100:
                    ascii=ascii-97+1
                    temp=122+ascii-3
                    string+=chr(temp)
                else:
                    temp=ascii-3
                    string+=chr(temp)
            else:
                string+=encrypted[i]

        return string
    def Morse_decrypt(encrypted):
        words=encrypted.split(" ")
        codes={
        '.-':'a',
        '-...':'b',
        '-.-.':'c',
        '-..':'d',
        '.':'e',
        '..-.':'f',
        '--.':'g',
        '....':'h',
        '..':'i',
        '.---':'j',
        '-.-':'k',
        '.-..':'l',
        '--':'m',
        '-.':'n',
        '---':'o',
        '.--.':'p',
        '--.-':'q',
        '.-.':'r',
        '...':'s',
        '-':'t',
        '..-':'u',
        '...-':'v',
        '.--':'w',
        '-..-':'x',
        '-.--':'y',
        '--..':'z',
        '.----':'1',
        '..---':'2',
        '...--':'3',
        '....-':'4',
        '.....':'5',
        '-....':'6',
        '--...':'7',
        '---..':'8',
        '----.':'9',
        '-----':'0',
        '--..--':',',
        '.-.-.-':'.',
        '..--..':'?',
        '-..-.':'/',
        '-....-':'-',
        '-.--.':'(',
        '-.--.-':')',
        '/':' ',
        '.--.-.':'@'
        }
        string=""
        for word in words:
            string+=codes[word]
        return string



    if hex:
        decrypted=hexa_decrypt(encrypted)
    if caes:
        decrypted=caesar_decrypt(encrypted)
    if Morse:
        decrypted=Morse_decrypt(encrypted)
    file2.write(decrypted)
    caes=False
    hex=False
    Morse=False
    decrypted=""
