import sys, math, os

def morseCode(cypher_text):
    morse = {".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l",
    "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
    "--..":"z"}
    decrypted = ""
    temp = ""
    for i in range(len(cypher_text)):
        if cypher_text[i] != " " and cypher_text[i] != "/":
            temp += cypher_text[i]
        elif cypher_text[i] == " " and cypher_text[i-1] != "/":
            decrypted += morse[temp]
            temp = ""
        elif cypher_text[i] == "/":
            decrypted += " "
    return decrypted

def ceasarCode(cypher_text):
    decrypted = ""
    alphabet = "xyzabcdefghijklmnopqrstuvwxyz"
    for i in cypher_text:
        if i != " ":
            if i in alphabet:
                pos = 3
                while alphabet[pos] != i:
                    pos += 1
                pos -= 3
                decrypted += alphabet[pos]
        elif i == " ":
            decrypted += i
    decrypted = decrypted.lower()
    return decrypted

def hexCode(cypher_text):
    decrypted = ""
    temp = ""
    for i in cypher_text:
        if i!=" ":
            temp += i
        else:
            pos = 0
            length = len(temp)
            for j in range(length):
                if temp[j] == "a":
                    pos += 10*pow(16, length - j - 1)
                elif temp[j] == "b":
                    pos += 11*pow(16, length - j - 1)
                elif temp[j] == "c":
                    pos += 12*pow(16, length - j - 1)
                elif temp[j] == "d":
                    pos += 13*pow(16, length - j - 1)
                elif temp[j] == "e":
                    pos += 14*pow(16, length - j - 1)
                elif temp[j] == "f":
                    pos += 15*pow(16, length - j - 1)
                else:
                    pos += int(temp[j])*pow(16, length - j - 1)
            temp = ""
            decrypted += chr(pos)
    pos = 0
    length = len(temp)
    for j in range(length):
        if temp[j] == "a":
            pos += 10*pow(16, length - j - 1)
        elif temp[j] == "b":
            pos += 11*pow(16, length - j - 1)
        elif temp[j] == "c":
            pos += 12*pow(16, length - j - 1)
        elif temp[j] == "d":
            pos += 13*pow(16, length - j - 1)
        elif temp[j] == "e":
            pos += 14*pow(16, length - j - 1)
        elif temp[j] == "f":
            pos += 15*pow(16, length - j - 1)
        else:
            pos += int(temp[j])*pow(16, length - j - 1)
    decrypted += chr(pos)
    decrypted = decrypted.lower()
    return decrypted

files = sys.argv
input_file_path = files[1]
output_file_path = files[2]
code = ""
cypherText = ""
files_names = os.listdir(input_file_path)
count = 0
with os.scandir(input_file_path) as files:
    for entry in files:
        with open(entry, "r") as file:
            code = ""
            cypherText = ""
            line = file.readline().rstrip()
            i = 0
            while line[i] != ":":
                    code += line[i]
                    i += 1
            i += 1
            for j in range(i, len(line)):
                cypherText += line[j]
            i = 0
            file_name = ""
            while files_names[count][i] != ".":
                file_name += files_names[count][i]
                i+=1
            file_name += "_d72499pd.txt"
            save_file = os.path.join(output_file_path, file_name)
            with open(save_file, "w") as output_file:
                if code == "Caesar Cipher(+3)":
                    output_file.write(ceasarCode(cypherText))
                elif code == "Morse Code":
                    output_file.write(morseCode(cypherText))
                elif code == "Hex":
                    output_file.write(hexCode(cypherText))
            count += 1
