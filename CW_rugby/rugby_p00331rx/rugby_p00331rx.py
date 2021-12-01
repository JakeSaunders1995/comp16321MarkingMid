import argparse
import os

p00331rx = "p00331rx"
parser = argparse.ArgumentParser()
parser.add_argument("input_path",
                    default="./midterm_files/Example_inputs/Example_inputs_program1", type=str)
parser.add_argument("output_path",
                    default="./midterm_files/Example_outputs/Example_inputs_program1",
                    type=str)
args = parser.parse_args()


def calculated_scores(data_text):
    team1_score_list = []
    team2_score_list = []
    score_map = {"t": 5, "c": 2, "p": 3, "d": 3}
    for i in range(0, len(data_text), 3):
        team = data_text[i: i + 2]
        score = data_text[i + 2]
        if team == "T1" and score in score_map:
            team1_score_list.append(score_map[score])
        elif team == "T2" and score in score_map:
            team2_score_list.append(score_map[score])
        else:
            raise ValueError
    return team1_score_list, team2_score_list


def read_txt(file_path):
    # read data
    with open(file_path, "r") as f:
        data_line = f.read().strip()
    return data_line


def write_txt(file_path, team1_score, team2_score):
    with open(file_path, "w") as f:
        f.write(f"{team1_score}:{team2_score}")


def main():
    # this is Rui Xu's midterm work!
    input_files = os.listdir(args.input_path)
    for file in input_files:
        file_path = os.path.join(args.input_path, file)
        file_datta = read_txt(file_path)
        team1_score_list, team2_score_list = calculated_scores(file_datta)
        team1_score = sum(team1_score_list)
        team2_score = sum(team2_score_list)
        out_file_path = os.path.join(args.output_path, file[:-4] + f"_{p00331rx}.txt")
        write_txt(out_file_path, team1_score, team2_score)


if __name__ == '__main__':
    main()
# python3 rugby_p00331rx.py ./midterm_files/Example_inputs/Example_inputs_program1 ./midterm_files/Example_outputs/Example_outputs_program1
