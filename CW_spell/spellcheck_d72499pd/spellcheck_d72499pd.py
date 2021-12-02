import sys, os

def format(text):
    global punctuation_removed, numbers_removed, upper_removed
    punctuation = "?!,;:/'{}[]()’\"-—…"
    numbers = "0123456789"
    upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation_removed = 0
    numbers_removed = 0
    upper_removed = 0
    formatted_text = ""
    i = 0
    while i < len(text):
        if text[i] in numbers:
            numbers_removed += 1
        elif text[i] in punctuation:
            punctuation_removed += 1
        elif text[i] in upperCase:
            upper_removed += 1
            formatted_text += text[i].lower()
        elif text[i] == ".":
            punctuation_removed += 1
            if (i+2) < len(text):
                if text[i+1] == "." and text[i+2] == ".":
                    i += 3
                    continue
        else:
            formatted_text += text[i]
        i += 1
    return formatted_text

def spellcheck(text, correct_words):
    global correct, incorrect, words_number
    words = text.split()
    words_number = len(words)
    correct = 0
    incorrect = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in words:
        newWord = ""
        i = i.rstrip()
        for j in i:
            if j in alphabet:
                newWord += j
        if newWord in correct_words:
            correct += 1
        else:
            incorrect += 1

files = sys.argv
library = files[1]
input_file_path = files[2]
output_file_path = files[3]
correct_words = []
with open(library, "r") as file:
    for line in file:
        line = line.rstrip()
        correct_words.append(line)
files_names = os.listdir(input_file_path)
count = 0
with os.scandir(input_file_path) as files:
    for entry in files:
        with open(entry, "r") as file:
            line = file.read()
            i = 0
            file_name = ""
            while files_names[count][i] != ".":
                file_name += files_names[count][i]
                i+=1
            file_name += "_d72499pd.txt"
            line = format(line)
            spellcheck(line, correct_words)
            text_to_write = []
            text_to_write.append("d72499pd\n")
            text_to_write.append("Formatting ###################\n")
            text_to_write.append("Number of upper case letters changed: " + str(upper_removed)+ "\n")
            text_to_write.append("Number of punctuations removed: " + str(punctuation_removed) + "\n")
            text_to_write.append("Number of numbers removed: " + str(numbers_removed) + "\n")
            text_to_write.append("Spellchecking ###################\n")
            text_to_write.append("Number of words: " + str(words_number) + "\n")
            text_to_write.append("Number of correct words: " + str(correct) + "\n")
            text_to_write.append("Number of incorrect words: " + str(incorrect))
            save_file = os.path.join(output_file_path, file_name)
            with open(save_file, "w") as output_file:
                for j in text_to_write:
                    output_file.write(j)
            count += 1
