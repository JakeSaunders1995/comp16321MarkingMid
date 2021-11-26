import argparse,os,re
punctuationlist = [".","?","!",",",":",";","‐","—","(",")","{","}","[","]","'",'"']
parser = argparse.ArgumentParser(description="checks for spelling mistakes")
parser.add_argument("dictionary", help="Input file path of dictionary")
parser.add_argument("input", help="Input file path")
parser.add_argument("save",help="Output file path")
folder = parser.parse_args()
dictionary = open(folder.dictionary,"r")
dictionarywords = dictionary.readlines()
for filename in os.listdir(folder.input): 
    if filename.endswith(".txt"):
        inputFile = open(folder.input + filename,"r")
        outputFile = open(folder.save + filename[0:-4] + "_m31181jg" + ".txt","w") 
        outputFile.write("m31181jg"+ "\n")
        outputFile.write("Formatting ###################"+ "\n")
        inputtext = inputFile.readline()
        words = inputtext.split()
        punctuation = 0
        capital = 0
        numbers = 0
        correct=0
        incorrect=0
        formattedwords= []
        skip = 0
        while words:
            word = words.pop()
            formattedword= ""
            for i in range(0,len(word)):
                if skip > 0:
                    skip -= 1
                else:
                    if ord(word[i]) >= 65 and ord(word[i]) <= 90:
                        capital += 1
                        formattedword = formattedword + word[i].lower()
                    elif ord(word[i]) >= 48 and ord(word[i]) <= 57:
                        numbers += 1
                    elif ord(word[i]) >= 97 and ord(word[i]) <= 122:
                        formattedword = formattedword + word[i]
                    elif word[i] in punctuationlist:
                        punctuation += 1
                        if word[i] != "'" and formattedword != "":
                            formattedwords.append(formattedword)
                            formattedword = ""
                        if i + 2 < len(word):
                            if word[i]== word[i+1] == word[i+2] == ".":
                                skip = 2
            if formattedword != "":
                formattedwords.append(formattedword)
        outputFile.write("Number of upper case words transformed: " + str(capital) + "\n")
        outputFile.write("Number of punctuation’s removed: " + str(punctuation)+ "\n")
        outputFile.write("Number of numbers removed: " + str(numbers)+ "\n")
        outputFile.write("Spellchecking ###################"+ "\n")
        outputFile.write("Number of words in file: " + str(len(formattedwords))+ "\n")
        for word in formattedwords:
            found = False
            for dictionaryword in dictionarywords:
                if word == dictionaryword[0:-1]:
                    found = True
                    correct+=1
                    break
            if found == False:
                incorrect += 1
        outputFile.write("Number of correct words in file: " + str(correct)+ "\n")
        outputFile.write("Number of incorrect words in file: " + str(incorrect))
        outputFile.close
        inputFile.close
dictionary.close
