import os,sys 
inputfile=sys.argv[2]
path1=os.listdir(inputfile)
outputfile=sys.argv[3]

def spellcheck():
	file3= open(sys.argv[1],"r")
	number = 0
	puncuation = 0
	upper_case = 0 
	no_of_words=0
	no_of_correct_words = 0
	no_of_incorrect_words = 0 
	#x=file1.read()
	word=x.split()
	y = file3.read()
	words=y.split(" ")
	str1 = ""
	for z in words:
		str1+=z

	str2=""
	for i in word:
		j=0
		while j < len(i):
			if i[j] in "1234567890":
	
				number+=1
				j+=1
				#print(i[j])
				continue
			elif i[j] in "?!,:–;-()[]{}\'\"":
				#no_of_incorrect_words+=1
				#print(i[j])
				puncuation+=1
				j+=1
				continue
			elif i[j] in ".":
				if j!=len(i)-1:
					if i[j+1] =="." and i[j+2]==".":
						puncuation+=1
						j+=3
						continue
					else:
						puncuation+=1
						j+=1
						continue
				else:
			
					puncuation+=1
					j+=1
					continue

			elif i[j].isupper():
				#no_of_incorrect_words+=1
				#print(i[j])
				upper_case+=1
				lowercase=i[j].lower()
				str2+=lowercase
				j+=1
				continue
			else:
				str2+=i[j]
				j+=1
		
		str2+=" "
		
	a=str2.split()
	
	for i in a:
		
		if i in z :
			no_of_correct_words+=1
		else:
			#print(i)
			no_of_incorrect_words+=1
		

	no_of_words=no_of_correct_words+no_of_incorrect_words
	
	file2.write("t30023mm\n") 
	file2.write("Formatting ###################\n")
	file2.write("Number of upper case letters transformed: " + str(upper_case) + "\n")
	file2.write("Number of puncuations removed: " + str(puncuation) + "\n")
	file2.write("Number of numbers removed: " + str(number) + "\n")
	file2.write("Spellchecking ###################" + "\n")
	file2.write("Number of words: " + str(no_of_words) + "\n")
	file2.write("Number of correct words: " + str(no_of_correct_words) + "\n")
	file2.write("Number of incorrect words: " + str(no_of_incorrect_words) + "\n")


for file in range(len(path1)):
	name_input=path1[file]
	a=os.path.join(inputfile,name_input)
	file1=open(a,"r")
	name=""
	for letter in name_input:
		if letter==".":
			break
		else:
			name+=letter
	name_output=name+"_t30023mm"
	b=os.path.join(outputfile,name_output)
	file2=open(b,"w")

	x=file1.read()
	spellcheck()