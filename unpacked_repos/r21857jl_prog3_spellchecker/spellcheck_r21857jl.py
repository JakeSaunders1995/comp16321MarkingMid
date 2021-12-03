import argparse
import os

PUNC = {
    ".",
    "?",
    "!",
    ",",
    ":",
    ";",
    "—",
    "-",
    "[",
    "]",
    "(",
    ")",
    "{",
    "}",
    "'",
    '"',
    "…",
}


class Counter:
    n = 0

    def __init__(self) -> None:
        pass

    def tick(self):
        self.n += 1

    def get(self):
        return self.n


class Remover:
    def __init__(self, value, pred, misscb) -> None:
        self.it = iter(value)
        self.pred = pred
        self.misscb = misscb
        pass

    def __iter__(self):
        while True:
            try:
                c = next(self.it)
            except:
                return
            if self.pred(c):
                yield c
            else:
                self.misscb()


class Changer:
    def __init__(self, value, pred, change, hitcb) -> None:
        self.it = iter(value)
        self.pred = pred
        self.change = change
        self.hitcb = hitcb
        pass

    def __iter__(self):
        while True:
            try:
                c = next(self.it)
            except:
                return
            if self.pred(c):
                self.hitcb()
                yield self.change(c)
            else:
                yield c


def work(ipath, opath, wpath):
    with open(ipath) as ifile:
        contents = ifile.readline()
        # FORMATTING
        # remove numbers
        num_removed = Counter()
        for num in map(str, range(0, 10)):
            contents = "".join(Remover(contents, lambda c: c != num, num_removed.tick))
        # remove punctuation
        punc_removed = Counter()
        for p in PUNC:
            contents = "".join(Remover(contents, lambda c: c != p, punc_removed.tick))
        # make everything lowercase
        upper_changed = Counter()
        contents = "".join(
            Changer(
                contents, lambda c: c.isupper(), lambda c: c.lower(), upper_changed.tick
            )
        )
        # SPELLING
        words = contents.split(" ")
        words = [word.strip() for word in words if word.strip() != '']
        word_count = len(words)
        correct_words = 0
        for checkword in words:
            correct = False
            with open(wpath) as wfile:
                for word in wfile:
                    word = word.strip()
                    if word == checkword:
                        correct = True
                        break
                if correct:
                    correct_words += 1

    # write results
    with open(opath, "w+") as ofile:
        ofile.write("[r21857jl]\n")
        # formatting
        ofile.write("Formatting ###################\n")
        ofile.write(f"Number of upper case letters changed: {upper_changed.get()}\n")
        ofile.write(f"Number of punctuations removed: {punc_removed.get()}\n")
        ofile.write(f"Number of numbers removed: {num_removed.get()}\n")
        # spelling
        ofile.write("Spellchecking ###################\n")
        ofile.write(f"Number of words: {word_count}\n")
        ofile.write(f"Number of correct words: {correct_words}\n")
        ofile.write(f"Number of incorrect words: {word_count-correct_words}\n")
        pass

    pass


def main(args):
    ifiles = os.listdir(args.input_dir)
    for ipath in ifiles:
        if ipath.endswith(".txt"):
            opath = f"{ipath.rstrip('.txt')}_r21857jl.txt"

            ipath = os.path.join(args.input_dir, ipath)
            opath = os.path.join(args.output_dir, opath)

            work(ipath, opath, args.words_file)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("words_file", type=str)
    parser.add_argument("input_dir", type=str)
    parser.add_argument("output_dir", type=str)
    args = parser.parse_args()
    main(args)
