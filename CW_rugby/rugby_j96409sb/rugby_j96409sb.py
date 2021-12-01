import argparse
from os import listdir
from os.path import isfile, join

def parse_command_line():
    '''Parse the command line arguments and return'''
    parser = argparse.ArgumentParser(description="Decrypt a message using the provided algorithm")
    parser.add_argument("input", metavar="I", type=str,
                        help="Input file path", action="store")
    parser.add_argument("output", metavar="O", type=str,
                        help="Output file path", action="store")

    args = parser.parse_args()
    return args.input, args.output

def read_file(filepath):
    '''Read the file given and return the text'''
    file = open(filepath, "r")
    file_text = file.read()
    file.close()
    return file_text

def write_files(filepath, score_string_list):
    for i in range(len(score_string_list)):
        file=open(f"{filepath}/test_file{i+1}_j96409sb.txt", "w")
        file.write(score_string_list[i])
        file.close()
    
def determine_score_types(text):
    score_list = text.split("T")
    score_list = score_list[1::]
    team_1 = []
    team_2 = []
    for score in score_list:
        if score[0] == "1":
            team_1.append(score[1])
        elif score[0] == "2":
            team_2.append(score[1])
    return team_1, team_2

def determine_score_num(team_1, team_2):
    score_type_dict = {
        "t": 5, "c": 2, "p": 3, "d":3
    }
    team_1_score = 0
    team_2_score = 0
    for score in team_1:
        team_1_score += score_type_dict[score]
    for score in team_2:
        team_2_score += score_type_dict[score]
    return f"{team_1_score}:{team_2_score}"
            

if __name__ == "__main__":
    input_path, output_path = parse_command_line()
    files = [file for file in listdir(input_path) if isfile(join(input_path, file))]
    score_string_list = []
    for file in files:
        score_from_file = read_file(f"{input_path}/{file}")
        team_1_type, team_2_type = determine_score_types(score_from_file)
        score_string = determine_score_num(team_1_type, team_2_type)
        score_string_list.append(score_string)
    write_files(output_path, score_string_list)
    
    
