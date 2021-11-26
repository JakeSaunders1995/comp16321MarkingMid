import os
import argparse

def hex2chr(txt):
    txt = txt[txt.find(":") + 1:]
    s = txt.split(" ")
    result = ""
    for i in s:
        tmp = int(i, 16)
        if (tmp >= 65 and tmp <= 90):
            tmp = chr(tmp + 32)
        else:
            tmp = chr(tmp)
        result += tmp
    return result

def caesar(txt):
    txt = txt[txt.find(":") + 1:]
    result = ""
    for i in range(len(txt)):
        tmp = ord(txt[i])
        if (tmp >= 65 and tmp <= 90):
            tmp += 32
        if (tmp >= 97 and tmp <= 99):
            tmp = chr(tmp + 23)
        elif (tmp >= 100 and tmp <= 122):
            tmp = chr(tmp - 3)
        else:
            tmp = chr(tmp)
        result += tmp
    return result

def morse(txt):
    txt = txt[txt.find(":") + 1:]
    s = txt.split(" ")
    result = ""
    dict = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
        "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
        "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
        "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
        ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
        "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
        "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
        "·-···": "&", ".--.-.": "@", ".-.-.": "+",
        ".-.-.-.-.-.-.-.-.-": "...", "": "", "/": " ",
    }
    for i in s:
        result += dict.get(i)
    return result

def detMetod(name):
    f = open(name, "r")
    txt = f.read()
    f.close()
    if (txt[0] == 'H' or txt[0] == 'h'):
        return hex2chr(txt)
    elif (txt[0] == 'C' or txt[0] == 'c'):
        return caesar(txt)
    elif (txt[0] == 'M' or txt[0] == 'm'):
        return morse(txt)

def store(name, content):
    if (os.path.isfile(name)):
        f = open(name, "w")
        f.write(content)
        f.close()
    else:
        f = open(name, "x")
        f.write(content)
        f.close()

parser = argparse.ArgumentParser()
parser.add_argument("inputPath", help="increase input path")
parser.add_argument("outputPath", help="increase output path")
args = parser.parse_args()
currentPath = os.getcwd()
os.chdir(args.inputPath)
pathList = os.listdir()
list1 = []
list2 = []
for text in pathList:
    list1.append(text)
    list2.append(detMetod(text))
os.chdir(currentPath)
os.chdir(args.outputPath)
for i in range(len(list1)):
    if (list1[i][-4:] == ".txt"):
        tmp = list1[i][0:-4] + "_y70582kd.txt"
    else:
        tmp = list1[i] + "_y70582kd"
    store(tmp, list2[i])

