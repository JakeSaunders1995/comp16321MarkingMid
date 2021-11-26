scoreTypes = []
T1scores = []
T2scores = []
T1 = 0
T2 = 0

inputFileName = input("Please enter the name of the input file including the extension: ")




inputFile = open(inputFileName, "r")
for x in inputFile:
	scoreTypes.append(x)


	for char in scoreTypes:
		length = len(char)
		noOfChars = length - 1
		
		for y in range(0, noOfChars):

			if (char[y] == str("1")):
				T1scores.append(char[y+1])
				#print("T1: "+ str(T1scores))
			elif (char[y] == str("2")):
				T2scores.append(char[y+1])
				#print("T2: " + str(T2scores))
				continue 
			continue
		continue 
		inputFile.close()
#print(T1scores)
#print(T2scores)

for z in T1scores:
	if (z == "c"):
		T1 += 2
	elif (z == "t"):
		T1 += 5
	elif (z == "p"):
		T1 += 3
	elif(z == "d"):
		T1 += 3
	else:
		continue
print("Team 1 scores: " + str(T1))

for z in T2scores:
	if (z == "c"):
		T2 += 2
	elif (z == "t"):
		T2 += 5
	elif (z == "p"):
		T2 += 3
	elif(z == "d"):
		T2 += 3
	else:
		continue
print("Team 2 scores: " + str(T2))

if (T1 > T2):
	print("Team 1 wins!")
elif(T1 == T2):
	print("It's a draw!")
elif(T2 > T1):
	print("Team 2 wins!")

outputFileName = input("Please enter the name of the output file including the extension: ")


outputFile = open(outputFileName, "w")
outputFile.write(str(T1)+":"+str(T2))
outputFile.close()