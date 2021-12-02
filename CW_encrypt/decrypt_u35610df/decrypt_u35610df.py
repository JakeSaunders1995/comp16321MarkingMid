import os, sys


def decodeHex(splitString):
    splitString = splitString.split(':')
    hexDict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '//':'\n'}
    # print(f'{splitString[1] = }')
    splitString = splitString[1].split(" ")

    # print(f'{splitString = }')
    string = ''
    for index, each in enumerate(splitString):
        # print(f'{each = } and {index = }')
        
        if len(each) > 2:
            # print(f'length is greater than 2! {len(each) = }')
            each = each.replace('\n', '/')
            loopNumber = len(each)
            for i in range(0, loopNumber):
                if each[i] == '/':
                    string += '\n'
                else:
                    try:
                        if each[i] != '\n' and each[i + 1] != '\n':
                            string += chr(16 * hexDict[each[i]] + hexDict[each[i + 1]])
                    except:
                        pass

        else:
            string += chr(16 * hexDict[each[0]] + hexDict[each[1]])


    print(f'translated {string.lower() = }')

    return string.lower()


def decodeMorse(splitString):
    splitString = splitString.split(':')

    morseDict = { '.-': 'a', '-...': 'b','-.-.': 'c', '-..':'d', 
                    '.':'e', '..-.':'f', '--.': 'g', '....':'h',
                    '..':'i', '.---':'j', '-.-':'k','.-..':'l', 
                    '--':'m', '-.':'n', '---': 'o', '.--.':'p', 
                    '--.-':'q','.-.':'r', '...':'s', '-':'t',
                    '..-':'u', '...-':'v', '.--':'w', '-..-':'x', 
                    '-.--':'y', '--..':'z','.----':'1', '..---':'2', 
                    '...--':'3','....-':'4', '.....':'5', '-....':'6',
                    '--...':'7', '---..':'8', '----.':'9',
                    '-----':'0', '--..--':',', '.-.-.-':'.',
                    '..--..':'?', '-..-.':'/', '-....-':'-',
                    '-.--.':'(', '-.--.-':')', '-.-.--':'!',
                    '-.-.-.':';', '---...':':','.-.-.':'+',
                    '-...-':'=', '/': '\n'}

    splitStringWords = splitString[1].split('/')
    # print(f'{splitStringWords = }')
    # print(f'{len(splitStringWords) = }')
    for index, each in enumerate(splitStringWords):
        # print(f'{splitStringWords[index] = }')

        tmpList = list(splitStringWords[index])
        # print(f'{tmpList = }')
        nl = '\n'
        # print(f'{nl in tmpList}')


        try:
            while '\n' in tmpList:
                # print(f'"\ n" in {splitStringWords}')
                try: 
                    tmpList = tmpList.replace('\n', ' / ')   
                except:
                    print("can't replace")
                    pass
                # print(f'{tmpList = }')
                tmpList = "".join(tmpList)
                splitStringWords[index] = tmpList
                # print(splitStringWords[index])

        except:
            pass
    # print(splitStringWords)
    finalList = []

    for index, each in enumerate(splitStringWords):
        finalList.append(each.split(' '))

    string = ''
    for word in finalList:

        # print(f'{word = }')

        for char in word:

            # print(f'{char = }')

            if char != '':

                # print(f'{morseDict[char]}')
                string += morseDict[char]
        string += " "   
    print(f'translated {string.lower() = }')

    return string.lower()

# change 65 to 97
# bot 33  and top is 126

def decodeCaesar(splitString):
    splitString = splitString[17:]
    alphabet = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w', 'x','y','z']
    # print(f'{splitString = }')
    
    print(f'we know that there is an apostrophe seperating each index and {len(splitString) = }')
    string = ''
    for i in range(1, len(splitString)):
        splitStringTemp = splitString[i].lower()
        
        for index,char in enumerate(splitStringTemp):
            # print(f'{char = }')
            if char not in alphabet:
                # we can assume it's punctuation
                # print("it's punctuation")
                string += char
                pass
            # print(f'{char = }')
            # if char == '\n':
            #     # print("it's a newline")
            #     string += '\n'
            #     pass
            # print(f'{char = }')
            # if char == " ":
            #     string += " "
            if char in alphabet:
                num = ord(char) - 3
        
                if num < 97:
                    num += 26


                string += chr(num)
        
            # print(f'{string = }')
    # print(f'{"".join(string) = }')
    print(f'translated {string = }')
    return string
    
    ###     Code below is not as robust as code above, however it was tested more than code above 
    #                       with test data containing no apostrophes

    # splitString = splitString[1].lower()
    # print(f'{splitString = }')
    # string = ''
    # for index,char in enumerate(splitString):
    #     print(f'{char = }')
    #     if char not in alphabet:
    #         # we can assume it's punctuation
    #         print("it's punctuation")
    #         pass

    #     if char == '\n':
    #         # print("it's a newline")
    #         string += '\n'
    #         pass

    #     if char == " ":
    #         string += " "
    #     elif ord(char) != 10:
    #         num = ord(char) - 3
     
    #         if num < 97:
    #             num += 26


    #         string += chr(num)

    #     # print(f'{string = }')
    # print(f'translated (no apostrophes) {string = }')
    # return string


def decrypt(string, fileName):
    splitString = string

    functionDict = {'H': decodeHex, 'M': decodeMorse, 'C': decodeCaesar, 'h': decodeHex, 'm': decodeMorse, 'c': decodeCaesar}
    output = functionDict[string[0]](splitString)

    outputFilePath = outputFolder + '/' + fileName.rstrip('.txt') + '_u35610df'
    outputFile = open(outputFilePath, 'w')
    outputFile.write(output)
    outputFile.close()



inputFolder = sys.argv[1]
outputFolder = sys.argv[2]
inputFiles = os.listdir(inputFolder)   

for each in inputFiles:
    filename = each
    inputFilePath = inputFolder + '/' + filename
    inputFile = open(inputFilePath, 'r')
    string = ''
    # for line in inputFile:  
    #     string += line + '\n'
    string = "".join(inputFile.readlines())
    
    print('\n\n'+filename )
    print(f'{string = }')
    decrypt(string, filename)



# string = 'Hex:53 6f 6c 76 69 6e 67 20 68 65 78 20 69 73 20 76 65 72 79 20 65 61 73 79 20 69 6e 20 70 79 74 68 6f 6e'
# string = 'Morse Code:.... --- .-- . ...- . .-. / ... --- .-.. ...- .. -. --. / -- --- .-. ... . / -.-. --- -.. . / -- .- -.-- / -... . / - .... . / -- --- ... - / -.. .. ..-. ..-. .. -.-. ..- .-.. -'
# string = 'Caesar Cipher(+3):exw fdhvdu lv d olwwoh pruh gliilfxow'

