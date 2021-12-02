import os
import sys
filenames = os.listdir(sys.argv[2])
for filename in filenames:
    file = open(sys.argv[2]+"/"+filename, "rb")
    text = file.read().decode('ISO-8859-1')
    file.close()
    fileE = open(sys.argv[1], "r")
    Ctext = text.split()
    CNtext = " "
    NPNtext = " "
    Ntext = ""
    Numbers = "0123456789"
    count = 0
    for cap in text:
        if cap.isupper():
            count = count + 1
    for num in text:
        if num in Numbers:
            CNtext = CNtext + num
    for i in range(len(text)):
        if i in list(range(0,10)):
            text = text.replace(str(i), "")
    punc = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    for word in text:
        if word not in punc:
            Ntext = Ntext + word
        else:
            NPNtext = NPNtext + word
    counter = len(NPNtext) - 1
    for word in Ctext:
        if "..." in word:
            counter = counter - 2
    Ntext = Ntext.lower()
    Ntext = Ntext.split(" ")
    Wwords = ""
    Rwords = ""
    fileE = fileE.read()
    for d in Ntext:
        if d in fileE:
            Rwords = Rwords + " " + d
        else:
            Wwords = Wwords + " " + d
    #fileE = fileE.close()
    s0 = "u75904yl"
    s1 = "Formatting ###################"
    s2 = "Number of upper case words transformed: " + str(count)
    s3 = "Number of punctuation's removed: " + str(counter)
    s4 = "Number of numbers removed: " + str(len(CNtext.strip()))
    s5 = "Spellchecking ###################"
    s6 = "Number of words in file: " + str(len(Ctext))
    s7 = "Number of correct words in  file: " + str(len(Rwords.split()))
    s8 = "Number of incorrect words in file: " + str(len(Wwords.split()))
    file = open(sys.argv[3]+"/"+filename[:-4]+"_u75904yl.txt", "w")
    file.write(str(s0) + "\n" + str(s1) + "\n" + str(s2) + "\n" + str(s3) + "\n" + str(s4) + "\n" + str(s5) + "\n" + str(s6) + "\n" + str(s7) + "\n" + str(s8))
    file.close()