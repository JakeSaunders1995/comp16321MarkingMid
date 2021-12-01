import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("echo_i")
parser.add_argument("echo_o")
args = parser.parse_args()

i_path = (args.echo_i)
o_path = (args.echo_o)

os.chdir(i_path) 

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        str_game = f.read()
      
    global teams
    teams = [0, 0]

    for i in range(int(len(str_game)/3)):
        if "T" == str_game[i*3]:
            if "1" == str_game[i*3+1]:
                team_num = 0
            else:
                team_num = 1
        if "t" == str_game[i*3+2]:
            teams[team_num] += 5
        elif "c" == str_game[i*3+2]:
            teams[team_num] += 2
        elif "p" == str_game[i*3+2]:
            teams[team_num] += 3
        elif "d" == str_game[i*3+2]:
            teams[team_num] += 3
    output(file_path) 

def output(file_path): 
    os.chdir(o_path)
    with open(file_path, 'a') as k:
        k = open(file[:-4] + "_j90992mm.txt", "w")
        k.write(str(teams[0]) + ":" + str(teams[1]))
        k.close
    os.chdir(i_path) 

for file in os.listdir():
    file_path = f"{i_path}\{file}"
    read_text_file(file_path)
