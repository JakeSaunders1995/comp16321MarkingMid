import argparse
import os

morse = { ".-":"A", "-...":"B",
"-.-.":"C", "-..":"D", ".":"E",
"..-.":"F", "--.":"G", "....":"H",
"..":"I", ".---":"J", "-.-":"K",
".-..":"L", "--":"M", "-.":"N",
"---":"O", ".--.":"P", "--.-":"Q",
".-.":"R", "...":"S", "-":"T",
"..-":"U", "...-":"V", ".--":"W",
"-..-":"X", "-.--":"Y", "--..":"Z",
".----":"1", "..---":"2", "...--":"3",
"....-":"4", ".....":"5", "-....":"6",
"--...":"7", "---..":"8", "----.":"9",
"-----":"0", "--..--":",", ".-.-.-":".",
"..--..":"?", "-..-.":"/", "-....-":"-",
"-.--.":"(", "-.--.-":")"
}

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args=parser.parse_args()

for file in os.listdir(args.input):
    filepath = os.path.join(args.input,file)


    with open(filepath, "r") as f:
        ciphertext = f.read()

    cipher=""
    encoded=""
    pastmid=False
    for n in ciphertext:
        if n == ":":
            pastmid=True
        elif pastmid == False:
            cipher+=n
        else:
            encoded+=n

    if cipher == "Hex":
        encoded.replace(" ","")
        decoded = bytearray.fromhex(encoded).decode()
    elif cipher == "Caesar Cipher(+3)":
        decoded = ""
        for n in encoded:
            if n != " ":
                ciphertextChar = n
                ASCIIValue = ord(ciphertextChar)
                ASCIIValue-=3
                decoded+=chr(ASCIIValue)
            else:
                decoded += " "
    elif cipher == "Morse Code":
        encoded+=" "
        decoded = ""
        encodedletter = ""
        for n in encoded:
            if n == "/":
                decoded+=" "
                continue
            elif n == " ":
                if encodedletter != "":
                    letter = morse[encodedletter]
                    decoded+=letter
                    encodedletter = ""
            else:
                encodedletter+=n

    decoded=decoded.lower()
    # with open(sys.argv[2], "w") as f:
    #     f.write(decoded)
    file = file[:len(file)-4]

    outputfile = file+"_r25329lc.txt"

    outputpath = os.path.join(args.output,outputfile)

    with open(outputpath, 'w') as f:
        f.write(decoded)