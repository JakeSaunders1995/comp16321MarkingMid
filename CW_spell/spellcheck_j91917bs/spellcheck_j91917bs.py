import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument("wordsFile", type=str, help="needs words file")
parser.add_argument('inputfile', type=str, help="need input file")
parser.add_argument('outputfile', type=str, help="need output file")
args = parser.parse_args()


wordsFile = args.wordsFile
inputFile = args.inputfile
# why have outputFile= when reassign at end?
outputFile = args.outputfile



for x in os.listdir(inputFile):
  file = os.path.join(inputFile, x)
  dpath = os.path.dirname(file)

  englishWords = open(wordsFile, "r")
  words = englishWords.read()
  file1 = open(file, "r")
  line = file1.read()

  if outputFile[-1] != "/":
    outputName = outputFile + "/" + x.split(".txt")[0] + "_j91917bs.txt"
    outFile = outputName
    dir = os.path.dirname(outFile)
    print(dir)
  else:
    outputName = outputFile + x.split(".txt")[0] + "_j91917bs.txt"
    outFile = outputName
    dir = os.path.dirname(outputFile)

  if not os.path.exists(dir):
    os.makedirs(dir)

  nums = ["0","1","2","3","4","5","6","7","8","9"]
  punct = [".","?","!",",",":",";","-","—","[","]","{","}","(",")","'","\"","…"]


  # removedUppers = ""
  removedNums = ""
  # removedPunct = ""
  # removedNumsAndPunct = ""

  uppersRemoved = 0
  numsRemoved = 0
  punctsRemoved = 0
  incorrectWords = 0
  correctWords = 0

  for i in line:
      if i != i.lower():
          uppersRemoved += 1

  for i in line:
      if i not in nums:
          removedNums += i
      else:
          numsRemoved += 1


  for i in removedNums:
      if i in punct:
          punctsRemoved += 1


  clearedWords = re.sub("[^\w\s]","",removedNums.lower())


  wordsSplit = clearedWords.split()
  englishWordsSplit = words.split()


  for x in range(len(wordsSplit)):
      if wordsSplit[x] in englishWordsSplit:
          correctWords += 1
      else:
          incorrectWords += 1


  numWordsFile = len(wordsSplit)

  print(uppersRemoved, punctsRemoved, numsRemoved, numWordsFile, correctWords, incorrectWords)

  file2 = open(outFile, "w")
  finalWrite = ("j91917bs \n"  + "Formatting ################### \n"  + "Number of upper case letters changed: " + str(uppersRemoved) + "\n" + "Number of punctuations removed: " + str(punctsRemoved) + "\n" + "Number of numbers removed: " + str(numsRemoved) + "\n"+ "Spellchecking ################### \n"+ "Number of words: "+ str(numWordsFile)+ "\n"+ "Number of correct words: "+ str(correctWords)+ "\n"+ "Number of incorrect words: "+ str(incorrectWords))

  file2.write(finalWrite)
