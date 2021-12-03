import sys
import os

englishworddir = sys.argv[1]
inputfolder = sys.argv[2]
outputfolder = sys.argv[3]

numberlist = "0123456789"
punctuation = "''" + ".?!,:;-()_[]}{"
alphatbet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercounter = 0
pcounter = 0
numcounter = 0
counter = 0
wordcounter = 0
dictwordslist = []
sentencelist = []
correctwords = 0
incorrectwords = 0

startdirectory = os.getcwd() + inputfolder.replace('.', '')
engwordstxtfile = os.getcwd() + englishworddir.replace('.', '', 1)


dictionairy = open(engwordstxtfile, 'r')
for line1 in dictionairy:
  linestrip = line1.strip()
  dictwordslist.append(linestrip)
dictionairy.close()



os.chdir(startdirectory)

for inputfile in os.listdir():
   sentencelist.clear()
   pcounter = 0
   counter = 1
   numcounter = 0
   uppercounter = 0
   incorrectwords = 0
   correctwords = 0
   file = open(inputfile, 'r')
   line = file.read().rstrip()


   for i in line:
      if i in punctuation:
          line = line.replace(i, "")
          pcounter += 1
      if i in numberlist:
          line = line.replace(i, "")
          numcounter += 1
      if i in alphatbet:
          line = line.replace(i, i.lower())
          uppercounter += 1


   linewords = line.split()
   wordcounter = len(linewords)

   sentencelist = line.split(" ")
   for words in sentencelist:
    if words in dictwordslist:
      correctwords += 1



   print("OUTPUTTED TO OUTPUT FOLDER")
   incorrectwords = wordcounter - correctwords


   os.chdir('..')
   if not os.path.exists(os.getcwd()  + outputfolder.replace('.', '')):
         os.makedirs(os.getcwd()  + outputfolder.replace('.', ''))
         os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

         f = open(inputfile + "_p80249ra.txt", 'w+')
         f.write("%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n" %(" p80249ra", "Formatting ###################", "Number of upper case words transformed: "+ str(uppercounter), "Number of punctuation’s removed: " + str(pcounter), "Number of numbers removed: "+  str(numcounter), "Spellchecking ###################", "Number of words: " + str(wordcounter), "Number of correct words: "+ str(correctwords), "Number of incorrect words: "+ str(incorrectwords) ))
         f.close()
         os.chdir('..')
         os.chdir(startdirectory)

         file.close()
   else:
     os.chdir(os.getcwd()  + outputfolder.replace('.', ''))

     f = open(inputfile + "_p80249ra.txt", 'w+')
     f.write("%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n" %(" p80249ra", "Formatting ###################", "Number of upper case words transformed: "+ str(uppercounter), "Number of punctuation’s removed: " + str(pcounter), "Number of numbers removed: "+  str(numcounter), "Spellchecking ###################", "Number of words: " + str(wordcounter), "Number of correct words: "+ str(correctwords), "Number of incorrect words: "+ str(incorrectwords) ))
     f.close()
     os.chdir('..')
     os.chdir(startdirectory)

     file.close()


