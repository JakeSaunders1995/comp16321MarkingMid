#Rugby
import os
import argparse

parser=argparse.ArgumentParser(description='Input File and output file')
parser.add_argument("source_file")
parser.add_argument("target_file")
args=parser.parse_args()

cwd=os.getcwd()
print(cwd)

input_file=args.source_file
print(input_file)

output_file=args.target_file
print(output_file)

dirs=os.listdir(input_file)
for file in dirs:
    team_1_score=0
    team_2_score=0
    print(file)
    os.chdir(str(cwd)+"/"+str(input_file))
    scores=open(file,"r")
    scores=scores.read()
    scores=scores.split("T")

    for i in range(1,len(scores)):
        if scores[i][0]=="1":
            if scores[i][1]=="t":
                team_1_score=team_1_score+5
            elif scores[i][1]=="c":
                team_1_score=team_1_score+2
            else:
                team_1_score=team_1_score+3

        else:
            if scores[i][1]=="t":
                team_2_score=team_2_score+5
            elif scores[i][1]=="c":
                team_2_score=team_2_score+2
            else:
                team_2_score=team_2_score+3
    print(str(team_1_score) + ":" + str(team_2_score))
    final_score=str(team_1_score) + ":" + str(team_2_score)

    os.chdir(str(cwd)+"/"+str(output_file))
    file=file[0:-4]
    print(file)
    file=str(file + "_d47007el.txt")
    file=open(file,"w")
    file.write(final_score)
