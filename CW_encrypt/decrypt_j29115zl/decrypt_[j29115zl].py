import sys
import os

input_path = sys.argv[1]
output_path = sys.argv[2]

input_list = os.listdir(input_path)
input_list.sort()
output_list = os.listdir(output_path)

MorseList = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G",
    "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N",
    "---": "O", ".--．": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"
}

def morse(string, sign):
    ans = ''
    lists = string.split(sign)
    for code in lists:
        if code != '/':
            ans += MorseList.get(code)
        else:
            ans += " "
    return ans

for file in input_list:
    with open(input_path + file, "r") as fr:
        data = fr.read()
        index = -1
        for i in range(len(data)):
            if data[i] == ':':
                index = i
                break        
        method = data[0:index]
        if method == 'Hex':
            ans = ''
            i = index + 1
            while i < len(data):
                st = data[i:i+2]
                num = int(st, 16)
                ans += chr(num)
                i = i + 3
            ans = ans.lower()
            
            output_file = file[0:10] + '_[j29115zl]' + file[10:]
            with open(output_path + output_file, "w+") as fw:
                fw.write(ans + "\n")
            
        elif method == 'Caesar Cipher(+3)':
            ans = ''
            i = index + 1
            while i < len(data): 
                st = data[i]
                num = ord(st)
                if num < ord('a') or num > ord('z'):
                    ans += ' '
                else:
                    pt = num - 3
                    if pt < 97:
                        pt += 26
                    ans += chr(pt)
                i = i + 1
            ans = ans.lower()
            output_file = file[0:10] + '_[j29115zl]' + file[10:]
            with open(output_path + output_file, "w+") as fw:
                fw.write(ans + "\n")
            
        elif method == 'Morse Code':
            ans = morse(data[index+1 :], " ")
            ans = ans.lower()
            
            output_file = file[0:10] + '_[j29115zl]' + file[10:]
            with open(output_path + output_file, "w+") as fw:
                fw.write(ans + "\n")
            
            
