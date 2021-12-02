import os
import sys

dictionary= sys.argv[1]
folder_output= sys.argv[3]
folder_input = sys.argv[2]
dictionary=open(dictionary,"r")
diction= dictionary.read()
dictionary.close()
diction=diction.split()
if not os.path.isdir(folder_output):
	os.mkdir(folder_output)
for file in os.listdir(folder_input):
	with open(os.path.join(folder_input,file),"r") as file_input:
		inputstr=file_input.read()
		w_list=inputstr.split()
		# def to count the words
		def words_counter (w_list):
			return len(w_list)
		#def calculate numbers and remove them	
		def numbers_counter ():
			global inputstr
			numbers=["1","2","3","4","5","6","7","8","9","0"]
			total=0
			for i in inputstr:
				for j in numbers:
					if i==j:
						inputstr=inputstr.replace(i,"",1)
						total+=1
			return total
		#def calculate punctuation and remove them
		def punctuation_counter():
			global inputstr
			temp=inputstr
			total=0
			punctuation=["[","]","(",")","{","}",";",".",",","!","?","/","-","'",'"',":"]
			for i in inputstr:
				for j in punctuation:
					if i==j:
						inputstr=inputstr.replace(i,"",1)
						total+=1
			for i in range(len(temp)):
				if temp[i]=="." and i<=len(temp)-3 and temp[i+1]=="." and temp[i+2]==".":
					total-=2

			return total
		#from upper case to lower case
		def low ():
			global inputstr
			total=0
			high=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
			lowList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
			for i in inputstr:
				for j in range(len(high)):
					if i==high[j]:
						inputstr=inputstr.replace(i,lowList[j],1)
						total+=1
			return total
		#def calculate numbers of incorrect words	
		def incorrect (w_list,diction):
			global inputstr
			total=0
			for i in w_list:
				if i in diction:
					total+=1
			
			inc=len(w_list)-total
			return inc
		n_number=numbers_counter()
		w_list=inputstr.split()

		p_number=punctuation_counter()
		w_list=inputstr.split()

		l_number=low()
		w_list=inputstr.split()
		w_number=words_counter(w_list)
		in_number=incorrect(w_list,diction)
		co_number=w_number-in_number
		result="p80873ab\nFormatting ###################\nNumber of upper case words changed: "+str(l_number)+"\nNumber of punctuations removed: "+str(p_number)+"\nNumber of numbers removed: "+str(n_number)
		result+="\nSpellchecking ###################\nNumber of words: "+str(w_number)+"\nNumber of correct words: "+str(co_number)+"\nNumber of incorrect words: "+str(in_number)
	with open(os.path.join(folder_output,os.path.basename(file)[:-4]+"_p80873ab"),"w") as file_output:
		file_output.write(result)	