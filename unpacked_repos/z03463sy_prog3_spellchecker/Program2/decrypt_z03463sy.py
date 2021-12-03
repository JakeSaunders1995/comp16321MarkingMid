
#/home/csimage/Program2/input files
import os,binascii

def Caesar(cipher):
    
    # ciphertext = cipher[18:]
    # plainText = ""
    # alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
    # ciphertextPosition = 0
    # while (ciphertextPosition < len(ciphertext)):

    #     ciphertextChar = ciphertext[ciphertextPosition]
    #     alphabetPosition =3
    #     while (ciphertextChar != alphabet[alphabetPosition] and alphabetPosition< len(alphabet)-1 ):
    #         alphabetPosition+=1

    #     alphabetPosition-=3
    #     plainText += alphabet[alphabetPosition]
    #     ciphertextPosition +=1

    



    ciphertext = cipher[18:-1]
    plainText = ""
    ciphertextPosition = 0
    while (ciphertextPosition < len(ciphertext)):

        ciphertextChar = ciphertext[ciphertextPosition]
        ASCIIValue = ord(ciphertextChar)
        if ASCIIValue==32:
            plainText += chr(ASCIIValue)
            ciphertextPosition +=1
        elif ASCIIValue==97:
            plainText+=chr(120)
            ciphertextPosition+=1
        elif ASCIIValue==98:
            plainText+=chr(121)
            ciphertextPosition+=1
        elif ASCIIValue==99:
            plainText+=chr(122)
            ciphertextPosition+=1

        else:
            ASCIIValue -=3
            plainText += chr(ASCIIValue)
            ciphertextPosition +=1
        
    return plainText
    
def morse(string, sign):
    MorseList = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
        "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
        "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "..--..": "?", "-.-.--": "!", "--..--": ",", "-....-": "-",
        "-.--.": "(", "-.--.-": ")","---...": ":", "-.-.-.": ";",".----.": "'", ".-..-.": '"',
        "-..-.": "/", "/":" "
    }
    string = string[11:]
    lists = string.split(sign)
    list=[]
    for code in lists:
        list.append(MorseList.get(code))        
    return ''.join(list)
def hex(string, sign):
    # 分割，字符串string，分割标识符sign
    string =string[4:]
    lists = string.split(sign)
    list=[]
    for code in lists:
        list.append(bytes.decode(binascii.a2b_hex(code)))
    return ''.join(list)
    
    



#f.close()

print("please input input files dir  \n")
dataDir = input()
print("please input output files dir \n")
dirPath = input()
for root, dirs, files in os.walk(dataDir):
    for file in files:
        if os.path.splitext(file)[1] == '.txt':
            f=open(root+"/"+file,'r')
            cipher=f.read()             
            if (cipher[0:2]) =='Ca':
                a=Caesar(cipher)
            elif (cipher[0:2]) == 'Mo':
                a=morse(cipher," ")               
            elif (cipher[0:2]) == "He":
                a=hex(cipher," ")
            
            if not os.path.exists(dirPath):
                os.makedirs(dirPath)
            with open(dirPath+"/"+file,"w") as f:
                test = f.write(str(a))