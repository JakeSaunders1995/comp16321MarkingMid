import os, argparse, re

parser = argparse.ArgumentParser()
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

# defining functions
def read_input(file_path):
    global input_variable
    with open(file_path, 'r') as f:
        input_variable = str(f.read())
def morsecode(n):
    if input_03[n] == "/":
        input_03[n] = " "
    elif input_03[n] == ".-":
        input_03[n] = "a"
    elif input_03[n] == "-...":
        input_03[n] = "b"
    elif input_03[n] == "-.-.":
        input_03[n] = "c"
    elif input_03[n] == "-..":
        input_03[n] = "d"
    elif input_03[n] == ".":
        input_03[n] = "e"
    elif input_03[n] == "..-.":
        input_03[n] = "f"
    elif input_03[n] == "--.":
        input_03[n] = "g"
    elif input_03[n] == "....":
        input_03[n] = "h"
    elif input_03[n] == "..":
        input_03[n] = "i"
    elif input_03[n] == ".---":
        input_03[n] = "j"
    elif input_03[n] == "-.-":
        input_03[n] = "k"
    elif input_03[n] == ".-..":
        input_03[n] = "l"
    elif input_03[n] == "--":
        input_03[n] = "m"
    elif input_03[n] == "-.":
        input_03[n] = "n"
    elif input_03[n] == "---":
        input_03[n] = "o"
    elif input_03[n] == ".--.":
        input_03[n] = "p"
    elif input_03[n] == "--.-":
        input_03[n] = "q"
    elif input_03[n] == ".-.":
        input_03[n] = "r"
    elif input_03[n] == "...":
        input_03[n] = "s"
    elif input_03[n] == "-":
        input_03[n] = "t"
    elif input_03[n] == "..-":
        input_03[n] = "u"
    elif input_03[n] == "...-":
        input_03[n] = "v"
    elif input_03[n] == ".--":
        input_03[n] = "w"
    elif input_03[n] == "-..-":
        input_03[n] = "x"
    elif input_03[n] == "-.--":
        input_03[n] = "y"
    elif input_03[n] == "--..":
        input_03[n] = "z"
    else:
        input_03[n] = " That is not an alphabet. "
def hexadecimal():
    global output
    bytes_object = bytes.fromhex(input_04)
    output = bytes_object.decode("ASCII")
def caesar():
    global input_02
    global output
    output = ""
    real_alphabet = "abcdefghijklmnopqrstuvwxyz"
    for n in range(len(input_02)):
        for x in range(len(real_alphabet)):
            if input_02[n] == real_alphabet[x]:
                location = x - 3
                output = output + real_alphabet[location]
        if input_02[n] == " ":
            output = output + " "
def actual_program(input_01):
    global output
    global input_02
    global input_03
    global input_04
    input_04 = ""
    # determine cipher type
    cipher = input_01[0]

    if cipher == "H":
        cipher_type = "Hex"
    elif cipher == "C":
        cipher_type = "Caesar Cipher"
    elif cipher == "M":
        cipher_type = "Morse Code"

    if cipher_type == "Morse Code":
        input_02 = input_01[11:]
        input_03 = re.split(r'\s', input_02)
        for n in range(len(input_03)):
            morsecode(n)
        for n in range(len(input_03)):
            output = output + input_03[n]
    elif cipher_type == "Caesar Cipher":
        input_02 = input_01[18:]
        caesar()
    elif cipher_type == "Hex":
        input_02 = input_01[4:]
        input_03 = re.split(r'\s', input_02)
        for n in range(len(input_03)):
            input_04 = input_04 + input_03[n]
        hexadecimal()
    else:
        print("I don't know what's going on")

# iterate through all file
counter = 0
for file in os.listdir():
    output = ""
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
        output = output.lower()

        with open("{}_p55643na.txt".format(file_name), "w") as f:
            f.write("{}".format(output))

    else:
        break