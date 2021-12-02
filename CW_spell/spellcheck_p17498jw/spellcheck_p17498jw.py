import argparse
import os
import re

parser = argparse.ArgumentParser()
# Create arguments
parser.add_argument("eng_words_file", help="A filepath to the file of English words")
parser.add_argument("input_dir", help="A dirpath for the input score files")
parser.add_argument("output_dir", help="A dirpath for the output score files")

args = parser.parse_args()

eng_words_file = args.eng_words_file
input_dir = args.input_dir
output_dir = args.output_dir

# Make output directory if required
if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

def to_lower(matchobj):
    return matchobj.group(0).lower()

input_files = []
output_files = []
# Walk through input directory recursively to get files
for root, dirs, files in os.walk(input_dir):
    for name in files:
        # root will be relative or absolute depending on what was given as an arg
        input_files.append(os.path.join(root, name))
        # The slice assumes that the input filename ends in .txt
        output_files.append(os.path.join(output_dir, name[:-4] + "_p17498jw.txt"))

# Get list of English words
eng_words_fh = open(eng_words_file, 'r')
eng_words = [w.strip() for w in eng_words_fh.readlines()]
eng_words_fh.close()

for i in range(0, len(input_files)):
    in_file = input_files[i]
    out_file = output_files[i]
    
    # Read string from file - assume on first and only first line
    in_fh = open(in_file, "r")
    string_to_parse = in_fh.readline()
    in_fh.close()

    # Remove numbers and punctuation, and replace uppercase letters
    new_string, num_of_nums = re.subn(r'\d', r'', string_to_parse)
    new_string, num_of_ellipsis = re.subn(r'\.\.\.', r'', new_string)
    new_string, num_of_puncs = re.subn(r'[.?!,:;\-\–\—(){}[\]\'"]', r'', new_string)
    new_string, num_of_uppers = re.subn(r'[A-Z]', to_lower, new_string)
    num_of_puncs += num_of_ellipsis

    words = new_string.split()
    num_of_words = len(words)

    # Check if words are correct
    num_of_words_correct = 0
    num_of_words_incorrect = 0
    for word in words:
        if word in eng_words:
            num_of_words_correct += 1
        else:
            num_of_words_incorrect += 1

    # Format results for output file
    result_lines = ["p17498jw\n"]
    result_lines.append("Formatting ###################\n")
    result_lines.append("Number of upper case letters changed: {}\n".format(num_of_uppers))
    result_lines.append("Number of punctuations removed: {}\n".format(num_of_puncs))
    result_lines.append("Number of numbers removed: {}\n".format(num_of_nums))
    result_lines.append("Spellchecking ###################\n")
    result_lines.append("Number of words: {}\n".format(num_of_words))
    result_lines.append("Number of correct words: {}\n".format(num_of_words_correct))
    result_lines.append("Number of incorrect words: {}\n".format(num_of_words_incorrect))

    # Store results in output file
    out_fh = open(out_file, "w+")
    out_fh.writelines(result_lines)
    out_fh.close()
