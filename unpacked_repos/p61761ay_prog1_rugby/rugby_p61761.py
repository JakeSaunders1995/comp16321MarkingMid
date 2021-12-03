import argparse, os, re


parser = argparse.ArgumentParser(
    description= "program 1"
)

parser.add_argument("input_file_path", type=str, help = "enter your input folder path directory")
parser.add_argument("output_file_path", type=str, help = "enter your output folder path directory")
args = parser.parse_args()

input_file_path = args.input_file_path
output_file_path = args.output_file_path


input_files_path_list = []
file_names = []
T1Score = 0
T2Score = 0



for filename in os.listdir(input_file_path):
    if filename.endswith(".txt"):
        construct = input_file_path + "/" + filename
        input_files_path_list.append(construct)



for inputFilePath in input_files_path_list:

    # get name of the input file, so I can make the relevent name for the output file
    deconstruct = re.split("[/.]",inputFilePath)
    fileNameOnly = deconstruct[1]


    f = open(inputFilePath,"r")
    scores = f.read()
    scoresList = re.findall("...",scores)

    # print(scoresList)

    for i in scoresList:
        if (i[:2] == "T1"):

            if (i[2] == "t"):
                T1Score += 5
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "c"):
                T1Score += 2
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "p"):
                T1Score += 3
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "d"):
                T1Score += 3
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")

        elif (i[:2] == "T2"):

            if (i[2] == "t"):
                T2Score += 5
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "c"):
                T2Score += 2
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "p"):
                T2Score += 3
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
            elif (i[2] == "d"):
                T2Score += 3
                # print("T1Score: " + str(T1Score))
                # print("T2Score: " +  str(T2Score))
                # print("----")
        

    outputFileDirectory = output_file_path + "/" + fileNameOnly + "_p61761ay.txt"


    if (T1Score > T2Score):
        # print("*** T1 Wins " + str(T1Score))
        # print("*** " + str(T1Score) + ":" + str(T2Score))


        outputFile = open(outputFileDirectory, "w")
        outputFile.write(str(T1Score) + ":" + str(T2Score))
        f.close()

        T1Score = 0
        T2Score = 0

    elif (T1Score < T2Score):
        # print("*** T2 Wins " + str(T2Score))
        # print("*** " + str(T1Score) + ":" + str(T2Score))

        outputFile = open(outputFileDirectory, "w")
        outputFile.write(str(T1Score) + ":" + str(T2Score))
        f.close()

        T1Score = 0
        T2Score = 0

    elif (T1Score == T2Score):
        # print("*** It is a Draw")
        # print("*** " + str(T1Score) + ":" + str(T2Score))

        outputFile = open(outputFileDirectory, "w")
        outputFile.write(str(T1Score) + ":" + str(T2Score))
        f.close()

        T1Score = 0
        T2Score = 0
            
            
            
            



