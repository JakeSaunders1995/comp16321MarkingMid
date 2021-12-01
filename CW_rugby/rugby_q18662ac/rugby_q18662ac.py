import argparse
import os

parse = argparse.ArgumentParser()
parse.add_argument("input_folder",help = "The folder which contains the inputs")
parse.add_argument("output_folder",help = "The folder which will contains the Output")
args  = parse.parse_args()

def score(file):

    def teamscore(data,i):
        Tscore = 0
        if data[i+1] == "t":
            Tscore += 5
        elif data[i+1] == "c":
            Tscore += 2
        elif data[i+1] == "p":
            Tscore += 3
        elif data[i+1] == "d":
            Tscore += 3
        return Tscore

    T1score = 0
    T2score = 0

    data = file.read()
    for i in range (1,len(data),3):
        if data[i] == "1":  
            T1score += teamscore(data,i)
        else:
            T2score += teamscore(data,i)
    
    if T1score>T2score:
        winner = "Team1"
    elif T1score<T2score:
        winner = "Team2"
    else:
        winner = "Draw"


    dataf = str(T1score)+":"+str(T2score)
    return dataf

for file in os.scandir(args.input_folder):
    file1=open(file,"r")
    pathname,filename=os.path.split(file)
    string=str(filename)
    string=string[0:len(string)-4]+"_q18662ac.txt"
    file2=open(args.output_folder+"/"+string,"w")
    file2.write(score(file1))
    file1.close()
    file2.close()