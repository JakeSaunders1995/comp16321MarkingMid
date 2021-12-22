import sys
import os
path=sys.argv[1]
outputpath=sys.argv[2]
path_list = os.listdir(path)
path_list.sort()
num = 0
T=""
for filename in path_list:
    num = num + 1
    f = open(os.path.join(path,filename))
    input=f.read()
    strlist=input.split(':')
    if strlist[0]=="Caesar Cipher(+3)":
        plaintext=strlist[1]
        ciphertext=""
        plaintextposition=0
        while(plaintextposition<len(plaintext)):
            plaintextChar=plaintext[plaintextposition]
            if plaintextChar == ' ':
                ciphertext += ' '
                plaintextposition += 1
                continue
            ASCIIValue=ord(plaintextChar)
            if 96 < ASCIIValue < 100:
                ASCIIValue+=26
            ASCIIValue-=3
            ciphertext+=chr(ASCIIValue)
            plaintextposition+=1
        T=ciphertext
    elif strlist[0]=="Hex":
        m = strlist[1]
        i = 0
        answer = ""
        while i < len(m):
            decimal = int(m[i] + m[i + 1], 16)
            if 64<decimal<91:
                decimal+=32
            acsiivcode = chr(decimal)
            answer += acsiivcode
            i+=3
        T=answer
    elif strlist[0]=="Morse Code":
        T=""
        cipertext = strlist[1]
        m = cipertext.split(" ")
        morselist = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd',
                     '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
                     '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
                     '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
                     '--.-': 'q', '.-.': 'r', '...': 's', '-': 't',
                     '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
                     '-.--': 'y', '--..': 'z', '/': ' '
                     }
        for i in m:
            T+=morselist[i]
    output_filename = 'test_file_j29403qy' + str(num) + '.txt'
    f1=open(os.path.join(outputpath,output_filename),'w')
    f1.write(T)
    f1.close()    

