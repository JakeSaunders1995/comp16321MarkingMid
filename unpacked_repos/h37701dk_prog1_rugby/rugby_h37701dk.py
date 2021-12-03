import argparse, os

def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser = argparse.ArgumentParser()
parser.add_argument('input_folder', type=dir_path)
parser.add_argument('output_folder', type=dir_path)
folders = parser.parse_args()

for file in os.listdir(folders.input_folder):
    filepath = folders.input_folder + '/' + file
    input_file = open(filepath, 'r')
    scores = input_file.read()
    input_file.close()
    scores = scores.strip('\n')
    scores = scores.split('T')
    scores.pop(0) # As T is the first character, splitting produces an empty string in the first position

    team1_points = 0
    team2_points = 0
    for score in scores:
        if score[1] == 't':
            points = 5
        elif score[1] == 'c':
            points = 2
        else:
            points = 3

        if score[0] == '1':
            team1_points += points
        else:
            team2_points += points

    if team1_points > team2_points:
        result = 'Team 1 wins'
    elif team2_points > team1_points:
        result = 'Team 2 wins'
    else:
        result = 'Draw'

    filename = os.fsdecode(file)
    filename = filename.replace('.txt', '')
    filename += '_h37701dk.txt'
    output_filepath = folders.output_folder + '/' + filename
    output_file = open(output_filepath, 'w+')
    output_file.write(str(team1_points) + ':' + str(team2_points))
    output_file.close()
