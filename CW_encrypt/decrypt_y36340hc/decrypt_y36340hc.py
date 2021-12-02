import sys
import os
# load input
inpath = rf"{sys.argv[1]}"
outpath = rf"{sys.argv[2]}"
for file in os.listdir(inpath):
    if ".txt" in file:
        f = open(rf"{str(inpath)}/{file}","r")
        ciphertext = f.read()
        text = ""
        # decryption for hexadecimal
        if ciphertext[0:3] == "Hex":
            ciphertext = ciphertext[4:]
            position = 0
            while position < len(ciphertext):
                text += chr(int(ciphertext[position:position+2],16))
                position += 3
        # decryption for caesar cipher(+3)
        elif ciphertext[0:17] == "Caesar Cipher(+3)":
            alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
            ciphertext = ciphertext[18:]
            position = 0
            while position < len(ciphertext):
                plain = ciphertext[position]
                alphabetposition = 3
                if plain not in alphabet:
                    text += plain
                    position += 1
                else:
                    while plain != alphabet[alphabetposition]:
                        alphabetposition += 1
                    alphabetposition -= 3
                    text += alphabet[alphabetposition]
                    position += 1
        # decryption for morse code
        elif ciphertext[0:10] == "Morse Code":
            ciphertext = ciphertext[11:]
            morse = [(" ","/"),("@",".--.-."),("$","...-..-"),("-","-....-"),("+",".-.-."),("=","-...-"),("_","..--.-"),("/","-..-."),(";","-.-.-."),(":","---..."),("&",".-..."),(")","-.--.-"),("(","-.--."),('"',".-..-."),("'",".----."),("!","-.-.--"),("?","..--.."),(",","--..--"),(".",".-.-.-"),("1",".----"),("2","..---"),("3","...--"),("4","....-"),("5","....."),("6","-...."),("7","--..."),("8","---.."),("9","----."),("0","-----"), ("a",".-"), ("b","-..."), ("c","-.-."), ("d","-.."), ("e","."), ("f","..-."), ("g","--."), ("h","...."), ("i",".."), ("j",".---"), ("k","-.-"), ("l",".-.."), ("m","--"), ("n","-."), ("o","---"), ("p",".--."), ("q","--.-"), ("r",".-."), ("s","..."), ("t","-"), ("u","..-"), ("v","...-"), ("w",".--"), ("x","-..-"), ("y","-.--"), ("z","--..")]
            position = 0
            for i in range(len(ciphertext)):
                if ciphertext[i] == " ":
                    for j in range(len(morse)):
                        if ciphertext[position:i] == morse[j][1]:
                            text += morse[j][0]
                            position = i+1
                elif i == len(ciphertext)-1:
                    for j in range(len(morse)):
                        if ciphertext[position:i+1] == morse[j][1]:
                            text += morse[j][0]
        text = text.lower()
        g = open(rf"{str(outpath)}/{file[:-4]}_y36340hc.txt","w")
        g.write(text)
