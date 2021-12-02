import os, sys, re

for filename in os.listdir(sys.argv[1]):
    with open(os.path.join(sys.argv[1], filename), 'r') as f:
        if filename.endswith(".txt"):
            code = f.read().rstrip()
            mode, todecrypt = code.split(":")
            todecrypt = todecrypt.lower()
            c = re.search("^Caesar", code)
            h = re.search("^Hex", code)
            m = re.search("^Morse", code)
            if c:
                cipherText = todecrypt
                plainText = ""
                alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc "
                cipherTextPosition = 0
                while(cipherTextPosition < len(cipherText)):
                    cipherTextChar = cipherText[cipherTextPosition]
                    alphabetPosition = 3
                    while cipherTextChar != alphabet[alphabetPosition]:
                        alphabetPosition += 1
                    alphabetPosition -= 3
                    if cipherTextChar == " ":
                        plainText += " "
                    else:
                        plainText += alphabet[alphabetPosition]
                    cipherTextPosition += 1
                filename = filename[:-4]
                path = sys.argv[2]
                f = open(os.path.join(path, filename + "_e58690mu.txt"), 'w')
                f.write(plainText)
            elif h:
                Hexadecimal = todecrypt
                plainText = ""
                hex = bytes.fromhex(Hexadecimal)
                plainText = hex.decode("ASCII")
                filename = filename[:-4]
                path = sys.argv[2]
                f = open(os.path.join(path, filename + "_e58690mu.txt"), 'w')
                f.write(plainText.lower())
            elif m:
                plainText = ""
                morseCode = todecrypt
                morse = {
                            "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
                            "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                            "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
                            "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                            "y": "-.--", "z": "--..", " ": "/",
                }

                words = morseCode.split(" ")
                for item in words:
                    letters = item.split(" ")
                    for char in letters:
                        if char == "/":
                            plainText += " "
                        else:
                            for i, j in morse.items():
                                if char == j:
                                    plainText += i
                filename = filename[:-4]
                path = sys.argv[2]
                f = open(os.path.join(path, filename + "_e58690mu.txt"), 'w')
                f.write(plainText)
        else:
            continue
