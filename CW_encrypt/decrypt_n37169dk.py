import os, sys
a=sys.argv[1]
b=os.listdir(a)
for c in b:
    d=a+"/"+c
    with open(d, 'r') as decrypt:
        decrypt=decrypt.read()
        combination=""
        word=[]
        out=""
        hex=[]
        if "Hex:" in decrypt:
            x=4
            y=0
            while x<len(decrypt):
                if decrypt[x] == " ":
                    combination=hex[0]+hex[1]
                    i=int(combination,16)
                    word.append(chr(i))
                    hex=[]
                    x+=1
                elif x==len(decrypt)-1:
                    hex.append(decrypt[x])
                    x+=1
                    combination=hex[0]+hex[1]
                    i=int(combination,16)
                    word.append(chr(i))
                    hex=[]
                else:
                    hex.append(decrypt[x])
                    x+=1
            while y<len(word):
                out=out+word[y]
                y+=1
        elif "Caesar Cipher(+3):" in decrypt:
            cipherText=""
            plaintextPosition=18
            while plaintextPosition < len(decrypt):
                plaintextChar=decrypt[plaintextPosition]
                if plaintextChar == " ":
                    out+=" "
                    plaintextPosition+=1
                else:
                    ASCIIValue= ord(plaintextChar)
                    ASCIIValue=ASCIIValue-3
                    if ASCIIValue == 96:
                        ASCIIValue=122
                    elif ASCIIValue == 95:
                        ASCIIValue=121
                    elif ASCIIValue==94:
                        ASCIIValue =120
                    if ASCIIValue in range(97,123):
                        out=out+chr(ASCIIValue)
                        plaintextPosition+=1
                    else:
                        plaintextPosition+=1
                        ASCIIValue+=3
                        out=out+chr(ASCIIValue)
        elif "Morse Code:" in decrypt:
            x=11
            while x<len(decrypt):
                if decrypt[x] == "/":
                    out+=" "
                    x+=1
                elif decrypt[x] == ".":
                    combination+=decrypt[x]
                    x+=1
                elif decrypt[x] == "-":
                    combination+=decrypt[x]
                    x+=1
                elif decrypt[x] == " ":
                    if combination == ".-":
                        out+="a"
                        x+=1
                    elif combination == "-...":
                        out+="b"
                        x+=1
                    elif combination == "-.-.":
                        out+="c"
                        x+=1
                    elif combination == "-..":
                        out+="d"
                        x+=1
                    elif combination == ".":
                        out+="e"
                        x+=1
                    elif combination == "..-.":
                        out+="f"
                        x+=1
                    elif combination == "--.":
                        out+="g"
                        x+=1
                    elif combination == "....":
                        out+="h"
                        x+=1
                    elif combination == "..":
                        out+="i"
                        x+=1
                    elif combination == ".---":
                        out+="j"
                        x+=1
                    elif combination == "-.-":
                        out+="k"
                        x+=1
                    elif combination == ".-..":
                        out+="l"
                        x+=1
                    elif combination == "--":
                        out+="m"
                        x+=1
                    elif combination == "-.":
                        out+="n"
                        x+=1
                    elif combination == "---":
                        out+="o"
                        x+=1
                    elif combination == ".--.":
                        out+="p"
                        x+=1
                    elif combination == "--.-":
                        out+="q"
                        x+=1
                    elif combination == ".-.":
                        out+="r"
                        x+=1
                    elif combination == "...":
                        out+="s"
                        x+=1
                    elif combination == "-":
                        out+="t"
                        x+=1
                    elif combination == "..-":
                        out+="u"
                        x+=1
                    elif combination == "...-":
                        out+="v"
                        x+=1
                    elif combination == ".--":
                        out+="w"
                        x+=1
                    elif combination == "-..-":
                        out+="x"
                        x+=1
                    elif combination == "-.--":
                        out+="y"
                        x+=1
                    elif combination == "--..":
                        out+="z"
                        x+=1
                    elif combination == "-----":
                        out+="0"
                        x+=1
                    elif combination == ".----":
                        out+="1"
                        x+=1
                    elif combination == "..---":
                        out+="2"
                        x+=1
                    elif combination == "...--":
                        out+="3"
                        x+=1
                    elif combination == "....-":
                        out+="4"
                        x+=1
                    elif combination == ".....":
                        out+="5"
                        x+=1
                    elif combination == "-....":
                        out+="6"
                        x+=1
                    elif combination == "--...":
                        out+="7"
                        x+=1
                    elif combination == "---..":
                        out+="8"
                        x+=1
                    elif combination == "----.":
                        out+="9"
                        x+=1
                    elif combination == "........":
                        out+="Error"
                        x+=1
                    elif combination == ".-...":
                        out+="&"
                        x+=1
                    elif combination == ".----.":
                        out+="'"
                        x+=1
                    elif combination == ".--.-.":
                        out+="@"
                        x+=1
                    elif combination == "-.--.-":
                        out+=")"
                        x+=1
                    elif combination == "-.--.":
                        out+="("
                        x+=1
                    elif combination == "---...":
                        out+=":"
                        x+=1
                    elif combination == "--..--":
                        out+=","
                        x+=1
                    elif combination == "-...-":
                        out+="="
                        x+=1
                    elif combination == "-.-.--":
                        out+="!"
                        x+=1
                    elif combination == ".-.-.-":
                        out+="."
                        x+=1
                    elif combination == "-....-":
                        out+="-"
                        x+=1
                    elif combination == "------..-.-----":
                        out+="%"
                        x+=1
                    elif combination == ".-.-.":
                        out+="+"
                        x+=1
                    elif combination == ".-..-.":
                        out+='"'
                        x+=1
                    elif combination == "..--..":
                        out+="?"
                        x+=1
                    elif combination == "-..-.":
                        out+="/"
                        x+=1
                    else:
                        x+=1
                    combination=""
                else:
                    x+=1
            if combination == ".-":
                out+="a"
                x+=1
            elif combination == "-...":
                out+="b"
                x+=1
            elif combination == "-.-.":
                out+="c"
                x+=1
            elif combination == "-..":
                out+="d"
                x+=1
            elif combination == ".":
                out+="e"
                x+=1
            elif combination == "..-.":
                out+="f"
                x+=1
            elif combination == "--.":
                out+="g"
                x+=1
            elif combination == "....":
                out+="h"
                x+=1
            elif combination == "..":
                out+="i"
                x+=1
            elif combination == ".---":
                out+="j"
                x+=1
            elif combination == "-.-":
                out+="k"
                x+=1
            elif combination == ".-..":
                out+="l"
                x+=1
            elif combination == "--":
                out+="m"
                x+=1
            elif combination == "-.":
                out+="n"
                x+=1
            elif combination == "---":
                out+="o"
                x+=1
            elif combination == ".--.":
                out+="p"
                x+=1
            elif combination == "--.-":
                out+="q"
                x+=1
            elif combination == ".-.":
                out+="r"
                x+=1
            elif combination == "...":
                out+="s"
                x+=1
            elif combination == "-":
                out+="t"
                x+=1
            elif combination == "..-":
                out+="u"
                x+=1
            elif combination == "...-":
                out+="v"
                x+=1
            elif combination == ".--":
                out+="w"
                x+=1
            elif combination == "-..-":
                out+="x"
                x+=1
            elif combination == "-.--":
                out+="y"
                x+=1
            elif combination == "--..":
                out+="z"
                x+=1
            elif combination == "-----":
                out+="0"
                x+=1
            elif combination == ".----":
                out+="1"
                x+=1
            elif combination == "..---":
                out+="2"
                x+=1
            elif combination == "...--":
                out+="3"
                x+=1
            elif combination == "....-":
                out+="4"
                x+=1
            elif combination == ".....":
                out+="5"
                x+=1
            elif combination == "-....":
                out+="6"
                x+=1
            elif combination == "--...":
                out+="7"
                x+=1
            elif combination == "---..":
                out+="8"
                x+=1
            elif combination == "----.":
                out+="9"
                x+=1
            elif combination == "........":
                out+="Error"
                x+=1
            elif combination == ".-...":
                out+="&"
                x+=1
            elif combination == ".----.":
                out+="'"
                x+=1
            elif combination == ".--.-.":
                out+="@"
                x+=1
            elif combination == "-.--.-":
                out+=")"
                x+=1
            elif combination == "-.--.":
                out+="("
                x+=1
            elif combination == "---...":
                out+=":"
                x+=1
            elif combination == "--..--":
                out+=","
                x+=1
            elif combination == "-...-":
                out+="="
                x+=1
            elif combination == "-.-.--":
                out+="!"
                x+=1
            elif combination == ".-.-.-":
                out+="."
                x+=1
            elif combination == "-....-":
                out+="-"
                x+=1
            elif combination == "------..-.-----":
                out+="%"
                x+=1
            elif combination == ".-.-.":
                out+="+"
                x+=1
            elif combination == ".-..-.":
                out+='"'
                x+=1
            elif combination == "..--..":
                out+="?"
                x+=1
            elif combination == "-..-.":
                out+="/"
                x+=1
            else:
                x+=1
        else:
            print("input not recognised")
            out="input not recognised"
    e=c.replace('.txt','')
    w=sys.argv[2]+"/"+e+"_n37169dk"+".txt"
    x=open(w, 'w')
    x.write(out)
