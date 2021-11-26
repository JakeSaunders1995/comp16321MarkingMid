import sys
import os

file_paths = sys.argv

input_path = file_paths[1]
output_path = file_paths[2]

os.chdir(input_path)
files_in_directory = os.listdir()


def rugby(input_file_string):
    os.chdir(input_path)

    teams_total = {
        "1": 0,
        "2": 0
    }

    input_file = open(input_file_string, "r")
    file_contents = input_file.read()

    score_board = [
        file_contents[curr: curr + 3]
        for curr in range(0, len(file_contents), 3)
    ]

    print(score_board)

    scoring_types = {
        "t": 5,
        "c": 2,
        "p": 3,
        "d": 3
    }

    for score in score_board:
        teams_total[score[1]] += scoring_types[score[2]]

    winning_score = max(teams_total.values())
    winning_team = []

    for team, final_score in teams_total.items():
        if final_score == winning_score:
            winning_team.append(team)

    if len(winning_team) > 1:
        print("THERE HAS BEEN A DRAW! ({} POINTS)".format(winning_score))
    else:
        print("TEAM {} HAS WON WITH {} POINTS!".format(winning_team[0], winning_score))

    output_score = str(teams_total["1"]) + ":" + str(teams_total["2"])

    os.chdir(output_path)
    output_file_name = input_file_string.replace(".txt", "") + "_m59511md.txt"
    output_file = open(output_file_name, "w")
    output_file.write(output_score)


for file in files_in_directory:
    rugby(file)
