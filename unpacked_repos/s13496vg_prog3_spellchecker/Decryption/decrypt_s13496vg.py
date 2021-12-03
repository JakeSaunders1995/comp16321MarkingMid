
def hex_ASCII():
	length=len(Read_File)



	rem=Read_File[4:length]
	List_File=rem.split()

	length_of_list=len(List_File)


	final=""

	for count in range(length_of_list):
		el=str(List_File[count])
		conbyte=bytes.fromhex(el)
		Byte_To_ASCII=conbyte.decode("ASCII")
		final=final+Byte_To_ASCII

	text=(final.lower())
	texfin.append(text)
	Input_File.close()


def Caeser_ASCII():
	length=len(Read_File)
	cipherText=Read_File[18:length]
	lens=len(cipherText)


	ASCIITEXT=""
	list_2=["x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w"]
	list_1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


	lenw=len(cipherText)

	for counter in range(lenw):
	    letter=cipherText[counter]

	    for total in range(len(list_1)):
	        if letter==list_1[total]:
	            ASCII=(list_2[total])
	            ASCIITEXT=ASCIITEXT+ASCII
	        elif letter==" ":
	            ASCIITEXT=ASCIITEXT+" "
	            break
	        



	text=(ASCIITEXT)
	texfin.append(text)
	Input_File.close()


def Morse_ASCII():
	length=len(Read_File)
	remmorse=Read_File[11:length]
	List_File=remmorse.split()

	input = [ '.-','-...','-.-.','-..','.','..-.','--.','....',
	                    '..','.---','-.-','.-..','--','-.','---','.--.','--.-',
	                    '.-.','...','-','..-','...-','.--','-..-','-.--','--..',
	                    '.----','..---','...--','....-','.....','-....','--...',
	                    '---..','----.','-----','.-.-.-', '..--..','-.-.--','--..--','---...','-.-.-.','-....-','-.--.','-.--.-','-.--.','-.--.-','.----.','.-..-.','.-.-.- .-.-.- .-.-.-']
	ASCII_OUTPUT=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0",'.','?','!',',',':',';','-','[',']','(',')'," ' ",' " ','...']
	length_of_list=len(List_File)

	asciifout=""

	for i in range(length_of_list):
		character=List_File[i]
		for count in range(len(input)):
			if character==input[count]:
				string_letter=str(ASCII_OUTPUT[count])
				asciifout=asciifout+string_letter
			elif character=='/':
				asciifout=asciifout+" "
				break

	text=(asciifout.lower())
	texfin.append(text)
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
length_of_List=len(Temp_List)
Locations_List=Temp_List[1:length_of_List]


asciifout=""
Temp_Location=Locations_List[0]
for i in range(len(Temp_Location)):
    letter=Temp_Location[i]
    if letter.isspace():
        asciifout=asciifout
    else:
        asciifout=asciifout+letter


Input_Location="/"+asciifout




Output_Folder=Locations_List[1]
Output_Location="/"+Locations_List[1]


all_files = os.listdir(Input_Location)



Output_Files_List=[]
texfin=[]


for counter in range(len(all_files)):
    file=Input_Location+"/"+str(all_files[counter])
    Input_File=open(file)
    len_of_name=len(all_files[counter])
    copy_text=len_of_name-4
    Output_file_name=all_files[counter][0:copy_text]
    Output_file_name=Output_Location+"/"+Output_file_name+"_s13496vg.txt"
    Output_Files_List.append(Output_file_name)

    
    Read_File=Input_File.read()
    length=len(Read_File)


    if Read_File[0]=='H' or Read_File[0]=='h':
    	hex_ASCII()

    elif Read_File[0]=='C' or Read_File[0]=='c':
    	Caeser_ASCII()

    elif Read_File[0]=='M' or Read_File[0]=='m':
    	Morse_ASCII()


for i in range(len(Output_Files_List)):
    file_name=Output_Files_List[i]
    Open_file=open(file_name,'w')
    input_text=texfin[i]
    Open_file.write(input_text)
    Open_file.close()
