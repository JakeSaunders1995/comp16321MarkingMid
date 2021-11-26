import sys
import os

folderInput = sys.argv[1]
folderOutput = sys.argv[2]





for folder in os.listdir(folderInput):
	
	files = os.path.join(folderInput, folder)
	if os.path.isfile(files):

		fileRead = open(files, 'r')

		fileName = os.path.basename(files)

		shortfileName = os.path.splitext(fileName)[0]

		if os.path.isdir(folderOutput):
			dirName = os.path.join(folderOutput, shortfileName + '_m83653ns.txt')
			
		
			data = fileRead.read()
			T1_Try_Count = data.count("1t")
			T2_Try_Count = data.count("2t")
			T1_C_Count = data.count("1c")
			T2_C_Count = data.count("2c")
			T1_P_Count = data.count("1p")
			T2_P_Count = data.count("2p")
			T1_D_Count = data.count("1d")
			T2_D_Count = data.count("2d")


			T1_Score = (T1_Try_Count * 5) + (T1_C_Count * 2) + (T1_P_Count * 3) + (T1_D_Count * 3)
			T2_Score = (T2_Try_Count * 5) + (T2_C_Count * 2) + (T2_P_Count * 3) + (T2_D_Count * 3)
			with open(dirName, 'a+') as fileNew:
				fileNew.write(str(T1_Score) + ":" + str(T2_Score))
		else:
			os.mkdir(folderOutput)