import os.path as path
import sys, os

def morse_code(to_decrypt):
    morse_code_dict = {
    ".-":"a",
    "-...":"b",
    "-.-.":"c",
    "-..":"d",
    ".":"e",
    "..-.":"f",
    "--.":"g",
    "....":"h",
    "..":"i",
    ".---":"j",
    "-.-":"k",
    ".-..":"l",
    "--":"m",
    "-.":"n",
    "---":"o",
    ".--.":"p",
    "--.-":"q",
    ".-.":"r",
    "...":"s",
    "-":"t",
    "..-":"u",
    "...-":"v",
    ".--":"w",
    "-..-":"x",
    "-.--":"y",
    "--..":"z",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
    "-----":"0",
    ".-.-.-":".",
    "--..--":",",
    "..--..":"?",
    ".----.":"'",
    "-.-.--":"!",
    "-..-.":"/",
    "-.--.":"(",
    "-.--.-":")",
    ".-...":"&",
    "---...":":",
    "-.-.-.":";",
    "-....-":"-",
    ".-..-.":'"'
    }
    string_to_build = ""

    to_decrypt = to_decrypt.split(" / ")
    for word in to_decrypt:
        word = word.split(" ")
        for character in word:
            try:
                string_to_build = string_to_build + morse_code_dict[character]
            except:
                print("morse code character not found, exiting...")
                sys.exit()
        string_to_build = string_to_build + " "
    return string_to_build

def caesar(to_decrypt):
    alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    alphabet3 = ("d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c")
    to_decrypt = to_decrypt.lower()
    string_to_build = ""

    for character in list(to_decrypt):
        if character in alphabet:
            index = alphabet3.index(character)
            string_to_build = string_to_build + alphabet[index]
        else:
            string_to_build = string_to_build + character

    return string_to_build

def hexadecimal(to_decrypt):
    to_decrypt = to_decrypt.split(" ")
    string_to_build = ""
    for letter in to_decrypt:
        string_to_build = string_to_build + chr(int(letter, 16))
    return string_to_build

def output_write(output_str, output_path, file):
    output_file = open(path.join(output_path, path.basename(file)[:-4]+"_s65422mt.txt"), "w")
    output_file.writelines(output_str)
    output_file.close()


if __name__ == "__main__":
    input_path, output_path = sys.argv[1], sys.argv[2]
    if path.isdir(input_path):
        for file in os.scandir(input_path):
            my_file = open(str(file.path), "r")
            input_str = my_file.readline()
            my_file.close()
            input_str = input_str.split(":",1)
            if input_str[0].lower().startswith("h"):
                output_str = hexadecimal(input_str[1])
            elif input_str[0].lower().startswith("c"):
                output_str = caesar(input_str[1])
            elif input_str[0].lower().startswith("m"):
                output_str = morse_code(input_str[1])
            else:
                print("unrecognised specified encoding algorithm. exiting...")
                sys.exit()
            output_write(output_str, output_path, file)

    else:
        print("not given directory, exiting program...")
        sys.exit()
