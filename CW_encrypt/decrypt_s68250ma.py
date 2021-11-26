import argparse,os
parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
args = parser.parse_args()
def hexToPlain(hex):
    start = hex.index(":") + 1
    hex = hex[start:]
    hex = hex.strip()
    return bytearray.fromhex(hex).decode().lower()

def caesarToPlain(caesar):
    start = caesar.index(":") + 1
    caesar = caesar[start:]
    plain = ""
    for i in range(0, len(caesar)):
        asccii = ord(caesar[i])
        asccii -= 3
        if(caesar[i] != " "):
            if(caesar[i] == 'a' or caesar[i] == 'A'):
                plain += 'x'
            elif(caesar[i] == 'b' or caesar[i] == 'B'):
                plain += 'y'
            elif(caesar[i] == 'c' or caesar[i] == 'C'):
                plain += 'z'
            elif(asccii >= 20):
                plain += str(chr(asccii))
        else:
            plain += " "
    return plain.lower()

def morseToPlain(morse):
    morse_dict = { 
                    ".-" : "a", "-...":"b",
                    "-.-.":"c", "-..":"d", ".":"e",
                    "..-.":"f", "--.":"g", "....":"h",
                    "..":"i", ".---":"j", "-.-":"k",
                    ".-..":"l", "--":"m", "-.":"n",
                    "---":"o", ".--.":"p", "--.-":"q",
                    ".-.":"r", "...":"s", "-":"t",
                    "..-":"u", "...-":"v", ".--":"w",
                    "-..-":"x", "-.--":"y", "--..":"z",
                    ".----":"1", "..---":"2", "...--":"3",
                    "....-":"4", ".....":"5", "-....":"6",
                    "--...":"7", "---..":"8", "----.":"9",
                    "-----":"0", "--..--":",", ".-.-.-":".",
                    "..--..":"?", "-..-.":"/", "-....-":"-",
                    "-.--.":"(", "-.--.-":")", "-.-.--":"!",
                    "..--.-":"_", ".-..-.":'"', "---...":":",
                    ".----.":"'", "-.-.-.":";", "/": " "}
    colon = morse.index(":") + 1
    morse = morse[colon:].split()
    plain = ""
    for letter in morse:
        plain += morse_dict[letter]   
    return plain.lower()

if(os.path.isdir(args.input_dir)):
    for files in os.listdir(args.input_dir):
        inputFile = os.path.join(args.input_dir, files)
        outputFile = os.path.join(args.output_dir,str(files.replace(".txt","_s68250ma.txt")))
        with open(inputFile, 'r') as file:
            with open(outputFile, 'w') as file2:
                content = file.read()
                if(content.find("Hex") != -1 or content.find("hex") != -1 ):
                    file2.write(hexToPlain(content))
                elif(content.find("Caesar") != -1 or content.find("caesar") != -1):
                    file2.write(caesarToPlain(content))
                elif(content.find("Morse") != -1 or content.find("morse") != -1):
                    file2.write(morseToPlain(content))