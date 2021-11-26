import sys
import os
def hexadecimal(d):
    d = d[4:]
    d = d + " "
    i = 0
    word = ""
    a = ""
    for char in d:
        if (char != " "):
            word = word + char
        else:
            i = i + 1
            bytes_object = bytes.fromhex(word)
            ascii_string = bytes_object.decode("ASCII")
            a = a + ascii_string
            word = ""
    output = str(sys.argv[2]) + "/" + str("output")
    o = open( output, "w")
    o.write(a)

def caesar(d):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if d[0] == "C":
        d = d[18 : ]
    d = d + " "
    a = ""
    word = ""
    for char in d:
        if (char != " "):
            letter_index = (alpha.find(char) - 3) % len(alpha)
            word = word + alpha[letter_index]
        else:
            a = a + word + " "
            word = ""
    output = str(sys.argv[2]) + "/" + str("output")
    o = open( output, "w")
    o.write(a)

def morse(d):
    morse_to_eng = {'....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' '}
    d = d[11:]
    a = ""
    d = d + " "
    word = ""
    for char in d:
        if (char != " "):
            word = word + char
        elif (char == '/'):
            a = a + morse_to_eng[word] + " "
        else:
            a = a + morse_to_eng[word]
            word = ""
    output = str(sys.argv[2]) + "/" +str("output")
    o = open( output, "w")
    o.write(a)

def main():
    y = sys.argv[1]
    files = os.listdir(y)
    z = ""
    for x in files:
        z = str(y) + "/" + str(x)
        if z[-3:] == "txt":
            f = open(z)
            d = f.read()
            if d[0] == "H":
                hexadecimal(d)
            elif d[0] == "M":
                morse(d)
            elif d[0] == "C":
                caesar(d)
        z = ""
if __name__ == "__main__":
    main()
