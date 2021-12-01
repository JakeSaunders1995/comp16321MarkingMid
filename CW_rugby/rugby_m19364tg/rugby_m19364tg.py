import os
import argparse
import re

def readArg():
	#Read Argument from Terminal
	parse = argparse.ArgumentParser()
	parse.add_argument("FileInput", help="Text Input File Path")
	parse.add_argument("FileOutput", help="Text Output File Path")

	ArgReader = parse.parse_args()
	return ArgReader.FileInput, ArgReader.FileOutput

def readFile(path):
	previousPath = os.getcwd()
	os.chdir(path)
	files = os.listdir()
	FileNames = []
	pattern = re.compile(r"^.*.txt$")
	for x in files:
		#print(x)
		if (pattern.search(x)):
			FileNames.append(x)
	os.chdir(previousPath)
	return FileNames

#Calculate the score for each team [Input Text, Team to Calculate Points for]
def DeterminePoint(FileInput, TeamNumber):
	counter = 0
	for x in range(0, len(FileInput)):
		if (FileInput[x] == "T"):
			if (FileInput[x+1] == str(TeamNumber)):
				if (FileInput[x+2] == "t"):
					counter = counter + 5
				elif (FileInput[x+2] == "c"):
					counter = counter + 2
				elif (FileInput[x+2] == "p"):
					counter = counter + 3
				elif (FileInput[x+2] == "d"):
					counter = counter + 3
				else:
					continue
			else:
				continue
		else:
			continue
	return counter


#Read Argument from Terminal
FileInputLocation, FileOutputLocation = readArg()



FileNames = readFile(FileInputLocation)

if (FileInputLocation[len(FileInputLocation)-1 : len(FileInputLocation)] != "/"):
		FileInputLocation = FileInputLocation + "/"
if (FileOutputLocation[len(FileOutputLocation)-1 : len(FileOutputLocation)] != "/"):
	FileOutputLocation = FileOutputLocation + "/"

for x in FileNames:
	print("Results from: " + x)



	#Open file at both Input and Output Location
	FileToRead = str(str(FileInputLocation) + x)
	FileInputReader = open(FileToRead, "r")
	FileInput = FileInputReader.readline()

	#Adding University Username to Output File
	lastLetterLoc = int(len(x)) - 4
	FileWriteName = x [0: lastLetterLoc]
	FileWriteName = FileWriteName + "_m19364tg.txt"
	FileToWrite = str(str(str(FileOutputLocation) + FileWriteName))
	FileOutputWriter = open(FileToWrite, "w")

	#Calculate Points for both teams and compare
	Team1 = DeterminePoint(str(FileInput), 1)
	print("Team 1: " + str(Team1))
	Team2 = DeterminePoint(str(FileInput), 2)
	print("Team 2: " + str(Team2))

	if (Team1 < Team2):
		print("Team 2 Won")
	elif (Team2 < Team1):
		print ("Team 1 won")
	else:
		print("Both teams draw")

	#Write results to result folder and close files
	FileOutputWriter.write(str(Team1) + ":" + str(Team2))
	FileInputReader.close()
	FileOutputWriter.close()
