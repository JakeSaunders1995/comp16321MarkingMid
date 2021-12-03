import argparse
import os


n = 1 # output in filename(n) in the loop

parser = argparse.ArgumentParser()
parser.add_argument('folder1')
parser.add_argument('folder2')
args = parser.parse_args()
folder_1 = args.folder1
folder_2 = args.folder2
a = os.listdir(folder_1)
a.sort(key = lambda x:int(x[-5:-4]))
os.chdir(folder_1)
for item in a:
    file = open(item, 'r')
    code = file.readline()

    new_code1 = code.replace("Morse Code:", "")
    new_code2 = code.replace("Hex:", "")
    new_code3 = code.replace("Caesar Cipher(+3):", "")


    def decrypt_hex():
        number = new_code2.replace(" ", "")
        test = bytes.fromhex(number).decode('utf-8')
        print(str(test).lower())
        return test


    def seperate(initial_list, e):   
        list_new=[]				
        list_temp=[]			
        for i in initial_list:
            if i!=e:		
                list_temp.append(i)
            else:
                list_new.append(list_temp)
                list_temp=[]
        list_new.append(list_temp) 
        return list_new


    def decrypt_caesar():
        new_cipher_text = seperate(new_code3, " ")
        caesar_text = ""
        n = 0
        while n < len(new_cipher_text):
            for c in new_cipher_text[n]:
                ascii_value = ord(c)
                if (ord(c) == 97 or ord(c) == 65):
                    new_ascii_value = 120
                elif (ord(c) == 98 or ord(c) == 66):
                    new_ascii_value = 121
                elif (ord(c) == 99 or ord(c) == 67):
                    new_ascii_value = 122
                elif (ord(c) >= 60 and ord(c) <= 90):
                    new_ascii_value = ascii_value + 29
                else:
                    new_ascii_value = ascii_value - 3
                caesar_text = caesar_text + chr(new_ascii_value)
            caesar_text = caesar_text + " "
            n += 1
        print(caesar_text.lower())
        return caesar_text.lower()


    def decrypt_morse(string, sign):
        morseList = {
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--．": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z",

        "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9",

        ".-.-.-": ".", "---...": ":", "--..--": ",", "-.-.-.": ";", "..--..": "?", "-...-": "=", ".----.": "'", "-..-.": "/", "-.-.--": "!", "-....-": "-", "..--.-": "_", ".-..-.": '"', "-.--.": "(", "-.--.-": ")", "...-..-": "$", ".--.-.": "@", ".-.-.": "+",
        }
        lists = string.split(sign)
        new_list = seperate(lists, '/')
        n = 0
        morse_text = ""
        while n < len(new_list):
            for text in new_list[n]:
                morse_text = morse_text + morseList.get(text)
            morse_text = morse_text + " "
            n += 1
        morse_text = morse_text.strip(" ")
        print(morse_text)
        return morse_text
        

    pardir = os.path.abspath(os.path.join(os.path.dirname(folder_1),os.path.pardir))
    # print(os.listdir(pardir))
    # b = os.listdir(folder_2)
    os.chdir(pardir)
    os.chdir(folder_2)
    if ("." in new_code1):
        with open(("%s%d_m50747jh.txt") %(item[:-5], n), "wt") as f:
            f.write(str(decrypt_morse(new_code1, " ")))
        f.close()
    elif (code[0] == "H" or code[0] == "h"):
        with open(("%s%d_m50747jh.txt") %(item[:-5], n), "wt") as f:
            low_case = str(decrypt_hex()).lower()
            f.write(low_case)
        f.close()
    else:
        with open(("%s%d_m50747jh.txt") %(item[:-5], n), "wt") as f:
            f.write(str(decrypt_caesar()))
        f.close()
    n += 1

    pardir2 = os.path.abspath(os.path.join(os.path.dirname(folder_2),os.path.pardir))
    # print(pardir2)
    os.chdir(pardir2)
    os.chdir(folder_1)