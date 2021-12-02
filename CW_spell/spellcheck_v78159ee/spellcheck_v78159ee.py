import os
import sys #takes command line arguments and passes it through the code

inputfolder = sys.argv[2]
outputfolder = sys.argv[3]
WordsFile = sys.argv[1]

eng = open(WordsFile)
EnglishWords = eng.read()







specialChar = """~)`,}!@#$]""%^&*(-_+={[|/:;'<>,.?"""
numbers = """0123456789"""


for filename in os.listdir(inputfolder):
	f = os.path.join(inputfolder, filename)
	if os.path.isfile(f):
		inputfile = open(f)
		contents = inputfile.read()
		
		rawText = contents
		readyText = ""
		
		punctuation = 0
		number = 0
		uppercase = 0
		
		
		for a in range(len(rawText)):
			if rawText[a].isupper(): 
				uppercase = uppercase + 1
				
				readyText = readyText + rawText[a] 
			elif rawText[a] in specialChar:
				punctuation = punctuation + 1
				
			elif rawText[a] in numbers:
				number = number + 1
				
			elif rawText[a] == " ":
				readyText = readyText + " "
				
			else: 
				readyText = readyText + rawText[a] 
			
		
					
		readyText = readyText.lower()
		
		print (readyText)
		print("Punctuation: " + str(punctuation))
		print("Numbers: " + str(number))
		print("Uppercase: " + str(uppercase))
		
		checkWords = readyText.split()
		correct = 0
		wrong = 0
		
		for b in range(len(checkWords)):
			if checkWords[b] in EnglishWords:
				correct = correct + 1
			else:
				wrong = wrong + 1
		print ("Number of words: " + str(len(checkWords)))
		print ("Correct: " + str(correct))
		print ("Wrong : " + str(wrong))
		
		
		output = filename[:-4] + "_v78159ee.txt"
		folderpath = os.path.join(outputfolder, output) #gets the path for the output folder
		output_file = open(folderpath, "w")
		output_file.write( "v78159ee \n Formatting ################### \n Number of upper case letters changed: " + str(uppercase) + "\n NUmber of punctuations removed: " + str(punctuation) + "\n Number of numbers removed: " + str(number) + "\n Spellchecking ################### \n Number of words: " + str(len(checkWords)) + "\n Number of correct words: " + str(correct) + "\n Number of incorrect words: " + str(wrong) )
		
	

				
					
				
		#[user name]
#Formatting ###################
#Number of upper case letters changed: 4
#Number of punctuations removed: 5
#Number of numbers removed: 0
#Spellchecking ###################
#Number of words: 54
#Number of correct words: 54
#Number of incorrect words: 
		
		
		
		#remove punctuations, number and special characters. Changing uppercase to lower, check if word is in English words file.
		
		#step one: split file for space
		#step 2: for loop to loop through all terms and nested for loop to look at each character
		#in the 2nd for loop, if statements to change uppercase and to remove punctuations, special characters, etc
		#add remainder to plaintext
		# plainText = plaintext + " " to put a space between each word
		#split plainText when done
		#for loop to check each word that has been spe
		#count number of punctuations removed
		
		
		

