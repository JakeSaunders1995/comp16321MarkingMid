import sys
import os

a = sys.argv[2]
b = sys.argv[3]
c = sys.argv[1]

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
        tem = a + file

        list = []
        with open(c,'r') as f:
            line =f.readline()
            while line:       
                temt = ""
                for i in line :
                    if ( ord(i) >= 97 and ord(i) <= 122 ):
                        temt += i
                list += [temt]
                line=f.readline()
        

        fold_ = open(tem)
        s = fold_.read()

        count = 0
        upper = 0
        punc = 0
        num = 0
        right = 0
        flag = False
        temp = ""
        tf = False
        for i in range(len(s)) :
            d = ord(s[i])
            if (flag):
                if (d >= 97 and d <= 122):
                    temp += s[i]
                elif (d >= 65 and d <= 90):
                    upper += 1
                    temp += chr(d+32)
                elif (d == 39):
                    temp += s[i]
                    punc += 1
                else:
                    flag = False
                    count += 1
                    for w in list:
                        if (w == temp):
                            right += 1
                            break
                    temp = ""
                    if (s[i] == ' '):
                        continue
                    elif (d >= 48 and d <= 57):
                        num += 1
                    elif (i == '.'):
                        punc += 1
                        if (s[i+1] == '.' and s[i+2] == '.'):
                            s[i+1] = ' '
                            s[i+2] = ' '
                    else:
                        punc += 1
            else:
                if (d >= 97 and d <= 122):
                    flag =True
                    temp += s[i]
                elif (d >= 65 and d <= 90):
                    Flag = True
                    upper += 1
                    temp += chr(d+32)
                else:
                    if (s[i] == ' '):
                        continue
                    elif (d >= 48 and d <= 57):
                        num += 1
                    elif (i == '.'):
                        punc += 1
                        if (s[i+1] == '.' and s[i+2] == '.'):
                            s[i+1] = ' '
                            s[i+2] = ' '
                    else:
                        punc += 1

        bt += os.path.splitext(file)[0] + '_k25612yz.txt'
        wp=open(bt,'w')
        wp.write("k25612yz"+'\n')
        wp.write("Formatting ###################"+'\n')
        wp.write("Number of upper case letters changed: "+str(upper)+'\n')
        wp.write("Number of punctuations removed: "+str(punc)+'\n')
        wp.write("Number of numbers removed: "+str(num)+'\n')
        wp.write("Spellchecking ###################"+'\n')
        wp.write("Number of words: "+str(count)+'\n')
        wp.write("Number of correct words: "+str(right)+'\n')
        wp.write("Number of incorrect words: "+str(count-right)+'\n')
        wp.close()




