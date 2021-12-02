"""Python Midterm Program 2."""

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
        cipher = split_data(data)
        plain = decrypt(cipher)

        if plain is None:
            print("Could not decrypt. Skipping...")
            continue

        # Get the file path to save the output to
        output_file_path = make_output_file_path(file, output_folder_path)
        save_to_file(output_file_path, plain)


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


def decrypt(cipher):
    """Run the appropriate decryption on the cipher text.

    Args:
        cipher: The list containing the cipher type and text
    """
    plain_text = None
    if cipher[0] == "Hex":
        plain_text = decrypt_hex(cipher[1])
    elif cipher[0] == "Morse Code":
        plain_text = decrypt_morse(cipher[1])
    elif cipher[0] == "Caesar Cipher(+3)":
        plain_text = decrypt_caesar(cipher[1])
    else:
        print("Unknown Cipher Type...")

    return plain_text


def decrypt_morse(cipher_text):
    """Run the morse code decryption algorithm.

    Args:
        cipher_text: The text to run the algorithm on

    Returns:
        A string with the plain text
    """
    morse = {'.-': 'a', '-...': 'b', '-.-.': 'c',
             '-..': 'd', '.': 'e', '..-.': 'f',
             '--.': 'g', '....': 'h', '..': 'i',
             '.---': 'j', '-.-': 'k', '.-..': 'l',
             '--': 'm', '-.': 'n', '---': 'o',
             '.--.': 'p', '--.-': 'q', '.-.': 'r',
             '...': 's', '-': 't', '..-': 'u',
             '...-': 'v', '.--': 'w', '-..-': 'x',
             '-.--': 'y', '--..': 'z', '-----': '0',
             '.----': '1', '..---': '2', '...--': '3',
             '....-': '4', '.....': '5', '-....': '6',
             '--...': '7', '---..': '8', '----.': '9',
             '.-.-.-': '.', '..--..': '?', '-.-.--': '!',
             '--..--': ',', '---...': ':', '-....-': '-',
             '.----.': "'", '-..-.': '/', '-.--.': '(',
             '-.--.-': ')', '.-..-.': '"', '.-.-.': '+',
             '.--.-.': '@', '': ''}
    plain_text = ""
    words = cipher_text.split("/")
    for word in words:
        word_plain = ""
        letters = word.split(" ")
        for letter in letters:
            word_plain += morse[letter]

        plain_text += word_plain + " "

    return plain_text


def decrypt_caesar(cipher_text):
    """Run the caesar cipher decryption algorithm.

    Args:
        cipher_text: The text to run the algorithm on

    Returns:
        A string with the plain text
    """
    plain_text = ""
    words = cipher_text.split(" ")
    for word in words:
        word_plain = ""
        for letter in word:
            x = ord(letter)

            word_plain += chr((((x - 3) - 97) % 26) + 97)

        plain_text += word_plain + " "

    return plain_text


def decrypt_hex(cipher_text):
    """Run the hex code decryption algorithm.

    Args:
        cipher_text: The text to run the algorithm on

    Returns:
        A string with the plain text
    """
    plain_text = ""
    letters = cipher_text.split(" ")
    for letter in letters:
        x = int(letter, 16)
        plain_text += chr(x)

    return plain_text


def split_data(data):
    """Split the data into a list containing the cipher type and the cipher text.

    Args:
        data: The data from the file

    Returns:
        The list containing the cipher type and text
    """
    return data.split(":")


def read_input_from_file(file):
    """Retrieve all the data in a file.

    Args:
        file: The filepath to the file to read

    Returns:
        The first line from the file as a string
    """
    line = ""
    with open(file, mode='r') as f:
        line = f.readline()

    return line


def save_to_file(file, plain_text):
    """Save the given score to a specified file.

    Args:
        file: The filepath to where the file should be saved
        score: The final score to save in the file
    """
    with open(file, mode='w') as f:
        f.write(plain_text)


if __name__ == "__main__":
    args = argv
    main(args[1], args[2])
