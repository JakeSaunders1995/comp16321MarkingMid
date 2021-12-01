import sys
import os

input_folder = sys.argv[1]
output_folder = sys.argv[2]

input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

points = {
    "t": 5, 
    "c": 2, 
    "p": 3, 
    "d": 3
}

for input_file in input_files:
    f = open(os.path.join(input_folder, input_file))
    input_file_contents = f.read()
    f.close()

    team1 = 0
    team2 = 0

    for i in range (0, len(input_file_contents)):
        if (input_file_contents[i] == "T"):
            if (input_file_contents[i + 2] in points.keys()):
                if (input_file_contents[i + 1] == "1"):
                    team1 += points[input_file_contents[i + 2]]
                elif (input_file_contents[i + 1] == "2"):
                    team2 += points[input_file_contents[i + 2]]

    f = open(os.path.join(output_folder, f"{input_file.split('.txt')[0]}_y35654gw.txt"), "w")
    f.write(f"{team1}:{team2}")
    f.close()