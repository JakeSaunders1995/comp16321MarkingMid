import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_folder")
parser.add_argument("output_folder")

args = parser.parse_args()
input_folder = os.path.join(os.getcwd(), args.input_folder)
output_folder = os.path.join(os.getcwd(), args.output_folder)

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

scores = {
    't': 5,
    'c': 2,
    'p': 3,
    'd': 3
}

for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file)) as f:
        game = f.read()

    triplets = [game[i:i+3] for i in range(0, len(game), 3)]
    final_score = {'T1': 0, 'T2': 0}

    for triple in triplets:
        final_score[triple[:2]] += scores.get(triple[-1])

    # Determine winner
    winner = "Draw" if final_score['T1'] == final_score['T2'] else max(final_score, key=final_score.get)

    filename, file_ext = os.path.splitext(file)
    new_file = filename + "_q00848wh" + file_ext
    with open(os.path.join(output_folder, new_file), "w") as f:
        f.write(f"{final_score['T1']}:{final_score['T2']}")
