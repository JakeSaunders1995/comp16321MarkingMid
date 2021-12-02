import sys, os
input_path = sys.argv[1]
output_path = sys.argv[2]
def CC():
    list = text.split(":")
    plaintext = list[1]
    cipherText = ""
    alphabet = "xyzabcdefghijklmnopqrstuvwxyzabc"
    plaintextPosition = 0
    while plaintextPosition < len(plaintext):
        plaintextChar = plaintext[plaintextPosition]
        alphabetPosition = 3
        if plaintextChar == " ":
            cipherText = cipherText + " "
            plaintextPosition += 1
        else:
            while plaintextChar != alphabet[alphabetPosition]:
                alphabetPosition += 1
            else:
                alphabetPosition -= 3
                cipherText = cipherText + alphabet[alphabetPosition]
                plaintextPosition += 1
    else:
        return cipherText
def MC():
    list = text.split(":")
    text2 = list[1]
    message = ""
    letter_morse = {".-":"a", "-.-.":"c", "-...":"b", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l",
                    "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q",  ".-.":"r", "...":"s", "-":"t","..-":"u","...-":"v", ".--":"w", "-..-":"x", "-.--":"y",
                    "--..":"z",  "/":" "}
    letters = text2.split(" ")
    for letter in letters:
        if letter not in letter_morse:
            print(1)
        elif letter in letters:
            message += letter_morse[letter]
    return message
def hex():
    list = text.split(":")
    text1 = list[1]
    result = ""
    times = (len(text1)+1)/3
    position = 0
    for i in range(int(times)):
        ten = text1[position]
        one = text1[position+1]
        ten = int(ten, 16) * 16
        one = int(one, 16)
        num = ten + one
        result = result + chr(num)
        position+=3
    return result
for input_file in os.listdir(input_path):
    os.chdir(input_path)
    with open(input_file) as f:
        text = f.read()
        if text[0] == "H":
            ans = hex()
        elif text[0] == "C":
            ans = CC()
        elif text[0] == "M":
            ans = MC()
        name = str(f.name)
        file_list = name.split('.')
        os.chdir(output_path)
        output_file = file_list[0] + "_h50141yq." + file_list[1]
        new = open(output_file, 'w')
        new.write(ans)
        new.close()
