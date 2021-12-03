import sys
english_filepath = sys.argv[1]
input_filepath = sys.argv[2]
output_filepath = sys.argv[3]
# if len(sys.argv) != 3:
#    print("Insufficient arguments")
#    sys.exit()
# print("input File path : " + input_filepath)
# print("ouput File path : " + output_filepath)


f = open(input_filepath,'r',encoding='utf-8')
f2 = open(output_filepath,'w',encoding='utf-8')
f3 = open(english_filepath,'r',encoding='utf-8')

ifc = f.read()

Ucnt =0
Pcnt =0
Rcnt =0
nofw =0
nofc =0
nofinc =0
allstr = []
allstr2 = []

wd = f3.read()
wordlist = []
wordlist = wd.split("\n")

for i in range(len(ifc)):
    if(ifc[i] == "." or ifc[i] == '?' or ifc[i] == '!' or ifc[i] == "," or ifc[i] ==':' or ifc[i]==';' or ifc[i] == '-' or ifc[i] == '[' or ifc[i] == ']' or ifc[i] == '{' or ifc[i] == '}' or ifc[i] == "'" or ifc[i] == '"' or ifc[i] == '...' or  ifc[i] == '—' or ifc[i] == '(' or ifc[i] == ')'):
        Pcnt=Pcnt+1
        allstr2.append('')
        continue
    if(ifc[i] == '1' or ifc[i] == '2' or ifc[i] == '3' or ifc[i] == '4' or ifc[i] == '8' or ifc[i] == '7' or ifc[i] == '6' or ifc[i] == '5' or ifc[i] == '9' or ifc[i] == '0'):
        Rcnt=Rcnt+1
        allstr2.append('')
        continue
    if(ifc[i].isupper()):
        Ucnt=Ucnt+1
        allstr2.append(ifc[i].lower())
        continue
    else:
        allstr2.append(ifc[i])

allstr2_str = ''.join(allstr2)
alist = []
alist = allstr2_str.split(" ")
axel = []
for i in range(len(alist)):
    strim = alist[i].strip()
    if ' ' not in strim and strim != '':
        nofw = nofw+1
        axel.append(strim)
        


i= 0
for i in wordlist:
    for j in range(len(axel)):
        if i == axel[j]:
            nofc = nofc + 1
            j = j+1
    
nofinc = nofw - nofc



f2.write('s42704jp\n')
f2.write("Formatting ###################\n")
f2.write(f'Number of upper case words changed: {Ucnt}\n')
f2.write(f'Number of punctuations removed: {Pcnt}\n')
f2.write(f'Number of numbers removed: {Rcnt}\n')
f2.write(f'Spellchecking ###################\n')
f2.write(f'Number of words: {nofw}\n')
f2.write(f'Number of correct words: {nofc}\n')
f2.write(f'Number of incorrect words: {nofinc}\n')
