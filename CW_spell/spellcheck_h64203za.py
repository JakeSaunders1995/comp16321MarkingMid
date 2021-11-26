import argparse, os, re

parser = argparse.ArgumentParser()
parser.add_argument('EnglishWords')
parser.add_argument('inputDir')
parser.add_argument('outputDir')

args = parser.parse_args()
english = args.EnglishWords
englishFile = os.path.join(english)
inputPath = args.inputDir
dirs = os.listdir(inputPath)
outputPath = args.outputDir
# print(dirs)
curDir = []
for k in range(len(dirs)):
    current = dirs[k]
    if current.endswith('.txt'):
        current = current[:-4]
        current = current + "_h64203za.txt"
        curDir.append(current)

for j in range(len(dirs)):
    readName = dirs[j]
    writeName = curDir[j]

    readFile = os.path.join(inputPath, readName)
    writeFile = os.path.join(outputPath, writeName)

    arr = []
    temp = []
    f = open(readFile,"r")
    line = f.readlines()
    for k in range(len(line)):
        line[k] = line[k].strip()
        temp.append(line[k].split(" "))
    for l in range(len(temp)):
        for m in range(len(temp[l])):
            arr.append(temp[l][m])
    f.close()
    # print(arr)

    upper = 0
    punctuation = 0
    numbers = 0
    puncList = ['!','(',')','-','[',']','{','}',';',':',"'",'"',"\ ",',','<','>','.','/','?','_','~']
    for i in range(len(arr)):
        word = arr[i]
        for j in range(len(word)):
            current = word[j]
            if ord(current) <91 and ord(current) > 64:
                upper += 1
            if ord(current) <58 and ord(current) > 47:
                numbers += 1
            for o in range(len(puncList)):
                if current in puncList[o]:
                    punctuation += 1
        arr[i] = word.lower()
        arr[i] = re.sub(r'[0-9]+', '', arr[i])
        arr[i] = re.sub(r'[^\w\s]', '', arr[i])
    formatting = []
    for n in arr:
        if (n != ""):
            formatting.append(n)

    # print("h64203za")
    # print("Formatting #################################")
    line1 = ("Number of upper case words transformed: " + str(upper))
    line2 = ("Number of punctuation removed: " + str(punctuation))
    line3 = ("Number of numbers removed: " + str(numbers))
    # print(formatting)

    c = open(englishFile,"r")
    cc = c.readlines()
    alphabet = []
    for item in range(len(cc)):
        cc[item] = cc[item].strip()
        alphabet.append(cc[item])
    totalWords = (len(formatting))
    correctWords = 0
    # print(alphabet)
    for v in range(len(formatting)):
        if formatting[v] in alphabet:
            correctWords += 1
    c.close()


    incorrectWords = totalWords - correctWords
    totalWords = str(totalWords)
    correctWords = str(correctWords)
    incorrect = str(incorrectWords)

    # print("Spellchecking #################################")
    line4 = ("Number of words: " + str(totalWords))
    line5 = ("Number of correct words: " +str(correctWords))
    line6 = ("Number of incorrect words: " + str(incorrectWords))
    s = open(writeFile,"w")
    s.write("h64203za\n")
    s.write("Formatting #################################\n")
    s.write(line1)
    s.write("\n")
    s.write(line2)
    s.write("\n")
    s.write(line3)
    s.write("\n")
    s.write("Spellchecking #################################\n")
    s.write(line4)
    s.write("\n")
    s.write(line5)
    s.write("\n")
    s.write(line6)
    s.close()
