import sys
import os

punctuations = '''.?!,:;-—'()[]{}"'''
numbers = '''0123456789'''

englishwords_path = sys.argv[1]
input_name = sys.argv[2]
output_name = sys.argv[3]

wordsdictionary = []
englishwords_file = open(englishwords_path, "r")
for line in englishwords_file:
    englishwords = line.strip()
    wordsdictionary.append(englishwords)

for testfile in os.listdir(input_name):
    f = os.path.join(input_name, testfile)
    print("File:", testfile)
    input_file = open(f, 'r')
    text = input_file.read()
    text_array = []
    count = len(text)

    print(text)

    text_nopunc = ""
    text_formatted = ""
    puncount = 0
    numcount = 0
    elipsis_count = 0


    for character in text:
        if character not in punctuations:
            text_nopunc += character
            puncount += 1
    for c in text_nopunc:
        if c not in numbers:
            text_formatted += c
            numcount += 1

    if "..." in text:
        print("has elispsis")
        puncount += 2

    text_formatted = text_formatted.lower()


    puncount = len(text) - puncount
    numcount = len(text_nopunc) - numcount

    print("punctuation:",puncount)
    print("numbers:",numcount)

    words = text_formatted.strip().split()
    wordsnum = len(words)
    print("words:",len(words))

    capitals = sum(1 for x in text if x.isupper())
    print("capitals:",capitals)

    print(text_formatted)

    misspellwords = []
    for w in words:
        if w not in wordsdictionary:
            misspellwords.append(w)
    incorrectwordsnum = len(misspellwords)
    correctwordsnum = wordsnum - incorrectwordsnum

    print("incorrect words:",incorrectwordsnum)
    print("correct words:",correctwordsnum)
    print("\n")

    output_file_name = testfile[:-4] + "_d71343si.txt"
    output_file_path = os.path.join(output_name, output_file_name)

    output_file = open(output_file_path, "w")
    output_file.write("d71343si\nFormatting ###################\n")
    output_file.write("Number of upper case letters changed: "+str(capitals)+"\n")
    output_file.write("Number of punctuations removed: "+str(puncount)+"\n")
    output_file.write("Number of numbers removed: "+str(numcount)+"\n")
    output_file.write("Spellchecking ###################"+"\n")
    output_file.write("Number of words: "+str(wordsnum)+"\n")
    output_file.write("Number of correct words: "+str(correctwordsnum)+"\n")
    output_file.write("Number of incorrect words: "+str(incorrectwordsnum))



    input_file.close()
    englishwords_file.close()
    output_file.close()