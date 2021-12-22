import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("dictionary")
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

for file in os.listdir(args.input):
	filepath = os.path.join(args.input,file)

	with open(filepath, "r") as f:
		string = f.read()+" "

		word=""
		upper=0
		punctuation=0
		numbers=0
		wordcount=0
		correct=0
		incorrect=0
		for character in string:
			if ord(character)>96 and ord(character)<123:
				word+=character
			elif ord(character)>64 and ord(character)<91:
				upper+=1
				character=character.lower()
				word+=character
			elif ord(character) == 39:
				punctuation+=1
			else:
				if ord(character)>47 and ord(character)<58:
					numbers+=1
				elif ord(character) != 32:
					punctuation+=1
				if word!="":
					wordcount+=1
					allwords=" "
					with open(args.dictionary, "r") as f:
						allwords += f.read()
					allwords=allwords.replace("\n"," ")
					wordcheck = " "+word+" "
					if wordcheck in allwords:
						correct+=1
					else:
						incorrect+=1
					word=""

		results=["r25329lc\n",
		"Formatting ###################\n",
		"Number of upper case words changed: "+str(upper)+"\n",
		"Number of punctuations removed: "+str(punctuation)+"\n",
		"Number of numbers removed: "+str(numbers)+"\n",
		"Spellchecking ###################\n",
		"Number of words: "+str(wordcount)+"\n",
		"Number of correct words: "+str(correct)+"\n",
		"Number of incorrect words: "+str(incorrect)]


		file = file[:len(file)-4]
		outputfile = file+"_r25329lc.txt"
		outputpath = os.path.join(args.output,outputfile)
		with open(outputpath, 'w') as f:
			for n in results:
				f.write(n)

