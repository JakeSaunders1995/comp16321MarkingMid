import os
import sys

#TO TAKE IN WORDS, NO NUMBERS/PUNCTUATIONS
def parse(string):
    words = []
    temp = ''

    for i in range(len(string)):
        if(string[i] == ' '):
            if(temp != ''):
                words.append(temp)
                temp = ''
                continue
        else:
            temp += string[i]

    if(temp != ''):
        words.append(temp)

    return words

def upperCount(string):
    count = 0

    for i in range(len(string)):
        asc = ord(string[i])

        if(asc >= 65 and asc <= 90):
            count += 1

    return count

def puncCount(string):
    count = 0
    i = 0

    while(1):
        if(i == len(string)):
            break

        asc = ord(string[i])

        if((asc >= 33 and asc <= 34) or
           (asc >= 39 and asc <= 41) or
           (asc >= 44 and asc <= 46) or
           (asc >= 58 and asc <= 59) or
           (asc == 63) or (asc == 91) or
           (asc == 93) or (asc == 123) or
           (asc == 125)):
            if(i <= len(string) - 3 and
                string[i + 1] == '.' and
                string[i + 2] == '.'):
                count += 1
                i = i + 3
                continue

            count += 1

        i += 1

    return count

def numberCount(string):
    count = 0

    for i in range(len(string)):
        asc = ord(string[i])

        if(asc >= 48 and asc <= 57):
            count += 1

    return count

def removeSymbols(string):
    newString = ''

    for i in range(len(string)):
        asc = ord(string[i])

        if((asc >= 33 and asc <= 34) or
           (asc >= 39 and asc <= 41) or
           (asc >= 44 and asc <= 46) or
           (asc >= 58 and asc <= 59) or
           (asc >= 48 and asc <= 57) or
           (asc == 63) or (asc == 91) or
           (asc == 93) or (asc == 123) or
           (asc == 125)):
            continue
        else:
            newString += string[i].lower()

    return newString

def typoCount(arr, filecheck):
    count = 0

    for words in arr:
        try:
            err = filecheck.index(words.lower())
        except:
            err = -1

        if(err == -1):
            count += 1

    return count

def main():
    with open(sys.argv[1], 'r') as input:
        dictionary = input.read().splitlines()

    files = os.listdir(sys.argv[2])
    for i in files:
        comp = ''

        for k in range(len(i)):
            if(i[k] == '.' or k == len(i) - 1):
                comp = sys.argv[3] + '/' + i[:k] + '_w92704dw.txt'
                break

        i = sys.argv[2] + '/' + i
        with open(i, 'r') as input:
            story = (input.read()).replace('\n', '')
            stripped = removeSymbols(story)
            words = parse(stripped)

        with open(comp, 'w') as output:
            output.write('w92704dw')
            output.write('\nFormatting ###################')
            output.write('\nNumber of upper case letters changed: ' + str(upperCount(story)))
            output.write("\nNumber of punctuations removed: " + str(puncCount(story)))
            output.write('\nNumber of numbers removed: ' + str(numberCount(story)))

            output.write('\nSpellchecking ###################')
            output.write('\nNumber of words: ' + str(len(words)))

            wrong = typoCount(words, dictionary)
            output.write('\nNumber of correct words: ' + str(len(words) - wrong))
            output.write('\nNumber of incorrect words: ' + str(wrong))


main()
            
