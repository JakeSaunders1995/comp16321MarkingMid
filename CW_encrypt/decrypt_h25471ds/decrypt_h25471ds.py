import os, argparse, re

morsedict = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '--..--': ',', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')', '.-..-.': '"', '-.-.--': '!', '.-...': '&', '---...': ':', '-.-.-.': ';', '..--.-': '_', '-...-': '=', '.-.-.': '+', '...-..-': '$', '.--.-.': '@', '.----.': "'" }

alphabet = 'abcdefghijklmnopqrstuvwxyz'

input_folder_path = ""
output_folder_path = ""


def cmdline(): # To get arguments from command line
    global input_folder_path, output_folder_path
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=str)
    parser.add_argument('output_path', type=str)
    args = parser.parse_args()

    input_folder_path = args.input_path
    output_folder_path = args.output_path



def fileextraction(arg):
    files = os.listdir(arg)
    for file in files:
        if file.endswith(".txt"): continue
        else: files.remove(file)
    return files

def inputfile(arg): # read the input file and store it in a variable
    with open(os.path.join(input_folder_path,arg),"r+") as file:
        x = file.readline()
        return x


def text_split(arg): 
    data_list = re.split("[:]", arg)
    return data_list

# code = text_split()
# print(code)

def hexdecrypter(arg):
    return bytearray.fromhex(arg).decode()

def morsedecrypter(arg):
    morselist = re.split("[/]",arg)
    for morsecode in morselist:
        idx = morselist.index(morsecode)
        morselist[idx] = "".join(str(morsedict.get(i)) for i in morsecode.split())
    outputsentence = " ".join(morselist)
    return outputsentence

def caesardecrypter(arg):
    words = re.split("[ ]", arg)
    for i in range(len(words)):
        words[i] = words[i].lower()
    for word in words:
        temp_string = ""
        for letter in word:
            if letter.isalpha():
                idx = alphabet.index(letter)
                temp_string += alphabet[idx-3]
            else: temp_string += letter
        word_idx = words.index(word)
        words[word_idx] = temp_string
    sentence_output = " ".join(words)
    return sentence_output


def decrypt(arg):
    if arg[0] == "Hex":
        output = hexdecrypter(arg[1])
        return output
    elif arg[0] == "Morse Code":
        output = morsedecrypter(arg[1])
        return output
    elif arg[0] == "Caesar Cipher(+3)":
        output = caesardecrypter(arg[1])
        return output
    else: pass

# output = decrypt().lower()

def outputfile(arg,arg1):
    if os.path.exists(output_folder_path): 
        pass
    else: os.makedirs(output_folder_path)
    with open(os.path.join(output_folder_path,arg1),"w+") as file:
        file.write(arg)

# outputfile()

def main():
    cmdline()
    input_files = fileextraction(input_folder_path)
    for testfile in input_files:
        cipher = inputfile(testfile)
        data = text_split(cipher)
        output = decrypt(data).lower()
        outputfilename = re.split("[.]",testfile)[0] + "_h25471ds.txt"
        outputfile(output, outputfilename)


main()
