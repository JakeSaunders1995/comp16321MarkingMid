import sys
import os

for file1 in sorted(os.listdir(sys.argv[1])):
	file = open(os.path.join(sys.argv[1], file1), 'r')
	readFile = file.read()
	T1 = 0
	T2 = 0
	for i in range (len(readFile)): 
		if (readFile[i]=="1"):
			if (readFile[i+1]=="t"):
				T1 += 5
			elif (readFile[i+1]=="c"):
				T1 += 2
			elif (readFile[i+1]=="p"):
				T1 += 3
			elif (readFile[i+1]=="d"):
				T1 += 3
		elif (readFile[i]=="2"):
			if (readFile[i+1]=="t"):
				T2 += 5
			elif (readFile[i+1]=="c"):
				T2 += 2
			elif (readFile[i+1]=="p"):
				T2 += 3
			elif (readFile[i+1]=="d"):
				T2 += 3
		newOutputFile = open(os.path.join(sys.argv[2], file1[:-4] +'_h60953dl.txt'), 'w')
		newOutputFile.write(str(T1) + ":" + str(T2))
		newOutputFile.close()
