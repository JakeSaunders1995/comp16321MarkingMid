import argparse
import os 

parser = argparse.ArgumentParser(description='input and output')
parser.add_argument('word_file', help='word')
parser.add_argument('input_file_path', help='input')
parser.add_argument('output_file_path', help='output')
args = parser.parse_args()
word_file = args.word_file

def process(in_file, word_file):
    with open(in_file) as f:
        content = f.read().lower() + " "
    with open(word_file) as f:
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


def main(input_file, output_file):
    ucount,punc,nums,words,cwords,iwords = process(input_file, word_file)
    with open(output_file, 'w') as f:
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

input_file_path = args.input_file_path
output_file_path = args.output_file_path

in_files = os.listdir(input_file_path)
if not os.path.exists(output_file_path):
    os.mkdir(output_file_path)
for item in in_files:
    out_name = os.path.join(output_file_path, item.split('.')[0]+'_v35117sy.txt')
    item = os.path.join(input_file_path, item)
    main(item, out_name)
