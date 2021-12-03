import argparse, os

numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
uppercase_letters_list = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
punctuation_list = [".", "?", "!", ",", ":", ";", "-", "—", "(", ")", "{", "}", "[", "]", """'""", '"']

parser = argparse.ArgumentParser()
parser.add_argument("english_words", type=argparse.FileType("r"))
parser.add_argument("input_directory")
parser.add_argument("output_directory")
args = parser.parse_args()
input_files = os.listdir(args.input_directory)


correctly_spelt_words_list = []
for line in args.english_words:
    correctly_spelt_words_list.append(line.strip())

for filename in input_files:
    input_file = open(os.path.join(args.input_directory, filename), "r")
    text = (input_file.readlines())[0]
    word = ""
    numbers = 0
    uppercase_letters = 0
    punctuation = 0
    words = 0
    correctly_spelt_words = 0
    for x in range(len(text)):
        character = text[x]
        if character != " ":
            if character in numbers_list:
                numbers += 1
            elif character in uppercase_letters_list:
                uppercase_letters += 1
                word = word + character
            elif character in punctuation_list:
                punctuation += 1
                if x > 0:
                    if (text[x] == "." and text[x+1] == "." and text[x+2] == "."):
                        punctuation = punctuation - 1
                        print("this is the first dot in the ellipses")
                    if (text[x-1] == "." and text[x] == "." and text[x+1] == "."):
                        punctuation = punctuation - 1
                        print("this is the second dot in the ellipses")

                else:
                    if (text[x] == "." and text[x+1] == "." and text[x+2] == "."):
                        punctuation = punctuation - 1
                        print("this is the first dot in the ellipses")
            else:
                word = word + character
        else:
            if word != "":
                words += 1
            if word.lower() in correctly_spelt_words_list:
                correctly_spelt_words += 1
            word = ""
    if word != "":
        words += 1
        if word.lower() in correctly_spelt_words_list:
            correctly_spelt_words += 1
    print("\n\n")
    print("file: " + filename)
    print("\n")
    print("uppercase: " + str(uppercase_letters))
    print("punctuation: " + str(punctuation))
    print("numbers: " + str(numbers))
    print("words: " + str(words))
    print("correct words: " + str(correctly_spelt_words))
    print("incorrect words: " + str(words-correctly_spelt_words))

    filename = filename[:-4] + "_x47813as.txt"
    output_file = open(os.path.join(args.output_directory, filename), "x")
    output_file.close
    output_file = open(os.path.join(args.output_directory, filename), "a")
    output_file.write("_x47813as")
    output_file.write("\nFormatting ####################")
    output_file.write("\nNumber of upper case letters changed: " + str(uppercase_letters))
    output_file.write("\nNumber of punctuations removed: " + str(punctuation))
    output_file.write("\nNumber of numbers removed: " +  str(numbers))
    output_file.write("\nSpellchecking ###################")
    output_file.write("\nNumber of words: " + str(words))
    output_file.write("\nNumber of correct words: " + str(correctly_spelt_words))
    output_file.write("\nNumber of incorrect words: " + str(words-correctly_spelt_words))
    output_file.close
    input_file.close
