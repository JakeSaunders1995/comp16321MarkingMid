import os, argparse, re

parser = argparse.ArgumentParser()
parser.add_argument('english', type=open)
parser.add_argument('inputpath', type=str, help= 'paste path to input files')
parser.add_argument('outputpath', type=str, help= 'paste path to output files')

originalpath = os.getcwd()

args = parser.parse_args()
path = args.inputpath
output_path = args.outputpath
os.chdir(args.inputpath)
cwd = os.getcwd()


# storing file names into variables
input_file_names = os.listdir()

txt = '.txt'
counter = 0
for n in range(len(input_file_names)):
    if re.search(txt, input_file_names[n]):
        counter += 1

for n in range(len(input_file_names)):
    input_file_names[n] = re.split(r'\.txt', input_file_names[n])


# reads English words file
english_words = str(args.english.read().splitlines())


# -- start of sorting english words into arrays --


# removing unwanted characters from text
english_words_in_arrays = re.split(r'[#@.,\[\]"\']', english_words)
for n in range(len(english_words_in_arrays)):
    english_words = english_words + english_words_in_arrays[n]

# removing digits from text
english_words_in_arrays = re.split(r'\d', english_words)
for n in range(len(english_words_in_arrays)):
    english_words = english_words + english_words_in_arrays[n]

# removing whitespace from text
english_words = re.split(r'\s', english_words)

# removing empty arrays
a = ''
counter = 0
for n in range(len(english_words)):
    if english_words[n] == '':
        counter += 1

while counter > 0:
    english_words.remove(a)
    counter = counter - 1

# -- end of sorting english words into arrays --


# -- start of defining functions --
# read files
def read_input(file_path):
    global input_variable
    with open(file_path, 'r') as f:
        input_variable = str(f.read())

def actual_program(input_variable):
    # initialising variables
    global output
    input_01 = input_variable
    input_02 = ""
    input_03 = ""
    input_04 = ""
    ad = "@@@"
    incorrect = 0
    correct = 0
    upper = 0
    num = 0
    punctuation = 0
    punc = "#@.,[]\"\'?!;:-–—()\{\}"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"

    # removing []. as it is causing errors
    for n in range(len(input_01)):
        if input_01[n] == "[" or input_01[n] == "]" or input_01[n] == ".":
            input_01 = input_01.replace("[", "@")
            input_01 = input_01.replace("]", "@")
            input_01 = input_01.replace(".", "@")

    if re.search(ad, input_01, flags=0) != None:
                punctuation = punctuation - 2

    input_06 = re.split(r'\s', input_01)

    # finding number of punctuations
    for n in range(len(input_06)):
        for x in range(len(input_06[n])):
            if re.search(input_06[n][x], punc, flags=0) == None:
                continue
            else:
                punctuation += 1

    # finding number of uppercase words
    for n in range(len(input_06)):
        for x in range(len(input_06[n])):
            if re.search(input_06[n][x], uppercase_letters,     flags=0) == None:
                a = 5
            else:
                upper += 1

    # finding number of numbers
    for n in range(len(input_06)):
        for x in range(len(input_06[n])):
            if re.search(input_06[n][x], numbers, flags=0) ==   None:
                continue
            else:
                num += 1

    # removing unwanted characters from text
    input_01 = re.split(r'[#@.,\[\]"\'(){}?!;:-]', input_01)
    print(input_01)
    for n in range(len(input_01)):
        input_02 = input_02 + input_01[n]

    # removing digits from text
    input_03 = re.split(r'\d', input_02)
    for n in range(len(input_03)):
        input_04 = input_04 + input_03[n]

    # removing whitespace from text
    input_05 = re.split(r'\s', input_04)

    # removing empty arrays
    a = ''
    counter = 0
    for n in range(len(input_05)):
        if input_05[n] == '':
            counter += 1

    while counter > 0:
        input_05.remove(a)
        counter = counter - 1

    # converting uppercase letters to lowercase letters
    for n in range(len(input_05)):
        word = input_05[n]
        word = word.lower()
        input_05[n] = word

    # finding number of correct and incorrect spelling
    a = 0
    for n in range(len(input_05)):
        if input_05[n] == "a":
            a += 1
        for x in range(len(english_words)):
            if input_05[n] == english_words[x]:
                correct += 1

    correct = int(correct/2)
    correct = correct + a

    total = len(input_05)
    incorrect = total - correct
    username = "p55643na"

    # setting the output
    output = username + "\nFormatting ###################\nNumber of upper case letters changed: " +  str(upper) + "\nNumber of punctuations removed: " + str  (punctuation) + "\nNumber of numbers removed: " + str(num) +  "\nSpellchecking ###################" + "\nNumber of words:  " + str(total) + "\nNumber of correct words: " + str (correct) + "\nNumber of incorrect words: " + str(incorrect)     + "\n"
    
# -- end of defining functions --


# iterate through all file
counter = 0
for file in os.listdir():
    # Check whether file is in text format or not
    if path.startswith(".") or file.endswith(".txt"):
        file_path = f"{cwd}/{file}"

        # call read text file function
        read_input(file_path)
        actual_program(input_variable)


        # to make output available with ./output
        if output_path.startswith("."):
            output_path_edited = output_path[2:]
            output_path_dir = f"{originalpath}/{output_path_edited}"
            os.chdir(output_path_dir)
        else:
            os.chdir(args.outputpath)

        for n in range(len(input_file_names[counter])):
            if input_file_names[counter][n] != '':
                file_name = input_file_names[counter][n]

        counter += 1

        with open("{}_p55643na.txt".format(file_name), "w") as f:
            f.write("{}".format(output))

    else:
        break