import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
parser.add_argument("output", type=str)
args = parser.parse_args()

input = args.input
output = args.output

for file in os.listdir(input):
    f = open(input+"/"+file,"r") #(folder path)+(name of file)
    game = f.read()

    Team1_Points=0
    Team2_Points=0
    for i in range(0,len(game),3):
        if game[i+1] == "1": #if the Team=1
            if game[i+2] == "t":
                Team1_Points+=5 #Try
            elif game[i+2] == "c":
                Team1_Points+=2 #Goal Kick
            elif game[i+2] == "p":
                Team1_Points+=3 #Penalty
            elif game[i+2] == "d":
                Team1_Points+=3 #Drop Goal

        elif game[i+1] == "2": #if the Team=2
            if game[i+2] == "t":
                Team2_Points+=5 #Try
            elif game[i+2] == "c":
                Team2_Points+=2 #Goal Kick
            elif game[i+2] == "p":
                Team2_Points+=3 #Penalty
            elif game[i+2] == "d":
                Team2_Points+=3 #Drop Goal
    f.close()
    file = open(output+"/"+file[:-4]+"_t56563bk.txt","w") #outputs a file called 'test_file1_t56563bk' for example
    #file[:-4] removed .txt so that we can readd it at the end of the file
    file.write(str(Team1_Points)+":"+str(Team2_Points))
