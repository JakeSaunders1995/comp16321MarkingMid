import os
import os.path
import sys

#assigning directory
inputDir = sys.argv[1]  
outputDir = sys.argv[2]  


#iterating over directory files
for filename in os.listdir(inputDir):

    file = open(inputDir+"/"+filename, 'r')
    Tscores = file.readline()
    outputfname = filename[:-4]

    team1 = 0
    team2 = 0

    for x in range(int(len(Tscores)/3)):
        point_type = Tscores[(3*x)+2]
        if Tscores[3*x+1] == "1":
            if "t" in point_type:
                team1 += 5
            elif "c" in point_type:
                team1 += 2
            elif "p" in point_type:
                team1 += 3
            elif "d" in point_type:
                team1 += 3
                
        if Tscores[3*x+1] == "2":
            if "t" in point_type:
                team2 += 5
            elif "c" in point_type:
                team2 += 2
            elif "p" in point_type:
                team2 += 3
            elif "d" in point_type:
                team2 += 3
            
    results = (str(team1) + ':' + str(team2))
    pathF = outputDir
    if not os.path.exists(pathF):
        os.makedirs(pathF)

    outputf = outputDir + '/' + filename[0:-4] + '_' + 'v21023jh.txt'
    output = open(outputf,'w')
    output.write(results)
    output.close()


    # /home/csimage/Documents/PythonStuff/16321_python_coursework_v21023jh/program1/inputF

    # /home/csimage/Documents/PythonStuff/16321_python_coursework_v21023jh/program1/outputF