import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("input", help="input folder path")
parser.add_argument("output", help="output folder path")
args = parser.parse_args()

inputPath = args.input
outputPath = args.output

inputFiles = sorted(os.listdir(inputPath))
outputFiles = sorted(os.listdir(outputPath))

file_num = 0
for x in inputFiles:
    file_num += 1
    input_file = inputPath + '/' + x
    with open(input_file, 'rb') as inputFile:
        content = inputFile.read()
    inputFile.close()


    moreseCode = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E',
                '..-.':'F', '--.':'G', '....':'H',
                '..':'I', '.---':'J', '-.-':'K',
                '.-..':'L', '--':'M', '-.':'N',
                '---':'O', '.--.':'P', '--.-':'Q',
                '.-.':'R', '...':'S', '-':'T',
                '..-':'U', '...-':'V', '.--':'W',
                '-..-':'X', '-.--':'Y', '--..':'Z',
                '.----':'1', '..---':'2', '...--':'3',
                '....-':'4', '.....':'5', '-....':'6',
                '--...':'7', '---..':'8', '----.':'9',
                '-----':'0', '.-...':'&', ".----.":"'",
                '.--.-.':'@', '-.--.-':')', '-.--.':'(',
                '---...':':', '--..--':',', '-...-':'=', '-.-.--':'!', '.-.-.-':'.',
                '-....-':'-', '.-.-.':'+', '.-..-.':'"', '..--..':'?', '-..-.':'/',
                '-.-.-.':';', '..--.-':'_', '...-..-':'$', '.-.-.-.-.-.-.-.-.-':'...'}

    position = 0
    if content[0] == 0x48 or content[0] == 0x68:
        while True:
            if content[position] != 0x3A:
                position += 1
            else:
                position += 1
                break
        text = ''
        while position < len(content):
            text += chr(content[position])
            position += 1
        p = 0
        Ptext = ''
        while p < len(text)-1:
            if text[p] == chr(0x20) or text[p] == '\n' or text[p] == '\t':
                p += 1
            else:
                Ptext += chr(int(text[p]+text[p+1], 16))
                p += 2
        final_text = Ptext.lower()
        if file_num > len(outputFiles):
            output_file = outputPath + '/' + x.replace('.txt', '_n20773yz.txt')
        else:
            output_file = outputPath + '/' + outputFiles[file_num - 1]
        outputFile = open(output_file, "w")
        outputFile.write(final_text)
        outputFile.close()
        os.rename(output_file, outputPath + '/' + x.replace('.txt', '_n20773yz.txt'))

    if content[0] == 0x43 or content[0] == 0x63:
        alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
        while True:
            if content[position] != 0x3A:
                position += 1
            else:
                position += 1
                break
        Ptext = ''
        while position < len(content):
            if content[position] == 0x20:
                Ptext += ' '
                position += 1
            elif chr(content[position]) == "\n" or chr(content[position]) == "\t":
                position += 1
            elif chr(content[position]) in alphabet:
                p = 3
                while chr(content[position]) != alphabet[p]:
                    p += 1
                p = p - 3
                Ptext += alphabet[p]
                position += 1
            else:
                ASCIIValue = content[position]
                ASCIIValue -= 3
                Ptext += chr(ASCIIValue)
                position += 1
        final_text = Ptext.lower()
        if file_num > len(outputFiles):
            output_file = outputPath + '/' + x.replace('.txt', '_n20773yz.txt')
        else:
            output_file = outputPath + '/' + outputFiles[file_num - 1]
        outputFile = open(output_file, "w")
        outputFile.write(final_text)
        outputFile.close()
        os.rename(output_file, outputPath + '/' + x.replace('.txt', '_n20773yz.txt'))

    if content[0] == 0x4D or content[0] == 0x6D:
        while True:
            if content[position] != 0x3A:
                position += 1
            else:
                position += 1
                break
        text = ''
        while position < len(content):
            text += chr(content[position])
            position += 1
        p = 0
        Ptext = ''
        while p < len(text):
            single_letter_code = ''
            while p < len(text) and (text[p] == '-' or text[p] == '.'):
                single_letter_code += text[p]
                p += 1
            if text[p-1] == '.' or text[p-1] == '-':
                Ptext += str(moreseCode.get(single_letter_code))
                if p < len(text) and text[p] == chr(0x2F):
                    Ptext += chr(0x20)
                p += 1
            else: 
                p += 1
            if p < len(text) and text[p] == chr(0x2F):
                Ptext += chr(0x20)
                p += 1
        final_text = Ptext.lower()   
        if file_num > len(outputFiles):
            output_file = outputPath + '/' + x.replace('.txt', '_n20773yz.txt')
        else:
            output_file = outputPath + '/' + outputFiles[file_num - 1]
        outputFile = open(output_file, "w")
        outputFile.write(final_text)
        outputFile.close()
        os.rename(output_file, outputPath + '/' + x.replace('.txt', '_n20773yz.txt'))
