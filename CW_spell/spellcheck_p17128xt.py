import argparse
import re
import os


parser = argparse.ArgumentParser()

parser.add_argument("dir", nargs = "+")
args = parser.parse_args()

fileList = os.listdir(args.dir[1])


for x in range (0,len(fileList)):
	englishWords = open(args.dir[0], "r")
	inputFile = args.dir[1] + "/" + fileList[x]
	text = open(inputFile,"r")
	text = text.read()
	englishlist = []
	englishlist= englishWords.readlines()

	numberofnumber = len(re.findall("\d",text))
	numberofpunc = len(re.findall("[^\w\s\#\@]|_",text))
	numberofcap = len(re.findall(r"[A-Z]",text))
	text = text.lower()

	text = re.sub("\d","",text)
	text = re.sub("[^\w\s\#\@]|_","",text)
	text = re.sub("\n","",text)	
	text = re.sub(" +"," ",text)


	listofword = []
	word = ""
	text = text +" "
	for i in text:
		if i == " " and word != "":
			listofword.append(word)
			word = ""
		else:
			word = word + i

	correct = 0
	for e in listofword:
		for rightwords in englishlist:
			if (e + "\n") == rightwords:
				correct += 1

	c = args.dir[2] + "/" + fileList[x]
	d = c.replace(".txt", "_p17128xt.txt")
	f = open(d,'w')
	f.write("p17128xt\n"+
		    "Formatting ###################\n"+
		    "Number of upper case letters changed: " + str(numberofcap) + "\n" +
		    "Number of punctuations removed: " + str(numberofpunc) + "\n" +
		    "Number of numbers removed: " + str(numberofnumber) + "\n" + 
		    "Spellchecking ###################\n"+
		    "Number of words: " + str(len(listofword)) + "\n" + 
		    "Number of correct words: " + str(correct) + "\n" +
		    "Number of incorrect words: " + str(len(listofword)-correct)

		    )
	f.close


