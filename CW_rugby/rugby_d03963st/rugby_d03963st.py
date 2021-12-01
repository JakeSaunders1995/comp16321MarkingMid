import sys
import re
import os

input_directory = sys.argv[1]

for input_file in os.listdir(input_directory):
    with open(os.path.join(input_directory, input_file), "r") as file:

        scores = file.read()

        T1t = re.findall("T1t", scores)
        T1c = re.findall("T1c", scores)
        T1p = re.findall("T1p", scores)
        T1d = re.findall("T1d", scores)

        score_T1 = (len(T1t) * 5) + (len(T1c) * 2) + (len(T1p) * 3) + (len(T1d) * 3)
        print(score_T1)

        T2t = re.findall("T2t", scores)
        T2c = re.findall("T2c", scores)
        T2p = re.findall("T2p", scores)
        T2d = re.findall("T2d", scores)

        score_T2 = (len(T2t) * 5) + (len(T2c) * 2) + (len(T2p) * 3) + (len(T2d) * 3)
        print(score_T2)

        if score_T1 > score_T2:
            print("Winner: Team 1")
        elif score_T2 > score_T1:
            print("Winner: Team 2")
        else:
            print("Draw")

        output_directory = sys.argv[2]

        output_file = output_directory + "/" + input_file[0:-4] + "_d03963st.txt"

        with open(output_file, "w+") as f:
            f.write(str(score_T1) + ":" + str(score_T2))
