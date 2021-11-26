import argparse
import os
t=5
c=2
p=3
d=3
t1_scoreName = []
t2_scoreName = []

def scoreAddition(team_score):
	score = 0
	for i in team_score:
		if i == "t":
			score += 5
		elif i == "c":
			score += 2
		elif i == "p":
			score += 3
		elif i == "d":
			score += 3
	return score

parser = argparse.ArgumentParser(description='put the file with the score')
parser.add_argument("input_file",type=str)
parser.add_argument("output_file",type=str)
args = parser.parse_args()
input_path = args.input_file
output_path = args.output_file

os.chdir(input_path)
files = os.listdir(input_path)
files.sort()
file_count = 1
for file in files:
	with open(file,"r") as f:
		content = f.readlines()
		f.close()
	scoreName = content[0]

	for index in range(len(scoreName)):
		if scoreName[index] == str(1):
			t1_scoreName.append(scoreName[index+1])
		elif scoreName[index] == str(2):
			t2_scoreName.append(scoreName[index+1])

	t1_score = scoreAddition(t1_scoreName)
	t2_score = scoreAddition(t2_scoreName)

	os.chdir(output_path)
	file_name = "test_file" + str(file_count) +"_v79907sy.txt"
	with open(file_name, "w") as f1:
		f1.write(str(t1_score) + ":" + str(t2_score))
		f1.close()
	file_count += 1
	t1_score = 0
	t2_score = 0
	t1_scoreName = []
	t2_scoreName = []
	os.chdir(input_path)