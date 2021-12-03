import sys
import os


alphabet = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

morse_dict = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }


def read_file(fpath):
    with open(fpath,"r") as data_file:
        data = data_file.readline()
        data_file.close()
    return data

#input
input_folder = sys.argv[1]
output_folder = sys.argv[2]
folder_list = os.listdir(input_folder)
folder_list.sort()
output_txt_files = []


for i in range(len(folder_list)):
    output_txt_files.append("test_file" + str(folder_list[i][9]) + "_s50548ma.txt")


for i in range(len(folder_list)):
    filepath = folder_list[i]
    output_filepath = output_folder + "/" + output_txt_files[i]

    db = read_file(input_folder + "/" + filepath)
    for i in range(len(db)):
        if db[i] == ":":
            substring = db[i+1:]
            break
    if filepath == "test_file1.txt":
        focus_list = substring.split()
        output_string = ""
        for i in range(len(focus_list)):
            bytes_object = bytes.fromhex(focus_list[i])
            ascii_string = bytes_object.decode("ASCII")
            output_string += ascii_string
        print("\nThis is the output string for test_file2.txt: " + output_string+"\n")
    elif filepath == "test_file2.txt":
        output_string = ""
        for i in range(len(substring)):
            if substring[i] == " ":
                output_string += " "
            else:
                for j in range(len(alphabet)):
                    if substring[i] == alphabet[j].lower():
                        output_string += alphabet[j-3].lower()
                        break
        print("\nThis is the output string for test_file2.txt: " + output_string+"\n")
    elif filepath == "test_file3.txt":
        focus_list = substring.split()
        output_string = ""
        for i in range(len(focus_list)):
            if focus_list[i] == "/":
                output_string += " "
            else:
                for key in morse_dict:
                    if focus_list[i] == morse_dict[key]:
                        output_string += key.lower()
        print("\nThis is the output string for test_file3.txt: " + output_string+"\n")

    else:
        input("An error has occured. Press enter to exit program...")

    with open(output_filepath,"w") as output_file:
        output_file.writelines(output_string.lower())
        output_file.close()
                
