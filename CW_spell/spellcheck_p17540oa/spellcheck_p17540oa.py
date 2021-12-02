import sys
import os.path
import os
import re

EnglishWords = sys.argv[1]
inputpath = sys.argv[2]
outputpath = sys.argv[3]
datafile = open('EnglishWords.txt', 'r')

filelist = os.listdir(inputpath)
for file in filelist:
	output_file_name = file[:-4]
	f = open(inputpath+"/"+file,).readline()
	message = f
	pattern = r'[0-9]'
	new_msg = re.sub(pattern, '', message) #all digits -> empty
	punc = ('''!()-[]{};:'"\',<>./?@#$%^&*_~''')
	for ele in new_msg:
		if ele in punc:
			new_msg = new_msg.replace(ele, "") #remove punc
			new_msg = new_msg.lower() 
		
	cap = sum(1 for c in message if c.isupper())

	punc_count=0
	for i in message:
		if i in ('''!()-[]{};:'"\',<>./?@#$%^&*_~'''):
			punc_count += 1

	digits = 0
	for i in message:
		if i.isdigit():
			digits += 1

	word_count = len(re.findall("[a-zA-Z_]+", message))
	correct_count = 0
	msglist = re.sub("[^\w]", " ", new_msg).split() #string to list
	lines = datafile.readlines()
	lines = [line.strip() for line in lines]
	eng_word_list = lines   

	for x in msglist:
		if x in eng_word_list:
			correct_count += 1

	path = outputpath
	if not os.path.exists(path):
		os.makedirs(path)
	#outputfile = outputpath.split(".")
	outputfile = (outputpath+'/'+file[:-4])
	output = open((outputfile+"_p17540oa.txt"),"x")
	output.write("p17540oa\n"+"Formatting ###################\n"+"Number of upper case letters changed: "+str(cap)+"\nNumber of punctuations removed: "+str(punc_count)+'\nNumber of numbers removed: '+str(digits)+'\nSpellchecking ###################'+'\nNumber of words: '+str(word_count)+'\nNumber of correct words: '+str(correct_count)+'\nNumber of incorrect words: '+str(word_count - correct_count))
	output.close()
