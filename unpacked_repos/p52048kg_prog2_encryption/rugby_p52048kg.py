import sys
import os

inputFolder = sys.argv[1]
outputFolder = sys.argv[2]

for filename in os.listdir(inputFolder):
    if filename.endswith(".txt"):
        Team1 = 0
        Team2 = 0
        
        if inputFolder.endswith("/"):
            inputFile = inputFolder+filename
        else:
            inputFile = inputFolder+"/"+filename

        outputFile = filename[:-4]+"_p52048kg"+".txt"
        if outputFolder.endswith("/"):
            outputPath = outputFolder+outputFile
        else:
            outputPath = outputFolder+"/"+outputFile
        
        file = open(str(inputFile), "rt")
        data = file.readline()

        for i in range (0, len(data), 3):
            team = data[i:i+2]
            action = data[i+2]
            if str(team) == "T1":
                if str(action) == "t":
                    Team1 = Team1 + 5
                elif str(action) == "c":
                    Team1 = Team1 + 2
                elif str(action) == ("p"):
                    Team1 = Team1 + 3
                elif str(action) == ("d"):
                    Team1 = Team1 + 3
                else:
                    pass
            elif str(team) == "T2":
                if str(action) == "t":
                    Team2 = Team2 + 5
                elif str(action) == "c":
                    Team2 = Team2 + 2
                elif str(action) == ("p"):
                    Team2 = Team2 + 3
                elif str(action) == ("d"):
                    Team2 = Team2 + 3
                else:
                    pass
                
        file.close()
        
        finalScore = str(Team1)+":"+str(Team2)
        
        """
        outputFile = filename[:-4]+"_p52048kg"+".txt"
        print(outputFile)
        if outputFolder.endswith("/"):
            outputPath = outputFolder+outputFile
        else:
            outputPath = outputFolder+"/"+outputFile
        """

        file = open(str(outputPath), "wt")
        file.write(finalScore)
        file.close()

    else:
        pass




        

