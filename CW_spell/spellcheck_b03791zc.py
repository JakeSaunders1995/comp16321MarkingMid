import argparse 
import os

numbers = ("1234567890")
punctuations = ("""!()-[]{};:'",<>./?@#$%^&*_~""")

numbers = list(numbers)
punctuations = list(punctuations)

path = argparse.ArgumentParser()
path.add_argument("English_words")
path.add_argument("input_path")
path.add_argument("output_path")

file = path.parse_args()
for infiles in os.listdir(file.input_path):
	Input = open(file.input_path + "/" +infiles, "r")
	t = list(file.output_path + "/" +infiles)
	for i in range (4):
		t.pop(-1)
	t = ("").join(t)
	filename = t + "_b03791zc"
	filepath = os.path.join(file.output_path, filename)
	Output = open(filepath, "w")
	wordF = open(file.English_words)
	EngW = wordF.readlines()
	for i in range (len(EngW)):
		EngW[i] = EngW[i].strip()
	OgTxt = Input.readlines()
	OgTxtSplit = list(str(OgTxt[0]))
	Uppercase = 0
	Numbers = 0
	Punctiations = 0
	CWords = 0
	WWords = 0
	length = len(OgTxtSplit)
	i = 0
	while i < length:
		if OgTxtSplit[i] in numbers:
			OgTxtSplit.pop(i)
			Numbers += 1
			length -= 1
		elif OgTxtSplit[i] in punctuations:
			OgTxtSplit.pop(i)
			Punctiations += 1
			length -= 1
		elif OgTxtSplit[i].isupper():
			OgTxtSplit[i] = OgTxtSplit[i].lower()
			Uppercase += 1
			i += 1
		elif OgTxtSplit[i] == "\n":
			OgTxtSplit.pop(i)
			length -= 1
		else:
			i += 1
		
	ModTxt = "".join(OgTxtSplit)
	test = []
	ModTxt = ModTxt.split()
	for o in range (len(ModTxt)):
		if ModTxt[o] in EngW:
			CWords += 1
		else:
			WWords += 1
			test.append(ModTxt[o])
	final = "b03791zc \n" + "Formatting ###################\n" + "Number of upper case letters changed: "+str(Uppercase)+ "\nNumber of punctuations removed: "+str(Punctiations)+"\nNumber of numbers removed: "+str(Numbers)+"\nSpellchecking ###################"+"\nNumber of words: "+str(len(ModTxt))+ "\nNumber of correct words: "+str(CWords)+ "\nNumber of incorrect words: "+str(WWords)
	Output.writelines(final)
	Input.close()
	Output.close()