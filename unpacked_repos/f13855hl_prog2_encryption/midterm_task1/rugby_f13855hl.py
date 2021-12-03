import os

settings = open("test_file5.txt")
score = settings.readline()

T1 = 0
T2 = 0

i = 0

while i < len(score):
	if "T1t" in score[i:i+3]:
		T1 = T1 + 5
	elif "T1c" in score[i:i+3]:
		T1 = T1 + 2
	elif "T1p" in score[i:i+3]:
		T1 = T1 + 3
	elif "T1d" in score[i:i+3]:
		T1 = T1 + 3
	elif "T2t" in score[i:i+3]:
		T2 = T2 + 5
	elif "T2c" in score[i:i+3]:
		T2 = T2 + 2
	elif "T2p" in score[i:i+3]:
		T2 = T2 + 3
	elif "T2d" in score[i:i+3]:
		T2 = T2 + 3
	i = i + 3

outputFile = open("test_file5_f13855hl.txt", "w")
outputFile.write(str(T1) + ":" + str(T2))
outputFile.close()