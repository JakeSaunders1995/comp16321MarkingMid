import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('dict_file')
parser.add_argument('input_folder')
parser.add_argument('output_folder')
args = parser.parse_args()
dict_file, input_folder, output_folder = args.dict_file, args.input_folder, args.output_folder
formatting_path = lambda path: os.getcwd()+path[1:] if path[0] == '.' else path
dict_file, input_folder, output_folder = formatting_path(dict_file), formatting_path(input_folder), formatting_path(output_folder)

def spellchecker(data):
    import re
    import bisect

    infos = [0]*6
    length = len(data)

    infos[0] = len(re.findall('[A-Z]', data))
    data = data.lower()

    ellipsis = data.count('...')
    data = re.sub('[(\.\.\.)\.\?\!,:;\-\]\[\]\}\{\)\(\'\"]', '', data)
    infos[1], length = length - len(data) - ellipsis*2, len(data)

    data = re.sub('\d', '', data)
    infos[2], infos[3] = length - len(data), len(data.split())

    infos[4] = sum((1 if dictionary[bisect.bisect(dictionary, word)-1] == word else 0 for word in data.strip().split()))
    infos[5] = infos[3]-infos[4]

    output = f'''x12691yl
Formatting ###################
Number of upper case words changed: {infos[0]}
Number of punctuations removed: {infos[1]}
Number of numbers removed: {infos[2]}
Spellchecking ###################
Number of words: {infos[3]}
Number of correct words: {infos[4]}
Number of incorrect words: {infos[5]}'''
    return output


dictionary = open(dict_file, "r").read().strip().split()
for file in filter(lambda x: x.endswith(".txt"), os.listdir(args.input_folder)):
    output = spellchecker(open(f'{args.input_folder}/{file}', "r").read().strip())
    file = file.replace('.txt', '')
    w = open(f'{args.output_folder}/{file}_x12691yl.txt', "w")
    w.write(output)
    w.close()
