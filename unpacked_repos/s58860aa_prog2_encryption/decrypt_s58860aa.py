import os
import sys

#assign input
input_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.isdir(output_folder):
    os.mkdir(output_folder)


for file in os.listdir(input_folder):
    with open(os.path.join(input_folder, file), "r") as inputt:
        encrypted = inputt.read()

    global decrypted
    decrypted = ""
    global morse
    morse = ""
    encryptedAfter = ""
    decrypted = ""

    morse_lib = {'.-': 'A', '-...': 'B',
                 '-.-.': 'C', '-..': 'D', '.': 'E',
                 '..-.': 'F', '--.': 'G', '....': 'H',
                 '..': 'I', '.---': 'J', '-.-': 'K',
                 '.-..': 'L', '--': 'M', '-.': 'N',
                 '---': 'O', '.--.': 'P', '--.-': 'Q',
                 '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W',
                 '-..-': 'X', '-.--': 'Y', '--..': 'Z',
                 '.----': '1', '..---': '2', '...--': '3',
                 '....-': '4', '.....': '5', '-....': '6',
                 '--...': '7', '---..': '8', '----.': '9',
                 '-----': '0', '--..--': ', ', '.-.-.-': '.',
                 '..--..': '?', '-..-.': '/', '-....-': '-',
                 '-.--.': '(', '-.--.-': ')', "/": " "}

    full_length = len(encrypted)

    # finding the colon
    colon = 0
    for x in range(0, len(encrypted)):
        if (encrypted[x] == ":"):
            colon = x + 1
        else:
            x += 1

    # updating the list_encrypted so it has the text after the colon
    for k in range(0, full_length):
        if (k > (colon - 1)):
            encryptedAfter += encrypted[k]
    list_encrypted = encryptedAfter.split()
    # print("list enc", list_encrypted)
    # print("encrypt after ", encryptedAfter)

    # from more to english
    if (encrypted[0] == "M"):
        for x in list_encrypted:
            for c in morse_lib.keys():
                if c == x:
                    decrypted += morse_lib.get(c)
        decrypted = decrypted.lower()

    # from  caesar +3 to english
    elif (encrypted[0] == "C"):
        cey = "abcdefghijklmnopqrstuvwxyz"
        plaintext = ""
        for word in list_encrypted:
            for letter in word:
                position_letter = cey.find(letter)
                plaintext += cey[(position_letter - 3)]
            plaintext += " "
        decrypted = plaintext

    # from hex to enlgish
    elif (encrypted[0] == "H"):
        eng = ""
        for word in (list_encrypted):
            if word != " ":
                b = bytes.fromhex(word)
                eng += b.decode("ASCII")
            else:
                eng += " "
        decrypted = eng
        decrypted = decrypted.lower()
    # checking
    with open(os.path.join(output_folder, os.path.basename(file)[:-4] + "_s58860aa.txt"), "w")as output_file:
        output_file.write(decrypted)