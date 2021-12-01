import sys, os, argparse



# handle input arguments
if len(sys.argv) == 3:

	inputDirectory = sys.argv[1]
	outputDirectory = sys.argv[2]

    #print(inputDirectory)
	for currentFileName in os.listdir(inputDirectory):
        #print(currentFileName)		
        
		with open(inputDirectory + "/" + currentFileName, 'r') as f:
            
            # step 1 - READ CURRENT FILE
			currentFileContents = f.read()
			print(currentFileContents)
			f.close()

            # step 2 - DO LOGIC 
			length = len(currentFileContents)
			i = 2
			y = 1

			scoreT1 = 0
			scoreT2 = 0

			while i <= length:
				if currentFileContents[y] == "1":
					if currentFileContents[i] == "t":
						scoreT1 += 5
					elif currentFileContents[i] == "c":
						scoreT1 += 2
					elif currentFileContents[i] == "p" or currentFileContents[i] == "d":
						scoreT1 += 3
				else:
					if currentFileContents[i] == "t":
						scoreT2 += 5
					elif currentFileContents[i] == "c":
						scoreT2 += 2
					elif currentFileContents[i] == "p" or currentFileContents[i] == "d":
						scoreT2 += 3
				i = i + 3
				y = y + 3
			print(str(scoreT1)+":"+str(scoreT2))

			# step 3 - CREATING OUTPUT FILEPATH AND FILENAME
			fileSplitArray = os.path.splitext(currentFileName)
			currentOutputFileName = outputDirectory + "/" + fileSplitArray[0] + "_n86729dg" + fileSplitArray[1]
			#print(currentOutputFileName)

			# step 4 - WRITE CONTENTS ON OUTPUT FILE
			currentFileWriter = open(currentOutputFileName, "w")
			currentFileWriter.write(str(scoreT1)+":"+str(scoreT2))
			currentFileWriter.close()
else:
	print("Invalid parameters error. Expected: python3 rugby_n86739dg.py ./[input folder] ./[output folder]")
