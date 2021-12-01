import os, argparse, re

parser = argparse.ArgumentParser(description = 'get i/o files')
parser.add_argument("input_path")
parser.add_argument("output_path")
args = parser.parse_args()

full_input_path = os.path.join(os.getcwd(), args.input_path)
input_files = os.listdir(full_input_path)

full_output_path = os.path.join(os.getcwd(), args.output_path)

score_inputs = []
filenames_split = []
for input_filename in input_files:
    input_path = full_input_path + "/" + input_filename
    input_file = open(input_path, "r")
    score_inputs.append(input_file.read())
    input_file.close

    temp_file_split = re.split(".txt", input_filename)
    filenames_split.append(temp_file_split[0])

file_num = 1
for score_input in score_inputs:
    total_score = [0,0]
    pos_input = 0
    while pos_input < len(score_input):
        team_num = int(score_input[pos_input + 1]) - 1
        
        if score_input[pos_input + 2] == 't':
            total_score[team_num] = total_score[team_num] + 5
        elif score_input[pos_input + 2] == 'c':
            total_score[team_num] = total_score[team_num] + 2
        else:
            total_score[team_num] = total_score[team_num] + 3


        pos_input = pos_input + 3

    output_path = full_output_path + "/" + filenames_split[file_num - 1] + "_n72421tn.txt"
   
    score_output = open(output_path, "w") 
    score_output.write(str(total_score[0]) + ":" + str(total_score[1]))
    score_output.close

    file_num = file_num + 1
