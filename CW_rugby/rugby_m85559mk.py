import argparse
import os

#Returns a tuple of T1's score and T2's score from a score string
def score_teams(score_string):
    score_string = score_string.strip()
    team_1_score = 0
    team_2_score = 0
    score_dictionary = {
        't' : 5,
        'c' : 2,
        'p' : 3,
        'd' : 3
    }
    for i in range(0, len(score_string), 3):
        if score_string[i+1] == "1":
            team_1_score += score_dictionary[score_string[i+2]]
        else:
            team_2_score += score_dictionary[score_string[i+2]]

    return team_1_score, team_2_score

#Returns a tuple of the input folder and the output folder
def get_io_folders():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("input_folder")
    my_parser.add_argument("output_folder")
    args = my_parser.parse_args()

    return args.input_folder, args.output_folder

def get_output_filename(input_filename, username):
    txt_removed = input_filename.split(".")[0]
    return f'{txt_removed}_{username}.txt'


def main():
    input_folder, output_folder = get_io_folders()
    #Creates the output path if it does not already exist
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.scandir(input_folder):
        with open(filename.path, 'r') as f:
            input_string = f.read()
        output_file_path = os.path.join(output_folder, get_output_filename(filename.name, 'm85559mk'))
        with open(output_file_path, "w+") as f:
            t1_score, t2_score = score_teams(input_string)
            f.write(f'{t1_score}:{t2_score}')


main()
