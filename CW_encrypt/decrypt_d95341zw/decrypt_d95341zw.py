import os,argparse,re

parser = argparse.ArgumentParser()
parser.add_argument("dir", nargs="+")
#parser.add_argument("--Decrypt")
args = parser.parse_args()
"""
2. Read in a .txt file containing a single cipher-text (the encrypted string) in the form of:
"""
a = os.listdir(args.dir[0])
for i in range(0, len(a)):
    b=args.dir[0]+"/"+a[i]
    c=args.dir[1]+"/"+a[i]
    d=c.replace(".txt", "_d95341zw.txt")
    file = open(b, "r")
    encrypt=file.read()
#print(encrypt)
    list1=list(encrypt.split(":"))


#morseCode
    morseCode={
    '.-':'a', '-...':'b','-.-.':'c', '-..':'d', '.':'e','..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j', '-.-':'k','.-..':'l', '--':'m', '-.':'n','---':'o', '.--.':'p', '--.-':'q','.-.':'r', '...':'s',
    '-':'t',
    '..-':'u', '...-':'v', '.--':'w','-..-':'x', '-.--':'y', '--..':'z','.----':'1', '..---':'2', '...--':'3','....-':'4', '.....':'5', '-....':'6','--...':'7', '---..':'8', '----.':'9',
    '-----':'0', '--..-- ':', ', '.-.-.-':'.','..--..':'?', '-..-.':'/', '-....-':'-','-.--.':'(', '-.--.-':')','/': " ",
    }
    if list1[0]=="Morse Code":
        list1.pop(0)
        encrypt2="".join(list1)
        encrypt2 = encrypt2 +" "
        #print(encrypt2)
        results = []
        code = ""
        result1=""

        for item in encrypt2:
            if item == " ":
                result1 += morseCode[code]
                code = ""

            else:
                code = code + item
                #results.append(morseCode.get(item))
        file3 = open(d, "w")
        file3.write(result1)
        #print(results)


#Caesar Cipher(+3)
    elif list1[0]=="Caesar Cipher(+3)":
        list1.pop(0)
        encrypt3 = "".join(list1)
        #print(encrypt3)
        plaintextPosition=0
        cipher2 = ""
        cipher3=""
        while (plaintextPosition < len(encrypt3)):
            plaintextChar = encrypt3[plaintextPosition]
            ASCIIvalue = ord(plaintextChar)
            ASCIIvalue = ASCIIvalue - 3
            CharValue = chr(ASCIIvalue)
            cipher = cipher2 + CharValue
            plaintextPosition += 1
            cipher=cipher.replace("", " ")
            cipher=cipher.replace("`", "z")
            cipher = cipher.replace("_", "y")
            cipher = cipher.replace("^", "x")
            cipher = cipher.replace("", "")   
            cipher3+=cipher
            #print(cipher)
            
        file3 = open(d, "w")
        file3.write(cipher3)
        #sfile3.close()






#Hex
    elif list1[0]=="Hex":
        list1.pop(0)
        encrypt4 = "".join(list1)
        bytes=bytes.fromhex(encrypt4)
        result3=bytes.decode("ASCII")
        result3 = result3.lower()
        #print(result3)

        file3=open(d, "w")
        file3.write(result3)
