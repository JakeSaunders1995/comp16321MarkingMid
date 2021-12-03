import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('inputpath', type=str)
parser.add_argument('outputpath', type=str)
args = parser.parse_args()

InputPath = args.inputpath
OutputPath = args.outputpath
path_1=InputPath
path_2=OutputPath
# end

li=[]
with open(path_1, encoding='utf-8') as file_1:
    li= file_1.readlines()

with open('EnglishWords.txt', encoding='utf-8') as file_1:
    English = file_1.readlines()
englishword=[]
for i in English:
    if i[-1]=='\n':
        englishword.append(i[:-1])
    else:
        englishword.append(i)


dan=0
daxie=0
zdan=0
cdan=0
fu=0
shu=0
for i in range(len(li)):
    st = ''
    for j in li[i]:

        if 'a'<=j<='z' or j==' ' or 'A'<=j<='Z':
            if 'A'<=j<='Z':
                daxie+=1
                st+=j.lower()
            else:
                st += j
        elif '0'<=j<='9':
            shu+=1
        else:
            fu+=1

    xiao=st.split(' ')
    st=''
    for ii in xiao:
        if ii!='':
            st+=ii+' '
    st=st[:-1]
    li[i]=st
    dan+=len(st.split(' '))

for i in range(len(li)):
    lii=li[i].split(' ')
    for j in lii:
        if j in englishword:
            zdan+=1
        else:
            cdan+=1

xie=[]
xie.append('[user_name]\n')
xie.append('Formatting ###################\n')
xie.append('Number of upper case words changed: ' +str(daxie)+'\n')
xie.append('Number of punctuations removed: '+str(fu)+'\n')
xie.append('Number of numbers removed: '+str(shu)+'\n')
xie.append('Spellchecking ###################\n')
xie.append('Number of words: '+str(dan)+'\n')
xie.append('Number of correct words: '+str(zdan)+'\n')
xie.append('Number of incorrect words: '+str(cdan)+'\n')
print(xie)

f = open(path_2, 'w', encoding='utf-8')
for i in xie:
     f.write(i)
f.close()


