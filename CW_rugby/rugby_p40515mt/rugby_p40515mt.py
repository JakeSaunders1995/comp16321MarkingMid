import argparse
from os import listdir
from os.path import isfile, join
def terminal_file():
    enterer = argparse.ArgumentParser(description="rugby match result")
    enterer.add_argument("input", metavar="In", type=str, help="enter input file path", action="store")
    enterer.add_argument("output", metavar="Out", type=str, help="enter output file path", action="store")
    global args
    args = enterer.parse_args()

    return args.input, args.output

terminal_file()

newfilelist = []
unordredfile = []
for fichier in listdir(args.input):
    output = ""
    if isfile(join(args.input, fichier)):
        if fichier[-4:] == ".txt" and fichier[:3] != '.DS':
            if fichier[-5] not in "0123456789":
                unordredfile.append(fichier)
            else:
                for i in range(10):
                    if fichier[-5] == f"{i}":
                        newfilelist.insert(i-1,fichier)
unordredfile.reverse()

final_list = newfilelist + unordredfile


for f in final_list:
    output = ""
    if isfile(join(args.input, f)):
        if f[-4:] == ".txt":
            file = open(f"{args.input}/{f}", "r")
            line = file.readlines()

            score = [0, 0]


            def Scoring(row, teamresult, teamscore):
                if line[row][teamresult] == 't':
                    score[teamscore] += 5
                elif line[row][teamresult] == 'c':
                    score[teamscore] += 2
                elif line[row][teamresult] == 'p':
                    score[teamscore] += 3
                elif line[row][teamresult] == 'd':
                    score[teamscore] += 3


            for i in range(len(line)):
                lenght_element = len(line[i])
                for l in range(lenght_element):
                    position = l % 3
                    if position == 2:
                        if line[i][l - 2:l] == 'T1':
                            m = 0
                            Scoring(i, l, m)
                        elif line[i][l - 2:l] == 'T2':
                            m = 1
                            Scoring(i, l, m)
            global Final_result
            Final_result = str(score[0]) + ":" + str(score[1])
            file.close()
            f2 = f[:-4]
            with open(f"{args.output}/{f2}_p40515mt.txt", 'w') as output_file:
               output_file.write(Final_result)
               output_file.close()
            if score[0] > score[1]:
                print("Team 1 is the winner.")
            elif score[0] < score[1]:
                print("Team 2 is the winner.")
            elif score[0] == score[1]:
                print("The match result is a draw.")
