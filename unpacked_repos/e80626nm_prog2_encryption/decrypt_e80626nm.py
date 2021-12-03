import os, argparse

parse = argparse.ArgumentParser()
parse.add_argument('directory', nargs='+')
args = parse.parse_args()
files = os.listdir(args.directory[0])



if not os.path.exists(args.directory[1]):
    os.mkdir(args.directory[1])

for theFile in files:
    message = []
    with open(args.directory[0] + '/' + theFile, 'r') as line:
        line = line.read().rstrip()

    line = line.lower()
    line = list(line)
    c = ''

    for i in range(20):
        if line[i] == ':':
            c = line[i - 1]
            del line[:i + 1]
            break

    if c == 'x':
        letters = []
        line.append(' ')
        for i in range(len(line)):
            if line[i] == ' ':
                letter = ''.join(line[i-2:i])
                letter = bytes.fromhex(letter)
                letter = letter.decode("ASCII")
                letters.append(letter)

        message = ''.join(letters)

    elif c == ')':
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        decoder = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        words = ''.join(line)
        words = words.split(' ')
        words[-1] += ' '

        for word in words:
            startIndex = 0
            letters = []
            for i in range(len(word)):
                if word[i] == ' ':
                    continue
                else:
                    letters.append(decoder[alphabet.index(word[i])])

            message.append(''.join(letters))

        message = ' '.join(message)



    elif c == 'e':
        decoder = {'.-': 'a', '-...': 'b', '-.-.': 'c',
                   '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g',
                   '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k',
                   '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q',
                   '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v',
                   '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
                   '-----' : '0',
                   '.----' : '1',
                   '..---' : '2',
                   '...--' : '3',
                   '....-' : '4',
                   '.....' : '5',
                   '-....' : '6',
                   '--...' : '7',
                   '---..' : '8',
                   '----.': '9',
                   '.-.-.-': '.',
                   '--.--': ','
                   }

        message = []
        words = ''.join(line)
        words = words.split('/ ')
        words[-1] += ' '

        for word in words:
            startIndex = 0
            letters = []
            for i in range(len(word)):
                if word[i] == ' ':
                    letters.append(decoder[word[startIndex:i]])
                    startIndex = i + 1
            message.append(''.join(letters))
        message = ' '.join(message)

    message = message.lower()
    with open(f'{args.directory[1]}/{theFile}_e80626nm.txt', 'w') as file:
        file.write(message)
