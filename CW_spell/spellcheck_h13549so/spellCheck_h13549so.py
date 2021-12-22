import sys
import os

# opens englishWords txt file and reads
englishWords = open(sys.argv[1], "r")
english = englishWords.read()

# iterates over input directory and stores an array of the files 
files = os.listdir(sys.argv[2])
for i in range(len(files)-1):
    if files[i] == ".DS_Store":
        files.remove(".DS_Store")
    else:
        continue
print(files)

for file in files:

    # opens input txt file and reads
    with open(sys.argv[2]+"/"+file, "r") as readFrom:
        originalWhole = readFrom.read()
        whole = ""
        for line in originalWhole:
            whole += line

    # counts punctuation and removes
    punctuation = '''!()-[];:'"\{,<>.}/?_~'''
    new = ""
    punctuationCount = 0 
    for char in whole:
        if char not in punctuation:
            new += char
        else:
            punctuationCount += 1
            
    # counts and replaces uppercase words
    upper = 0
    capitalsDetected = []
    print("SPLIT: ", new.split())
    for index, i in enumerate(new.split()):
        for j in range(len(i)):
            if i[j].isupper() and [i,index] not in capitalsDetected:
                new = new.replace(i, i.lower())
                upper += 1
                capitalsDetected.append([i, index])
            else:
                continue
    print(capitalsDetected)

    # count and replace numbers
    numberCount = 0
    for i in new:
        if i.isnumeric():
            numberCount += 1
            new = new.replace(i, "")
        else:
            continue

    # count and replace numbers
    for i in new:
        if i.isnumeric():
            numberCount += 1
            new = new.replace(i, "")
        else:
            continue

    # checks for incorrect words
    incorrectWords = 0 
    for i in new.split():
        if i.lower().strip() not in english.split():
            incorrectWords += 1
        else:
            continue
        
    # calculate number of words
    numberOfWords = len(new.split())
    correctWords = numberOfWords - incorrectWords

    # write results to output file
    output = open(sys.argv[3]+"/"+file.removesuffix(".txt")+"_h13549so.txt", "w")
    output.write("h13549so\n")
    output.write("Formatting ###################\n")
    output.write("Number of uppercase words changed: "+str(upper)+"\n")
    output.write("Number of punctuations removed: "+str(punctuationCount)+"\n")
    output.write("Number of numbers removed: "+str(numberCount)+"\n")
    output.write("Spellchecking ###################\n")
    output.write("Number of words: "+str(numberOfWords)+"\n")
    output.write("Number of correct words: "+str(correctWords)+"\n")
    output.write("Number of inccorrect words: "+str(incorrectWords)+"\n")