import sys
import contextlib
walk_dir=sys.argv[1]
dest_dir=sys.argv[2]
with open (walk_dir, "r") as f:
        data =(f.read()).lower()
        txt=data.split(" ")
# text=(txt[0].split(":"))[1]
# text2=txt[1:]
# text2.insert(0,text)

# string=" ".join(text2)
# print(string)
# word=""
# sentence=""
# position=0

    
if txt[0]=="hex":
    text=(txt[0].split(":"))[1]
    text2=txt[1:]
    text2.insert(0,text)

    string=" ".join(text2)
    print(string)
    word=""
    sentence=""
    position=0

    word= bytes.fromhex(string)
    word= word.decode("ascii").lower()
    trans=(f"Hex:{word}")
    with open(dest_dir,"w") as o:
         with contextlib.redirect_stdout(o):
            print(trans)





if txt[0]=="caesar": 
    text=(txt[1].split(":"))[1]
    text2=txt[2:]
    text2.insert(0,text)
    string=" ".join(text2)

    sentence=""
    position=0
    
    while position<len(string) :

        char=string[position]
        if char== " ":
            continue
        else:
            ASCIIValue=ord(char)
            ASCIIValue=ASCIIValue-3
            charValue=chr(ASCIIValue)
            sentence += charValue
        position +=1
        trans=(f"Caesar Cipher(+3):{sentence}")
    print(trans)






if txt[0]=="morse": 
    text=(txt[1].split(":"))[1]
    text2=txt[2:]
    text2.insert(0,text)
    string=" ".join(text2)
    string.replace(" / ","  ")

    stringlist=string.split(" ")
    position=0  
    result=""   
    prkataan= 0
    while prkataan < len(stringlist):
        perqataan=stringlist[prkataan]
        hurufs=perqataan.split(" ")
        nombor=0
        while nombor<len(hurufs):
            huruf=hurufs[nombor]
            morse= {'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..',
    'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
    'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.',
     'Q':'--.-','R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
     'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---',
     '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
     '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', 
    '-':'-....-', '(':'-.--.', ')':'-.--.-'}

            inverse=dict((v,k) for (k,v) in morse.items())
            sebenar=inverse.get(huruf)

            print(sebenar)
            
            nombor +=1
            
        prkataan +=1
     
    