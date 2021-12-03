import sys, os

morse_dict = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5',
     '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
     '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
     '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
     '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
     '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
     '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
     '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
     '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3', '/': ' ' }


def unhex(s):
    return ''.join([chr(int(i, 16)) for i in s.split(' ')])


def unmorse(s):
    return ''.join([morse_dict[i] for i in s.split(' ')])


def uncaesar(s):
    out = ""
    for i in s:
        if i == " " or i in list("1234567890"):
            out += i
        else:
            val = ord(i) - 3
            if val < 97:
                val += 26
            out += chr(val)
    return out

filenames = os.listdir(sys.argv[1])
for input_file in filenames:
    with open(sys.argv[1] + "/" + input_file) as f:
        text = f.read().replace('\n', '')
        if text[0] == "H":
            plaintext = unhex(text[4:])
        elif text[0] == "M":
            plaintext = unmorse(text[11:])
        else:
            plaintext = uncaesar(text[18:].lower())

    output_filename = sys.argv[2] + "/" + input_file[:-4] + "_k01756ws.txt"
    with open(output_filename, 'w') as f:
        f.write(plaintext.lower())

