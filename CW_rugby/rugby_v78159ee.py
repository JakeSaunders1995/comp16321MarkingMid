import os
import sys #takes command line arguments and passes it through the code

inputfolder = sys.argv[1]
outputfolder = sys.argv[2]

for filename in os.listdir(inputfolder):
	f = os.path.join(inputfolder, filename)
	if os.path.isfile(f):
		inputfile = open(f)
		contents = inputfile.read()
		
		c = 0
		T1 = 0
		T2 = 0
		
		while c < len(contents):
			if contents[c] == "1":
				if contents[c+1] == "t":
					T1 = T1 + 5
				elif contents[c+1] == "c":
					T1 = T1 + 2 
				elif contents[c+1] == "p":
					T1 = T1 + 3
				elif contents[c+1] == "d":
					T1 = T1 + 3
			elif contents[c] == "2":
				if contents[c+1] == "t":
					T2 = T2 + 5
				elif contents[c+1] == "c":
					T2 = T2 + 2 
				elif contents[c+1] == "p":
					T2 = T2 + 3
				elif contents[c+1] == "d":
					T2 = T2 + 3
			c += 1
		if T1 > T2:
			print("Team 1 Wins")
		if T2 > T1:
			print("Team 2 wins")
		if T1 == T2:
			print("Its a draw")
			
		output = filename[:-4] + "_v78159ee.txt"
		folderpath = os.path.join(outputfolder, output) #gets the path for the output folder
		output_file = open(folderpath, "w")
		output_file.write(str(T1) + ":" + str(T2))
        
		
		
		
			
						
			
				
		
