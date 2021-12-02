import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('word')
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()
word = args.word
input = args.input
output = args.output


def process(file_in, word):
    with open(file_in) as f:
        content = f.read().lower() + " "
    with open(word) as f:
        words_ls = f.readlines()
    cWord= ""
    res=""
    nums = 0
    punc = 0
    ucount = 0
    words = 0
    cwords = 0
    iwords = 0
    is_upper = False
    for char in content:
        code = ord(char)
        if (code>=65 and code <(65+26)):
            code+=32

        if (code >= 96 and code < (96+26)):
            cWord+=chr(code)
        elif code == 32 or code == 10:
            words+=1
            if(is_upper):
                ucount+=1
            if cWord in words_ls:
                cwords+=1
            else:
                iwords+=1
            res += cWord+char
            cWord = ""
            is_upper = False
        elif (code >= 48 and code < 58):
            nums+=1
        else:
            punc+=1
    return ucount,punc,nums,words,cwords,iwords

def main(input, output):
    ucount,punc,nums,words,cwords,iwords = process(input, word)
    with open(output, 'w') as f:
        f.write(f"""[username]
    Formatting ###################
    Number of upper case words transformed: {ucount}
    Number of punctuation’s removed: {punc}
    Number of numbers removed: {nums}
    Spellchecking ###################
    Number of words in file: {words}
    Number of correct words in file: {iwords}
    Number of incorrect words in file: {cwords}
    """)

file_in = os.listdir(input)
if not os.path.exists(output):
    os.mkdir(output)
for item in file_in:
    name=os.path.join(output, item.split('.')[0]+'_f60163yw.txt')
    item = os.path.join(input, item)
    main(item, name)
