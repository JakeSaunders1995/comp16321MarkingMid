import argparse
import os

parser= argparse.ArgumentParser()
parser.add_argument('iPath', type=str)
parser.add_argument('oPath', type=str)
args = parser.parse_args()


FileList=os.listdir(args.iPath)
FilenameList=[]
for item in FileList:
    if ".txt" in item:
        FilenameList.append(item)


for Filename in FilenameList:
    file = open(args.iPath+"/"+Filename,"r")
    Cyphertext=file.readlines()
    def CheckEmpty(item):
        if not item:
            return("Empty")
        else:return("Not Empty")
    if CheckEmpty(Cyphertext)=="Not Empty":
        print(Cyphertext)
        Cyphertext=Cyphertext[0]
        for i in range(0,len(Cyphertext)):
            if Cyphertext[i]==":":
                EncryptionTec   = Cyphertext[0:i]
                EncryptedText   = Cyphertext[i+1:]

        def decryptHex():
            global EncryptedText, Character
            EncryptedText=EncryptedText+" "
            EncryptedText=list(EncryptedText)
            GroupofNumbers=[]
            x=0
            while EncryptedText!=[]:
                l = EncryptedText[x]
                if l == " ":
                    z = "".join(EncryptedText[0:x])
                    GroupofNumbers.append(z)
                    del EncryptedText[0:x+1]
                    x=0
                if l != " ":
                    x+=1

            for i in range(0, len(GroupofNumbers)):
                GroupofNumbers[i]=chr(int(GroupofNumbers[i],16))
            Character="".join(GroupofNumbers)
            print(Character)
        if "Hex" in EncryptionTec:
            decryptHex()

        def decrpyptcasesar():
            global Character, EncryptedText
            OrigTXT =EncryptedText.lower()
            plaintxt=""
            TXTPo=0
            Alphabet="xyzabcdefghijklmnopqrstuvw"
            while TXTPo<len(OrigTXT):
                CurrentCar    = OrigTXT[TXTPo]
                if CurrentCar in Alphabet:
                    if CurrentCar!=" ":
                        Alphapos=0
                        while CurrentCar!=Alphabet[Alphapos]:
                            Alphapos+=1
                        CurrentCar=Alphabet[Alphapos-3]
                plaintxt+=CurrentCar
                Character = plaintxt
                TXTPo+=1
        if "aesar" in EncryptionTec:
            decrpyptcasesar()

        def decryptMorse():
            global EncryptedText, Word, Character
            Dict_Morse = {  '.-'  : "A" , '-...'  :"B",
                            '-.-.': "C" , '-..'   :"D", '.'     :"E",
                            '..-.': "F" , '--.'   :"G", '....'  :"H",
                            '..'  : "I" , '.---'  :"J", '-.-'   :"K",
                            '.-..': "L" , '--'    :"M", '-.'    :"N",
                            '---' : "O" , '.--.'  :"P", '--.-'  :"Q",
                            '.-.' : "R" , '...'   :"S", '-'     :"T",
                            '..-' : "U" , '...-'  :"V", '.--'   :"W",
                            '-..-': "X" , '-.--'  :"Y", '--..'  :"Z",
                            '.----':'1' , '..---' :'2', '...--' :'3',
                            '....-':'4' , '.....' :'5', '-....' :"6",
                            '--...':'7' , '---..' :'8', '----.' :'9',
                            '-----':'0' , '--..--':',', '.-.-.-':'.',
                            '..--..':'?', '-..-.' :'/', '-....-':'-',
                            '-.--.' :'(', '-.--.-':')', '-.-.-.':';',
                            '---...':':', '.----.':"'", '-.-.--':'!',
                            '.-..-.':'"'
                        }
            
            EncryptedText=EncryptedText+" / "

            Character = ""
            
            while EncryptedText!="":
                Word=EncryptedText[0:EncryptedText.index("/ ")]
                EncryptedText = EncryptedText[EncryptedText.index("/ ")+2:]
                while Word!="":
                    Letter= Dict_Morse[Word[0:Word.index(" ")]]
                    Character+= Letter
                    Word  = Word[Word.index(" ")+1:]
                Character+=" "
            Character=Character[0:-1]
        if "orse" in EncryptionTec:
            decryptMorse()
        Character = Character.lower()
        file = open(args.oPath+"/"+Filename[:-4]+"_s23522ym.txt","w")
        file.write(Character)