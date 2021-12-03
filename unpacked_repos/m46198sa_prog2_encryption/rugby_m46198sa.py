import argparse,os

def rugby(file):
	result = ""
	team1_scores = []
	team2_scores = []
	n = 3

	score = [file[i:i+n] for i in range(0, len(file),n) ]


	for i in range(len(score)):
		if score[i] == 'T1p' or score[i] == 'T1d' or score[i] == 'T1t' or score[i] == 'T1c':
			team1_scores.append(score[i])
		else :
			team2_scores.append(score[i])

	for i in range(len(team1_scores)):
		if team1_scores[i] == 'T1p':
			team1_scores[i] = 3
		if team1_scores[i] == 'T1d':
			team1_scores[i] = 3
		if team1_scores[i] == 'T1t':
			team1_scores[i] = 5
		if team1_scores[i] == 'T1c':
			team1_scores[i] = 2

	for i in range(len(team2_scores)):
		if team2_scores[i] == 'T2p':
			team2_scores[i] = 3
		if team2_scores[i] == 'T2d':
			team2_scores[i] = 3
		if team2_scores[i] == 'T2t':
			team2_scores[i] = 5
		if team2_scores[i] == 'T2c':
			team2_scores[i] = 2
	print(team2_scores)
	print(team1_scores)

	final_team1_score = sum(team1_scores)
	final_team2_score = sum(team2_scores)

	if final_team1_score > final_team2_score :
		print("Team 1 is the winner !")
		result =  f'{final_team1_score}:{final_team2_score}'
	if final_team2_score > final_team1_score :
		print("Team 2 is the winner !")
		result =  f'{final_team1_score}:{final_team2_score}'
	elif final_team1_score == final_team2_score: 
		print("It's a draw !")
		result = f'{final_team1_score}:{final_team2_score}'

	print(team1_scores)
	print(team2_scores)
	return result

parser = argparse.ArgumentParser(description = "rugby scores")
parser.add_argument('input', help='the input directory')
parser.add_argument('output', help='the output directory')
args = parser.parse_args()


path = args.input
path_output = args.output

for file in os.listdir(path):
	with open(path+"/"+file, 'r') as f:
		with open(path_output + "/" + file.replace(".txt","_m46198.txt"),"w") as n:
			n.write(rugby(f.read()))
			