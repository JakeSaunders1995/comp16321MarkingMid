import sys
import re
import os

OutputFolder = sys.argv[-1]
InputFolder = sys.argv[-2]

textFiles = os.listdir(InputFolder)

for each in textFiles:
    outFilePath = OutputFolder + '/' + each[0:-4] + '_h08963ob.txt'
    path = InputFolder + '/' + each

    Team1points = 0
    Team2points = 0

    ScoreRules = {'t':5,'c':2,'p':3,'d':3} # make dict of the rules,

    inpf = open(path, "r")
    ScoreString = inpf.read()
    inpf.close()

    ScoreList = re.findall('...',ScoreString)

    for each in ScoreList:
        if int(each[1]) == 1:
            Team1points += ScoreRules[each[2]]
        elif int(each[1]) == 2:
            Team2points += ScoreRules[each[2]]
        

    finalPoints = str(Team1points) +':'+str(Team2points)

#Comparing the scores to determine a winner
    if Team1points > Team2points:
        Winner = 'Team 1 won'
    elif Team1points < Team2points:
        Winner = 'Team 2 won'
    else:
        Winner = 'It was a Draw'
    
    #print(Winner) #not sure if supposed to print this or not, decided against it
        
    outf = open(outFilePath,"w+")
    outf.write(finalPoints)
    outf.close()

    #for each in Score list check the 2nd character and then retrieve the number associated with the 3rd character
    #from the dictionary and add it to the correct score variable
    
    
    #t = 5 points (Try)
    ##c = 2 points (Goal kick) 
    #p = 3 points (Penalty)
    #d = 3 points (Drop goal)