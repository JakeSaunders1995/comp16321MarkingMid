import os, argparse, re
parser = argparse.ArgumentParser()
parser.add_argument('x', type = str)
parser.add_argument('y', type = str)
args = parser.parse_args()

def score_board_(file_111):

	file_output_ = file_111[0:(len(file_111) - 4)] + "_y48052as" + ".txt"
	file_output_ = args.y + file_output_
	file_111 = args.x + file_111
	file1 = open(file_111)
	file2 = open(file_output_, "w")



	'''s = file1.read()
	for i in range(3, len(s)):
		if(s[(i-1)] == 1):
			score += score_converter(s[i])
		else:
			score4 += score_converter(s[i])'''

	def score_converter(c1):
		if(c1 == "t"):
			return 5
		elif(c1 == "c"):
			return 2
		elif(c1 == "d"):
			return 3
		elif(c1 == "p"):
			return 3
		else:
			return ""


	s = file1.read()
	score, score4 = 0, 0
	for i in range(0, len(s) - 1):
		'''print(s[i].isdigit())'''
		if(s[i].isdigit()):
			if(int(s[i]) == 1):
				score = score + score_converter(s[(i + 1)])
				'''print(score)'''
			elif(int(s[i]) == 2):
				score4 = score4 + score_converter(s[(i + 1)])
				'''print(score4)'''
			else:
				continue
		else:
			continue

	score_final_ = str(score) + ":" + str(score4)
	file2.write(score_final_)
	file1.close()
	file2.close()


for file in os.listdir(args.x):
	score_board_(file)