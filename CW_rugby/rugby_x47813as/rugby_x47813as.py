import argparse

team_1 = 0
team_2 = 0

parser = argparse.ArgumentParser()
parser.add_argument("input_scores", type=argparse.FileType("r"))
parser.add_argument("output_ratio", type=argparse.FileType("a"))
args = parser.parse_args()

string_of_scores = (args.input_scores.readlines()[0])
for x in range (int((len(string_of_scores))/3)):
    points = 0
    if string_of_scores[(3*x)+2] == "t":
        points = 5
    elif string_of_scores[(3*x)+2] == "c":
        points = 2
    elif string_of_scores[(3*x)+2] == "p":
        points = 3
    else: # string_of_scores[(3*x)+2] == "d":
        points = 3
    if string_of_scores[(3*x)+1] == "1":
        team_1 = team_1 + points
    else:  # string_of_scores[(3*x)+1] == "2":
        team_2 = team_2 + points
print("team 1 score: " + str(team_1))
print("team 2 score: " + str(team_2))
ratio = str(team_1) + ":" + str(team_2)
print("final ratio T1:T2 is " + ratio)

args.output_ratio.write(ratio)

args.output_ratio.close()
args.input_scores.close()
