import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument('input')
parser.add_argument('output')
args = parser.parse_args()

inputfolder = args.input
outputfolder = args.output
inputfiles = os.listdir(inputfolder)

for i in inputfiles:

    filepath = os.path.join(inputfolder, i)
    currentfile = open(filepath)
    inputtext = currentfile.read()
    currentfile.close()

    if inputtext[0] == "H":
        cipher = "hex"
    elif inputtext[0] == "M":
        cipher = "morsecode"
    elif inputtext[0] == "C":
        cipher = "caesar(+3)"

    decryptedtext = ""

    if cipher == "morsecode":
        morsealphabet = {
            '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
        }
        inputtext = inputtext[11:]
        inputtext += " "
        a = 0
        currentchar = ""
        while a < len(inputtext):
            if inputtext[a] != " " and inputtext[a] != "/":
                currentchar += inputtext[a]
            elif inputtext[a] == " ":
                letter = ""
                if len(currentchar) != 0:
                    letter = morsealphabet.get(currentchar)
                decryptedtext += letter
                currentchar = ""
            elif inputtext[a] == "/":
                decryptedtext += " "
            a += 1
    
    elif cipher == "caesar(+3)":
        inputtext = inputtext[18:]
        a = 0
        while a < len(inputtext):
            if inputtext[a] == " ":
                decryptedtext += " "
            elif inputtext[a] == "a":
                decryptedtext += "x"
            elif inputtext[a] == "b":
                decryptedtext += "y"
            elif inputtext[a] == "c":
                decryptedtext += "z"
            else:
                decryptedtext += chr(ord(inputtext[a]) - 3)
            a += 1

    elif cipher == "hex":

        inputtext = inputtext[4:]
        a = 0
        while a < len(inputtext) - 1:
            if inputtext[a] != " " and inputtext[a + 1] != " ":
                hexdigit = str(inputtext[a] + inputtext[a + 1])
                dendigit = int(hexdigit, 16)
                decryptedtext += chr(dendigit)
            a += 1

    decryptedtext = decryptedtext.lower()
    print(decryptedtext)

    outputname = i[:-4] + "_w73862jb.txt"
    outputpath = os.path.join(outputfolder, outputname)

    outputfile = open(outputpath, "w")
    outputfile.write(decryptedtext)
    outputfile.close()