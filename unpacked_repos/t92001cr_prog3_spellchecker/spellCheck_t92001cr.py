import argparse, os
parser = argparse.ArgumentParser()
parser.add_argument("argEng", help="English Words file path")
parser.add_argument("a1", help="input file path")
parser.add_argument("a2", help="output file path")
args = parser.parse_args()
files = []
for file in os.listdir(args.a1):
        if file.endswith(".txt"):
                files.append(file)
files.remove("EnglishWords.txt")
for z in range (len(files)):
        f = open(files[z], "r")
        line = f.readline()
        f.close()
        punc = [".","?","!",",",":",";","-","(",")","{","}","[","]","'",'"',"..."]
        digits = ["1","2","3","4","5","6","7","8","9","0"]
        numOfDigits = 0
        numOfPunc = 0
        numOfUpper = 0
        numOfWords = 0
        correctWords = 0
        incorrectWords = 0
        lineList = list(line)
        for x in range(0,len(lineList)-2):
                if line[x] == "." and line[x+1] == "." and line[x+2] == ".":
                        lineList[x] = ""
                        lineList[x+1] = ""
                        lineList[x+2] = ""
                        numOfPunc += 1

        for let in lineList:
                if let in digits:
                        let = ""
                        numOfDigits += 1

        for let in lineList:
                if let in punc:
                        let = ""
                        numOfPunc += 1 

        for let in lineList:
                if let.isupper():
                        numOfUpper += 1

        line = "".join(lineList)
        line = line.lower()

        listOfWords = line.split(" ")
        listOfWords = list(filter(lambda x: x != "",listOfWords))

        f = open(args.argEng)
        englishWords = f.read()
        f.close()
        for words in listOfWords:
                numOfWords += 1
                if words in englishWords:
                        correctWords += 1
                else:
                        incorrectWords += 1

        noExt = files[z][:-4]

        f = open(str(args.a2) + "/" + noExt + "_t92001cr.txt" , "w")
        f.write("t92001cr\n")
        f.write("Formatting ###################\n")
        f.write("Number of upper case words changed: " + str(numOfUpper) + "\n")
        f.write("Number of punctuations removed: " + str(numOfPunc) + "\n")
        f.write("Number of numbers removed: " + str(numOfDigits) + "\n")
        f.write("Spellchecking ###################\n")
        f.write("Number of words: " + str(numOfWords) + "\n")
        f.write("Number of correct words: " + str(correctWords) + "\n")
        f.write("Number of incorrect words: " + str(incorrectWords))
        f.close()