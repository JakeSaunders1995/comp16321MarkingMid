import sys
import os
engFile = sys.argv[1]
infolder = sys.argv[2]
outfolder = sys.argv[3]

for filename in os.listdir(infolder):

    infile = open(infolder + "/" + filename, "r")

    upper = 0
    numbers = 0
    punc = 0
    currentword = ""
    ellipse = 0

    for line in infile:
        line = line.strip()

        for char in line:
            if char == " " or char.islower():
                currentword += char
            elif char.isnumeric():
                numbers += 1
            elif char.isupper():
                currentword += char.lower()
                upper += 1
            else:
                punc += 1

        ellipse += line.count("...")
    punc -= (ellipse * 2)

    infile.close()
    words = currentword.split()
    engWords = open(engFile, "r")

    correct = 0
    for lines in engWords:
        lines = lines.strip()
        if lines in words:
            correct += words.count(lines)

    engWords.close()

    outfilename = outfolder + "/" + filename[:-4] + "_h32647nh.txt"
    outfile = open(outfilename, "w")
    outfile.write("h32647nh \n")
    outfile.write("Formatting ###################\n")
    outfile.write("Number of upper case letters changed: " + str(upper) + "\n")
    outfile.write("Number of punctuations removed: " + str(punc) + "\n")
    outfile.write("Number of numbers removed: " + str(numbers) + "\n")
    outfile.write("Spellchecking ###################\n")
    outfile.write("Number of words: " + str(len(words)) + "\n")
    outfile.write("Number of correct words: " + str(correct) + "\n")
    outfile.write("Number of incorrect words: " + str(len(words)-correct))
    outfile.close()
