import sys

InputFolder = sys.argv[1] + "/test_file1.txt"
OutputFolder = sys.argv[2] + "/rugbyOutput.txt"

readFile = open(InputFolder, "r")

fileTextRaw = readFile.readlines()
input = ""
for a in fileTextRaw:
	input = input + a
pass


split_input = []
for index in range(0, len(input), 3):
    split_input.append(input[index : index + 3])
T1 = 0
T2 = 0
t = 5
c = 2
p = 3
d = 3
for i in split_input:
	if(i[1] == "1"):
		if(i[2] == "t"):
			T1 = T1 + t
		elif(i[2] == "c"):
			T1 = T1 + c
		elif(i[2] == "p"):
			T1 = T1 + p 
		elif(i[2] == "d"):
			T1 = T1 + d 	
	if(i[1] == "2"):
		if(i[2] == "t"):
			T2 = T2 + t
		elif(i[2] == "c"):
			T2 = T2 + c
		elif(i[2] == "p"):
			T2 = T2 + p 
		elif(i[2] == "d"):
			T2 = T2 + d 
newFile = open(OutputFolder, "w")
newFile.write(str(T1) + ":" + str(T2))
newFile.close()