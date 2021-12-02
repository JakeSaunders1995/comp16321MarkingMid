import argparse,string
from os import listdir
from os.path import isfile, join
def terminal_file():
    enterer = argparse.ArgumentParser(description="Spellchecker")
    enterer.add_argument("english", metavar="english", type=str, help="enter englishword file path", action="store")
    enterer.add_argument("input", metavar="In", type=str, help="enter input file path", action="store")
    enterer.add_argument("output", metavar="Out", type=str, help="enter output file path", action="store")

    global args
    args = enterer.parse_args()

    return args.english, args.input, args.output

terminal_file()

with open(f"{args.english}",'r') as english_file:
    english_line = english_file.readlines()
    for n in range(len(english_line)):
        english_line[n] = english_line[n].strip()

newfilelist = []
unordredfile = []
for fichier in listdir(args.input):
    output = ""
    if isfile(join(args.input, fichier)):
        if fichier[-4:] == ".txt" and fichier[:3] != '.DS':
            if fichier[-5] not in "0123456789":
                unordredfile.append(fichier)
            else:
                for i in range(10):
                    if fichier[-5] == f"{i}":
                        newfilelist.insert(i-1,fichier)
unordredfile.reverse()

final_list = newfilelist + unordredfile

for f in final_list:
    if isfile(join(args.input, f)):
        if f[-4::] == ".txt":
            file = open(f"{args.input}/{f}", "r")
            line = file.readlines()

            numbers = "0123456789"
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Capital_letter = 0
            Numberofnumbers = 0
            Numberofpunctuation = 0
            list_indesrable = []
            list_separated_words = []
            list_correct_words = []
            list_incorrect_words = []
            liste_de_ponctuation = []
            for i in string.punctuation:
                if i != "@" and i != "#" and i != ".":
                    liste_de_ponctuation.append(i)

            for i in range(len(line)):
                for l in range(len(line[i])):
                    if line[i][l] == ".":
                        list_indesrable += line[i][l]
                        if line[i][l:l+3] == "···":
                            Numberofpunctuation += 1
                        else :
                            Numberofpunctuation += 1
                    elif line[i][l] in liste_de_ponctuation:
                        Numberofpunctuation += 1
                        if line[i][l] not in list_indesrable:
                            list_indesrable += line[i][l]
                    elif line[i][l] in numbers:
                        Numberofnumbers += 1
                        if line[i][l] not in list_indesrable:
                            list_indesrable += line[i][l]
                    if line[i][l] in alphabet:
                        Capital_letter += 1
                for char in list_indesrable:
                    line[i] = line[i].replace(char, "")
                    line[i] = line[i].lower()

                starting_point = 0
                for m in range(len(line[i])):
                    if line[i][m] == " ":
                        needed_word = line[i][starting_point:m]
                        list_separated_words.append(needed_word)
                        starting_point = m + 1
                    elif m == len(line[i]) - 1:
                        needed_word = line[i][starting_point:m + 1]
                        list_separated_words.append(needed_word)
                    if '\n' in list_separated_words:
                        list_separated_words.remove('\n')
                    if '' in list_separated_words:
                        list_separated_words.remove('')


                Number_words_file = len(list_separated_words)
                for word in list_separated_words:
                    for k in range(len(english_line)):
                        if word == english_line[k]:
                            list_correct_words.append(word)
                    if word not in list_correct_words:
                        list_incorrect_words.append(word)

                Numbers_correctwords = len(list_correct_words)
                Numbers_incorrectwords = len(list_incorrect_words)
                text = "p40515mt\n" \
                       "Formatting #################\n" \
                       f"Number of upper case words changed: {Capital_letter}\n" \
                       f"Number of punctuations removed: {Numberofpunctuation}\n" \
                       f"Number of numbers removed: {Numberofnumbers}\n" \
                       "Spellchecking ###################\n" \
                       f"Number of words: {Number_words_file}\n" \
                       f"Number of correct words: {Numbers_correctwords}\n" \
                       f"Number of incorrect words: {Numbers_incorrectwords}\n"



    f2 = f[:-4]
    with open(f"{args.output}/{f2}_p40515mt.txt",'w') as output_file:
        output_file.write(text)
        output_file.close()
