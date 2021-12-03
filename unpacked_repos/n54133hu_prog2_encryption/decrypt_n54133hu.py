import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('input', metavar='i', type=str)
parser.add_argument('output', metavar='o', type=str)
paths = parser.parse_args()
def decrypter(ciphertext):
    decrypted = []
    hex = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
    morse = {".-":"a","-...":"b", "-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j-","-.-":"k",".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w","-..-":"x","-.--":"y","--..":"z","-----":"1",".---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",".-.-.-":".","--..--":",","..--..":"?" }
    if ciphertext[0] == "Morse Code":
        back = 0
        front = 0
        ciphertext = ciphertext[1].split("/")
        for word in ciphertext:
            word = word.split(' ')
            for decrypt in word:
                if decrypt != ' ' and decrypt != '':
                    decrypted.append(morse[str(decrypt)])
            decrypted.append(" ")
        #while front < len(ciphertext[1]):
         #   if ciphertext[1][front] != '/' and front != len(ciphertext[1]) -1:
          #      front += 1
           # else:
            #    decryption = ciphertext[1][back:front]
             #   back = front
              #  front += 1
               # decryption = decryption.split(' ')
                #for character in decryption:
                 #   if(character != "/" and character != ''):
                  #      decrypted.append(morse[str(character)])
                #decrypted.append(" ")
    elif ciphertext[0] == "Hex":
        ciphertext = ciphertext[1].split(' ')
        for character in ciphertext:
            hexout = 0
            i = len(character) -1
            for hexchar in character:
                hexout += hex[hexchar] * (16**i)
                i -= 1
            decrypted.append(chr(hexout))
            hexout = 0
    elif ciphertext[0] == "Caesar Cipher(+3)":
        ciphertext = ciphertext[1].split(' ')
        print(ciphertext)
        for word in ciphertext:
            for character in word:
                if character != ('') and character != (' '):
                    print(character)
                    dec = ord(character)
                    if dec <= 122 and dec >= 97:
                        flag = False
                        for i in range(3):
                            dec -=1
                            if dec<97:
                                if not flag:
                                    dec = 122
                                    print("run")
                                    flag = True
                                else:
                                    flag = True
                        decrypted.append(chr(dec))
            decrypted.append(' ')
    
    return decrypted




files = os.scandir(paths.input)
for entry in files:
    path = ""
    if paths.input[-1] != "/":
        path = paths.input +"/"
    else:
        path = paths.input
    fileInput = open(path+"/"+entry.name)
    stringIn = fileInput.read()
    fileInput.close()
    path = ""
    if paths.input[-1] != "/":
        path = paths.output +"/"
    else:
        path = paths.output
    out = decrypter(stringIn.split(':'))
    outputText = ''.join(out).lower()
    print(outputText)
    fileOutput = open(path+"/"+entry.name.replace('.txt','')+"_n54133hu.txt",'w')
    fileOutput.write(outputText)
    fileOutput.close()