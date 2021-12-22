import argparse
import os

def process(text):

    # inputFile = open(args.input, "r")
    # outputFile = open(args.output, "w")
    # text = inputFile.read()

    capitalCount = 0
    numberCount = 0
    punctuation = 0
    result = ""
    tempText = text
    for x in range(len(text)):
        ASCIIvalue = ord(text[x])
        if ASCIIvalue>=65 and ASCIIvalue<=90:
            capitalCount+=1
            result+=chr(ASCIIvalue+32)
        elif ASCIIvalue>=48 and ASCIIvalue<=57:
            numberCount+=1
        elif ASCIIvalue==32:
            result+=chr(ASCIIvalue)
        elif ASCIIvalue>=97 and ASCIIvalue<=122:
            result+=chr(ASCIIvalue)
        # elif ord(text[x]) == ord(text[x+1]) == ord(text[x+2]):
        #     punctuation-=1
        elif "..." in tempText:
            punctuation-=1
            tempText = tempText[tempText.index('...')+1:]
        elif text[x]=="\n":
            continue
        else:
            print(text[x])
            punctuation+=1

    correctCount = 0
    wordCount = 0
    result+=" "
    while True:
        if len(result)==0:
            break
        word = result[0:result.index(' ')]
        word=word.rstrip(" ")
        # print(word)
        if len(word)==0:
            result=result[1:]
            continue
        wordCount+=1
        
        for x in engDict:
            if word == x:
                correctCount+=1
                # print(word)
        result = result[result.index(' ')+1:]        
    incorrectCount = wordCount - correctCount

    result =""
    result+=universityName[1:] + "\n"
    result+="Formatting ###################\n"
    result+="Number of upper case letters changed: " + str(capitalCount) + "\n"
    result+="Number of punctuations removed: " +str(punctuation) + "\n"
    result+="Number of numbers removed: " + str(numberCount) + "\n"
    result+="Spellchecking ###################\n"
    result+="Number of words: " + str(wordCount) + "\n"
    result+="Number of correct words: " + str(correctCount) + "\n"
    result+="Number of incorrect words: " + str(incorrectCount) +"\n"
    return result


parser = argparse.ArgumentParser()
parser.add_argument('dict', type=str)
parser.add_argument('input', type=str)
parser.add_argument('output', type=str)
args = parser.parse_args()

dictFileName = ""
if "\\" in args.dict:
    dictFileName = args.dict[args.dict.rindex('\\')+1:]
elif "/" in args.dict:
    dictFileName = args.dict[args.dict.index('/')+1:]
engDict = [line.rstrip("\n") for line in open(args.dict, "r")]
inputFileFolder = os.listdir(args.input)
universityName = "_a38752yw"
for files in inputFileFolder:
    if files[-4:] ==".txt" and files!=dictFileName:
        outputFileName = files[:-4] + universityName + ".txt"
        inputFile = open(args.input+"/"+files,"r")
        outputFile = open(args.output+"/"+outputFileName,"w")
        inputFileString = inputFile.read()
        result = process(inputFileString)
        outputFile.write(result)
