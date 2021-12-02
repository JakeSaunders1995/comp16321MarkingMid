import os, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument("english_words")
parser.add_argument("input_folder")
parser.add_argument("output_folder")

args = parser.parse_args()
english_words_path = os.path.join(os.getcwd(), args.english_words)
input_folder = os.path.join(os.getcwd(), args.input_folder)
output_folder = os.path.join(os.getcwd(), args.output_folder)

with open(english_words_path) as f:
    english_words = f.read().split("\n")

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

dashes = "".join(map(chr, range(8208, 8214)))  # All variations of dashes/hyphens in unicode (except for chr(45))
punctuation = rf".?!,:;\-{dashes}\[\]{{}}()'\""

for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file)) as f:
        text = f.read()

    formatted = re.sub(rf"[0-9{punctuation}]", "", text).lower()
    words = formatted.split()
    correct_words = [word for word in words if word in english_words]

    num_uppercase = len(re.findall("[A-Z]", text))
    num_punc = len(re.findall(rf"[{punctuation}]", text)) - 2 * len(re.findall("[.]{3}", text))
    num_numbers = len(re.findall("[0-9]", text))

    output = f"""q00848wh
Formatting ###################
Number of upper case letters changed: {num_uppercase}
Number of punctuations removed: {num_punc}
Number of numbers removed: {num_numbers}
Spellchecking ###################
Number of words: {len(words)}
Number of correct words: {len(correct_words)}
Number of incorrect words: {len(words) - len(correct_words)}
"""

    filename, file_ext = os.path.splitext(file)
    new_file = filename + "_q00848wh" + file_ext
    with open(os.path.join(output_folder, new_file), "w") as f:
        f.write(output)
