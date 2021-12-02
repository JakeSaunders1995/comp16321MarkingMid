import argparse
import re

username = 'h72507by'

number = re.compile(r'\d')
symbol = re.compile(r'''(?:——)|[\.\?!,:;\-\[\]\{\}'"…@#]''')
word = re.compile(r'''[a-zA-Z']+''')
up_word = re.compile(r'''[A-Z]+''')

class Trie:
    
    def __init__(self):
        self.root = {}
        self.end_flag = -1

    def insert(self, word):
        curNode = self.root
        for c in word:
            if curNode.get(c, None) is None:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end_flag] = True

    def search(self, word):
        curNode = self.root
        for c in word:
            if curNode.get(c, None) is None:
                return False
            curNode = curNode[c]
        return curNode.get(self.end_flag, False)


def get_word_tree(words):
    tree = Trie()
    with open(words, 'r') as f:
        for w in f.readlines():
            tree.insert(w.strip().lower())
    return tree

def check(words, input):
    res = [0] * 6
    tree = get_word_tree(words)
    with open(input, 'r') as f:
        for x in f.readlines():
            wd = re.findall(word, x)
            res[1] += len(re.findall(symbol, x))
            res[2] += len(re.findall(number, x))
            res[3] += len(wd)
            for w in wd:
                if re.search(up_word, w) is not None:
                    res[0] += 1
                if tree.search(w.lower()):
                    res[4] += 1
                else:
                    res[5] += 1
    return res

def main(words, input, output):
    res = check(words, input)
    with open(output, 'w') as f:
        f.write(username + '\n')
        f.write('Formatting ###################\n')
        f.write('Number of upper case words changed: {}\n'.format(res[0]))
        f.write('Number of punctuations removed: {}\n'.format(res[1]))
        f.write('Number of numbers removed: {}\n'.format(res[2]))
        f.write('Spellchecking ###################\n')
        f.write('Number of words: {}\n'.format(res[3]))
        f.write('Number of correct words: {}\n'.format(res[4]))
        f.write('Number of incorrect words: {}\n'.format(res[5]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('words', type=str)
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    args = parser.parse_args()
    main(args.words, args.input, args.output)
