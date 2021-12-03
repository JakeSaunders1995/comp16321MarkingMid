import os, argparse

parse = argparse.ArgumentParser()
parse.add_argument('directory', nargs='+')
args = parse.parse_args()
files = os.listdir(args.directory[1])



if not os.path.exists(args.directory[2]):
    os.mkdir(args.directory[2])


with open(args.directory[0], 'r') as file:
    words = []
    for word in file.readlines():
        word = word.strip()
        words.append(word)

words.append(' ')
punctuation = ['.', '?', '!', ',', ':', ';', '?', '-', '[', ']', '{', '}', '(', ')', '\'', '\"', '...']



for theFile in files:
    message = []
    with open(args.directory[1] + '/' + theFile, 'r') as line:
        f = list(line.read().rstrip())
    f.append(' ')

    n_up = 0
    n_punctuation = 0
    n_numeric = 0
    n_correct_words = 0
    n_wrong_words = 0

    start_index = 0
    i = 0
    while i < len(f):
        if f[i].isupper():
            n_up += 1
            f[i] = f[i].lower()
        elif f[i] in punctuation:
            if i+3 < len(f) and ''.join(f[i:i+3]) == '...':
                del f[i:i+3]
                i -= 3
            else:
                del f[i]
                i -= 1

            n_punctuation += 1

        elif f[i].isnumeric():
            n_numeric += 1
            del f[i]
            i -= 1
        elif f[i] == ' ':
            theWord = ''.join(f[start_index: i])
            if theWord.isalpha():
                if theWord in words:
                    n_correct_words += 1
                else:
                    n_wrong_words += 1

            start_index = i + 1
        i += 1

    out = []
    out.append('e80626nm\n')
    out.append("Formatting ###################\n")
    out.append(f"Number of upper case letters changed: {n_up}\n")
    out.append(f"Number of punctuations removed: {n_punctuation}\n")
    out.append(f"Number of numbers removed: {n_numeric}\n")
    out.append("Spellchecking ###################\n")
    out.append(f"Number of words: {n_correct_words + n_wrong_words}\n")
    out.append(f"Number of correct words: {n_correct_words}\n")
    out.append(f"Number of incorrect words: {n_wrong_words}")

    out = ''.join(out)

    with open(f'{args.directory[2]}/{theFile}_e80626nm.txt', 'w') as file:
        file.write(out)

