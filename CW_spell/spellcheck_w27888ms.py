import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("english", help="English words file path")
parser.add_argument("input", help="Input folder path")
parser.add_argument("output", help="Output folder path")
args = parser.parse_args()
files = []
for file in os.listdir(args.input):
    if file.endswith(".txt"):
        files.append(file)
for x in files:
    upcase = punct = delnum = num = cnum = inum = 0
    with open(os.path.join(args.input, x)) as file1:
        for line in file1:
            text = ""
            characters = list(line)
            if characters[-1] == "\n":
                del characters[-1]
            size = len(characters)
            characters = [a for a in characters if a.isnumeric() is False]
            delnum += size - len(characters)
            size = len(characters)
            characters = [a for a in characters if a not in """.?!,:;-–'[]{}"()…"""]
            punct += size - len(characters)
            for i in range(len(characters)):
                if characters[i].isupper():
                    characters[i] = characters[i].lower()
                    upcase += 1
            text = text.join(characters).split()
            num += len(text)
            with open(args.english) as file2:
                englishdictionary = [row.strip() for row in file2]
            for z in text:
                if z in englishdictionary:
                    cnum += 1
                else:
                    inum += 1
    with open(os.path.join(args.output, f"{x[:-4]}_w27888ms.txt"), "w") as file3:
        file3.write(f"w27888ms\nFormatting ###################\nNumber of upper case letters changed: {upcase}\nNumber of punctuations removed: {punct}\nNumber of numbers removed: {delnum}\nSpellchecking ###################\nNumber of words: {num}\nNumber of correct words: {cnum}\nNumber of incorrect words: {inum}")
