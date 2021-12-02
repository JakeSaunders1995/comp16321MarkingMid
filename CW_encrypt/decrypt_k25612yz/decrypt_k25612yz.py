import sys
import os

a = sys.argv[1]
b = sys.argv[2]

if (a[-1] != '/'):
	a += '/' 
if (b[-1] != '/'):
	b += '/'

test = os.path.exists(b)
if not test:              
    os.makedirs(b)

for (d1,d2,fs) in os.walk(a):
    for file in fs:
        bt=b
        temp = a + file
        fold_ = open(temp)
        s = fold_.read()
        output = ""

        if (s[0] == "H"):
            t = s[4:-1]+s[-1]
            h = "0"
            for i in range(len(t)):
                if (t[i] != " "):
                    h += t[i]
                elif (t[i] == " "):
                    d = int(h,16)
                    if ( d >= 65 and d <= 90 ):
                        d += 32
                    output += str(chr(d))
                    h = "0"
            output += str(chr(int(h,16)))
            if (ord(output[-1]) == 0):
                output=output[0:-1]

        elif (s[0] == "C"):
            t = s[18:-1] + s[-1]
            for i in range(len(t)):
                d = ord(t[i])
                if ((d >= 65 and d <= 90) or (d >= 97 and d <= 122)):
                    if ( d >= 65 and d <= 90 ):
                        d += 32
                    if (d <= 99):
                        d += 26
                    output += chr(d-3)
                elif (t[i] == " "):
                    output += " "
            
        elif (s[0] == "M"):
            t = s[11:-1] + s[-1]
            m = ""
            for i in range(len(t)):
                if (t[i] == " "):
                    r = ""
                    if (m != ""):
                        if (m == ".-"):
                            r = "a"
                        elif (m == "-..."):
                            r = "b"
                        elif (m == "-.-."):
                            r = "c"
                        elif (m == "-.."):
                            r = "d"
                        elif (m == "."):
                            r = "e"
                        elif (m == "..-."):
                            r = "f"
                        elif (m == "--."):
                            r = "g"
                        elif (m == "...."):
                            r = "h"
                        elif (m == ".."):
                            r = "i"
                        elif (m == ".---"):
                            r = "j"
                        elif (m == "-.-"):
                            r = "k"
                        elif (m == ".-.."):
                            r = "l"
                        elif (m == "--"):
                            r = "m"
                        elif (m == "-."):
                            r = "n"
                        elif (m == "---"):
                            r = "o"
                        elif (m == ".--."):
                            r = "p"
                        elif (m == "--.-"):
                            r = "q"
                        elif (m == ".-."):
                            r = "r"
                        elif (m == "..."):
                            r = "s"
                        elif (m == "-"):
                            r = "t"
                        elif (m == "..-"):
                            r = "u"
                        elif (m == "...-"):
                            r = "v"
                        elif (m == ".--"):
                            r = "w"
                        elif (m == "-..-"):
                            r = "x"
                        elif (m == "-.--"):
                            r = "y"
                        elif (m == "--.."):
                            r = "z"
                        elif (m == ".----"):
                            r = "1"
                        elif (m == "..---"):
                            r = "2"
                        elif (m == "...--"):
                            r = "3"
                        elif (m == "....-"):
                            r = "4"
                        elif (m == "....."):
                            r = "5"
                        elif (m == "-...."):
                            r = "6"
                        elif (m == "--..."):
                            r = "7"
                        elif (m == "---.."):
                            r = "8"
                        elif (m == "----."):
                            r = "9"
                        elif (m == "-----"):
                            r = "0"
                    m = ""
                    output += r
                elif (t[i] == "/"):
                    output += " "
                else:
                    m += t[i]

            if (m != ""):
                if (m == ".-"):
                    r = "a"
                elif (m == "-..."):
                    r = "b"
                elif (m == "-.-."):
                    r = "c"
                elif (m == "-.."):
                    r = "d"
                elif (m == "."):
                    r = "e"
                elif (m == "..-."):
                    r = "f"
                elif (m == "--."):
                    r = "g"
                elif (m == "...."):
                    r = "h"
                elif (m == ".."):
                    r = "i"
                elif (m == ".---"):
                    r = "j"
                elif (m == "-.-"):
                    r = "k"
                elif (m == ".-.."):
                    r = "l"
                elif (m == "--"):
                    r = "m"
                elif (m == "-."):
                    r = "n"
                elif (m == "---"):
                    r = "o"
                elif (m == ".--."):
                    r = "p"
                elif (m == "--.-"):
                    r = "q"
                elif (m == ".-."):
                    r = "r"
                elif (m == "..."):
                    r = "s"
                elif (m == "-"):
                    r = "t"
                elif (m == "..-"):
                    r = "u"
                elif (m == "...-"):
                    r = "v"
                elif (m == ".--"):
                    r = "w"
                elif (m == "-..-"):
                    r = "x"
                elif (m == "-.--"):
                    r = "y"
                elif (m == "--.."):
                    r = "z"
                elif (m == ".----"):
                    r = "1"
                elif (m == "..---"):
                    r = "2"
                elif (m == "...--"):
                    r = "3"
                elif (m == "....-"):
                    r = "4"
                elif (m == "....."):
                    r = "5"
                elif (m == "-...."):
                    r = "6"
                elif (m == "--..."):
                    r = "7"
                elif (m == "---.."):
                    r = "8"
                elif (m == "----."):
                    r = "9"
                elif (m == "-----"):
                    r = "0"
                output += r

        bt += os.path.splitext(file)[0] + '_k25612yz.txt'
        wp=open(bt,'w')
        wp.write(output)
        wp.close()