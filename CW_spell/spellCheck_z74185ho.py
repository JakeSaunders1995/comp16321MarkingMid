import os, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument("ewordspath", type=str)
parser.add_argument("inputpath", type=str)
parser.add_argument("outputpath", type=str)
args = parser.parse_args()

cwd = os.getcwd()

# print(getpath(args.ewordspath))

punctuations = """!()-[]{,};:'".?…–"""
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWX"

for dirpath, dirnames, filenames in os.walk(args.inputpath):
	for file in filenames:
		# print(file)
		if file.endswith(".txt"):
			targetfile = os.path.join(os.path.relpath(dirpath, cwd),file)
			# Create the target list of words
			with open(targetfile,'r') as f:
				text = f.read()
				# print(text)
				wordslist = text.split()
				# print(wordslist)
				resultlist = []
				wordposition = 0
				u = 0
				p = 0
				n = 0
				
				while wordposition < len(wordslist):
					theword = wordslist[wordposition]
					charposition = 0
					puncposition = 0
					upperposition = 0
					newWord = ""
					while charposition < len(theword):
						char = theword[charposition]
						if (char.isdigit() == True):
							char = ""
							newWord += char
							n += 1
							charposition += 1

						elif (char in punctuations):
							char = ""
							newWord += char
							p += 1
							charposition += 1

						elif (char in uppercase):
							char = char.lower()
							newWord += char
							u += 1
							charposition += 1

						else:
							newWord += char
							charposition += 1
						
					# print(newWord)
					
					if (newWord == ""):
						pass
					else:
						resultlist.append(newWord)
					
					wordposition += 1
				# print(resultlist)

				# Compare string with file
				with open(args.ewordspath, 'r') as ewf:
					# ewords is the list of english words
					ewords = ewf.read().split()
					# print(ewords)
					newWordposition = 0
					correct = 0
					incorrect = 0
					while newWordposition < len(resultlist):
						currentWord = resultlist[newWordposition]
						ewordposition = 0
						while (currentWord != ewords[ewordposition]):
							ewordposition += 1
							if ewordposition >= len(ewords):
								break
						if ewordposition == len(ewords):
							incorrect += 1
							newWordposition += 1
						else:
							correct += 1
							newWordposition += 1
		
			FileName = file.split(".")
			outputFileName = FileName[0] + "_z74185ho." + FileName[1]
			outputFilePath = os.path.join(args.outputpath, outputFileName)

			# output style
			username = "z74185ho\n"

			formatting1 = "Formatting ###################\n"
			formatting2 = "Number of upper case words transformed: %s\n" % str(u)
			formatting3 = "Number of punctuation's removed: %s\n" % str(p)
			formatting4 = "Number of numbers removed: %s\n" % str(n)
			formatting = formatting1 + formatting2 + formatting3 + formatting4

			sc1 = "Spellchecking ###################\n"
			sc2 = "Number of words in file: %s\n" % str(len(resultlist))
			sc3 = "Number of correct words in file: %s\n" % str(correct)
			sc4 = "Number of incorrect words in file: %s\n" % str(incorrect)
			sc = sc1 + sc2 + sc3 + sc4

			out = username + formatting + sc


			with open(outputFilePath, 'w') as of:
				of.write(out)








