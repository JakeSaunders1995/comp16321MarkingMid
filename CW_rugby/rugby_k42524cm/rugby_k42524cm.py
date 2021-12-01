import os, re, argparse

from pathlib import Path
DIR = Path(__file__).parent.absolute()
os.chdir(DIR)

parser = argparse.ArgumentParser()
parser.add_argument("input_folder", help="The folder that contains the input files for the program")
parser.add_argument("output_folder", help="The folder that will contain the output files for the program")
args = parser.parse_args()

def write(input_file, output_file):
    f = open(input_file, 'r')
    scoreString = f.read()
    f.close()

    scores = {
        'T1': 0,
        'T2': 0
    }
    points = {
        't': 5,
        'c': 2,
        'p': 3,
        'd': 3
    }

    for score in re.findall('.{3}',scoreString):
        scores[score[0:2]] += points[score[2]]

    final = ':'.join([f'{team}' for team in scores.values()])

    f = open(output_file, 'w')
    f.write(final)
    f.close()

for file in os.listdir(args.input_folder):
    output_file = re.sub('\.txt$', '', file)
    file = f'{args.input_folder}/{file}'
    output_file = f'{args.output_folder}/{output_file}_k42524cm.txt'
    write(file, output_file)

# python3 rugby_k42524cm.py ../Example_inputs/Example_inputs_program1 ../Example_outputs/Example_outputs_program1
