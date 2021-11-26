
def Hex_ASCII():
	length=len(Read_File)



	String_Remove_Hex=Read_File[4:length]
	List_File=String_Remove_Hex.split()

	length_of_list=len(List_File)


	finalstr=""

	for count in range(length_of_list):
		String_From_Element=str(List_File[count])
		Convert_Into_Byte=bytes.fromhex(String_From_Element)
		Byte_To_ASCII=Convert_Into_Byte.decode("ASCII")
		finalstr=finalstr+Byte_To_ASCII

	text=(finalstr.lower())
	Text_to_be_included.append(text)
	Input_File.close()


def Caeser_ASCII():
	length=len(Read_File)
	cipherText=Read_File[18:length]
	lens=len(cipherText)


	string_to_ASCII=""
	list_2=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
	list_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


	lenw=len(cipherText)

	for counter in range(lenw):
	    letter=cipherText[counter]

	    for total in range(len(list_1)):
	        if letter==list_1[total]:
	            ASCII=(list_2[total])
	            string_to_ASCII=string_to_ASCII+ASCII
	        elif letter==" ":
	            string_to_ASCII=string_to_ASCII+" "
	            break
	        



	text=(string_to_ASCII)
	Text_to_be_included.append(text)
	Input_File.close()


def Morse_ASCII():
	length=len(Read_File)
	String_Remove_Morse=Read_File[11:length]
	List_File=String_Remove_Morse.split()

	MORSE_CODE_INPUT = [ '.-','-...','-.-.','-..','.','..-.','--.','....',
	                    '..','.---','-.-','.-..','--','-.','---','.--.','--.-',
	                    '.-.','...','-','..-','...-','.--','-..-','-.--','--..',
	                    '.----','..---','...--','....-','.....','-....','--...',
	                    '---..','----.','-----','.-.-.-', '..--..','-.-.--','--..--','---...','-.-.-.','-....-','-.--.','-.--.-','-.--.','-.--.-','.----.','.-..-.','.-.-.- .-.-.- .-.-.-']
	ASCII_OUTPUT=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",'.','?','!',',',':',';','-','[',']','(',')'," ' ",' " ','...']
	length_of_list=len(List_File)

	ASCII_FINAL_OUTPUT=""

	for i in range(length_of_list):
		character=List_File[i]
		for count in range(len(MORSE_CODE_INPUT)):
			if character==MORSE_CODE_INPUT[count]:
				string_letter=str(ASCII_OUTPUT[count])
				ASCII_FINAL_OUTPUT=ASCII_FINAL_OUTPUT+string_letter
			elif character=='/':
				ASCII_FINAL_OUTPUT=ASCII_FINAL_OUTPUT+" "
				break

	text=(ASCII_FINAL_OUTPUT.lower())
	Text_to_be_included.append(text)
	Input_File.close()

import sys
import argparse
import os


args = str(sys.argv[1:])
args = args.replace("[","")
args = args.replace("]","")
args = args.replace(",","")
args = args.replace("'","")


templ=args.split('./')
length_of_List=len(templ)
Locations_List=templ[1:length_of_List]


finalOLoc=""
temp_Loc=Locations_List[0]
for i in range(len(temp_Loc)):
    letter=temp_Loc[i]
    if letter.isspace():
        finalOLoc=finalOLoc
    else:
        finalOLoc=finalOLoc+letter


Input_Location="/"+finalOLoc




Output_Folder=Locations_List[1]
Output_Location="/"+Locations_List[1]


all_files = os.listdir(Input_Location)



Output_Files_List=[]
Text_to_be_included=[]


for counter in range(len(all_files)):
    file=Input_Location+"/"+str(all_files[counter])
    Input_File=open(file)
    LENname=len(all_files[counter])
    copy_text=LENname-4
    Output_file_name=all_files[counter][0:copy_text]
    Output_file_name=Output_Location+"/"+Output_file_name+"_u63378mr.txt"
    Output_Files_List.append(Output_file_name)

    
    Read_File=Input_File.read()
    length=len(Read_File)


    if Read_File[0]=='H' or Read_File[0]=='h':
    	Hex_ASCII()

    elif Read_File[0]=='C' or Read_File[0]=='c':
    	Caeser_ASCII()

    elif Read_File[0]=='M' or Read_File[0]=='m':
    	Morse_ASCII()


for i in range(len(Output_Files_List)):
    file_name=Output_Files_List[i]
    Open_file=open(file_name,'w')
    input_text=Text_to_be_included[i]
    Open_file.write(input_text)
    Open_file.close()
