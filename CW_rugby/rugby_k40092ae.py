import os
import argparse
parser = argparse.ArgumentParser()

#parser.add_argument("readme", help="rugby scoring program")

parser.add_argument('input_folder_path')
parser.add_argument('output_folder_path')

args = parser.parse_args()

inputfolpath = (args.input_folder_path)
outputfolpath = (args.output_folder_path)


def calcpoint(symbol):
		if symbol == "t":
			return 5
		elif symbol == "c":
			return 2
		elif symbol == "p":
			return 3
		elif symbol == "d":
			return 3

for filename in os.listdir(inputfolpath):
	inputfile = open(inputfolpath + "/" + filename,"r")
	temp = filename.split(".")
	username = 'k40092ae'
	
	output_file_name = temp[0] +"_"+ username + "." + temp[1] 
	line = inputfile.readline()
	biglist = list(line)

	team1scr = 0
	team2scr = 0

	for j in range(len(biglist)):
		if biglist[j-1] == "1" and j != 0:
			team1scr = team1scr + calcpoint(biglist[j])
		elif biglist[j-1] == "2" and j != 0:
			team2scr = team2scr + calcpoint(biglist[j])


	finalstring = str(team1scr) +":" + str(team2scr)
	outputfile = open(outputfolpath+ "/" + output_file_name,"w")
	outputfile.write(finalstring)
