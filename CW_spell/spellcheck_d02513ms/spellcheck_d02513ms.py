import sys
import os
for fi in os.listdir(sys.argv[2]):
	with open(sys.argv[2] + "/" + fi,'r') as f:
		contents = f.read().rstrip()
		simpletext = ""
		spellcheck = ""
		upper_letters=0
		punctuations=0
		punc=['?','!',',',':',';','-','<','>','[',']','(',')','{','}',"'",'"','–','—']
		numbers=0
		words=0
		correct_words=0
		incorrect_words=0
		i=0
		while i<len(contents):
			if contents[i] in punc:
				punctuations+=1
				i+=1
			elif(contents[i]=='.'):
				if(i<(len(contents)-2)):
					if(contents[i+1]=='.' and contents[i+2]=='.'):
						punctuations+=1
						i+=3
					else:
						punctuations+=1
						i+=1
				else:
					punctuations+=1
					i+=1
			else:
				if(contents[i].isnumeric()):
					numbers+=1
				elif(contents[i].isupper()):
					upper_letters+=1
					simpletext+=contents[i]
				else:
					simpletext+=contents[i]
				i+=1
		simpletext=simpletext.lower()
		theWords = []
		file = open(sys.argv[1],'r')
		for line in file:
			line=line.rstrip()
			theWords.append(line)
		for cuvant in simpletext.split():
			words+=1
			if(cuvant in theWords):
				correct_words+=1
			else:
				incorrect_words+=1
		spellcheck+="d02513ms"
		spellcheck+="\nFormatting ###################"
		spellcheck+="\nNumber of upper case letters changed: "
		spellcheck+=str(upper_letters)
		spellcheck+="\nNumber of punctuations removed: "
		spellcheck+=str(punctuations)
		spellcheck+="\nNumber of numbers removed: "
		spellcheck+=str(numbers)
		spellcheck+="\nSpellchecking ###################"
		spellcheck+="\nNumber of words: "
		spellcheck+=str(words)
		spellcheck+="\nNumber of correct words: "
		spellcheck+=str(correct_words)
		spellcheck+="\nNumber of incorrect words: "
		spellcheck+=str(incorrect_words)
	Output_folder = sys.argv[3]
	fi = fi.replace(".txt","")
	fi += "_d02513ms.txt"
	output_file=open(Output_folder+"/" + fi,"w")
	output_file.write(spellcheck)