import os, sys, string


#function for error message when the arguments are not right
def print_help_and_exit():
    print("Usage: " + sys.argv[0] + "[EnglishWords file] [input folder] [output folder]")
    sys.exit(0)

#spell check main code
#read the english file and test files and compare how many words are correct.
def checkspell(input_folder, output_folder, english_file, filename):
	f1=open(input_folder + filename,"r")
	f2=open(output_folder + filename.replace(".txt","_p98424rp.txt"),"w")
	f3=open(english_file,"r")
	word=f1.read()
	num=0
	punc=0
	upp=0
	cont=word.split()
	cont1=[]
	punctu=string.punctuation
	for con in cont:
	    ncont=""
	    for c in con:
	        if c.isdigit():
	            num+=1
	            ncont=ncont+""
	        elif c in punctu:
	        	punc+=1
	        	ncont=ncont+""
	        elif c.isupper():
	        	upp+=1
	        	ncont=ncont+ str(c.lower())
	        else:
	        	ncont=ncont+ str(c)
	    cont1.append(ncont)
	cont1=' '.join(cont1)

	f1.close()
	#formatting the file
	f1=open(input_folder + filename,"w")
	f1.write(cont1)
	f1.close()

	#checking the words in the file with the english words text file
	f1=open(input_folder + filename,"r")
	cont=f1.read()
	cont=cont.split()
	wordconte=f3.read()
	wordconte=wordconte.split()
	crctwords=0
	incrctwords=0
	leng=len(cont)
	for each in cont:
	    if each in wordconte:
	        crctwords+=1
	    else:
	        incrctwords+=1



	l1=["p98424rp",'\n',"Formatting ###################",'\n',"Number of upper case words transformed: " + str(upp),'\n',"Number of punctuations removed: "+str(punc),'\n',"Number of numbers removed: "+ str(num),'\n']
	f2.writelines(l1)


	l2=["Spellchecking ###################", '\n',"Number of words in file: "+ str(leng),'\n',"Number of correct words in file: "+str(crctwords),'\n',"Number of incorrect words in file: "+str(incrctwords),'\n']
	f2.writelines(l2)

	f3.close()
	f2.close()
	f1.close()

#checks number of arguments
if(len(sys.argv) != 4):
    print("ERROR: incorrect number of arguments")
    print_help_and_exit()

#get the files
english_folder_string = sys.argv[1]
input_folder_string = sys.argv[2]
output_folder_string = sys.argv[3]

#gets the list of files in the given directory
dire=os.listdir(input_folder_string)

#skims through files only if it is a text file and executes the calculation part
for file in dire:
    if ".txt" in file:
    	checkspell(input_folder_string, output_folder_string, english_folder_string, file)
