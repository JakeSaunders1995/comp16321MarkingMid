#Program 2 - decrypt#
#  #             #  #
#  #             #  #
#Import the contents of the text into Python for subsequent operations.
input_file_name = str (input("Please type the file name: "))
file = open ("./input_folder/" + input_file_name, "r")
filerecord = file.read()

#creat loop for distinguish which types of encryption we need to solve.
#The first if loop is for Hex.
if filerecord[0] == "H" and filerecord[1] == "e" and filerecord[2] == "x":
    #create while loop to delete extra strings ("Hex:").
    deletecount = 0
    while deletecount < 4: #here need to do 4 times.
        filerecord = list(filerecord)
        filerecord.pop(0)
        filerecord = ''.join(filerecord)
        deletecount += 1

    #delete space between each other.
    filerecord = filerecord.replace(' ','')
    #translation
    filerecord = bytes.fromhex(filerecord)
    #decode the filerecord.
    filerecord = filerecord.decode()
    print (filerecord)

#The second if is for Caesar Cipher(+3)
elif filerecord[0] == "c" or "C" and filerecord[1] == "a" and filerecord[2] == "e":
    #create while loop to delete extra strings ("caesar:").
    deletecount = 0
    while deletecount < 18: #here need to do 18 times.
        filerecord = list(filerecord)
        filerecord.pop(0)
        filerecord = ''.join(filerecord)
        deletecount += 1

    #create loop to translation.
    rec = ""
    for i in range(len(filerecord)):
        if 'a' <= filerecord[i] <= 'z':
            rec += chr( ord('a') + ((ord(filerecord[i]) - ord('a')) - 3 )%26 )#we calculate the result by reduce 3 and mod 26 by ASCII value.
        elif 'A'<= filerecord[i] <='Z':
            rec += chr( ord('A') + ((ord(filerecord[i]) - ord('A')) - 3 )%26 )
        else:
            rec += " "
    filerecord = rec

#The second is for Morse code.
elif filerecord[0] == "m" or "M" and filerecord[1] == "o" and filerecord[2] == "r":
    #create while loop to delete extra strings ("Morse:").
    deletecount = 0
    while deletecount < 11: #here need to do 11 times.
        filerecord = list(filerecord)
        filerecord.pop(0)
        filerecord = ''.join(filerecord)
        deletecount += 1

    #create the dictionary for the morse code.
    morse_dic = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.',   'f':'..-.', 'g':'--.', 'h':'....',
                 'i':'..', 'j':'.---', 'k':'-.-',  'l':'.-..','m':'--',  'n':'-.',   'o':'---', 'p':'.--.', 'q':'--.-',
                 'r':'.-.','s':'...',  't':'-',    'u':'..-', 'v':'...-','w':'.--',  'x':'-..-','y':'-.--', 'z':'--..',
                 ' ':'/'}
    #create the function to decode it.
    def de(morse_code):
        morse_code += " "
        deci = ""
        cite = ""

        for l in morse_code:
            if l != " ": #here to distinguish whether it has spaces.
                morse_i = 0
                cite += l
            else: #if it include spaces.
                morse_i += 1

                if morse_i == 2:
                    deci += " " #we do space for separate words.

                else:
                    deci += list(morse_dic.keys())[list(morse_dic.values()).index(cite)]
                    cite = ""
        return deci
    #to check whether the output is correct, and store it to filerecord.
    morse_code = filerecord
    output = de(morse_code)
    print (output)
    filerecord = output

#output the answer to output file.
input_file_name = input_file_name.replace(".txt","") #at here I need to delete the string ".txt" which users typed in
file_creation = open ("./output_folder/" + input_file_name + "_s94292yy.txt", "a")
file_creation.write (filerecord)
file_creation.close ()
#close the file to do new loop.
file.close()
