import os
import sys
Dictionary = sys.argv[1]
Input = sys.argv[2]
Output = sys.argv[3]
input_file = os.listdir(Input)
for p in input_file:
    file = open(Input + "/" + p,'r')
    text = file.readline()
    text2 = ""


        
    wordsremoved = 0
    capitalsremoved = 0
    punctuationremoved = 0
    numbersremoved = 0
    numbers = [1,2,3,4,5,6,7,8,9]
    alphabet = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    count = 0

    for x in range(0 ,(len(text))):

        if text[x] not in numbers: 
            if text[x] in alphabet :
                if str.isupper(text[x]) == False :
                    text2 += (text[x]).lower()
                else: 
                    capitalsremoved += 1
                    text2 += (text[x]).lower()
            else: 
                punctuationremoved += 1
        else:
            numbersremoved += 1




    print("Formatting ###################")
    print("Number of upper case words transformed: " + str(capitalsremoved))
    print("Number of punctuation's removed: " + str(punctuationremoved))
    print("Number of numbers removed: " + str(numbersremoved))


    file = open(Dictionary)
    dictionary = file.readlines()
    text3 = ""
    match = False
    words = 0
    for y in range(0 ,(len(text2))):
        
        if text2[y] != " ":
            count += 1
        elif text2[y] == " ":
            match = False
            count = 0
            words+= 1
            text4 = str(text3 + "\n")
            text3 = ""
            for line in dictionary:
                if text4 == line:
                    match = True
            if match != True:
                wordsremoved += 1
        if count > 0:
            text3 += text2[y]
    text4 = str(text3 + "\n")
    words+= 1
    for line in dictionary:
        if text4 == line:
            match = True
    if match != True:
        wordsremoved += 1

    print("Spellchecking ###################")
    print("Number of words in file: " + str(words))
    print("Number of correct words in file: " + str(words - wordsremoved))
    print("Number of incorrect words in file: " + str(wordsremoved))

    filew = open(Output + "/" + p.replace(".txt" , "") + "d30839jl",'w') 
    filew.write("d30839jl" + '\n')
    filew.write("Formatting ###################")
    filew.write('\n' + "Number of upper case words transformed: " + str(capitalsremoved))
    filew.write('\n' "Number of punctuation's removed: " + str(punctuationremoved))
    filew.write('\n' + "Number of numbers removed: " + str(numbersremoved))
    filew.write('\n' + "Spellchecking ###################")
    filew.write('\n' + "Number of words in file: " + str(words))
    filew.write('\n' + "Number of correct words in file: " + str(words - wordsremoved))
    filew.write('\n' + "Number of incorrect words in file: " + str(wordsremoved))
