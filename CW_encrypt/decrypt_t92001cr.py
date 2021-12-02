import argparse, os
morseDict = {'a': '.-',     'b': '-...',   'c': '-.-.', 
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
        's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.', 

        ".": ".-.-.-", ",": "--..--", "?": "..--..",
        "!": "-.-.--", ":": "---...", "`": ".----.",
        "=": "-...-",  "(": "-.--.",  ")": "-.--.-", 
        "&": ".-...",  ";": "-.-.-.", "+": ".-.-.",  
        "-": "-....-", "_": "..--.-", "$": "...-..-",
        "@": ".--.-.", "'": ".----.", '"': ".-..-."
        }

parser = argparse.ArgumentParser()
parser.add_argument("a1", help="input file path")
parser.add_argument("a2", help="output file path")
args = parser.parse_args()
files = []
for file in os.listdir(args.a1):
        if file.endswith(".txt"):
                files.append(file)

for z in range (len(files)):
        f = open(files[z], "r")
        line = f.readline()
        f.close()
        lowercase = line.split(":")[0].lower()
        cipherTxt = line.split(":")[1]
        plainTxt = ""

        if ("hex") in lowercase:
        	hexCodes = cipherTxt.split(" ")
        	for x in range (0,len(hexCodes)):
        		plainTxt = plainTxt + str((bytearray.fromhex(hexCodes[x]).decode()).lower())

        elif ("caesar") in lowercase:
        	words = cipherTxt.split(" ")
        	for x in range(0,len(words)):
        		for y in range(0,len(words[x])):
                                if ord(words[x][y].lower()) >= 97 and ord(words[x][y].lower()) <= 122:
        			     code = ord(words[x][y].lower()) - 3
        			if code < 97 and code + 3 > 96 and code + 3 < 123:
        				code = code + 26
        			asc = chr(code)
        			plainTxt = plainTxt + str(asc)
        		plainTxt = plainTxt + " "

        elif ("morse") in lowercase:
        	morseCode = cipherTxt.split(" ")
        	for x in range(0,len(morseCode)):
        		if morseCode[x] == "/":
        			plainTxt += " "
        		else:
        			plainTxt += list(morseDict.keys())[list(morseDict.values()).index(morseCode[x])]

        noExt = files[z][:-4]

        f = open(str(args.a2) + "/" + noExt + "_t92001cr.txt" , "w")
        f.write(plainTxt)
        f.close()