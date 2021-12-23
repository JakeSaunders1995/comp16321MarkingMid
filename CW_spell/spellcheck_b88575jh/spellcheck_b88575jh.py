import argparse
import os

corrections = {
    "Case" : 0,
    "Punct" : 0,
    "Num" : 0,
}

def formatText(text):
    output = ""
    for x in text:
        output += parseChar(x)

    return output

def parseChar(char):
    if char.isupper():
        type = "Case"
        char = char.lower()
    elif char.isalpha() or char == " ":
        return char
    else:
        if char.isnumeric():
            type = "Num"
        else:
            type = "Punct"
        char = ""

    corrections[type] += 1
    return char

def checkWords(text):
    goodWords = 0
    f = open(args.words, "r")
    allwords = f.read()

    for word in text.split(" "):
        if word in allwords:
            goodWords += 1

    f.close()

    return goodWords

def wordCount(text):
    words = text.split(" ")
    count = 0

    for word in words:
        count += 1

    return count

def getText(f):
    text = f.read()
    return formatText(text)

def main():
    if not os.path.isdir(args.output):
        os.mkdir(args.output)


    for filename in os.listdir(args.input):
        if ".txt" in filename:
            f = open((args.input +"/"+ filename), "r")
            text = getText(f)
            f.close()
            count = wordCount(text)
            goodCount = checkWords(text)
            outputFile = filename[:-4] + "_b88575jh.txt"
            f = open((args.output + "/" +outputFile), "w")
            f.write(
                "b88575jh"+
                "\nFormatting ###################"+
                "\nNumber of upper case words transformed: "+str(corrections["Case"])+
                "\nNumber of punctuations removed: "+str(corrections["Punct"])+
                "\nNumber of numbers removed: "+str(corrections["Num"])+
                "\nSpellchecking ###################"+
                "\nNumber of words in file: "+str(count)+
                "\nNumber of correct words in file: "+str(goodCount)+
                "\nNumber of incorrect words in file: "+str(int(count)-int(goodCount))
                )
            f.close()

parser = argparse.ArgumentParser(description='Checks text for spelling errors')
parser.add_argument('words', type=str,help='Path to file containing list of english words') #?
parser.add_argument('input', type=str, help='Path to folder containing files to be checked')
parser.add_argument('output', type=str, help='Path to folder to output to')
args=parser.parse_args()

main()
