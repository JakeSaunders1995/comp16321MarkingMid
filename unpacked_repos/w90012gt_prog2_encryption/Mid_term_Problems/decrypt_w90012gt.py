import sys
import os

eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..',
     'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 
     'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 
     'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 
     'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 
     'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 
     'y' : '-.--', 'z' : '--..', 
     '.' : '.-.-.-',
      '?' : '..--..', '!' : '-.-.--', ':' : '---...',
       ',' : '--..--', ' ' : '/', '-' : '-....-',
       ';' : '-.-.-.', '(' : '-.--.', ')' : '-.--.-',
       "'" : '.----.', '"' : '.-..-.'
        }
morse_to_eng = dict((v,k) for k,v in eng_to_morse.items())



def Read_File (file_name):
	
	
	file = open(file_name, "r")

	information = file.read()
	information = information.rstrip()
	file.close()
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





def Decryption_Method(data):
	algorithm =""
	#print("Data: ", data)
	while (data[0] != ":"):
		algorithm += data[0]
		data = data[1:]

	#print (algorithm)
	data = data[1:]
	info = [algorithm, data]
	return info

def Hex(data):
	#print ("Empty???", data)
	info = bytes.fromhex(data).decode("ASCII")
	no_upper_info=""
	for i in range (len(info)):
		#print(type(ord(info[i])))
		if (ord(info[i])>=65 and ord(info[i])<=90):
			no_upper_info +=chr(ord(info[i])+32)
		else:
			no_upper_info+= info[i]
	return no_upper_info

def Caesar(data):
	info=""
	for i in range(len(data)):
		if(data[i] != " " and data[i] !="a" and data[i] !="b" and data[i]!="c" and data[i] !="A" and data[i] !="B" and data[i]!="C"):
			x = chr(ord(data[i])-3)
			info+=x
		elif(data[i]=="a"):
			info+="x"
		elif(data[i]=="b"):
			info+="y"
		elif(data[i]=="c"):
			info+="z"
		elif(data[i]=="A"):
			info+="X"
		elif(data[i]=="B"):
			info+="Y"
		elif(data[i]=="C"):
			info+="Z"
		else:
			info+=" "
	#print(info)
	return info


def Morse(data):
	list_of_words= data.split("/")
	info=""
	for word in list_of_words:
		keeper = word.split()
		#print("Word: ", keeper)
		decript_word=""
		for letter in keeper:
			#print("Code: ", letter)
			decript_word+=morse_to_eng[letter]
		info+=decript_word
		info+=" "
	return info
		

def Decripting(data, algorithm):
	
	information = " "
	#print("Reached Here??")
	if (algorithm == "Hex"): 
		#print("Here Ok")
		information = Hex(data)
		
	elif (algorithm == "Caesar Cipher(+3)"):
		information = Caesar(data)

	elif (algorithm=="Morse Code"):
		#print("Here Ok")
		information = Morse(data)
	return information

def Connecting (information):
	algorithm= Decryption_Method(information)
	info = Decripting(algorithm[1], algorithm[0])
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


file_path_name = sys.argv[1]
file_path_name_output = sys.argv[2]
Names_Files_Information = Get_Input(file_path_name)
Create_file(file_path_name_output, Names_Files_Information)



