import argparse
import os

def pointcalc(y):
	if line[y+1] == "t":
		p = 5
	elif line[y+1] == "c":
	 	p = 2
	elif line[y+1] == "p":
		p = 3
	elif line[y+1] == "d":
		p = 3
	return p

parser = argparse.ArgumentParser() 	# initialing parser
parser.add_argument('inputFolder') 	# inputting input folder from command line
parser.add_argument('outputFolder') 
folders = parser.parse_args() 		# passing the parameters

inputpath = folders.inputFolder
outputpath = folders.outputFolder	
inputDir = os.listdir(inputpath) # stores the list of files in the input folder to inputDir
outputDir = os.listdir(outputpath)

for inputfilename in inputDir:	
	inputtext = os.path.join(inputpath,inputfilename) # creating the path of the input file
	team1score = 0
	team2score = 0
	if os.path.isfile(inputtext) and inputfilename.endswith(".txt"):
		with open(inputtext) as inputfile:
			line = inputfile.readline()
			line = line.strip()
			for pos in range (len(line)):
				if line[pos] == "1":
					point = pointcalc(pos)
					team1score += point
				elif line[pos] == "2":
					point = pointcalc(pos)
					team2score += point

		score = str(team1score) + ":" + str(team2score)
		outputfilename = inputfilename.replace('.txt', "") + "_p75341vk.txt" # creating the output file name from the input file name
		outputtext = os.path.join(outputpath,outputfilename) # creating the path of the output file

		if (outputfilename not in outputDir): # to check if the file is present or not
			outputfile = open(outputtext, "x") # create file, if not present
		else:
			outputfile = open(outputtext, "w") # write to existing file, if present

		outputfile.write(score)
		outputfile.close()
		inputfile.close()
