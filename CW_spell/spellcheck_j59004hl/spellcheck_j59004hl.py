import argparse
import os

input_dir=[]# input files list
global objectText
objectText=""
numUpper=0
numPunc=0
numNum=0
Spell={}

def ChangePath(path):# add /
	if path[-1]!="\\" or path[-1]!="/":
		path+="/"
	return path

def UpperCounter():
	global objectText
	counter=0

	for char in objectText:
		ASVal=ord(char)
		if ASVal>=65 and ASVal<=90:
			#print(ASVal)
			counter+=1
	objectText=objectText.lower()
	return counter

def NumCounter():
	global objectText
	counter=0
	#print(len(objectText))
	#print("----------------------------")
	degree=0
	while degree<len(objectText):
		#print(charPosition)
		#print(objectText[charPosition])
		ASVal=ord(objectText[degree])
		if ASVal>=48 and ASVal<=57:
			#print(ASVal)
			counter+=1
			objectText=objectText[0:degree]+objectText[degree+1:]
			degree-=1
		degree+=1
	return counter

def PuncCounter():
	global objectText
	counter=0
	degree=0
	ellipsis=0
	while degree<len(objectText):

		ASVal=ord(objectText[degree])
		if (ASVal>=33 and ASVal<=47) or (ASVal>=58 and ASVal<=64) or (ASVal>=91 and ASVal<=96) or (ASVal>=123 and ASVal<=126):
			if objectText[degree]=="@" or objectText[degree]=="#":
				ellipsis=0
				objectText=objectText[0:degree]+objectText[degree+1:]
				degree-=1
			elif objectText[degree]=="." and ellipsis<2:
				ellipsis+=1
				objectText=objectText[0:degree]+objectText[degree+1:]
				counter+=1
				degree-=1
			elif objectText[degree]=="." and ellipsis>=2:
				ellipsis=0
				objectText=objectText[0:degree]+objectText[degree+1:]
				counter-=1
				degree-=1
			else:
				#print(ASVal)
				ellipsis=0
				counter+=1
				objectText=objectText[0:degree]+objectText[degree+1:]
				degree-=1
		else:
			ellipsis=0
		degree+=1
	return counter

def SpellCheck(Dictionary):
	global objectText
	degree=0
	counter={"numWords":0,"numCorrect":0,"numIncorrect":0}
	words=objectText.split(" ")
	while degree<len(words):# remove surpus spaces

		if len(words[degree])>0:
			if words[degree][0]=="\n":
				words[degree]=words[degree][1:]
		if len(words[degree])>0:
			if words[degree][-1]=="\n":
				words[degree]=words[degree][0:-1]
		if words[degree]=="":
			words.pop(degree)
			degree-=1
		if "\n" in words[degree]:
			words.append(words[degree][words[degree].index("\n")+1:])
			words[degree]=words[degree][0:words[degree].index("\n")]
			
		if words[degree]=="":
			words.pop(degree)
			degree-=1
		degree+=1
	#print(words)
	for word in words:
		#print(word)
		counter["numWords"]+=1
		if (word+"\n") in Dictionary:
			counter["numCorrect"]+=1
	counter["numIncorrect"]=counter["numWords"]-counter["numCorrect"]
	return counter

parser=argparse.ArgumentParser()
parser.add_argument("English_words_file", type=str)
parser.add_argument("inputFile", type=str)
parser.add_argument("outputFile", type=str)
args=parser.parse_args()

#EngWDictionary=ChangePath(args.English_words_file)
input_folder=ChangePath(args.inputFile)
output_folder=ChangePath(args.outputFile)

input_dir = os.listdir(input_folder)

#os.chdir(input_folder)# change to that path

EngWList=open(args.English_words_file, "r")
EngWDictionary=EngWList.readlines()
EngWList.close()
print("There are "+str(len(input_dir))+" files in the input_folder.\n")

for file in input_dir:
	#print(file)
	mark_file= open(input_folder+file, "r")
	objectText=mark_file.read()
	#print(objectText[171])
	numUpper=UpperCounter()
	numNum=NumCounter()
	numPunc=PuncCounter()#   Formating
	Spell=SpellCheck(EngWDictionary)
	outContent="j59004hl\nFormatting ###################\nNumber of upper case words changed: "+str(numUpper)+"\nNumber of punctuations removed: "+str(numPunc)+"\nNumber of numbers removed: "+str(numNum)+"\nSpellchecking ###################\nNumber of words: "+str(Spell["numWords"])+"\nNumber of correct words: "+str(Spell["numCorrect"])+"\nNumber of incorrect words: "+str(Spell["numIncorrect"])+"\n"

	print(outContent)
	print("(The Spell Check result has saved into the output folder)\n")
	result=open(output_folder+file[0:-4]+"_j59004hl.txt", "w")
	result.write(outContent)
	result.close()

