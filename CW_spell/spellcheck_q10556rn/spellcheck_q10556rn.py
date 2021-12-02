import sys
import os

englishwords = sys.argv[1]
input_direct = sys.argv[2]
output_direct= sys.argv[3]

alphabet = "abcdefghijklmnopqrstuvwxyz"
numlist = "0123456789"
punctlist = ".?!,:;-()—[]}{'"+'"' 

with open(englishwords,'r') as i:
   linesindic = i.readlines()

filenames = os.listdir(input_direct)

for filename in filenames:

   wordslist = []
   wordsintext =[]

   upcasecounter = 0
   punctcounter = 0
   numcounter = 0
   wordcounter = 0 
   incorrectcounter = 0
   ellipsecounter = 0

   with open(os.path.join(input_direct,filename),'r') as i:
      linesintxt = i.readlines()
   filename =  filename[:-4] + "_q10556rn.txt"

   for line in linesindic:
      for s in line.split():
         wordslist.append(s)

   for line in linesintxt:
      for s in line.split():
         letters = ""
         for i in range(0, len(s)):
            #check at the start to ensure dots seperated by other types of characters are
            #not counted into an ellipsis
            if s[i] != ".":
               ellipsecounter = 0

            if s[i].lower() in alphabet:
               if (s[i] != s[i].lower()):
                  upcasecounter += 1
               letters += s[i].lower()
            elif (s[i] in numlist):
               numcounter+=1
            elif (s[i] in punctlist):
               punctcounter+=1
              #This if statement checks if a dot is part of an ellipsis or not 
               if s[i] == ".":
                  if ellipsecounter == 2:
                     ellipsecounter = 0
                     punctcounter -= 2
                  else:
                     ellipsecounter +=1

         if len(letters)>0:
            wordcounter += 1
            wordsintext.append(letters)

   for word in wordsintext:
      if word not in wordslist:
         incorrectcounter += 1

   correctcounter = wordcounter - incorrectcounter

   with open(os.path.join(output_direct,filename),'w') as o:
      o.write("q10556rn \n")
      o.write("Formatting ################### \n") 
      o.write("Number of upper case letters changed: " + str(upcasecounter) + "\n")
      o.write("Number of punctuations removed: " + str(punctcounter) + "\n")
      o.write("Number of numbers removed: " + str(numcounter) + "\n")
      o.write("Spellchecking ################### \n")
      o.write("Number of words: " + str(wordcounter) + "\n")
      o.write("Number of correct words: " + str(correctcounter) + "\n")
      o.write("Number of incorrect words: " + str(incorrectcounter) + "\n")