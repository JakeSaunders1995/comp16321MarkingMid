"""Python Midterm Program 1."""
# python3 rugby_k14454hd.py ./inputs ./outputs

from sys import argv
from os import listdir
from os.path import isfile, join


def main(input_folder_path, output_folder_path):
    """Run the main program.

    Args:
        inputFilePath: The file path to the input file
        outputFilePath: The file path to the output file
    """
    files = find_file_names_in_folder(input_folder_path)
    for file in files:
        # Join the file name and input folder path
        full_input_file_path = join(input_folder_path, file)

        # Get the data from the file
        data = read_input_from_file(full_input_file_path)
        split_data = split_data_from_file(data)
        # Check for empty file
        if split_data == [] or split_data == [""]:
            print("Empty file... Skipping.")
            continue

        # Calculate the score
        score = calculate_scores(split_data)
        # Get the file path to save the output to
        output_file_path = make_output_file_path(file, output_folder_path)
        save_to_file(output_file_path, score)


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
    print(file)
    line = ""
    with open(file, mode='r') as f:
        line = f.readline()

    return line[1:]


def calculate_scores(scores):
    """Calculate the scores for each team.

    Args:
        scores: A list of strings which details the point scoring moments of the game

    Returns:
        The final score of the game as a string
    """
    team_1_score = 0
    team_2_score = 0
    points = {
        "t": 5,
        "c": 2,
        "p": 3,
        "d": 3
    }
    for score in scores:
        if score[0] == "1":
            team_1_score += points[score[1]]
        else:
            team_2_score += points[score[1]]

    return str(team_1_score) + ":" + str(team_2_score)


def split_data_from_file(data_from_file):
    """Split the data retrieved from the file.

    This functions splits the data on the "T" character

    Args:
        data_from_file: The data from the file

    Returns:
        A list containing each point scoring moment in the game
    """
    return data_from_file.split("T")


def save_to_file(file, score):
    """Save the given score to a specified file.

    Args:
        file: The filepath to where the file should be saved
        score: The final score to save in the file
    """
    with open(file, mode='w') as f:
        f.write(score)


if __name__ == "__main__":
    args = argv
    main(args[1], args[2])
