import os
import sys
import re

input_folder = sys.argv[1]
output_folder = sys.argv[2]
dir_list = os.listdir(input_folder)
print(dir_list)

def upptolower():
	count = 0
	newlist = ''
	for a in list1:
		if a.isupper() == True:
			count += 1
			newlist += (a.lower())
		else:
			newlist += a	
	print("\nNumber of upper case letters chenged: ",count)
	pat = '[0-9]'
	numbers = "123456789"
	newlist1 = ""
	count1 = 0
	for j in list1:
		if j not in numbers:
			newlist1 = newlist1
		else:
			newlist1 = re.sub(pat, '', list1)
			count1 = count1 + 1
	print ("\nNumber of numbers removed: ",count1)
	count2 = 0
	punctuations = """?-'"\,{}<>./!()[]@#$%^;:&*_~"""
	newlist1 = ""
	for x in list1:
		if x not in punctuations:
			newlist1 = newlist1 + x
		else: 
			count2 = count2 + 1
	print("\nNumber of punctuations removed: ", count2)

	output_file = dir_list[i].replace("txt","_p01679ma.txt")
	output_file=output_folder+"/"+output_file
	with open (output_file, "a")as file:
		file.write(f'\nNumber of upper case letters chenged:{count}')
		file.write(f'\nNumber of numbers removed: ,{count1}')
		file.write(f'\nNumber of punctuations removed, {count2}')




i=0

for i in range (i, len(dir_list),1):
	file = open(input_folder +"/"+ dir_list[i])
	print("\n")
	list1=file.readline()
	upptolower()
	