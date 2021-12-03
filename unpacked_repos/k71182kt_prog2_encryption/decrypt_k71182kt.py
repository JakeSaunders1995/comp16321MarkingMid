import argparse, os

def directory_path(string):
    if os.path.isdir(string):
        return string
    else:
        return str(string)

# input text file
python_file_location = os.getcwd()
parser = argparse.ArgumentParser()
parser.add_argument('inputpath', type=directory_path)
parser.add_argument('outputpath', type=directory_path)
args = parser.parse_args()
outputStringList = []
name_of_file_list = []
os.chdir(args.inputpath)

for file in os.listdir():
    if file.endswith(".txt"):
        with open(file, 'r') as f:
            name_of_file = str(file)[0:len(str(file))-4] + "_k71182kt.txt"
            name_of_file_list.append(name_of_file)
            inputString = str(f.read())
            method = ""
            count = 0
            for i in inputString:
                if i == ":":
                    break
                else:
                    method = method + i
                    count = count + 1
            cipherText = inputString[count+1:len(inputString)]
            cipherText = cipherText.lower().rstrip()
            plainText = ""
            if method == "Hex":
                # hex decryption method
                bytes_object = bytes.fromhex(cipherText)
                plainText = bytes_object.decode("ASCII")
                plainText = plainText.lower()
                outputStringList.append(plainText)
            elif method == "Caesar Cipher(+3)":
                # caesar cipher decryption method
                plain_alphabet = "abcdefghijklmnopqrstuvwxyz0123456789.?!,;:-(){}[]' "
                caesar_alphabet = "defghijklmnopqrstuvwxyzabc0123456789.?!,;:-(){}[]' "
                for letter in cipherText:
                    position = 0
                    while position < len(caesar_alphabet):
                        if letter == caesar_alphabet[position]:
                            break
                        else:
                            position = position + 1
                    plainText = plainText + plain_alphabet[position]
                plainText = plainText.lower()
                outputStringList.append(plainText)
            elif method == "Morse Code":
                # morse code decryption method
                morse_code_dictionary = {
                                    '.-':'a', '-...':'b',
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
                                    '..--..':'?', '-..-.':'/', '-....-':'-',
                                    '-.--.':'(', '-.--.-':')', '/':' ', '-.-.--':'!',
                                    '---...':':'
                }

                part = ""
                for sign in cipherText:
                    if sign != " ":
                        part = part + sign
                    else:
                        plainText = plainText + morse_code_dictionary[part]
                        part = ""
                plainText = plainText + morse_code_dictionary[part]
                plainText = plainText.lower()
                outputStringList.append(plainText)

os.chdir(python_file_location)
directory = args.outputpath
if os.path.exists(directory):
    os.chdir(directory)
else:
    os.mkdir(directory)
    os.chdir(directory)

output_count = 0
for i in name_of_file_list:
    output_text_file = open(i, 'w')
    output_text_file.write(outputStringList[output_count])
    output_text_file.close()
    output_count = output_count + 1
