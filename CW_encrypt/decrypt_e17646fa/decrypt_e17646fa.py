import sys
import os


output =[]
index =0
#assign directory
directory = os.listdir(sys.argv[1])
directory.sort()
# for files in directory:
#     with open(sys.argv[1]+"/"+files, 'r') as h:
#         result= h.read()
        #print(result)

# inputFile = sys.argv[1]
# outputFile = sys.argv[2]
#
# with open(inputFile, 'r') as input:
#     result = input.read()

def hexToEng(result):
    result = result[4:]
    result = result.replace(" ", "")
    bytes_object = bytes.fromhex(result)
    result = bytes_object.decode("ASCII")

    # with open(outputFile, "w+") as output:
    #     output.write(result)
    return result

def CaeToEng(result):
    resultList = list(result[18:])
    j = 0
    while j < len(resultList):
        if (ord(resultList[j]) <= 122 and ord(resultList[j]) >= 100):
            k = ord(resultList[j]) - 3
            resultList[j] = chr(k)
        elif (ord(resultList[j]) == 97):
            resultList[j] = 'x'
        elif (ord(resultList[j]) == 98):
            resultList[j] = 'y'
        elif (ord(resultList[j]) == 99):
            resultList[j] = 'z'
        j = j + 1
    # l= print(''.join(str(resultList)))
    # with open(outputFile, "w+") as output:
    #     output.write(''.join(resultList))
    return ''.join(resultList)


def MorToEng(result):

    morseD = {
        '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '
    }


    lenword = len(result)
    result = result[11:]
    result = result.split()
    words = ''
    n = ''
    for i in result:
        if i != ' ':
            words=words+i
            if i not in morseD:
                break

            n +=morseD[words]
            words = ''
    return n

for files in directory:
    with open(sys.argv[1]+"/"+files, 'r') as u:
        string = u.read()
        with open(sys.argv[2]+"/"+files[:-4]+ '_e17646fa.txt','w+') as h:
            if (string[0] == "H" ):
                h.write(hexToEng(string))
            elif (string[0] == "C" ):
                h.write(CaeToEng(string))
            elif (string[0] == "M" ):
                h.write(MorToEng(string))
    # with open(outputFile, "w+") as output:
    #     output.write(result)

        # with open(outputFile, "w+") as output:
        #     output.write(str(n))
