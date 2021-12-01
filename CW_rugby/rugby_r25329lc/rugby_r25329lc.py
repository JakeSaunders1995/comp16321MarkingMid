import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args=parser.parse_args()

for file in os.listdir(args.input):
    filepath = os.path.join(args.input,file)
    with open(filepath, 'r') as f:
        results = f.read()

    team_1=0
    team_2=0
    points=0
    team=0

    for n in results:
        if n == "T":
            points=0
        if n == "1":
            team=1
        elif n == "2":
            team=2
        elif n == "t":
            points=5
        elif n == "c":
            points=2
        elif n == "p":
            points=3
        elif n == "d":
            points=3
        if team==1:
            team_1+=points
        elif team==2:
            team_2+=points

    file = file[:len(file)-4]

    outputfile = file+"_r25329lc.txt"

    outputpath = os.path.join(args.output,outputfile)

    with open(outputpath, 'w') as f:
        f.write(str(team_1)+":"+str(team_2))

