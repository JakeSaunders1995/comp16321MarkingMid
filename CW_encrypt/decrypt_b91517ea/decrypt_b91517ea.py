import sys, os

for file in os.listdir(sys.argv[1]):
    with open(os.path.join(sys.argv[1], file), 'r') as f:
        file1 = str(f.read())

    newFilename = str(os.path.splitext(file)[0]) + "_b91517ea.txt"
    newFile = os.path.join(sys.argv[2], newFilename)
    file2 = open(newFile, "w")

    cipherType = file1.split(":")[0]
    text = file1.split(":")[1]
    decrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    morse = {".-": "a",   "-...": "b",   "-.-.": "c",
            "-..": "d",      ".": "e",   "..-.": "f",
            "--.": "g",   "....": "h",     "..": "i",  
           ".---": "j",    "-.-": "k",   ".-..": "l",
             "--": "m",     "-.": "n",    "---": "o", 
           ".--.": "p",   "--.-": "q",    ".-.": "r",
            "...": "s",      "-": "t",    "..-": "u", 
           "...-": "v",    ".--": "w",   "-..-": "x",
           "-.--": "y",   "--..": "z",  "-----": "0", 
          ".----": "1",  "..---": "2",  "...--": "3",
          "....-": "4",  ".....": "5",  "-....": "6", 
          "--...": "7",  "---..": "8",  "----.": "9",
              "/": " ", ".-.-.-": ".", "--..--": ",",
         "..--..": "?", "-.-.--": "!", "---...": ":",
         ".-..-.": '"', ".----.": "'", ".--.-.": "@",
         "-....-": "-", "-.-.-.": ";",  "-...-": "=",
         "..--.-": "_", "...-..-": "$", "-.--.": "(",
         "-.--.-": ")",   "-..-.": "/", ".-...": "&",
          ".-.-.": "+",      "\n": " ",
    }

    if cipherType == "Hex":
        decrypted = (bytes.fromhex(text).decode()).lower()
        file2.write(decrypted)
        file2.close()
        print(decrypted)

    elif cipherType == "Caesar Cipher(+3)":
        loweredText = text.lower()
        for character in loweredText:
            if character in alphabet:
                position = (alphabet.find(character) - 3) % 26
                decrypted += alphabet[position]
            else:
                decrypted += character
        file2.write(decrypted)
        file2.close()
        print(decrypted)

    elif cipherType == "Morse Code":
        for code in text.split(" "):
            decrypted += morse[code]
        file2.write(decrypted)
        file2.close()
        print(decrypted)