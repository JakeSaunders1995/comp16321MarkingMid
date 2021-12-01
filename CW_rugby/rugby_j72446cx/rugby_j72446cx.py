import os
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

GetRealInputPath = os.path.realpath(input_file)

filelsit = os.listdir(GetRealInputPath)
for item in filelsit:
    GetFileNameInput = os.path.basename(item)
    GetPath = os.path.realpath(output_file)

    print(item)
    OpenFiles = open(GetRealInputPath + "/" + item, 'r')
    textname = GetFileNameInput.replace(".txt","_j72446cx.txt")

    theFirstOutput = open(os.path.join(GetPath, textname),"w")

    s = OpenFiles.read()
    T1 = 0
    T2 = 0
    a = 0
    b = 3
    while b <= len(s) + 1:

        if s[a:b] == "T1t":
            T1 += 5
        if s[a:b] == "T1c":
            T1 += 2
        if s[a:b] == "T1p":
            T1 += 3
        if s[a:b] == "T1d":
            T1 += 3
        if s[a:b] == "T2t":
            T2 += 5
        if s[a:b] == "T2c":
            T2 += 2
        if s[a:b] == "T2p":
            T2 += 3
        if s[a:b] == "T2d":
            T2 += 3
        a += 3
        b += 3
    print(T1,":",T2)
    if T1 < T2:
        print("The winner is team 1")
    elif T1 > T2:
        print("The winner is team 2")
    elif T1 == T2:
        print("They draw")



    theFirstOutput.write(str(T1))
    theFirstOutput.write(":")
    theFirstOutput.write(str(T2))

    OpenFiles.close()
    theFirstOutput.close()