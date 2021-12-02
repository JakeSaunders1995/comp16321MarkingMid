import argparse,os,re
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('print')
args = parser.parse_args()
startfile=os.listdir(args.file)
printfile=os.listdir(args.print)
t=0
while t<len(startfile):
    openfile= args.file+"/"+startfile[t]
    text=open(openfile,"r")
    word=""
    while True :
        x=text.read(1)
        if not x :
            break
        word+=x
    text.close()
    i=0
    p=""
    z=""
    plaintext=word
    cipherText=str()
    cipher = ""
    m=len(word)
    MORSE_CODE = {'..-.': 'F', '-..-': 'X',
                     '.--.': 'P', '-': 'T', '..---': '2',
                     '....-': '4', '-----': '0', '--...': '7',
                     '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                     '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                     '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                     '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                     '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                     '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1',"/":" "}
    k=1
    while i<m :
        if word[0]=="m" or word[0]=="M":
            p="m"
            break
        elif word[0]=="c" or word[0]=="C"  :
            p="c"
            while word[k]!= ":":
    #skip all the letters including ":"
                k+=1
        elif word[0]=="h" or word[0]=="H" :
            p="h"
            break
        i+=1
    plainttextposition=k+1
    while k<m :
        if p=="c" :
            while plainttextposition < len(plaintext) :
                    plaintextchar=plaintext[plainttextposition]
                    ASCIIValue=ord(plaintextchar)
                    if chr(ASCIIValue)== " " :
                        cipherText+=" "
                    else :
                        ASCIIValue=ASCIIValue-3
                        cipherText=cipherText+chr(ASCIIValue)
                    plainttextposition+=1
        k+=1
    if p=="m" :
        morse_word=str()
        code=word.split(":")
        list=code[1].split(" ")
        for w in list :
            encry_word= MORSE_CODE.get(w)
            morse_word+=str(encry_word)
        z=morse_word.lower()
    elif p=="c" :
        z=cipherText.lower()
    elif p=="h" :
        hex_word=str()
        n_char=int((len(word)-3)/3)
        for w in range (n_char):
            hex_char=word[4+3*w : 6+w*3]
            ascii_char=int(hex_char,16)
            char = chr(ascii_char)
            hex_word+=char
        z=hex_word.lower()
    renamefile=startfile[t]
    renamed=renamefile[0:len(renamefile)-4]+"_m92824cm.txt"
    outputfile=open(renamed,"w")
    outputfile.write(str(z))
    outputfile.close()
    t+=1
