import os, sys

t, c, p, d = 5, 2, 3, 3
contentInDir = []
for element in os.listdir(sys.argv[1]):
	contentInDir.append(os.path.join(sys.argv[1],element))
files = list(filter(os.path.isfile, contentInDir))
for eachFile in files:
	file = open(eachFile,"r")
	T1_scores = 0
	T2_scores = 0
	scores = file.read()
	for a in range(0, len(scores)):
		while scores[a] == '1' or scores[a] == '2':
			globals()["T" + str(scores[a]) +"_scores"] += globals()[scores[a+1].lower()]
			break
	file.close()
	winner =""
	if (T1_scores > T2_scores):
		winner = "T1"
	elif (T1_scores < T2_scores):
		winner = "T2"
	else:
		winner = "draw"
	print(winner)
	output_file = open(os.path.join(sys.argv[2], eachFile[0 -(len(eachFile) - len(sys.argv[1]) - 1):-4] + "_y02478jh.txt"), "w")
	output_file.write(str(T1_scores) + ':' + str(T2_scores))
	output_file.close()