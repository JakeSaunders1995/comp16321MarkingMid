import os.path as path
import sys, os


##  FUNCTIONS ##
def main(input_path, output_path):
    if path.isdir(input_path):
        for file in os.scandir(input_path):
            my_file = open(str(file.path), "r")
            input_str = my_file.readline()
            my_file.close()
            output_str = points_calc(input_str)
            output_write(output_str, output_path, file)
    else:
        print("not given directory, exiting program...")
        sys.exit()


def points_calc(input_str):
    team1 = 0
    team2 = 0
    if len(input_str) == 0:
        print("Empty input file / data not on first line of input file")
    else:
        for i in range(0, len(input_str)-1, 3):
            if input_str[i] == "T":
                if input_str[i+2] == "p" or input_str[i+2] == "d":
                    if input_str[i+1] == "1":
                        team1 += 3
                    elif input_str[i+1] == "2":
                        team2 += 3
                    else:
                        print("Error: cannot find if either team 1 or team 2. incorrect input file")

                elif input_str[i+2] == "t":
                    if input_str[i+1] == "1":
                        team1 += 5
                    elif input_str[i+1] == "2":
                        team2 += 5
                    else:
                        print("Error: cannot find if either team 1 or team 2. incorrect input file")

                elif input_str[i+2] == "c":
                    if input_str[i+1] == "1":
                        team1 += 2
                    elif input_str[i+1] == "2":
                        team2 += 2
                    else:
                        print("Error: cannot find if either team 1 or team 2. incorrect input file")
                else:
                    print("error tracking scores")
        return str(team1)+":"+str(team2)






def output_write(output_str, output_path, file):
    output_file = open(path.join(output_path, path.basename(file)[:-4]+"_s65422mt.txt"), "w")
    output_file.writelines(output_str)
    output_file.close()

## EXECUTION STARTS HERE ##
try:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
except:
    print("ERROR: problem with arguments from command line. Program exiting...")#
    sys.exit()

main(input_path, output_path)
