#get the command line part working

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input",type=str)
parser.add_argument("output",type=str)

args = parser.parse_args()



#read the input file and determine what cypher that is then decrypt the string

import os

#counts the number of files in input
directory = args.input
totalFiles = 0

inputcount = 0
dir = args.input
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        inputcount+=1
#print(inputcount)

#counts the number of files in output

totalFiles = 0

outputcount = 0
dir = args.output
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        outputcount+=1
#print(outputcount)


#---encryption---
for filename in os.scandir(directory):

    if filename.is_file():

        file = open(filename,"r")

        encryption = ""

        for line in file:
            #line=line.rstrip()
            encryption=line

       # print(encryption)
       # print('""')
        #print(encryption[18:])



        if encryption[0]=="M" or encryption[0]=="m":
            #print("its morse code")
            for i in range(len(encryption)):
                if encryption[i] == ":":
                    #print(i)
                    #print("now we can decrypt the cipher")

                    ciphertext = encryption[i+1:]
                    array = list(ciphertext)
                    #print(ciphertext)
                    #print(array)

                    morse = []
                    y=0
                    #print(ciphertext[-1])
                    for x in range(len(array) ):
                        if ciphertext[x] == ' ':

                            if ciphertext[x]==' ':
                                #print(ciphertext[y:x])
                                initial = ciphertext[y:x]
                                morse.append(initial)
                                y = x

                        #print(ciphertext[y:x])
                        elif ciphertext[x] != ' ':
                            continue
                        # elif ciphertext[-1] != ' ':
                        #     initial = ciphertext[-1]
                        #     morse.append(initial)
                    if ciphertext[-1] != ' ':
                        initial = ciphertext[-1]
                        morse.append(initial)


                   # print(morse)


                    #now we have to define morsecode for python to decrypt it and assign numbers etc

                    # a=".-" or " .-"
                    # b="-..."or " -..."
                    # c="-.-."or" -.-."
                    # d="-.."or" -.."
                    # e="."or" ."
                    # f="..-."or" ..-."
                    # g="--."or" --."
                    # h="...."or" ...."
                    # i=".."or" .."
                    # j=".---"or " .---"
                    # k="-.-"or " -.-"
                    # l=".-.."or" .-.."
                    # m="--"or " --"
                    # n="-."or " -."
                    # o="---"or " ---"
                    # p=".--."or " .--."
                    # q="--.-"or " --.-"
                    # r=".-."or " .-."
                    # s="..."or " ..."
                    # t="-"or" -"
                    # u="..-"or " ..-"
                    # v="...-"or " ...-"
                    # w=".--"or " .--"
                    # x="-..-"or " -..-"
                    # y="-.--"or " -.--"
                    # z="--.." or " --.."
                    #
                    plaintext = ''
                    ciphertextPostion = 0
                   # print(len(morse))
                    while (ciphertextPostion < len(morse)):

                        ciphertextChar = morse[ciphertextPostion]

                        #print(morse[ciphertextPostion])
                        if ciphertextChar == ".-" or ciphertextChar == " .-":
                            ciphertextChar = "a"
                            #plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            #print(plaintext)
                            continue
                        elif ciphertextChar == "-..."or ciphertextChar ==" -...":
                            ciphertextChar = "b"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.-."or ciphertextChar ==" -.-.":
                            ciphertextChar = "c"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.."or ciphertextChar ==" -..":
                            ciphertextChar = "d"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "."or ciphertextChar == " .":
                            ciphertextChar = "e"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "..-."or ciphertextChar == " ..-.":
                            ciphertextChar = "f"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--." or ciphertextChar ==" --.":
                            ciphertextChar = "g"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "...."or ciphertextChar ==" ....":
                            ciphertextChar = "h"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".."or ciphertextChar ==" ..":
                            ciphertextChar = "i"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".---"or ciphertextChar ==" .---":
                            ciphertextChar = "j"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.-"or ciphertextChar ==" -.-":
                            ciphertextChar = "k"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".-.."or ciphertextChar ==" .-..":
                            ciphertextChar = "l"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--"or ciphertextChar ==" --":
                            ciphertextChar = "m"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-."or ciphertextChar ==" -.":
                            ciphertextChar = "n"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "---"or ciphertextChar ==" ---":
                            ciphertextChar = "o"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".--."or ciphertextChar ==" .--.":
                            ciphertextChar = "p"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--.-"or ciphertextChar ==" --.-":
                            ciphertextChar = "q"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".-."or ciphertextChar ==" .-.":
                            ciphertextChar = "r"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "..."or ciphertextChar ==" ...":
                            ciphertextChar = "s"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-"or ciphertextChar ==" -":
                            ciphertextChar = "t"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "..-"or ciphertextChar == " ..-":
                            ciphertextChar = "u"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "...-"or ciphertextChar ==" ...-":
                            ciphertextChar = "v"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".--"or ciphertextChar ==" .--":
                            ciphertextChar = "w"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-..-"or ciphertextChar ==" -..-":
                            ciphertextChar = "x"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.--"or ciphertextChar ==" -.--":
                            ciphertextChar = "y"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--.." or ciphertextChar ==" --..":
                            ciphertextChar = "z"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "/" or ciphertextChar ==" /":
                            ciphertextChar = " "
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".-.-.-" or ciphertextChar ==" .-.-.-":
                            ciphertextChar = "."
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "..--.." or ciphertextChar ==" ..--..":
                            ciphertextChar = "?"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.-.--" or ciphertextChar ==" -.-.--":
                            ciphertextChar = "!"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--..--" or ciphertextChar ==" --..--":
                            ciphertextChar = ","
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "---..." or ciphertextChar ==" ---...":
                            ciphertextChar = ":"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.-.-." or ciphertextChar ==" -.-.-.":
                            ciphertextChar = ";"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-....-" or ciphertextChar ==" -....-":
                            ciphertextChar = "-"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.--." or ciphertextChar == " -.--.":
                            ciphertextChar = "("
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-.--.-" or ciphertextChar == " -.--.-":
                            ciphertextChar = ")"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        # elif ciphertextChar == "/" or ciphertextChar == " /":
                        #     ciphertextChar = "{"
                        #     # plaintext = plaintext + ciphertextChar
                        #     ciphertextPostion = ciphertextPostion + 1
                        #     ASCIIValue = ord(ciphertextChar)
                        #     plaintext = plaintext + chr(ASCIIValue)
                        #     continue
                        # elif ciphertextChar == "/" or ciphertextChar == " /":
                        #     ciphertextChar = "}"
                        #     # plaintext = plaintext + ciphertextChar
                        #     ciphertextPostion = ciphertextPostion + 1
                        #     ASCIIValue = ord(ciphertextChar)
                        #     plaintext = plaintext + chr(ASCIIValue)
                        #     continue
                        elif ciphertextChar == ".----." or ciphertextChar == " .----.":
                            ciphertextChar = "'"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".-..-." or ciphertextChar == " .-..-.":
                            ciphertextChar = '"'
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        # elif ciphertextChar == "/" or ciphertextChar == " /":
                        #     ciphertextChar = "..."
                        #     # plaintext = plaintext + ciphertextChar
                        #     ciphertextPostion = ciphertextPostion + 1
                        #     ASCIIValue = ord(ciphertextChar)
                        #     plaintext = plaintext + chr(ASCIIValue)
                        #     continue
                        elif ciphertextChar == "-----" or ciphertextChar == " -----":
                            ciphertextChar = "0"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == ".----" or ciphertextChar == " .----":
                            ciphertextChar = "1"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "..---" or ciphertextChar == " ..---":
                            ciphertextChar = "2"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "...--" or ciphertextChar == " ...--":
                            ciphertextChar = "3"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "....-" or ciphertextChar == " ....-":
                            ciphertextChar = "4"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "....." or ciphertextChar == " .....":
                            ciphertextChar = "5"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "-...." or ciphertextChar == " -....":
                            ciphertextChar = "6"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "--..." or ciphertextChar == " --...":
                            ciphertextChar = "7"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "---.." or ciphertextChar == " ---..":
                            ciphertextChar = "8"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        elif ciphertextChar == "----." or ciphertextChar == " ----.":
                            ciphertextChar = "9"
                            # plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            ASCIIValue = ord(ciphertextChar)
                            plaintext = plaintext + chr(ASCIIValue)
                            continue
                        else:
                          #  print("punctuation")
                            ciphertextChar="!"
                            ASCIIValue = ord(ciphertextChar)
                            # print(ASCIIValue)
                            ASCIIValue = ASCIIValue
                            # print(ASCIIValue)

                            plaintext = plaintext + chr(ASCIIValue)
                            ciphertextPostion = ciphertextPostion + 1
                            # print(plaintext)

                  #  print(plaintext.lower())








        elif encryption[0]=="C" or encryption[0]=="c":
            #print("its Caesar cipher")
            for i in range(len(encryption)):
                if encryption[i] == ":":
                    #print(i)
                    #print("now we can decrypt the cipher")

                    ciphertext = encryption[i+1:]
                    #plaintext =
                    plaintext = ""

                    ciphertextPostion = 0
                    while (ciphertextPostion < len(ciphertext)):

                        ciphertextChar = ciphertext[ciphertextPostion]
                        if ciphertextChar == ' ':
                            plaintext = plaintext +ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            continue
                        elif ord(ciphertextChar) < 34:
                            ciphertextPostion = ciphertextPostion + 1

                            continue
                        elif (ciphertextChar) == '@' or (ciphertextChar) == '#'or (ciphertextChar) == '0'or (ciphertextChar) == '1' or (ciphertextChar) == '2'or (ciphertextChar) == '3'or (ciphertextChar) == '4'or (ciphertextChar) == '5'or (ciphertextChar) == '6'or (ciphertextChar) == '7'or (ciphertextChar) == '8'or (ciphertextChar) == '9':
                            plaintext = plaintext + ciphertextChar

                            ciphertextPostion = ciphertextPostion + 1

                            continue
                        else:

                            ASCIIValue = ord(ciphertextChar)
                            #print(ASCIIValue)
                            ASCIIValue = ASCIIValue - 3
                            #spaces =0
                            #print(ASCIIValue)
                            if ASCIIValue < 97 and ASCIIValue >91:
                                spaces = 97 -ASCIIValue
                                #print(spaces)
                                if spaces == 2:
                                    ASCIIValue = 122
                                    ASCIIValue = ASCIIValue - 1
                                elif spaces == 1:
                                    ASCIIValue = 122
                                    ASCIIValue = ASCIIValue - 0

                                elif spaces== 3:
                                    ASCIIValue = 122
                                    ASCIIValue = ASCIIValue - 2


                            plaintext = plaintext + chr(ASCIIValue)
                            ciphertextPostion = ciphertextPostion + 1
                            #print(plaintext)


                 #   print(plaintext.lower())
                    #test whther you need loer fucntion to ignore caps
                    #rember to add this to the output file, plaintext










        elif encryption[0]=="H" or encryption[0]=="h":
            #print("its Hexdecimal")
            for i in range(len(encryption)):
                if encryption[i] == ":":
                    ciphertext = encryption[i + 1:]
                    array = list(ciphertext)
                   # print(ciphertext)
                    #print(array)
                    z = []
                    for x in range(len(array)-1):
                        if array[x+1] != ' 'and array[x] != ' ':
                            p=int(array[x],16)
                            q=int(array[x+1],16)


                            y= (p)*(16**1)+ (q*(16**0))
                            #y= array[x]+array[x+1]
                            z.append(y)


                        elif array[x+1] == ' ':
                            continue
                        elif array[x] == ' ':
                            continue
                    #print(z)
                    #print(z[0])

                    plaintext = ""

                    ciphertextPostion = 0
                    while (ciphertextPostion < len(z)):

                        ciphertextChar = z[ciphertextPostion]
                        if ciphertextChar == '32':
                            plaintext = plaintext + ciphertextChar
                            ciphertextPostion = ciphertextPostion + 1
                            continue
                        else:
                            #change this part
                            #ASCIIValue = ord(ciphertextChar)
                            # print(ASCIIValue)
                            ASCIIValue = ciphertextChar
                            # print(ASCIIValue)

                            plaintext = plaintext + chr(ASCIIValue)
                            ciphertextPostion = ciphertextPostion + 1
                            #print(plaintext)

                    #rint(plaintext)
                   # print(plaintext.lower())
                    # rember to add this to the output file, plaintext




        #ceasercipher+3 would be -3 to decrypt it
        #hexdecimal
        #use spaces as  conyinue for for loop
        #morsecode



        #we should output the decrypted message to the outfile file:output like we did on rugby

        #outputFile = open(args.output,"w")
       # outputFile.write(plaintext.lower())

        dict = args.output
        obj = os.scandir(dict)
        f = filename.name.split(".")
        if outputcount < inputcount:
           # print("b")
            for u in range(inputcount):
                username = '_p50792sd'
                outputfilename = ""
                #outputfilename = outputfilename + (filename.name[0:10])
                #print(filename.name[0:10])
                f= filename.name.split(".")
                #print(f[0])
                outputfilename = outputfilename + f[0]
                outputfilename = outputfilename + username
                arguments = outputfilename + ".txt"
                arguments = args.output + '/' + arguments
               # print(arguments)
                file = open(arguments, "x")
                break
        #e = entry.name.split(".")
        obj = os.scandir(dict)
        for entry in obj:
            e = entry.name.split("_")
            #print(e[0])
            #print(f[0])
            #print(e[1])
            #print(e[0]+"_"+e[1])
            file_output = e[0]+"_"+e[1]
            #print(e[2])
            if f[0] == file_output:
            #if filename.name[0:10] == entry.name[0:10]:
               # print(filename.name[0:10])
               # print(entry.name[0:10])
                #print("it works")
                #print("a")

                outputFile = (open(entry, "w+"))
                outputFile.write(plaintext.lower())
            else:
                continue