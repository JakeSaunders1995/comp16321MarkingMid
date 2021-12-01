import argparse,os,re
score = {"t":5,"c":2,"p":3,"d":3}
parser = argparse.ArgumentParser(description="rugby score calculator")
parser.add_argument("input", help="Input file path")
parser.add_argument("save",help="Output file path")
folder = parser.parse_args()
for filename in os.listdir(folder.input):
    if filename.endswith(".txt"):
        inputFile = open(folder.input + filename,"r")
        scores = inputFile.readline()
        if re.match("T1.|T2.",scores):
            outputFile = open(folder.save + filename[0:-4] + "_m31181jg" + ".txt","w")    
            team1score=0
            team2score=0
            for i in range(0,len(scores),3):
                if scores[i:(i+2)] == "T1":        
                    team1score += score[scores[i+2]]
                else:
                    team2score += score[scores[i+2]]
            outputFile.write(str(team1score) + ":" + str(team2score))
            outputFile.close
        inputFile.close
        