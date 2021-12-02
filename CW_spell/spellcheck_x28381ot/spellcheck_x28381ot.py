
import os
import sys


command_line_arguments = sys.argv
dictionary_filename = command_line_arguments[1][2:]
input_directory_name = command_line_arguments[2][2:]
output_directory_name = command_line_arguments[3][2:]


# ---- Main Body of Execution

def execute(inputs, output_path):
  for file in inputs:
    input_data = extract_input_data_from_filename(file)

    results = clean_input(input_data)
    cleaning_data = results[0]
    clean_data = results[1]

    english_dictionary = load_dictionary(dictionary_filename)
    spellcheck_data = spellcheck(clean_data, english_dictionary)

    spellcheck_report = format_results(cleaning_data, spellcheck_data)
    output_filename = create_empty_file(output_path, file)
    write_data_to_file(spellcheck_report, output_filename)
    print("Spellcheck complete, report available in  " + str(output_filename) + ".")

# ---- File Operations

def load_dictionary(filename):
    file = open('./' + filename, 'r')
    dictionary = file.read()

    file.close()
    return dictionary

def extract_input_data_from_filename(input_filename):
    file = open('./' + input_directory_name + '/' + input_filename, 'r')
    data = file.read()

    if (data[-2:] == '\n'):
        data = data[:-2]

    file.close()
    return data


def create_empty_file(location, input_filename):
    new_filename = input_filename[:-4] + '-prog-3-output.txt'
    open('./' + location + '/' + new_filename, 'x').close()
    return new_filename


def get_filenames_from_input_directory(directory_name):
  directory_contents = os.listdir('./' + directory_name)
  files = []

  for item in directory_contents:
    if(item[-4:] == '.txt'):
        files.append(item)

  return files


def write_data_to_file(data, filename):
    output_file = open('./' + output_directory_name + '/' + filename, 'w')

    output_file.write(data)

    output_file.close()
    return


# ---- Data Processing

def format_results(cleaning_data, spellcheck_data):
    results = """
        x238381ot
        Formatting ###################
        Number of upper case letters changed: {case_change}
        Number of punctuations removed: {removed_punctuation}
        Number of numbers removed: {removed_numbers}
        Spellchecking ###################
        Number of words: {total_words}
        Number of correct words: {correct_words}
        Number of incorrect words: {incorrect_words}
    """.format(case_change=cleaning_data["case_change"],
               removed_punctuation=cleaning_data["removed_punctuation"],
               removed_numbers=cleaning_data["removed_numbers"],
               total_words=spellcheck_data["total_words"],
               correct_words=spellcheck_data["correct_words"],
               incorrect_words=spellcheck_data["incorrect_words"])

    return results

def clean_input(data):
    results = []
    cleaning_data = {}
    cleaning_data["case_change"] = count_character_occurrance(data, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    cleaning_data["removed_punctuation"] = count_character_occurrance(data, "!,./?\[{]})\'(-_=+<>~#|\"£$%^&*")
    cleaning_data["removed_numbers"] = count_character_occurrance(data, "123456789")
    results.append(cleaning_data)

    cleaned_data = []
    words = data.split(" ")

    for word in words:
        clean_word = ""

        for character in word:
            if character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                 clean_word += character

        if "\n" not in clean_word and clean_word and " " not in clean_word:
            cleaned_data.append(clean_word.lower())

    results.append(cleaned_data)
    return results


def spellcheck(data, dictionary):
    spellcheck_data = {}
    spellcheck_data["total_words"] = len(data)
    correct_word_count = 0
    incorrect_word_count = 0

    for word in data:
        if word in dictionary:
            correct_word_count += 1
        else:
            incorrect_word_count += 1


    spellcheck_data["correct_words"] = correct_word_count
    spellcheck_data["incorrect_words"] = incorrect_word_count

    return spellcheck_data


def count_character_occurrance(string, characters_as_string):
    char_count = 0

    for i in characters_as_string:
        char_count += string.count(i)

    return char_count


# ---- Actual Execution

test_results = {"case_change": 1,
                "removed_punctuation": 2,
                "removed_numbers": 3}
test_spellcheck = {"total_words": 4,
                "correct_words": 5,
                "incorrect_words": 6}

print(clean_input("t!2E?.s£/t \[d*a4!!T\(77&a")[1]) # "test data"
print(format_results(test_results, test_spellcheck))

execute(get_filenames_from_input_directory(input_directory_name), output_directory_name)
