import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('inputDir')
parser.add_argument('outputDir')

args = parser.parse_args()

inputPath = args.inputDir
dirs = os.listdir(inputPath)
outputPath = args.outputDir
# print(dirs)
curDir = []
for k in range(len(dirs)):
    current = dirs[k]
    if current.endswith('.txt'):
        current = current[:-4]
        current = current + "_h64203za.txt"
        curDir.append(current)

for j in range(len(dirs)):
    readName = dirs[j]
    writeName = curDir[j]

    readFile = os.path.join(inputPath, readName)
    writeFile = os.path.join(outputPath, writeName)

    f = open(readFile,"r")
    line = f.readline()
    for i in range(len(line)):
        if line[i] == ":":
            cipher = line[0:i]
            code = line[i+1:]
            break
    f.close()


    if cipher == "Hex":
        decipher = bytearray.fromhex(code).decode()
        decipher = decipher.lower()
        # print(decipher)
    elif cipher == "Caesar Cipher(+3)":
        code = code.lower()
        decipher = ""
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        for x in range(len(code)):
            alphabetPos = 3
            codeChar = code[x]
            while codeChar != alphabet[alphabetPos]:
                if codeChar not in alphabet:
                    break
                alphabetPos += 1
            if codeChar not in alphabet:
                decipher += codeChar
                continue
            alphabetPos -= 3
            decipher += alphabet[alphabetPos]
        # print(decipher)
    elif cipher == "Morse Code":
        decipher = ""
        morse = { '.-':'a', '-...':'b',
            '-.-.':'c', '-..':'d', '.':'e',
            '..-.':'f', '--.':'g', '....':'h',
            '..':'i', '.---':'j', '-.-':'k',
            '.-..':'l', '--':'m', '-.':'n',
            '---':'o', '.--.':'p', '--.-':'q',
            '.-.':'r', '...':'s', '-':'t',
            '..-':'u', '...-':'v', '.--':'w',
            '-..-':'x', '-.--':'y', '--..':'z',
            '.----':'1', '..---':'2', '...--':'3',
            '....-':'4', '.....':'5', '-....':'6',
            '--...':'7', '---..':'8', '----.':'9',
            '-----':'0', '--..--':',', '.-.-.-':'.',
            '..--..':'?', '---...':':',
            '-....-':'-', '.----.':"'", '.-..-.':'"',
            '-.--.':'(', '-.--.-':')', '-.-.--':'!'

        }
        code = code.split(" ")
        for j in range(len(code)):
            if code[j] == "/":
                code[j] = " "
                decipher += code[j]
                continue
            letter = morse[code[j]]
            decipher += letter
        # print(code)
        # print(decipher)

    s = open(writeFile,"w")
    s.write(decipher)
    s.close()
