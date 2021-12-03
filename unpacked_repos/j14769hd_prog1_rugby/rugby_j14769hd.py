import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file path here")
parser.add_argument("output", help="Output file path here")
args = parser.parse_args()
scoring = {"t":5,"c":2,"p":3,"d":3}
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        f = open(os.path.join(args.input, file),"r")
        data = f.read()
        f.close()
        data = data.replace("T","")
        data = list(data)
        scores = [0,0]
        teamData = data[::2]
        for i in range(len(teamData)):
            temp = int(teamData[i])-1
            temp2 = scoring[data[(i*2)+1]]
            scores[temp] += temp2

        name = file.split(".")[0]
        name = name + "_j14769hd.txt"
        if not os.path.exists(args.output):
            os.mkdir(args.output)
        f = open(os.path.join(args.output,name),"w+")
        f.write(str(scores[0])+":"+str(scores[1]))
        f.close()
