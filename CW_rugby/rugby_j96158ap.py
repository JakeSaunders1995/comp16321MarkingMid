import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Enter input file")
    parser.add_argument("output_file", help="Enter output file")
args = parser.parse_args()
inp_file = args.input_file

for g in os.listdir(inp_file):
    tx_position = g.find('.txt')
    input_file_name = g[0:tx_position]
    file = open(f'{args.input_file}/{g}', 'r')
    #print(inputStr)
    inputStr = file.read()
    #inputStr = "T1pT2pT2cT1cT1d"

    # assigning the variable w to obtain the length of the input string
    w = len(inputStr)

    list=[]

    # creating substrings to group in sets of three

    for i in range(0,w,3):
        x = inputStr[i:i+3]
        list.append(x)
    # print(list)

    # Creating variable 'length' for the

    length = len(list)

    # Scoring System:
    # • t = 5 points (Try)
    # • c = 2 points (Goal kick)
    # • p = 3 points (Penalty)
    # • d = 3 points (Drop goal)

    team1_score = 0
    team2_score = 0


    for p in range(len(list)):
        if list[p] == 'T1t':
            team1_score = team1_score + 5
        # print(team1_score)
        # p += 1


        elif list[p] == 'T1p':
            team1_score = team1_score + 3
        # print(team1_score)
        # p += 1

        elif list[p] == 'T1c':
            team1_score = team1_score + 2
        # print(team1_score)
        # p += 1

        elif list[p] == 'T1d':
            team1_score = team1_score + 3
        # print(team1_score)
        # p += 1

    else: pass

    p += 1

    for r in range(len(list)):
        if list[r] == 'T2t':
            team2_score = team2_score + 5
        # print(team2_score)
        # r += 1


        elif list[r] == 'T2p':
            team2_score = team2_score + 3
        # print(team2_score)
        # r += 1

        elif list[r] == 'T2c':
            team2_score = team2_score + 2
        # print(team2_score)
        # r += 1

        elif list[r] == 'T2d':
            team2_score = team2_score + 3
        # print(team2_score)
        # r += 1

    else: pass

    r += 1

    # Determining the Winner:
    Winner = ""
    if team1_score > team2_score:
        Winner = "Team 1"
    elif team1_score == team2_score:
        Winner = "The match is a drawn"
    else: Winner = "Team 2"


    print(str(team1_score) + ":" + str(team2_score))

    print("The winner is " + Winner)

    line = f"{team1_score} : {team2_score}"

    with open(os.path.join(args.output_file, f'{input_file_name}_j96158ap.txt'), 'w') as f:
        f.writelines(line)




