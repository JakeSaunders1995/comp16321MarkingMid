
def Hex_INTO_ASCII():
	LENGTH=len(Read_File)



	String_Remove_Hex=Read_File[4:LENGTH]
	List_File=String_Remove_Hex.split()

	length_of_list=len(List_File)


	FINAL_ASCII_STRING=""

	for count in range(length_of_list):
		String_From_Element=str(List_File[count])
		Convert_Into_Byte=bytes.fromhex(String_From_Element)
		Byte_To_ASCII=Convert_Into_Byte.decode("ASCII")
		FINAL_ASCII_STRING=FINAL_ASCII_STRING+Byte_To_ASCII

	text=(FINAL_ASCII_STRING.lower())
	Text_to_be_included.append(text)
	Input_File.close()


def Caeser_Cipher_INTO_ASCII():
	LENGTH=len(Read_File)
	cipherText=Read_File[18:LENGTH]
	length_of_string=len(cipherText)


	ASCIITEXT=""
	list_2=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
	list_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


	len_of_word=len(cipherText)

	for counter in range(len_of_word):
	    letter=cipherText[counter]

	    for total in range(len(list_1)):
	        if letter==list_1[total]:
	            ASCII=(list_2[total])
	            ASCIITEXT=ASCIITEXT+ASCII
	        elif letter==" ":
	            ASCIITEXT=ASCIITEXT+" "
	            break
	        



	text=(ASCIITEXT)
	Text_to_be_included.append(text)
	Input_File.close()


def Morse_Code_INTO_ASCII():
	LENGTH=len(Read_File)
	String_Remove_Morse=Read_File[11:LENGTH]
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


Temp_List=args.split('./')
Length_of_List=len(Temp_List)
Locations_List=Temp_List[1:Length_of_List]


Final_Input_Location=""
Temp_Location=Locations_List[0]
for i in range(len(Temp_Location)):
    letter=Temp_Location[i]
    if letter.isspace():
        Final_Input_Location=Final_Input_Location
    else:
        Final_Input_Location=Final_Input_Location+letter


Input_Location="/"+Final_Input_Location




Output_Folder=Locations_List[1]
Output_Location="/"+Locations_List[1]


all_files = os.listdir(Input_Location)



Output_Files_List=[]
Text_to_be_included=[]


for counter in range(len(all_files)):
    file=Input_Location+"/"+str(all_files[counter])
    Input_File=open(file)
    len_of_name=len(all_files[counter])
    copy_text=len_of_name-4
    Output_file_name=all_files[counter][0:copy_text]
    Output_file_name=Output_Location+"/"+Output_file_name+"_u63378mr.txt"
    Output_Files_List.append(Output_file_name)

    
    Read_File=Input_File.read()
    LENGTH=len(Read_File)


    if Read_File[0]=='H' or Read_File[0]=='h':
    	Hex_INTO_ASCII()

    elif Read_File[0]=='C' or Read_File[0]=='c':
    	Caeser_Cipher_INTO_ASCII()

    elif Read_File[0]=='M' or Read_File[0]=='m':
    	Morse_Code_INTO_ASCII()


for i in range(len(Output_Files_List)):
    file_name=Output_Files_List[i]
    Open_file=open(file_name,'w')
    input_text=Text_to_be_included[i]
    Open_file.write(input_text)
    Open_file.close()
