import sys, os
inputfoldername = sys.argv[1]
files = os.listdir(inputfoldername)
print(files)
for filename in files:
    file = open("./"+inputfoldername+"/"+filename,"r")
    inp = file.read()
    file.close()
    print(filename)
    enctype = ""
    enctext = ""
    x=False
    for item in inp:
        if item == ":":
            x=True
        elif x==True:
            enctext = enctext+item
        else:
            enctype = enctype+item

    if enctype == "Hex":
        enctext= enctext.split(' ')
    elif enctype == "Caesar Cipher(+3)":
        enctext= list(enctext)
    elif enctype == "Morse Code":
        enctext = enctext.split(' ')
    else:
        print("???")

    print(enctext)
    print(enctype)

    dectext=""
    if enctype == "Hex":
        for item in enctext:
            dec = int(item, 16)
            dectext = dectext+chr(dec)
    elif enctype == "Caesar Cipher(+3)":
        alph = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for item in enctext:
            if item in alph:
                c = 3
                while c< len(alph):
                    if item == alph[c]:
                        break
                    else:
                        c=c+1
                dectext = dectext + alph[c-3]
            else:
                dectext = dectext + item
    elif enctype == "Morse Code":
        dict = {
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
            ".--l":"p",
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
            "-----":"0",
            ".----":"1",
            "..---":"2",
            "...--":"3",
            "....-":"4",
            ".....":"5",
            "-....":"6",
            "--...":"7",
            "---..":"8",
            "----.":"9",
            ".-.-.-":".",
            "--..--":",",
            "..--..":"?",
            "-.-.--":"!",
            "---...":":",
            "-.-.-.":";",
            "[m dash not found]":"—",#em dash
            "[n dash not found]":"–",#en dash
            "-....-":"-",#hyphen
            "-.--.":"(",
            "-.--.-":")",
            "[{ not found]":"{",
            "[}not found]":"}",
            "[[not found]":"[",
            "[]not found]":"]",
            ".----.":"\'",#apostrophe
            ".-..-.":"\"",#quotation mark
            "\n":"\n"
        }
        for item in enctext:
            dectext = dectext+dict[item]
    else:
        print("???")
    dectext = dectext.lower()
    outputfoldername = sys.argv[2]

    file = open("./"+outputfoldername+"/"+filename[0:len(filename)-4]+'_n62189sd.txt',"w")
    file.write(dectext)
    file.close()
