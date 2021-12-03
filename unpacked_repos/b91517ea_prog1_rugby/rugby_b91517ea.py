import sys, os

for file in os.listdir(sys.argv[1]):
    with open(os.path.join(sys.argv[1], file), 'r') as f:
        file1 = str(f.read())

    score1 = 0
    score2 = 0

    i = 0
    while i < len(file1):

        if file1[i+1] == "1":
            if file1[i+2] == "t":
                score1 += 5
            if file1[i+2] == "c":
                score1 += 2
            if file1[i+2] == "p":
                score1 += 3
            if file1[i+2] == "d":
                score1 += 3

        if file1[i+1] == "2":
            if file1[i+2] == "t":
                score2 += 5
            if file1[i+2] == "c":
                score2 += 2
            if file1[i+2] == "p":
                score2 += 3
            if file1[i+2] == "d":
                score2 += 3

        i += 3

    outputScore = str(score1) + ":" + str(score2)
    print("The score is", outputScore)

    newFilename = str(os.path.splitext(file)[0]) + "_b91517ea.txt"
    newFile = os.path.join(sys.argv[2], newFilename)

    file2 = open(newFile, "w")
    file2.write(outputScore)
    file2.close()

    if score1 > score2:
        print("Team 1 is the Winner.")
    elif score1 < score2:
        print("Team 2 is the Winner.")
    else:
        print("It is a Draw.")