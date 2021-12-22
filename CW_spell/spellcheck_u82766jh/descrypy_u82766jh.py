import os,argparse,re
argv = argparse.ArgumentParser()
argv.add_argument("a")
argv.add_argument("b")
argv_list = argv.parse_args()
file1 = open(argv_list.a,'r')
content = file1.read()
check = 0
if content[0] == "H" :
    check = 1
elif content[0] == "C":
    check = 2
elif content[0] == "M" :
    check = 3
index = content.find(':')+1
content = content[index:]
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
codes = """.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-..
-- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..
.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"""
DD = dict(zip(codes.split(),chars.lower()))
i = 0
def morse2chars(morse):
    return DD.get(morse,' ')
if check == 1 :
    result = content.split()
    file2 = open(argv_list.b,'w')
    for i in range(0,len(result)) :
        result[i] = int(result[i],16)
        result[i] = chr(result[i])
        s = (re.sub(r"['{},]*",'',str(result[i]))).replace(':',',')
        file2.write(s)
    file2.close
if check == 2 : 
    flag = 0
    file2 = open(argv_list.b,'w')
    for i in range(0,len(content)) :
        num = ord(content[i])
        if num == 32 :
            s = (re.sub(r"['{},]*",'',str(chr(num)))).replace(':',',')
            file2.write(s)
            continue
        num = num - 3
        if num <= 96 :
            flag = 96 - num
            num = 120 - flag
        s = (re.sub(r"['{},]*",'',str(chr(num)))).replace(':',',')
        file2.write(s)
    file2.close
elif check == 3 : 
    result = content.split()
    file2 = open(argv_list.b,'w')
    for i in range(0,len(result)) :
        if re.match('/',result[i]):
            file2.write(str(' '))
            continue
        else : ans = ''.join(morse2chars(result[i]))
        s = (re.sub(r"['{},]*",'',str(ans))).replace(':',',')
        file2.write(s)
    file2.close

