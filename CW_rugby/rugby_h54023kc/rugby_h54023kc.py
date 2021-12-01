import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs="+")
path = parser.parse_args()

scanned_folder = os.scandir(path.files[0])
full_paths = []
for i in scanned_folder:
    if i.is_file():
        full_paths.append(i.path)
full_paths = sorted(full_paths)

for file_num, current_file in enumerate(full_paths):
    #print(path.files[0])
    file = open(current_file,"r")
    data = file.read().strip("\n")
    data = data.strip(" ")
    file.close()
    #print(data)

    point_allocation_dict = {"t":5, "c":2, "p":3, "d":3}

    team1 = 0
    team2 = 0
    for i in range (0,len(data),3):
        if data[i+1] == "1":
            team1 += point_allocation_dict[data[i+2]]
        else:
            team2 += point_allocation_dict[data[i+2]]

    #print(team1)
    #print(team2)

    if team1>team2:
        print("Team 1 wins")
    elif team1==team2:
        print("Draw")
    elif team1<team2:
        print("Team 2 wins")


    file = open(path.files[1]+"/test_file"+str(file_num+1)+"_h54023kc.txt","w")
    file.write(str(team1)+":"+str(team2))
    file.close()
