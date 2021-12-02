"""

Adil Hanney 8/11/2021
"""

from os import listdir, path
from argparse import ArgumentParser, Namespace

from typing import Optional


class ALGORITHMS:
    HEX = "Hex"
    CAESAR = "Caesar Cipher"
    MORSE = "Morse Code"


alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_morse = ".- / -... / -.-. / -.. / . / ..-. / --. / .... / .. / .--- / -.- / .-.. / -- / -. / --- / .--. / " \
                 "--.- / .-. / ... / - / ..- / ...- / .-- / -..- / -.-- / --.. ".split(" / ")


def getArgs() -> (str, str):
    argParser: ArgumentParser = ArgumentParser()
    argParser.add_argument("input_folder")
    argParser.add_argument("output_folder")
    args: Namespace = argParser.parse_args()
    return args.input_folder, args.output_folder


def decipher_caesar(cipher: str, shift: Optional[int]) -> str:
    cipher = cipher.lower()
    plain = ""

    if shift is None:
        shift = +3  # update: this is the only shift being used

    for letter in cipher:
        try:
            i = alphabet.index(letter)
            i -= shift
            i %= len(alphabet)
            plain += alphabet[i]
        except ValueError:  # not a letter; preserve character
            plain += letter

    return plain


def decipher_morse(morse: str) -> str:
    plain = ""

    for letter in morse.lower().split(" "):
        if letter == "/":
            plain += " "
        else:
            i = alphabet_morse.index(letter)
            plain += alphabet[i]

    return plain


if __name__ == "__main__":
    input_folder, output_folder = getArgs()

    for filename in listdir(input_folder):
        with open(path.join(input_folder, filename)) as input_file:
            algorithm_key, cipher_text = input_file.read().strip().split(":", 1)
            algorithm_suffix: Optional[str] = None

            if "(" in algorithm_key:
                parts = algorithm_key.split("(", 1)
                algorithm_key = parts[0]
                algorithm_suffix = parts[1][:-1]  # the :-1 part is to remove the other bracket

        decrypted: str
        if algorithm_key == ALGORITHMS.HEX:
            decrypted = bytes.fromhex(cipher_text).decode("UTF-8")
        elif algorithm_key == ALGORITHMS.CAESAR:
            decrypted = decipher_caesar(cipher_text, int(algorithm_suffix))
        elif algorithm_key == ALGORITHMS.MORSE:
            decrypted = decipher_morse(cipher_text)
        else:
            raise ValueError("Unknown encryption algorithm")

        filename = filename.rsplit(".", 1)[0] + "_n58949ah.txt"  # username needs to be in output filename
        with open(path.join(output_folder, filename), "w") as output_file:
            output_file.write(decrypted)
