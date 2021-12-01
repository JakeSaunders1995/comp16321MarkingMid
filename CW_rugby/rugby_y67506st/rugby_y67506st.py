import argparse
import os

# argparse
parser = argparse.ArgumentParser(description="rugby game")
parser.add_argument('rugbyIndir', type=str, help='Input dir for rugby')
parser.add_argument('rugbyOutdir', type=str, help='Output dir for rugby')

args, unknown = parser.parse_known_args()

path = os.path.abspath(args.rugbyIndir)
outputPath = os.path.abspath(args.rugbyOutdir)

for filename in os.listdir(path):
	if filename.endswith(".txt"):
		f = open(os.path.join(path, filename), 'r')
		score = f.read()
		# print(score)

		x = filename.replace(".txt","_y67506st.txt")
		outputFolder = os.path.join(outputPath, x)

		# list comprehension
		n = 3
		points = [(score[i:i+n]) for i in range(0, len(score), n)]

		Team1Sort= filter(lambda sepoint: sepoint[:2] == "T1", points)
		Team2Sort= filter(lambda sepoint: sepoint[:2] == "T2", points)

		Team1 = list(Team1Sort)
		Team2 = list(Team2Sort)

		# Extract the last character for every term
		Team1 = [x[-1:] for x in Team1]
		Team2 = [y[-1:] for y in Team2]

		# Convert last character to the score types for Team 1
		for i in range(len(Team1)):
			if  Team1[i] == 't':
				Team1[i] = 5
			elif Team1[i] == 'c':
				Team1 [i] = 2
			elif Team1[i] == 'p':
				Team1[i] = 3
			elif Team1[i] == 'd':
				Team1[i] = 3
		Team1F = sum(Team1)

		# Convert last character to the score types for Team 2
		for n in range(len(Team2)):
			if  Team2[n] == 't':
				Team2[n] = 5
			elif Team2[n] == 'c':
				Team2[n] = 2
			elif Team2[n] == 'p':
				Team2[n] = 3
			elif Team2[n] == 'd':
				Team2[n] = 3
		Team2F = sum(Team2)

		f = open(outputFolder, 'w')
		f.write(str(Team1F)+ ":"+ str(Team2F))
		f.close()