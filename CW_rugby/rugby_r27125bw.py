import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()



for f in os.listdir(args.input):
    file = open(args.input + "/" + f, "r")
    text = file.read()

    file.close()

    team1_score = 0
    team2_score = 0

    events = text.split('T')[1:]

    def return_points(event):
        if event == "t":
            return 5
        elif event == "c":
            return 2
        elif event == "p" or event == "d":
            return 3
        else:
            return 0

    for event in events:
        if event[0] == "1":
            team1_score += return_points(event[1])
        elif event[0] == "2":
            team2_score += return_points(event[1])


    file_write = open(args.output + "/" + f[:-4] + "_r27125bw.txt", "w")
    file_write.write(f"{team1_score}:{team2_score}")
    file_write.close()
