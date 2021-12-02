import os, argparse, re

input_folder_path = ""
output_folder_path = ""
EnglishWords = ""

punctuations =['!', '"', '$', '%', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '…','—']
punctuationString = '!"$%\'()*+,-./:;<=>?[\\]^_`{|}~—…'


def cmdline(): # To get arguments from command line
    global input_folder_path, output_folder_path, EnglishWords
    parser = argparse.ArgumentParser()
    parser.add_argument('Englishwords', type=str)
    parser.add_argument('input_path', type=str)
    parser.add_argument('output_path', type=str)
    args = parser.parse_args()

    EnglishWords = args.Englishwords
    input_folder_path = args.input_path
    output_folder_path = args.output_path


def fileextraction(arg):
    files = os.listdir(arg)
    for file in files:
        if file.endswith(".txt"): continue
        else: files.remove(file)
    return files

def inputfile(arg): # read the input file and store it in a variable
    with open(os.path.join(input_folder_path,arg),"r+") as file:
        x = file.read()
        return x


def outputfile(arg, arg1):
    if os.path.exists(output_folder_path):
        pass
    else: os.makedirs(output_folder_path)
    with open(os.path.join(output_folder_path,arg1),"w+") as file:
        file.writelines(arg)


def match(checkfile, inpt):
    Correctword_counter, Incorrectword_counter = 0, 0
    with open(checkfile,"r+") as file:
        data = file.read().splitlines()
        for i in inpt:
            if i in data: Correctword_counter += 1
            else: Incorrectword_counter += 1
    file.close()
    return Correctword_counter, Incorrectword_counter


def punctuationcounter(string, punctuationlist, punctuationstring):
    count = 0
    if "..." in string:
        string = string.replace("...","…")
    for i in string:
        if i in punctuationlist:
            count += 1
    string = re.sub(f"[{punctuationstring}]","",string)
    return count, string


def numbercounter(newstr):
    count = 0
    for i in newstr:
        if i.isdigit(): count += 1
    newstr = re.sub("[0-9]","",newstr)
    return count, newstr


def wordcounter(somestring):
    words = somestring.split()
    count_for_uppercase = 0
    for idx in range(len(words)):
        for i in words[idx]:
            if i.isupper(): count_for_uppercase += 1
        words[idx] = words[idx].lower()
    total_words = len(words)
    return count_for_uppercase, total_words, words


def main():
    cmdline()
    global EnglishWords
    if os.path.isfile(EnglishWords) == True:
        pass
    else:
        EnglishWords = os.path.join(EnglishWords,"EnglishWords.txt")
    input_files = fileextraction(input_folder_path)
    for testfile in input_files:
        stringdata = inputfile(testfile)
        punctuation_count, stringnopuncts = punctuationcounter(stringdata, punctuations, punctuationString)
        number_count, finalstring = numbercounter(stringnopuncts)
        uppercase_count, total_words, words = wordcounter(finalstring)
        Correct_Words, Incorrect_words = match(EnglishWords, words)
        datalist = ["h25471ds", "\nFormatting ###################", f"\nNumber of upper case letters changed: {uppercase_count}", f"\nNumber of punctuations removed: {punctuation_count}", f"\nNumber of numbers removed: {number_count}", "\nSpellchecking ###################", f"\nNumber of words: {total_words}", f"\nNumber of correct words: {Correct_Words}", f"\nNumber of incorrect words: {Incorrect_words}"]
        outputfilename = re.split("[.]",testfile)[0] + "_h25471ds.txt"
        outputfile(datalist,outputfilename)



main()
