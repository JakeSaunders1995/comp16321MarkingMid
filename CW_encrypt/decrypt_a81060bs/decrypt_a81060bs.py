


#my code goes here:
# NOTE: the file should show its contents in this form: algorith : ciphertext. assume the file is imported.

# NOTE: establishing dictionary:
# NOTE: Curly brackets are used to define a dictionary
# Morse Code dictionary => (MCD)
morse_to_eng = { '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ' }

import sys
# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

f = open(sys.argv[1], 'r')
file = f.read()
z = open(sys.argv[2], 'w')
# output_file = z.write()
# print(output_file)



# NOTE: the code below shows the key word that appears before ':'
alg = (file.split(':')[0])

# NOTE: The code below eleminates Morse code and : to create a better list.
string = file.replace(alg+':', '')
message = string.split()
# NOTE: from morse to english.



if alg == 'Hex':
    # NOTE: decryption goes here
    print('This is hex code')
    # NOTE: the code below shows the key word that appears before ':'
    alg = (file.split(':')[0])
    # NOTE: Making a list from a file
    string = file.replace(alg+':', '')
    message = string.split()

    hex = bytes.fromhex(string)
    ascii_string = hex.decode("ASCII")
    print(ascii_string.lower())
    output_file = z.write(ascii_string.lower())
    # print(output_file)

elif alg =='Caesar Cipher(+3)':
    # NOTE: decryption goes here
    print('This is Caesar Cipher')
    message = list(string)
    # print(message)
    decoded_message =''
    # print(string)
    for x in message:
        decoded = ord(x) - 3
        if decoded > ord('z'): #ord converts a character into its Unicode code value
            decoded -= 26
        elif x == ' ':
            decoded_message += ' '
        final_chr = chr(decoded)
        decoded_message += final_chr
    output_file = z.write(decoded_message.lower())
    # print(output_file)

    print(decoded_message)
elif alg =='Morse Code':
    # NOTE: decryption goes here
    print('The file is Morse Code')
    for x in message:
        if x not in morse_to_eng:
            print('Wrong data!')
            break
        else:
            y = morse_to_eng[x]
            output_file = z.write(y.lower())
            print(y, end = '')
