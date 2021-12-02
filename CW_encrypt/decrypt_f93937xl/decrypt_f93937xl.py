import binascii
import argparse
import os


parser = argparse.ArgumentParser(description='rugby')
parser.add_argument('input_path', type=str, help='A required string argument -- input path')
parser.add_argument('output_path', type=str, help='A required string argument -- output path')


args = parser.parse_args()


input_path = args.input_path
output_path = args.output_path
input_files = os.listdir(input_path)
output_files = os.listdir(output_path)


a = 0
while a < len(input_files):
    input_file = input_files[a]
    input_path_1 = input_path + "/" + input_file
    with open(input_path_1, "r") as f:
        lst = f.read()
        if lst[0] == "H":
            lst1 = lst
            a1 = lst1[4:]
            b1 = a1.split()
            c1 = "".join(b1)
            t1 = c1
            s = binascii.a2b_hex(t1)
            char = str(s)
            s2 = char[2: -1]
            answer = (s2.lower())
        if lst[0] == "C":
            lst2 = lst
            a2 = lst2[18:]
            t2 = a2.strip()
            cipherText = " "
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            plaintextPosition = 0
            while plaintextPosition < len(t2):
                plaintextChar = t2[plaintextPosition]
                alphabetPosition = 0
                if plaintextChar == " ":
                    cipherText = cipherText + " "
                else:
                    while plaintextChar != alphabet[alphabetPosition]:
                        alphabetPosition = alphabetPosition + 1
                    alphabetPosition = alphabetPosition - 3
                    cipherText = cipherText + alphabet[alphabetPosition]
                plaintextPosition = plaintextPosition + 1
                answer = (cipherText.lower().strip())
        if lst[0] == "M":
            answer3 = ""
            lst3 = lst
            a3 = lst3[11:]
            t3 = a3.split()
            MorseList = {
                ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
                "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
                "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z",
                "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
                ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",
                ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?",
                "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-",
                "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$",
                ".--.-.": "@", ".-.-.": "+", "/": " "
            }
            for item in t3:
                answer3 += MorseList[item].lower()
            answer = answer3
    output_file = input_file[:-4] + "_f93937xl" + input_file[-4:]
    output_path_1 = output_path + "/" + output_file
    with open(output_path_1, "w+") as f:
        answer = f.write(answer)
    a += 1


f.close()