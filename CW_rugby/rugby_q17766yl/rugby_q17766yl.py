import argparse, os
# get folder names
parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

score_lookup = {
    't': 5,
    'c': 2,
    'p': 3,
    'd': 3
}

file_list = [i for i in os.listdir(args.input_folder) if os.path.isfile(f'{args.input_folder}/{i}')]

for file_name in file_list:
    # read input file
    f = open(f'{args.input_folder}/{file_name}')
    score_list = f.read().strip()
    f.close()

    # count score
    team_score = [0, 0]
    for i in range( int(len(score_list)/3) ):
        team_score[ int(score_list[i*3+1:i*3+2])-1 ] += score_lookup[ score_list[i*3+2:i*3+3] ]

    # write output file
    if '.' in file_name:
        file_name_part = file_name.split('.')
        file_extension = file_name_part.pop(-1)
        new_file_name = f'{".".join(file_name_part)}_q17766yl.{file_extension}'
    else:
        new_file_name = f'{file_name}_q17766yl'
    f = open(f'{args.output_folder}/{new_file_name}', 'w')
    f.write(f'{team_score[0]}:{team_score[1]}')
    f.close()