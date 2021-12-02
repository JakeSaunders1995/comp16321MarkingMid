import sys
import argparse
import os
args = str(sys.argv[1:])
args = args.replace("[","")
args = args.replace("]","")
args = args.replace(",","")
args = args.replace("'","")
breif_list=args.split("./")
length_of_breif_list=len(breif_list)
Locations_List=breif_list[1:length_of_breif_list]
Text_location="/"
Temporary_location=Locations_List[0]
for count in range(len(Temporary_location)):
	character=Temporary_location[count]
	if character.isspace():
		Text_location=Text_location
	else:
		Text_location=Text_location+character
Complete_Location_Input=""
Temporary_location=Locations_List[1]
for count in range(len(Temporary_location)):
	character=Temporary_location[count]
	if character.isspace():
		Complete_Location_Input=Complete_Location_Input
	else:
		Complete_Location_Input=Complete_Location_Input+character
Location_Input="/"+Complete_Location_Input
total_files=os.listdir(Location_Input)
Folder_for_Output=Locations_List[2]
Location_for_Output="/"+Folder_for_Output
all_ouput_files=os.listdir(Location_for_Output)
List_for_Output_Files=[]
Included_Text=[]


for number in range(len(total_files)):
	name_of_file=Location_Input+"/"+str(total_files[number])
	input_file=open(name_of_file)
	length_of_file_name=len(total_files[number])
	Text_to_be_copied=length_of_file_name-4
	Output_file_name=total_files[number][0:Text_to_be_copied]
	Output_file_name=Location_for_Output+"/"+Output_file_name+"_y44780cs.txt"
	List_for_Output_Files.append(Output_file_name)
	Test_File=open(Text_location)
	Reading_Test_File=Test_File.read()
	Comparison_List=Reading_Test_File.split()
	Comparison_List_Length=len(Comparison_List)
	Read_Input_File=input_file.read()
	String_Length=len(Read_Input_File)
	numbers=0
	Upper_Letter=0
	Special_Characters=0
	Alphabets=0
	Punctuations=0
	Final_String=""
	List_of_Punctuations=['.','?','!',',',':',';','-','[',']','(',')',"'",'"']



	for digit in range(String_Length):
		if Read_Input_File[digit].isnumeric():
			numbers=numbers+1
		elif Read_Input_File[digit].isupper():
			Upper_Letter=Upper_Letter+1
			Final_String=Final_String+Read_Input_File[digit]
		elif Read_Input_File[digit].isalpha() or Read_Input_File[digit].isspace():
			Alphabets=Alphabets+1
			Final_String=Final_String+Read_Input_File[digit]
		elif Read_Input_File[digit] in List_of_Punctuations:
			Punctuations=Punctuations+1
		elif Read_Input_File[digit]=="." and Read_Input_File[digit+1]=="." and Read_Input_File[digit+2]==".":
			Punctuations=Punctuations+1
		else:
			Special_Characters=Special_Characters+1

	Final_String=Final_String.lower()
	Files_List=Final_String.split()
	total_words=len(Files_List)
	Correct_Word=0
	Incorrect_Word=0

	for checking in range(total_words):
		if Files_List[checking] in Comparison_List:
			Correct_Word=Correct_Word+1
		else:
			Incorrect_Word=Incorrect_Word+1

	p=("y44780cs")
	q=("Formatting ###################")
	r=("Number of upper case letters changed:")+" "+str(Upper_Letter)
	s=("Number of punctuations removed:")+" "+str(Punctuations)
	t=("Number of numbers removed:")+" "+str((numbers))
	u=("Spellchecking ###################")
	v=("Number of words:")+" "+str(total_words)
	w=("Number of correct words:")+" "+str(Correct_Word)
	x=("Number of incorrect words:")+" "+str(Incorrect_Word)
	Words_to_be_added=[p,q,r,s,t,u,v,w,x]
	length_of_words=len(Words_to_be_added)
	Included_Text.append(Words_to_be_added)
	input_file.close()

for y in range(len(List_for_Output_Files)):
	name=List_for_Output_Files[y]
	File_Open=open(name,'w')
	for z in range(length_of_words):
		text_for_input=Included_Text[y][z]
		File_Open.write(text_for_input)
		File_Open.write("\n")






















