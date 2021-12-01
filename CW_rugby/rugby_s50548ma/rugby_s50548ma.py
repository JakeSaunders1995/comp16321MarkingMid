import os
import sys

print("welcome to the Rugby program ")
#globals

#fucntions
def points(char):
    if char == "t":
        return(5)
    elif char == "c":
        return(2)
    elif char == "p":
        return (3)
    elif char == "d":
        return(3)
    else:
        print("an error has occured")
        return (0)

def main(input_filepath):
    team1_score = 0
    team2_score = 0
    #reading the file
    with open(input_filepath) as inputFile:
        data = inputFile.readline()
        inputFile.close()
    for i in range(len(data)):
        if data[i] == "1":
            team1_score += points(data[i+1])
        elif data[i] == "2":
            team2_score += points(data[i+1])
        else:
            pass
    output_statement = str(team1_score) + ":" + str(team2_score)
    return output_statement

#input
input_folder = sys.argv[1][2:]
output_folder = sys.argv[2][2:]
folder_list = os.listdir(input_folder)
output_txt_files = []


for i in range(len(folder_list)):
    output_txt_files.append("test_file" + str(folder_list[i][9]) + "_s50548ma.txt")

print(output_txt_files)
print(folder_list)


for i in range(len(folder_list)):
    cur_input_file = input_folder + "/" + folder_list[i]
    output_statement = main(cur_input_file)
    print(output_statement)
    cur_output_file = output_folder +"/"+output_txt_files[i]
    with open(cur_output_file,"w") as output_file:
        output_file.writelines(output_statement)
