import os
import os.path
import sys
import re

eng = open(sys.argv[1])
english = eng.read()
eng.close()	
inputdir2 = os.listdir(sys.argv[2])
inputdir2.sort()


# outputdir = sys.argv[3]



# for filename in os.listdir(inputdir2):
# f = open(inputdir2 + "/" + filename, 'r')
# data = f.read()

# finaloutput = []
# folder = os.listdir(inputdir2)
# index = 0
# folder.sort()
# for filename in folder:
	# filepath = inputdir2 + "/" + filename
	# f = open(inputdir2 + "/" + filename, 'r')
	# data = f.read()
	# path = outputdir
	# outputfname = filename[:-4]

numbercount = 0
ellipsis = 0
puntuationcount = 0 
uppercasecount = 0
lowercasecount = 0
wordscorrect = 0
wordsincorrect = 0

 # number count
def A(data):
	global puntuationcount , numbercount , uppercasecount
	for char in data:
		if char.isdigit():
			numbercount += 1
# print('number count',numbercount)

# remove numbers

	string = data
	p = r'[0-9]'
	result = re.sub(p,'',string)


# remove punctuation

	punctuation = '''!()-[]{};:'",<>./?#%^&*_~'''
	punctuationcount = 0
	testStr = result
	for ele in testStr:
		if ele in punctuation:
		   	testStr = testStr.replace(ele, "")
		   	puntuationcount += 1
# print('punctuation count',puntuationcount)

# number of caps
	uppercasecount = 0
	for i in testStr:
		if i.isupper():
			uppercasecount += 1
# print('upperCase count:',uppercasecount)

# make them all lowercase

	lowercase = testStr.lower()

#split string into list of words 

	lowerLst = lowercase.split()
	countwords = len(lowerLst)
# print(lowerLst)
# print('word count',countwords)

#comparing with dictionary to see if they're correct

	dictionarylist = english.split()
	wordscorrect = 0
	wordsincorrect = 0
	for word in lowerLst:
		if word in dictionarylist:
			wordscorrect += 1
		else:
			wordsincorrect += 1

#displaying output 

	finaloutput = ""

	finaloutput += 'p37429am\n'
	finaloutput += 'Formatting ###################\n'
	finaloutput += 'Number of upper case letters changed:' + str(uppercasecount) + '\n'
	finaloutput += 'Number of punctuations removed:' + str(puntuationcount) + '\n'
	finaloutput += 'Number of numnbers removed:' + str(numbercount) + '\n'
	finaloutput += 'Spellchecking ###################\n'
	finaloutput += 'Number of words:' + str(countwords) + '\n'
	finaloutput += 'Number of correct words:' + str(wordscorrect) + '\n'
	finaloutput += 'Number of incorrect words:' + str(wordsincorrect)

	return finaloutput

for files in inputdir2:
    with open(sys.argv[2]+"/"+files, 'r') as b:
        string = b.read()
        with open(sys.argv[3]+"/"+files[:-4]+ '_p37429am.txt','w+') as h:
            h.write(A(string))


	# if not os.path.exists(path):
	# 	os.makedirs(path)
	# outputf = outputdir + '/' + filename[0:-4] + '_' + 'p37429am.txt'
	# output = open(outputf,'w')
	# output.write(finaloutput)
	# output.close()

# with open(outputfile, "w") as output:
# 	output.write(finaloutput)
# 	
# /home/csimage/Documents/PythonStuff/COMP16321-Labs_p37429am/program3/inputfiles
