import argparse
import os
def parser():
	parser = argparse.ArgumentParser()
	parser.add_argument('input' , type = str, help = "Your input folder path to be processed.")
	parser.add_argument('output' , type = str, help = "The output folder path where the processed data will be stored in.")
	args = parser.parse_args()
	return args.input, args.output

def main():
	scores_list = []
	team1 , team2 = 0, 0
	score_values = {'t':5,
	'c': 2,
	'p':3,
	'd':3
	}
	inputFolder , outputFolder = parser()
	txt_arr = sorted([x for x in os.listdir(inputFolder) if x.endswith(".txt")])
	for inputFile in txt_arr:
		
		with open (os.path.join(inputFolder,inputFile),'r') as data:
			data = data.read()
		for i in range(3,len(data)+3,3):
			scores_list.append(data[i-3:i])
		for score in scores_list:
			score_v = score_values[score[2]]
			if score[1] == '1':
				team1+=score_v
			elif score[1] == '2':
				team2+=score_v
		if team1 >  team2: print("Team 1 Win")
		elif team2 > team1: print("Team 2 Win")
		else: print("Draw!")

		with open (os.path.join(outputFolder,inputFile.split(".")[0]+"_x62165ih.txt"),'w') as out:
			out.write("{}:{}".format(team1,team2))
		scores_list = []
		team1 , team2 = 0, 0
if __name__ == '__main__':
	main()
