import argparse, os


parser = argparse.ArgumentParser()
parser.add_argument("input_directory")
parser.add_argument("output_directory")
args = parser.parse_args()
input_files = os.listdir(args.input_directory)


for filename in input_files:
    input_file = open(os.path.join(args.input_directory, filename), "r")
    team_1 = 0
    team_2 = 0
    string_of_scores = (input_file.readlines()[0])
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
    if team_1 > team_2:
        print("team 1 won")
    elif team_1 == team_2:
        print("the teams drew")
    else:
        print("team 2 won")
    filename = filename[:-4] + "_x47813as.txt"
    output_file = open(os.path.join(args.output_directory, filename), "x")
    output_file.write(ratio)
    output_file.close
    input_file.close
