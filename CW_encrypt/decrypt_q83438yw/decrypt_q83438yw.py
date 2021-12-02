import sys
import os
input_folder = sys.argv[1]
output_folder = sys.argv[2]
input = os.path.realpath(input_folder)
sum = os.listdir(input)
for i in sum:
    Code = open(input + "/" + i, 'r')
    output = os.path.realpath(output_folder)
    name = os.path.basename(i)
    name1 = name.replace(".txt", "_q83438yw.txt")
    outcome = open(os.path.join(output, name1), 'w')
    if Code.read(4) == 'Hex:':
        message = Code.read()
        dictionary = {'20': ' ', '21': '!', '22': '"', '23': '#', '24': '$', '25': '%', '26': '&',
                      '27': "'", '28': '(', '29': ')', '2a': '*', '2b': '+', '2c': ',', '2d': '-',
                      '2e': '.', '2f': '/', '30': '0', '31': '1', '32': '2', '33': '3', '34': '4',
                      '35': '5', '36': '6', '37': '7', '38': '8', '39': '9', '3a': ':', '3b': ';',
                      '3c': '<', '3d': '=', '3e': '>', '3f': '?', '40': '@', '41': 'a', '42': 'b', '43': 'c',
                      '44': 'd', '45': 'e', '46': 'f', '47': 'g', '48': 'h', '49': 'i', '4a': 'j',
                      '4b': 'k', '4c': 'l', '4d': 'm', '4e': 'n', '4f': 'o', '50': 'p', '51': 'q', '52': 'r',
                      '53': 's', '54': 't', '55': 'u', '56': 'v', '57': 'w', '58': 'x', '59': 'y',
                      '5a': 'z', '5b': '[', '5d': ']', '5e': '^', '5f': '_', '60': '`',
                      '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g',
                      '68': 'h', '69': 'i', '6a': 'j', '6b': 'k', '6c': 'l', '6d': 'm', '6e': 'n',
                      '6f': 'o', '70': 'p', '71': 'q', '72': 'r', '73': 's', '74': 't', '75': 'u',
                      '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7a': 'z', '7b': '{', '7c': '|',
                      '7d': '}', '7e': '~',
                      };
        message_split = message.split()
        for item in message_split:
            value1 = str(dictionary[item])
            outcome.write(value1)

    elif Code.read(7) == 'e Code:':
        message = Code.read()
        dictionary = {
            ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
            "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n",
            "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t",
            "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

            "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
            ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

            ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
            "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
            "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
            ".--.-.": "@", ".-.-.": "+", "/": " "
        }

        message_split = message.split()
        for item in message_split:
            value2 = str(dictionary[item])
            outcome.write(value2)

    elif Code.read(7) == 'er(+3):':
        message = Code.read()
        cipherText = ""
        messagePosition = 0
        if " " in message:
            message = message.replace(" ", chr(35))
            message = message.replace("\n", chr(35))
        while messagePosition < len(message):
            messageChar = message[messagePosition]
            if "a" in messageChar:
                messageChar = messageChar.replace("a", chr(123))
            elif "b" in messageChar:
                messageChar = messageChar.replace("b", chr(124))
            elif "c" in messageChar:
                messageChar = messageChar.replace("c", chr(125))
            ASCIIValue = ord(messageChar)
            ASCIIValue = ASCIIValue - 3
            cipherText = cipherText + chr(ASCIIValue)
            messagePosition = messagePosition + 1
        else:
            value3 = str(cipherText)
            outcome.write(value3)
            outcome.close()

