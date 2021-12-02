import sys
import os
folder  = os.listdir(sys.argv[2])

base= os.getcwd()

with open(sys.argv[1], 'r') as y:
	wordlist = y.read()
wordlist = wordlist.split()

for file in folder:
	os.chdir(sys.argv[2])
	with open(file, 'r') as f:
		contents = f.read()
	num=0
	punct=0
	caps=0
	typo=0
	x=0
	while x < len(contents):
		if contents[x].isdigit() == True:
			contents = contents[0:x] + contents[x+1:]
			num+=1
			x-=1
		x+=1

	x=0
	while (x!=-1): 
		x = contents.find("...")
		if (x!=-1):
			contents = contents[:x]+contents[x+3:]
			punct+=1

	x=0
	while x < len(contents):
		if contents[x].isalpha() != True and contents[x] != " " and contents[x] != "@" and contents[x] != "#":
			contents = contents[0:x] + contents[x+1:]
			punct+=1
			x-=1
		x+=1

	x=0
	z= contents
	contents = contents.lower()
	while x < len(contents):
		if contents[x] != z[x]:
			caps+=1
		x+=1
	contents = contents.split()
	correct=0
	for word in contents:
		if word in wordlist:
			correct+=1

	typo = len(contents)-correct

	new_file = sys.argv[3] + "/" + file[:-4] +"_w65214ka.txt"
	os.chdir(base)
	text_file = open(new_file, 'w')
	text_file.write("w65214ka\n")
	text_file.write("Formatting ###################\n")
	text_file.write("Number of upper case letters changed: " + str(caps) + "\n")
	text_file.write("Number of punctuations removed: " + str(punct) +"\n")
	text_file.write("Number of numbers removed: " + str(num) + "\n")
	text_file.write("Spellchecking ###################" + "\n")
	text_file.write("Number of words: "+ str(len(contents)) + "\n")
	text_file.write("Number of correct words: " + str(correct) + "\n")
	text_file.write("Number of incorrect words: " + str(typo) + "\n")
	text_file.close()