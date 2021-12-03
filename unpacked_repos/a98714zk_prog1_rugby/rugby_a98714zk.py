import sys
import os

# Command line test input: python3 rugby_[yourUsername].py ./input folder ./output folder
#                                  sys.argv[0]             sys.argv[1]     sys.argv[2]

directory = str(sys.argv[1])
for filename in os.listdir(directory): # Records all the files/directories in the specified path
    if filename.endswith(".txt"):
        inputTXTfile = os.path.join(directory, filename)
        inputFile = open(inputTXTfile, "r")
        scoreboard = inputFile.read()
        inputFile.close()

        # Logic implementation starts below
        # Calculate total scores of all teams first
        # Then subtract scores of team 1 from total scores to get scores of team 2

        totalScore = 0
        for i in range(2, len(scoreboard), 3):
            if (scoreboard[i] == 't'):
                totalScore += 5
            elif (scoreboard[i] == 'c'):
                totalScore += 2
            elif (scoreboard[i] == 'p'):
                totalScore += 3
            elif (scoreboard[i] == 'd'):
                totalScore += 3

        t1Score = 0
        count = 1
        while (count < len(scoreboard)):
            if (scoreboard[count] == '1'):
                if (scoreboard[count+1] == 't'):
                    t1Score += 5
                elif (scoreboard[count+1] == 'c'):
                    t1Score += 2
                elif (scoreboard[count+1] == 'p'):
                    t1Score += 3
                elif (scoreboard[count+1] == 'd'):
                    t1Score += 3
                count += 3
            else:
                count += 3

        t2Score = totalScore - t1Score

        scoreRatio = str(t1Score) + ":" + str(t2Score)

        save_path = str(sys.argv[2])
        filename_removeTXT = filename[0:-4]
        output_filename = str(filename_removeTXT+"_a98714zk.txt")

        completeName = os.path.join(save_path, output_filename)

        outputFile = open(completeName, "w+")
        outputFile.write(scoreRatio)
        outputFile.close
        
    else:
        continue
