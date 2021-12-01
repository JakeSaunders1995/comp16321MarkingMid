#research how to get that command to work
#we want it to read a text file and make it like an array and for every 3rd chacter in text file will be that teams points and 1st and 2nd chacter are the team and carry on from there
#might need to use a for loop to interrate over all the charcter in the array of the text file
#need a adding function to which ever team scores and is stated in that for loop
#caculate the winner:the team with the most points
#output the results to a empty text file and write in there T1:t2 where t1 is points of team1 vs points of team 2
#run it on vm and test it works


#you have to use argparse for the commandline option watch week 5 again and see the python documentation

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("input",type=str)
parser.add_argument("output",type=str)

args = parser.parse_args()
#print(args.input)
#print(args.output)

import os

#counts the number of files in input
directory = args.input
totalFiles = 0

inputcount = 0
dir = args.input
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        inputcount+=1
#print(inputcount)

#counts the number of files in output

totalFiles = 0

outputcount = 0
dir = args.output
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir,path)):
        outputcount+=1
#print(outputcount)



for filename in os.scandir(directory):

    if filename.is_file():


        #-----Rugby----
        file = open(filename,"r")

        team1 = 0
        team2 = 0
        t = 5
        c = 2
        p = 3
        d = 3

        Scores = ""




        for line in file:
            line=line.rstrip()
            Scores=line


        #print(Scores)
        #print(len(Scores))
        #print(Scores[0])
        #this works as intenteded check later

        for i in range(len(Scores)):

            if Scores[i]== "1":
                if Scores[i+1] == "t":
                    team1 = team1 + t
                elif Scores[i+1] == "c":
                    team1 = team1 +c
                elif Scores[i+1] == "p":
                    team1 = team1 +p
                elif Scores[i+1] == "d":
                    team1 = team1 +d


            elif Scores[i] == "2":
                if Scores[i+1] == "t":
                    team2 = team2 + t
                elif Scores[i+1] == "c":
                    team2 = team2 + c
                elif Scores[i+1] == "p":
                    team2 = team2 + p
                elif Scores[i+1] == "d":
                    team2 = team2 + d


            elif Scores[i] == "T":
                continue
         # works as intenteded try other test files and outpur it to empty text file(maybe on the vm)

        #print(team1)
        #print(team2)
        #print(team1,":",team2 )
        final_Score = (str(team1) +":" +str(team2))
        #print(final_Score)

        dict = args.output
        obj = os.scandir(dict)
        f = filename.name.split(".")

        if outputcount < inputcount:
            #print("b")
            for u in range(inputcount):
                username = '_p50792sd'
                outputfilename = ""
                f = filename.name.split(".")
                outputfilename = outputfilename + f[0]
                outputfilename = outputfilename + username
                arguments = outputfilename + ".txt"
                arguments = args.output + '/' + arguments
               # print(arguments)
                file = open(arguments, "x")
                break

        obj = os.scandir(dict)
        for entry in obj:
            e = entry.name.split("_")
            file_output = e[0] + "_" + e[1]
            if f[0] == file_output:
            #if filename.name[0:10] == entry.name[0:10]:
                #print(filename.name[0:10])
                #print(entry.name[0:10])
                #print("88888888888")

                outputFile = (open(entry, "w+"))
                outputFile.write(final_Score)
            else:
                continue


#last part i to ouput it in the above form maybe by overwriting the output file
#outputFile = open(args.output,"w")
#outputFile.write(final_Score)

#it works
#check that other test files work and push it




