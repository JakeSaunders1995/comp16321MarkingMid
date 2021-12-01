# - Imports -
import sys
from os import listdir
from os.path import isfile, join

# - Global variables and inputs -
scoring = {'t': 5, 'c': 2, 'p': 3, 'd': 3}
input_folder = sys.argv[1]
test_files = [file for file in listdir(input_folder) if isfile(join(input_folder, file)) and file[0] != '.']



# - Main functions -
def print_winner(score_count):
	if score_count['T1'] > score_count['T2']: return "T1 WINS"
	elif score_count['T1'] < score_count['T2']: return "T2 WINS"
	else: return "DRAW"

def actions_adder(score_history, team_actions):
	# Recursion end condition:
	if len(score_history) == 0: return team_actions
	# Recursion instructions:
	actual_team = score_history[:2]
	team_actions[actual_team].append(score_history[2])
	# Recursion call:
	return actions_adder(score_history[3:], team_actions)

def score_counter(team_actions, scoring):
	score_count = {'T1': 0, 'T2': 0}
	for team in team_actions:
		score = sum([scoring[i] for i in team_actions[team]])
		score_count[team] = score
	print(print_winner(score_count))
	return f"{score_count['T1']}:{score_count['T2']}"



# - Outputs -
for file in test_files:
	input_file = open(f"{input_folder}/{file}")
	score_history = input_file.readline()

	team_actions = actions_adder(score_history, {'T1': [], 'T2': []})
	final_score = score_counter(team_actions, scoring)

	output_folder = sys.argv[2]
	output_file = open(f"{output_folder}/{file[:-4]}_n61655sb.txt", "w")
	output_file.write(final_score)

	input_file.close()
	output_file.close()

