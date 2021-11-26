
import argparse, os


parser = argparse.ArgumentParser()
parser.add_argument('words')
parser.add_argument('originalfile')
parser.add_argument('spellcheckedfile')
args = parser.parse_args()

#words = open(args.words, "r")
#filetobechecked = open(args.originalfile, "r")
strfile = os.listdir(args.originalfile)
outputfile = os.listdir(args.spellcheckedfile)
q=0
while q<len(strfile):
	paragraph = ""
	file = args.originalfile+"/"+strfile[q]
	filetobechecked = open(file, "r")
	#loading everything in 'originalfile' into a variable/array so that it can be searched 
	while True:
		w = filetobechecked.read(1)
		if not w:#if end of file is reached
			break
		paragraph = paragraph + w

	filetobechecked.close()

	#initialising all variables
	newpar = ""
	i=0
	numremoved = 0
	punctremeoved = 0
	uppercasechanges = 0
	m=0
	n=0
	w = ""
	newword = ""
	numofwords=0
	spellingerrors = 0



	while i < len(paragraph):#loop through all characters in paragraph
		
		num1 = ord(paragraph[i])#converting each character into its ASCII/unicde value
		#incorrectchar = False
		#while incorrectchar == False:
			
		if (num1 >= 48 and num1 <= 57) or (num1 >=33 and num1 <= 34) or (num1 >=39 and num1 <=41) or (num1 >= 44 and num1 <=45) or (num1 >= 58 and num1 <= 59) or (num1 == 63) or (num1 == 91) or (num1 ==93) or (num1 ==96) or (num1 == 123) or (num1 == 125):#if number or punctuation/special character
			if num1 >=48 and num1 <= 57:
				numremoved += 1#counter fo numbers found and removed 
			else:
				punctremeoved += 1#counter for punctuation/ special characters found and removed
		#	incorrectchar = True
		elif num1 == 46:
			if paragraph[i:i+2] == "...":
				i+=2
			punctremeoved += 1
		#	incorrectchar = True
		else:
			if (num1>=65 and num1<=90):#if num1 is a capital letter
				uppercasechanges += 1#counter for capital letters found and converted
			newpar = newpar + paragraph[i].lower()
		#	incorrectchar = True
		
		i+=1 # go to next charcter
	print(newpar)

	while m<(len(newpar)-1):
		m+=1
		found = False
		r = 0
		while found == False:
			if newpar[n+r] == " ":#getting rid of any extra spaces before comparing each word
				r += 1
			else:
				found = True
				n += r ##move to character after any extra spaces
				m += r
		if newpar[m] == " ":
			numofwords+=1 # if a space is found that means characters between n and m are not a space and so a word has been found 
			newword = newpar[n:m]
			n = m + 1 # go to characters after space to identify start of next word
			vocab = open(args.words, "r") # open english words file
			while found==True:
				# read each line of file into variable w
				w = vocab.readline() 
				if not w: # if end of file has been reached, word not in dictionary and so spelling error has occured
					spellingerrors += 1
					found = False
				w = w[0:len(w)-1] # because each word in file is separated by /n take each word to compare as its (total length - /n)
				if newword == w:# word has been found 
					found = False
			vocab.close()		
			
	# increment number of words as havent checked last word and need to do so 
	numofwords += 1
	vocab = open(args.words,"r")
	#found = False
	while found == False:
		w = vocab.readline()
		newword = newpar[n:len(newpar)] #last word in file must be located from position n to the position of the last character in newpar 
		
		if not w:
			spellingerrors += 1
			found = True
		w = w[0:(len(w)-1)]
			
		if newword == w:
			found = True
						

	vocab.close()
	numofcorrectwords = numofwords - spellingerrors#difference between total word count and words with spelling errorw == total number of words spelt correctly

	spellcheckedfile = strfile[q]
	spellchecked = spellcheckedfile[0:len(spellcheckedfile)-4]+"_r85193di.txt"

	outputfile = open(spellchecked, "w")#open file to write into
	outputfile.write(f"r85193di \n")
	outputfile.write(f"Formatting ################### \n")
	outputfile.write(f"Number of upper case words changed: {uppercasechanges} \n")
	outputfile.write(f"Number of punctuations removed: {punctremeoved} \n")
	outputfile.write(f"Number of numbers removed: {numremoved} \n")
	outputfile.write(f"Spellchecking ################### \n")
	outputfile.write(f"Number of words: {numofwords} \n")
	outputfile.write(f"Number of correct words: {numofcorrectwords} \n")
	outputfile.write(f"Number of incorrect words: {spellingerrors} \n")
	outputfile.close()
	q+=1