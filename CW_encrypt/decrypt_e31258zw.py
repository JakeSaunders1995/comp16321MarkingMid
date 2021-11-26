# Program 2 - Encryption - e31258zw - Ziyi Wang
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder_in")
parser.add_argument("folder_out")
args = parser.parse_args()

# initialization
files_arr = []      # store the files name

hex = {
    'a' : 10,
    'b' : 11,
    'c' : 12,
    'd' : 13,
    'e' : 14,
    'f' : 15
}

# check from the website https://en.wikipedia.org/wiki/Morse_code
#                   and https://morsecode.world/international/morse2.html
morse = {
    # letter (no uppercase -> lowercase)
    ".-" : 'a', "-..." : 'b', "-.-." : 'c', "-.." : 'd', "." : 'e', "..-." : 'f', "--." : 'g',
    "...." : 'h', ".." : 'i', ".---" : 'j', "-.-" : 'k', ".-.." : 'l', "--" : 'm', "-." : 'n',
    "---" : 'o', ".--." : 'p', "--.-" : 'q', ".-." : 'r', "..." : 's', "-" : 't',
    "..-" : 'u', "...-" : 'v', ".--" : 'w', "-..-" : 'x', "-.--" : 'y', "--.." : 'z',
    # number
    ".----" : '1', "..---" : '2', "...--" : '3', "....-" : '4', "....." : '5',
    "-...." : '6', "--..." : '7', "---.." : '8', "----." : '9', "-----" : '0',
    # symbols -> not include
    # ".-.-.-" : '.', "--..--" : ',', "..--.." : '?', "-.-.--" : '!', "---..." : ':',
    # ".-.-." : '+', "-...-" : '=', "-.--.": '(', "-.--.-" : ')', ".--.-." : '@',
    # ".-..." : '&', ".-..-." : '"', ".----." : "'", "-..-." : '/', "-....-" : '-',
    # "-.-.-." : ';', "..--.-": '_', "...-..-": '$', 
}


def file_name(folder):
    """ 
    function to get the files from the folder
    :folder: the folder where the file needs to be extracted
    """
    global files_arr
    for files in os.walk(folder):
        files_arr = files[2]


def decrypt_Caesar(ci_text,count):
    """ 
    function to decrypt the cipher-text in caesar +3 mode, only transfer the letters, punctuation and others will remain the same
    :ci_text: the string from the input file
    :count: the index of the string
    """
    global de_str
    while (count < len(ci_text)):
        # begin decrypt
        ciChar = ci_text[count]
        if (ciChar == " "):
            de_str = de_str + " "   # keep the space
            count += 1
        else:   # letters
            if (ciChar == 'a' or ciChar == 'A'):
                de_str = de_str + 'x'
                count += 1
            elif (ciChar == 'b' or ciChar == 'B'):
                de_str = de_str + 'y'
                count += 1
            elif (ciChar == 'c' or ciChar == 'C'):
                de_str = de_str + 'z'
                count += 1
            else:
                ci_ascii = ord(ciChar)      # convert Char to its ASCII value
                ci_ascii -= 3
                if (ci_ascii > 64 and ci_ascii < 88):   # A -> 65; W -> 87
                    ci_ascii = ci_ascii + 32    # convert to lowercase
                    de_str = de_str + chr(ci_ascii)
                    count += 1
                elif (ci_ascii > 96 and ci_ascii < 120):  # w -> 119
                    de_str = de_str + chr(ci_ascii)
                    count += 1
                else:   # any other not letter character will remain the same
                    de_str = de_str + chr(ci_ascii + 3)
                    count += 1


def decrypt_Hex(ci_text,count):
    """ 
    function to decrypt the cipher-text in hexadecimal mode
    :ci_text: the string from the input file
    :count: the index of the string
    """
    global de_str
    ci_ascii = 0    # store the ASCII value of a character
    while (count < len(ci_text)):
        # begin decrypt
        ciChar = ci_text[count]
        if (ciChar == " " or ciChar == '\n'):
            count += 1
            if (ci_ascii != 0):
                # converting uppercase -> lowercase
                if (ci_ascii > 64 and ci_ascii < 91):   # A -> 65; Z -> 90
                    de_str = de_str + chr(ci_ascii + 32)
                else:
                    de_str = de_str + chr(ci_ascii)
            ci_ascii = 0
        else:
            # print("ths char is",ciChar)
            if ciChar in "0123456789":
                ci_ascii = ci_ascii * 16 + int(ciChar)
            else:
                ci_ascii = ci_ascii * 16 + hex[ciChar]
            count += 1
            # print("now the ci_acsii is", ci_ascii)

    # do remember to add the last character if there is no space or '\n' in the end
    if (ci_ascii != 0): 
        de_str = de_str + chr(ci_ascii)


def decrypt_Morse(ci_text, count):
    """ 
    function to decrypt the cipher-text in morseCode mode
    :ci_text: the string from the input file
    :count: the index of the string
    """
    global de_str
    char = ""
    while (count < len(ci_text)):
        # begin decrypt
        ciChar = ci_text[count]
        if (ciChar == " " or ciChar == '\n'):
            if (char != ""):
                # try to find in the dic -> if not find key, add a '#'
                try:
                    de_str = de_str + morse[char]
                except:
                    de_str = de_str + '#'
                char = ""
            count += 1
        elif (ciChar == '/'):
            de_str = de_str + " "   # space
            count += 2      # char after '/' is still a space
        else:
            char = char + ciChar
            count += 1 
    # do remember to add the last character if there is no space or '\n' at the end
    if (char != ""):
        try:
            de_str = de_str + morse[char]
        except:
            de_str = de_str + '#'


def skip_begin(ci_text):
    """ 
    a function to skip the beginning of the input file which is not the encrypted text
    return a int which is the index of the starting of the encrypted text 
    :ci_text: the string from the input file
    """
    count = 0
    # Skip string at the beginning
    while(count < len(ci_text)):
        ci_Char = ci_text[count]     # get one character
        if (ci_Char == ":"):
            count += 1
            return count
        else:
            count += 1
    # if ':' is not in the string
    return 0


# main program ----------------------------------------------------------------

file_name(args.folder_in)

# no need to check now
# check if the output folder exist -> if not, create
# if not os.path.exists(args.folder_out):
#     os.makedirs(args.folder_out)

for item in files_arr:
    de_str = ""     # store the decrypted string

    file_in_path = args.folder_in + "/" + item
    file_out_path = args.folder_out + "/" + item[:-4] + "_e31258zw.txt"

    # open the file in read mode -> read into a string
    file_r = open(file_in_path,"r")
    str_in = file_r.read()

    file_r.close()

    # the index of the encrypt text
    index = skip_begin(str_in)

    # to decide to decrypt in which mode
    if "Hex" in str_in:
        decrypt_Hex(str_in, index)
    elif "Caesar" in str_in:
        decrypt_Caesar(str_in, index)
    elif "Morse" in str_in:  
        decrypt_Morse(str_in, index)


    # open the file for writing, create if it doesn't exist
    file_w = open(file_out_path,"w")

    file_w.write(de_str)
    file_w.close()

