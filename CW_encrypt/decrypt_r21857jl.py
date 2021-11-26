import argparse
import os
from enum import Enum

#  from wikipedia
# https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
MORSE_CODES = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
}


class Algo(Enum):
    HEX = (1,)
    CAESAR = (2,)
    MORSE = (3,)


def parse(contents: str):
    contents = contents.split(":", maxsplit=1)
    algo = contents[0]
    if algo == "Hex":
        algo = Algo.HEX
    elif algo == "Caesar Cipher(+3)":
        algo = Algo.CAESAR
    else:
        algo = Algo.MORSE
    data = contents[1]
    return (algo, data)


def decrypt(algo: Algo, data: str) -> str:
    if algo == Algo.HEX:
        # hex
        return "".join([chr(int(c, 16)).lower() for c in data.split(" ")])
    elif algo == Algo.CAESAR:
        A = 97
        shift = 3
        # caesar
        return " ".join(
            [
                "".join(
                    [
                        chr((ord(c.lower()) - shift - A) % 26 + A)
                        for c in word
                        if c.isalpha()
                    ]
                )
                for word in data.split(" ")
            ]
        )
    else:
        # morse
        return " ".join(
            [
                "".join(
                    [
                        MORSE_CODES[c]
                        for c in word.strip().split(" ")
                        if c in MORSE_CODES
                    ]
                )
                for word in data.split("/")
            ]
        )


def work(ipath, opath):
    with open(ipath) as ifile, open(opath, "w+") as ofile:
        contents = ifile.readline().strip()
        algo, data = parse(contents)
        result = decrypt(algo, data)
        ofile.write(result)

    pass


def main(args):
    ifiles = os.listdir(args.input_dir)
    for ipath in ifiles:
        if ipath.endswith(".txt"):
            opath = f"{ipath.rstrip('.txt')}_r21857jl.txt"

            ipath = os.path.join(args.input_dir, ipath)
            opath = os.path.join(args.output_dir, opath)
            work(ipath, opath)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()
    main(args)
