
# Python 3 script to calculate rugby scores from one or more files of input
# Individual score data is of the form TNx where N is the team number and x is the score code
# Meaning T can probably be used as a delimiter

import sys
import os
import re

command_line_arguments = sys.argv
input_directory_name = command_line_arguments[1][2:]
output_directory_name = command_line_arguments[2][2:]


def extract_input_data_from_filename(input_filename):
    file = open('./' + input_directory_name + '/' + input_filename, 'r')
    data = file.read()

    if (data[-2:] == '\n'):
        data = data[:-2]

    file.close()
    return data

# --

def execute(inputs, output_path):
  for file in inputs:
    input_data = extract_input_data_from_filename(file)
    results = process_scores(input_data)
    output_filename = create_empty_file(output_path, file)
    write_data_to_file(results, output_filename)
    print("Successfully processed scores from " + str(file) + ".")
    print("The winner is " + determine_winner(results) + "!")

# --


def process_scores(raw_score_data):
  team1_score = 0
  team2_score = 0
  score_dictionary = {'t': 5, 'c': 2, 'p': 3, 'd': 3}
  scores = raw_score_data.split('T')
  scores.remove('')

  for score in scores:
      if '1' in score:
          team1_score += score_dictionary.get(score[1])
      elif '2' in score:
          team2_score += score_dictionary.get(score[1])
      else:
          raise RuntimeError('Error, no team ID detected in score.')

  return str(team1_score) + ':' + str(team2_score)

def determine_winner(results):
    scores = results.split(':')

    if(scores[0] > scores[1]):
        return 'team 1'
    elif(scores[1] > scores[0]):
        return 'team 2'
    else:
        return 'no-one, it\'s a draw'

# ----

def create_empty_file(location, input_filename):
  new_filename = input_filename[:-4] + '-prog-1-output.txt'
  open('./' + location + '/' + new_filename, 'x').close()
  return new_filename

# ----

def get_filenames_from_input_directory(directory_name):
  directory_contents = os.listdir('./' + directory_name)
  files = []

  for item in directory_contents:
    if(item[-4:] == '.txt'):
        files.append(item)

  return files

# ----

def write_data_to_file(data, filename):
    output_file = open('./' + output_directory_name + '/' + filename, 'w')

    output_file.write(data)

    output_file.close()
    return

# ----

input_files = get_filenames_from_input_directory(input_directory_name)  # argument 0 is the script itself

execute(input_files, output_directory_name)
