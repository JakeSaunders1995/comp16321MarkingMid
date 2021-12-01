import os,sys

#function for error message when the arguments are not right
def print_help_and_exit():
    print("Usage: " + sys.argv[0] + " [input folder] [output folder]")
    sys.exit(0)

#main code for calculation
def rugbycode(input_folder, output_folder, filename):
	one=[]
	two=[]
	f1=open(input_folder + filename,"r")
	f2=open(output_folder + filename.replace(".txt","_p98424rp.txt"),"w")
	word=f1.read()
	i=1
	while i<len(word):
		if word[i]=="1":
			one.append(word[i+1])
		elif word[i]=="2":
			two.append(word[i+1])
		i+=3

	sumone=0
	sumtwo=0
	for i in one:
		if i=="t":
			sumone+=5
		elif i=="c":
			sumone+=2
		elif i=="p":
			sumone+=3
		elif i=="d":
			sumone+=3

	for j in two:
		if j=="t":
			sumtwo+=5
		elif j=="c":
			sumtwo+=2
		elif j=="p":
			sumtwo+=3
		elif j=="d":
			sumtwo+=3

	a=str(sumone)+":"+str(sumtwo)
	f2.write(a)

	f2.close()
	f1.close()

#checks number of arguments
if(len(sys.argv) != 3):
    print("ERROR: incorrect number of arguments")
    print_help_and_exit()

#get the files
input_folder_string = sys.argv[1]
output_folder_string = sys.argv[2]

#gets the list of files in the given directory
dire=os.listdir(input_folder_string)

#skims through files only if it is a text file and executes the calculation part
for file in dire:
	if ".txt" in file:
		rugbycode(input_folder_string, output_folder_string, file)





