import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input_folder_path")
parser.add_argument("output_folder_path")

def get_results(scores):
    results = {"1" : 0, "2" : 0}
    points_dict = {
        "t" : 5,
        "c" : 2,
        "p" : 3,
        "d" : 3
    }

    scores = scores.split("T")
    for score in scores:
        if len(score) < 2:
            continue
        results[score[0]] += points_dict[score[1]]

    return results

def main():
    args = parser.parse_args()

    for file_name in os.listdir(args.input_folder_path):
        if file_name.endswith('.txt'):
            # read file contents
            input_file_path = os.path.join(args.input_folder_path, file_name)
            with open(input_file_path) as f:
                scores = f.read().strip('\n')

            # solve problem
            results = get_results(scores)

            # write results
            output_file_name = file_name[:-4] + '_m18453ab.txt'
            output_file_path = os.path.join(args.output_folder_path, output_file_name)
            with open(output_file_path, 'w') as f:
                f.write(str(results['1']) + ':' + str(results['2']))


if __name__ == "__main__":
    main()