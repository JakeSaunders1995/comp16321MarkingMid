import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("EnglishWordsPath", type=str)
parser.add_argument("input", type=str)
parser.add_argument("output", type=str)
args = parser.parse_args()

EnglishWordsPath = args.EnglishWordsPath
input = args.input
output = args.output

for file in os.listdir(input):
    f = open(input+"/"+file,"r")
    text = f.read()

    punctuation=[".","?","!",",",":",";","/","-","(",")","[","]","{","}","'",'"']
    words = text.split(" ")
    formatted_words=[]

    upper_words=0
    punctuation_rem=0
    numbers_rem=0
    ellipses=0
    for word in words:
        indiv=""
        if "..." in word:

            ellipses+=1
        for char in word:
            if char in punctuation:
                punctuation_rem+=1
                pass
            elif char.isdigit():
                numbers_rem+=1
                pass
            elif char.isupper():
                char=char.lower()
                upper_words+=1
                indiv+=char
            else:
                indiv+=char
        if indiv!="":
            formatted_words.append(indiv)
    punctuation_rem-=(ellipses*2)

    file_eng=open(EnglishWordsPath,"r") #midterm said to use the FILE path, not folder path so there you go
    EnglishWords=file_eng.read()
    Words_from_English=EnglishWords.split("\n")

    words_total=0
    correct=0
    incorrect=0
    for word in formatted_words:
        if word in Words_from_English:
            correct+=1
        else:
            incorrect+=1
        words_total+=1

    f.close()
    file=open(output+"/"+file[:-4]+"_t56563bk.txt","w")
    file.write("t56563bk")
    file.write("\nFormatting ###################")
    file.write("\nNumber of upper case words changed: "+str(upper_words))
    file.write("\nNumber of punctuations removed: "+str(punctuation_rem))
    file.write("\nNumber of numbers removed: "+str(numbers_rem))
    file.write("\nSpellchecking ###################")
    file.write("\nNumber of words: "+str(words_total))
    file.write("\nNumber of correct words: "+str(correct))
    file.write("\nNumber of incorrect words: "+str(incorrect))
