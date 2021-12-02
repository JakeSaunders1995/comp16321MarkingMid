import os
import argparse

empty_string = ""


def hex(s):
    global empty_string
    for word in s.split():
        ascii = int(word, 16)
        empty_string = empty_string + (chr(ascii))


def caesar(s):
    global empty_string
    s = s.lower()
    for i in s:
        if i.isalpha():
            dec = (ord(i[0]) - ord('a') - 3) % 26
            letter = (chr(dec + ord('a')))
            empty_string = empty_string + letter
        else:
            empty_string = empty_string + i


def morse(s):
    global empty_string
    encode = {'.-': 'a', '-...': 'b', '-.-.': 'c',
              '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
              '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm',
              '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's',
              '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y',
              '--..': 'z', '..--..': '?',
              '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '.-.-.-': '.',
              '--..--': ',', "..--.": '?', '-.-.-.': ';',
              '---...': ':', '-....-': '-', ".----.": '\'', '..--.-': '_',
              '-.--.': '(', '-.--.-': ')', '-...-': '=', '.-.-.': '+',
              '.--.-.': '@', '-.-.--': '!', '-..-.': '/',
              }

    for word in s.split():
        if word == "/":
            empty_string = empty_string + " "
        else:
            letter = encode[word]
            empty_string = empty_string + letter


def main(s):
    slice_index = string.find(':')
    algorithm = string[0:slice_index]
    code = string[slice_index + 1:]

    if algorithm[0] == 'H':
        hex(code)
    elif algorithm[0] == 'C':
        caesar(code)
    else:
        morse(code)

    return empty_string.lower()


parser = argparse.ArgumentParser()
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder
input_files = os.listdir(f"./{input_folder}")

for file in input_files:
    f = open(f"{input_folder}/{file}", "r")
    string = f.read().replace("\n", " ")
    string = string.strip()
    empty_string = ""
    ans = main(string)
    k = file.find('.')
    output_file = file[0:k] + "_h63651bn" + file[k:]
    g = open(f"{output_folder}/{output_file}", "w")
    g.write(ans)
    f.close()
    g.close()

