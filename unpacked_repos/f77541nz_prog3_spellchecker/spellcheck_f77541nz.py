import os, argparse, re
from pathlib import Path

#takes folder input
parser = argparse.ArgumentParser()
parser.add_argument("english_words", type=Path)
parser.add_argument("file_path", type=Path)
parser.add_argument("destination_path", type=Path)
p = parser.parse_args()


EnglishWordsList = []
x = 0
english = ""
#sets english words up
with open(str(p.english_words), "r") as openedFile:

    for line in openedFile:
        line = line.strip()
        EnglishWordsList.append(line)
    openedFile.close()

#loops through folders files
for file in os.listdir(p.file_path):
      openedFile = open((str(p.file_path) + "/" + str(file)),"r")
      paragraph = openedFile.read()
      openedFile.close()

      UPtransformed = 0
      PuncGone = 0
      NumGone = 0
      BasicWordCount = 0
      CorrectWordCount = 0
      BadWordCount = 0
      word =""

      #checks uppercase
      for x in range (0,len(paragraph)):
          if paragraph[x].isupper() == True:
              UPtransformed += 1
      paragraph = paragraph.lower()

      newParagraph = ""
      for x in range (0,len(paragraph)):
          #checks for num
          if paragraph[x].isdigit() == True:
              NumGone += 1
          else:
              newParagraph = newParagraph + paragraph[x]

      #checks punctuation
      newerPara = ""
      punctuation = [".","?","!",",",":",";","-","–","[","]","{","}","(",")","'",'"',"..."]
      for x in range (0,len(newParagraph)):
          if newParagraph[x] in punctuation:
              PuncGone += 1
          else:
              newerPara = newerPara + newParagraph[x]
          #deals with ellipses
          if newParagraph[x] == "." and newParagraph[x-1] == "." and newParagraph[x-2] == ".":
              PuncGone = PuncGone - 2

      #finds end of word and valuates word
      for x in range (0,len(newerPara)):

          if (newerPara[x] == " "):
              word = word.strip()
              if word in EnglishWordsList:
                  CorrectWordCount += 1
                  BasicWordCount += 1
              elif word == "":
                  continue
              else:
                  BadWordCount += 1
                  BasicWordCount += 1
              word = ""

          #adds letter to word
          else:
              word += newerPara[x]
              if x == len(newerPara)-1:
                  if word in EnglishWordsList:
                      CorrectWordCount += 1
                      BasicWordCount += 1
                  else:
                      BadWordCount += 1
                      BasicWordCount += 1

      file = file.replace(".txt", "_f77541nz.txt", 1)
      openedFile = open((str(p.destination_path) + "/" + str(file)),"w")
      openedFile.write("f77541nz" + "\n")
      openedFile.write("Formatting ###################" + "\n")
      openedFile.write("Number of upper case letters changed: " + str(UPtransformed) + "\n")
      openedFile.write("Number of punctuations removed: " + str(PuncGone) + "\n")
      openedFile.write("Number of numbers removed: " + str(NumGone) + "\n")
      openedFile.write("Spellchecking ###################" + "\n")
      openedFile.write("Number of words: " + str(BasicWordCount) + "\n")
      openedFile.write("Number of correct words: " + str(CorrectWordCount) + "\n")
      openedFile.write("Number of incorrect words: " + str(BadWordCount) + "\n")
      openedFile.close()
