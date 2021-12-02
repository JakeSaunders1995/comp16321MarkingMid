import argparse, os

def directory_path(string):
    if os.path.isdir(string):
        return string
    else:
        return str(string)

# input text file
python_file_location = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('engwords', type = argparse.FileType('r'))
parser.add_argument('inputpath', type=directory_path)
parser.add_argument('outputpath', type=directory_path)
args = parser.parse_args()
outputStringList = []
name_of_file_list = []
os.chdir(args.inputpath)
english_words = args.engwords.readlines()
english_words = list(map(lambda x:x.strip(), english_words))

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, 'r') as f:
            name_of_file = str(file)[0:len(str(file))-4] + "_k71182kt.txt"
            name_of_file_list.append(name_of_file)
            inputString = str(f.read())
            # upper case words transforming
            upper = 0
            for i in inputString:
                if (i.isupper()):
                    upper = upper + 1
            inputString = inputString.lower()

            # removing punctuation
            punct_count = 0
            # punctuation = ".?!,:;-\"<>()[]{}+=%^&*/"
            punctuation = ".?!,:;-()[]{}'\""

            while "..." in inputString:
                inputString = inputString.replace("...", "", 1)
                punct_count = punct_count + 1

            for char in punctuation:
                while char in inputString:
                    inputString = inputString.replace(char, "", 1)
                    punct_count = punct_count + 1

            while "\'" in inputString:
                inputString = inputString.replace("\'", "", 1)
                punct_count = punct_count + 1

            # removing numbers
            num_count = 0
            numbers = "0123456789"
            for char in numbers:
                while char in inputString:
                    inputString = inputString.replace(char, "", 1)
                    num_count = num_count + 1

            # total number of words count
            word_list = inputString.split()
            total_words = len(word_list)

            # correct and incorrect words count
            correct_words_count = 0
            incorrect_words_count = 0
            for word in word_list:
                if word in english_words:
                    correct_words_count = correct_words_count + 1
                else:
                    incorrect_words_count = incorrect_words_count + 1

            outputString = "k71182kt\nFormatting ###################\nNumber of upper case letters changed: " + str(upper) + "\nNumber of punctuations removed: " + str(punct_count) + "\nNumber of numbers removed: " + str(num_count) +"\nSpellchecking ###################" + "\nNumber of words: " + str(total_words) + "\nNumber of correct words: " + str(correct_words_count) + "\nNumber of incorrect words: " + str(incorrect_words_count)
            outputStringList.append(outputString)

os.chdir(python_file_location)
directory = args.outputpath
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)
    os.chdir(directory)

output_count = 0
for i in name_of_file_list:
    output_text_file = open(i, 'w')
    output_text_file.write(outputStringList[output_count])
    output_text_file.close()
    output_count = output_count + 1
