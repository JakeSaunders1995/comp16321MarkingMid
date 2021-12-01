import argparse
import os 
parser = argparse.ArgumentParser(description='Goal to score')
parser.add_argument('goaltxt', type=str, help='Goal/input')
parser.add_argument('scoretxt', type=str, help='Score/output')
args = parser.parse_args()

inputDirectory = args.goaltxt
outputDirectory = args.scoretxt

for i in os.listdir(inputDirectory):
    dirname = os.path.join(inputDirectory, i)
    directory = os.path.dirname(outputDirectory)
    file1 = open(dirname, "r")

    t1_scores = 0 
    t2_scores = 0
    input = file1.readline()


    for x in range(len(input)):
        if (x % 3 == 1):
            teamname = int(input[x])
            if teamname == 1:
                goals = input[x+1]
                if goals == "t":
                    t1_scores += 5
                elif goals == "c":
                    t1_scores += 2
                elif goals == "p":
                    t1_scores += 3
                elif goals == "d":
                    t1_scores += 3
                else:
                    print("Not valid!")
            elif teamname == 2:
                goals = input[x+1]
                if goals == "t":
                    t2_scores += 5
                elif goals == "c":
                    t2_scores += 2
                elif goals == "p":
                    t2_scores += 3
                elif goals == "d":
                    t2_scores += 3
                else: 
                    print("Really?!")
        else:
            continue
    
    if outputDirectory[-1] != "/":
        nameout = outputDirectory + "/" + i.split(".txt")[0] + "_q08386js.txt"
    else:
        nameout = outputDirectory + i.split(".txt")[0] + "_q08386js.txt"
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    file2 = open(nameout, "w")
    finalresults = str(t1_scores) + ":" + str(t2_scores)
    file2.write(finalresults)

    file1.close()
    file2.close()