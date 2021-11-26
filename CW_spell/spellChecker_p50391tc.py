file= open('test_file1.txt','r')
filecontent=file.read()
words=filecontent.split()
wordss=filecontent.split()


upper_count=digit_count=punctuation_count=lowercase_count=space_count=0


for i in filecontent:
	if(i.isupper()):
		upper_count+=1
	elif(i.isdigit()):
		digit_count+=1
	elif(i.islower()):
		lowercase_count+=1
	elif(i.isspace()):	
		space_count+=1
	else:
	    punctuation_count+=1; 

with open('EnglishWords.txt','r') as englishwords:
	englishwordscontent=englishwords.read()
	engwords=englishwordscontent.split()
	
	correct=wrong1=0
	for word in wordss:
		if word in engwords:
			correct+=1
		else:
			wrong1+=1
		wrong=wrong1-punctuation_count-digit_count-upper_count 

f=open('test_file1_p50391tc.txt','w')
f.write('p50391tc'+'\n'+
	            'Formatting ###################'+'\n'+
	            'Number of upper case words transformed:'+str(upper_count)+'\n'+
	            'Number of punctuation’s removed:'+str(punctuation_count)+'\n'+
	            'Number of numbers removed:'+str(digit_count)+'\n'+
	            'Spellchecking ###################'+'\n'+
	            'Number of words:'+str(len(words)-digit_count)+'\n'+
	            'Number of correct words in file:'+str(len(words)-digit_count-wrong)+'\n'+
	            'Number of incorrect words:'+str(wrong))