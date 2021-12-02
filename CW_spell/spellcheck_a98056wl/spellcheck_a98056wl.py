import sys, os, re

# read command line arguments
englishWordsFile = sys.argv[1]
inputDirectory = sys.argv[2]
outputDirectory = sys.argv[3]

# define variables
punctuation = [".", "?", "!", ",", ":", ";", "-", "–", "—", "(", ")", "{", "}", "[", "]", "'", "\"", "…"]

# read english words
englishWords = []
file = open(englishWordsFile)
for line in file:
    englishWords.append(line.rstrip())
file.close()

# analyse file
def GetOutput(data):
    # go through each character
    # remove punctuation, numbers, transform capital letters
    capitalCount = 0
    wrongWords = 0
    numsRemoved = 0
    puncRemoved = 0
    newData = ""
    for i in range(len(data)):
        if data[i].isupper():
            capitalCount += 1
        if data[i].isnumeric():
            numsRemoved += 1
            continue
        if data[i] in punctuation:
            puncRemoved += 1
            continue
        newData += data[i].lower()
    # use regular expression to remove multiple spaces left after
    # removing punctuation, also removing any spaces left at the end
    # with rstrip
    newData = re.sub("[ ]+", " ", newData).rstrip()
    words = newData.split(" ")
    for word in words:
        if not word in englishWords:
            wrongWords += 1
    output = "a98056wl\nFormatting ###################\n"
    output += f"Number of upper case letters changed: {capitalCount}\n"
    output += f"Number of punctuations removed: {puncRemoved}\n"
    output += f"Number of numbers removed: {numsRemoved}\n"
    output += "Spellchecking ###################\n"
    output += f"Number of words: {len(words)}\n"
    output += f"Number of correct words: {len(words) - wrongWords}\n"
    output += f"Number of incorrect words: {wrongWords}\n"
    return output
    
            

# read & write final scores to files
for root, dirs, files in os.walk(inputDirectory):
    for fileName in files:
        inputPath = inputDirectory + "/" + fileName
        outputPath = outputDirectory + "/" + fileName[:-4] + "_a98056wl.txt"

        data = []
        file = open(inputPath)
        data = file.read().replace("\n", " ").rstrip()
        file.close()
        outputText = GetOutput(list(data))

        file = open(outputPath, "w")
        file.write(outputText)
        file.close()
