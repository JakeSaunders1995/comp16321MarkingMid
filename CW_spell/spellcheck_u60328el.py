import argparse
import os
import re
import string

parser=argparse.ArgumentParser()
parser.add_argument("inputfolder")
parser.add_argument("engfile")
parser.add_argument('outputfolder')

args=parser.parse_args()

inputfolder=args.inputfolder
if(inputfolder[-1]!= '/'):
    inputfolder=inputfolder+'/'
input_files=os.listdir(inputfolder)

outputfolder=args.outputfolder
if(outputfolder[-1]!='/'):
    outputfolder=outputfolder+'/'
outputfile=os.listdir(outputfolder)

numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['.','?','/','"',"'",'-',')','(',']','[', ';',':','...','{','}','!',',','…']

engdict=args.engfile
english=open(engdict).readlines()


for file in range(len(input_files)):
    inputfile=open(inputfolder+input_files[file],'r')


#initialise alphabetic sentences only
    wordonly=""

    Up,Punct,No,Cword,ICword=0,0,0,0,0 	

    for word in inputfile:
    	for letter in word:
    		if letter in string.ascii_uppercase:
    			Up+=1

    		for j in symbols:
    			if letter == j:
    				letter = ''
    				Punct+=1
    		for k in numbers:
    			if letter == k:
    				letter = ''
    				No += 1


    		wordonly += letter
    	 	

    wordonlyList=re.split(" ",wordonly)
    #To filter out empty strings in list and convert to low case
    wordonlyList = list(filter(None, wordonlyList))
    wordonlyList=[word.lower()for word in wordonlyList]

    

    updatedEnglish=[]
    #to remove \n and whitesp
    for Words in english:
    	updatedEnglish.append(Words.strip())


    for word in wordonlyList:
        if(word =='\n'):
            wordonlyList.remove(word)
    
        #No of words
    wordcount=(len(wordonlyList))

    for word in wordonlyList:
        if word in updatedEnglish:
            Cword+=1
        else:
            ICword+=1

    output=("u60328el"+"\nFormatting ###################"+
    	"\nNumber of upper case letters changed: "+str(Up)+
    	"\nNumber of punctuations removed: "+str(Punct)+
    	"\nNumber of numbers removed: "+str(No)+
    	"\nSpellchecking ###################"+
    	"\nNumber of words: "+str(wordcount)+
    	"\nNumber of correct words: "+ str(Cword)+
    	"\nNumber of incorrect words: "+ str(ICword)
    	)

    outputfile=open(str(outputfolder)+str((input_files[file])[0:(len(input_files[file])-4)])+'_u60328el'+".txt",'w')
    outputfile.write(output)









