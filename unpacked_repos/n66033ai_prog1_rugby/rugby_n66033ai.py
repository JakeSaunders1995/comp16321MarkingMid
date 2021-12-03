import os, argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	for file in os.listdir(args.input):
		filepath = os.path.join(args.input, file)
		scores = extractData(filepath)
		separatedScores = []
		t1 = 0
		t2 = 0
		for i in range(len(scores) // 3):
			separatedScores.append(scores[i*3:(i+1)*3])
		# end for
		for i in range(len(separatedScores)):
			if separatedScores[i][1] == '1':
				if separatedScores[i][2] == 't':
					t1 += 5
				elif separatedScores[i][2] == 'c':
					t1 += 2
				elif separatedScores[i][2] == 'p':
					t1 += 3
				elif separatedScores[i][2] == 'd':
					t1 += 3
				# end if
			else:
				if separatedScores[i][2] == 't':
					t2 += 5
				elif separatedScores[i][2] == 'c':
					t2 += 2
				elif separatedScores[i][2] == 'p':
					t2 += 3
				elif separatedScores[i][2] == 'd':
					t2 += 3
				# end if
			# end if
		# end for
		if t1 > t2:
			print("Team 1 wins!")
		elif t2 > t1:
			print("Team 2 wins!")
		else:
			print("It's a draw!?")
		result = outputName(file)
		result = os.path.join(args.output, result)
		f = open(result, 'w')
		f.write(str(t1) + ':' + str(t2))
		f.close()
	# end for
# end def

def extractData(file):
	f = open(file, 'r')
	scores = f.read()
	f.close()
	return scores
# end def

def outputName(file):
	firstHalf = file[:-4]
	output = firstHalf + "_n66033ai.txt"
	return output
# end def

main()
