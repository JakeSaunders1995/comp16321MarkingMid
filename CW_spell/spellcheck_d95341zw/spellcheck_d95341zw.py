import os,argparse,re


def countUpper():
    count=0
    for i in txt:

        if i.isupper():
            count +=1
    return count

def number():
    count1=0
    for i in txt:
        if i.isdigit():
            count1 += 1
    return count1

def punctuation():
    count2 = 0
    for i in txt:
        if i in("?", ".", ";", ":", "!", ",", "[", "]", "#", "@", "-", "(", ")", "{", "}","'","...",'"'):
            count2 += 1
    return count2

def correctWords():
    count3=0
    for i in list3:
        if i in wordsList:
            count3 += 1

    return count3
def incorrectWords():
    count4 = 0
    for i in list3:
        if i not in wordsList:
            count4 += 1

    return count4

parser = argparse.ArgumentParser()
parser.add_argument("dir", nargs='+')
#parser.add_argument("bbb")
args = parser.parse_args()
a = os.listdir(args.dir[1])
b=args.dir[0]
for i in range(0, len(a)):
    #b=args.dir[0]
    c=args.dir[1]+"/"+a[i]
    d=args.dir[2]+"/"+a[i]
    e=d.replace(".txt", "_d95341zw.txt")
    txt=open(c, "r")
    txt = txt.read()
    txt=txt.replace("\n", " ")
#uppercase to lowercase
    new_file = txt.lower()
#remove numbers
    new_file1 = ''.join((n for n in new_file if not n.isdigit()))
#remove pun
    new_file2 ="".join(p for p in new_file1 if p not in ("?", ".", ";", ":", "!", ",", "[", "]", "#", "@", "-", "(", ")", "{", "}","'","...",'"'))


    

    list2=list(new_file2.split(" "))
    list3=[x for x in list2 if x]


    result = open(b, "a")
    result.write("\na")
    result.close()
    result = open(b, "r")
    englishWords = result.readline().split()
#EnglishWords.txt -- list
    wordsList = []
    for line in result:
        strippedLine = line.strip()
    #line_list = strippedLine.split()
        wordsList.append(strippedLine)
#print(wordsList)

    #result.close()
  
    #result.close()
    #output=open(e, "w")
    #output.write(username
    username="d95341zw"
    #print(username)
    output9= username
    output1="Formatting ###################"
    output2="Number of upper case letters changed: " + str(countUpper())
    output3="Number of punctuations removed: " + str(punctuation())
    output4="Number of numbers removed: " + str(number())
    output5="Spellchecking ###################"
    output6="Number of words: "+ str(len(list3))
    output7="Number of correct words: " + str(correctWords())
#incorrectWords= len(list3) - correctWords()
    output8="Number of incorrect words: " + str(incorrectWords())
    output = open(e, "w")
    output.write(output9 + "\n" + output1 + "\n" + output2+ "\n" +output3+ "\n" +output4+ "\n" +output5+ "\n" +output6+ "\n" +output7+ "\n" +output8)

