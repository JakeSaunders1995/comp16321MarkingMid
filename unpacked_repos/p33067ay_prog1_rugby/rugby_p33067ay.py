import argparse
import os

parser = argparse.ArgumentParser(description="Goals to scores")
parser.add_argument("goalfile", type=str, help="Input for the goals")
parser.add_argument("scoresfile", type=str, help="output for scores")
args = parser.parse_args()

goalfile = args.goalfile
scoresfile = args.scoresfile
for y in os.listdir(goalfile):
    store_directory = os.path.join(goalfile, y)
    file = open(store_directory, "r")

    team1_result = 0
    team2_result = 0
    input_string = file.readline()

    for x in range(len(input_string)):
        if (x % 3 == 1):
            team = int(input_string[x])
            if team == 1:
                goal = input_string[x + 1]
                if goal == "t":
                    team1_result = team1_result + 5
                elif goal == "c":
                    team1_result = team1_result + 2
                elif goal == "p":
                    team1_result = team1_result + 3
                elif goal == "d":
                    team1_result = team1_result + 3
                else:
                    print("Invalid!")
            elif team == 2:
                goal = input_string[x + 1]
                if goal == "t":
                    team2_result = team2_result + 5
                elif goal == "c":
                    team2_result = team2_result + 2
                elif goal == "p":
                    team2_result = team2_result + 3
                elif goal == "d":
                    team2_result = team2_result + 3
                else:
                    print("Something wrong!")
        else:
            continue

        if scoresfile[-1] != "/":
            outputfile = scoresfile + "/" + y.split(".txt")[0] + "_p33067ay"
            directory_create = os.path.dirname(outputfile)

        else:
            outputfile = scoresfile + y.split(".txt")[0] + "_p33067ay"
            directory_create = os.path.dirname(outputfile)

        if not os.path.exists(scoresfile):
            os.makedirs(scoresfile)


        final = open(outputfile, "w")
        final_score = str(team1_result)+":"+str(team2_result)
        final.write(str(final_score))

