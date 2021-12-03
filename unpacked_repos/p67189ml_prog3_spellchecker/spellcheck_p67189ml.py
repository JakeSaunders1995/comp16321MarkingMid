import argparse
import re
import os


parser = argparse.ArgumentParser()
parser.add_argument("wordListFilePath")
parser.add_argument("inputDirectory")
parser.add_argument("outputDirectory")

args = parser.parse_args()

for filename in os.listdir(args.inputDirectory):
  filePath = os.path.join(args.inputDirectory,filename)
  if os.path.isfile(filePath):
    
    f = open(filePath, "r")
    string = f.read()
    f.close()

    f = open(args.wordListFilePath, "r")
    englishWords = f.read().split("\n")
    f.close()

    ellipsisRegex1 = r"\. \. \."
    ellipsisRegex2 = r"\.\.\."
    puncRegex = r"[\.\?\!\,\:\;\–\—\―\‒\-\(\)\[\]\{\}\'\‘\’\“\”\"]"
    upperRegex = r"[A-Z]"
    numbersRegex = r"[0-9]"

    words = re.split(r"[ \n]", string)

    ellipsisCount = len(re.findall(ellipsisRegex1, string)) + len(re.findall(ellipsisRegex2, string))
    puncCount =  len(re.findall(puncRegex, string)) - ellipsisCount*2
    upperCount = len(re.findall(upperRegex, string))
    numbersCount = len(re.findall(numbersRegex, string))

    wordCount = 0
    correctWords = 0
    incorrectWords = 0

    for word in words:
      #convert to lower case
      modified_string = word.lower()

      #remove all numbers
      modified_string = re.sub(numbersRegex, "", modified_string)

      #ignore everything after the first punctuation mark remove all punctuation
      modified_string = re.split(puncRegex, modified_string)[0]

      #remove spaces
      modified_string = re.sub(" ", "", modified_string)
      
      if modified_string != "":

        wordCount += 1
        if modified_string in englishWords:
          correctWords += 1
        else:
          incorrectWords += 1

    output = """p67189ml
Formatting ###################
Number of upper case words changed: {}
Number of punctuations removed: {}
Number of numbers removed: {}
Spellchecking ###################
Number of words: {}
Number of correct words: {}
Number of incorrect words: {}
""".format(upperCount, puncCount, numbersCount ,wordCount, correctWords, incorrectWords)

    f = open(args.outputDirectory + "/" + filename[:-4] + "_p67189ml.txt", "w")
    f.write(output)
    f.close()

