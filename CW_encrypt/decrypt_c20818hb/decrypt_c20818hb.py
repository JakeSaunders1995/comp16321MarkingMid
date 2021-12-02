import sys

inputFilePath = sys.argv[1]
outputFilePath = sys.argv[2]

morseCode = [[".-", "a"], ["-...", "b"], ["-.-.", "c"], ["-..", "d"], [".", "e"], ["..-.", "f"],
             ["--.", "g"], ["....", "h"], ["..", "i"], [".---", "j"], ["-.-", "k"], [".-..", "l"],
             ["--", "m"], ["-.", "n"], ["---", "o"], [".--.", "p"], ["--.-", "q"], [".-.", "r"],
             ["...", "s"], ["-", "t"], ["..-", "u"], ["...-", "v"], [".--", "w"], ["-..-", "x"],
             ["-.--", "y"], ["--..", "z"]]

alphabet = "abcdefghijklmnopqrstuvwxyz"

with open(inputFilePath, 'r') as f:
    inputFileData = f.readline()

encryptionMethod = inputFileData[0:inputFileData.index(":")]

if encryptionMethod == "Hex":
    dataList = list(inputFileData)
    for character in dataList:
        if character == " ":
            dataList.remove(character)
    dataList = dataList[4:]
    hexString = "".join(dataList)
    decryptedString = bytes.fromhex(hexString).decode("ASCII").lower()
    
if encryptionMethod == "Morse Code":
    inputFileData = inputFileData[11:]
    dataList = inputFileData.split(" ")
    print(dataList)
    for codeIndex in range(0, len(dataList)):
        if dataList[codeIndex] == "/":
            decryptedString += " "
        for morse in range(0, 25):
            if dataList[codeIndex] == morseCode[morse][0]:
                decryptedString += morseCode[morse][1]

if encryptionMethod == "Caesar Cipher(+3)":
    inputFileData = inputFileData[18:]
    dataList = inputFileData.split(" ")
    decryptedString = ""
    for encryptedWord in dataList:
        for letter in encryptedWord:
            for alphabetPos in range(0,25):
                if letter == alphabet[alphabetPos]:
                    decryptedString += alphabet[alphabetPos - 3]
        decryptedString += " "
                
with open(outputFilePath, 'w') as f:
    f.write(decryptedString)   
