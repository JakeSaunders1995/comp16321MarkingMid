import argparse
import os
import re

#Arguments
parser = argparse.ArgumentParser(description = "Input and Output to folders specified")
parser.add_argument("input", type = str, help = "Input folder path")
parser.add_argument("output", type = str, help = "Output folder path")
args = parser.parse_args()

#Functions
def CheckInput():
	exists = os.path.isdir(args.input)
	if exists == False:
		print("The specified input folder does not exist")
		exit()
	else:
		return

def CheckOutput():
	exists = os.path.isdir(args.output)
	if exists == False:
		os.mkdir(args.output)
	else:
		return

def GetScores():
	opendir = str(args.input) + "/" + str(inputlist[file])
	if str(inputlist[file]).endswith(".txt"):
		f = open(opendir)
		scores = f.read()
	else:
		scores = "voidFile"
		print('\nIncompatible file type found:', inputlist[file], '\nAll files in input folder that do not end in ".txt" will be skipped.\n')
	return scores

def DisplayWinners():
	if team1 > team2:
		print("In", inputlist[file],"The winning team is Team 1")
	elif team2 > team1:
		print("In", inputlist[file],"The winning team is Team 2")
	elif team1 == team2:
		print("In", inputlist[file],"Team 1 and Team 2 have drawn")

def OutputScores():
	opendir = str(args.output) + "/" + str(inputlist[file].rstrip(".txt")) + "_y62498rh.txt"
	g = open(opendir, "w")
	finalscore = str(team1) + ":" + str(team2)
	g.write(finalscore)

#Logic
CheckInput()
CheckOutput()
inputlist = os.listdir(args.input)
for file in range (0, len(inputlist)):
	scores = GetScores()
	if scores == "voidFile":
		continue
	scorenumber = len(scores) / 3
	team1, team2, t, s = 0, 0, 1, 2
	for x in range(0, int(scorenumber)):
		if scores[t] == "1":
			if scores[s] == "t":
				team1 += 5
			elif scores[s] == "c":
				team1 += 2
			elif scores[s] == "p" or scores[s] == "d":
				team1 += 3
			else:
				print("\n")
				print(inputlist[file], "is not of correct format, reuslt may be incorrect")
				break

		elif scores[t] == "2":
			if scores[s] == "t":
				team2 += 5
			elif scores[s] == "c":
				team2 += 2
			elif scores[s] == "p" or scores[s] == "d":
				team2 += 3
			else:
				print("\n")
				print(inputlist[file], "is not of correct format, reuslt may be incorrect")
				break
		else:
			print("\n")
			print(inputlist[file], "is not of correct format, reuslt may be incorrect")
			break
		t += 3
		s += 3
	DisplayWinners()
	OutputScores()