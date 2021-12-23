import sys, os, os.path

source = str(sys.argv[1])
destination = str(sys.argv[2])
sourceFiles = os.listdir(source)
points = {
    "t" : 5,
    "c" : 2,
    "p" : 3,
    "d" : 3
}


i = 0
while(i < len(sourceFiles)):
    score1 = 0
    score2 = 0
    file = open(source + sourceFiles[i])
    content = file.read()
    x = 1
    while(True):
        try:
            if(content[(3 * x) - 2] == "1"): #If team1
                score1 += points[content[(3 * x) - 1]]
            else:
                score2 += points[content[(3 * x) - 1]]
            x += 1
        except:
            break

    file.close()
    file = open(destination + sourceFiles[i] + "_output.txt", "x")
    file.write(str(score1) + ":" + str(score2))
    file.close()

    print(score1)
    print(str(score2) + "\n")
    i += 1
