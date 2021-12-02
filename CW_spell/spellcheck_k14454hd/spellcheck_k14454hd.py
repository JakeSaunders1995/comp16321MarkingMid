"""Python Midterm Program 3."""

from sys import argv
import re
from os import listdir
from os.path import isfile, join


def main(english_words_file_path, input_folder_path, output_folder_path):
    """Run the main program.

    Args:
        inputFilePath: The file path to the input file
        outputFilePath: The file path to the output file
    """
    files = find_file_names_in_folder(input_folder_path)
    for file in files:
        print(file)
        # Join the file name and input folder path
        full_input_file_path = join(input_folder_path, file)

        # Get the data from the file
        data = read_input_from_file(full_input_file_path)
        # Replace new lines from file
        data = remove_newlines(data)

        formatted, upper_count, symbol_count, num_count = format_text(data)

        words = create_word_list(formatted)

        num_correct = spellchecking(words, english_words_file_path)

        text = create_output_text(
            upper_count,
            symbol_count,
            num_count,
            len(words),
            num_correct
        )

        output_file_path = make_output_file_path(file, output_folder_path)

        save_to_file(output_file_path, text)


def make_output_file_path(input_file_name, output_folder):
    """Generate the output file path for a given input file.

    Args:
        input_file_name: The name of the input file to make an output for

    Returns:
        A file path to save the output file to
    """
    file_name = input_file_name[:-4] + "_k14454hd" + input_file_name[-4:]
    return join(output_folder, file_name)


def find_file_names_in_folder(folder_file_path):
    """Return a list of all the file paths in a folder.

    Args:
        folder_file_path: The file path to the folder to search in

    Returns:
        A list of strings containing the file paths
    """
    files = []
    for file in listdir(folder_file_path):
        if isfile(join(folder_file_path, file)) and file.endswith(".txt"):
            files.append(file)

    return files


def read_input_from_file(file):
    """Retrieve all the data in a file.

    Args:
        file: The filepath to the file to read

    Returns:
        The first line from the file as a string
    """
    lines = ""
    with open(file, mode='r') as f:
        lines = f.read()

    return lines


def remove_newlines(data):
    """Replace the new lines in a string with spaces.

    Args:
        data: The string which contains the contents of a txt file

    Returns:
        A string with no new line characters
    """
    return data.replace("\n", " ")


def create_word_list(data):
    """Convert a string into a list of words.

    Args:
        data: A string to turn into a list of words

    Returns:
        A list of words in the string
    """
    words = data.split()

    return words


def remove_ellipses(data_string):
    """Remove ellipses from a string of text.

    Args:
        data_string: The string from which to remove ellipses from

    Returns:
        The string with no ellipses and the count of ellipses removed
    """
    formatted = data_string.replace("...", "")
    return formatted, (len(data_string) - len(formatted)) / 3


def remove_numbers(data_string):
    """Remove the numbers from a string of text.

    Args:
        data_string: The string from which to remove numbers from

    Returns:
        The string with no numbers and the count of numbers removed
    """
    formatted = "".join(c for c in data_string if not c.isdigit())
    return formatted, len(data_string) - len(formatted)


def remove_symbols(data_string):
    """Remove the symbols from a string of text.

    Args:
        data_string: The string from which to remove symbols from

    Returns:
        The string with no symbols and the count of symbols removed
    """
    formatted = "".join(c for c in data_string if c.isalpha() or c == " ")
    return formatted, len(data_string) - len(formatted)


def replace_upper_case(data_string):
    """Replace the upper case letters with lower case letters in a string.

    Args:
        data_string: The string from which to replace upper case letters from

    Returns:
        String with no upper case letters and the count of characters replaced
    """
    formatted = ""
    count = 0
    for i in range(len(data_string)):
        if data_string[i].isupper():
            formatted += data_string[i].lower()
            count += 1
        else:
            formatted += data_string[i]

    return formatted, count


def format_text(data_string):
    """Format the text to remove numbers and symbols.

    Args:
        data: The list of strings.

    Returns:
        The formatted string
    """
    # Remove Ellipses
    formatted, ellipsis_count = remove_ellipses(data_string)

    # Remove Numbers
    formatted, numbers_count = remove_numbers(formatted)

    # Remove symbols
    formatted, symbol_count = remove_symbols(formatted)

    # Replace upper case
    formatted, upper_case_count = replace_upper_case(formatted)

    symbol_count += ellipsis_count

    return formatted, upper_case_count, symbol_count, numbers_count


def spellchecking(words, words_file_path):
    """Determine the number of correct and incorrect words in the string.

    Args:
        words: The list of words to check

    Returns:
        The number of correct and incorrect words in the list
    """
    correct = 0
    incorrect = 0

    with open(words_file_path) as fh:
        file_data = fh.read()
        for word in words:
            if re.search("^" + word + "$", file_data, re.MULTILINE):
                correct += 1
            else:
                incorrect += 1

    return correct


def create_output_text(num_upper, num_punc, num_num, num_words, num_correct):
    """Create the text to be output for each file.

    Args:
        num_upper: The number of upper case words changed
        num_punc: The number of punctuation symbols removed
        num_num: The number of numbers removed
        num_words: The number of words in total
        num_correct: The number of correct words

    Returns:
        The text to be saved to the output file as a list of lines
    """
    output_lines = [
        "Formatting ###################",
        "Number of upper case letters changed: ",
        "Number of punctuations removed: ",
        "Number of numbers removed: ",
        "Spellchecking ###################",
        "Number of words: ",
        "Number of correct words: ",
        "Number of incorrect words: "
    ]
    output_lines[1] += str(int(num_upper))
    output_lines[2] += str(int(num_punc))
    output_lines[3] += str(int(num_num))
    output_lines[5] += str(int(num_words))
    output_lines[6] += str(int(num_correct))
    output_lines[7] += str(int(num_words - num_correct))

    return output_lines


def save_to_file(file, lines):
    """Save the given score to a specified file.

    Args:
        file: The filepath to where the file should be saved
        lines: The lines to save to the file
    """
    with open(file, mode='w') as f:
        for line in lines:
            f.write(line + "\n")


if __name__ == "__main__":
    args = argv
    main(args[1], args[2], args[3])
