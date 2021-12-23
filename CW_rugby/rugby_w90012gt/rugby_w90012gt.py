import sys
import os

def Read_File (file_name):
	
	
	file = open(file_name, "r")

	information = file.read()
	information = information.rstrip()
	file.close()
	# print(information)
	# print (len(information))
	return information

def Winner(data):
	score1=0
	score2=0
	for i in range (1,len(data),3):
		if (data[i]=="1"):
			if (data[i+1] == "t"):
				score1+=5
			elif (data[i+1] == "c"):
				score1+=2
			elif (data[i+1] == "p"):
				score1+=3
			elif (data[i+1] == "d"):
				score1+=3
		else:
			if (data[i+1] == "t"):
				score2+=5
			elif (data[i+1] == "c"):
				score2+=2
			elif (data[i+1] == "p"):
				score2+=3
			elif (data[i+1] == "d"):
				score2+=3
	information = str(score1) + ":" + str(score2)
	return information
	#print(str(score1) + ":" + str(score2))





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

def Create_file(file_path_name_output, Names_Files_Information):
	files=Names_Files_Information[0]
	list_of_information=Names_Files_Information[1]
	counter = Names_Files_Information[2]
	#print(Names_Files_Information)
	for i in range (counter):
		data = Winner(list_of_information[i])
		files[i] = Get_Name(files[i])
		file = open(os.path.join(file_path_name_output, files[i]), "w")
		file.write(data)
		file.close()


print("Start")

file_path_name = sys.argv[1]
file_path_name_output = sys.argv[2]
#print("1" , file_path_name_output)

#print("2", file_name_output)

Names_Files_Information = Get_Input(file_path_name)
Create_file(file_path_name_output ,Names_Files_Information)




