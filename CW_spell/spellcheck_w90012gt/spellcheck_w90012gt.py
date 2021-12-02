import sys
import os



def Read_File_English_Words (file_name):
	
	
	information = list()
	file = open(file_name, "r")
	
	for line in file:
		line = line.rstrip()

		information.append(line)
	# print(information)
	# print (len(information))
	file.close()
	
	return information

English_Location = sys.argv[1]
checker = Read_File_English_Words(English_Location)


def Read_File (file_name):
	
	information=""
	file = open(file_name, "r")
	for line in file:
		
		line = line.rstrip()
		
		information += " " + line
		

	
	# print(information)
	# print (len(information))

	return information





def Get_Name(file_name):
	
	listing=file_name.split(".")
	
	My_Info = listing[0]+ "_w90012gt."+listing[1]
	#print(My_Info)
	return My_Info


def Get_Input(file_path_name):
	list_of_information = list()
	files = os.listdir(file_path_name)
	# print("Work Here??")
	# print(files)
	# print(len(files))
	# print("Here OK")
	for file_name in files:

		file_name= os.path.join(file_path_name, file_name)
		information = Read_File(file_name)
		list_of_information.append(information)
	My_Info = [files, list_of_information, len(files)]
	return My_Info



def Upper_Case(information):
	counter=0
	for i in range(len(information)):
		if(ord(information[i])>64 and ord(information[i])<91):
			counter+=1

	return counter

def Punctuations(information):
	counter=0
	elipses=False
	br=0
	for i in range(len(information)):
		
		if(elipses):
			if(br==2):
				elipses=False
				br=0
			else:
				br+=1
			continue
		
		if(information[i] != " " and not (ord(information[i])>64 and ord(information[i])<91) and not (ord(information[i])>96 and ord(information[i])<123) and not (ord(information[i])>47 and ord(information[i])<58)):
			#print(information[i])
			if(i < len(information)-2 and information[i=="."] and information[i+1]=="." and information[i+2]=="."):
				elipses = True
				
			counter+=1

			

	return counter

def Numbers(information):
	counter=0
	for i in range(len(information)):
		if(ord(information[i])>47 and ord(information[i])<58):
			counter+=1
			#print(information[i])
	return counter


def Wording(information):
	#print("Here?")
	list_words = information.split()
	number = len(list_words)
	for word in list_words:
		#print(word)
		if ( not( (ord(word[0]) >64 and ord(word[0])<91) or (ord(word[0])<123 and ord(word[0])>96) ) ):
			number-=1
			#print(word[0])
	#print (type(information))
	return number



def Correct(information):
	list_words = information.split()
	number = 0
	for word in list_words:
		temp=list(word)
		# print(word)
		# print(temp)
		# print(len(temp))
		removing=list()
		for i in range (len(temp)):
			if(ord(temp[i])>64 and ord(temp[i])<91):
				x=ord(temp[i]) + 32
				temp[i]= chr(x)
			elif(not(ord(temp[i])>96 and ord(temp[i])<123)):
				removing.append(temp[i])

		for i in range (len(removing)):
				temp.remove(removing[i])
		alq=""
		for i in range (len(temp)):
			alq+=temp[i]
		if (alq in checker):

			number+=1
		#else:
			#print(word)
	return number


def Connecting (information):
	#print("1", information, "\n" )

	upper = Upper_Case(information)
	punctuations = Punctuations(information)
	numbers= Numbers(information)
	#print("Reached?")
	words = Wording(information)
	#print("Not in function?")
	correct_words = Correct(information)
	incorrect_words = words - correct_words
	info=""

	info += "w90012gt" + "\n"  
	info += "Formatting ###################"+"\n"
	info += "Number of upper case words changed: " + str(upper)
	info+= "\n"+ "Number of punctuations removed: "+ str(punctuations)
	info+= "\n"+ "Number of numbers removed: " + str(numbers)
	info+="\n" + "Spellchecking ###################" 
	info+="\n"+ "Number of words: " + str(words)
	info+="\n" + "Number of correct words: " + str(correct_words)
	info+="\n" + "Number of incorrect words: " + str(incorrect_words)

	return info


def Create_file(file_path_name_output, Names_Files_Information):
	files=Names_Files_Information[0]
	list_of_information=Names_Files_Information[1]
	counter = Names_Files_Information[2]
	#print(Names_Files_Information)
	for i in range (counter):
		data = Connecting(list_of_information[i])
		files[i] = Get_Name(files[i])
		file = open(os.path.join(file_path_name_output, files[i]), "w")
		file.write(data)
		file.close()

#print (checker[15], len(checker[15]))

file_path_name = sys.argv[2]
file_path_name_output = sys.argv[3]
Names_Files_Information = Get_Input(file_path_name)
Create_file(file_path_name_output, Names_Files_Information)