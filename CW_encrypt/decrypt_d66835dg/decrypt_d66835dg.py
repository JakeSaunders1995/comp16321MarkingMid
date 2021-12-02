import sys, os

def hexDecrypt(text):
    out_txt = ""
    for i in range(len(text)):
        text[i] = text[i].upper()
        byte_array = bytes.fromhex(text[i])
        out_txt += byte_array.decode()
    out_txt = out_txt.lower()
    return out_txt

def caesarDecrypt(text):
    out_txt = ""
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c"]
    numbers = ["1","2","3","4","5","6","7","8","9","0","1","2","3"]
    for i in range(len(text)):
        text[i] = text[i].lower()
        for j in range(len(text[i])):
            out_c = ""
            if text[i][j].isalpha():
                alphaPos = len(alphabets) - 1
                while True:
                    if text[i][j] == alphabets[alphaPos]:
                        out_c = alphabets[alphaPos-3]
                        break
                    alphaPos -= 1
            elif text[i][j].isnumeric():
                numPos = len(numbers) - 1
                while True:
                    if text[i][j] == numbers[numPos]:
                        out_c = numbers[numPos-3]
                        break
                    numPos -= 1
            else:
                out_c = text[i][j]
            out_txt += out_c
        out_txt += " "
    return out_txt

def morseDecrypt(text):
    out_txt = ""
    morsedict = {
    ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z",
    ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5","-....":"6","--...":"7","---..":"8", "----.":"9", "-----":"0",
    ".-.-.-":".", "--..--":",", "-.--.":"(", "-.--.-":")", "---...":":", ".----.":"'", ".-..-.":"\"", "-....-":"-", ".-.-.":"+", "-...-":"=", ".-...":"&", ".--.-.":"@", "-.-.--":"!", "-..-.":"/", "..--..":"?", "/":" "
    }
    for i in range(len(text)):
        out_txt += morsedict[text[i]]
    return out_txt

f_in = sys.argv[1]
f_out = sys.argv[2]

for in_f_name in os.listdir(f_in):
    input_file = open(os.path.join(f_in, in_f_name), "r")
    # to store the message in the input file into a list
    input_message = input_file.readline().split(":")


    encrypt_message = input_message[1].split()
    output_message = ""

    if "hex" in input_message[0].lower():
        output_message = hexDecrypt(encrypt_message)
    elif "caesar" in input_message[0].lower():
        output_message = caesarDecrypt(encrypt_message)
    elif "morse" in input_message[0].lower():
        output_message = morseDecrypt(encrypt_message)
    in_f_name_arr = in_f_name.split(".")
    out_f_name = in_f_name_arr[0] + "_d66835dg." + in_f_name_arr[1]
    try:
        output_file = open(os.path.join(f_out, out_f_name), "w")
    except:
        os.makedirs(f_out)
        out_f_name = in_f_name_arr[0] + "_d66835dg." + in_f_name_arr[1]
        output_file = open(os.path.join(f_out, out_f_name), "w")
    output_file.write(output_message)
