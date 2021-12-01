import argparse
import glob

my_parser = argparse.ArgumentParser()

my_parser.add_argument('input', type = str)
my_parser.add_argument('output', type = str)

args = my_parser.parse_args()

scoring_series = ''

for input_file_path in glob.glob(args.input + '/*.txt'):
    with open(input_file_path, "r") as f:
        scoring_series = f.readline()
    score_t1, score_t2 = 0, 0
    while len(scoring_series) > 0:
        if (scoring_series[0:2]) == 'T1':
            if scoring_series[2] == 't':
                score_t1 += 5
            elif scoring_series[2] == 'c':
                score_t1 += 2
            elif scoring_series[2] == 'p' or scoring_series[2] == 'd':
                score_t1 += 3
        elif (scoring_series[0:2]) == 'T2':
            if scoring_series[2] == 't':
                score_t2 += 5
            elif scoring_series[2] == 'c':
                score_t2 += 2
            elif scoring_series[2] == 'p' or scoring_series[2] == 'd':
                score_t2 += 3
        scoring_series = scoring_series[3:]

    input_file = input_file_path.split('/')[-1]

    with open(f'{args.output}/{input_file[0:-4]}_f05815rb.txt', "w") as g:
        g.write(f'{score_t1}:{score_t2}')
