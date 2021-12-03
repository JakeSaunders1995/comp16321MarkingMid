import argparse, os, sys, re

engpath = sys.argv[1]
filepath = sys.argv[2]
outputpath = sys.argv[3]
os.mkdir(outputpath)

inputfile = os.listdir(filepath)
print(inputfile)
for file in inputfile:


	inputfilepath = os.path.join(filepath,file)
	with open (inputfilepath) as f:
		contentofinput = f.read()
		print(contentofinput)
		print(type(contentofinput))

		#remove puncations
		apple = r"\w| "
		numberandletter = re.findall(apple, contentofinput)
		withnumber = ''.join(str(i) for i in numberandletter)
		# print(withnumber)
		# print(type(withnumber))
		punc = len(contentofinput) - len(withnumber)
		print("number of puncation: ",punc)

		#remove numbers
		banana = "[^0-9]| "
		onlyletter = re.findall(banana, withnumber)
		onlyletter = ''.join(str(i) for i in onlyletter)
		# print(onlyletter)
		numb = len(withnumber) - len(onlyletter)
		print("number of numbers: ",numb)

		#transform upper to lower
		noupper = onlyletter.lower()
		#numberoftotalword = len(noupper)
		# print(noupper)
		orange = "[a-z]| "
		lowerletter = re.findall(orange, onlyletter)
		lowerletter = ''.join(str(i) for i in lowerletter)
		upper = len(onlyletter) - len(lowerletter)
		print("number of upper letter: ", upper)

		#number of words
		str1 = []
		str2 = []
		fp = open("text.txt","w")
		fp.write(noupper)
		fp.close()

		f = open("text.txt",'r')
		wordintext = open("wordlist.txt",'w')
		for line in f:
			words = line.split()
			numofwords = len(words)
	
		for line in f.readlines():
			str1.append(line.replace("\n",""))
			
		print("number of words: ",numofwords)
		print(type(words))
		print(words)



		
		#read the content of englishword.txt
		englishwordlist = []
		fe = open(engpath,'r')
		lines = fe.readlines()
		for line in lines:
			englishwordlist.append(line.strip('\n'))

		# englishword = list(englishwordlist)
		
		words_set = set(words)
		intersection = words_set.intersection(englishwordlist)
		intersection_list = list(intersection)
		print(intersection_list)
		noofco = len(intersection_list)
		print("number of correct words: ",noofco)
		noofinc = numofwords - noofco
		print("number of incorrect words: ",noofinc)

		os.chdir(outputpath)
		outputfilename = 'text_file' + file[9] + '_r42421yz.txt'
		fp = open(outputfilename,'a')

		fp.write("r42421yz")
		fp.write('\n')
		fp.write("Formatting ###################")
		fp.write('\n')
		
		fp.write("Number of upper case words transformed: ")
		fp.write(str(upper))
		fp.write('\n')

		
		fp.write("Number of punctuation's removed: ")
		fp.write(str(punc))
		fp.write('\n')

		fp.write("Number of numbers removed: ")
		fp.write(str(numb))
		fp.write('\n')

		fp.write("Spellchecking ###################")
		fp.write('\n')
		
		fp.write("Number of words in file: ")
		fp.write(str(numofwords))
		fp.write('\n')
		
		fp.write("Number of correct words in file: ")
		fp.write(str(noofco))
		fp.write('\n')
		
		fp.write("Number of incorrect words in file: ")
		fp.write(str(noofinc))
		fp.close()